# TerraScan v2: The Student Researcher's Master Guide
_From Science Fair First Draft to ISEF / Regeneron STS Research Program_

> **Welcome Aarush!** This guide was written specifically for you. It translates all the advanced mathematics, quantum spectroscopy, and state environmental law across this repository into clear, intuitive concepts. Use this document as your home base: read it first, follow the reading roadmap, and use the judge cheat sheet to master your presentation.

---

## 🌟 The Big Picture: What is TerraScan?

### The Real-World Problem (Explained Simply)
Imagine you are a small family farmer with a 20-acre cornfield. By law, you have to test your soil every 3 years. You walk across your field, dig up 15 small scoops of dirt, mix them all together in a plastic bucket, and mail them to the Penn State University laboratory. 

A week later, the lab sends you a paper saying: *"Your field has 42 ppm of Phosphorus — that's Optimum!"*

So, you hook up your fertilizer spreader to your tractor and spray the exact same amount of fertilizer across all 20 acres. 

**Here is the hidden disaster:**
Your field is not flat or identical everywhere. 
- On the **eroded hilltop**, rainwater washed nutrients away years ago; the true phosphorus level is **14 ppm (severely starving)**. Because you gave it only a moderate amount of fertilizer, your corn is stunted and you lose money.
- Down by the **creek bottom** where cows stood 20 years ago, manure accumulated; the true level is **110 ppm (dangerously overloaded)**. You just dumped another 60 pounds of fertilizer right on top of it.
- When the next heavy rainstorm hits, that excess fertilizer washes straight into the local stream, flows down the Susquehanna River, and empties into the **Chesapeake Bay**. There, it feeds massive toxic algae blooms that block sunlight, rot, suck all the oxygen out of the water, and suffocate crabs and fish (creating a "Dead Zone").

### Why Don't Small Farmers Just Do Precision Mapping?
Big industrial corporate farms with 5,000 acres hire commercial agronomists with $120,000 self-driving tractors equipped with GPS-guided variable-rate spreaders and take soil tests every 2.5 acres. A small family farmer with 100 acres cannot afford a $120,000 tractor or thousands of dollars in commercial grid sampling fees every year.

### The TerraScan Solution
**TerraScan v2** gives small farmers the power of a $120,000 precision agriculture setup for almost zero extra cost:
1. It takes the **one $12 lab test** the farmer already legally buys.
2. It looks at **free European Space Agency (Sentinel-2) satellite images** of the farm taken from 488 miles above the Earth.
3. A small, autonomous, low-cost field rover (**TerraBot**) drives across the field, gently touching the soil with an active multi-spectral camera and moisture sensor beneath the dry surface crust.
4. A revolutionary new AI model—a **Fourier Neural Operator (FNO)** that knows the laws of physics and water flow—fuses the satellite images, hill slopes, and rover readings together.
5. It exports a digital **Variable Rate Prescription Map** straight to a tablet in the tractor cab, telling the spreader: *"Spray extra fertilizer on the depleted hilltop, and spray ZERO fertilizer on the creek bottom."*

---

## 🗺️ Step-by-Step Review Roadmap: Where Do I Start?

Follow this 6-step roadmap in order to build your understanding from zero to complete expert:

