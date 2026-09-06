# Soil Nutrient Domain Knowledge Base
_Last updated: 2026-09-06 · Status: Active Persistent Memory_

## Purpose
This document serves as TerraScan v2's running scientific reference and glossary for soil chemistry, nutrient transport dynamics, ground-truth laboratory analytical methods, and spectral absorption behavior across Nitrogen (N), Phosphorus (P), and Potassium (K). It is updated and corrected in place as new empirical and literature findings are established.

---

## Macro-Nutrient Spectral & Chemical Profiles

### 1. Nitrogen (N)
- **Dominant Soil Forms**:
  - Organically bound N (>95% of total soil nitrogen): Amino acids, proteins, heterocyclic N, amino sugars incorporated into humic substances.
  - Inorganic mineral N (<5%): Ammonium (NH₄⁺) and Nitrate (NO₃⁻).
- **Physical Concentration Range**:
  - Total Nitrogen (TN): 0.5 to 5.0 g/kg (500 to 5,000 mg/kg) in agricultural topsoils.
  - Plant-available mineral N (NO₃⁻-N): 5 to 50 mg/kg (highly dynamic).
- **Spectroscopic Detectability in VNIR/SWIR**:
  - **Category 1: Directly Detectable via Organic Matter Covariance**.
  - Direct fundamental vibrational overtones and combinations:
    - N-H stretch 1st overtone: ~1450–1510 nm.
    - C-N stretch and N-H in-plane bend combination: ~2060 nm.
    - Protein absorption complexes: ~2180 nm and ~2300 nm (aligns with Sentinel-2 Band 11 and Band 12).
  - Strong indirect coupling: High stoichiometric correlation with Soil Organic Carbon (SOC) via a constrained C:N ratio (typically 10:1 to 14:1 in mineral soils).
- **Standard Analytical Lab Methods**:
  - Total N: Dry combustion (Dumas method, ISO 10694) at $950^{\circ}\text{C} - 1050^{\circ}\text{C}$ with TCD detection, or Kjeldahl acid digestion.
  - Available N: 2 M KCl extraction followed by automated colorimetric cadmium reduction spectrophotometry.

> 💻 **Computer Science Translation (Nitrogen)**:
> - **Data Structure**: Nitrogen is a **giant linked list / JSON blob** (proteins, organic matter). 95% is compiled into dead plant tissue.
> - **Why Satellite Cameras See It**: The N-H and C-H connections are like vibrating springs. They absorb infrared light packets at specific clock frequencies (~1450 nm, ~2180 nm). Furthermore, nature hardcodes a strict ratio: $\approx 10$ Carbons for every $1$ Nitrogen. When the satellite observes dark carbon in the soil, it reliably predicts Nitrogen!
> - **The Runtime Value (Nitrate NO₃⁻)**: Plants actually drink Nitrate, but it has a negative charge ($-1$). Soil clay is also negative, so clay repels it. Nitrate cannot be cached; it floats free in water and causes a **memory leak / buffer overflow** into rivers during rain.

### 2. Phosphorus (P)
- **Dominant Soil Forms**:
  - Inorganic orthophosphate anions: Dihydrogen phosphate (H₂PO₄⁻) at pH < 7.2; Hydrogen phosphate (HPO₄²⁻) at pH > 7.2.
  - Fixed/Precipitated: Bound to calcium (Ca-P, e.g., hydroxyapatite) in alkaline soils; chemisorbed to iron and aluminum oxyhydroxides (e.g., strengite, variscite) in acidic soils.
  - Organic P (30%–65% of total P): Inositol phosphates (phytates), phospholipids, nucleic acids.
- **Physical Concentration Range**:
  - Total Phosphorus (TP): 200 to 1,200 mg/kg.
  - Plant-available P (STP): 5 to 60 mg/kg (Bray-1, Mehlich-3, or Olsen).
- **Spectroscopic Detectability in VNIR/SWIR**:
  - **Category 3: Indirect & Poorly Correlated**.
  - Orthophosphate possesses fundamental P-O stretching and bending vibrations strictly in the Thermal Infrared (9.0–11.2 µm / 900–1100 cm$^{-1}$).
  - Completely lacks primary absorption bands in the 400–2500 nm range of Sentinel-2 and AS7265x.
  - Low concentration threshold: 5–50 mg/kg represents 0.0005%–0.005% of soil mass—at least two orders of magnitude below optical diffuse reflectance detection limits (~0.1%).
  - Apparent optical correlation is mediated solely by indirect adsorption onto iron oxides (Fe³⁺ crystal field transitions at 450–900 nm) and clay lattice edges (Al-OH band at 2200 nm).
- **Standard Analytical Lab Methods**:
  - Mehlich-3 extraction (acidic to neutral soils): 0.2 M CH₃COOH + 0.25 M NH₄NO₃ + 0.015 M NH₄F + 0.013 M HNO₃ + 0.001 M EDTA (pH 2.5). ICP-OES or colorimetry (molybdenum blue).
  - Olsen extraction (calcareous/alkaline soils, LUCAS standard): 0.5 M NaHCO₃ at pH 8.5. Conversion to Mehlich-3: $\text{M3P} \approx 2.05 \times \text{Olsen P}$.
  - Bray-1 extraction: 0.03 M NH₄F + 0.025 M HCl.

