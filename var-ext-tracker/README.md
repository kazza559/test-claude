# VAR · EXT TGE Watch

Dashboard tracking the expected FDV 24 hours after listing (D+1) for Variational (VAR) and Extended (EXT)
until their TGEs. Published as a claude.ai artifact that reads its numbers from the artifact database:

- Artifact: https://claude.ai/artifact/7zoVsn9D4kHbJoF24CLkhj
- `state/latest`: full latest snapshot (metrics, Polymarket curves, model breakdown, market context, peers)
- `series/daily`: `{"rows": {"YYYY-MM-DD": {...}}}`, one row per day (merged with `update`, so appending a day never rewrites history)

## Files

- `collect.py`: collector (public APIs only: Variational, Extended, DefiLlama, CoinGecko, Polymarket, alternative.me)
- `dashboard.template.html`: the page; `build.py` injects a publish-time snapshot used when the database is unavailable

## Daily update

```bash
OUT=$(mktemp -d)
# 1. optional: read series/daily from the artifact database into $OUT/series.json (fallback for the 30-day volume)
python3 collect.py latest "$OUT" "$OUT/series.json"
# 2. write to the artifact database:
#    set    state/latest  <- $OUT/latest.json
#    update series/daily  <- $OUT/row.json   (adds today's row)
```

Rebuild history from scratch (about 185 days): `python3 collect.py history "$OUT" 185`.
CoinGecko's free API rate-limits hard; set `VOL_CACHE_DIR` to a directory holding `vc365_<exchange>.json`
volume charts to avoid refetching them.

## Model

D+1 calibration multiples = FDV 24h after listing / 30-day average metric before TGE, from LIT (2025-12-30),
EDGE (2026-03-31), GRVT (2026-07-30) and BP (2026-03-23). For each method (OI, TVL, 30-day volume, annualized fees)
the model takes the median multiple times the token's current metric, then the median across methods.
The VAR history series uses OI and volume only because Variational TVL has no history.
No market-regime multiplier is applied: within-token checks from Fear (June 2026) to Greed (September 2026)
showed valuation multiples moving only about 0.9–1.35x, with wide dispersion.

Polymarket median = linear interpolation of the "FDV above ___ one day after launch" survival curve at 50%.
It is not a traded price and not a probability-weighted mean.

Not investment advice.
