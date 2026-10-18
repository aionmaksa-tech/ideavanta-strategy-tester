# IdeaVanta Strategy Tester & Portfolio Basket Lab

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-5865F2?logo=discord&logoColor=white)](https://discord.gg/6q2gsDvae)
[![Research: Live Data](https://img.shields.io/badge/Data-13--Year%20Tick%20Data-orange)](https://ideavanta.com)

A standalone quantitative research lab and portfolio simulator based on **99,103 historical trades** across **34 verified MetaTrader 5 Expert Advisor profiles** (2013–2026).

Developed as an open-source companion to the [IdeaVanta VantaBox Project](https://ideavanta.com).

---

## 💡 Overview

**VantaBox** operates within a selected time window by observing market data and evaluating it against preset rules to decide whether to trade the current session or skip it. When conditions qualify, it places and manages the configured orders and protection, finishing according to the session schedule.

This standalone portfolio simulator allows algorithmic traders and researchers to:
1. **Explore 34 historical MT5 test profiles** across 5 currency pairs (`AUDJPY`, `EURJPY`, `EURUSD`, `GBPUSD`, `USDJPY`).
2. **Simulate multi-pair portfolio baskets** in real time, observing how combining multiple setups affects overall portfolio drawdown and return-to-drawdown ratios.
3. **Compare fixed dollar risk ($100) vs percentage risk (1%)** models across 13 years of historical data (2013–2026).

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

## 📊 Dataset & Backtest Summary

* **Test Horizon:** 2013-01-03 through 2026-07-14 (historical simulations; past performance does not guarantee future live results).
* **Execution Engine:** MetaTrader 5 Strategy Tester (with real-tick coverage where available).
* **Confidentiality Note:** This repository contains only aggregated summary metrics from the public [IdeaVanta Historical Tests Library](https://ideavanta.com/historical-tests/). Proprietary strategy rules, filters, level calculations, and `.set` parameters are never disclosed.
* **Profiles:** 17 strategy setups, each evaluated under fixed \$100 risk and 1% risk per trade.

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