> 💻 **Computer Science Translation (Phosphorus)**:
> - **Data Structure**: A **deadlocked file / locked mutex**. 
> - **The Problem**: Plant roots want to read Orthophosphate (H₂PO₄⁻), but it chemically binds to iron and aluminum rocks (like an OS file lock with `chmod 000`). Over 99% is locked in storage; less than 0.1% is active in RAM.
> - **Why Satellite Cameras CANNOT See It**: Its vibrating spring operates in the deep thermal infrared (9,000–11,000 nm heat waves), far beyond Sentinel-2 optical bands (which stop at 2,200 nm). Furthermore, its concentration (5–50 ppm = 0.005%) is buried deep under sensor noise.
> - **Lab Tests (Mehlich-3 vs Olsen)**: These are **custom database queries** (`SELECT available_p`). Mehlich-3 uses mild acid to temporarily unlock the file and measure what a root hair could absorb this season.

### 3. Potassium (K)
- **Dominant Soil Forms**:
  - Structural / Mineral lattice K (90%–98%): Non-exchangeable constituent of primary minerals (micas, muscovite, biotite, potassium feldspars).
  - Slowly exchangeable / Fixed K (1%–10%): Trapped between interlayer sheets of 2:1 clay minerals (vermiculite, illite).
  - Readily available / Exchangeable K⁺ (1%–2%): Hydrated K⁺ cations electrostatically held on soil exchange complexes (CEC) and dissolved in soil solution.
- **Physical Concentration Range**:
  - Exchangeable K⁺: 80 to 500+ mg/kg.
- **Spectroscopic Detectability in VNIR/SWIR**:
  - **Category 3: Spectroscopically Inactive / Completely Indirect**.
  - Monoatomic K⁺ possesses zero covalent chemical bonds and zero vibrational degrees of freedom ($d\vec{\mu}/dQ = 0$). It produces zero infrared absorption bands.
  - Electronic transitions occur strictly in the far UV (<200 nm) or flame emission spectra (766.5 nm atomic line, observable only in thermal plasma excitation, not passive diffuse reflectance).
  - Any machine learning correlation is purely an artifact of covarying clay mineralogy (e.g., illite lattice bands) or soil electrical conductivity.
- **Standard Analytical Lab Methods**:
  - Neutral 1 M NH₄OAc (ammonium acetate) extraction or Mehlich-3 extraction, followed by ICP-OES or flame emission spectrophotometry.

> 💻 **Computer Science Translation (Potassium)**:
> - **Data Structure**: A **raw primitive integer with no pointers** (`int K = 19;`).
> - **Why Satellite Cameras CANNOT See It**: Potassium exists as a single atom with a positive charge (K⁺). Because it has no covalent bonds (no springs connecting it to another atom), it has zero vibrational frequencies. Trying to see K⁺ with a camera is like trying to ping an IP address with no network card. It produces `NULL` optical signal ($d\vec{\mu}/dQ = 0$).
> - **The Soil Cache (CEC)**: K⁺ has a positive charge ($+1$), and clay sheets have negative charges ($-1$). Clay acts as an **L1 hardware cache**, magnetically storing K⁺ so it doesn't wash away in the rain.

---

## The Depth Stratification & Transport Kinetics

### 1. Exponential Vertical Depth Decay in No-Till Soils
In continuous conservation tillage and no-till systems (>65% of PA cropland), non-mobile nutrients (P and K) stratify near the surface:
$$C(z) = C_{\text{deep}} + (C_{\text{surface}} - C_{\text{deep}}) \exp(-\beta z)$$
- $\delta_{\text{pen}}$ (Optical penetration depth): $50\text{ }µm$ to $2.0\text{ mm}$ (surface skin).
- Agronomic root zone: $0$ to $15\text{ cm}$ (or $20\text{ cm}$).
- $\beta$ (attenuation coefficient): $0.15$ to $0.35\text{ cm}^{-1}$.
- Models predicting homogenized root-zone cores from surface skin reflectance require conditioning on tillage management history.

> 💻 **Computer Science Translation (Depth Stratification)**:
> - **L1 Cache vs Disk Storage**: Satellite optical photons only penetrate the top **$1\text{ mm}$ (L1 cache)**. Crop roots live **$15\text{ cm}$ deep (disk drive)**.
> - **Cache-Write Policy**: In no-till fields, fertilizer is applied to the surface and never plowed. This creates an intense surface concentration that decays exponentially with depth ($C(z) = C_0 e^{-\beta z}$).
> - **Why v1 Failed**: It tried to directly map the L1 cache state to disk contents without modeling the write-back pipeline! TerraScan v2 incorporates this decay function directly into the loss function.

### 2. Hydrological Transport & The Pennsylvania Phosphorus Index
$$\text{P-Index Score} = \text{Source Factor} \times \text{Transport Factor}$$
- Source Factor: Weighted sum of Soil Test P ($0.2 \times \text{STP ppm}$), fertilizer rate/timing, and manure rate/method.
- Transport Factor: Product of RUSLE2 soil erosion loss, runoff class, distance to stream, and buffer presence.
- P-Index determines regulatory limits: Low (<60, N-based), Medium (60–79), High (80–99, P crop removal rate), Very High ($\ge 100$, zero P application allowed).
