# Open Questions & Investigation Backlog
_Last updated: 2026-09-06 · Status: Active Persistent Memory_

## Purpose
This document tracks every hypothesis, empirical contradiction, unverified claim, or technical challenge identified throughout the TerraScan v2 research program. Items remain flagged as "Open / In Investigation" until resolved with rigorous literature evidence or experimental proof, preventing premature conclusions.

---

## Inquiries & Resolution Status

### OQ-001: True Units and Processing of Nitrogen in the v1 LUCAS Dataset
- **Status**: RESOLVED
- **Resolution**: ESDAC LUCAS Topsoil 2018 database measures Total Nitrogen (TN) via high-temperature dry combustion (Dumas method, ISO 10694) in units of **g/kg** (mean ~2.5 g/kg across European croplands). Available P is measured via sodium bicarbonate (Olsen method) in **mg/kg**. Exchangeable K is measured via ammonium acetate in **mg/kg**. The v1 PJAS deck treated Total N values without unit conversion, leading to a reported MAE of 1.63 g/kg (which is 1,630 mg/kg, an enormous 65% relative error). TerraScan v2 harmonizes all datasets to standard agronomic units: Total N (g/kg), Available P ($\text{mg/kg Mehlich-3 equivalent}$ via $\text{M3P} \approx 2.05 \times \text{Olsen P}$), and Exchangeable K ($\text{mg/kg Mehlich-3 equivalent}$).

### OQ-002: Spatial Sampling Footprint & Bare Soil Filtering of the 628 Points
- **Status**: RESOLVED
- **Resolution**: The 628 points in v1 represented a single-date cloud-filtered subset where bare soil was not masked, leading to severe vegetation and residue contamination. In TerraScan v2, we implement multi-temporal bare-soil medoid compositing over a 3-year window (2021–2024) in Google Earth Engine using dual filtering ($\text{NDVI} < 0.25$ and $\text{NBR2} < 0.15$), generating continuous 10m bare-soil rasters.

### OQ-003: Physical Formulation of In-Situ AS7265x Proximal Sensor Fusion
- **Status**: RESOLVED
- **Resolution**: The AS7265x (410–940 nm) cannot directly measure ionic P or K, and circular label perturbation in v1 was invalid. In v2, the rover's in-situ probe is equipped with an active tungsten halogen light cup, an automated 99% diffuse PTFE calibration standard, and a concurrent TDR soil moisture sensor. The probe measures in-situ iron oxide absorption and soil organic darkening beneath the surface crust, de-convolving soil moisture. The FNO fuses these readings with satellite SWIR clay bands and DEM slope gradients, regularized by the certified laboratory anchor test ($\mathcal{L}_{\text{anchor}}$).

### OQ-004: Governing Transport PDE for Physics-Guided Operator Loss
- **Status**: RESOLVED
- **Resolution**: The continuous 2D advection-dispersion solute transport equation along topographic elevation gradients ($-\kappa \nabla z \cdot \nabla C - \mathbf{D} \nabla^2 C - R = 0$) has been mathematically formalized and integrated into `models/fno_v2/model.py` and `research/03_ml_architectures_pinn_fno.md`, alongside mass conservation and the exponential vertical depth-stratification operator ($C(z) = C_0 e^{-\beta z}$).
