🌌 SvetLuna — Dark Matter Simulation

Core Research Project — 2025
Synthetic modeling of dark-matter resonance fields using 2D spectral density, anomaly detection (LOF), and resonance correlation analysis.

🧭 Обзор

Этот проект моделирует синтетическое резонансное поле, вдохновлённое физическим и информационным поведением тёмной материи. Он генерирует случайные двумерные распределения энергии, анализирует их спектральную плотность мощности (СПМ) и выявляет аномалии с помощью локального коэффициента выбросов (ЛКВ).
Каждый эксперимент даёт уникальную визуализацию поля и спектральный отпечаток.

🧩 Структура проекта
configs/         → YAML configuration files (parameters, noise models)  
data/            → Input and reference data (optional)  
outputs/         → Simulation outputs, spectra, and plots  
src/             → Core source code (simulation, detection, visualization)  
Makefile         → Automates setup, run, and visualization  
requirements.txt → Python dependencies  

⚙️ Запуск симуляции
git clone https://github.com/SvetLuna-Lab/SvetLuna-Dark-Matter-Simulation.git  
cd SvetLuna-Dark-Matter-Simulation  

make setup  
make run  
make plots  


Outputs will be saved into outputs/figures/.

🔬 Methods

Synthetic field construction (combining drift, 1/f noise, white noise)

2D Power Spectral Density (PSD) computation

Resonance feature extraction

Anomaly detection via LOF

Visualization of energy distributions and pattern emergence

📊 Example Outputs

Field | PSD | Anomalies | Spectrum
Here you can insert links or thumbnails of example images.

🧭 Engineering Note Preview
6

Stochastic field model (drift + 1/f + white) with latent response (τ ≈ 0.8 s).
Interpretation: the 1/f region corresponds to background density clustering. The latent tail visualises stored-energy release controlled by τ.
This layer feeds TIA/SPICE and CEA with realistic stochastic input.

📘 View Full Engineering-Note (PDF)
 – optional link to full document

🧬 Research Direction

This repository belongs to the SvetLuna Research Continuum (2025) — a transdisciplinary exploration of resonance, energy, and consciousness through machine-intelligence.
📘 Previous: Hybrid Atmospheric Installation
🔭 Next: Cascade Resonance Fields & Quantum Echoes (in preparation)

© 2025 Светлана Романова (SvetLuna)
Independent researcher — dark matter simulation, hybrid atmospheric energy systems.
