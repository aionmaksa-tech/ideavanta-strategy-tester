"""
IdeaVanta · Strategy Tester Local Web Dashboard
Zero-dependency browser application powered by Python standard library.
"""
import os
import json
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from strategy_tester import StrategyTester

PORT = 8055
tester = StrategyTester()

HTML_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IdeaVanta · Quant Strategy Tester & Portfolio Basket Lab</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #0d1117;
      --card-bg: #161b22;
      --border: #30363d;
      --accent: #58a6ff;
      --green: #2ea043;
      --red: #f85149;
      --gold: #d29922;
      --text: #c9d1d9;
      --text-muted: #8b949e;
      --font-mono: 'JetBrains Mono', monospace;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text); padding: 24px; line-height: 1.5; }
    header { max-width: 1280px; margin: 0 auto 24px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border); padding-bottom: 16px; }
    .brand { font-size: 20px; font-weight: 800; color: #fff; display: flex; align-items: center; gap: 10px; }
    .brand span { color: var(--accent); }
    .nav-links a { color: var(--text-muted); text-decoration: none; margin-left: 16px; font-size: 14px; font-weight: 500; }
    .nav-links a:hover { color: #fff; }
    .nav-discord { background: #5865F2; color: #fff !important; padding: 6px 14px; border-radius: 6px; }
    
    .container { max-width: 1280px; margin: 0 auto; display: grid; grid-template-columns: 1fr 370px; gap: 24px; }
    .panel { background: var(--card-bg); border: 1px solid var(--border); border-radius: 8px; padding: 20px; }
    h2 { font-size: 18px; margin-bottom: 14px; color: #fff; display: flex; align-items: center; justify-content: space-between; }
    
    .filters { display: flex; gap: 12px; margin-bottom: 16px; }
    select { background: #21262d; border: 1px solid var(--border); color: #fff; padding: 8px 12px; border-radius: 6px; font-family: inherit; font-size: 14px; }
    
    .table-container { overflow-x: auto; max-height: 560px; }
    table { width: 100%; border-collapse: collapse; font-size: 13px; text-align: left; }
    th { position: sticky; top: 0; background: #21262d; padding: 10px 8px; border-bottom: 2px solid var(--border); font-weight: 600; color: #fff; white-space: nowrap; }
    td { padding: 9px 8px; border-bottom: 1px solid var(--border); white-space: nowrap; }
    tr:hover { background: rgba(88, 166, 255, 0.05); }
    .mono { font-family: var(--font-mono); }
    .positive { color: var(--green); font-weight: 600; }
    .accent { color: var(--accent); font-weight: 600; }
    .gold { color: var(--gold); font-weight: 600; }
    
    .metric-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 16px; }
    .metric-card { background: #21262d; padding: 12px; border-radius: 6px; border: 1px solid var(--border); }
    .metric-label { font-size: 11px; color: var(--text-muted); margin-bottom: 4px; text-transform: uppercase; letter-spacing: 0.4px; }
    .metric-val { font-size: 19px; font-weight: 700; color: #fff; font-family: var(--font-mono); }
    
    .cta-button { display: block; width: 100%; text-align: center; background: var(--green); color: #fff; padding: 12px; border-radius: 6px; font-weight: 700; text-decoration: none; margin-top: 12px; border: none; cursor: pointer; }
    .cta-button:hover { opacity: 0.9; }
    .cta-discord { background: #5865F2; }
    .badge { display: inline-block; padding: 3px 8px; border-radius: 4px; font-size: 11px; font-weight: 600; background: #21262d; color: var(--accent); }
  </style>
</head>
<body>
  <header>
    <div class="brand">IdeaVanta <span>· Quant Strategy Tester (11.88B Real Ticks)</span></div>
    <div class="nav-links">
      <a href="https://ideavanta.com" target="_blank">Research Library</a>
      <a href="https://discord.gg/6q2gsDvae" class="nav-discord" target="_blank">Join Discord</a>
    </div>
  </header>

  <div class="container">
    <div class="panel">
      <h2>
        Historical MT5 Strategy Library (2013–2026 · 99% Real Ticks)
        <span class="badge" id="totalCount">34 Profiles</span>
      </h2>
      <div class="filters">
        <select id="pairFilter" onchange="filterData()">
          <option value="">All Currency Pairs</option>
          <option value="AUDJPY">AUDJPY</option>
          <option value="EURJPY">EURJPY</option>
          <option value="EURUSD">EURUSD</option>
          <option value="GBPUSD">GBPUSD</option>
          <option value="USDJPY">USDJPY</option>
        </select>
        <select id="riskFilter" onchange="filterData()">
          <option value="">All Risk Models</option>
          <option value="$100">Fixed $100 Risk</option>
          <option value="1%">1% Compounding</option>
        </select>
      </div>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th width="34"><input type="checkbox" id="selectAll" onclick="toggleSelectAll()"></th>
              <th>Pair</th>
              <th>Setup</th>
              <th>Profit Factor</th>
              <th>Sharpe</th>
              <th>LR Smoothness</th>
              <th>Payoff (R:R)</th>
              <th>Win Rate</th>
              <th>Trades</th>
              <th>Max DD</th>
              <th>Net Profit</th>
            </tr>
          </thead>
          <tbody id="tableBody"></tbody>
        </table>
      </div>
    </div>

    <div class="panel">
      <h2>Portfolio Basket Lab</h2>
      <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 14px;">
        Select setups on the left to evaluate combined multi-pair portfolio metrics across 13.5 years of MT5 real-tick data.
      </p>

      <div class="metric-grid">
        <div class="metric-card" style="grid-column: span 2; background: rgba(46, 160, 67, 0.1); border-color: rgba(46, 160, 67, 0.4);">
          <div class="metric-label" style="color: var(--green); font-weight: 600;">Total Historical Net Profit</div>
          <div class="metric-val" id="labNet" style="color: var(--green); font-size: 25px;">+$0</div>
        </div>
        <div class="metric-card">
          <div class="metric-label">Composite Sharpe</div>
          <div class="metric-val accent" id="labSharpe">0.00</div>
        </div>
        <div class="metric-card">
          <div class="metric-label">LR Curve Smoothness</div>
          <div class="metric-val gold" id="labLr">0.000</div>
        </div>
        <div class="metric-card">
          <div class="metric-label">Composite Profit Factor</div>
          <div class="metric-val" id="labPf">0.00</div>
        </div>
        <div class="metric-card">
          <div class="metric-label">Payoff Ratio (R:R)</div>
          <div class="metric-val" id="labRr">0.0x</div>
        </div>
        <div class="metric-card">
          <div class="metric-label">Diversified Max DD</div>
          <div class="metric-val" id="labDd" style="color: var(--red);">$0</div>
        </div>
        <div class="metric-card">
          <div class="metric-label">Return / DD (Recovery)</div>
          <div class="metric-val accent" id="labRecovery">0.0x</div>
        </div>
      </div>

      <div id="basketSummary" style="font-size: 12px; color: var(--text-muted); margin-bottom: 12px; line-height: 1.5;">
        No setups selected.
      </div>

      <a href="https://ideavanta.com" target="_blank" class="cta-button">
        Explore Research & VantaBox EA on IdeaVanta.com
      </a>
      <a href="https://discord.gg/6q2gsDvae" target="_blank" class="cta-button cta-discord">
        Join IdeaVanta Research Community (Discord)
      </a>
      <p style="font-size: 11px; color: var(--text-muted); margin-top: 12px; line-height: 1.4;">
        ⚖️ <strong>Disclaimer:</strong> Provided strictly for educational and quantitative software research. Not financial or investment advice. Historical MT5 simulations do not guarantee future results.
      </p>
    </div>
  </div>

  <script>
    let rawProfiles = [];
    let selectedIndices = new Set([10, 14, 26]);

    async function loadData() {
      const res = await fetch('/api/profiles');
      rawProfiles = await res.json();
      renderTable();
      calculateBasket();
    }

    function renderTable() {
      const pair = document.getElementById('pairFilter').value;
      const risk = document.getElementById('riskFilter').value;
      const tbody = document.getElementById('tableBody');
      tbody.innerHTML = '';

      let count = 0;
      rawProfiles.forEach((p, idx) => {
        if (pair && p.pair !== pair) return;
        if (risk && !p.setup.includes(risk)) return;
        count++;

        const tr = document.createElement('tr');
        const checked = selectedIndices.has(idx) ? 'checked' : '';
        const sharpe = p.sharpe_ratio ? p.sharpe_ratio.toFixed(2) : 'N/A';
        const lr = p.lr_correlation ? p.lr_correlation.toFixed(4) : 'N/A';
        const rr = p.payoff_ratio ? p.payoff_ratio.toFixed(2) + 'x' : 'N/A';
        tr.innerHTML = `
          <td><input type="checkbox" ${checked} onchange="toggleSelect(${idx})"></td>
          <td><strong>${p.pair}</strong></td>
          <td>${p.setup}</td>
          <td class="mono positive">${p.profit_factor.toFixed(2)}</td>
          <td class="mono accent">${sharpe}</td>
          <td class="mono gold">${lr}</td>
          <td class="mono">${rr}</td>
          <td class="mono">${p.win_rate}</td>
          <td class="mono">${p.trades.toLocaleString()}</td>
          <td class="mono" style="color:var(--red);">${p.max_dd}</td>
          <td class="mono positive">${p.reported_net}</td>
        `;
        tbody.appendChild(tr);
      });
      document.getElementById('totalCount').innerText = `${count} Profiles`;
    }

    function toggleSelect(idx) {
      if (selectedIndices.has(idx)) selectedIndices.delete(idx);
      else selectedIndices.add(idx);
      calculateBasket();
    }

    function toggleSelectAll() {
      const chk = document.getElementById('selectAll').checked;
      if (chk) rawProfiles.forEach((_, idx) => selectedIndices.add(idx));
      else selectedIndices.clear();
      renderTable();
      calculateBasket();
    }

    function filterData() {
      renderTable();
    }

    async function calculateBasket() {
      const indices = Array.from(selectedIndices);
      if (indices.length === 0) {
        document.getElementById('labNet').innerText = '+$0';
        document.getElementById('labSharpe').innerText = '0.00';
        document.getElementById('labLr').innerText = '0.000';
        document.getElementById('labPf').innerText = '0.00';
        document.getElementById('labRr').innerText = '0.0x';
        document.getElementById('labRecovery').innerText = '0.0x';
        document.getElementById('labDd').innerText = '$0';
        document.getElementById('basketSummary').innerText = 'No setups selected.';
        return;
      }

      const res = await fetch('/api/simulate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ indices })
      });
      const data = await res.json();

      document.getElementById('labNet').innerText = data.total_reported_net;
      document.getElementById('labSharpe').innerText = data.composite_sharpe_ratio;
      document.getElementById('labLr').innerText = data.composite_lr_correlation;
      document.getElementById('labPf').innerText = data.composite_profit_factor;
      document.getElementById('labRr').innerText = data.composite_payoff_ratio;
      document.getElementById('labRecovery').innerText = data.recovery_factor + 'x';
      document.getElementById('labDd').innerText = '$' + Math.round(data.estimated_max_dd).toLocaleString();
      const ticksM = (data.total_ticks_modeled / 1e6).toFixed(0);
      document.getElementById('basketSummary').innerHTML = `
        Active Basket: <strong>${data.num_setups} setups</strong> across <strong>${data.unique_pairs.join(', ')}</strong><br>
        Trades: <code>${data.total_historical_trades.toLocaleString()} (${data.composite_win_rate} WR)</code> · Real Ticks: <code>${ticksM}M+</code>
      `;
    }

    window.onload = loadData;
  </script>
</body>
</html>
"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/" or parsed.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(HTML_PAGE.encode("utf-8"))
        elif parsed.path == "/api/profiles":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(tester.profiles).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path == "/api/simulate":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            payload = json.loads(body.decode("utf-8"))
            indices = payload.get("indices", [])
            result = tester.simulate_portfolio(indices)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(result).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

def run_server():
    server = HTTPServer(("127.0.0.1", PORT), Handler)
    print(f"IdeaVanta Strategy Tester running at http://127.0.0.1:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")

if __name__ == "__main__":
    run_server()
