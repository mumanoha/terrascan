# Remote Sensing & Soil Spectroscopy: Physical Mechanisms from Optical Bands to SWIR
_Last updated: 2026-09-06 · Status: reviewed_

## TL;DR
Optical satellite sensors do not measure soil nutrients directly; they detect photons reflected from the surface that have been modulated by electronic transitions in transition metals and vibrational overtones in covalent bonds. Sentinel-2 MSI captures strong physical signals for iron oxides (bands 2–4, 8A), clay mineral lattices (band 12 at 2190 nm), and organic carbon/nitrogen complexes (bands 11 and 12), but lacks direct physical sensitivity to ionic potassium and trace orthophosphate. Multi-temporal bare-soil compositing is mandatory to strip away vegetation and crop residue, while surface moisture and micro-topography represent major physical confounding variables that must be normalized.

---

## What we're trying to answer
1. What are the governing physical principles of radiative transfer (diffuse reflectance, Kubelka-Munk theory, Hapke scattering) when sunlight interacts with a particulate agricultural soil surface?
2. What specific electronic transitions (crystal field splitting, charge transfer) and vibrational molecular modes (overtones and combination bands of $\text{O-H}, \text{C-H}, \text{N-H}, \text{Al-OH}$) generate diagnostic spectral absorption features in soil?
3. Which Sentinel-2 MSI spectral bands and derived indices (NDVI, NDRE, NDMI, SWIR ratios) carry genuine physical signals for soil properties, and which bands act merely as proxies or noise?
4. How do multi-temporal bare-soil compositing algorithms (e.g., GEOS3, Barest Pixel Composites) isolate pure bare soil from active vegetation and crop residues?
5. What are the fundamental physical limits of optical satellite remote sensing regarding penetration depth, soil moisture interference, and surface roughness?

---

## What the literature says

### 1. Radiative Transfer Physics in the Soil Matrix

When solar irradiance ($E$) strikes an agricultural soil surface, the incident photons undergo a combination of specular surface reflection, internal refraction, multiple volume scattering among discrete mineral and organic grains, and wavelength-dependent absorption (Hapke, 2012; Ben-Dor et al., 2009):

```
                       INCIDENT SOLAR IRRADIANCE
                                   │
                                   ▼
          ┌─────────────────────────────────────────────────┐
          │  Soil Surface Boundary                          │
          └────────┬───────────────────────────────┬────────┘
                   │ Specular Reflection           │ Refraction / Penetration
                   ▼ (Polarized, uninformative)    ▼ (0.05 to 2.0 mm)
            ┌──────────────┐              ┌────────────────────────┐
            │ Surface Glint│              │ Multiple Scattering    │
            └──────────────┘              │ Between Soil Particles │
                                          └───────────┬────────────┘
                                                      │
                            ┌─────────────────────────┴────────────────────────┐
                            ▼                                                  ▼
                  Resonant Absorption                                  Diffuse Reflectance
            • Electronic Transitions (VIS-NIR)                    • Photons escaped back
            • Vibrational Overtones (SWIR)                          to sensor aperture
            (Beer-Lambert Exponential Loss)                       (Measured by Sentinel-2)
```

#### A. Kubelka-Munk Radiative Transfer Formulation
For an optically thick, semi-infinite particulate soil layer where specular reflection is neglected, diffuse reflectance ($R_\infty$) at a specific wavelength $\lambda$ is governed by the Kubelka-Munk equation (Kubelka & Munk, 1931):
$$\frac{K(\lambda)}{S(\lambda)} = \frac{(1 - R_\infty(\lambda))^2}{2 R_\infty(\lambda)}$$
where:
- $K(\lambda)$ is the spectral absorption coefficient, determined by the concentration and molar absorptivity of specific soil chromophores (iron oxides, organic matter, clay hydroxyls, and pore water):
  $$K(\lambda) = \sum_{i} \epsilon_i(\lambda) C_i$$
- $S(\lambda)$ is the diffuse scattering coefficient, governed by physical particle size distribution, packing geometry, mineral refractive index discontinuities, and aggregate roughness:
  $$S(\lambda) \propto \frac{1}{d_{\text{particle}}}$$

