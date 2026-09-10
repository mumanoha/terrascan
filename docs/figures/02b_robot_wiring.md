# TerraBot Rover: Electronics Architecture & Complete Interconnect Wiring Diagram
_Last updated: 2026-09-09 · Status: reviewed_

## TL;DR
This document provides the production-grade electrical and interconnect wiring schematic for the TerraBot v2 autonomous field rover. Operating from a 12.8V 20Ah ($256\text{ Wh}$) LiFePO4 battery recharged by a 50W semi-flexible solar panel via MPPT, the system employs multi-stage synchronous buck converters and an ultra-low-noise LDO to provide clean, isolated power rails (12.8V, 5.1V, 5.0V, and 3.3V). The Raspberry Pi 5 and Hailo-8L NPU communicate deterministically with sensors and actuators across dedicated I2C, SPI, UART, and RS-485 Modbus buses. Inductive motor noise is strictly isolated from sensitive optical photodiodes using an air-gapped star-ground topology, optocouplers, TVS clamp diodes, and LC filters.

---

## What we're trying to answer
1. How are all seven BOM subsystems physically wired to the Raspberry Pi 5 (and fallback NVIDIA Jetson Nano) across specific GPIO pins and communication buses (I2C, SPI, UART, RS-485)?
2. How is raw 12.8V battery power safely stepped down, regulated, and protected against reverse polarity, overcurrent faults, and inductive voltage spikes?
3. What is the rigorous component-by-component electrical power budget, and what is the exact mathematical runtime on a 256 Wh LiFePO4 battery under zero-solar and solar-recharged conditions?
4. How do we eliminate electromagnetic interference (EMI) and ground loops so the 15A motor switching noise does not corrupt the micro-amp photocurrents of the AS7265x 18-channel spectral sensor?
5. Why was the original PJAS $485 hardware estimate unviable, and what is the true itemized 2026 component cost ($1,481.80)?

---

## Complete System Wiring Schematic (Vector Architecture)

The vector schematic below illustrates the complete electrical interconnect, power distribution tree, pinout mapping, protection circuitry, and star-ground topology of the TerraBot v2 rover.

<p align="center">
  <img src="docs/figures/02b_robot_wiring.svg" alt="TerraBot v2 Electrical &amp; Interconnect Schematic" width="100%" style="background:#ffffff; border: 1px solid #E2E8F0; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);" />
</p>
<p align="center">
  <em>Figure 2B: TerraBot v2 Complete Electrical Interconnect Schematic (Drawing No. TB-ELEC-2026-02B). Color-coded wiring buses: Red (12.8V Power), Amber (5.0V/5.1V Regulated Bus), Purple (3.3V Logic/Sensor Rail), Green (I2C), Blue (UART), Orange (SPI), Pink (RS-485 Differential), Dashed Black (GND_PWR Dirty Ground), Solid Green (GND_LOGIC Clean Ground).</em>
</p>

---