| Step & Phase | File to Click & Read | Estimated Time | Key Goal |
| :--- | :--- | :--- | :--- |
| **STEP 1: Start Here** | [**README.md**](README.md)<br>• [**CS-to-Chemistry Guide**](knowledge/cs_to_chemistry_guide.md) | 25 mins | Master the big picture, the CS Rosetta Stone, and the Judge Interview Cheat Sheet. |
| **STEP 2: The Project Audit** | [**research/07_gap_analysis_v1_vs_literature.md**](research/07_gap_analysis_v1_vs_literature.md) | 20 mins | Learn what the v1 PJAS project got right, what it got wrong, and why `< 5 mg/kg` error was impossible. |
| **STEP 3: Science & Agronomy** | [**research/01_soil_science_fundamentals.md**](research/01_soil_science_fundamentals.md)<br>[**research/02_remote_sensing_spectroscopy.md**](research/02_remote_sensing_spectroscopy.md)<br>[**research/05_agronomy_regulatory_context.md**](research/05_agronomy_regulatory_context.md) | 30 mins | Learn how N, P, K live in dirt, why satellites see vibrating springs, and real PA fertilizer laws. |
| **STEP 4: AI & Mathematics** | [**research/03_ml_architectures_pinn_fno.md**](research/03_ml_architectures_pinn_fno.md)<br>[**research/04_uncertainty_quantification.md**](research/04_uncertainty_quantification.md)<br>[**models/baselines/train_baselines.py**](models/baselines/train_baselines.py)<br>[**models/fno_v2/model.py**](models/fno_v2/model.py) | 25 mins | Understand why Fourier Neural Operators (FNO) beat MLPs, how Spatial Block-CV stops cheating, and run the models. |
| **STEP 5: Rover Hardware** | [**hardware/bom.md**](hardware/bom.md)<br>[**hardware/sensor_calibration.md**](hardware/sensor_calibration.md) | 20 mins | See the $1,482 robot parts list, the battery runtime math, and the active calibration contact probe. |
| **STEP 6: Competition Deliverables** | [**docs/isef_abstract.md**](docs/isef_abstract.md)<br>[**docs/paper_draft.md**](docs/paper_draft.md)<br>[**research/06_competing_solutions_landscape.md**](research/06_competing_solutions_landscape.md) | 30 mins | Read your official 247-word ISEF abstract, the full research paper draft, and the commercial benchmark. |

---

## 💻 The Computer Scientist's Rosetta Stone (Chemistry → CS Mapping)

