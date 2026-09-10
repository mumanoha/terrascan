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

### Phase 3: Step 2 — Scientific Deep Dive (COMPLETED)
- Completed `research/01_soil_science_fundamentals.md`, `research/02_remote_sensing_spectroscopy.md`, and `research/05_agronomy_regulatory_context.md`.
- Completed `knowledge/cs_to_chemistry_guide.md` and updated `knowledge/` base.

### Phase 4: Step 3 — Computational & Machine Learning Deep Dive (COMPLETED)
- Completed `research/03_ml_architectures_pinn_fno.md`, `research/04_uncertainty_quantification.md`.
- Trained and verified `models/baselines/` and `models/fno_v2/`.

### Phase 5: Step 4 — Rover Hardware & Physical Schematics (ACTIVE)
- **Completed**:
  1. `hardware/bom.md`: Full 2026 BOM ($1,482) and power runtime analysis.
  2. `hardware/sensor_calibration.md`: 4-step optical standardization protocol.
  3. `docs/figures/02a_robot_cad_concept.md` & `.svg`: 3-view orthographic CAD blueprint, slope stability physics, 520 mm chassis packaging, and EPDM light-shield skirt.
- **Active Task**:
  4. `docs/figures/02b_robot_wiring.md` & `02b_robot_wiring.svg`: Complete internal electronics wiring diagram, pin-to-pin interconnects, voltage regulation, protection circuitry (fuses, TVS, flyback, reverse-polarity MOSFET), star-ground topology, power budget derivation, EMI mitigation, and updated 2026 BOM.

### Phase 6: Step 5 — Research Synthesis & Deliverables (COMPLETED / ACTIVE)
- Completed `docs/figures/01_system_overview.md`, `docs/isef_abstract.md`, `docs/paper_draft.md`, `research/06_competing_solutions_landscape.md`.
- Deployed on Google Cloud Run and GitHub Pages.
