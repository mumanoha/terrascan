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
- **Deliverable**: [docs/figures/02a_robot_cad_concept.md](/docs/figures/02a_robot_cad_concept.md).

### Entry MD-011: TerraBot Electrical Architecture, Multi-Rail Regulation, and Photodiode Star-Ground Isolation
- **Date**: 2026-09-09
- **Author**: TerraScan Research Agent
- **Context**: The v1 project assumed all components wired directly to a common battery rail without regulation, fusing, level-shifting, or reverse-polarity protection. Concurrently, high-current (10–15A) motor switching generates severe ground bounce and EMI capable of destroying 3.3V silicon and corrupting nano-amp photodiode readouts on the AS7265x spectrometer.
- **Decision**:
  1. *Power Regulation*: Multi-stage synchronous buck converters (12.8V -> 5.1V 5A for Pi 5 + NPU; 12.8V -> 5.0V 3A for GPS/servos) and a dedicated ultra-low-noise LDO (TI LP5907, $<6.5\mu\text{V}_{\text{RMS}}$ noise, PSRR $>82\text{ dB}$) isolated strictly for the AS7265x sensor.
  2. *Safety & Protection*: 15A master ATC fuse, 20A SPST master E-Stop switch, and an ideal diode circuit utilizing an IRF4905 P-Channel MOSFET with 12V Zener gate clamp (yielding $<0.04\text{V}$ drop vs. $0.6\text{V}$ diode loss). TVS bidirectional suppressors across 12V and solar buses; 1N5819 Schottky flyback diodes across inductive lamp and actuator relays.
  3. *Noise & Ground Loop Mitigation*: Star-ground topology anchored at the negative battery terminal bolt. Complete physical separation between dirty motor/actuator return (`GND_PWR`) and clean logic/sensor return (`GND_LOGIC`). Control signals to the motor driver are optoisolated via 6N137 high-speed optocouplers. The 20W halogen lamp features an LC low-pass inrush filter ($10\mu\text{H} + 220\mu\text{F}$) to prevent brownouts.
  4. *Serial Bus Integrity*: Differential RS-485 with SP3485 transceiver and SM712 TVS diodes for the 0–15 cm TDR soil moisture probe; hardware $4.7\text{ k}\Omega$ metal-film pull-up resistors for Fast Mode I2C.
  5. *Power Derivation*: Demonstrated $8.21\text{ hours}$ continuous field runtime on 256 Wh LiFePO4 battery ($25.96\text{ W}$ average draw) and $+50.7\text{ Wh/day}$ net-positive solar equilibrium under PA insolation.
- **Deliverables**: [docs/figures/02b_robot_wiring.md](/docs/figures/02b_robot_wiring.md) and [docs/figures/02b_robot_wiring.svg](/docs/figures/02b_robot_wiring.svg).

### Entry MD-012: Enterprise GCP Cloud Architecture, BigQuery-Backed Feature Store, and Zero-Loss Rural Store-and-Forward
- **Date**: 2026-09-09
- **Author**: TerraScan Research Agent
- **Context**: Moving TerraScan v2 from an isolated research prototype to a field-deployable platform requires an enterprise cloud architecture that handles intermittent rural wireless connectivity, ingests multimodal data (Sentinel-2 rasters + rover telemetry), scales efficiently across seasonal agricultural cycles, and strictly protects proprietary farm boundaries and soil fertility records.
- **Decision**:
  1. *Edge Ingestion Pattern (Post-Cloud IoT Core)*: Google Cloud IoT Core was officially retired in August 2023. TerraScan v2 routes rover LoRaWAN packets through a managed LoRaWAN Network Server (The Things Stack / ChirpStack) that terminates radio-layer encryption and invokes an HMAC-authenticated HTTPS Webhook hosted on serverless Cloud Run, publishing directly to Cloud Pub/Sub.
  2. *Compute Layer (Cloud Run vs. GKE vs. App Engine)*: Selected serverless Cloud Run (FastAPI backend). Provides scale-to-zero capability ($0 idle cost during winter dormancy), sub-second container cold starts, automated TLS/DNS, and full OCI container support for custom C++ geospatial libraries (GDAL, PROJ, GEOS). GKE was rejected due to a fixed $73/mo cluster management fee and unnecessary operational overhead; App Engine was rejected due to slow cold starts (>15s) and legacy vendor lock-in.
  3. *Feature Store Architecture*: Selected the modern BigQuery-backed Vertex AI Feature Store (2024 architecture). Eliminates the dual-storage synchronization drift and high provisioned cost ($350+/mo) of legacy Redis-based feature stores by serving directly from BigQuery tables. Leverages native `GEOGRAPHY` spatial indexing (`ST_CONTAINS`, `ST_INTERSECTS`) for 10-meter satellite pixel joins with RTK rover ground truth.
  4. *Store-and-Forward Rural Outage Resilience*: Implemented an edge SQLite Write-Ahead Log (WAL) with monotonic 64-bit sequence IDs, millisecond UTC timestamps, and SHA-256 payload checksums. During cellular/LoRa blackouts, the rover buffers records locally without data loss. Upon reconnection, windowed burst transmission paired with Cloud Dataflow sliding-window deduplication (Bloom filter) guarantees strict end-to-end idempotency.
  5. *Agricultural Data Governance & Spatial Differential Privacy*: Implemented tenant isolation in Cloud Firestore and BigQuery Row-Level Security (RLS). For public model training and benchmarking, precise field coordinates are obfuscated via 250m Laplacian spatial jittering and aggregated to Uber H3 Resolution 7 hexagonal zones (~5.16 km²), preventing reverse-engineering of farm boundaries while preserving pedological gradients.
  6. *Pilot Cost Economics*: Itemized pilot deployment operating costs across all subgraphs to \$75.00/month for 10 farms / 5,000 acres, with GPU model serving representing 72% of expenditures and serverless components running almost entirely within free tier allocations.
