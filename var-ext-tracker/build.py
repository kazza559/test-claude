#!/usr/bin/env python3
"""Inject a publish-time snapshot (fallback when the live database is unavailable) into the dashboard template."""
import json, sys
tpl, latest, series, out = sys.argv[1:5]
fb = {"latest": json.load(open(latest)), "rows": json.load(open(series))["rows"]}
html = open(tpl).read().replace("/*__FALLBACK__*/null", json.dumps(fb, separators=(",", ":")))
open(out, "w").write(html)
print(out, len(html), "bytes")
