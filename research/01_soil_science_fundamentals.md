# Soil Science Fundamentals: Nutrient Geochemistry, Speciation, and Soil Matrix Interactions
_Last updated: 2026-09-06 · Status: reviewed_

## TL;DR
Soil nitrogen, phosphorus, and potassium do not exist as free elements, but in complex chemical pools ranging from labile ions in pore water to insoluble minerals and organic polymers. Standard laboratory soil tests use aggressive chemical extractants (e.g., Mehlich-3, Bray-1, Olsen) to dissolve or displace a specific plant-available fraction from the top 15 cm of soil. In contrast, satellites and optical sensors only measure photon reflection from the upper 50 micrometers to 2 millimeters of the surface skin, where they detect molecular bonds, not dissolved ions.

---

## What we're trying to answer
1. In what physical and chemical forms do Nitrogen (N), Phosphorus (P), and Potassium (K) actually reside within the soil matrix (soil organic matter, clay mineral lattices, cation exchange complexes, and soil pore solution)?
2. What are the biological and geochemical mechanisms governing their mobility, retention, fixation, and vertical stratification across the soil profile?
3. What do standard agricultural wet-chemistry extraction protocols (Mehlich-3, Bray-1, Olsen, Dumas/Kjeldahl digestion, 2 M KCl) chemically extract and measure, and how does that differ fundamentally from what a remote or proximal optical sensor observes?
4. Why does vertical depth stratification create a physical disconnect between surface optical reflectance (0–2 mm) and the agronomic crop root zone (0–15 or 0–20 cm)?

---

## What the literature says