## 1. Subsystem Interconnect & Pinout Mapping

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                               COMPLETE SUBSYSTEM INTERCONNECT REGISTER                                 │
├────────────────────┬──────────┬──────────────┬────────────┬─────────────┬──────────────────────────────┤
│ Subsystem / Device │ Interface│ Pi 5 Pins    │ Voltage    │ Logic Level │ Signal Integrity & Protection│
├────────────────────┼──────────┼──────────────┼────────────┼─────────────┼──────────────────────────────┤
│ Raspberry Pi 5 SBC │ Power In │ Pins 02, 04  │ 5.1 V DC   │ 3.3V Logic  │ 5A Polyfuse, TVS clamp diode │
│ Hailo-8L AI NPU    │ PCIe Gen3│ M.2 Hat Slot │ 3.3 V (PCI)│ 1.8V / 3.3V │ Direct 16-lane differential  │
│ AS7265x Spectrometer│ I2C1     │ Pins 03, 05  │ 3.3 V LDO  │ 3.3 V CMOS  │ 4.7 kΩ pull-ups, STP shielded│
│ u-blox ZED-F9P RTK │ UART0    │ Pins 08, 10  │ 5.0 V Aux  │ 3.3 V TTL   │ 100 Ω series damping, 460k bd│
│ Adafruit RFM95W    │ SPI0     │ 18,19,21,23,24│ 3.3 V Rail │ 3.3 V CMOS  │ 10µF Tant + 0.1µF decoupling │
│ TrueSoil TDR-100   │ RS-485   │ Pins 35,37,38│ 12.8 V DC  │ Diff A/B    │ SP3485 transceiver, SM712 TVS│
│ Roboteq Dual Driver│ PWM/DIR  │ 12,16,32,33  │ 12.8 V Fused│ 3.3 V Opto  │ 6N137 optocouplers, 20kHz PWM│
│ Solux Halogen 20W  │ Gate SW  │ Pin 13       │ 12.8 V Fused│ 3.3 V CMOS  │ IRLZ44N N-FET, 1N5819 flyback│
│ Linear Actuator    │ H-Bridge │ Pin 11       │ 12.8 V Fused│ 3.3 V Logic │ Polarity relay, limit switches│
└────────────────────┴──────────┴──────────────┴────────────┴─────────────┴──────────────────────────────┘
```

### Detailed Pin-by-Pin Wiring Breakdown

#### A. Raspberry Pi 5 Compute Core (Primary)
- **Power Input**: Powered via high-current synchronous buck converter feeding **5.1V at up to 5.0A (25.5W)** directly to GPIO **Pin 02 (`5V`)** and **Pin 04 (`5V`)**, or through the onboard USB-C PD controller. Pins 06, 09, 14, 20, 25, 30, 34, and 39 are tied to the clean logic ground plane (`GND_LOGIC`).
- **I2C1 Bus (Spectral Triad)**:
  - `SDA` connected to **Pin 03 (GPIO 2)**.
  - `SCL` connected to **Pin 05 (GPIO 3)**.
  - Hardwired external $4.7\text{ k}\Omega$ pull-up metal-film resistors tied to the clean $3.3\text{V}$ sensor rail to prevent bus capacitance rise-time degradation across long cable runs.
- **UART0 Serial (RTK-GNSS Primary Navigation)**:
  - `TXD` (Pi $\to$ GPS) on **Pin 08 (GPIO 14)** connected to ZED-F9P `RX1`.
  - `RXD` (GPS $\to$ Pi) on **Pin 10 (GPIO 15)** connected to ZED-F9P `TX1`.
  - Operating baud rate: $460,800\text{ bps}$, 8 data bits, no parity, 1 stop bit (8N1).
- **SPI0 Bus (LoRaWAN 915 MHz Telemetry)**:
  - `MOSI` on **Pin 19 (GPIO 10)**.
  - `MISO` on **Pin 21 (GPIO 09)**.
  - `SCLK` on **Pin 23 (GPIO 11)**.
  - `CE0 / NSS` on **Pin 24 (GPIO 08)**.
  - `DIO0` (Packet RX Interrupt) on **Pin 18 (GPIO 24)**.
  - `RESET` on **Pin 22 (GPIO 25)**.
- **Motor Control PWM & Direction**:
  - `PWM_L` (Left wheel bank speed) on **Pin 12 (GPIO 18 / PWM0)**.
  - `DIR_L` (Left direction) on **Pin 16 (GPIO 23)**.
  - `PWM_R` (Right wheel bank speed) on **Pin 33 (GPIO 13 / PWM1)**.
  - `DIR_R` (Right direction) on **Pin 32 (GPIO 12)**.
  - All four control lines feed into high-speed optocouplers ($6\text{N}137$) inside the motor driver enclosure, ensuring complete galvanic isolation between logic and power stages.
- **Soil Probe RS-485 Modbus Interface**:
  - `UART1_RXD` on **Pin 35 (GPIO 19)** connected to SP3485 Receiver Output (`RO`).
  - `UART1_TXD` on **Pin 37 (GPIO 26)** connected to SP3485 Driver Input (`DI`).
  - `RS485_DE_RE` on **Pin 38 (GPIO 20)** toggles the SP3485 half-duplex Driver Enable / Receiver Enable pins.
- **Actuation & Illumination Switches**:
  - `HALOGEN_GATE` on **Pin 13 (GPIO 27)** drives the gate of an IRLZ44N logic-level N-channel MOSFET through a $220\ \Omega$ series resistor with a $100\text{ k}\Omega$ pulldown resistor.
  - `ACTUATOR_TRIG` on **Pin 11 (GPIO 17)** actuates the lead-screw lowering relay.

#### B. NVIDIA Jetson Nano Alternative / Fallback Pinout Mapping
The NVIDIA Jetson Nano Developer Kit utilizes the identical 40-pin header layout, enabling drop-in physical harness compatibility:
* Jetson `Pin 03 (I2C1_SDA)` and `Pin 05 (I2C1_SCL)` operate at 3.3V.
* Jetson `Pin 08 (UART1_TXD)` and `Pin 10 (UART1_RXD)` match the GPS interface.
* Jetson `Pin 19, 21, 23, 24` match the SPI0 LoRa interface.
* Jetson `Pin 32 (PWM0)` and `Pin 33 (PWM1)` drive the motor PWM channels.
* **Performance Fallback Note**: The legacy Jetson Nano (EOL since 2023) delivers only $0.472\text{ TFLOPS FP16}$ (~0.5 TOPS INT8) while consuming $10\text{--}12\text{ W}$, whereas the Raspberry Pi 5 + Hailo-8L combination delivers **$26\text{ TOPS INT8}$ ($52\times$ AI inference throughput)** at only $2.5\text{ W}$. Jetson Nano is documented strictly as a legacy lower-cost fallback with reduced on-device inference capability.

---

## 2. Power Distribution & Protection Architecture

```
                                    CENTRAL POWER TOPOLOGY
                                              │
                      ┌───────────────────────┴───────────────────────┐
                      ▼                                               ▼
             50W Monocrystalline                             12.8V 20Ah LiFePO4
                 Solar Panel                                    Battery Bank
                      │                                               │
                      ▼                                               ▼
             Genasun MPPT 14.2V                             15A Master ATC Fuse
                      │                                               │
                      └───────────────────────┬───────────────────────┘
                                              │
                                              ▼
                                   Master E-Stop SPST (20A)
                                              │
                                              ▼
                                Reverse-Polarity Protection (IRF4905)
                                              │
                         ┌────────────────────┴────────────────────┐
                         ▼                                         ▼
                 12.8V DIRECT FUSED BUS                   STEP-DOWN CONVERTERS
           ┌─────────────┬─────────────┐                   ┌───────┴───────┐
           ▼             ▼             ▼                   ▼               ▼
      Motor Driver  Halogen Lamp   Actuator Probe     5V 5A Buck       5V 3A Buck
      (10A Fuse)    (3A Fuse+FET)  (3A Fuse+Relay)    (Pi 5 + NPU)     (RTK GPS+Servos)
                                                                           │
                                                                           ▼
                                                                     3.3V LDO (<4µV)
                                                                     (AS7265x Sensor)
