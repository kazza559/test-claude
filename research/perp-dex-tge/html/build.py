#!/usr/bin/env python3
"""Build the self-contained HTML report: report.template.html + chart_data.json -> reports/*.html."""
import json
import pathlib

here = pathlib.Path(__file__).resolve().parent
repo = here.parents[2]
template = (here / "report.template.html").read_text(encoding="utf-8")
data = json.loads((here / "chart_data.json").read_text(encoding="utf-8"))
blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
assert template.count("/*__DATA__*/") == 1
out = repo / "reports" / "Phân tích perp DEX - pattern TGE và định giá.html"
out.write_text(template.replace("/*__DATA__*/", blob), encoding="utf-8")
print(out, out.stat().st_size, "bytes")