### 1. Geochemical Speciation and Pool Dynamics of Macro-Nutrients

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 SOIL MATRIX NUTRIENT POOLS & EQUILIBRIA                          │
├───────────────────────────────┬──────────────────────────────────┬───────────────────────────────┤
│        NITROGEN (N)           │         PHOSPHORUS (P)           │         POTASSIUM (K)         │
├───────────────────────────────┼──────────────────────────────────┼───────────────────────────────┤
│ Organic N (95–98%)            │ Mineral Precipitates (40–60%)    │ Structural Mineral K (90–98%) │
│ (Proteins, amines, humic N)   │ • Acid: Fe/Al oxides (strengite) │ • Feldspars (orthoclase)      │
│               │               │ • Alk: Ca-phosphates (apatite)   │ • Micas (muscovite, biotite)  │
│      Mineralization           │               ▲                  │               ▲               │
│               ▼               │       Precipitation / Dissolution │          Weathering           │
│ Inorganic N (2–5%)            │               ▼                  │               ▼               │
│ • Ammonium (NH4+ on CEC)      │ Adsorbed P (30–50%)              │ Fixed / Interlayer K (1–10%)  │
│ • Nitrate (NO3- in solution)  │ • Inner-sphere chemisorption     │ • Trapped in 2:1 clays        │
│               │               │               ▲                  │   (illite, vermiculite)       │
│        Nitrification          │         Desorption / Adsorption   │               ▲               │
│               ▼               │               ▼                  │          Slow Release         │
│ Highly Mobile / Leachable     │ Solution Orthophosphate (<0.1%)  │               ▼               │
│ Anion (NO3-)                  │ • H2PO4- (pH < 7.2)              │ Exchangeable K+ (1–2% on CEC) │
│                               │ • HPO4(2-) (pH > 7.2)            │               ▲               │
│                               │ Highly Immobile / Bound          │      Rapid Cation Exchange    │
│                               │ (Lost via particulate erosion)   │               ▼               │
│                               │                                  │ Solution K+ (0.1–0.2%)        │
└───────────────────────────────┴──────────────────────────────────┴───────────────────────────────┘
```

#### A. Nitrogen (N): Biological Cycling and Anionic Mobility
Nitrogen in agricultural soils is governed primarily by microbial biological transformations rather than purely inorganic mineral equilibria (Havlin et al., 2013; Brady & Weil, 2016):
- **Organic Pool (>95% of Total N)**:
  - Over 95% of total soil nitrogen is bound within Soil Organic Matter (SOM) in the form of amino acids, amino sugars, peptides, proteins, and recalcitrant heterocyclic nitrogen (e.g., pyrroles, pyridines) condensed into humic complexes.
  - Typical Total Nitrogen (TN) concentrations in agricultural topsoils range from **0.8 to 4.0 g/kg (800 to 4,000 mg/kg)**.
- **Inorganic Labile Pool (<5% of Total N)**:
  - Ammonium (NH₄⁺): Generated via biological ammonification/mineralization:
    ```text
    R-NH₂ + H₂O  ──▶  NH₃ + R-OH
    NH₃ + H⁺     ⇋   NH₄⁺
    ```
    Because it is a positively charged cation, NH₄⁺ is electrostatically retained on the negatively charged Cation Exchange Capacity (CEC) surfaces of phyllosilicate clay minerals and humic carboxyl/phenolic groups (-COO⁻, -O⁻), making it relatively resistant to immediate hydrological leaching.
  - Nitrate (NO₃⁻): Produced via biological two-step nitrification by obligate chemolithoautotrophic bacteria:
    ```text
    Step 1 (Nitrosomonas):  2 NH₄⁺ + 3 O₂  ──▶  2 NO₂⁻ + 2 H₂O + 4 H⁺ + Energy
    Step 2 (Nitrobacter):   2 NO₂⁻ + O₂    ──▶  2 NO₃⁻ + Energy
    ```
  - **Mobility Mechanism**: The nitrate anion (NO₃⁻) possesses a net negative charge. Because virtually all agricultural soils in temperate regions (such as Pennsylvania) have an Anion Exchange Capacity (AEC) close to zero, NO₃⁻ is electrostatically repelled from negative soil mineral and organic colloids. Consequently, NO₃⁻ remains fully dissolved in the gravitational pore water, making it extremely mobile. It leaches rapidly through the soil profile into groundwater aquifers during precipitation events or denitrifies into gaseous nitrous oxide (N₂O) and dinitrogen (N₂) under anaerobic saturated conditions.

> 💻 **Computer Science Translation (Nitrogen)**:
> - **Data Structure**: Nitrogen is a **giant linked list / JSON blob** (proteins in rotting plant tissue). 95% is in this complex object pool.
> - **Satellite Visibility**: High! The N-H and C-H covalent bonds act like physical vibrating springs that absorb shortwave infrared light (~1450 nm, ~2180 nm). Plus, nature hardcodes a strict ratio: $\approx 10$ Carbons for every $1$ Nitrogen (C:N ≈ 10:1).
> - **The Runtime Value (Nitrate NO₃⁻)**: The active variable plants drink is Nitrate. But Nitrate is negative ($-1$), and soil clay is also negative ($-1$). Negative repels negative! Nitrate cannot stick to the soil memory cache; it leaks into water during rain (a **memory leak / buffer overflow** into local rivers).

#### B. Phosphorus (P): The Fixation Paradox and Surface Immobility
Phosphorus behavior is dominated by complex inorganic chemical precipitation-dissolution and surface chemisorption equilibria (Sharpley et al., 2001; Pierzynski et al., 2005):
- **Total Soil Phosphorus (TP)**: Ranges from **200 to 1,500 mg/kg**, but generally **less than 0.1% to 1.0%** of this total is readily available for plant root uptake at any given moment.
- **Solution Orthophosphate**: Plant roots absorb phosphorus exclusively as dissolved inorganic orthophosphate ions. The speciation of orthophosphate is strictly governed by soil solution pH:
  ```text
  H₃PO₄  ⇋  H₂PO₄⁻ (dominant at pH < 7.2)  ⇋  HPO₄²⁻ (dominant at pH > 7.2)  ⇋  PO₄³⁻
  ```
  In standard agricultural soils (pH 5.5–7.5), the bioavailable species are **dihydrogen phosphate (H₂PO₄⁻)** (dominant at pH < 7.2) and **hydrogen phosphate (HPO₄²⁻) (dominant at pH > 7.2)**.
- **Fixation & Geochemical Sinks**:
  - *Acidic Soils (pH < 6.0)*: Orthophosphate rapidly undergoes specific inner-sphere ligand exchange chemisorption onto the hydroxylated surfaces of iron (Fe³⁺) and aluminum (Al³⁺) oxyhydroxides (e.g., goethite α-FeOOH, hematite α-Fe₂O₃, gibbsite Al(OH)₃). Over time, solid-state diffusion locks phosphorus into highly insoluble secondary phosphate minerals such as **strengite (FePO₄·2H₂O)** and **variscite (AlPO₄·2H₂O)** ($K_{sp} \approx 10^{-21}$ to $10^{-22}$).
  - *Alkaline / Calcareous Soils (pH > 7.3)*: Orthophosphate precipitates with calcium (Ca²⁺) to form dicalcium phosphate dihydrate (CaHPO₄·2H₂O), which progressively transforms into insoluble octacalcium phosphate and ultimately refractory **hydroxyapatite (Ca₁₀(PO₄)₆(OH)₂)** ($K_{sp} \approx 10^{-116}$).
  - *Maximum Bioavailability Window*: Orthophosphate solubility peaks in a narrow window between **pH 6.2 and 6.8**.
- **Mobility & Transport Implications**: Because of high affinity chemisorption onto soil mineral surfaces, phosphorus has an extremely low diffusion coefficient in soil water ($D \approx 10^{-12} \text{ to } 10^{-15} \text{ m}^2/\text{s}$, approximately 10,000 times slower than nitrate). Orthophosphate rarely leaches vertically through the soil profile except in coarse sands or soils severely saturated with phosphorus ($>200\text{ mg/kg}$ Mehlich-3 P). **Over 90% of agricultural phosphorus loss occurs via surface runoff and particulate erosion**, where soil particles with adsorbed P are physically detached and transported across field surfaces into waterways (Sharpley et al., 2001).

> 💻 **Computer Science Translation (Phosphorus)**:
> - **Data Structure**: A **deadlocked file / locked mutex** (`chmod 000`).
> - **The Problem**: Over 99% of phosphorus chemically locks onto iron/aluminum rocks (*fixation*). Less than 0.1% is unlocked and available in water for roots to drink.
> - **Satellite Visibility**: Zero. Its vibrating springs only absorb thermal infrared heat waves (9,000–11,000 nm), which optical satellites cannot see. Plus, its concentration (5–50 ppm = 0.005%) is drowned out by background noise.

#### C. Potassium (K): Cation Exchange and Clay Interlayer Dynamics
Potassium exists entirely in inorganic states as the monovalent cation **K⁺**; it is not incorporated into structural biological molecules or organic carbon polymers (Havlin et al., 2013):
- **1. Structural / Mineral K (90%–98% of Total K)**:
  - Exists within the crystal lattice frameworks of primary aluminosilicate minerals, specifically potassium feldspars (orthoclase, microcline: KAlSi₃O₈) and micas (muscovite: KAl₂(AlSi₃O₁₀)(OH)₂; biotite: K(Mg,Fe)₃(AlSi₃O₁₀)(OH)₂).
  - Total K is large (**10,000 to 25,000 mg/kg**, or 1%–2.5% of total soil mass), but this structural pool is released only through geological chemical weathering over decades to centuries.
- **2. Fixed / Non-Exchangeable K (1%–10% of Total K)**:
  - Resides within the non-hydrated interlayer spaces of 2:1 expanding and partially weathered clay minerals, particularly **illite (hydrous mica)** and **vermiculite**.
  - The unhydrated ionic radius of K⁺ (1.38 Å) fits into the hexagonal cavities (1.40 Å diameter) formed by oxygen atoms in adjoining silica tetrahedral sheets. When the clay dries, the sheets contract and collapse around the K⁺ ions, trapping them electrostatically so they cannot be displaced by ordinary neutral salt solutions. Fixed K acts as a slow-release reservoir that buffers exchangeable K.
- **3. Exchangeable K (1%–2% of Total K)**:
  - Represents the primary agronomic plant-available fraction measured in soil testing (**80 to 500+ mg/kg**).
  - Hydrated K⁺ ions are electrostatically held on outer planar and edge surface negative charges of clay minerals and humic colloids. They exist in dynamic equilibrium with the soil solution and are readily displaced by other cations (Ca²⁺, Mg²⁺, NH₄⁺) through rapid reversible cation exchange according to the Gapon equation:
    ```text
    [K⁺]_exch / ([Ca²⁺] + [Mg²⁺])_exch^(1/2)  =  k_G × [K⁺]_sol / ([Ca²⁺] + [Mg²⁺])_sol^(1/2)
    ```
- **4. Solution K (0.1%–0.2% of Total K)**:
  - Free K⁺ ions dissolved in soil pore water (**2 to 20 mg/L**). Plant roots absorb K⁺ from this solution via high-affinity active transport membrane proteins (HAK/KUP/KT transporters).

> 💻 **Computer Science Translation (Potassium)**:
> - **Data Structure**: A **raw primitive integer without pointers** (`int K = 19;`).
> - **Satellite Visibility**: Zero. Potassium in soil exists as isolated K⁺ ions. With no covalent spring bonds connecting it to anything else, it cannot stretch or bend ($d\vec{\mu}/dQ = 0$). Pinging it with optical satellite light returns zero signal!
> - **The Cache (CEC)**: K⁺ is positive ($+1$), and clay is negative ($-1$). Clay serves as a **hardware L1 memory cache**, holding K⁺ so rain doesn't wash it away.

---

### 2. Standard Ground-Truth Analytical Laboratory Protocols vs. Optical Sensors

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   LABORATORY EXTRACTION VS. SATELLITE/OPTICAL SENSING MATRIX                     │
├───────────────────────────────┬──────────────────────────────────┬───────────────────────────────┤
│ Metric / Dimension            │ Standard Wet-Chemistry Lab Test │ Remote/Proximal Optical Sensor│
├───────────────────────────────┼──────────────────────────────────┼───────────────────────────────┤
│ Physical Measurement Depth    │ 0 to 15 cm (0–6 in) plow layer   │ Top 0.05 to 2.0 mm surface skin│
│ Target Measured               │ Chemically labile / desorbable   │ Surface molecular reflectance │
│ Destruction of Soil Matrix    │ Destructive (acid/salt digestion)│ Non-destructive (photon flux) │
│ Analytical Principle          │ ICP-OES, Atomic Emission, Color. │ Electronic & vibrational modes│
│ Nitrogen Target               │ Total N (Dumas) or NO3- (KCl)    │ Proxy via Soil Organic Carbon │
│ Phosphorus Target             │ Labile Orthophosphate (Mehlich-3)│ None (indirect via iron oxides)│
│ Potassium Target              │ Exchangeable K+ (Mehlich-3 / NH4)│ None (indirect via clay bands)│
│ Turnaround Time               │ 3 to 7 business days             │ Instantaneous / 5-day revisit │
│ Cost per Sample / Area        │ $10–$15/sample ($1–$3/acre)      │ $0 (open Sentinel-2 data)     │
│ Legal Compliance Status       │ Statutory standard (PA Act 38)   │ Not legally recognized        │
└───────────────────────────────┴──────────────────────────────────┴───────────────────────────────┘
```

