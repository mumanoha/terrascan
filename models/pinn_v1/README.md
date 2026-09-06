# TerraScan v1 Model Specification & Frozen Baseline

_Frozen: 2026-09-05 · Source: PJAS Presentation 2026 (`context/V2 - TerraScan - PJAS Presentation - 2026.pptx.pdf`)_

## Overview
TerraScan v1 was developed as a 9th-grade Pennsylvania Junior Academy of Science (PJAS) project. It proposed predicting topsoil Nitrogen (N), Phosphorus (P), and Potassium (K) from Sentinel-2 MultiSpectral Instrument (MSI) reflectance data using a "Physics-Informed Neural Network" (PINN).

## Model Architecture
- **Framework**: PyTorch (`nn.Module`)
- **Layers**: 4-Layer Multi-Layer Perceptron (MLP)
  - Layer 1: Linear(12 -> 128), LeakyReLU(negative_slope=0.1), BatchNorm1d(128), Dropout(p=0.25)
  - Layer 2: Linear(128 -> 256), LeakyReLU(negative_slope=0.1), BatchNorm1d(256), Dropout(p=0.25)
  - Layer 3: Linear(256 -> 128), LeakyReLU(negative_slope=0.1)
  - Output Head: Linear(128 -> 3)
  - Output Constraint: `nn.Softplus()`
- **"Physics-Informed" Rationale in v1**: The `nn.Softplus()` activation function was applied to the final layer to guarantee that predicted chemical concentrations remain strictly non-negative ($C \ge 0$), representing a physical mass positivity constraint.

## Training Configuration
- **Dataset**: LUCAS-SOIL 2018 ($N = 628$ validated sample points)
- **Filtering**: 99th percentile quantile filtration, null-value remediation
- **Features**: 12 Sentinel-2 MSI spectral bands (B1 to B12) at 20 m spatial resolution
- **Feature Scaling**: `sklearn.preprocessing.StandardScaler` (zero mean, unit variance)
- **Data Splitting**: 80/20 randomized train/test split (unstratified, non-spatial)
- **Optimizer**: `torch.optim.AdamW(lr=LEARNING_RATE, weight_decay=1e-4)`
- **Learning Rate Scheduler**: `ReduceLROnPlateau(factor=0.5, patience=50, mode='min')`
- **Training Epochs**: 1000
- **Loss Function**: Mean Absolute Error (MAE / L1 Loss)

## Reported Performance Metrics
### Training Convergence
- Start Training MAE: 71.81 mg/kg
- Final Training MAE: 24.07 mg/kg

### Test Set Performance (Satellite-Only)
| Target Nutrient | Test MAE (mg/kg) | Observed Ground Truth Range (mg/kg) | Relative Error Behavior |
| :--- | :--- | :--- | :--- |
| **Nitrogen (N)** | **1.63** | ~0.0 – 20.0 | Severe clustering at ~2.5 mg/kg; fails on high values |
| **Phosphorus (P)** | **16.31** (or 16.88) | ~0 – 100 | Severe dispersion; low correlation; clusters at 20–30 mg/kg |
| **Potassium (K)** | **142.40** (or 135.95)| ~0 – 800 | Massive regression to the mean (~150–200 mg/kg); fails high range |

### Simulated Robot Augmented Results (Slide 23)
- Nitrogen MAE: 0.22 mg/kg
- Phosphorus MAE: 1.47 mg/kg
- Potassium MAE: 10.60 mg/kg
- *Note*: Results were derived from synthetic/simulated ground-truth noise perturbation rather than field testing of the AS7265x sensor.

## Preservation Rule
This directory is strictly frozen. No code or configuration in `models/pinn_v1/` should be modified. It serves as the historical baseline against which TerraScan v2 architectures and traditional ML baselines will be rigorously benchmarked.
