# Modeling Decisions Log
_Last updated: 2026-09-06 · Status: Active Persistent Memory_

## Purpose
This log documents every architectural, data engineering, feature selection, loss formulation, and validation protocol decision made for TerraScan v2. Each entry includes timestamped rationale, alternatives considered, empirical results, and failure modes. Entries are preserved historically and corrected in place when assumptions are superseded.

---

## Chronological Decision Entries

### Entry MD-001: Audit of v1 Architecture and Rejection of Softplus-Only "PINN" Formulation
- **Date**: 2026-09-05
- **Author**: TerraScan Research Agent
- **Context**: TerraScan v1 relied on a 4-layer MLP (`Linear -> LeakyReLU -> BatchNorm -> Dropout`) with a terminal `nn.Softplus()` layer, claiming it informed the AI about the laws of physics by preventing negative mass.
- **Decision**: Reject the claim that `nn.Softplus()` constitutes a Physics-Informed Neural Network (PINN). Formulate true physics-guided learning for v2 based on continuous spatial differential constraints (mass conservation, advection-dispersion, and vertical depth-decay profiles).
- **Alternatives Considered**:
  1. *Retain Softplus as the primary physics claim*: Rejected because it lacks scientific credibility for ISEF/STS review; non-negative activations are standard bounding techniques, not physical law embeddings.
  2. *Standard unconstrained Deep Learning (ResNet/MLP)*: Rejected because purely empirical models overfit spurious regional correlations between satellite spectral bands and indirect soil nutrients (P and K).
  3. *Physics-Guided Neural Operators (FNO/PINN)*: Selected. FNO captures spatial continuous field operators across multi-resolution grids, and physics loss terms enforce genuine physical mass and transport constraints.