#### Detailed Laboratory Wet-Chemistry Protocols
1. **Mehlich-3 Multielement Extractant (Mehlich, 1984)**:
   - **Formulation**: 0.2 M CH₃COOH + 0.25 M NH₄NO₃ + 0.015 M NH₄F + 0.013 M HNO₃ + 0.001 M EDTA buffered at pH 2.5 ± 0.1.
   - **Extraction Mechanism**:
     - Dilute HNO₃ and CH₃COOH dissolve soluble and calcium-bound phosphates.
     - Ammonium fluoride (NH₄F) provides fluoride ions (F⁻) that selectively complex Al³⁺ and Fe³⁺, releasing chemisorbed orthophosphate into solution through ligand competition.
     - Ammonium nitrate (NH₄NO₃) provides NH₄⁺ cations that displace exchangeable K⁺, Ca²⁺, Mg²⁺, Na⁺ from clay and humus CEC sites.
     - EDTA chelates micronutrient cations (Cu²⁺, Zn²⁺, Mn²⁺).
   - **Detection Method**: The filtered extract is analyzed simultaneously using **Inductively Coupled Plasma Optical Emission Spectrometry (ICP-OES)** at specific atomic emission wavelengths ($\text{P}$: 213.618 nm; $\text{K}$: 766.491 nm), or via ascorbic acid molybdenum blue colorimetry at 882 nm.
   - **Standard Application**: Adopted across the Mid-Atlantic and Northeast US (including Penn State Agricultural Analytical Services Lab) for acidic to neutral soils (pH < 7.3).

