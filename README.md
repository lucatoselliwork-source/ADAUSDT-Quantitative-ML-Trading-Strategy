# ADAUSDT Quantitative Machine Learning Trading Strategy

This repository presents a complete quantitative research project focused on
systematic trading of the ADAUSDT cryptocurrency pair.

The goal of the project is to demonstrate a clean, reproducible, and
well-structured quantitative workflow suitable for academic or professional
review.

---

## Project Overview

- **Market**: ADAUSDT (Binance)
- **Timeframe**: 16-hour OHLC bars
- **Data window**: Approximately 3 years
- **Model class**: Linear autoregressive models (AR)
- **Evaluation**: Transaction-cost-aware backtesting and benchmarking

The project emphasizes interpretability, robustness, and realistic performance
assessment rather than model complexity.

---

## Repository Structure

notebooks/ 
- 01_data_and_feature_engineering.ipynb
- 02_model_training.ipynb  
- 03_strategy_validation.ipynb  

src/adausdt_qml/
- research.py   (research and backtesting utilities)
- models.py     (model definitions)
- binance.py    (data download helpers)
- project.py    (project setup helpers)

cache/  
- Local market data (ignored by git)

outputs/  
- Figures and intermediate outputs (ignored by git)

model_weights.pth  
- Trained model parameters

---

## Methodology Summary

1. **Data acquisition**  
   Binance trade data is downloaded and aggregated into OHLC bars.

2. **Feature engineering**  
   Log-returns and lagged log-returns are constructed following an
   autoregressive structure.

3. **Model training**  
   Models are trained using time-based splits and batch gradient descent.

4. **Strategy evaluation**  
   Performance is evaluated using equity curves, drawdowns, Sharpe ratios,
   and transaction costs.

5. **Benchmarking**  
   Strategy performance is compared against a buy-and-hold baseline.

All analysis details, diagnostics, and plots are contained inside the notebooks.

---

## Environment Setup

### 1. Install Miniforge
https://conda-forge.org/download/

### 2. Create the research environment
conda create -n research python=3.12  
conda activate research

### 3. Install required libraries
conda install -c conda-forge -c pytorch \
polars pytorch requests scipy matplotlib altair tqdm vegafusion

---

## How to Run the Project

Open the repository in Visual Studio Code and execute the notebooks in order:

1. 01_data_and_feature_engineering.ipynb  
2. 02_model_training.ipynb  
3. 03_strategy_validation.ipynb  

If market data is not found locally, it will be downloaded automatically.

---

## Disclaimer

This project is for educational and research purposes only and does not
constitute financial or investment advice.

---

Author:  
Luca Toselli

Local Libraries Author:
MemLabs