"""Refresh stats.json, which gen.py reads for the CV's citation table.

Google Scholar citations are fetched automatically. ResearchGate blocks scripts,
so pass the Research Interest Score by hand:

    python update_stats.py              # refresh Scholar citations only
    python update_stats.py --rg 112.2   # also set the ResearchGate score

Then rebuild:  python gen.py && python gen.py --white
"""
import argparse, json, re, urllib.request
from pathlib import Path

SCHOLAR = "https://scholar.google.com/citations?user=_Q0VXwsAAAAJ&hl=en"
FILE = Path(__file__).with_name("stats.json")

ap = argparse.ArgumentParser()
ap.add_argument("--rg", help="ResearchGate Research Interest Score, e.g. 112.2")
args = ap.parse_args()

stats = json.loads(FILE.read_text(encoding="utf-8"))
if args.rg:
    stats["researchgate_score"] = args.rg

try:
    req = urllib.request.Request(SCHOLAR, headers={"User-Agent": "Mozilla/5.0"})
    html = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "ignore")
    cells = re.findall(r'gsc_rsb_std">(\d+)<', html)
    if not cells:
        raise ValueError("citation table not found (Scholar may be showing a captcha)")
    stats["scholar_citations"] = cells[0]
except Exception as e:
    print("Could not refresh Google Scholar automatically:", e)

FILE.write_text(json.dumps(stats, indent=2) + "\n", encoding="utf-8")
print("stats.json ->", stats)