### Entry MD-013: Interactive Diagram & Image Lightbox Modal and Aspect-Ratio Balanced Architecture Flowchart
- **Date**: 2026-09-09
- **Author**: TerraScan Research Agent
- **Context**: The full GCP cloud architecture diagram rendered at extreme horizontal width (>3400px), causing Docsify's responsive CSS (920px container) to squash the Mermaid flowchart down to an unreadable 135px height. Simultaneously, native Docsify plugins (like zoom-image) ignore dynamically injected Mermaid SVGs and vector schematics, preventing users and science judges from zooming into critical subsystem details.
- **Decision**:
  1. *Balanced 2-Tier Stacked Flowchart Architecture*: Refactored the single-line `flowchart LR` diagram in `docs/figures/03_gcp_technical_architecture.md` into a structured 2-tier DAG (`flowchart TB`). Tier 1 pairs parallel ingestion pipelines (Subgraphs 1 & 2: Rover Telemetry + Copernicus Satellite Pull) feeding down into Subgraph 3 (Cloud Ingestion & Streaming Feature Store). Tier 2 places Subgraph 4 (Vertex AI Platform) feeding Subgraphs 5 & 6 (Application, Analytics & Farmer Delivery), framed by Cross-Cutting Governance & Security. This reduced the aspect ratio from 6:1 to ~1.2:1, increasing native on-page text and node size by ~2.5x.
  2. *Universal Lightbox Pop-up Modal*: Engineered a vanilla JavaScript and CSS lightbox modal in `index.html` featuring:
     - Full click delegation across `.mermaid` diagrams, `.markdown-section img` tags, and standalone SVGs.
     - Cloned SVG DOM tree preservation with viewBox-calculated aspect-ratio fitting.
     - Smooth pan-and-drag interaction with cursor cues (`grab` / `grabbing` / `zoom-in`).
     - Dynamic scaling via mouse wheel, trackpad pinch, and hardware-accelerated zoom buttons (`+ Zoom`, `- Zoom`, `Reset 1:1`, from 15% up to 600%).
     - Dual-mode card background toggle (`Card: White` vs `Card: Clear`) to ensure high contrast for black-line CAD blueprints and white-background diagrams against the dark frosted backdrop.
     - Contextual title bar auto-extracting preceding Markdown headings or figure captions.
- **Deliverables**: [index.html](/index.html), [docs/figures/03_gcp_technical_architecture.md](/docs/figures/03_gcp_technical_architecture.md).

### Entry MD-014: Responsive Table Horizontal Scrolling and Root-Relative SPA Navigation
- **Date**: 2026-09-09
- **Author**: TerraScan Research Agent
- **Context**: Users reported inability to scroll horizontally on multi-column benchmark and audit tables (e.g., Table 1 in `research/07_gap_analysis_v1_vs_literature.md`), clipping critical evidence columns on the right. Simultaneously, relative markdown paths in Docsify sidebars (`_sidebar.md`) caused nested 404 navigation errors when users clicked between subdirectory pages.
- **Decision**:
  1. *Root Cause Analysis*: CSS rule `table { display: table !important; width: 100% !important; }` overrode Docsify's native `display: block; overflow: auto;`. Per CSS 2.1 / Display Module Level 3 specification, browsers strictly ignore `overflow-x: auto` on elements with `display: table`.
  2. *Responsive Table Container Architecture*: Wrapped all rendered tables inside a responsive `.table-wrapper` with `width: 100% !important; max-width: 100% !important; overflow-x: auto !important; -webkit-overflow-scrolling: touch;`. Table styling inside wrapper configured to `display: table !important; width: auto !important; min-width: 100% !important;` with `th { white-space: nowrap; }`. This preserves natural column proportions without artificially stretching narrow columns to 500px, while enabling smooth horizontal scrolling with custom emerald scrollbars (`#10b981`).
  3. *Dynamic DOM Lifecycle Hook*: Implemented a Docsify lifecycle plugin (`hook.doneEach`) that automatically scans the `.markdown-section` DOM on every route change and wraps any newly compiled `<table>` elements into `.table-wrapper` idempotently. Added a CSS direct-child fallback (`.markdown-section > table { display: block !important; overflow-x: auto !important; }`) to prevent clipping before JS execution.
  4. *Root-Relative Navigation*: Prepend leading slashes (`/...`) across all 25 links in root `_sidebar.md` and synchronized identical copies across all 6 subdirectory sidebars (`docs/`, `docs/figures/`, `hardware/`, `knowledge/`, `models/`, `research/`). Fixed all relative links in `knowledge/modeling_decisions_log.md`.
  5. *Automated Verification*: Developed headless Chrome CDP crawler (`scratch/test_portal_e2e.py`) validating all 26 routes (HTTP 200, 0 JS errors, all tables wrapped, horizontal scroll verified with `maxScroll = 792px`).
- **Deliverables**: [index.html](/index.html), [_sidebar.md](/_sidebar.md), [knowledge/modeling_decisions_log.md](/knowledge/modeling_decisions_log.md).