```

### Circuit Protection & Safety Engineering
1. **Master Inline Overcurrent Fuse**:
   - A **$15\text{A}$ ATC automotive fast-acting blade fuse** is positioned $<8\text{ cm}$ from the battery positive terminal in a splash-proof inline holder. It protects against catastrophic battery short-circuits.
2. **Emergency Stop (E-Stop)**:
   - A heavy-duty $20\text{A}$ rated SPST push-lock/twist-release red mushroom button physically breaks the main positive conductor downstream of the primary fuse, allowing immediate manual system shutdown.
3. **Ideal Diode Reverse-Polarity Protection**:
   - Instead of a traditional Schottky diode (which would drop $0.5\text{--}0.7\text{ V}$ and dissipate $2\text{--}4\text{ W}$ of wasted heat), TerraBot uses an **IRF4905 P-Channel Power MOSFET** in an "ideal diode" circuit:
     - Drain connected to Battery Positive, Source connected to System Bus.
     - Gate pulled to Ground via a $100\text{ k}\Omega$ resistor and clamped with an internal $12\text{V}$ Zener diode ($1\text{N}4742\text{A}$) to prevent $V_{gs}$ gate puncture.
     - Under normal polarity, the MOSFET is fully enhanced ($R_{ds(on)} = 0.02\ \Omega$), producing a negligible voltage drop of only $V_{\text{drop}} = 2.0\text{ A} \times 0.02\ \Omega = \mathbf{0.04\text{ V}}$ ($0.08\text{ W}$ heat loss).
     - Under reverse polarity, $V_{gs} > 0$, immediately cutting off current and protecting all downstream silicon.
4. **Transient Voltage Suppression (TVS)**:
   - Bidirectional TVS diodes (Littelfuse SMBJ15CA, $15\text{V}$ standoff, $24\text{V}$ clamp) are placed across the $12\text{V}$ motor bus and the solar input to absorb lightning-induced field surges and inductive dump spikes.
5. **Inductive Flyback Clamping**:
   - The Solux halogen lamp and linear actuator relays are shunted with high-speed **1N5819 Schottky diodes** ($40\text{V}, 1\text{A}, t_{rr} < 10\text{ ns}$) to safely recirculate back-EMF voltage transients when inductive coils are de-energized ($V = -L \frac{di}{dt}$).

---

## 3. Power Budget & Field Autonomy Engineering Math

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 COMPREHENSIVE ELECTRICAL POWER BUDGET                                  │
├──────────────────────────┬────────┬──────────┬──────────┬──────────┬────────────┬──────────────────────┤
│ Subsystem Component      │ Voltage│ Idle (A) │ Avg (A)  │ Peak (A) │ Duty Cycle │ Effective Power (W)  │
├──────────────────────────┼────────┼──────────┼──────────┼──────────┼────────────┼──────────────────────┤
│ Raspberry Pi 5 (8GB)     │ 5.1 V  │ 0.60 A   │ 1.10 A   │ 2.40 A   │ 100%       │ 5.61 W               │
│ Hailo-8L M.2 AI Hat      │ 3.3 V  │ 0.15 A   │ 0.60 A   │ 0.80 A   │ 40% (Burst)│ 0.79 W               │
│ ZED-F9P RTK GNSS Receiver│ 5.0 V  │ 0.20 A   │ 0.25 A   │ 0.32 A   │ 100%       │ 1.25 W               │
│ AS7265x Spectral Triad   │ 3.3 V  │ 0.01 A   │ 0.05 A   │ 0.08 A   │ 25% (Scans)│ 0.04 W               │
│ Solux 20W Halogen Lamp   │ 12.0 V │ 0.00 A   │ 1.67 A   │ 5.20 A*  │ 8% (5s/pt) │ 1.60 W               │
│ TrueSoil TDR-100 Probe   │ 12.0 V │ 0.02 A   │ 0.04 A   │ 0.06 A   │ 25%        │ 0.12 W               │
│ Adafruit RFM95W LoRaWAN  │ 3.3 V  │ 0.01 A   │ 0.08 A   │ 0.12 A   │ 15% (TX)   │ 0.04 W               │
│ Motor Driver (Logic+Idle)│ 12.0 V │ 0.08 A   │ 0.10 A   │ 0.15 A   │ 100%       │ 1.20 W               │
│ 4x Drive Motors (4WD)    │ 12.0 V │ 0.00 A   │ 1.50 A   │ 6.80 A** │ 70% (Move) │ 12.60 W              │
│ Linear Actuator Probe    │ 12.0 V │ 0.00 A   │ 1.20 A   │ 2.20 A   │ 5% (Deploy)│ 0.72 W               │
│ Power Converter Losses   │ —      │ 0.25 W   │ 1.99 W   │ 3.50 W   │ 100% (η=91)│ 1.99 W               │
├──────────────────────────┼────────┼──────────┼──────────┼──────────┼────────────┼──────────────────────┤
│ TOTAL SYSTEM METRICS     │ —      │ 6.82 W   │ 25.96 W  │ 124.5 W  │ —          │ 25.96 Watts (Average)│
└──────────────────────────┴────────┴──────────┴──────────┴──────────┴────────────┴──────────────────────┘
* Note: Halogen cold filament inrush current reaches 5.2A for 18 ms until heated.
** Note: Motor peak current reflects 4-wheel concurrent stall when breaking through muddy furrow walls.
```

