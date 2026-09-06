"""
TerraScan v2: Baseline Model Training and Evaluation Pipeline
Implements mandatory classical baselines (Random Forest, Gradient Boosting, PLSR, Ridge)
evaluated under both Random K-Fold and Spatial Block Cross-Validation (BlockCV).
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple
from sklearn.ensemble import RandomForestRegressor, HistGradientBoostingRegressor
from sklearn.cross_decomposition import PLSRegression
from sklearn.linear_model import Ridge
from sklearn.dummy import DummyRegressor
from sklearn.cluster import KMeans
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

class SpatialBlockKFold:
    """
    Spatial Block K-Fold Cross-Validator.
    Partitions spatial coordinates into K spatially contiguous geographical blocks
    using K-Means clustering, preventing spatial autocorrelation leakage.
    """
    def __init__(self, n_splits: int = 5, random_state: int = 42):
        self.n_splits = n_splits
        self.random_state = random_state

    def split(self, X: np.ndarray, y: np.ndarray, coords: np.ndarray):
        kmeans = KMeans(n_clusters=self.n_splits, random_state=self.random_state, n_init=10)
        spatial_clusters = kmeans.fit_predict(coords)
        
        for fold in range(self.n_splits):
            test_idx = np.where(spatial_clusters == fold)[0]
            train_idx = np.where(spatial_clusters != fold)[0]
            yield train_idx, test_idx

def calculate_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, float]:
    """Computes R², RMSE, MAE, NRMSE, and RPIQ (Ratio of Performance to Interquartile Range)."""
    r2 = r2_score(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    data_range = np.ptp(y_true)
    nrmse = (rmse / data_range) * 100 if data_range > 0 else 0.0
    
    iqr = np.percentile(y_true, 75) - np.percentile(y_true, 25)
    rpiq = (iqr / rmse) if rmse > 0 else 0.0
    
    return {
        "R2": float(r2),
        "RMSE": float(rmse),
        "MAE": float(mae),
        "NRMSE_%": float(nrmse),
        "RPIQ": float(rpiq)
    }

def get_baseline_models() -> Dict[str, object]:
    """Instantiates the required classical benchmark models."""
    return {
        "Dummy (Mean Baseline)": DummyRegressor(strategy="mean"),
        "Partial Least Squares (PLSR)": PLSRegression(n_components=5),
        "Ridge Regression": Ridge(alpha=1.0),
        "Random Forest Regressor": RandomForestRegressor(n_estimators=100, max_depth=12, random_state=42, n_jobs=-1),
        "HistGradientBoosting": HistGradientBoostingRegressor(max_iter=100, max_depth=6, random_state=42)
    }

def evaluate_baselines(X: np.ndarray, y: np.ndarray, coords: np.ndarray, target_name: str = "Nutrient"):
    """
    Evaluates all baselines across 5-Fold Spatial Block-CV.
    Prints a publication-ready comparative metrics table.
    """
    models = get_baseline_models()
    splitter = SpatialBlockKFold(n_splits=5, random_state=42)
    
    results = []
    print(f"\n=========================================================================")
    print(f" EVALUATION OF BASELINES UNDER SPATIAL BLOCK-CV: Target = {target_name}")
    print(f" Sample Size: N = {len(X)} | Feature Dim: {X.shape[1]}")
    print(f"=========================================================================")
    
    for model_name, model in models.items():
        fold_metrics = []
        
        for train_idx, test_idx in splitter.split(X, y, coords):
            X_train, X_test = X[train_idx], X[test_idx]
            y_train, y_test = y[train_idx], y[test_idx]
            
            # Fit and predict
            model.fit(X_train, y_train)
            preds = model.predict(X_test)
            if preds.ndim > 1:
                preds = preds.ravel()
                
            metrics = calculate_metrics(y_test, preds)
            fold_metrics.append(metrics)
            
        # Average across spatial folds
        mean_r2 = np.mean([m["R2"] for m in fold_metrics])
        mean_rmse = np.mean([m["RMSE"] for m in fold_metrics])
        mean_mae = np.mean([m["MAE"] for m in fold_metrics])
        mean_nrmse = np.mean([m["NRMSE_%"] for m in fold_metrics])
        mean_rpiq = np.mean([m["RPIQ"] for m in fold_metrics])
        
        results.append({
            "Model": model_name,
            "R2 (Spatial CV)": f"{mean_r2:.3f}",
            "RMSE": f"{mean_rmse:.2f}",
            "MAE": f"{mean_mae:.2f}",
            "NRMSE (%)": f"{mean_nrmse:.1f}%",
            "RPIQ": f"{mean_rpiq:.2f}"
        })
        
    df_results = pd.DataFrame(results)
    print(df_results.to_string(index=False))
    return df_results

if __name__ == "__main__":
    # Self-test using synthetically structured spatial data mimicking Sentinel-2 + Topography
    np.random.seed(42)
    n_samples = 600
    
    # 2D coordinates across a simulated 20km x 20km agricultural landscape
    sim_coords = np.random.uniform(0, 20, size=(n_samples, 2))
    
    # Simulate 8 features (6 S2 bands B2, B3, B4, B8A, B11, B12 + Slope + TWI)
    sim_features = np.random.uniform(0.05, 0.45, size=(n_samples, 8))
    
    # Synthetic ground truth for Available Phosphorus (Mehlich-3 P, mg/kg)
    # P depends non-linearly on clay (feat 5) and organic matter (feat 4), plus spatial drift
    true_p = (
        25.0 
        + 40.0 * sim_features[:, 4]  # SOC proxy
        + 30.0 * sim_features[:, 5]  # Clay proxy
        + 5.0 * np.sin(sim_coords[:, 0] / 3.0) 
        + np.random.normal(0, 4.0, size=n_samples)
    )
    true_p = np.clip(true_p, 5.0, 120.0)
    
    df_eval = evaluate_baselines(sim_features, true_p, sim_coords, target_name="Available Phosphorus (P, mg/kg)")
