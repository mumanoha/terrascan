# TerraScan v2 Research & Engineering Task Board

## Project Objectives
Elevate TerraScan from a Grade 9 PJAS science fair presentation to an ISEF / Regeneron Science Talent Search (STS) research program in computational agronomy and physics-guided machine learning for precision soil nutrient estimation.

## Roadmap & Status
- [x] **Part 1 & 2: Infrastructure & Agent Rules**
  - [x] Create standardized project directory structure
  - [x] Initialize `AGENTS.md` with ISEF/STS research standards
  - [x] Initialize persistent knowledge base in `knowledge/`
  - [x] Freeze v1 model architecture and metrics in `models/pinn_v1/`
  - [x] Initialize `data/README.md`, `task.md`, `implementation_plan.md`, `walkthrough.md`
- [x] **Part 4, Step 1: Comprehensive Audit of TerraScan v1**
  - [x] Audit every factual, numerical, and architectural claim from the v1 deck
  - [x] Interrogate the "< 5 mg/kg error" hypothesis against peer-reviewed Sentinel-2 soil spectroscopy benchmarks
  - [x] Unpack physical & spectral mechanisms explaining why P and K severely underperformed N
  - [x] Classify all claims: Confirmed / Partially Supported / Contradicted / Untested
  - [x] Publish `research/07_gap_analysis_v1_vs_literature.md`
  - [x] Update `knowledge/` base and provide Step 1 Learning Recap
- [x] **Part 4, Step 2: Scientific Deep Dive**
  - [x] Soil Chemistry & Extraction Dynamics (`research/01_soil_science_fundamentals.md`)
  - [x] Radiative Transfer & Remote Sensing Spectroscopy (`research/02_remote_sensing_spectroscopy.md`)
  - [x] Agronomic & Regulatory Grounding in PA DEP / USDA (`research/05_agronomy_regulatory_context.md`)
  - [x] Update `knowledge/` base and provide Step 2 Learning Recap
- [x] **Part 4, Step 3: Computational & ML Deep Dive**
  - [x] Architecture comparison: PINN vs. FNO vs. Baselines (`research/03_ml_architectures_pinn_fno.md`)
  - [x] Rigorous Physics-Informed Formulation & Governing Partial Differential Equations
  - [x] Calibrated Uncertainty Quantification via Split Conformal Prediction (`research/04_uncertainty_quantification.md`)
  - [x] Spatial Block Cross-Validation Evaluation Protocol (5-fold, 5 km buffer)
  - [x] Implement executable baseline script (`models/baselines/train_baselines.py`)
  - [x] Implement executable 2D FNO, Physics Loss & Conformal Calibrator (`models/fno_v2/model.py`)
- [x] **Part 4, Step 4: Hardware & Sensor Engineering Deep Dive**
  - [x] Sensor & Robot Bill of Materials (BOM) & Power Budget Audit (`hardware/bom.md`)
  - [x] In-situ AS7265x Multi-Spectral Sensor Calibration & Drift Protocol (`hardware/sensor_calibration.md`)
  - [x] End-to-End Multimodal Data Fusion Pipeline Architecture (Mermaid diagram)
  - [x] Identify single highest-leverage engineering change closing P/K gap
- [x] **Part 4, Step 5: Research Synthesis & Competition Deliverables**
  - [x] ISEF Competition Abstract (`docs/isef_abstract.md`)
  - [x] Full Structured Research Paper Draft (`docs/paper_draft.md`)
  - [x] Comprehensive Threats to Validity & Limitations Analysis
  - [x] Commercial Competitors Benchmark (`research/06_competing_solutions_landscape.md`)
  - [x] Master Student Guide, Plain-English Glossary & Judge Cheat Sheet (`README.md`)
- [x] **Part 4, Step 6: Computer Science Translation Layer**
  - [x] Master CS Rosetta Stone (`knowledge/cs_to_chemistry_guide.md`)
  - [x] CS-First Translation Rule in `AGENTS.md` (Rule 7)
  - [x] Quick-Lookup Rosetta Stone in `README.md`
  - [x] Inline CS translation callout blocks in `knowledge/soil_nutrient_domain.md` and `research/01_soil_science_fundamentals.md`
- [x] **Part 4, Step 7: Universal Markdown Rendering & Remote Git Sync**
  - [x] Standardized chemical rendering across all 14 markdown files using clean, universal Unicode (NH₄⁺, NO₃⁻, K⁺, H₂PO₄⁻, etc.)
  - [x] Initialized Git repository, added `.gitignore`, and synced to GitHub (`https://github.com/mumanoha/terrascan`)