### Entry MD-002: Elimination of Random Cross-Validation in Geospatial Soil Modeling
- **Date**: 2026-09-05
- **Author**: TerraScan Research Agent
- **Context**: TerraScan v1 used an 80/20 random train/test split on 628 LUCAS samples. In geospatial domains, random splitting induces severe spatial autocorrelation leakage (Tobler's First Law), creating unrealistically optimistic error metrics.
- **Decision**: Mandate Spatial Block Cross-Validation (Spatial Block-CV) with a minimum geographic exclusion buffer (5 km) between training and evaluation folds.
- **Alternatives Considered**:
  1. *Standard K-fold CV*: Rejected due to severe spatial leakage.
  2. *Leave-One-Field-Out (LOFO) CV*: Acceptable for single-farm datasets, but insufficient for multi-regional/continental benchmarks like LUCAS.
  3. *Spatial Block-CV with Buffering*: Selected. Provides an unbiased estimate of model transferability to unseen geographic regions.

### Entry MD-003: Abandonment of Uniform "< 5 mg/kg" Metric
- **Date**: 2026-09-05
- **Author**: TerraScan Research Agent
- **Context**: v1 proposed a uniform threshold of $< 5\text{ mg/kg}$ MAE across N, P, and K.
- **Decision**: Supersede this metric with property-specific, statistically normalized metrics: $R^2$, Root Mean Square Error (RMSE), Normalized RMSE (NRMSE = RMSE / range), and Ratio of Performance to Interquartile Range (RPIQ).
- **Rationale**: An error of 5 mg/kg represents >50% error for available N, ~20% error for available P, but <1.5% error for exchangeable K. Uniform error thresholds fail basic stoichiometric and agronomic sanity checks.

### Entry MD-004: Anchor-Calibrated Spatial Field Interpolation Framework
- **Date**: 2026-09-06
- **Author**: TerraScan Research Agent
- **Context**: Regulatory audit confirms Pennsylvania law (Act 38 / Chapter 91) rejects satellite nutrient predictions as legal substitutes for mandatory 3-year wet chemistry lab testing. However, farmers suffer from severe intra-field spatial variability across 10-to-20 acre composite zones.
- **Decision**: Position TerraScan v2 not as a zero-shot replacement for lab testing, but as an **anchor-calibrated spatial field interpolator**. The model ingests the farmer's certified 3-year lab test as an anchor ground-truth constraint ($C_{\text{lab}}$), using satellite bare-soil reflectance, terrain covariates, and in-situ rover sampling to produce 10m Variable Rate Technology (VRT) prescription maps.

### Entry MD-005: Multi-Temporal Medoid Bare-Soil Compositing Protocol
- **Date**: 2026-09-06
- **Author**: TerraScan Research Agent
- **Context**: Single-date satellite images are contaminated by clouds, varying soil moisture, crop residues, and seasonal vegetation cover. In Pennsylvania croplands, bare soil occurs for only 2 to 4 weeks annually.
- **Decision**: Adopt a multi-year (2021–2024) Sentinel-2 L2A bare-soil compositing protocol in Google Earth Engine using dual filtering ($\text{NDVI} < 0.25$ and $\text{NBR2} < 0.15$) and multi-dimensional medoid aggregation (SYSI / Tellus S2 framework).

### Entry MD-006: Satellite Feature Band Selection and Pruning
- **Date**: 2026-09-06
- **Author**: TerraScan Research Agent
- **Context**: TerraScan v1 fed all 12 Sentinel-2 bands into an MLP indiscriminately.
- **Decision**: Prune atmospheric bands B1 (443 nm, coastal aerosol) and B9 (945 nm, water vapor), which operate at coarse 60m resolution and inject atmospheric noise. Focus core feature extraction on **B2, B3, B4, B8A (20m NIR), B11 (SWIR-1), and B12 (SWIR-2)** alongside calculated ratios ($\text{NDVI}, \text{NBR2}, \text{NDMI}, B11/B12, B4/B3$).

### Entry MD-007: 2D Fourier Neural Operator (FNO) for Spatial Continuous Fields
- **Date**: 2026-09-06
- **Author**: TerraScan Research Agent
- **Context**: Standard CNNs and MLPs are mesh-dependent and lack whole-watershed spatial context.
- **Decision**: Deploy a 4-layer 2D Fourier Neural Operator with 16 Fourier modes and 64 latent channels. FNO parameterizes integral kernels in the frequency domain, enabling continuous spatial field mapping, zero-shot super-resolution, and global receptive fields.

### Entry MD-008: Split Conformal Prediction for Distribution-Free Uncertainty Quantification
- **Date**: 2026-09-06
- **Author**: TerraScan Research Agent
- **Context**: Point predictions do not tell farmers where the model is confident vs. uncertain, and standard Gaussian error bars fail on asymmetric soil data.
- **Decision**: Implement Inductive Split Conformal Prediction, calculating non-conformity scores on held-out spatial blocks to output finite-sample, distribution-free 90% confidence intervals for every 10-meter pixel.

### Entry MD-009: Edge Compute Selection: Raspberry Pi 5 + Hailo-8L NPU
- **Date**: 2026-09-06
- **Author**: TerraScan Research Agent
- **Context**: The NVIDIA Jetson Nano specified in v1 is discontinued (EOL since 2023) and power-inefficient (10–12W).
- **Decision**: Select Raspberry Pi 5 (8GB) paired with the official Raspberry Pi AI Kit (Hailo-8L M.2 NPU). Delivers 26 TOPS of INT8 inference at only 2.5W, enabling real-time edge FNO evaluation in the field at an affordable price ($155 combined).

### Entry MD-010: TerraBot Physical/Mechanical Layout, 4WD Skid-Steer Drivetrain, and Dark-Current Optical Articulation
- **Date**: 2026-09-09
- **Author**: TerraScan Research Agent
- **Context**: Ground-truth calibration requires a field-capable rover that traverses muddy agricultural topsoils, fits between standard 30-inch (76.2 cm) crop rows without root damage, resists rollover on 20° hillsides, and seals an optical chamber against cloddy soil for drift-free reflectance scans.
- **Decision**:
  1. *Chassis & Dimensions*: 520 mm outer width, 400 mm wheelbase, 450 mm track gauge, 110 mm ground clearance. Constructed with 2.5 mm 5052-H32 aluminum tub and 2020 T-slot rails.
  2. *Drivetrain*: 4WD Skid-Steer with 180 mm R-1 chevron rubber tires ($4.4\text{ psi}$ ground pressure, zero soil compaction risk, true $0\text{ cm}$ zero-radius turning). Rejected continuous tracks due to destructive topsoil shearing and sticky clay packing.
  3. *Center of Gravity & Stability*: Slung low-belly battery tray ($Z = 120\text{ mm}$) lowers overall vehicle $Z_{cg}$ to $135.5\text{ mm}$ (gross mass $13.90\text{ kg}$). Static roll threshold is $58.9^{\circ}$ ($2.95\times$ safety factor on 20° PA hillsides).
  4. *Sensor Articulation & Optical Dark Subtraction*: 2-DOF linear lead-screw actuated arm with 110 mm vertical stroke. Cup rimmed with 40 Shore A EPDM accordion skirt ($<0.01\text{ lux}$ ambient leakage) to execute a 4-step dark-current and PTFE 99% white reference subtraction.
  5. *Environmental Sealing*: IP65 sealed compute bay with conductive chassis heat sinking; IP66 battery bay with IP67 Gore hydrophobic membrane pressure equalization vent plug.
- **Deliverable**: [docs/figures/02a_robot_cad_concept.md](docs/figures/02a_robot_cad_concept.md).