#### B. Beer-Lambert Optical Penetration Depth
Light attenuation into the soil bed follows the modified Beer-Lambert Law:
$$I(z, \lambda) = I_0(\lambda) \exp\left(-\alpha_{\text{ext}}(\lambda) z\right)$$
where $\alpha_{\text{ext}}(\lambda) = K(\lambda) + S(\lambda)$ is the total extinction coefficient, and $z$ is depth below the soil surface. The optical penetration depth ($\delta_{\text{pen}}$), defined as the depth where irradiance drops to $1/e$ (~37%) of incident intensity, is given by:
$$\delta_{\text{pen}}(\lambda) = \frac{1}{\alpha_{\text{ext}}(\lambda)}$$
In moist, aggregated agricultural silt loams and clays, $\alpha_{\text{ext}}$ is large ($50 - 200 \text{ mm}^{-1}$ in the visible and SWIR regions), restricting the effective optical observation depth to **$50 \text{ }µm$ to $2.0 \text{ mm}$** (Ben-Dor et al., 2009; Stenberg et al., 2010).

---

### 2. Physical Absorption Mechanisms: Electronic vs. Vibrational Spectroscopy

Spectral absorption features across the 400–2500 nm range arise from two fundamentally different quantum physical processes (Hunt, 1977; Clark, 1999; Stenberg et al., 2010):

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                           SPECTROSCOPIC ABSORPTION MECHANISMS IN SOIL                            │
├────────────────────────────────────────┬─────────────────────────────────────────────────────────┤
│ 1. ELECTRONIC TRANSITIONS (400–1000 nm)│ 2. VIBRATIONAL TRANSITIONS (1000–2500 nm)               │
├────────────────────────────────────────┼─────────────────────────────────────────────────────────┤
│ • Crystal Field Transitions:           │ • Fundamental Vibrations: Occur in Mid-IR (2.5–25 μm)   │
│   Partially filled 3d orbitals of Fe3+ │   (e.g., C-H, O-H, N-H stretch; P-O stretch at 9–11 μm) │
│   split by ligand oxygen field.        │ • Overtones: 1st, 2nd, 3rd overtones at 1/2, 1/3, 1/4   │
│ • Iron Oxides (Hematite, Goethite):    │   fundamental wavelength (anharmonic transitions).      │
│   - Fe3+ absorption: 450–550 nm        │ • Combination Bands: Simultaneous excitation of two     │
│   - Fe3+ crystal field: 650–700 nm     │   differing vibrational modes (e.g., stretch + bend).   │
│   - Fe3+ band minimum: 850–920 nm      │ • Clay Lattices: Al-OH combination at 2200 nm.          │
│ • Soil Organic Matter Darkening:       │ • Organic Matter: C-H (1720, 2300 nm); N-H (2060, 2180) │
│   Broad, overlapping pi-pi* transitions│ • Soil Water: O-H stretch/bend combinations at          │
│   across visible wavelengths.          │   1400 nm and 1900 nm (drowns adjacent features).       │
└────────────────────────────────────────┴─────────────────────────────────────────────────────────┘
```

#### A. Electronic Transitions (Visible to Near-Infrared: 400–1000 nm)
1. **Iron Oxyhydroxides (Fe³⁺ Chromophores)**:
   - Free iron oxides (hematite α-Fe₂O₃, goethite α-FeOOH, ferrihydrite) strongly color soils red, yellow, and brown.
   - When Fe³⁺ is coordinated octahedrally by oxygen (O²⁻) and hydroxyl (OH⁻) ligands, electrostatic repulsion splits the degenerate $3d$ electron orbitals into lower ($t_{2g}$) and higher ($e_g$) energy sub-levels (Crystal Field Theory).
   - Photon absorption triggers forbidden electronic spin transitions:
     - $^6A_{1g} \rightarrow {}^4T_{1g}(^4G)$ transition produces a broad absorption band centered at **850 to 920 nm** (captured by Sentinel-2 Band 8A).
     - $^6A_{1g} \rightarrow {}^4T_{2g}(^4G)$ transition produces an absorption shoulder at **650 to 700 nm** (Sentinel-2 Band 4).
     - Intense charge-transfer absorption between oxygen $2p$ and iron $3d$ orbitals in the near-UV and blue (<500 nm) creates a steep reflectance slope between 450 nm and 600 nm (Sentinel-2 Bands 1, 2, and 3).
2. **Soil Organic Carbon Non-Selective Darkening**:
   - Humic and fulvic acids contain polycyclic aromatic rings, conjugated double bonds ($-\text{C}=\text{C}-\text{C}=\text{C}-$), and quinone groups.
   - Overlapping $\pi \rightarrow \pi^*$ electronic transitions span the entire ultraviolet and visible spectrum, acting as a broad, non-selective light sink that lowers overall surface albedo across all visible bands.

#### B. Vibrational Molecular Transitions (Shortwave-Infrared: 1000–2500 nm)
Molecules vibrate at characteristic fundamental resonant frequencies ($\nu_0$) governed by atomic mass ($m_1, m_2$) and chemical bond spring stiffness ($k$):
$$\nu_0 = \frac{1}{2\pi c} \sqrt{\frac{k}{\mu}} \quad \text{where } \mu = \frac{m_1 m_2}{m_1 + m_2}$$
Because chemical bonds exhibit quantum mechanical anharmonicity (departing from ideal harmonic oscillators), higher-order transitions occur:
- **Overtones**: Transitions from ground state $v=0$ to $v=2$ (first overtone, $\approx 2\nu_0$), $v=3$ (second overtone, $\approx 3\nu_0$).
- **Combination Bands**: Simultaneous excitation of two or more fundamental modes ($\nu_{\text{comb}} = \nu_1 + \nu_2$).

Diagnostic vibrational features in agricultural soils:
1. **Free Water and Interlayer Hydroxyl (O-H)**:
   - Fundamental O-H symmetric/asymmetric stretching ($\nu_1, \nu_3$) and bending ($\nu_2$) occur in the Mid-IR ($2.7 - 6.1 \text{ }µm$).
   - In the SWIR:
     - **1400 nm**: First overtone of the O-H stretching mode ($2\nu_3$).
     - **1900 nm**: Combination band of O-H stretch and H-O-H molecular bending ($\nu_1 + \nu_2$ or $\nu_3 + \nu_2$). This is the definitive indicator of unbound pore water.
2. **Phyllosilicate Clay Minerals (Al-OH and Mg-OH Lattices)**:
   - Octahedral sheet structural hydroxyls bonded to aluminum (Al-OH) in kaolinite, illite, and montmorillonite display a combination band of Al-OH stretch plus Al-O-H in-plane deformation at **2200 nm to 2210 nm**. This feature falls inside **Sentinel-2 Band 12 (2190 nm)**.
   - Trioctahedral minerals (chlorite, talc) display Mg-OH combination bands at **2300 nm to 2320 nm**.
3. **Soil Organic Nitrogen and Carbon (N-H and C-H)**:
   - Aliphatic C-H stretching first overtones occur at **1720 nm and 1760 nm**.
   - Protein and amine N-H stretching first overtones occur at **1450–1510 nm**.
   - The combination of C-N stretch and N-H in-plane deformation produces absorption at **2060 nm**.
   - Protein absorption complexes occur at **2180 nm**, aligning with **Sentinel-2 Band 12**.

---

### 3. Sentinel-2 MSI Spectral Band Allocation and Soil Information Content

The Copernicus Sentinel-2 MultiSpectral Instrument (MSI) carries 13 optical bands spanning 443 nm to 2190 nm (Drusch et al., 2012; European Space Agency, 2021). The table below details the physical and chemical information content of each band for soil characterization:

| Band | Central Wavelength ($\lambda_c$) | Bandwidth ($\Delta\lambda$) | Spatial Res. | Primary Physical Soil Interaction | Diagnostic Chromophore / Chemical Target | Signal Role for TerraScan v2 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **B1** | 443 nm | 21 nm | 60 m | Atmospheric Rayleigh scattering, aerosol optical depth | Atmospheric aerosols, blue-edge charge transfer | Atmospheric correction (Sen2Cor / ACOLITE); not used for soil |
| **B2 (Blue)** | 490 nm | 66 nm | 10 m | Iron oxide charge-transfer absorption; high organic darkening | Fe³⁺ oxyhydroxides; Soil Organic Carbon (SOC) | Albedo baseline; organic matter contrast |
| **B3 (Green)** | 560 nm | 36 nm | 10 m | Transition between blue absorption and red reflectance | Iron oxide reflection shoulder | Soil redness index; background brightness |
| **B4 (Red)** | 665 nm | 31 nm | 10 m | Chlorophyll absorption in vegetation; hematite (Fe³⁺) absorption | Free iron oxides (α-Fe₂O₃); bare soil brightness | Crucial for NDVI vegetation masking; iron oxide quantification |
| **B5 (Red Edge 1)**| 705 nm | 15 nm | 20 m | Sharp red-edge chlorophyll transition | Green vegetation boundary | Detects cover crop emergence and low-canopy greenness |
| **B6 (Red Edge 2)**| 740 nm | 15 nm | 20 m | Vegetation red-edge inflection point | Leaf cellular structure | Vegetation mask thresholding |
| **B7 (Red Edge 3)**| 783 nm | 20 m | 20 m | Upper red-edge canopy plateau | Canopy structural scattering | Vegetation separation |
| **B8 (Broad NIR)** | 842 nm | 106 nm | 10 m | Structural internal scattering; iron oxide absorption shoulder | Iron oxide crystal field minimum; plant leaf reflectance | Primary 10m band for NDVI; bare soil baseline |
| **B8A (Narrow NIR)**| 865 nm | 21 nm | 20 m | Diagnostic Fe³⁺ crystal field absorption well ($^6A_{1g} \rightarrow {}^4T_{1g}$) | Goethite (α-FeOOH) and Hematite (Fe³⁺) | Pure iron oxide mineralogy without water vapor distortion |
| **B9** | 945 nm | 20 nm | 60 m | Atmospheric water vapor column absorption | Atmospheric moisture | Water vapor correction; excluded from soil model |
| **B11 (SWIR-1)** | 1610 nm | 91 nm | 20 m | Cellulose/lignin absorption; broad organic C-H overtone window | Soil Organic Carbon (SOC); dry crop residue | Core feature for Total Nitrogen (TN) via SOC; soil moisture |
| **B12 (SWIR-2)** | 2190 nm | 175 nm | 20 m | Diagnostic Al-OH clay lattice combination; organic protein/N-H | Kaolinite/Illite/Smectite clays; organic N-H (2180 nm) | Core feature for clay texture, CEC, and organic nitrogen |

---

### 4. Key Soil Spectral Indices and Physical Interpretations

To extract robust physical signals while reducing solar zenith angle variations and topographic illumination shadows, mathematical band ratios and normalized differences are computed (Castaldi et al., 2019; Vaudour et al., 2021; Žížala et al., 2022):

1. **Normalized Difference Vegetation Index (NDVI)**:
   $$\text{NDVI} = \frac{B8 - B4}{B8 + B4}$$
   - *Physical Mechanism*: Contrasts the deep chlorophyll absorption in the red band ($B4$) with the intense structural leaf mesophyll scattering in the near-infrared ($B8$).
   - *Application in Soil Mapping*: Serves as a strict binary masking filter. A threshold of **$\text{NDVI} < 0.25$** (or $< 0.20$ in sparse croplands) is required to ensure that Sentinel-2 pixels represent bare soil rather than green vegetation canopies.
2. **Normalized Difference Red Edge (NDRE)**:
   $$\text{NDRE} = \frac{B8 - B5}{B8 + B5}$$
   - *Physical Mechanism*: Sensitive to moderate-to-low chlorophyll concentrations where NDVI saturates; captures early crop emergence and weeds.
3. **Normalized Difference Moisture Index (NDMI) / Normalized Difference Water Index (NDWI)**:
   $$\text{NDMI} = \frac{B8 - B11}{B8 + B11}$$
   - *Physical Mechanism*: Contrasts NIR structural reflectance with SWIR-1 liquid water absorption. Indicates surface gravimetric soil moisture. When $\text{NDMI}$ is elevated, optical spectra are suppressed by liquid water films.
4. **Normalized Burn Ratio 2 (NBR2 / Soil Residue Index)**:
   $$\text{NBR2} = \frac{B11 - B12}{B11 + B12}$$
   - *Physical Mechanism*: Cellulosic dry crop residue (straw, corn stover) possesses distinct cellulose and lignin absorption features at 2100 nm, elevating $B12$ absorption relative to $B11$. Unweathered bare mineral soil exhibits a different SWIR slope.
   - *Application*: A threshold of **$\text{NBR2} < 0.15$** is applied in tandem with NDVI to filter out non-photosynthetic crop residue in conservation-tillage fields (Vaudour et al., 2021).
5. **Soil Clay and Carbonate Index (SCCI)**:
   $$\text{SCCI} = \frac{B11}{B12}$$
   - *Physical Mechanism*: Evaluates the depth of the $2200\text{ nm}$ clay hydroxyl absorption band relative to the SWIR-1 continuum. Positively correlated with clay fraction and CEC.
6. **Redness Index (RI)**:
   $$\text{RI} = \frac{B4^2}{B3^3} \quad \text{or} \quad \frac{B4 - B3}{B4 + B3}$$
   - *Physical Mechanism*: Measures the slope of the iron oxide absorption edge, directly correlating with hematite concentration and soil weathering status.

---

### 5. Multi-Temporal Bare-Soil Compositing Methodologies

A major challenge in satellite digital soil mapping is that agricultural fields are covered by green crops, pasture, or crop residue throughout most of the year. In temperate humid regions like Pennsylvania, a single field may be bare for only **2 to 4 weeks in early spring (April–May) or post-harvest (October–November)** (Diek et al., 2021).

To construct continuous regional bare-soil reflectance rasters, three multi-temporal compositing frameworks have been developed in literature:

```
Multi-Temporal Sentinel-2 L2A Stack (2018–2024 Cloud-Free Imagery)
                            │
                            ▼
    Apply Atmospheric Correction & Cloud/Shadow QA Masking
                            │
                            ▼
    Pixel-by-Pixel Spectral Filtering:
    • NDVI < 0.25  (Eliminates Green Photosynthetic Vegetation)
    • NBR2 < 0.15  (Eliminates Dry Cellulosic Crop Residues)
    • NDMI < 0.30  (Eliminates Standing Water / Water-Saturated Soil)
                            │
                            ▼
    Multi-Temporal Temporal Aggregation:
    ┌────────────────────────────────────────────────────────┐
    │ Method A: Geospatial Soil Sensing System (GEOS3)       │
    │           (Demattê et al., 2020)                       │
    │           Extracts median reflectance of valid pixels  │
    ├────────────────────────────────────────────────────────┤
    │ Method B: Barest Pixel Composite (Min-NDVI)            │
    │           (Diek et al., 2021; Rogge et al., 2018)      │
    │           Selects spectral vector at minimum NDVI date │
    ├────────────────────────────────────────────────────────┤
    │ Method C: Tellus S2 / Synthetic Soil Image (SYSI)      │
    │           (Vaudour et al., 2021; Žížala et al., 2022)  │
    │           Medoid reflectance vector in bare feature space│
    └────────────────────────────────────────────────────────┘
                            │
                            ▼
           Harmonized Pristine Bare-Soil Spectral Cube
