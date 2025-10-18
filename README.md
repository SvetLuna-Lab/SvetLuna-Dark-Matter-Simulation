# 🌌 SvetLuna — Dark Matter Simulation  
**Core Research Project — 2025**  
Synthetic modeling of dark-matter resonance fields using 2D spectral density, anomaly detection (LOF), and resonance correlation analysis.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org)

---

## Table of Contents  
- [Overview](#overview)  
- [Project Structure](#project-structure)  
- [Run Simulation](#run-simulation)  
- [Methods](#methods)  
- [Example Outputs](#example-outputs)  
- [Engineering Note Preview](#engineering-note-preview)  
- [Research Direction](#research-direction)  
- [License](#license)

---

## 🧭 Overview  
This project models a synthetic *resonance field* inspired by the physical and informational behaviour of dark matter. It generates random 2D energy distributions, analyses their power spectral density (PSD), and detects anomalies using **Local Outlier Factor (LOF)**.  
Each experiment produces a unique field visualization and spectral fingerprint.

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
```bash
git clone https://github.com/SvetLuna-Lab/SvetLuna-Dark-Matter-Simulation.git  
cd SvetLuna-Dark-Matter-Simulation  

make setup  
make run  
make plots

The outputs will be saved into outputs/figures/.

🔬 Methods

Synthetic field construction (combining drift, 1/f noise, white noise)

2D Power Spectral Density (PSD) computation

Resonance feature extraction

Anomaly detection via LOF

Visualization of energy distributions and pattern emergence

📊 Example Outputs

Field | PSD | Anomalies | Spectrum
Insert thumbnail images and links here.

🧭 Engineering Note Preview

Stochastic field model (drift + 1/f + white) with latent response (τ ≈ 0.8 s).
Interpretation: the 1/f region corresponds to background density clustering. The latent tail visualises stored-energy release controlled by τ.
This layer feeds TIA/SPICE and CEA with realistic stochastic input.

📘 View full Engineering Note (PDF)

🧬 Research Direction

This repository belongs to the SvetLuna Research Continuum (2025) — a transdisciplinary exploration of resonance, energy, and consciousness through machine intelligence.
Previous: Hybrid Atmospheric Installation
Next: Cascade Resonance Fields & Quantum Echoes (in preparation)

© 2025 Светлана Романова (SvetLuna)
Independent researcher — dark matter simulation, hybrid atmospheric energy systems.

License

This project is licensed under the MIT License — see the LICENSE
 file for details.

