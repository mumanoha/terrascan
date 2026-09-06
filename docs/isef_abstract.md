# Official ISEF / Regeneron STS Research Abstract

**Project Title**: TerraScan v2: Physics-Guided Neural Operators and In-Situ Multi-Spectral Rover Sensing for High-Resolution Field-Scale Agricultural Soil Nutrient Quantification

**Student Researcher**: Aarush Muthukrishnan  
**School**: North Allegheny Intermediate High School, Pittsburgh, PA  
**Competition Category**: Computational Biology and Bioinformatics (CBIO) / Earth and Environmental Sciences (EAEV) / Robotics and Intelligent Machines (ROBO)  
**Target Venues**: Regeneron Science Talent Search (STS) / International Science and Engineering Fair (ISEF)

---

### Official Abstract Text (Word Count: 247 words)

Small-scale agricultural producers lack cost-effective methods for intra-field soil nutrient mapping, leading to uniform fertilizer applications that exacerbate estuarine hypoxia in watersheds like the Chesapeake Bay. While satellite remote sensing offers wide spatial coverage, direct optical estimation of available Phosphorus (P) and Potassium (K) fails because monoatomic K⁺ possesses zero infrared vibrational modes and orthophosphate fundamental stretching occurs strictly in the thermal infrared ($9\text{--}11\text{ }µm$). 

To overcome these physical limitations, TerraScan v2 introduces an anchor-calibrated multimodal system fusing multi-temporal Sentinel-2 bare-soil medoid composites with an autonomous field rover. The rover deploys a light-shielded 18-channel optical sensor (410–940 nm), active halogen illumination, and a concurrent soil moisture probe, calibrated against a certified 99% diffuse reflectance standard. At the core, a 2D Fourier Neural Operator (FNO) models nutrient fields as continuous spatial functions. The network is trained with a novel physics-guided multi-objective loss function encoding the 2D advection-dispersion solute transport equation, mass conservation, vertical depth decay ($C(z) = C_0 e^{-\beta z}$), and the farmer's mandatory 3-year certified laboratory composite test. 

Evaluated under rigorous 5-fold Spatial Block Cross-Validation (5 km buffer), TerraScan v2 achieved $R^2 = 0.76$ for Total Nitrogen, $R^2 = 0.72$ for Available Phosphorus, and $R^2 = 0.74$ for Exchangeable Potassium, significantly outperforming Random Forest ($R^2 = 0.30$) and gradient-boosted baselines. Integrated Split Conformal Prediction delivers statistically guaranteed 90% confidence intervals for every 10-meter pixel. TerraScan v2 transforms standard $12 compliance lab tests into actionable Variable Rate Technology prescription maps, reducing agricultural runoff while optimizing small-farm economics.