### Operational Modes Power Consumption
1. **Idle / Standby Mode** (GPS locked, Pi idling, waiting for mission command): **$6.82\text{ Watts}$** ($0.53\text{ A}$ @ $12.8\text{V}$).
2. **Transit / Autonomous Crawl Mode** (Pi calculating ROS2 Nav2 paths, motors driving at $0.5\text{ m/s}$): **$22.8\text{ Watts}$** ($1.78\text{ A}$ @ $12.8\text{V}$).
3. **Active Sampling Mode** (Rover halted, actuator lowered, 20W halogen ON, AS7265x scanning, Hailo-8L running FNO inference): **$34.8\text{ Watts}$** ($2.72\text{ A}$ @ $12.8\text{V}$).
4. **Weighted Average Operational Draw**: **$25.96\text{ Watts}$** ($2.03\text{ A}$ @ $12.8\text{V}$).

### Exact Mathematical Battery Runtime Derivation
- **Nominal Battery Energy**:
  $$E_{\text{nom}} = V_{\text{nominal}} \times Q = 12.8\text{ V} \times 20.0\text{ Ah} = \mathbf{256.0\text{ Watt-hours (Wh)}}$$
- **Usable Capacity Factor ($\text{DoD}$)**:
  LiFePO4 chemistry safely tolerates an $85\%$ Depth of Discharge without cell degradation ($>3,000$ cycles):
  $$E_{\text{usable}} = 256.0\text{ Wh} \times 0.85 = \mathbf{217.6\text{ Wh}}$$
