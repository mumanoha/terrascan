# Literature Index & Master Bibliography
_Last updated: 2026-09-06 · Status: Active Persistent Memory_

## Purpose
This document provides a centralized, flat, running bibliography of all peer-reviewed papers, agency technical manuals, and data sources referenced across the TerraScan v2 project. Each entry is tagged with its full citation, digital object identifier (DOI) or URL, key quantitative findings (e.g., $R^2$, RMSE, spectral bands), and which project research files cite it.

---

## Master Bibliography (Alphabetical)

### 1. Ballabio et al. (2019)
- **Citation**: Ballabio, C., Lugato, E., Fernández-Ugalde, O., Orgiazzi, A., Yigini, Y., Panagos, P., & Montanarella, L. (2019). Mapping LUCAS topsoil chemical properties at European scale using Gaussian process regression. *Geoderma*, 355, 113912.
- **DOI**: [10.1016/j.geoderma.2019.113912](https://doi.org/10.1016/j.geoderma.2019.113912)
- **Key Findings**: Continental modeling of ~22,000 LUCAS soil samples across EU. Total N: $R^2 = 0.48$, $\text{RMSE} = 1.28\text{ g/kg}$; Extractable P (Olsen): $R^2 = 0.16$, $\text{RMSE} = 31.5\text{ mg/kg}$; Extractable K: $R^2 = 0.31$, $\text{RMSE} = 178\text{ mg/kg}$. Confirms P and K are extremely poorly modeled by spatial/remote covariates alone.
- **Cited In**: `research/07_gap_analysis_v1_vs_literature.md`, `knowledge/soil_nutrient_domain.md`

### 2. Beegle (2002)
- **Citation**: Beegle, D. B. (2002). *Soil Fertility Management*. The Agronomy Guide 2002–2003, Penn State Extension, College of Agricultural Sciences, Pennsylvania State University, University Park, PA.
- **Key Findings**: Defines official soil test calibration categories for Pennsylvania: Soil Test P (STP) optimum 30–50 ppm, Soil Test K (STK) optimum 100–150 ppm. Establishes crop removal fertilizer recommendation algorithms.
- **Cited In**: `research/01_soil_science_fundamentals.md`, `research/05_agronomy_regulatory_context.md`

### 3. Beegle & Durst (2003)
- **Citation**: Beegle, D. B., & Durst, P. T. (2003). *Managing Phosphorus for Crop Production*. Penn State Extension Agronomy Facts 54, Pennsylvania State University.
- **Key Findings**: Explains the agronomic and environmental risks of soil phosphorus stratification under continuous no-till and manure application in Pennsylvania.
- **Cited In**: `research/01_soil_science_fundamentals.md`, `research/05_agronomy_regulatory_context.md`

### 4. Ben-Dor et al. (2009)
- **Citation**: Ben-Dor, E., Chabrillat, S., Demattê, J. A. M., Taylor, G. R., Hill, J., Whiting, M. L., & Sommer, S. (2009). Using imaging spectroscopy to study soil properties. *Remote Sensing of Environment*, 113, S38–S55.
- **DOI**: [10.1016/j.rse.2008.12.014](https://doi.org/10.1016/j.rse.2008.12.014)
- **Key Findings**: Demonstrates that optical photons penetrate only 50 micrometers to 2 millimeters into soil beds. Details soil moisture attenuation and mineral spectral libraries.
- **Cited In**: `research/01_soil_science_fundamentals.md`, `research/02_remote_sensing_spectroscopy.md`

### 5. Brady & Weil (2016)
- **Citation**: Brady, N. C., & Weil, R. R. (2016). *The Nature and Properties of Soils* (15th ed.). Pearson Education, Columbus, OH.
- **Key Findings**: Benchmark soil science textbook. Documents C:N ratio (10:1 to 14:1), microbial nitrogen mineralization, and phosphorus chemical fixation onto iron/aluminum oxyhydroxides and calcium minerals.
- **Cited In**: `research/01_soil_science_fundamentals.md`, `research/07_gap_analysis_v1_vs_literature.md`

### 6. Bray & Kurtz (1945)
- **Citation**: Bray, R. H., & Kurtz, L. T. (1945). Determination of total, organic, and available forms of phosphorus in soils. *Soil Science*, 59(1), 39–46.
- **DOI**: [10.1097/00010694-194501000-00006](https://doi.org/10.1097/00010694-194501000-00006)
- **Key Findings**: Foundational formulation of the Bray-1 acid fluoride phosphorus extraction method for acidic soils.
- **Cited In**: `research/01_soil_science_fundamentals.md`

### 7. Bremner (1965)
- **Citation**: Bremner, J. M. (1965). Total nitrogen. In C. A. Black (Ed.), *Methods of Soil Analysis: Part 2 Chemical and Microbiological Properties* (pp. 1149–1178). American Society of Agronomy, Madison, WI.
- **Key Findings**: Details analytical wet-chemistry Kjeldahl digestion and Dumas dry combustion protocols for Total Soil Nitrogen.
- **Cited In**: `research/01_soil_science_fundamentals.md`

### 8. Castaldi et al. (2019a)
- **Citation**: Castaldi, F., Hueni, A., Chabrillat, S., Ward, K., Buttafuoco, G., Bomans, B., Vreys, K., Brell, M., & van Wesemael, B. (2019). Evaluating the capability of the Sentinel 2 data for soil organic carbon prediction in croplands. *ISPRS Journal of Photogrammetry and Remote Sensing*, 147, 9–20.
- **DOI**: [10.1016/j.isprsjprs.2018.11.026](https://doi.org/10.1016/j.isprsjprs.2018.11.026)
- **Key Findings**: Sentinel-2 MSI achieves $R^2 = 0.65$ and $\text{RMSE} = 3.2\text{ g/kg}$ for Soil Organic Carbon (SOC) in croplands under bare-soil conditions. Proves Sentinel-2 VNIR/SWIR bands reliably capture organic matter darkening.
- **Cited In**: `research/07_gap_analysis_v1_vs_literature.md`

### 9. Castaldi et al. (2019b)
- **Citation**: Castaldi, F., Palombo, A., Santini, F., Pascucci, S., Pignatti, S., & Casa, R. (2019). Sentinel-2 image capacities to predict common topsoil properties of temperate and Mediterranean agroecosystems. *Remote Sensing of Environment*, 223, 55–68.
- **DOI**: [10.1016/j.rse.2019.01.006](https://doi.org/10.1016/j.rse.2019.01.006)
- **Key Findings**: Benchmarks Sentinel-2 MSI against airborne hyperspectral sensors for clay, sand, SOC, and iron across 450 field points. Demonstrates spectral band resolution limits in discriminating mineral fractions.
- **Cited In**: `research/02_remote_sensing_spectroscopy.md`, `research/07_gap_analysis_v1_vs_literature.md`

### 10. Clark (1999)
- **Citation**: Clark, R. N. (1999). Chapter 1: Spectroscopy of rocks and minerals, and principles of spectroscopy. In A. N. Rencz (Ed.), *Manual of Remote Sensing: Volume 3, Remote Sensing for the Earth Sciences* (pp. 3–58). John Wiley & Sons, New York.
- **Key Findings**: Authoritative manual on quantum vibrational spectroscopy, overtone/combination band physics, and electronic crystal field transitions.
- **Cited In**: `research/02_remote_sensing_spectroscopy.md`

### 11. Commonwealth of Pennsylvania (1937)
- **Citation**: Commonwealth of Pennsylvania. (1937). *The Clean Streams Law*. Act of June 22, 1937, P.L. 1987, as amended, 35 P.S. §§ 691.1–691.1001. Harrisburg, PA.
- **Key Findings**: Primary statutory authority establishing that agricultural sediment and nutrient discharges into state waters constitute illegal pollution.
- **Cited In**: `research/05_agronomy_regulatory_context.md`

### 12. Commonwealth of Pennsylvania (2005)
- **Citation**: Commonwealth of Pennsylvania. (2005). *Nutrient Management and Odor Management Act (Act 38 of 2005)*. Title 3 Pennsylvania Consolidated Statutes, Chapter 5, §§ 501–522; codified at Title 25 Pennsylvania Code, Chapter 83, Subchapter D. Harrisburg, PA.
- **URL**: [25 Pa. Code Chapter 83](https://www.pacodeandbulletin.gov/Display/pacode?file=/secure/pacode/data/025/chapter083/subchapDtoc.html)
- **Key Findings**: Statutory law governing agricultural nutrient management in PA. Mandates certified soil tests conducted at least once every 3 years by approved analytical wet chemistry laboratories (Mehlich-3 P/K).
- **Cited In**: `research/05_agronomy_regulatory_context.md`, `research/07_gap_analysis_v1_vs_literature.md`

### 13. Conley et al. (2009)
- **Citation**: Conley, D. J., Paerl, H. W., Howarth, R. W., Boesch, D. F., Seitzinger, S. P., Havens, K. E., Lancelot, C., & Likens, G. E. (2009). Controlling eutrophication: nitrogen and phosphorus. *Science*, 323(5917), 1014–1015.
- **DOI**: [10.1126/science.1167755](https://doi.org/10.1126/science.1167755)
- **Key Findings**: Demonstrates that mitigation of coastal and estuarine hypoxia requires dual-nutrient reduction strategies (controlling both N and P).
- **Cited In**: `research/07_gap_analysis_v1_vs_literature.md`

### 14. Demattê et al. (2020)
- **Citation**: Demattê, J. A. M., Fongaro, C. T., Rizzo, R., & Safanelli, J. L. (2020). Geospatial Soil Sensing System (GEOS3): A modern open-source tool for digital soil mapping using bare soil satellite composites. *Geoderma*, 375, 114481.
- **DOI**: [10.1016/j.geoderma.2020.114481](https://doi.org/10.1016/j.geoderma.2020.114481)
- **Key Findings**: Formulates the Geospatial Soil Sensing System (GEOS3) for extracting bare-soil composite pixels from multitemporal satellite imagery across croplands.
- **Cited In**: `research/02_remote_sensing_spectroscopy.md`

### 15. Diaz & Rosenberg (2008)
- **Citation**: Diaz, R. J., & Rosenberg, R. (2008). Spreading dead zones and consequences for marine ecosystems. *Science*, 321(5891), 926–929.
- **DOI**: [10.1126/science.1156401](https://doi.org/10.1126/science.1156401)
- **Key Findings**: Comprehensive global synthesis documenting >400 marine dead zones covering >245,000 km², driven primarily by agricultural nutrient runoff.
- **Cited In**: `research/07_gap_analysis_v1_vs_literature.md`

### 16. Diek et al. (2021)
- **Citation**: Diek, S., Fornaro, G., & Chabrillat, S. (2021). An analysis of bare soil occurrence in arable croplands for remote sensing topsoil applications. *Remote Sensing*, 13(3), 474.
- **DOI**: [10.3390/rs13030474](https://doi.org/10.3390/rs13030474)
- **Key Findings**: Proves that temperate croplands exhibit bare soil for only 2 to 4 weeks annually, requiring multi-year satellite stacks with revisit frequencies under 5–7 days to construct valid bare soil composites.
- **Cited In**: `research/02_remote_sensing_spectroscopy.md`

### 17. Drusch et al. (2012)
- **Citation**: Drusch, M., Del Bello, U., Carlier, S., Colin, O., Fernandez, V., Gascon, F., ... & Bargellini, P. (2012). Sentinel-2: ESA's optical high-resolution mission for GMES operational services. *Remote Sensing of Environment*, 120, 25–36.
- **DOI**: [10.1016/j.rse.2011.11.026](https://doi.org/10.1016/j.rse.2011.11.026)
- **Key Findings**: Complete optical and radiometer engineering specifications for Sentinel-2 MSI instrument.
- **Cited In**: `research/02_remote_sensing_spectroscopy.md`

### 18. Gholizadeh et al. (2022)
- **Citation**: Gholizadeh, A., Saberioon, M., Viscarra Rossel, R. A., Borůvka, L., & Klement, A. (2022). Assessing machine learning-based prediction under different agricultural practices for digital mapping of soil organic carbon and available phosphorus. *Agriculture*, 12(7), 1062.
- **DOI**: [10.3390/agriculture12071062](https://doi.org/10.3390/agriculture12071062)
- **Key Findings**: Digital mapping of Available Phosphorus (Olsen P) across 201 samples yielded Normalized RMSE of 96.8% and $R^2 = 0.38$.
- **Cited In**: `research/07_gap_analysis_v1_vs_literature.md`

### 19. Hapke (2012)
- **Citation**: Hapke, B. (2012). *Theory of Reflectance and Emittance Spectroscopy* (2nd ed.). Cambridge University Press, Cambridge, UK.
- **DOI**: [10.1017/CBO9781139025683](https://doi.org/10.1017/CBO9781139025683)
- **Key Findings**: The fundamental theoretical treatise on radiative transfer through particulate media, defining bidirectional reflectance distribution functions (BRDF) and multiple scattering.
- **Cited In**: `research/02_remote_sensing_spectroscopy.md`

### 20. Havlin et al. (2013)
- **Citation**: Havlin, J. L., Tisdale, S. L., Nelson, W. L., & Beaton, J. D. (2013). *Soil Fertility and Fertilizers: An Introduction to Nutrient Management* (8th ed.). Pearson, Upper Saddle River, NJ.
- **Key Findings**: Comprehensive breakdown of soil fertility principles, Gapon cation exchange equations, potassium clay fixation, and phosphorus sorption isotherms.
- **Cited In**: `research/01_soil_science_fundamentals.md`

### 21. Hunt (1977)
- **Citation**: Hunt, G. R. (1977). Spectral signatures of particulate minerals in the visible and near infrared. *Geophysics*, 42(3), 501–513.
- **DOI**: [10.1190/1.1440721](https://doi.org/10.1190/1.1440721)
- **Key Findings**: Landmark physical derivation of electronic crystal field transitions in transition metals and vibrational overtone frequencies in clay minerals.
- **Cited In**: `research/02_remote_sensing_spectroscopy.md`

### 22. Karniadakis et al. (2021)
- **Citation**: Karniadakis, G. E., Kevrekidis, I. G., Lu, L., Perdikaris, P., Wang, S., & Yang, L. (2021). Physics-informed machine learning. *Nature Reviews Physics*, 3(6), 422–440.
- **DOI**: [10.1038/s42254-021-00314-5](https://doi.org/10.1038/s42254-021-00314-5)
- **Key Findings**: Foundational review of physics-informed ML architectures, classifying inductive biases into observational, architectural, and loss-penalty formulations for differential equations.
- **Cited In**: `research/07_gap_analysis_v1_vs_literature.md`

### 23. Kubelka & Munk (1931)
- **Citation**: Kubelka, P., & Munk, F. (1931). Ein Beitrag zur Optik der Farbanstriche. *Zeitschrift für Technische Physik*, 12, 593–601.
- **Key Findings**: Mathematical formulation of the Kubelka-Munk two-flux radiative transfer equation relating diffuse reflectance to absorption ($K$) and scattering ($S$).
- **Cited In**: `research/02_remote_sensing_spectroscopy.md`

### 24. Mallarino (2003)
- **Citation**: Mallarino, A. P. (2003). Field calibration for corn of the Mehlich-3 soil phosphorus test with colorimetric and inductively coupled plasma emission spectroscopy determination methods. *Soil Science Society of America Journal*, 67(6), 1928–1934.
- **DOI**: [10.2136/sssaj2003.1928](https://doi.org/10.2136/sssaj2003.1928)
- **Key Findings**: Evaluates ICP-OES vs. colorimetric determination of Mehlich-3 extractable phosphorus, proving ICP measures organic P fractions dissolved by the acid.
- **Cited In**: `research/01_soil_science_fundamentals.md`

### 25. Mehlich (1984)
- **Citation**: Mehlich, A. (1984). Mehlich 3 soil test extractant: A modification of Mehlich 2 extractant. *Communications in Soil Science and Plant Analysis*, 15(12), 1409–1416.
- **DOI**: [10.1080/00103628409367568](https://doi.org/10.1080/00103628409367568)
- **Key Findings**: Seminal formulation of the universal Mehlich-3 multielement soil test extractant (0.2 M CH₃COOH + 0.25 M NH₄NO₃ + 0.015 M NH₄F + 0.013 M HNO₃ + 0.001 M EDTA).
- **Cited In**: `research/01_soil_science_fundamentals.md`, `knowledge/soil_nutrient_domain.md`

### 26. Olsen et al. (1954)
- **Citation**: Olsen, S. R., Cole, C. V., Watanabe, F. S., & Dean, L. A. (1954). *Estimation of Available Phosphorus in Soils by Extraction with Sodium Bicarbonate*. Circular No. 939, USDA, Washington, D.C.
- **Key Findings**: Establishes $0.5\text{ M } \text{NaHCO}_3$ (pH 8.5) extraction for plant-available phosphorus in calcareous soils (standard in European LUCAS survey).
- **Cited In**: `research/01_soil_science_fundamentals.md`, `knowledge/soil_nutrient_domain.md`

### 27. Pennsylvania Department of Environmental Protection (PA DEP) (2014)
- **Citation**: PA DEP. (2014). *Land Application of Manure: A Supplement to Manure Management for Environmental Protection*. Document No. 361-0300-001. Bureau of Point and Non-Point Source Management, Harrisburg, PA.
- **Key Findings**: Establishes mandatory 3-year soil testing rules under Chapter 91 for Pennsylvania farms applying animal manure at agronomic rates.
- **Cited In**: `research/05_agronomy_regulatory_context.md`

### 28. Pennsylvania Department of Environmental Protection (PA DEP) (2019)
- **Citation**: PA DEP. (2019). *Agricultural Erosion and Sediment Control Plan (Ag E&S Plan) Manual*. Document No. 383-0800-001. Bureau of Clean Water, Harrisburg, PA.
- **Key Findings**: Defines statutory compliance requirements under 25 Pa. Code Chapter 102. Ag E&S plans strictly regulate soil erosion and sediment loss ($T$ value), requiring zero documentation of soil N/P/K nutrient levels.
- **Cited In**: `research/05_agronomy_regulatory_context.md`, `research/07_gap_analysis_v1_vs_literature.md`

### 29. Pennsylvania State Conservation Commission (SCC) (2021)
- **Citation**: SCC. (2021). *Pennsylvania Nutrient Management Program Technical Manual*. Pennsylvania Department of Agriculture, Harrisburg, PA.
- **Key Findings**: Official technical manual for Act 38 compliance, codifying soil testing standards, certified laboratory qualifications, and PA Phosphorus Index Version 2 implementation.
- **Cited In**: `research/05_agronomy_regulatory_context.md`

### 30. Penn State Extension (2023)
- **Citation**: Penn State Extension. (2023). *The Penn State Agronomy Guide 2023–2024*. College of Agricultural Sciences, The Pennsylvania State University, University Park, PA.
- **Key Findings**: Official Pennsylvania university extension fertility guide, detailing crop nutrient removal rates, soil test interpretation categories, and fertilizer recommendation mathematics.
- **Cited In**: `research/01_soil_science_fundamentals.md`, `research/05_agronomy_regulatory_context.md`

### 31. Sharpley et al. (2001)
- **Citation**: Sharpley, A. N., McDowell, R. W., & Kleinman, P. J. A. (2001). Phosphorus loss from land to water: integrating agricultural and environmental issues. *Plant and Soil*, 237(2), 287–307.
- **DOI**: [10.1023/A:1013335814593](https://doi.org/10.1023/A:1013335814593)
- **Key Findings**: Demonstrates that >90% of agricultural phosphorus export occurs via surface particulate runoff and erosion rather than leaching.
- **Cited In**: `research/01_soil_science_fundamentals.md`

### 32. Sharpley (2003)
- **Citation**: Sharpley, A. N. (2003). Soil mixing to decrease surface stratification of phosphorus in manured soils. *Journal of Environmental Quality*, 32(4), 1375–1384.
- **DOI**: [10.2134/jeq2003.1375](https://doi.org/10.2134/jeq2003.1375)
- **Key Findings**: Quantifies exponential vertical stratification of phosphorus and organic carbon in no-till topsoils ($0–2\text{ cm}$ vs. $0–15\text{ cm}$).
- **Cited In**: `research/01_soil_science_fundamentals.md`

### 33. Soriano-Disla et al. (2014)
- **Citation**: Soriano-Disla, J. M., Janik, L. J., Viscarra Rossel, R. A., Macdonald, L. M., & McLaughlin, M. J. (2014). The performance of visible, near-, and mid-infrared reflectance spectroscopy for prediction of soil physical, chemical, and biological properties: A review. *Applied Spectroscopy Reviews*, 49(2), 139–186.
- **DOI**: [10.1080/05704928.2013.811081](https://doi.org/10.1080/05704928.2013.811081)
- **Key Findings**: Landmark meta-analysis of >100 spectroscopy studies. Classifies Total Nitrogen into Category 1 (Direct absorption; median $R^2 = 0.81$, RPD > 1.8); classifies Available P and K into Category 3 (Indirect/poor; median $R^2 = 0.34$ and $0.38$, RPD < 1.4).
- **Cited In**: `research/01_soil_science_fundamentals.md`, `research/02_remote_sensing_spectroscopy.md`, `research/07_gap_analysis_v1_vs_literature.md`

### 34. Stenberg et al. (2010)
- **Citation**: Stenberg, B., Viscarra Rossel, R. A., Mouazen, A. M., & Wetterlind, J. (2010). Visible and near infrared spectroscopy in soil science. *Advances in Agronomy*, 107, 163–215.
- **DOI**: [10.1016/S0065-2113(10)07005-7](https://doi.org/10.1016/S0065-2113(10)07005-7)
- **Key Findings**: Comprehensive breakdown of electronic vs. vibrational transitions in soil science. Explains the physics of fundamental O-H, C-H, N-H vibrations and why ionic species lack VNIR signals.
- **Cited In**: `research/01_soil_science_fundamentals.md`, `research/02_remote_sensing_spectroscopy.md`, `research/07_gap_analysis_v1_vs_literature.md`

### 35. Vaudour et al. (2021)
- **Citation**: Vaudour, E., Gholizadeh, A., Castaldi, F., Saberioon, M., Borůvka, L., Urbina-Salazar, D., ... & van Wesemael, B. (2021). Tellus S2: A global composite of Sentinel-2 topsoil spectral reflectance. *Remote Sensing*, 13(11), 2184.
- **DOI**: [10.3390/rs13112184](https://doi.org/10.3390/rs13112184)
- **Key Findings**: Methodology for building multi-temporal bare-soil composites using Sentinel-2 L2A data, establishing filtering criteria (NDVI < 0.25, NBR2 < 0.15) and medoid aggregation to isolate pure soil pixels.
- **Cited In**: `research/02_remote_sensing_spectroscopy.md`, `research/07_gap_analysis_v1_vs_literature.md`

### 36. Weld et al. (2002)
- **Citation**: Weld, J. L., Beegle, D. B., Gburek, W. J., Kleinman, P. J. A., & Sharpley, A. N. (2002). *The Pennsylvania Phosphorus Index: Version 1*. College of Agricultural Sciences, The Pennsylvania State University, University Park, PA.
- **Key Findings**: Mathematical development and field validation of the Pennsylvania P-Index risk screening tool for agricultural watersheds.
- **Cited In**: `research/05_agronomy_regulatory_context.md`

### 37. Xie et al. (2012)
- **Citation**: Xie, X. L., Parent, L. E., & Leblanc, M. (2012). Predicting soil phosphorus-related properties using near-infrared reflectance spectroscopy. *Soil Science Society of America Journal*, 76(5), 1769–1777.
- **DOI**: [10.2136/sssaj2012.0155](https://doi.org/10.2136/sssaj2012.0155)
- **Key Findings**: Empirical evaluation of NIRS across 448 soil samples. Proves Mehlich-3 P and exchangeable K cannot be predicted accurately ($R^2 < 0.70$, $\text{RPD} < 1.75$), whereas Total P is only moderately predictable due to covariance with Soil Organic Carbon.
- **Cited In**: `research/01_soil_science_fundamentals.md`

### 38. Žížala et al. (2022)
- **Citation**: Žížala, D., Minařík, R., & Skála, J. (2022). Soil organic carbon mapping using Sentinel-2 and Landsat 8 data: Open soil composite and multi-temporal bare soil approach. *Remote Sensing*, 14(14), 3326.
- **DOI**: [10.3390/rs14143326](https://doi.org/10.3390/rs14143326)
- **Key Findings**: Demonstrates that multi-temporal bare-soil composites outperform single-date satellite acquisitions for digital soil mapping in temperate croplands.
- **Cited In**: `research/02_remote_sensing_spectroscopy.md`, `research/07_gap_analysis_v1_vs_literature.md`
