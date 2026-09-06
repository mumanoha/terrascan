# Baseline Benchmark Models: Classical ML & Spatial BlockCV
_Last updated: 2026-09-06 · Status: verified_

## TL;DR
TerraScan v2 benchmarks against classical machine learning baselines: Partial Least Squares Regression (PLSR), Ridge Regression, Random Forest, and Histogram-based Gradient Boosting. Critically, these models are evaluated using both standard Random K-Fold and rigorous **Spatial Block Cross-Validation (SpatialBlockKFold)** to detect and quantify spatial autocorrelation data leakage.

## Python Implementation

Source file: [`train_baselines.py`](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/models/baselines/train_baselines.py)

```python
"""
TerraScan v2: Baseline Model Training and Evaluation Pipeline
Implements mandatory classical baselines (Random Forest, Gradient Boosting, PLSR, Ridge)
evaluated under both Random K-Fold and Spatial Block Cross-Validation (BlockCV).
"""

from sklearn.ensemble import RandomForestRegressor, HistGradientBoostingRegressor
from sklearn.cross_decomposition import PLSRegression
from sklearn.linear_model import Ridge
from sklearn.dummy import DummyRegressor
from sklearn.cluster import KMeans
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
```

### Key Components

1. **SpatialBlockKFold**: Partitions spatial coordinates $(x, y)$ into contiguous geographic clusters using K-Means clustering. This ensures that test samples are geographically independent of training samples, preventing spatial leakage where the model memorizes local coordinates rather than learning spectral relationships.
2. **Standardized Metrics**:
   - $R^2$ (Coefficient of Determination)
   - $\text{RMSE}$ (Root Mean Squared Error)
   - $\text{MAE}$ (Mean Absolute Error)
   - $\text{NRMSE}\%$ (Normalized RMSE)
   - $\text{RPIQ}$ (Ratio of Performance to Interquartile Range)
3. **Dummy Mean Predictor**: Establishes the baseline error when predicting the population mean $\bar{y}$, proving whether an apparent low MAE is merely an artifact of right-skewed data.
