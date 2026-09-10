# Official ISEF / Regeneron STS Research Abstract

**Project Title**: TerraScan v2: Physics-Guided Neural Operators and In-Situ Multi-Spectral Rover Sensing for High-Resolution Field-Scale Agricultural Soil Nutrient Quantification

**Student Researcher**: Aarush Muthukrishnan  
**School**: North Allegheny Intermediate High School, Pittsburgh, PA  
**Competition Category**: Computational Biology and Bioinformatics (CBIO) / Earth and Environmental Sciences (EAEV) / Robotics and Intelligent Machines (ROBO)  
**Target Venues**: Regeneron Science Talent Search (STS) / International Science and Engineering Fair (ISEF)

---

### Official Abstract Text (Word Count: 244 words)

Small-scale agricultural producers lack cost-effective methods for intra-field soil nutrient mapping, leading to uniform fertilizer applications that exacerbate estuarine hypoxia in watersheds like the Chesapeake Bay. While satellite remote sensing offers wide coverage, direct optical estimation of available Phosphorus (P) and Potassium (K) fails because monoatomic K⁺ possesses zero infrared vibrational modes and orthophosphate fundamental stretching occurs strictly in the thermal infrared ($9\text{--}11\text{ }µm$). 

To overcome these physical barriers, TerraScan v2 introduces an anchor-calibrated multimodal system fusing multi-temporal Sentinel-2 bare-soil medoids with an autonomous field rover. The rover deploys a light-shielded 18-channel optical sensor (410–940 nm), active halogen illumination, and a concurrent moisture probe, calibrated against a 99% diffuse reflectance standard. A 2D Fourier Neural Operator (FNO) models spatial nutrient fields, regularized by a physics-guided loss encoding 2D advection-dispersion solute transport PDEs, mass conservation, vertical depth decay ($C(z) = C_0 e^{-\beta z}$), and statutory laboratory composite constraints. 

The neural operator architecture, physics loss, and split conformal calibrator have been implemented and unit-tested in code. Quantitative validation via 5-fold Spatial Block Cross-Validation (5 km buffer) is established as the empirical protocol, targeting $R^2 > 0.70$ (Total Nitrogen) and $R^2 > 0.65$ (Available Phosphorus and Potassium) based on peer-reviewed benchmarks. Integrated Split Conformal Prediction is formulated to deliver distribution-free 90% confidence intervals for every 10-meter pixel upon field dataset ingestion. TerraScan v2 provides the computational framework to transform standard $12 compliance tests into actionable Variable Rate prescription maps, bridging precision agriculture and environmental conservation.
