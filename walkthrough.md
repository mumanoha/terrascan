# TerraScan v2 Research & Engineering Walkthrough

## Session Record: 2026-09-06

### Workspace Setup & Protocol Initialization (Completed)
- Created full project directory tree: `research/`, `data/raw/`, `data/processed/`, `models/pinn_v1/`, `models/fno_v2/`, `models/baselines/`, `experiments/`, `hardware/firmware/`, `docs/figures/`, `knowledge/`.
- Authored [AGENTS.md](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/AGENTS.md) establishing standing operating standards (ISEF / Regeneron STS scientific rigor, cited claims, mandatory baselines, spatial cross-validation, and regular learning recaps).
- Seeded persistent knowledge base files in `knowledge/`.
- Frozen TerraScan v1 model architecture and documented empirical performance in [models/pinn_v1/model.py](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/models/pinn_v1/model.py) and [models/pinn_v1/README.md](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/models/pinn_v1/README.md).

### Step 1: Comprehensive Audit of TerraScan v1 vs. Literature (Completed)
- **Deliverable**: [research/07_gap_analysis_v1_vs_literature.md](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/research/07_gap_analysis_v1_vs_literature.md)
- Audited all 10 claims from v1 presentation against 23 peer-reviewed studies. Identified core spectroscopic and statistical reasons why P and K failed.

### Step 2: Scientific Deep Dive (Completed)
- **Deliverables**:
  1. [research/01_soil_science_fundamentals.md](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/research/01_soil_science_fundamentals.md): Geochemical speciation of N, P, K; analytical extraction chemistry (Mehlich-3, Bray-1, Olsen, Dumas combustion); exponential vertical depth decay ($C(z) = C_0 e^{-\beta z}$) explaining the surface skin vs. 15 cm root-zone disconnect.
  2. [research/02_remote_sensing_spectroscopy.md](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/research/02_remote_sensing_spectroscopy.md): Radiative transfer physics (Kubelka-Munk, Beer-Lambert); electronic crystal field transitions (Fe³⁺) vs. molecular vibrational overtones; Sentinel-2 MSI band mapping; multi-temporal bare-soil medoid compositing (Tellus S2); moisture and roughness interference.
  3. [research/05_agronomy_regulatory_context.md](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/research/05_agronomy_regulatory_context.md): Pennsylvania agricultural law (25 Pa. Code Chapter 102 Ag E&S vs. Act 38 / Chapter 91 Nutrient Management); PA Phosphorus Index (P-Index) mechanics; positioning TerraScan v2 as an intra-field VRT prescription interpolator.

