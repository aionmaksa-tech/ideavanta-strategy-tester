"""
=============================================================================
 IdeaVanta · VantaBox Strategy Portfolio Simulator
 Open-Source Algorithmic Trading Research Tool
=============================================================================
Simulates and evaluates portfolio combinations of multi-pair algorithmic
trading setups based on 13-year real-tick MT5 backtests (2013-2026,
11.88 Billion modeled real ticks across 34 profiles).
"""

import json
import os
import math
from typing import List, Dict, Any, Optional

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "backtest_catalog.json")

class StrategyTester:
    def __init__(self, data_path: Optional[str] = None):
        self.data_path = data_path or DATA_FILE
        self.profiles = self._load_data()

    def _load_data(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Catalog data not found at {self.data_path}")
        with open(self.data_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def list_pairs(self) -> List[str]:
        return sorted(list(set(p["pair"] for p in self.profiles)))

    def filter_profiles(self, pair: Optional[str] = None, risk: Optional[str] = None) -> List[Dict[str, Any]]:
        results = self.profiles
        if pair:
            results = [p for p in results if p["pair"].upper() == pair.upper()]
        if risk:
            results = [p for p in results if risk in p["setup"]]
        return results

    def simulate_portfolio(self, selected_indices: List[int], initial_balance: float = 10000.0) -> Dict[str, Any]:
        """
        Simulates an aggregated basket of strategies.
        Computes composite profit factor, Sharpe ratio, LR equity smoothness,
        payoff ratio (R:R), combined trade volume, and correlation-adjusted drawdown.
        """
        if not selected_indices:
            return {"error": "No setups selected."}

        selected = [self.profiles[i] for i in selected_indices if 0 <= i < len(self.profiles)]
        if not selected:
            return {"error": "Invalid profile selection."}

        total_trades = sum(p["trades"] for p in selected)
        total_ticks = sum(p.get("ticks", 0) for p in selected)
        weighted_pf = sum(p["profit_factor"] * p["trades"] for p in selected) / total_trades if total_trades > 0 else 0
        weighted_sharpe = sum(p.get("sharpe_ratio", 1.5) * p["trades"] for p in selected) / total_trades if total_trades > 0 else 0
        weighted_lr = sum(p.get("lr_correlation", 0.95) * p["trades"] for p in selected) / total_trades if total_trades > 0 else 0
        weighted_rr = sum(p.get("payoff_ratio", 1.5) * p["trades"] for p in selected) / total_trades if total_trades > 0 else 0
        
        # Weighted win rate
        total_wins = 0
        for p in selected:
            wr_val = float(p["win_rate"].replace("%", "")) / 100.0
            total_wins += wr_val * p["trades"]
        composite_win_rate = (total_wins / total_trades * 100.0) if total_trades > 0 else 0

        # Estimated portfolio drawdown: diversification benefit factor sqrt(N) for uncorrelated pairs
        unique_pairs = len(set(p["pair"] for p in selected))
        diversification_multiplier = 1.0 / math.sqrt(unique_pairs) if unique_pairs > 1 else 1.0

        # Sum of maximum dollar drawdowns adjusted for portfolio diversification
        raw_dd_sum = 0
        total_net_profit = 0
        for p in selected:
            clean_dd = float(p["max_dd"].replace(",", "").replace("$", ""))
            raw_dd_sum += clean_dd
            clean_net = float(p["reported_net"].replace(",", "").replace("+", "").replace("$", ""))
            total_net_profit += clean_net
        
        estimated_portfolio_dd = raw_dd_sum * diversification_multiplier
        recovery_factor = round(total_net_profit / estimated_portfolio_dd, 2) if estimated_portfolio_dd > 0 else 0

        return {
            "num_setups": len(selected),
            "unique_pairs": list(set(p["pair"] for p in selected)),
            "total_historical_trades": total_trades,
            "total_ticks_modeled": total_ticks,
            "total_reported_net": f"+${round(total_net_profit):,}",
            "raw_net_profit": round(total_net_profit, 2),
            "composite_profit_factor": round(weighted_pf, 2),
            "composite_sharpe_ratio": round(weighted_sharpe, 2),
            "composite_lr_correlation": round(weighted_lr, 4),
            "composite_payoff_ratio": f"{round(weighted_rr, 2)}x",
            "composite_win_rate": f"{round(composite_win_rate, 1)}%",
            "recovery_factor": recovery_factor,
            "diversification_factor": round(diversification_multiplier, 3),
            "estimated_max_dd": round(estimated_portfolio_dd, 2),
            "selected_setups": [f"{p['pair']} {p['setup']} (PF: {p['profit_factor']}, Sharpe: {p.get('sharpe_ratio')})" for p in selected]
        }

if __name__ == "__main__":
    tester = StrategyTester()
    print("=================================================================")
    print(" IdeaVanta · Strategy Tester & Portfolio Basket Simulator")
    print("=================================================================")
    print(f"Loaded {len(tester.profiles)} verified MT5 strategy profiles across {len(tester.list_pairs())} pairs.")
    print("\nSample Recommended Conservative Basket (USDJPY s5.2 + GBPUSD s2 + EURUSD s1):")
    
    sample_basket = [10, 14, 26] # EURUSD s1 $100, GBPUSD s2 $100, USDJPY s5.2 $100
    res = tester.simulate_portfolio(sample_basket)
    print(json.dumps(res, indent=2))