- **Temperature & Peukert Derating**:
  Because LiFePO4 internal resistance is exceptionally low ($<15\text{ m}\Omega$), Peukert's exponent is $k \approx 1.03$ (nearly ideal). Derating for $35^{\circ}\text{C}$ summer field temperatures ($C_T = 0.98$):
  $$E_{\text{net}} = 217.6\text{ Wh} \times 0.98 = \mathbf{213.25\text{ Wh}}$$
- **Continuous Field Runtime (Battery-Only, Zero Sunlight)**:
  $$\text{Runtime}_{\text{battery\_only}} = \frac{E_{\text{net}}}{P_{\text{avg}}} = \frac{213.25\text{ Wh}}{25.96\text{ W}} = \mathbf{8.21\text{ Hours}}$$
  At a crawling survey speed of $0.5\text{ m/s}$ ($1.8\text{ km/h}$), TerraBot traverses **$14.8\text{ kilometers}$ ($9.2\text{ miles}$)** on a single charge.

### Solar Equilibrium & Net-Positive Daily Field Autonomy
- **Photovoltaic Generation (Pennsylvania Summer Solar Insolation)**:
  - Average Peak Sun Hours (NREL NSRDB Lancaster, PA): $H = 4.2\text{ peak hours/day}$.
  - Rated Panel Output: $P_{\text{stc}} = 50\text{ W}$.
  - MPPT Conversion Efficiency: $\eta_{\text{mppt}} = 0.92$.
  - Flat horizontal mounting dirt/dust derate factor: $f_{\text{tilt}} = 0.80$.
  $$E_{\text{solar\_daily}} = 50\text{ W} \times 4.2\text{ h} \times 0.92 \times 0.80 = \mathbf{154.5\text{ Wh/day}}$$
- **Typical Daily Operational Campaign**:
  - 4 hours of active surveying per day: $E_{\text{consumed}} = 25.96\text{ W} \times 4.0\text{ h} = \mathbf{103.8\text{ Wh/day}}$.
  - **Net Energy Surplus**:
    $$\Delta E = E_{\text{solar\_daily}} - E_{\text{consumed}} = +154.5\text{ Wh} - 103.8\text{ Wh} = \mathbf{+50.7\text{ Wh/day}}$$
  The rover operates in **perpetual net-positive energy autonomy**, maintaining 100% battery state-of-charge without ever requiring AC grid tethering.

---

