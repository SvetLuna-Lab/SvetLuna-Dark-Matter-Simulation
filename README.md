# 🌌 SvetLuna — Dark Matter Simulation

**Core Research Project — 2025**  
Synthetic modeling of dark matter resonance fields using 2D spectral density, anomaly detection (LOF), and resonance correlation analysis.

---

## 🧭 Overview

This project models a synthetic *resonance field* inspired by the physical and informational behavior of dark matter.  
It generates random 2D energy distributions, analyzes their spectral power density (PSD), and detects anomalies using **Local Outlier Factor (LOF)**.

Each experiment produces a unique field visualization and its spectral fingerprint.

---

## 🧩 Project Structure
configs/ → YAML configuration files (parameters, noise models)
data/ → Input and reference data (optional)
outputs/ → Simulation outputs, spectra, and plots
src/ → Core source code (simulation, detection, visualization)
Makefile → Automates setup, run, and visualization
requirements.txt → Python dependencies

---

## ⚙️ Run Simulation

Clone and run in a Python 3.10+ environment:

```bash
git clone https://github.com/SvetLuna-Lab/SvetLuna-Dark-Matter-Simulation.git
cd SvetLuna-Dark-Matter-Simulation

make setup
make run
make plots

outputs/figures/


🔬 Methods

Synthetic field construction (pink noise, Gaussian blobs, waveforms)

2D Power Spectral Density (PSD) computation

Resonance feature extraction

Anomaly detection via LOF (Local Outlier Factor)

Visualization of energy distribution and pattern emergence


## 📊 Example Outputs

| Field | PSD | Anomalies | Spectrum |
|-------|-----|------------|-----------|
| ![](outputs/figures/field.png) | ![](outputs/figures/psd.png) | ![](outputs/figures/scores.png) | ![](outputs/figures/radial.png) |



📘 [View Engineering Note (PDF)](Dark_Matter_Engineering_Note.pdf)

Detailed figures and explanations of the synthetic-field dynamics,  
including spectral drift, cascade resonance layers, and energy field response.


	
	
	
🧬 Research Direction

This repository belongs to the SvetLuna Research Continuum (2025) —
a transdisciplinary exploration of resonance, energy, and consciousness through machine intelligence.

📘 Hybrid Atmospheric Installation

🔭 Next: Cascade Resonance Fields & Quantum Echoes (in preparation)

© 2025 Svetlana Romanova (SvetLuna)
Independent researcher — dark matter simulation, hybrid atmospheric energy systems.