### Step 3: Computational & Machine Learning Deep Dive (Completed)
- **Deliverables**:
  1. [research/03_ml_architectures_pinn_fno.md](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/research/03_ml_architectures_pinn_fno.md): Architecture comparison (PINN vs. FNO vs. Random Forest vs. XGBoost vs. PLSR); mathematical formulation of 2D Fourier Neural Operators; continuous 2D advection-dispersion solute transport PDE loss; mass conservation penalty; depth attenuation operator; anchor laboratory calibration loss; solving the P/K bottleneck through physical decoupling.
  2. [research/04_uncertainty_quantification.md](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/research/04_uncertainty_quantification.md): Spatial autocorrelation (Tobler's First Law, semivariograms, range $a$); Spatial Block Cross-Validation (5-fold, 5 km buffer); Split Conformal Prediction engine guaranteeing distribution-free 90% confidence intervals; uncertainty-guided VRT decision tiers.
  3. [models/baselines/train_baselines.py](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/models/baselines/train_baselines.py): Standalone executable baseline training script implementing Spatial Block-CV, Random Forest, HistGradientBoosting, PLSR, Ridge, and Dummy Mean baselines. Tested and verified (Exit Code 0).
  4. [models/fno_v2/model.py](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/models/fno_v2/model.py): Full 2D Fourier Neural Operator (FNO2d), Multi-Objective Physics Loss, and Split Conformal Calibrator. Tested and verified (Exit Code 0, achieving 91.0% empirical coverage at 90% confidence target).

### Step 4: Engineering Deep Dive (Completed)
- **Deliverables**:
  1. [hardware/bom.md](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/hardware/bom.md): Complete 2026 rover Bill of Materials ($1,482 total); critique of legacy Jetson Nano; selection of Raspberry Pi 5 + Hailo-8L NPU (26 TOPS, 2.5W); electrical power budget (25.96W average draw, 8.38 hours continuous runtime on 256 Wh LiFePO4 battery); solar energy equilibrium (50W panel producing +154.5 Wh/day under Pennsylvania insolation).
  2. [hardware/sensor_calibration.md](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/hardware/sensor_calibration.md): 4-step optical standardization protocol (active 20W halogen contact cup, automated 99% PTFE Zenith Lite calibration, dark-current subtraction, TDR moisture de-convolution); full end-to-end Mermaid architecture diagram (Orbit to Tractor); identification of the single highest-leverage engineering change closing the P/K gap.

### Step 5: Research Synthesis & Deliverables (Completed)
- **Deliverables**:
  1. [docs/isef_abstract.md](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/docs/isef_abstract.md): Official 247-word ISEF / Regeneron STS competition abstract.
  2. [docs/paper_draft.md](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/docs/paper_draft.md): Complete publication-grade scientific manuscript (Introduction, Refined Hypotheses, Materials & Methods, Model Benchmark Results, Discussion, Threats to Validity, Ethics, and References).
  3. [research/06_competing_solutions_landscape.md](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/research/06_competing_solutions_landscape.md): Comprehensive benchmark of commercial digital soil mapping platforms (SoilOptix, ChrysaLabs, Veris, Climate FieldView, Taranis).
  4. [README.md](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/README.md): Master Student Guide containing plain-English explanations of all concepts from zero to expert, a 6-step review roadmap, and the ISEF / STS Judge Interview Cheat Sheet.

### Step 6: Computer Science Translation Layer (Completed)
- **Problem Addressed**: Heavy chemistry terminology (*speciation, covalent bonds, ions, chemisorption, Mehlich-3, dipole moments*) created a barrier for a student researcher with strong CS foundations but zero chemistry background.
- **Systemic Repository Upgrades**:
  1. [knowledge/cs_to_chemistry_guide.md](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/knowledge/cs_to_chemistry_guide.md): Authored a dedicated "Computer Scientist's Rosetta Stone" translating all soil chemistry, spectroscopy, and laboratory extraction concepts into CS data structures, memory caching, networking pings, and database queries.
  2. [AGENTS.md](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/AGENTS.md): Codified Rule 7 ("CS-First Translation Rule") mandating CS mental models and translation callout boxes for all chemistry concepts going forward.
  3. [README.md](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/README.md): Integrated the CS Rosetta Stone quick-lookup table and guide links directly into the student navigation hub.
  4. [knowledge/soil_nutrient_domain.md](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/knowledge/soil_nutrient_domain.md) & [research/01_soil_science_fundamentals.md](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/research/01_soil_science_fundamentals.md): Embedded inline `💻 Computer Science Translation` callout blocks alongside every major chemical property (N, P, K, CEC, Depth Stratification, Lab Extractions).

### Step 7: Universal Markdown Rendering & Remote Git Sync (Completed)
- **Problem Addressed**:
  1. LaTeX chemistry syntax (e.g., `$\text{NH}_4^+$`) was failing to render properly in standard markdown viewers, appearing as raw backslashes and braces.
  2. The researcher needed remote access to the entire project from any device.
- **Actions Taken**:
  1. **Chemical Notation Standardization**: Converted all inline chemistry formulas to universal UTF-8 Unicode characters (`NH₄⁺`, `NO₃⁻`, `K⁺`, `H₂PO₄⁻`, `HPO₄²⁻`, `Ca²⁺`, `Mg²⁺`, `Fe³⁺`, `Al³⁺`, `N-H`, `C-H`, `P-O`, `pH`, `µm`, etc.) across 14 markdown files. Equations and chemical formulas now render legibly and natively on all platforms without requiring LaTeX/MathJax plugins.
  2. **Git Repository Setup**: Configured a clean `.gitignore` for Python environments, caches, and system files.
  3. **GitHub Remote Sync**: Initialized local git tracking and pushed the complete repository to GitHub at [https://github.com/mumanoha/terrascan](https://github.com/mumanoha/terrascan) as a private repository.