## 4. EMI, Ground Loops & Analog Signal Integrity

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              ELECTROMAGNETIC INTERFERENCE (EMI) MITIGATION                             │
├─────────────────────┬───────────────────────────────┬──────────────────────────────────────────────────┤
│ Noise Source        │ Affected Victim Subsystem     │ Physical & Electrical Countermeasure             │
├─────────────────────┼───────────────────────────────┼──────────────────────────────────────────────────┤
│ 20 kHz Motor PWM    │ AS7265x Photodiode ADCs       │ Star-ground separation (`GND_PWR` vs `GND_LOGIC`)│
│ Motor Brush Arcing  │ Pi 5 / Hailo PCIe Bus         │ Fair-Rite 75 clamp ferrites + optocouplers (6N137│
│ Halogen Cold Inrush │ 12V System Rail Droop         │ 10 µH shielded inductor + 220 µF low-ESR LC tank │
│ Fast Switching Buck │ I2C SDA/SCL Signal Edges      │ Dedicated low-noise LDO (LP5907) for 3.3V sensor │
│ Soil Ground Currents│ TDR Soil Moisture Reading     │ RS-485 differential signaling + SM712 TVS diodes │
└─────────────────────┴───────────────────────────────┴──────────────────────────────────────────────────┘
```

### Why the AS7265x Requires Extreme Noise Isolation
- The AS7265x spectral triad contains 18 discrete silicon photodiodes coupled to 16-bit analog-to-digital converters measuring photocurrents on the order of **nano-amperes ($10^{-9}\text{ A}$)** to micro-amperes.
- Concurrently, the four DC drive motors switch **$10\text{--}15\text{ Amperes}$** of current at $20\text{ kHz}$ PWM frequencies. If motor return currents share even $0.05\ \Omega$ of common ground wire impedance with the sensor, the resulting ground bounce ($V = I \times R = 10\text{ A} \times 0.05\ \Omega = \mathbf{0.5\text{ V}}$) completely annihilates the sensor's microvolt spectral baseline.

### Engineering Mitigations Implemented
1. **Star-Ground Topology**:
   - A single, gold-plated M5 chassis bolt positioned immediately adjacent to the LiFePO4 battery negative terminal serves as the **System Star Ground**.
   - `GND_PWR` (carrying noisy motor and actuator return currents) and `GND_LOGIC` (carrying clean sensor and digital return currents) trace along physically separate copper conductors and meet **exclusively at this single star bolt**. No circulating ground currents can flow across the logic board.
2. **Dedicated Ultra-Low-Noise Sensor LDO**:
   - The AS7265x is strictly forbidden from running off the Raspberry Pi's digital 3.3V header (which carries high-frequency ripple from CPU core clock switching).
   - Instead, power is drawn from the auxiliary 5V buck and regulated down through a dedicated **TI LP5907 ultra-low-noise LDO regulator** ($<6.5\ \mu\text{V}_{\text{RMS}}$ output noise, PSRR $>82\text{ dB}$ at 1 kHz).
3. **Halogen Lamp Inrush Damper (LC Low-Pass Filter)**:
   - A cold tungsten halogen filament exhibits an electrical resistance only $1/10\text{th}$ of its operating resistance, producing a momentary $5.2\text{A}$ inrush spike that could reset the Pi 5.
   - A low-pass tank circuit comprising a **$10\ \mu\text{H}$ high-current toroidal inductor** and a **$220\ \mu\text{F}$ Panasonic FR low-ESR electrolytic capacitor** buffers the inrush current, smoothing the rail transition.
4. **Shielded Twisted-Pair (STP) Cabling**:
   - The I2C and RS-485 communication lines run inside foil-shielded twisted-pair cables. The braided shield is grounded at **one end only** (the Star Ground) to eliminate ground-loop antenna pickup.

---

## 5. Updated Itemized BOM Table (2026 Reality vs. v1 PJAS Slide)

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                          REALISTIC 2026 BILL OF MATERIALS VS. v1 PRESENTATION                          │
├────────────────────┬─────────────────────────────┬───────────────────┬──────────┬──────────┬───────────┤
│ Subsystem Category │ Component Name & Model      │ Supplier / Part # │ v1 Claim │ 2026 Real│ Delta /   │
│                    │                             │                   │ (PJAS)   │ Price    │ Why v1 Err│
├────────────────────┼─────────────────────────────┼───────────────────┼──────────┼──────────┼───────────┤
│ Core Compute       │ Raspberry Pi 5 (8GB)        │ DigiKey / Pi Org  │ $120.00* │ $80.00   │ Jetson EOL│
│ AI Acceleration    │ Hailo-8L M.2 AI Kit (26TOPS)│ Raspberry Pi Org  │ $0.00    │ $70.00   │ Omitted   │
│ Active Cooling     │ Pi 5 Aluminum Active Cooler │ Pi Org SC1148     │ $0.00    │ $5.00    │ Omitted   │
│ High-Speed Storage │ 256GB PCIe NVMe M.2 SSD     │ Kingston NV2      │ $0.00    │ $32.00   │ Omitted   │
│ Spectral Sensor    │ AS7265x 18-Channel Triad    │ SparkFun SEN-15050│ $65.00   │ $69.95   │ Realistic │
│ Optical Reference  │ 99% PTFE Zenith Lite Tile   │ SphereOptics      │ $0.00    │ $145.00  │ Omitted   │
│ Active Illuminator │ Solux 4700K 20W Halogen Bulb│ Tailored Lighting │ $0.00    │ $24.00   │ Omitted   │
│ Positioning / GNSS │ u-blox ZED-F9P RTK Receiver │ SparkFun GPS-16481│ $15.00** │ $249.95  │ 3m vs 1cm │
│ GNSS Antenna       │ Multi-Band L1/L2/E5b IP67   │ SparkFun GPS-17751│ $0.00    │ $64.95   │ Omitted   │
│ Soil Moisture      │ TrueSoil TDR-100 RS-485 Mod │ DFRobot / SparkFun│ $0.00    │ $38.00   │ Omitted   │
│ Telemetry Radio    │ Adafruit RFM95W LoRaWAN 915 │ Adafruit ID 3072  │ $0.00    │ $24.95   │ Omitted   │
│ Drive Motors       │ 4x 12V 120RPM Planetary+Enc │ GoBILDA 5202 Ser. │ $80.00   │ $140.00  │ Toy motors│
│ Motor Driver       │ Cytron MDDS30 Dual 15A Smart│ Cytron MDDS30     │ $0.00    │ $85.00   │ Drove dir.│
│ Agricultural Tires │ 4x 150mm R-1 Chevron Rubber │ GoBILDA 584454    │ $0.00    │ $64.00   │ Omitted   │
│ Main Battery       │ 12.8V 20Ah LiFePO4 (256 Wh) │ Miady / Amazon    │ $50.00   │ $69.00   │ Undersized│
│ Solar Power Gen.   │ 50W Semi-Flexible PV Panel  │ Renogy 50W 12V    │ $0.00    │ $89.00   │ Omitted   │
│ Solar Controller   │ Genasun GV-5-Li-14.2V MPPT  │ SunSaver / Victron│ $0.00    │ $65.00   │ Omitted   │
│ DC-DC Power Reg.   │ Mean Well 5V 5A + LDOs+Fuses│ DigiKey Parts     │ $0.00    │ $48.00   │ Omitted   │
│ Chassis & Shell    │ 5052-H32 Al Tub + Extrusions│ SendCutSend/Misumi│ $0.00    │ $85.00   │ $0 chassis│
│ Mechanical Actuator│ 12V Linear Lead-Screw Probe │ Progressive Auto. │ $0.00    │ $58.00   │ Sketched  │
│ IP65 Sealed Encl.  │ Polycarbonate Weatherproof  │ BUD Industries    │ $0.00    │ $42.00   │ Omitted   │
├────────────────────┼─────────────────────────────┼───────────────────┼──────────┼──────────┼───────────┤
│ TOTAL SYSTEM COST  │ Complete Field Prototype    │ All Tier-1 Vendors│ $485.00  │ $1,481.80│ Realistic │
└────────────────────┴─────────────────────────────┴───────────────────┴──────────┴──────────┴───────────┘
* v1 priced an NVIDIA Jetson Nano at $120; officially EOL since 2023, remaining stock costs $250+.
** v1 priced a generic $15 USB GPS dongle with 3 to 5 meter error, which makes repeatable sub-meter spatial soil mapping mathematically impossible.
```

---

## 6. Engineering Decision Explanations ("The Why Sheet")

1. **Why Raspberry Pi 5 + Hailo-8L over Jetson Nano?** — Jetson Nano is discontinued (2023 EOL) and power-hungry ($10\text{--}12\text{W}$, 0.5 TOPS). Pi 5 + Hailo delivers $26\text{ TOPS}$ of INT8 AI power at only $2.5\text{W}$ ($52\times$ inference efficiency).
2. **Why an ideal P-MOSFET circuit over a Schottky diode for reverse polarity?** — A Schottky diode causes a $0.5\text{V}$ voltage drop and burns $2\text{--}4\text{W}$ of battery power as heat; the IRF4905 drops only $0.04\text{V}$ ($0.08\text{W}$ loss) with zero heat sinking.
3. **Why multi-stage buck converters instead of linear regulators?** — Stepping $12.8\text{V}$ down to $5.1\text{V}$ at $2.0\text{A}$ with a linear regulator would burn $(12.8 - 5.1) \times 2.0 = 15.4\text{ Watts}$ of battery power as useless heat! Synchronous buck converters operate at $>92\%$ electrical efficiency.
4. **Why an isolated 3.3V LDO for the AS7265x?** — Digital 3.3V rails from the Pi 5 carry high-frequency switching hash that corrupts the micro-amp photocurrents of the 18 spectrometer photodiodes.
5. **Why optocouplers between the Pi 5 and the motor driver?** — Galvanically isolates the Pi 5’s fragile Broadcom SoC from high-voltage inductive spikes ($L \frac{di}{dt}$) generated by the 120RPM planetary motors.
6. **Why a single-point Star Ground?** — Prevents massive $10\text{A}$ motor return currents from circulating through sensitive logic reference planes, eliminating ground bounce.
7. **Why an LC tank on the halogen lamp?** — A cold halogen bulb draws a $5.2\text{A}$ inrush spike for $18\text{ ms}$; the $10\ \mu\text{H} + 220\ \mu\text{F}$ LC filter buffers this spike to prevent CPU brownouts.
8. **Why RS-485 Modbus for the soil probe?** — Standard 3.3V UART signals degrade within $1\text{ meter}$ in noisy farm environments; RS-485 uses balanced differential pairs ($A$ and $B$) that reject common-mode EMI up to $1,000\text{ meters}$.
9. **Why $4.7\text{ k}\Omega$ pull-ups on the I2C bus?** — Sensor cables routed through the robot arm exhibit parasitic capacitance; $4.7\text{ k}\Omega$ pull-ups guarantee sharp square-wave rise times under $1\ \mu\text{s}$ at $400\text{ kHz}$ Fast Mode.
10. **Why fuse the battery at 15A?** — A dead short on a 20Ah LiFePO4 battery can release $>200\text{ Amperes}$ of explosive arc-flash current; a $15\text{A}$ ATC fuse clears the fault in $<5\text{ ms}$.

---

> 💻 **Computer Science Translation**:
> - **Voltage Regulators (Buck Converters) = Type Casting**: Connecting a 12.8V line directly to a 3.3V chip is like casting a 64-bit integer into an 8-bit pointer without bounds checking—it causes a fatal hardware stack overflow (blown silicon). Buck converters act as **safe narrowing type casters** (`static_cast<uint5_t>(uint12_t)`).
> - **Pull-Up Resistors = Null-Coalescing Operator / Default Initializers**: Open-drain I2C buses float when idle. A $4.7\text{ k}\Omega$ pull-up resistor is equivalent to a **null-coalescing default operator** (`signal ?? HIGH`), ensuring the bus defaults to logical `1` instead of an undefined `null` floating state.
> - **Star Grounding = Process Sandboxing & Memory Isolation**: Sharing a dirty ground wire between motors and sensors is like allowing multiple threads to write to un-mutexed global memory (race conditions and dirty reads). Star grounding **sandboxes memory domains**, giving each subsystem an isolated address space back to the root pointer (`BAT_MINUS`).
> - **Flyback Diodes = Exception Handling (`try...catch`)**: When an inductive motor turns off, collapsing magnetic fields generate a massive reverse-voltage spike. A flyback diode acts as an **asynchronous exception handler**, catching the high-voltage panic and safely shunting it to ground before it crashes the system.
> - **Level Shifters (RS-485 / SP3485) = Protocol Adapters & Serialization**: Converting 3.3V single-ended UART into differential RS-485 packets is equivalent to an **API Gateway serializing internal JSON objects into encrypted, fault-tolerant gRPC protocol buffers** across an untrusted network link.

---

## References
1. Texas Instruments (2020). *LP5907 250-mA Ultra-Low-Noise, Low-IQ LDO Linear Regulator*. TI Datasheet SNVSA23I.
2. u-blox AG (2024). *ZED-F9P Integration Manual: High Precision GNSS Receiver*. Document UBX-18010802.
3. AMS AG (2021). *AS7265x 18-Channel Multi-Spectral Triad Device Specification*. Premstaetten, Austria.
4. Linear Technology / Analog Devices (2018). *AN-139: Power Conditioning and EMI Mitigation in Industrial Field Robotics*.
5. National Renewable Energy Laboratory (NREL). (2021). *National Solar Radiation Database (NSRDB)*. U.S. Department of Energy.
