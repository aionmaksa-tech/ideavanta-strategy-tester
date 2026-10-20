# IdeaVanta Strategy Tester & Portfolio Basket Lab

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-5865F2?logo=discord&logoColor=white)](https://discord.gg/6q2gsDvae)
[![Research: 11.88B Real Ticks](https://img.shields.io/badge/Data-11.88B%20Real%20Ticks-orange)](https://ideavanta.com)

A standalone quantitative research lab and portfolio simulator based on **11,876,579,606 modeled real ticks** and **99,103 simulated trades** across **34 verified MetaTrader 5 Expert Advisor profiles** (2013–2026).

Developed as an open-source research companion to [IdeaVanta.com](https://ideavanta.com).

---

## 💡 Overview

**VantaBox** operates within a selected time window by observing market data and evaluating it against preset rules to decide whether to trade the current session or skip it. When conditions qualify, it places and manages the configured orders and protection, finishing according to the session schedule.

This standalone portfolio simulator allows algorithmic traders and researchers to:
1. **Explore 34 historical MT5 test profiles** across 5 currency pairs (`AUDJPY`, `EURJPY`, `EURUSD`, `GBPUSD`, `USDJPY`) modeled on **99% Real Ticks**.
2. **Evaluate institutional quantitative metrics** including **Sharpe Ratio** (up to `2.96`), **Linear Regression Equity Smoothness** (`LR Correlation` up to `0.9927`), **Reward-to-Risk Payoff Ratio** (`Avg Win / Avg Loss` up to `4.55x`), and **Recovery Factor**.
3. **Simulate multi-pair portfolio baskets** in real time, comparing **Fixed \$100 Risk** vs **1% Compounding Risk** across 13.5 years of data (2013–2026).

---

## 📊 Sample Institutional Highlights (2013–2026 · 99% Real Ticks)

| Pair | Preset | Profit Factor | Sharpe Ratio | LR Smoothness | Payoff (R:R) | Win Rate | Max DD | Simulated Net |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **USDJPY** | `Setup 5.2 · $100` | **1.32** | **2.13** | **0.9927** | **2.02x** | 39.6% | \$4,313 | +\$94,427 |
| **USDJPY** | `Setup 1 · $100` | **1.29** | **2.89** | **0.9856** | **1.72x** | 42.9% | \$3,907 | +\$43,721 |
| **GBPUSD** | `Setup 1 · $100` | **1.16** | **2.96** | **0.9387** | **1.22x** | 48.7% | \$2,690 | +\$25,383 |
| **GBPUSD** | `Setup 2 · $100` | **1.15** | **2.39** | **0.9685** | **1.24x** | 48.1% | \$4,193 | +\$29,482 |
| **USDJPY** | `Setup 6 · $100` | **1.25** | **1.63** | **0.9777** | **4.55x** | 21.6% | \$5,530 | +\$76,419 |
| **EURUSD** | `Setup 1 · $100` | **1.11** | **1.90** | **0.9548** | **1.47x** | 43.1% | \$2,202 | +\$14,476 |

---

## 🚀 Quick Start (Zero Dependencies)

The dashboard runs out-of-the-box using the Python standard library—no `pip install` required!

### 1. Launch the Interactive Web Dashboard
```bash
python app.py
```
Open your browser to: **`http://127.0.0.1:8055`**

### 2. Run via Command Line / Headless
```bash
python strategy_tester.py
```

---

## 🔗 About IdeaVanta & VantaBox Software

* **IdeaVanta (`ideavanta.com`):** An independent quantitative research and software platform publishing historical MetaTrader 5 dataset analyses and portfolio simulation tools.
* **VantaBox MT5 Expert Advisor:** A software tool for MetaTrader 5 offered via [ideavanta.com](https://ideavanta.com) for technical and educational evaluation.
* **Community Discussion:** Join the [IdeaVanta Discord](https://discord.gg/6q2gsDvae) to discuss quantitative testing, portfolio diversification, and MT5 execution mechanics.

---

## ⚖️ Legal & Regulatory Disclaimer

* **Software & Research Only (Not Financial Advice):** This repository, dashboard, and all associated materials from IdeaVanta are provided strictly for **educational, informational, and software research purposes**. Nothing herein constitutes financial, investment, legal, or tax advice, nor a solicitation to buy, sell, or copy any financial instrument.
* **Simulated Performance Limitation:** Historical backtest metrics (2013–2026) represent hypothetical computer simulations in MetaTrader 5. Past or simulated performance is not indicative of, and does not guarantee, future live results. Foreign exchange (Forex) and CFD trading carry a high level of risk and may not be suitable for all individuals.

---

## 📄 License
MIT License. Free for personal, educational, and research use.
