# TerraScan Data Directory & Provenance Protocol

_Last updated: 2026-09-05 · Status: Standard Operating Protocol_

## Directory Structure
- `raw/`: Unaltered, pristine raw data files downloaded directly from upstream repositories (LUCAS Topsoil 2018, USDA SoilGrids/SSURGO, Sentinel-2 L2A tile exports). Files here must never be edited manually.
- `processed/`: Derived, cleaned, spatially indexed, and feature-engineered datasets ready for modeling pipelines.

## Provenance Tracking Requirements (Standing Rule)
Every dataset ingested or created must be documented with:
1. **Source & Version**: Upstream repository identifier (e.g., ESDAC LUCAS 2018 Topsoil Module, Copernicus Sentinel-2 MSI L2A).
2. **Geographic Coverage**: Latitude/longitude bounding box, spatial projection (CRS/EPSG), and specific countries/states covered.
3. **Temporal Alignment**: Date range of ground-truth sample collection vs. Sentinel-2 cloud-free acquisition window (must enforce seasonal/phenological alignment).
4. **Laboratory Ground-Truth Protocols**:
   - Nitrogen: Total N via dry combustion (ISO 10694) or Kjeldahl ($g/kg$ or $mg/kg$).
   - Phosphorus: Extractable P via Mehlich-3, Olsen, or Bray-1 ($mg/kg$).
   - Potassium: Extractable K via ammonium acetate (NH₄OAc) or Mehlich-3 ($mg/kg$).
5. **Spatial Autocorrelation Partitioning**: Definition of spatial buffer or spatial block cross-validation (e.g., spatial k-fold / BlockCV) to eliminate spatial leakage between training and evaluation splits.