2. **Bray-1 Extractant (Bray & Kurtz, 1945)**:
   - **Formulation**: $0.03\text{ M } \text{NH}_4\text{F} + 0.025\text{ M } \text{HCl}$ (pH 2.6).
   - **Extraction Mechanism**: Similar to Mehlich-3 P extraction; F⁻ dissolves aluminum phosphates while dilute HCl dissolves readily soluble calcium phosphates. Ineffective in calcareous soils (pH > 7.3) because CaCO₃ neutralizes the acid and fluorite (CaF₂) precipitates, removing F⁻ from solution.

3. **Olsen Sodium Bicarbonate Extractant (Olsen et al., 1954)**:
   - **Formulation**: $0.5\text{ M } \text{NaHCO}_3$ adjusted to pH 8.5 with NaOH.
   - **Extraction Mechanism**: Designed specifically for neutral to calcareous/alkaline soils. In alkaline soils, bicarbonate ions (HCO₃⁻) precipitate Ca²⁺ as CaCO₃, decreasing calcium activity and driving the dissolution of calcium phosphates. Hydroxide ions (OH⁻) displace phosphate from iron and aluminum oxide surfaces through competitive desorption. This is the official extraction protocol used in the European **LUCAS Topsoil** survey!

4. **Total Nitrogen Determination (Dumas Combustion vs. Kjeldahl)**:
   - **Dumas High-Temperature Combustion (ISO 10694 / AOAC 990.03)**: Dry soil sample is combusted in pure oxygen at $950^{\circ}\text{C} - 1050^{\circ}\text{C}$. All carbon and nitrogen are oxidized to CO₂, H₂O, and nitrogen oxides (NOₓ). Gases pass through copper reduction tubes at $650^{\circ}\text{C}$ to reduce NOₓ to molecular dinitrogen (N₂). Water and CO₂ are scrubbed, and N₂ is quantified using a calibrated thermal conductivity detector (TCD). This measures **Total Nitrogen (TN)**, encompassing both organic and inorganic pools.
   - **Kjeldahl Acid Digestion**: Soil is digested in concentrated sulfuric acid (H₂SO₄) with catalysts (CuSO₄, K₂SO₄, Se) at $380^{\circ}\text{C}$, converting organic N to ammonium sulfate (NH₄)₂SO₄. Digested solution is made alkaline with NaOH, and liberated NH₃ gas is steam-distilled into a boric acid indicator solution and titrated with standardized HCl or H₂SO₄.