```

#### Comparison of Compositing Algorithms
- **Barest Pixel Composite (Min-NDVI)**: For each spatial pixel, selects the full 12-band spectral vector from the single acquisition date where NDVI achieved its absolute minimum over a multi-year window. *Advantage*: Guarantees physical spectral consistency (all 12 bands originate from a single coherent physical observation). *Disadvantage*: Vulnerable to residual cloud shadows or extreme soil crusting on that single date.
- **GEOS3 Median Composite (Demattê et al., 2020)**: Computes the median reflectance across all dates identified as bare soil for each band independently. *Advantage*: Suppresses atmospheric noise, sudden rainfall events, and tractor wheel ruts. *Disadvantage*: Independent band medians can slightly distort inter-band slope relationships.
- **Medoid Composite (SYSI / Tellus S2, Vaudour et al., 2021)**: Computes the multi-dimensional medoid—the actual acquired spectral vector that minimizes the Euclidean distance to the centroid of all bare-soil observations for that pixel. *Advantage*: Combines physical spectral integrity with multi-temporal noise rejection. **Adopted as the target protocol for TerraScan v2.**

---

### 6. Physical Confounding Factors: Moisture, Crusts, and Roughness

When translating satellite or proximal spectral measurements into quantitative nutrient predictions, three physical environmental factors distort spectral reflectance:

1. **Soil Moisture Attenuation**:
   - Liquid water has a high dielectric constant and strong absorption coefficients across the infrared. As volumetric water content increases from $5\%$ to $35\%$, overall soil reflectance drops dramatically across all bands (darkening effect) due to increased internal optical scattering inside water films coating soil particles (Lobell & Asner, 2002; Liu et al., 2002).
   - Water absorption overtones at $1400\text{ nm}$ and $1900\text{ nm}$ broaden significantly, masking the subtle Al-OH clay band at $2200\text{ nm}$ and the N-H protein band at $2180\text{ nm}$.
   - *Mitigation*: Multi-temporal compositing selects dry soil dates, while proximal rovers must incorporate an on-board high-frequency moisture sensor (e.g., TDR / capacitance probe) or SWIR water-index normalization.
2. **Surface Roughness & Micro-Shadowing**:
   - Tillage operations (chisel plowing, disking) create soil clods ranging from 1 cm to 15 cm. Low solar elevation angles cast micro-shadows that reduce total measured radiance at the satellite sensor.
   - Non-Lambertian diffuse scattering distorts spectral shape.
   - *Mitigation*: Computing normalized band ratios (e.g., $B11/B12, B4/B3$) largely cancels out multiplicative illumination variations caused by surface shadows.
3. **Physical & Biological Soil Crusts**:
   - Raindrop impact on bare soil forms physical structural seals (1–3 mm thick) characterized by clay dispersion and particle re-orientation.
   - Surface crusts concentrate fine silt and clay particles at the very surface, artificially elevating clay spectral signatures relative to the bulk plow layer underneath.
   - *Mitigation*: Incorporating terrain roughness derivatives (topographic slope, curvature) and rover in-situ scratch sensors to penetrate surface crusts.

---

## How this applies to TerraScan v2

These spectroscopic principles reshape TerraScan v2's data ingestion and modeling pipeline:

1. **Band Selection Strategy**:
   - Drop Band 1 (coastal aerosol) and Band 9 (water vapor) from soil feature sets; their spatial resolution (60 m) and atmospheric sensitivity add noise rather than soil signal.
   - Focus feature extraction on **B2, B3, B4, B8A (20m), B11 (SWIR-1), and B12 (SWIR-2)**, which contain direct physical information on iron oxides, SOC, and clay mineralogy.
2. **Bare Soil Preprocessing Pipeline**:
   - Implement multi-temporal Sentinel-2 L2A compositing in Google Earth Engine (GEE) using a **3-year window (2021–2024)** with dual filtering ($\text{NDVI} < 0.25$ and $\text{NBR2} < 0.15$) and multi-dimensional medoid selection.
3. **Indirect Nutrient Coupling Architecture**:
   - Accept that Sentinel-2 cannot see K⁺ or PO₄³⁻ directly. Structure the machine learning architecture to explicitly predict the **three physical master variables** ($SOC$, $Clay$, $Fe$-oxides) for which real optical signals exist.
   - Use these master variables as physical latent constraints to regularize downstream spatial nutrient mapping.
4. **Proximal Rover Sensor Selection**:
   - The AMS AS7265x sensor (410–940 nm) cuts off before the SWIR region, meaning it cannot detect the $1400\text{ nm}$, $1900\text{ nm}$, $2060\text{ nm}$, or $2200\text{ nm}$ vibrational absorption features.
   - TerraScan v2 will acknowledge this physical boundary: the AS7265x on the robot will be utilized strictly for in-situ high-resolution iron oxide and organic darkening tracking ($410-940\text{ nm}$), while SWIR clay and moisture signals will be supplied by Sentinel-2 Band 11 and Band 12.

---

## Confidence & caveats

- **Confidence in Spectral Absorption Physics**: High. Crystal field splitting of Fe³⁺ and vibrational overtones of $\text{O-H}, \text{C-H}, \text{Al-OH}$ are grounded in quantum mechanics and verified by USGS and JPL spectral libraries.
- **Confidence in Sentinel-2 Band Capabilities**: High. Documented across dozens of bare-soil digital soil mapping investigations (Castaldi et al., 2019; Vaudour et al., 2021; Žížala et al., 2022).
- **Caveat on Crop Residue Interference**: In high-residue no-till fields, decaying corn or wheat straw covers $>50\%$ of the surface even during planting. If $\text{NBR2}$ filtering removes too many pixels, composite coverage may have gaps, requiring reliance on terrain covariates or rover ground sampling.

---

## References

1. Ben-Dor, E., Chabrillat, S., Demattê, J. A. M., Taylor, G. R., Hill, J., Whiting, M. L., & Sommer, S. (2009). Using imaging spectroscopy to study soil properties. *Remote Sensing of Environment*, 113, S38–S55. https://doi.org/10.1016/j.rse.2008.12.014
2. Castaldi, F., Palombo, A., Santini, F., Pascucci, S., Pignatti, S., & Casa, R. (2019). Sentinel-2 image capacities to predict common topsoil properties of temperate and Mediterranean agroecosystems. *Remote Sensing of Environment*, 223, 55–68. https://doi.org/10.1016/j.rse.2019.01.006
3. Clark, R. N. (1999). Chapter 1: Spectroscopy of rocks and minerals, and principles of spectroscopy. In A. N. Rencz (Ed.), *Manual of Remote Sensing: Volume 3, Remote Sensing for the Earth Sciences* (pp. 3–58). John Wiley & Sons, New York.
4. Demattê, J. A. M., Fongaro, C. T., Rizzo, R., & Safanelli, J. L. (2020). Geospatial Soil Sensing System (GEOS3): A modern open-source tool for digital soil mapping using bare soil satellite composites. *Geoderma*, 375, 114481. https://doi.org/10.1016/j.geoderma.2020.114481
5. Diek, S., Fornaro, G., & Chabrillat, S. (2021). An analysis of bare soil occurrence in arable croplands for remote sensing topsoil applications. *Remote Sensing*, 13(3), 474. https://doi.org/10.3390/rs13030474
6. Drusch, M., Del Bello, U., Carlier, S., Colin, O., Fernandez, V., Gascon, F., ... & Bargellini, P. (2012). Sentinel-2: ESA's optical high-resolution mission for GMES operational services. *Remote Sensing of Environment*, 120, 25–36. https://doi.org/10.1016/j.rse.2011.11.026
7. European Space Agency (ESA). (2021). *Sentinel-2 User Handbook* (Issue 2, Rev. 3). European Space Research and Technology Centre (ESTEC), Noordwijk, Netherlands.
8. Hapke, B. (2012). *Theory of Reflectance and Emittance Spectroscopy* (2nd ed.). Cambridge University Press, Cambridge, UK. https://doi.org/10.1017/CBO9781139025683
9. Hunt, G. R. (1977). Spectral signatures of particulate minerals in the visible and near infrared. *Geophysics*, 42(3), 501–513. https://doi.org/10.1190/1.1440721
10. Kubelka, P., & Munk, F. (1931). Ein Beitrag zur Optik der Farbanstriche. *Zeitschrift für Technische Physik*, 12, 593–601.
11. Liu, W., Baret, F., Gu, X., Tong, Q., Zheng, L., & Zhang, B. (2002). Relating soil surface moisture to reflectance. *Remote Sensing of Environment*, 81(2–3), 238–246. https://doi.org/10.1016/S0034-4257(01)00347-9
12. Lobell, D. B., & Asner, G. P. (2002). Moisture effects on soil reflectance. *Soil Science Society of America Journal*, 66(3), 722–727. https://doi.org/10.2136/sssaj2002.7220
13. Rogge, D., Bauer, A., Zeidler, J., Mueller, A., Esch, T., & Heiden, U. (2018). Building an open soil spectral library using bare soil composites from Landsat-8 and Sentinel-2 data. *Remote Sensing of Environment*, 218, 282–295. https://doi.org/10.1016/j.rse.2018.09.009
14. Stenberg, B., Viscarra Rossel, R. A., Mouazen, A. M., & Wetterlind, J. (2010). Visible and near infrared spectroscopy in soil science. *Advances in Agronomy*, 107, 163–215. https://doi.org/10.1016/S0065-2113(10)07005-7
15. Vaudour, E., Gholizadeh, A., Castaldi, F., Saberioon, M., Borůvka, L., Urbina-Salazar, D., ... & van Wesemael, B. (2021). Tellus S2: A global composite of Sentinel-2 topsoil spectral reflectance. *Remote Sensing*, 13(11), 2184. https://doi.org/10.3390/rs13112184
16. Žížala, D., Minařík, R., & Skála, J. (2022). Soil organic carbon mapping using Sentinel-2 and Landsat 8 data: Open soil composite and multi-temporal bare soil approach. *Remote Sensing*, 14(14), 3326. https://doi.org/10.3390/rs14143326