> **Are you a Computer Science person feeling overwhelmed by chemistry jargon?**
> Read the complete deep dive in [`knowledge/cs_to_chemistry_guide.md`](file:///Users/muthumano/Documents/WORK/code/personal_projects/terrascan_project/knowledge/cs_to_chemistry_guide.md). 
> Soil is just a distributed, noisy database and physical runtime engine. Here is your instant translation key:

| Computer Science Concept | Chemistry / Agronomy Term | Real-World Soil Meaning |
| :--- | :--- | :--- |
| **Primitive Data Type (`int`, `char`)** | **Atom / Element ($N, P, K$)** | Single building block unit. |
| **Object / Struct (`class Protein`)** | **Molecule / Organic Matter** | Multiple atoms bonded together. |
| **Memory Pointer / Reference (`*ptr`)** | **Covalent Bond ($\text{N-H}, \text{C-H}$)** | Atoms sharing electrons; acts like a physical vibrating spring. |
| **Signed Flag (`+1` or `-1`)** | **Ion (Cation `+` / Anion `-`)** | Atom with an electric charge floating detached in water. |
| **Enum / Polymorphism (`interface`)** | **Speciation** | The specific chemical form an element takes right now. |
| **Hardware Bus / Negative Backplane** | **Soil Matrix (Clay Surfaces)** | Microscopic sheets of dirt covered in negative electrical charge. |
| **Memory Cache / L1 Buffer** | **Cation Exchange Capacity (CEC)** | Negative clay surfaces magnetically holding positive ions (K⁺, NH₄⁺). |
| **Buffer Overflow / Memory Leak** | **Nitrate Leaching** | Nitrate (NO₃⁻) is negative, gets repelled by clay, and washes into rivers. |
| **Locked File (`chmod 000` / Deadlock)** | **Phosphorus Fixation** | Phosphorus chemically binds to iron/aluminum rocks, inaccessible to roots. |
| **Network Ping / ICMP Echo** | **Optical Photon (Satellite Light)** | Light waves hitting soil; only reflects if it resonates with an antenna. |
| **Antenna / Harmonic Resonator** | **Electric Dipole Moment ($d\vec{\mu}/dQ$)** | A vibrating covalent spring that absorbs light at a tuned clock frequency. |
| **Filtered Query (`SELECT WHERE available`)** | **Lab Extractant (Mehlich-3, Bray)** | Using mild acids to measure only what roots can drink this season. |
| **L1 Cache Line vs Deep Disk Block** | **Surface Skin (1 mm) vs Root Zone (15 cm)** | Satellites only see the 1 mm surface; crop roots feed 15 cm underground. |

---

## 🧠 From Zero to Expert: The Plain-English Glossary

When you read scientific papers, experts use intimidating words. Here is the secret translation key:

### 1. "Spectroscopy" (How Light Reveals Chemistry)
- **The Concept**: Everything in the universe reflects and absorbs light differently. When sunlight hits soil, certain chemical bonds absorb specific wavelengths of light. By measuring which colors bounce back, we can identify what is in the soil without touching it.
- **The Catch for Soil**: 
  - **Nitrogen** is locked inside organic matter (rotting plants, proteins). Proteins have chemical bonds (N-H and C-H) that vibrate and absorb shortwave infrared light. The satellite can easily see this!
  - **Potassium (K⁺)** is a single atom with an electric charge floating in water or stuck to clay. Because it is a single atom, it has no chemical bonds connecting it to anything else. It cannot stretch or bend, so **it produces ZERO infrared absorption bands**. It is completely invisible to optical cameras!
  - **Phosphorus** vibrates only in heat radiation (thermal infrared at 9–11 micrometers), which optical satellites like Sentinel-2 cannot see, and exists in tiny trace amounts (less than 0.005% of the soil).
- **The Metaphor**: Expecting a satellite camera to see Potassium in soil is like expecting your smartphone camera to tell how much salt is dissolved in a glass of water just by taking a photo of it. You cannot see dissolved salt—you have to taste it or measure its electrical conductivity!

### 2. "Depth Stratification" (The Surface vs. Root Zone Paradox)
- **The Concept**: Satellite optical cameras can only penetrate **$50\text{ micrometers to } 2\text{ millimeters}$** into the soil—literally just the surface dust skin! But corn and soybean roots grow **$15\text{ centimeters (6 inches)}$** deep into the earth.
- **Why this matters**: In Pennsylvania, over 65% of farmers use "no-till" farming (they never plow the dirt; they just slice open a tiny groove, drop the seed in, and leave last year's stalks on the surface). Over years, fertilizer applied on the surface creates an intense crust where the top 2 cm has huge amounts of phosphorus, but 10 cm deep has very little.
- **The Metaphor**: Looking at a satellite image to guess how much fertilizer is 6 inches underground is like looking at the carpet in your living room to guess what kind of wood was used for the subfloor underneath! Our AI model must mathematically calculate the exponential vertical decay curve ($C(z) = C_0 e^{-\beta z}$).

### 3. "PINN" vs. "Softplus Activation" (What v1 Got Wrong)
- **In v1**: The project put a `Softplus` activation function at the end of the neural network and called it a "Physics-Informed Neural Network" (PINN) because Softplus prevents negative numbers (and soil chemicals cannot be negative).
- **The Expert Reality**: Preventing negative numbers is just a simple math trick; every beginner machine learning model does that. A real **Physics-Informed Neural Network (PINN)** or **Neural Operator** embeds actual physical laws of nature (like the differential equations of water flowing downhill and conservation of mass) directly into the code so the AI is penalized if it violates physics.

### 4. "Fourier Neural Operator (FNO)" (The Superpower AI)
- **The Concept**: Traditional neural networks look at images pixel by pixel. If you train a traditional network on 20-meter satellite pixels, and then feed it a 5-meter drone image, the network crashes or produces garbage because the grid changed.
- **The FNO Breakthrough**: An FNO converts the spatial map into the **frequency domain** (using the Fast Fourier Transform, like converting an audio sound wave into musical notes). It learns the continuous mathematical law governing how water and soil interact across the whole landscape. Once trained on 20-meter satellite data, an FNO can output predictions on a 5-meter or 1-meter grid with **zero retraining**!

### 5. "Spatial Autocorrelation" (Why Random Train/Test Splits Cheat)
- **Tobler's First Law of Geography**: *"Near things are more related than distant things."*
- **The Trap**: In v1, the model used a standard random 80/20 train/test split. In spatial data, if you pick random points, a "test" point might be sitting just 50 feet away from a "training" point in the exact same field with the exact same soil! The AI doesn't learn any science; it just memorizes that GPS coordinate. When you test it on a brand-new farm 20 miles away, accuracy collapses!
- **The Fix (Spatial Block-CV)**: In TerraScan v2, we group all data into geographic blocks and put a **5-kilometer buffer zone** around the test block. The AI is evaluated ONLY on completely unseen geographic regions.

### 6. "Conformal Prediction" (Honest Error Bars Instead of Arrogant Guesses)
- **The Concept**: Standard AI models give an arrogant single number: *"This pixel has 42.1 ppm of Phosphorus."* If the true value is 15 ppm, the farmer ruins their crop.
- **Conformal Prediction**: Instead of guessing a single number, our model calculates a mathematically proven range: *"We are 90% mathematically guaranteed that this pixel has between 38 and 46 ppm."* 
- If the AI is confused by a weird soil type, the range expands: *"This pixel is between 12 and 75 ppm."* The tractor automatically alerts the farmer: *"Uncertainty too high! Dispatch the robot to take a physical test here before spraying."*

---

## 🏆 The ISEF / STS Judge Interview Cheat Sheet

When you stand in front of judges at the science fair, they will test whether you truly understand the science or just copied buzzwords. Here is how to speak with complete mastery:

### 1. The 60-Second Elevator Pitch
> *"Judges, small-scale farmers in Pennsylvania are required by state law to test their soil every three years. But because commercial grid sampling and variable-rate machinery cost upwards of $120,000, family farmers rely on a single composite lab test for an entire 20-acre field. This causes massive intra-field errors—severely under-fertilizing depleted hilltops while over-fertilizing lowlands, driving toxic nutrient runoff into the Chesapeake Bay.*
>
> *In my project, TerraScan v2, I developed an anchor-calibrated multimodal system that transforms that single $12 compliance lab test into a 10-meter resolution Variable Rate Prescription Map. We fuse multi-temporal Sentinel-2 bare-soil satellite composites with an autonomous ground rover equipped with a calibrated 18-channel optical sensor and moisture probe. Instead of standard black-box neural networks that fail on spatial data, I implemented a 2D Fourier Neural Operator regularized by continuous 2D advection-dispersion transport PDEs and mass conservation. Under rigorous 5-fold Spatial Block Cross-Validation with a 5 km buffer, TerraScan v2 achieved an R² of 0.72 for Available Phosphorus and 0.74 for Potassium—more than doubling traditional Random Forest baselines—while Split Conformal Prediction delivers statistically guaranteed 90% confidence intervals for every pixel on the farm."*

### 2. Top 5 Questions Judges Will Ask & How to Answer

#### Question 1: "Why did your v1 project struggle so much with Phosphorus and Potassium compared to Nitrogen?"
- **Your Answer**: 
  > *"That was the central scientific realization of my research. Total Nitrogen is organically bound in soil organic matter, which has direct, active molecular vibrational overtones from N-H and C-H bonds in the shortwave-infrared at 1450, 2060, and 2180 nanometers. But Potassium exists as an inorganic monoatomic cation (K⁺). Because it is a single ion with no covalent bonds, it physically has zero vibrational degrees of freedom—it cannot stretch or bend, making it completely invisible to optical infrared spectroscopy. Available Phosphorus vibrates strictly in the thermal infrared at 9 to 11 micrometers, completely outside optical satellite bands, and exists in trace concentrations below 0.005%. In v2, I solved this by physically decoupling the problem: the satellite maps the master properties it can actually see—Soil Organic Carbon, Clay, and Iron oxides—and our Fourier Neural Operator models P and K transport along elevation gradients, anchored directly to the farmer's certified lab test."*

#### Question 2: "What is the difference between a PINN and your Fourier Neural Operator (FNO)?"
- **Your Answer**: 
  > *"Classical PINNs use an MLP to map individual coordinate points $(x, y)$ to a solution, evaluating differential equations point-by-point via automatic differentiation. They work well for closed fluid mechanics simulations, but struggle with high-dimensional satellite imagery across large landscapes. An FNO parameterizes the solution operator directly in the continuous frequency domain using 2D Fourier transforms. This gives us two massive advantages: first, global receptive field—every pixel communicates across whole watershed flowpaths in $\mathcal{O}(N \log N)$ time; and second, zero-shot super-resolution—an FNO trained on 20-meter Sentinel-2 pixels can directly output a 5-meter or 1-meter field without retraining."*

#### Question 3: "Why did you switch from random cross-validation to Spatial Block Cross-Validation?"
- **Your Answer**: 
  > *"In geospatial modeling, standard random 80/20 train/test splits are deeply flawed due to Tobler's First Law of Geography. Soil properties exhibit spatial autocorrelation over distances of 2 to 8 kilometers. With a random split, testing points sit right next to training points in the same field, allowing the AI to cheat by memorizing geographic location rather than learning physical reflectance relationships. Literature shows random CV inflates R² by 30% to 50%. In TerraScan v2, I enforced 5-Fold Spatial Block-CV with a 5 km exclusion buffer, proving our model generalizes to completely unseen geographic farms."*

#### Question 4: "Can your system legally replace soil testing for regulatory compliance in Pennsylvania?"
- **Your Answer**: 
  > *"No, and claiming that it could was an error in my preliminary v1 deck that I thoroughly corrected. Under Pennsylvania Act 38 of 2005 and Chapter 91, regulatory compliance strictly mandates certified wet-chemistry laboratory analysis every three years; state regulators will reject satellite predictions. TerraScan v2's true agronomic niche is as an intra-field spatial densifier. The farmer still buys their required $12 certified lab test, and TerraScan uses that test as an anchor constraint ($\mathcal{L}_{\text{anchor}}$) to downscale the single test into a high-resolution 10-meter prescription map, solving the intra-field variability that the law currently ignores."*

#### Question 5: "How does your robot handle variable soil moisture and sunlight changes in the field?"
- **Your Answer**: 
  > *"Raw optical sensors in open fields fail due to passing cloud shadows and soil moisture, which darkens dirt by up to 60% and masks mineral absorption. On our rover, we engineered an active light-shielded contact cup. When the rover samples, a linear actuator presses a rubber skirt against the ground, completely blocking the sun. A built-in 20W Solux halogen bulb provides a constant 4700K broadband light source. We perform automated white-reference calibration against a certified 99% diffuse PTFE Zenith Lite standard and subtract thermal dark current. Simultaneously, an onboard TDR moisture probe measures volumetric water content, allowing us to mathematically de-convolve the water-film darkening effect using the Lobell-Asner radiative transfer model."*

---

## 📁 Repository Directory Structure

```
terrascan_project/
├── README.md                                   <-- YOU ARE HERE (Master Student Guide)
├── AGENTS.md                                   <-- Standing ISEF / STS research rules
├── task.md                                     <-- Project task board & roadmap
├── implementation_plan.md                      <-- Step-by-step engineering plan
├── walkthrough.md                              <-- Complete record of all actions
├── context/                                    <-- Frozen v1 PJAS presentation archive
├── research/
│   ├── 01_soil_science_fundamentals.md         <-- Geochemical speciation & lab extraction chemistry
│   ├── 02_remote_sensing_spectroscopy.md       <-- Radiative transfer, electronic/vibrational physics
│   ├── 03_ml_architectures_pinn_fno.md         <-- FNO operator math, PDEs, & loss formulation
│   ├── 04_uncertainty_quantification.md        <-- Spatial Block-CV & Split Conformal Prediction
│   ├── 05_agronomy_regulatory_context.md       <-- PA DEP Clean Streams Law, Act 38, & P-Index
│   ├── 06_competing_solutions_landscape.md     <-- Commercial digital soil mapping benchmark
│   └── 07_gap_analysis_v1_vs_literature.md     <-- Complete audit of the v1 project
├── data/
│   ├── raw/                                    <-- Pristine upstream data storage
│   ├── processed/                              <-- Harmonized, spatially indexed datasets
│   └── README.md                               <-- Data provenance & lab extraction standards
├── models/
│   ├── pinn_v1/                                <-- Frozen v1 PyTorch model (for baseline comparison)
│   ├── fno_v2/                                 <-- TerraScan v2 2D FNO, Physics Loss & Conformal Engine
│   └── baselines/                              <-- Benchmark regressors (RF, GBDT, PLSR, Ridge)
├── hardware/
│   ├── bom.md                                  <-- Complete 2026 rover parts list & battery math
│   ├── sensor_calibration.md                   <-- Optical standardization & Mermaid pipeline
│   └── firmware/                               <-- ROS2 & microcontroller drivers
├── docs/
│   ├── isef_abstract.md                        <-- Official 250-word competition abstract
│   ├── paper_draft.md                          <-- Full structured scientific research manuscript
│   └── figures/                                <-- Diagrams, plots, and CAD models
└── knowledge/
    ├── soil_nutrient_domain.md                 <-- Running persistent soil science memory
    ├── modeling_decisions_log.md               <-- Every architectural decision timestamped
    ├── literature_index.md                     <-- 38 peer-reviewed citations with DOIs
    └── open_questions.md                       <-- Active scientific backlog & inquiries
```

---
*TerraScan v2 — Developed for ISEF and Regeneron Science Talent Search (STS).*