> 💻 **Computer Science Translation (Lab Methods = Database Queries)**:
> - **Total Analysis (Dumas)** = `SELECT * FROM soil_all_atoms;` (A raw disk dump of the entire drive, counting every atom even if it's locked inside bedrock).
> - **Agronomic Test (Mehlich-3 / Bray / Olsen)** = `SELECT nutrient WHERE status = 'available_to_roots_this_season';` (A filtered query simulating plant root acid excretion).
> - **Different SQL Flavors**: Mehlich-3 is the query dialect for acidic soils (East Coast USA), while Olsen is the query dialect for alkaline soils (Europe / LUCAS dataset). That's why we have a conversion function: $\text{M3P} \approx 2.05 \times \text{Olsen P}$.

---

### 3. Quantitative Comparison of Soil Extraction Lab Methods in Literature

The table below contrasts standard soil testing methods, highlighting extractant targets, typical agricultural ranges, and comparability factors across agronomic benchmarks.

| Extraction Method | Target Soil Property | Target Chemical Pool | Typical Agricultural Range | Analytical Precision (Lab CV %) | Conversion Factor to Mehlich-3 | Primary Reference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Mehlich-3 P (M3P)** | Plant-Available P | Labile orthophosphate + Al-P + Ca-P | 15–80 mg/kg | 4.5%–7.2% | Baseline ($1.00 \times \text{M3P}$) | Mehlich (1984) |
| **Bray-1 P (B1P)** | Plant-Available P | Labile orthophosphate + Al-P | 12–65 mg/kg | 4.8%–8.0% | $\text{M3P} \approx 1.25 \times \text{B1P}$ | Bray & Kurtz (1945); Beegle (2002) |
| **Olsen P** | Plant-Available P (Calcareous) | Desorbable orthophosphate | 8–45 mg/kg | 5.2%–9.1% | $\text{M3P} \approx 2.05 \times \text{Olsen P}$ (acid/neutral) | Olsen et al. (1954); Mallarino (2003) |
| **Dumas Total N** | Total Nitrogen (TN) | Organic N + NH₄⁺ + NO₃⁻ | 800–4,500 mg/kg (0.8–4.5 g/kg) | 1.8%–3.5% | $\approx 1.02 \times \text{Kjeldahl N}$ | ISO 10694; Bremner (1965) |
| **2 M KCl Extraction** | Mineral Inorganic N | $\text{NO}_3^--\text{N} + \text{NH}_4^+-\text{N}$ | 5–45 mg/kg | 3.5%–6.0% | Measures labile fraction only | Keeney & Nelson (1982) |
| **Ammonium Acetate K** | Exchangeable K⁺ | Electrostatic CEC-bound K⁺ | 75–450 mg/kg | 3.8%–6.5% | $\text{M3K} \approx 1.05 \times \text{NH}_4\text{OAc-K}$ | Thomas (1982); Penn State (2023) |
| **Mehlich-3 K (M3K)** | Exchangeable K⁺ | Electrostatic CEC-bound K⁺ | 80–500 mg/kg | 4.0%–6.8% | Baseline ($1.00 \times \text{M3K}$) | Mehlich (1984); Penn State (2023) |

---

### 4. The Depth Stratification Paradox: Surface Skin vs. Agronomic Root Zone

A fundamental physical barrier in satellite remote sensing of agricultural soils is the **depth penetration mismatch**:

```
0 mm   ════════════════════════════════════════════════════════════════════════  <- Soil Surface
       ┌──────────────────────────────────────────────────────────────────────┐
2 mm   │ OPTICAL PENETRATION SKIN (Sentinel-2 / AS7265x: Visible, NIR, SWIR) │  <- What Satellite Sees
       └──────────────────────────────────────────────────────────────────────┘
5 cm   │ High Organic Matter & Surface P Stratification (No-Till Crust)       │
       │                                                                      │
10 cm  │ AGRONOMIC ROOT ZONE / STANDARD SOIL CORE DEPTH (0–15 or 0–20 cm)     │  <- What Lab Tests Measure
       │ (Active nutrient uptake by corn, soy, wheat, forage crops)          │
15 cm  │                                                                      │
       └──────────────────────────────────────────────────────────────────────┘
```

1. **Optical Penetration Depth**: In the VNIR-SWIR spectrum (400–2500 nm), electromagnetic radiation interacts with soil particles purely through multiple surface scattering and shallow absorption. In agricultural soils with typical bulk densities ($1.2 - 1.5 \text{ g/cm}^3$) and field moisture ($10\% - 25\%$), **photons penetrate only 50 micrometers to 2.0 millimeters** before being completely absorbed or scattered back out (Ben-Dor et al., 2009; Stenberg et al., 2010). Thus, Sentinel-2 observes **only the optical surface skin**.
2. **Agronomic Core Sampling Depth**: Statutory soil fertility guidelines (Penn State Extension, USDA-NRCS) mandate sampling the entire **0 to 15 cm (0–6 in)** or **0 to 20 cm (0–8 in)** plow layer, which is the primary rooting zone for annual field crops.
3. **No-Till Nutrient Stratification**: In conservation tillage and continuous no-till systems—which represent over **65% of Pennsylvania cropland** (USDA-NASS, 2022)—fertilizer, animal manure, and crop residues are applied exclusively to the soil surface without mechanical inversion. Because phosphorus and potassium are relatively immobile, they become **strongly stratified vertically** (Beegle & Durst, 2003; Sharpley, 2003):
   - Available P in the top 0–2 cm may exceed **120 mg/kg**, while at 5–15 cm depth it drops to **25 mg/kg**.
   - Total Organic Carbon and Nitrogen are similarly concentrated in the top 0–3 cm.
4. **Governing Depth-Decay Relationship**: Nutrient concentrations under conservation tillage follow an exponential vertical decay profile:
   $$C(z) = C_{\text{deep}} + (C_{\text{surface}} - C_{\text{deep}}) e^{-\beta z}$$
   where $z$ is depth (cm), $C_{\text{surface}}$ is the topsoil skin concentration, $C_{\text{deep}}$ is the baseline subsoil concentration, and $\beta$ is the stratification attenuation coefficient ($\beta \approx 0.15 - 0.35 \text{ cm}^{-1}$ for P in no-till silt loams; Sharpley, 2003).
5. **Physical Implication for Remote Sensing**: When a satellite model is trained directly against a homogenized 0–15 cm lab core, the model is forced to map surface skin reflectance to a vertically integrated composite. If the stratification profile varies across fields due to differing tillage history (e.g., conventional moldboard plow vs. vertical tillage vs. long-term no-till), **the surface-to-depth correlation collapses**, introducing systematic errors that no purely empirical machine learning model can overcome without incorporating tillage depth priors.

---

## How this applies to TerraScan v2

Understanding these geochemical and physical mechanisms directly dictates five architectural improvements for TerraScan v2:

1. **Explicit Target Variable Definition**:
   - TerraScan v2 will not predict an ambiguous "Nitrogen" target. It will explicitly model **Total Nitrogen (TN, g/kg)** from satellite bare-soil composites (where organic matter coupling provides genuine physical signal), while treating plant-available **Nitrate (NO₃⁻)** as a transient hydrological pool requiring local ground sampling or meteorological water-balance modeling.
2. **Rejection of Pure Optical Modeling for P and K**:
   - Because plant-available orthophosphate ($\text{P}$) and exchangeable potassium ($\text{K}$) lack direct optical absorption bands and reside below diffuse reflectance detection limits, TerraScan v2 will not rely solely on direct spectral regression.
   - Instead, v2 will formulate a **Physics-Guided Hybrid Model**: It will predict Soil Organic Carbon (SOC), clay content, and iron oxide indices from Sentinel-2 SWIR/VNIR bands as physical master variables, and then use regional stoichiometric/pedotransfer transfer functions and proximal rover calibration to infer P and K.
3. **Encoding the Vertical Depth Attenuation Operator**:
   - In Step 3, we will formalize a vertical profile transfer operator in the neural network loss function, mapping surface skin predictions $C(0)$ to agronomic 0–15 cm root-zone concentrations $\bar{C}_{0-15}$ using an exponential decay prior parameter $\beta$ conditioned on field management history (tillage class).
4. **Targeting Surface Runoff Transport Mechanics**:
   - Because phosphorus is tightly bound to soil particles and lost primarily via surface particulate erosion, TerraScan v2 will integrate Digital Elevation Model (DEM) slope-length factors ($LS$) and topographic wetness indices (TWI) to model phosphorus redistribution along field flowpaths.
5. **Harmonizing Multi-Dataset Laboratory Units**:
   - When training on European LUCAS data or US agricultural datasets, all ground-truth targets must be mathematically harmonized to standardized units: Total N in **g/kg**, Available P in **mg/kg Mehlich-3 equivalent** (using published conversion equations, e.g., $\text{M3P} \approx 2.05 \times \text{Olsen P}$), and Exchangeable K in **mg/kg Mehlich-3 equivalent**.

---

## Confidence & caveats

- **Confidence in Geochemical Speciation**: High. The dissociation equilibria of orthophosphate, the anionic mobility of nitrate, and the non-vibrational monoatomic nature of K⁺ are fundamental inorganic chemistry principles.
- **Confidence in Laboratory Extraction Chemistry**: High. Extraction dynamics of Mehlich-3, Olsen, and Bray-1 are codified in official USDA-NRCS Soil Survey Laboratory Methods (Soil Survey Investigations Report No. 42) and Penn State Agricultural Analytical Services procedures.
- **Caveat on Biological Mineralization**: Nitrogen availability changes dynamically within days based on soil temperature, moisture, and microbial activity. A satellite image acquired under bare-soil conditions in April cannot accurately predict available nitrate in mid-July without an auxiliary temperature-moisture biogeochemical decay model.

---

## References

1. Beegle, D. B. (2002). *Soil Fertility Management*. The Agronomy Guide 2002–2003, Penn State Extension, College of Agricultural Sciences, Pennsylvania State University, University Park, PA.
2. Beegle, D. B., & Durst, P. T. (2003). *Managing Phosphorus for Crop Production*. Penn State Extension Agronomy Facts 54, Pennsylvania State University.
3. Ben-Dor, E., Chabrillat, S., Demattê, J. A. M., Taylor, G. R., Hill, J., Whiting, M. L., & Sommer, S. (2009). Using imaging spectroscopy to study soil properties. *Remote Sensing of Environment*, 113, S38–S55. https://doi.org/10.1016/j.rse.2008.12.014
4. Brady, N. C., & Weil, R. R. (2016). *The Nature and Properties of Soils* (15th ed.). Pearson Education, Columbus, OH.
5. Bray, R. H., & Kurtz, L. T. (1945). Determination of total, organic, and available forms of phosphorus in soils. *Soil Science*, 59(1), 39–46. https://doi.org/10.1097/00010694-194501000-00006
6. Bremner, J. M. (1965). Total nitrogen. In C. A. Black (Ed.), *Methods of Soil Analysis: Part 2 Chemical and Microbiological Properties* (pp. 1149–1178). American Society of Agronomy, Madison, WI.
7. Havlin, J. L., Tisdale, S. L., Nelson, W. L., & Beaton, J. D. (2013). *Soil Fertility and Fertilizers: An Introduction to Nutrient Management* (8th ed.). Pearson, Upper Saddle River, NJ.
8. Keeney, D. R., & Nelson, D. W. (1982). Nitrogen—Inorganic forms. In A. L. Page et al. (Eds.), *Methods of Soil Analysis: Part 2 Chemical and Microbiological Properties* (2nd ed., pp. 643–698). American Society of Agronomy, Madison, WI.
9. Mallarino, A. P. (2003). Field calibration for corn of the Mehlich-3 soil phosphorus test with colorimetric and inductively coupled plasma emission spectroscopy determination methods. *Soil Science Society of America Journal*, 67(6), 1928–1934. https://doi.org/10.2136/sssaj2003.1928
10. Mehlich, A. (1984). Mehlich 3 soil test extractant: A modification of Mehlich 2 extractant. *Communications in Soil Science and Plant Analysis*, 15(12), 1409–1416. https://doi.org/10.1080/00103628409367568
11. Olsen, S. R., Cole, C. V., Watanabe, F. S., & Dean, L. A. (1954). *Estimation of Available Phosphorus in Soils by Extraction with Sodium Bicarbonate*. Circular No. 939, United States Department of Agriculture (USDA), Washington, D.C.
12. Penn State Extension. (2023). *The Penn State Agronomy Guide 2023–2024*. College of Agricultural Sciences, The Pennsylvania State University, University Park, PA.
13. Pierzynski, G. M., McDowell, R. W., & Sims, J. T. (2005). Chemistry, cycling, and potential movement of inorganic phosphorus in soils. In J. T. Sims & A. N. Sharpley (Eds.), *Phosphorus: Agriculture and the Environment* (pp. 53–86). American Society of Agronomy, Madison, WI.
14. Sharpley, A. N. (2003). Soil mixing to decrease surface stratification of phosphorus in manured soils. *Journal of Environmental Quality*, 32(4), 1375–1384. https://doi.org/10.2134/jeq2003.1375
15. Sharpley, A. N., McDowell, R. W., & Kleinman, P. J. A. (2001). Phosphorus loss from land to water: integrating agricultural and environmental issues. *Plant and Soil*, 237(2), 287–307. https://doi.org/10.1023/A:1013335814593
16. Stenberg, B., Viscarra Rossel, R. A., Mouazen, A. M., & Wetterlind, J. (2010). Visible and near infrared spectroscopy in soil science. *Advances in Agronomy*, 107, 163–215. https://doi.org/10.1016/S0065-2113(10)07005-7
17. Thomas, G. W. (1982). Exchangeable cations. In A. L. Page et al. (Eds.), *Methods of Soil Analysis: Part 2 Chemical and Microbiological Properties* (2nd ed., pp. 159–165). American Society of Agronomy, Madison, WI.
18. United States Department of Agriculture - National Agricultural Statistics Service (USDA-NASS). (2022). *2022 Census of Agriculture: Pennsylvania State and County Data*. Volume 1, Geographic Area Series, Part 38. Washington, D.C.
19. Xie, X. L., Parent, L. E., & Leblanc, M. (2012). Predicting soil phosphorus-related properties using near-infrared reflectance spectroscopy. *Soil Science Society of America Journal*, 76(5), 1769–1777. https://doi.org/10.2136/sssaj2012.0155
