# Implementation Plan: TerraScan v2 Research Program

## User Review Required
> [!IMPORTANT]
> Step 2 executes the Scientific Deep Dive across soil science fundamentals (`research/01`), remote sensing spectroscopy physics (`research/02`), and Pennsylvania regulatory/agronomic frameworks (`research/05`). It grounds TerraScan v2 in physical mechanisms and real compliance law, establishing the foundation for the ML architectures in Step 3.

## Proposed Plan of Action

### Phase 1: Setup and Baseline Freezing (COMPLETED)
- Established directory hierarchy and `AGENTS.md` operating standards.
- Initialized persistent memory in `knowledge/` (`soil_nutrient_domain.md`, `modeling_decisions_log.md`, `literature_index.md`, `open_questions.md`).
- Frozen v1 architecture and PJAS performance records in `models/pinn_v1/`.

### Phase 2: Step 1 — Audit the v1 Project against Literature (COMPLETED)
- Completed `research/07_gap_analysis_v1_vs_literature.md` benchmarking all 10 v1 claims against 23 peer-reviewed studies.
- Updated `knowledge/` base with spectroscopic physics of N, P, K and logged decisions MD-001 through MD-003.

### Phase 3: Step 2 — Scientific Deep Dive (ACTIVE)
- **Target Deliverables**:
  1. `research/01_soil_science_fundamentals.md`: Comprehensive breakdown of N, P, K chemical speciation, pool dynamics, wet chemistry laboratory extraction protocols (Mehlich-3, Bray-1, Olsen, Dumas/Kjeldahl, KCl) vs. optical sensor capabilities, and vertical depth-decay profiles.
  2. `research/02_remote_sensing_spectroscopy.md`: Rigorous radiative transfer physics (Kubelka-Munk, Hapke), electronic crystal field transitions (Fe³⁺) vs. molecular vibrational overtones/combinations ($\text{O-H}, \text{C-H}, \text{N-H}, \text{Al-OH}$), detailed Sentinel-2 MSI band-by-band information mapping, multi-temporal bare-soil compositing algorithms (GEOS3, SYSI, Barest Pixel), and fundamental physical limits (optical penetration depth, moisture masking, surface crusts).
  3. `research/05_agronomy_regulatory_context.md`: Pennsylvania agricultural regulatory statutes (25 Pa. Code Chapter 102 Ag E&S vs. Act 38 / Chapter 91 Nutrient Management Plans), PA Phosphorus Index (P-Index) mechanics, Penn State Extension soil test calibration and agronomic interpretation tables (STP, STK), and positioning TerraScan v2 as an intra-field VRT spatial interpolator rather than a statutory test substitute.
- **Verification & Documentation**:
  - Update `knowledge/soil_nutrient_domain.md` and `knowledge/literature_index.md` with new citations and mechanisms.
  - Update `walkthrough.md` and provide the required Step 2 Learning Recap.

### Subsequent Phases
- Step 3: Computational/ML Deep Dive (`research/03`, `04`, `models/`)
- Step 4: Engineering Deep Dive (`hardware/`, data pipeline architecture)
- Step 5: Research Synthesis (`docs/isef_abstract.md`, `docs/paper_draft.md`)
