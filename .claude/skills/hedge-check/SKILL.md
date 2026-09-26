---
name: hedge-check
description: Suggest which TradFi pair to open as a delta-neutral hedge between Variational (Omni) and Extended right now, minimizing cost per point. Use when the user asks to check/scan hedge pairs, which pair to open, "check cặp hedge", "nên mở cặp nào", or asks about closing an open VAR/EXT hedge.
---

1. Run `python3 hedge-scan/scan.py` from the repo root. Pass what the user gave you:
   - size per leg: `--size 20000` (the user trades $10k–20k per leg, leverage included; default 15k)
   - holding time in hours: `--hold 24`
   - specific tickers: `--only AAPL,XAG`
   - an open position to close: `--exit AAPL:short-var` (short-var = short on Variational, long on Extended)
   By default only the user's listed tickers are scanned (`listed_only` + `var_points_per_m` in config; CL excluded).
   Add `--all` so closed listed pairs still show; use `--any` only if the user asks to look beyond the list.
   If the user gives a size range, also run the two ends (`--size 10000`, `--size 20000`) and say which is cheaper per point.
2. Reply in Vietnamese, short:
   - the pick: ticker, which side on which exchange (e.g. "SHORT AAPL trên Variational + LONG AAPL_24_5 trên Extended"), size,
     estimated round-trip cost ($ and bps), points and $/pt, then 1–2 runners-up;
   - the reason (spread, funding, basis) and any warning the tool printed (off-hours session, volatility, unverified points);
   - remind them to compare the Variational UI quote with the tool's estimate before clicking, since VAR spread at 10–20k is interpolated.
3. If nothing is tradable or the US session is closed, say so and give the next good window (US regular session, 20:30–03:00 ICT in summer, 21:30–04:00 in winter).

Cost model, assumptions and config keys: `hedge-scan/README.md`. Points per $1M and boost live in `hedge-scan/config.json`; update them when the user reports real numbers.
