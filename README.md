# IdeaVanta Strategy Tester & Portfolio Basket Lab

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-5865F2?logo=discord&logoColor=white)](https://discord.gg/6q2gsDvae)
[![Research: Live Data](https://img.shields.io/badge/Data-13--Year%20Tick%20Data-orange)](https://ideavanta.com)

A standalone quantitative research lab and portfolio simulator based on **99,103 historical trades** across **34 verified MetaTrader 5 Expert Advisor profiles** (2013–2026).

Developed as an open-source companion to the [IdeaVanta VantaBox Project](https://ideavanta.com).

---

## 💡 Overview

Most retail Forex trading bots fail because they run as single-pair Martingale or unbounded grid systems that eventually experience a catastrophic margin call. 

This simulator allows algorithmic traders and quants to:
1. **Explore 34 real-tick backtests** across 5 currency pairs (`AUDJPY`, `EURJPY`, `EURUSD`, `GBPUSD`, `USDJPY`).
2. **Simulate multi-pair portfolio baskets** in real time, observing how combining uncorrelated setups reduces overall portfolio drawdown while stabilizing equity curve slope.
3. **Compare fixed dollar risk ($100) vs compounding risk (1%)** regimes over 13 years of turbulent market conditions (including the 2015 SNB shock, 2016 Brexit, 2020 COVID volatility, and 2024 Yen carry unwind).

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

## 📊 Dataset & Backtest Methodology

* **Test Horizon:** 2013-01-03 through 2026-07-14.
* **Execution Engine:** MetaTrader 5 Strategy Tester with Real Ticks modeling.
* **Risk Control:** Every setup strictly enforces a mathematical Stop-Loss. Zero Martingale. Zero unbounded grid doubling.
* **Profiles:** 17 distinct strategy setups, each tested under fixed \$100 risk and 1% risk per trade.

---

## 🤝 Community & Automated Execution

* **Vantage Copy Trading:** Want to copy this conservative multi-pair portfolio without running MT5 or a VPS? Join our [Discord Community](https://discord.gg/6q2gsDvae) to get 1-click mobile copy trading access on Vantage Markets.
* **Free VantaBox MT5 EA:** Free software license access is available during public testing at [ideavanta.com](https://ideavanta.com).

---

## 📄 License
MIT License. Free for personal and research use.
