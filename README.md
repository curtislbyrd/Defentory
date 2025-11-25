<p align="center">
  <img src="images/defentory.png" alt="Defentory" width="300"/>
  <br>
  <em><strong>Because knowing your defenses is the new offense.</strong></em>
</p>


## Why Defentory?

Most teams track ATT&CK coverage.  
**Defentory gives you D3FEND coverage** — the defensive side of the coin.

See instantly where you’re strong (Detect/Harden) and where you have blind spots (Isolate/Deceive/Restore).

Built for SOC analysts, detection engineers, and leadership who want visibility **today**.

## Features

- Full **D3FEND + ATT&CK tactic mapping** for every detection
- Real-time **coverage dashboard** with doughnut chart, progress rings, and coverage bars
- Interactive **D3FEND Heatmap** — red/yellow/green visualization of defensive maturity
- One-click **Export to CSV & JSON** (perfect for Splunk, Panther, Sigma rules, or audits)
- Clean, responsive UI with dark mode and mobile support
- Runs locally in seconds — no heavy stack required


## Quick Start

```bash
git clone https://github.com/yourusername/defentory.git
cd defentory
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install flask
python3 app.py
```

Open your browser → **http://127.0.0.1:5001**


## Tech Stack

- Python + Flask
- SQLite
- Chart.js
- CSS 

## Adding Test Data

add_test_data.py is used to generate test data for testing of this application

## Contributing

Pull requests are welcome! Especially:
- Technique-level D3FEND mapping
- PDF report export
- Sigma rule generation
- Authentication / multi-user support

## License

MIT License — feel free to use, modify, and deploy internally or publicly.

---

*MITRE D3FEND® is a registered trademark of The MITRE Corporation. This is an independent community project and is not endorsed by or affiliated with MITRE.*

---

