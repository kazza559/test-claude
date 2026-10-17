# Instruments and position structures for a ~$7K Vietnam-based trader (crypto bull leg, Q4 2026 – Q1 2027)

All market data was pulled on **2026-10-17, ~03:23 UTC** unless stated. At that time the Deribit BTC index was **$81,400**, ETH **$2,421.65** and SOL **$104.54**. Hyperliquid (HL) marks were BTC 81,491, ETH 2,423.7, SOL 104.61, HYPE 79.901, LIT 3.1992, BNB 720.94 and LINK 12.311. Scripts are in `/tmp/claude-0/-home-user-test-claude/8ec8a334-85ed-54af-babc-62d7e4c0704b/scratchpad/research/instruments/` (`pull_hl.py`, `pull_options.py`, `analyze1-3.py`, `risk_math.py`, `basket_mc.py`, `implied_probs.py`, `hip3_meta.py`). Raw JSON and outputs are in its `data/` subfolder (`risk_math.out`, `basket_mc.out`, `analyze3.out`, `pull_hl.log`).

## 1. Perps on Hyperliquid: margin, leverage, fees, funding, liquidation/ADL, liquidation distance, funding and volatility drag

### Takeaway
- **Costs are small:** base fees are 0.045% taker and 0.015% maker.
- **Margin rule:** maintenance margin is half the initial margin at the coin's max leverage. Current max leverage and the resulting maintenance margin are:
  - BTC: 40x, 1.25%
  - ETH: 25x, 2%
  - SOL: 20x, 2.5%
  - HYPE, BNB, LINK: 10x, 5%
  - LIT: 5x, 10%
- **Liquidation distance for a long:** 2x is about 44–49% away, 3x about 26–33%, 5x about 11–19%.
- **Funding is the real carry.** The baseline is about 11% APR. Over the last 90 days it averaged 7–12% APR. In past bull legs it reached 15–36% APR on majors and 55–119% on HYPE.
- **The trader's resting basket (if fully filled):** $11.5K notional on $6.4K equity, which is 1.8x.
  - Liquidating the account takes a ~53% uniform drop from entries.
  - Simulated chance of liquidation over 160 days: about 8% if prices drift flat, 25% at −30% drift, about 2% at +40%.
  - At 2.7x the flat-drift figure jumps to about 35%. At 0.9x it is about 0%.

### Cited Findings
**Max leverage and margin tiers (2026-10-17)** — [HL info API `metaAndAssetCtxs` / `meta`](https://api.hyperliquid.xyz/info)
- BTC 40x (tiered: 40x up to $150M notional, then 20x); ETH 25x (15x above $100M); SOL 20x (10x above $70M).
- HYPE and LINK 10x (5x above $20M); BNB 10x (5x above $3M); LIT 5x, single tier (margin table id 5).
- Of the 178 live main-dex perps, 88 cap at 3x, 56 at 5x, 30 at 10x, 2 at 20x (SOL, XRP), 1 at 25x (ETH) and 1 at 40x (BTC).

**Margin modes and rules** — [HL docs: Margining](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/margining)
- Cross is the default and shares collateral across positions. Isolated restricts collateral to one asset. Strict isolated does not allow margin removal. HIP-3 "no cross" markets are isolated only.
- Leverage is checked only when a position opens; after that, the user must monitor it.
- Unrealized PnL on cross positions can be used as initial margin for new positions.
- Withdrawing margin requires remaining margin ≥ max(initial margin, 10% of total position notional).
- "The maintenance margin is currently set to half of the initial margin at max leverage."
- With a unified account or portfolio margin, cross positions on DEXs that share the same collateral also share margin.

**Liquidation mechanics** — [HL docs: Liquidations](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/liquidations)
- Maintenance margin runs from about 1.25% to 16.7% of notional, depending on the asset's max leverage (40x down to 3x).
- Liquidation price formula: `liq_price = price − side × margin_available / position_size / (1 − l × side)`, where l = 1/maintenance leverage.
- For cross, the liquidation price "is independent on the leverage set". For isolated, it depends on the leverage set.
- Positions above $100K are liquidated in 20% chunks, with a 30-second cooldown.
- Positions below 2/3 of maintenance margin can be taken over by the liquidator vault (part of HLP).
- On a cross backstop liquidation, all cross positions and cross margin transfer to the liquidator. With no isolated positions, the trader ends with zero equity. Maintenance margin is not returned.
- Liquidations use the mark price, which blends CEX prices with HL book state.

**Fees** — [HL info API `userFees` feeSchedule](https://api.hyperliquid.xyz/info), 2026-10-17
- Base perps: taker 0.045%, maker 0.015%. Spot: taker 0.07%, maker 0.04%.
- VIP volume tiers: from $5M at 0.040%/0.012% down to above $7B at 0.024%/0%.
- Maker rebates of −0.001% to −0.003% for maker volume share above 0.5%/1.5%/3%.
- Referral discount 4%; HYPE staking discounts from 5% to 40%.
- Builder-deployed HIP-3 markets reportedly carry 2x base fees — [bex.co, 2026-04-28](https://bex.co/blog/2026/04/28/perp-dex-cohort-2026-lighter-airdrop-hyperliquid-long-tail) (secondary).

**Funding mechanics** — [HL docs: Funding](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/funding)
- Formula: F = average premium + clamp(interest − premium, −0.0005, 0.0005).
- Interest component: 0.01% per 8h, i.e. 0.00125% per hour, about **10.95% APR** paid by longs when the premium is near zero.
- Paid hourly; capped at 4% per hour; computed on oracle-price notional.

**Current and recent funding (annualized, longs pay when positive)** — [HL info API `metaAndAssetCtxs` / `fundingHistory`](https://api.hyperliquid.xyz/info), via `analyze1.py`

| Coin | Current hourly rate | 30-day mean | 90-day mean | 200-day mean | Paid by a long, last 90 days (% of notional) |
|---|---|---|---|---|---|
| BTC | 11.0% | 8.9% | 8.3% | 5.9% | 2.05% |
| ETH | 1.8% | 9.3% | 8.8% | 6.6% | 2.18% |
| SOL | −0.5% | 8.4% | 6.9% | 3.9% | 1.69% |
| HYPE | 7.3% | 10.1% | 9.9% | 9.4% | 2.44% |
| LIT | −12.8% | 10.6% | 11.8% | 11.5% | 2.91% |
| BNB | 7.4% | 8.9% | 9.5% | 8.0% | — |
| LINK | 0.3% | 10.1% | 10.9% | 10.2% | — |

**Funding in past bull legs (mean annualized)** — [HL info API `fundingHistory`](https://api.hyperliquid.xyz/info), via `risk_math.py`

| Window | BTC | ETH | SOL | HYPE |
|---|---|---|---|---|
| Nov–Dec 2024 | 30.2% (peak 7-day 56%) | 33.9% (61%) | 35.9% (71%) | 118.8% (155%) |
| Jan 2025 | 16.6% | 11.8% | 11.1% | 55.3% |
| Jul–Aug 2025 | 15.4% | 16.6% | 15.8% | 20.4% |

**Carry on Deribit dated futures vs the index (81,400)** — [Deribit public API, BTC futures](https://www.deribit.com/api/v2/public/get_book_summary_by_currency?currency=BTC&kind=future)
- Dec-26 at 82,275 (+1.07%, about 5.6% annualized); Mar-27 at 83,321 (+2.36%, about 5.4%); Jun-27 at 84,435 (+3.73%, about 5.4%).
- Locking exposure there costs roughly half of HL's ~11% funding baseline. This is a computed comparison.

**Auto-deleveraging rules** — [HL docs: Auto-deleveraging](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/auto-deleveraging)
- ADL triggers when an account's value or an isolated position's value becomes negative.
- Profitable opposite-side users are ranked by (mark/entry) × (notional/account value).
- Their positions are closed at the previous mark price against the underwater user.

**ADL on 2025-10-10/11**
- It was HL's first cross-margin ADL in more than two years. The founder said the venue had "100% uptime with zero bad debt" — [WuBlockchain](https://wublock.substack.com/p/hyperliquid-activates-cross-margin)
- Academic analysis — [arXiv 2512.01112](https://arxiv.org/html/2512.01112v2):
  - From 10:21 UTC there were at least 40 ADL waves in about 10–12 minutes, closing about $2.1B of positions. The time is as stated in the paper; the crash is widely reported in the evening UTC of 2025-10-10, so treat the clock time with caution.
  - 34,983 ADL executions hit 19,337 wallets across 162 tickers.
  - True negative equity was about $23.2M. The authors estimate about $653M of overshoot ("unnecessary haircuts" on winners, about 28x their optimal policy).
- HLP's all-time PnL rose from $80.33M (2025-10-01) to $121.76M (2025-10-15), about +$41M — [HL info API `vaultDetails`](https://api.hyperliquid.xyz/info).

**Wick and drawdown history (HL daily candles, 2025-08-23 → 2026-10-17)** — [HL info API `candleSnapshot`](https://api.hyperliquid.xyz/info)

| Coin | 2025-10-10 low vs prior close | Peak → trough in window | Max drawdown | Worst forward 30d / 90d drawdown | Realized vol 30d / 90d |
|---|---|---|---|---|---|
| BTC | −17.1% | 126,297 (2025-10-06) → 57,768 (2026-07-01) | −54.3% | −38% / −43% | 37% / 38% |
| ETH | −25.8% | 4,960 → 1,504 (2026-06-06) | −69.7% | — | 43% / 52% |
| SOL | −37.8% | 253.6 (2025-09-18) → 60.06 (2026-06-06) | −76.3% | −54% / −60% | 59% / 56% |
| HYPE | −27.7% | low 20.46 (2026-01-21), high 97.999 (2026-09-23) | — | −46% / −60% | 60% / 71% |
| LIT | n/a (listed later) | 0.78 (2026-03-31) → 5.59 (2026-09-24) | — | −61% / −78% | 96% / 107% |
| BNB | −35.5% | — | — | — | 33% / 36% |
| LINK | −65.4% | — | — | — | 74% / 70% |

**Liquidation distance for a long (computed; `risk_math.py`).** Formula: d = (1/L − mm)/(1 − mm). L is effective leverage: notional/account equity for cross, the leverage set for isolated. Inputs are the API max-leverage values and the docs' maintenance-margin rule.

| Coin | 2x | 3x | 5x |
|---|---|---|---|
| BTC | 49.4% | 32.5% | 19.0% |
| ETH | 49.0% | 32.0% | 18.4% |
| SOL | 48.7% | 31.6% | 17.9% |
| HYPE, BNB, LINK | 47.4% | 29.8% | 15.8% |
| LIT | 44.4% | 25.9% | 11.1% |

**Trader's resting orders if all fill (computed; `risk_math.py`).** The notional split is **assumed equal** across the five orders; the actual split is unknown.
- Positions: HYPE $4.6K (average entry 71.41), SOL $4.6K (91.37), LIT $2.3K (2.6999).
- 1.80x effective leverage on $6.4K equity; maintenance margin at entry $575.
- A **53.3% uniform drop from entries** liquidates the whole cross account (HYPE ≈ 33.3, SOL ≈ 42.7, LIT ≈ 1.26).
- Replaying the 2025-10-10-type wick at entries (SOL −37.8%, HYPE −27.7%, LIT −32.1%) leaves $2,649 of equity against $394 maintenance, so the account survives. The same wick at 2x the notional (3.6x effective) liquidates it.
- Distance of the orders below 2026-10-17 marks: HYPE 74/69 = −7.4%/−13.6%; SOL 95/88 = −9.2%/−15.9%; LIT 2.6999 = −15.6%.

**Monte Carlo, single asset, 160 days to 2027-03-26 (computed; `risk_math.py`).**
- Method: bootstrapped HL daily returns with intraday-low wicks, demeaned, plus a scenario drift; 11% APR funding; 4,000 paths.
- Probability of liquidation:

| Asset, drift | 2x | 3x | 5x |
|---|---|---|---|
| BTC, flat | 2.0% | 18.6% | 47.6% |
| BTC, +40% | 0.1% | 2.6% | 16.4% |
| BTC, −30% | 19.9% | 59.8% | 85.4% |
| SOL, flat | 17.3% | 46.7% | 71.7% |
| SOL, +40% | 6.1% | 26.7% | 51.0% |
| HYPE, flat | 29.1% | 56.9% | 78.5% |
| HYPE, +40% | 16.1% | 39.3% | 65.3% |

- Median worst drawdown from start (flat drift): BTC −18%, SOL −30%, HYPE −35%.
- **Caveat:** the sample (Aug 2025 → Oct 2026) includes the Oct 2025 crash and a high-vol 2026 regime. HYPE's full-window realized vol is 92% against current implied vol of about 55–57%, so liquidation odds for alts are likely overstated relative to today's implied vols.

**Monte Carlo, the trader's actual basket in one cross account (computed; `basket_mc.py`).**
- Method: joint bootstrap of same-day HYPE/SOL/LIT returns over 299 overlapping days (2025-12-22 → 2026-10-17); 11% APR funding; liquidation checked against simultaneous intraday lows.

| Notional (effective leverage) | Drift | P(liquidation) | Equity p5 / p50 / p95 |
|---|---|---|---|
| $11.5K (1.8x, as planned) | −30% | 25.0% | — / $2.8K / — |
| $11.5K (1.8x) | flat | 8.4% | $0 / $6.6K / $20.7K |
| $11.5K (1.8x) | +40% | 1.9% | — / $11.6K / — |
| $11.5K (1.8x) | +80% | 0.5% | — / $16.4K / — |
| $17.25K (2.7x) | flat | 34.9% | — |
| $17.25K (2.7x) | +40% | 15.2% | — |
| $23K (3.6x) | flat | 53.8% | — |
| $23K (3.6x) | +40% | 31.4% | — |
| $5.75K (0.9x) | any of −30% to +80% | 0% | flat-drift p50 $6.45K |

### Inferences
- **Cross vs isolated for a no-stop trader.**
  - Under cross, what matters is total equity against total notional. Every dollar of idle USDC left in the cross account pushes all liquidation prices away, so 2x "cross" with spare USDC really behaves like 1.x.
  - Isolated caps the loss on each position at its margin, but each position then dies at its own 2x/3x distance (about 47% for HYPE at 2x).
  - With correlated alts, a crash hits all positions at once. Isolated mainly prevents one bad coin from draining the rest. It does not stop a market-wide wick.
- **Without stops, the liquidation price is the stop.** A backstop liquidation also forfeits the remaining maintenance margin.
- **Funding is the main drag on a fixed-size long.**
  - At 11% APR on the planned $11.5K notional: about $105/month, or about $527 (8.2% of equity) over 5 months.
  - At a bull-leg 30% APR: about $1,438 (22.5% of equity) over 5 months.
  - Trading fees on the planned orders (maker in, taker out) are about $7 in total, which is negligible.
- **Volatility drag.**
  - A fixed-notional perp has a linear payoff, so there is no classic volatility drag. Path risk comes from the liquidation barrier.
  - Drag appears when the trader re-levers to a constant leverage (topping up margin, adding to winners, resizing to "2x" again). Its cost relative to L times the asset's log return is about (L² − L)·σ²/2 per year:
    - 2x on BTC (σ ≈ 37–43%): about 14–18% per year.
    - 2x on SOL/HYPE (σ ≈ 55–70%): about 30–49% per year.
    - 3x on those alts: about 91–147% per year.
    - Over 5 months, multiply by 5/12.
- **ADL cuts winners on the upside.** For a long-only trader, ADL is mainly an upside risk: if shorts go bankrupt in a violent squeeze, profitable high-leverage longs are force-closed at the prior mark, so gains are cut at the best moment. In crashes the risk is liquidation, plus HL's mark-price wick (LINK printed −65% on 2025-10-10).
- **Leverage and coin choice dominate risk of ruin.** 1.8x on high-vol alts held 5 months without stops carries a non-trivial ruin probability (about 1-in-12 if flat, about 1-in-4 at −30% drift). The same capital at about 0.9x is essentially un-liquidatable on these paths. BTC at 2x is far safer (about 2% if flat) than HYPE at 2x (about 29% if flat).

### Gaps
- HL's mark-price formula weights were not fetched. Whether funds supplied to HyperCore lending still count as perp margin in "unified account/portfolio margin" mode was not verified.
- HL docs do not state the ADL history beyond 2025-10-10. I found no official HL post-mortem with exact ADL totals; the figures above come from WuBlockchain and an arXiv preprint.
- The Monte Carlo is a bootstrap from one regime and ignores ADL, funding spikes and gaps beyond daily lows. Treat it as a relative comparison, not a forecast.

## 2. Options: access for Vietnam residents, indicative prices and IVs, calls vs 2x perps

### Takeaway
- **Deribit is the deep venue.**
  - BTC and ETH options run to Sep-2027.
  - USDC-settled SOL and HYPE options exist only to **25-Dec-2026**.
  - Vietnam does not appear in the restricted-jurisdiction list surfaced from Deribit's support page, but I could not load the page directly, so confirm at KYC.
- **OKX quotes BTC options comparable to Deribit, including USD-margined ones.** OKX SOL options are only weekly.
- **Prices (BTC ≈ $81.4K):**
  - BTC Mar-27 100K/110K/120K calls cost about $3.1K/$1.75K/$1.0K per BTC, IV 38–40%.
  - Dec-26 strikes cost about $0.82K/$0.30K/$0.15K, IV 37–42%.
- **Calls vs 2x perps:** a 25%-of-bankroll call position caps the loss at about 24%, versus up to 100% for 2x perps. It beats 2x perps only if BTC is above about $111K (100K strike) or $117K (110K strike) at the 26-Mar-2027 expiry.
- **Market-implied odds:** about 20% that BTC is above 100K at end-March 2027, and about 10% that it is above 100K at end-December 2026.

### Cited Findings
**Deribit BTC calls** — [Deribit public API, BTC options](https://www.deribit.com/api/v2/public/get_book_summary_by_currency?currency=BTC&kind=option)
- Inverse contracts: premium in BTC, converted at the underlying/forward price. Breakevens are vs spot $81.4K.

| Expiry | Strike | Bid / ask (USD) | Native bid / ask (BTC) | Mark IV | OI (BTC) | Breakeven at expiry |
|---|---|---|---|---|---|---|
| 27-Nov-26 | 100K | $262 / $295 | — | 37.6% | — | — |
| 25-Dec-26 (fwd 82,275) | 90K | $2,304 / $2,386 | — | 35.6% | — | — |
| 25-Dec-26 | 100K | $740.5 / $822.8 | 0.009 / 0.010 | 36.8% | 6,027 | ~$100.8K (+23.9%) |
| 25-Dec-26 | 110K | $279.7 / $304.4 | — | 39.1% | — | ~$110.3K (+35.5%) |
| 25-Dec-26 | 120K | $123.4 / $148.1 | — | 42.5% | 5,957 | ~$120.1K (+47.6%) |
| 26-Mar-27 (fwd 83,321) | 90K | $5,624 / $5,708 | — | 37.65% | — | — |
| 26-Mar-27 | 100K | $3,041 / $3,125 | 0.0365 / 0.0375 | 37.8% | 1,382 | ~$103.1K (+26.7%) |
| 26-Mar-27 | 110K | $1,666 / $1,750 | — | 38.6% | 1,477 | ~$111.7K (+37.3%) |
| 26-Mar-27 | 120K | $958 / $1,000 | — | 39.6% | 829 | ~$121.0K (+48.6%) |
| 26-Mar-27 | 150K | $258 / $283 | — | 44.2% | — | — |
| 25-Jun-27 | 100K | $5,362 / $5,531 | — | 38.3% | — | — |

- BTC option open interest is concentrated on 30-Oct-26 (149,751 BTC) and 25-Dec-26 (130,937 BTC).

**Deribit volatility index (DVOL)** — [Deribit API `get_volatility_index_data`](https://www.deribit.com/api/v2/public/get_volatility_index_data?currency=BTC&resolution=86400&start_timestamp=1757635200000&end_timestamp=1792207400000)
- BTC DVOL is 37.6 (range over the past ~400 days: 33.6 on 2026-09-17 to 82.6 on 2026-02-05).
- ETH DVOL is 51.4 (range 46.1 to 95.8).

**Greeks per 1 BTC contract (Aevo marks, which mirror Deribit)** — [Aevo API markets](https://api.aevo.xyz/markets?asset=BTC&instrument_type=OPTION)

| Contract | Mark | Delta | Theta per day | Vega per vol point |
|---|---|---|---|---|
| Mar-27 100K C | $3,096 | 0.273 | −$21.7 | $183.5 |
| Dec-26 100K C | $785 | 0.128 | −$19.9 | $74.9 |
| Mar-27 110K C | — | 0.169 | −$16.7 | $139 |

**Deribit ETH calls** — [Deribit public API, ETH options](https://www.deribit.com/api/v2/public/get_book_summary_by_currency?currency=ETH&kind=option)

| Expiry | 2400 (ATM) | 3000 | 3500 | 4000 |
|---|---|---|---|---|
| 25-Dec-26 | $228 / $232, IV 49.7% | $54.9 / $57.4, IV 50.8%, OI 22,867 ETH | $18.3 / $20.8, IV 54.7%, OI 31,539 | $7.8 / $9.0, IV 59.2% |
| 26-Mar-27 | — | $164 / $167, IV 52.0% | $86 / $90, IV 53.3% | $49 / $52, IV 55.3% |

**Deribit SOL (USDC-settled, linear; index 104.54)** — [Deribit public API, USDC options](https://www.deribit.com/api/v2/public/get_book_summary_by_currency?currency=USDC&kind=option)

| Contract | Bid / ask | IV | OI (SOL) |
|---|---|---|---|
| 25-Dec-26 100C | 12.3 / 13.1 | 55.1% | — |
| 25-Dec-26 120C | 4.9 / 5.2 | 55.7% | 7,360 |
| 25-Dec-26 130C | 3.2 / 3.4 | 57.7% | — |
| 25-Dec-26 150C | 1.7 / 1.8 | 64.4% | 32,800 |
| 25-Dec-26 200C | 0.4 / 0.6 | 76.5% | — |

- The latest SOL expiry listed is 25-Dec-26.

**Deribit HYPE (USDC-settled; underlying 81.19)** — same source
- 25-Dec-26 calls:

| Strike | Bid / ask | IV |
|---|---|---|
| 80C | 8.24 / 8.26 | 54.7% |
| 90C | 4.53 / 4.55 | 55.4% |
| 100C | 2.44 / 2.46 | 56.7% (OI 6,640 HYPE) |
| 110C | 1.36 / 1.38 | 58.6% |
| 120C | 0.79 / 0.81 | 60.7% |
| 150C | 0.23 / 0.256 | 68.7% |

- 25-Dec-26 puts: 70P 2.96/2.98 (IV 55.2%, OI 17,500); 60P 0.94/0.96.
- Total Dec-26 HYPE option OI is 343,110 HYPE. Expiries run only to 25-Dec-26.
- Deribit's USDC options book also lists BTC_USDC, ETH_USDC, XRP_USDC, AVAX_USDC and TRX_USDC.

**OKX** — [OKX tickers](https://www.okx.com/api/v5/market/tickers?instType=OPTION&uly=BTC-USD), [OKX opt-summary BTC](https://www.okx.com/api/v5/public/opt-summary?uly=BTC-USD), [OKX opt-summary SOL](https://www.okx.com/api/v5/public/opt-summary?uly=SOL-USD)
- The public API was reachable. BTC-USD expiries run to 24-Sep-2027.
- Dec-26: 100K C 0.009/0.0095 BTC (mark vol 36.8%); 110K C 0.0035/0.0036 (39.0%); 120K C 0.0016/0.0017 (42.1%).
- Mar-27: 100K/110K/120K C 0.0365/0.0375, 0.020/0.021 and 0.0115/0.012.
- USD-margined "BTC-USD_UM" options also trade (Mar-27 100K C bid/ask $2,990/$3,105).
- OKX SOL options were listed only to 23-Oct-2026.

**Other venues**
- The Binance options API returned HTTP 451 ("restricted location") and Bybit returned 403 from this US-based proxy. That says nothing about Vietnam access, but no prices could be pulled — [Binance eapi](https://eapi.binance.com/eapi/v1/mark), [Bybit v5](https://api.bybit.com/v5/market/tickers?category=option&baseCoin=BTC)
- Derive (ex-Lyra) public API returned HTTP 503 on 2026-10-17 — [api.lyra.finance](https://api.lyra.finance/public/get_all_currencies)
- Aevo's API was live, with BTC option expiries through 24-Sep-27 — [Aevo API](https://api.aevo.xyz/markets?asset=BTC&instrument_type=OPTION)

**Deribit access rules** — [Deribit support: Restricted Jurisdictions](https://support.deribit.com/hc/en-us/articles/25944487427741-Restricted-Jurisdictions) (search-surfaced; direct fetch returned 403)
- Named restrictions: Belarus, Canada, Cuba, Iran, Iraq, Japan, North Korea, Libya, Myanmar, Puerto Rico, Guam, American Samoa, Somalia, South Sudan, Sudan, Syria, and the sanctioned regions of Ukraine. UAE and Panama are spot-only for retail; the UK bars retail clients. **Vietnam was not among the names surfaced.**
- KYC is mandatory (government ID plus proof of residence). Third-party sites also say the US is blocked — [Datawallet (secondary)](https://www.datawallet.com/es/cripto/deribit-restricted-countries)

**Hyperliquid has no native options.** HIP-3 dex "mkts" lists `BVIV` (a Bitcoin volatility-index perp, 5x strict isolated, OI ≈ $0.23M) — [HL info API `metaAndAssetCtxs` (dex=mkts)](https://api.hyperliquid.xyz/info)

**Risk-neutral probabilities from Deribit marks (computed; `implied_probs.py`).** "Touch" means trading at or above the strike at any time before expiry.

| Contract | P(above at expiry) | Approx. P(touch before expiry) |
|---|---|---|
| BTC Dec-26 100K | 9.8% | 22% |
| BTC Dec-26 110K | 3.7% | 9% |
| BTC Mar-27 100K | 19.7% | 47% |
| BTC Mar-27 110K | 11.2% | 28% |
| BTC Mar-27 120K | 6.4% | 17% |
| ETH Mar-27 3000 | 23.0% | — |
| SOL Dec-26 150 | 8.1% | — |
| HYPE Dec-26 100 | 16.7% | — |
| HYPE Dec-26 120 | 5.4% | — |

**Polymarket on 2026-10-17** — [Polymarket gamma search "bitcoin price"](https://gamma-api.polymarket.com/public-search?q=bitcoin%20price&limit_per_type=50&events_status=active)
- "What price will Bitcoin hit in 2026?" ($76.0M volume): ↑95K 34.5%, ↑110K 10%, ↑120K 5.5%; ↓70K 39%, ↓65K 22.5%, ↓60K 16.5%.
- "When will Bitcoin hit $150k?": by 31-Mar-2027 4.5%; by 30-Jun-2027 12.5%.
- "Bitcoin all time high by Dec 31, 2026": 4.25%.

**Payoff on 2027-03-26 for a $6,400 bankroll, BTC only (computed; `risk_math.py`).**
- Perps include 11% APR funding. Call rows keep unspent USDC at 4.5% APR and use Deribit Mar-27 asks.
- $1,600 buys 0.512 BTC of 100K calls, 0.914 BTC of 110K calls or 0.28 BTC of 90K calls.

| Structure | BTC 60K | 70K | 81.45K | 90K | 100K | 110K | 120K | 150K |
|---|---|---|---|---|---|---|---|---|
| 1x perp/spot | 4,406 | 5,192 | 6,091 | 6,763 | 7,549 | 8,335 | 9,120 | 11,478 |
| 2x perp | 2,412 | 3,983 | 5,783 | 7,126 | 8,698 | 10,269 | 11,841 | 16,556 |
| 3x perp | 418 | 2,775 | 5,474 | 7,490 | 9,847 | 12,204 | 14,561 | 21,633 |
| 5x perp | 0 | 359 | 4,857 | 8,216 | 12,145 | 16,074 | 20,002 | 31,789 |
| 25% in Mar 100K C | 4,895 | 4,895 | 4,895 | 4,895 | 4,895 | 10,016 | 15,136 | 30,499 |
| 25% in Mar 110K C | 4,895 | 4,895 | 4,895 | 4,895 | 4,895 | 4,895 | 14,039 | 41,472 |
| 25% in Mar 90K C | 4,895 | 4,895 | 4,895 | 4,895 | 7,698 | 10,501 | 13,305 | 21,715 |
| 85% as 1x perp + 15% in Mar 110K C | 3,745 | 4,413 | 5,178 | 5,749 | 6,417 | 7,085 | 13,239 | 31,703 |

- Crossover vs 2x perp: about $110.7K for the 100K calls and about $117.1K for the 110K calls (computed).

### Inferences
- **Calls cap the loss but need a big move.**
  - With a 25% premium budget, the worst case is about −24% of the bankroll in every bear path, versus a possible total wipe for 2x perps at about BTC $41K at entry. That level rises to about $45K by March as roughly $617 of funding (11% APR on $12.8K for 160 days) erodes equity. This is computed.
  - The price of that floor is underperformance between about $82K and $110K. That is the most likely zone for a "first leg to ~$100K" thesis.
  - If the thesis is "BTC to ~100K", 2x perps or 1x plus a few calls pay better. If the thesis is "parabolic leg to 120K+", calls dominate.
- **Dec-26 calls are cheap lottery tickets.** 25% in Dec-26 100K calls buys about 1.94 BTC notional. At BTC 120K on 25-Dec that returns about $43.7K; at or below 100K it loses about 24%. Market odds of finishing above 100K are about 10%. Mar-27 calls give more time (P about 20%) at about 3.8x the price per contract.
- **IV is mid-range.** BTC DVOL near 38 is near the bottom of its 1-year range (33.6–82.6), so buying optionality now is relatively cheap versus history. Vega is positive: +10 vol points adds about $1,835 per Mar-27 100K contract.
- **Alt options are short and have smile cost.** SOL and HYPE options cover only the Q4 leg (to 25-Dec-26), with steep call-side smiles (HYPE 150C at 68.7% IV vs about 55% ATM), so far-OTM alt calls carry extra premium.
- **Covered calls on the existing BTC holding (outside the $7K scope).** The trader plans to sell BTC above $100K anyway. Selling Mar-27 100K calls against that holding would collect about $3,041 per BTC (bid; about 3.7% of spot) and enforce the sale at 100K, but it caps upside above 100K and requires moving BTC to Deribit/OKX.

### Gaps
- Deribit contract specs (minimum size, believed to be 0.1 BTC; option fee schedule) and whether USDC alone can margin inverse BTC options were not verified in this session.
- Coinbase's ownership of Deribit was not independently verified here.
- OKX, Binance and Bybit eligibility rules for Vietnam residents were not verified from primary sources. Their APIs were reachable or blocked only from the research proxy's location.
- Derive was down (503), and on-chain option liquidity (Aevo order-book depth, Rysk, Hypersurface on HyperEVM) was not measured. Those venues mostly let users sell rather than buy options; treat them as unverified.

## 3. Pre-market / pre-TGE instruments

### Takeaway
- **No crypto pre-launch "hyperps" were visible on Hyperliquid's main dex on 2026-10-17.** The only assets flagged strict-isolated are delisted.
- **HL's live "pre-market" exposure is HIP-3 pre-IPO equity perps** (Anthropic, OpenAI, SpaceX).
- **Pre-TGE crypto bets are live on Polymarket**, as FDV-one-day-after-launch ladders and "launch by" markets, for Variational, Extended, Predict.fun, Pacifica and others. They are thin and long-dated, with resolution risk.

### Cited Findings
**How hyperps work** — [HL docs: Hyperps](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/hyperps)
- The oracle is an 8-hour EMA of HL's own minutely mark prices, capped at 4x the initial or one-month-average mark.
- The mark is capped at 3x the 8-hour EMA (and at 1.5x the median external pre-launch perp price, if one exists).
- Funding premium samples are 1% of the standard formula. Funding can "heavily incentivize positions in the opposite direction" after one-way moves.
- A hyperp converts to a vanilla perp shortly after spot listing on Binance, OKX or Bybit.

**Live main-dex universe** — [HL info API `meta`](https://api.hyperliquid.xyz/info)
- 234 entries, 56 delisted. The 8 assets carrying `onlyIsolated`/`strictIsolated` flags (HPOS, RLB, UNIBOT, OX, FRIEND, SHIA, NFTI, PANDORA) are all delisted.

**HIP-3 builder dexes (2026-10-17)** — [HL info API `perpDexs` + `metaAndAssetCtxs` per dex](https://api.hyperliquid.xyz/info)
- `io` (EntropyIO): ANTH (6x strict isolated, OI ≈ $41.0M, 24h volume ≈ $11.9M); OAI (6x no-cross, OI ≈ $7.0M).
- `xyz` (Trade.xyz): SPCX (20x; OI ≈ $128M) plus stocks, indices and commodities.
- Felix, Ventuals, HyENA, Kinetiq "km", dreamcash and ABCDEx currently have 0 live assets.
- Decrypt describes the HIP-3 pre-IPO wave (SpaceX, Anthropic, OpenAI) — [Decrypt](https://decrypt.co/368172/hyperliquid-defies-market-downturn-as-spacex-anthropic-openai-ipos-loom)

**Polymarket FDV-one-day-after-launch ladders ("Yes" prices)** — [Polymarket gamma search "FDV"](https://gamma-api.polymarket.com/public-search?q=FDV&limit_per_type=50&events_status=active)

| Project | Volume / liquidity | Ladder |
|---|---|---|
| Variational | $3.55M / $452K | >$300M 93.1%, >$500M 86.5%, >$800M 72.5%, >$1B 58.5%, >$2B 27.75%, >$3B 13.6%, >$4B 6.85%, >$5B 3% |
| Extended | $3.97M | >$150M 66%, >$300M 38.5%, >$500M 19%, >$1B 5% |
| Predict.fun | $7.04M | >$500M 79%, >$800M 54.5% |
| Base | — | >$1B 38.5%, >$5B 28.5% |
| Pacifica | — | >$50M 21.5%, >$100M 15% |
| Ethereal | — | >$25M 50%, >$100M 20.5% |

- Other ladders: Opensea, Metamask, StandX, Ink, Reya, Ostium, Hyperbeat, Felix, Unit, Abstract, Arc and others. Most have $20K–$250K of liquidity and end dates of 2027-01-01 or 2028-01-01.

**Polymarket "launch by" markets** — [Polymarket gamma search "token launch"](https://gamma-api.polymarket.com/public-search?q=token%20launch&limit_per_type=50&events_status=active), [Polymarket gamma search "airdrop"](https://gamma-api.polymarket.com/public-search?q=airdrop&limit_per_type=50&events_status=active)
- Variational token by 31-Dec-2026: 86.55% (by 30-Nov 30%; by 31-Oct 4.75%).
- Predict.fun by 30-Nov-2026: 78.5%. Hibachi by 31-Dec-2026: 62%. Base by 31-Dec-2026: 8%.
- MegaETH airdrop by 31-Dec-2026: 11.5%. Hyperliquid airdrop by 31-Dec-2026: 7.5% (by 31-Dec-2027: 48%). Pump.fun airdrop by 31-Dec-2026: 15.5%.

### Inferences
- **Hedging Variational points with Polymarket.** A Variational points farmer can hedge part of the FDV uncertainty by buying "No" on high-FDV rungs (e.g., FDV >$2B is about 28% "Yes"), or monetize a view directly.
- **Market-implied Variational FDV (computed from the ladder above).** Mean ≈ $1.6–1.7B; median ≈ $1.2–1.3B. This roughly matches the $1.53–1.85B third-party estimate in section 4.
- **Main risks of these instruments:**
  - Thin books, so getting out costs a lot.
  - Capital locked until launch or the end date.
  - Ambiguous "one day after launch" FDV resolution (UMA oracle disputes).
  - For hyperps: no external price anchor, so they can be squeezed; funding flips sharply after one-way moves; and HL caps (3x/4x EMA) can still allow large moves.

### Gaps
- I could not confirm from HL announcements whether any current main-dex listing (e.g., MEGA) is technically a hyperp, because the API does not flag hyperps explicitly. Whales.market and other CEX pre-markets were not checked.

## 4. Points/airdrop farming as a return kicker (Variational, other perp DEXs, Pendle YT) and EV for ~$7K

### Takeaway
- **Variational fits the "zero-fee perps" brief.**
  - Its OLP vault is the sole counterparty and earns the spread.
  - Points run at 150K per week until a VAR TGE now guided for Q4 2026. 32% of supply goes to points holders, fully unlocked.
  - Market-implied value is about $45–59 per point.
- **But entry is late.** Only roughly 1–1.5M of an estimated 10–11M total points remain to be emitted.
- **The true points-per-volume rate is not public,** so EV for a $7K account cannot be computed precisely. Expect a modest kicker (likely hundreds of dollars, not thousands) that is very sensitive to volume share and FDV.
- **Other programs (Extended, Pacifica, Ethereal, edgeX, GRVT) have stale or unverified parameters.**
- **Pendle has "points"-tagged markets** (HYPE LSTs, RWA stables), but **no YT on Variational or other perp-DEX points** was found.

### Cited Findings
**Variational trading model** — [Alea Research](https://alearesearch.substack.com/p/variational)
- No maker or taker fees; the Omni Liquidity Provider (OLP) is the sole counterparty and earns the spread, and the protocol takes a cut.
- OLP hedges on external venues. OLP deposits have been team-seeded, with plans to open them to users.

**Variational points and token** — [KuCoin flash, 2026-09-24](https://www.kucoin.com/news/flash/variational-reveals-airdrop-details-var-token-valuation-estimated-at-1-53b-1-85b)
- Points started 2025-12-17 with 3M retroactive points — [AirdropAlert](https://airdropalert.com/blogs/variational-review/)
- The program was originally set to end in Q3. It now runs until TGE (Q4 2026), with 150,000 points per week.
- VAR allocation: 32% genesis airdrop pro-rata to points (fully unlocked at TGE); 18% ecosystem reserve; 50% team and investors (12-month lock, then at least 3 years of vesting). Unclaimed tokens are burned.
- Dune projects about 9.15M points by end of Q3; total estimated at 9.3–10M (TGE early Q4) or about 11M (TGE late Q4).
- Implied value: $44.5–59.2 per point at $1.53–1.85B FDV (the Polymarket median and probability-weighted mean as of 2026-09-24).
- A headline also says Variational set the VAR TGE for Q4 2026 with a 32% genesis allocation — [KuCoin](https://www.kucoin.com/news/flash/variational-sets-var-tge-for-q4-2026-with-32-genesis-allocation)

**Variational access**
- Search-surfaced reviews say Omni was in private beta and excluded US and Canada. The attribution to a specific review is uncertain, and no official Variational page was fetched — [AirdropAlert](https://airdropalert.com/blogs/variational-review/), [Airdrops.io](https://airdrops.io/variational/)
- Before TGE the team plans to end the private beta and move to public mainnet, per the announcements summarized by KuCoin — [KuCoin](https://www.kucoin.com/news/flash/variational-sets-var-tge-for-q4-2026-with-32-genesis-allocation)

**Polymarket on Variational (2026-10-17)** — [Polymarket](https://gamma-api.polymarket.com/public-search?q=FDV&limit_per_type=50&events_status=active)
- FDV ladder as in section 3: P(>$1B) 58.5%, P(>$2B) 27.75%.
- Token launch by 31-Dec-2026: 86.55%.

**Lighter (already launched) as a reference** — [bex.co, 2026-04-28](https://bex.co/blog/2026/04/28/perp-dex-cohort-2026-lighter-airdrop-hyperliquid-long-tail)
- Airdropped 250M LIT (25% of supply) on 2025-12-30, with no vesting.
- Opened above $3.30 and settled near $2.50 (about $675M headline value). Volume fell about 70% within three weeks.
- LIT now trades at $3.20, with a range of 0.78–5.59 since listing — [HL candles](https://api.hyperliquid.xyz/info)

**Other programs (stale; verify)**
- Extended: 30% of supply confirmed for airdrop; points since May 2025 — [Dropstab, Feb 2026](https://news.dropstab.com/research/top-perpetual-dex-platforms-for-point-farming)
- Pacifica: closed beta, 10M points every Thursday — same source.
- Ethereal: points from USDe/eUSDe deposits — same source.
- edgeX: token "widely expected" Q3 2026. GRVT: token "telegraphed" for early Q4 2026. Both unconfirmed — [bex.co](https://bex.co/blog/2026/04/28/perp-dex-cohort-2026-lighter-airdrop-hyperliquid-long-tail)

**Pendle active markets tagged "points" (2026-10-17)** — [Pendle API HyperEVM](https://api-v2.pendle.finance/core/v1/999/markets/active), [Pendle API Ethereum](https://api-v2.pendle.finance/core/v1/1/markets/active)
- HyperEVM: kHYPE (exp. 2027-03-25, implied APY 1.93%, liquidity $1.9M), vkHYPE (2.22%), stHYPE (exp. 2027-01-28, 2.09%), haHYPE (3.32%).
- Ethereum: apyUSD (15.83%, $18.5M), USDat/sUSDat (8.0%/14.06%), siUSD, strUSD, sUSDe (4.71%), srUSDe/jrUSDe and others.
- No Variational, Extended, Pacifica or other perp-DEX points markets appeared on chains 1, 999, 42161 or 8453.

### Inferences
- **Remaining Variational emission is small.**
  - If TGE lands about 6–10 weeks from now, about 0.9–1.5M points remain. That is roughly 8–14% of the final total, or about $40–75M of value at $45–50 per point, shared among all active farmers.
  - The trader's share is (their weighted weekly volume share) × 150K per week. Volume-weighting rules are not public.
- **Illustrative EV (assumptions, not data):**
  - Earning 10–30 points before TGE would be worth about $450–1,800 at today's implied $45–59 per point.
  - It would drop to about $200–700 if FDV prints near the $500M–$800M lower rungs.
- **Costs and risks against that:**
  - Spread paid to OLP (zero fees does not mean zero cost).
  - Funding.
  - Counterparty and beta-software risk from a single-LP venue.
  - Opportunity cost of moving margin off HL.
- **Sensible use:** farming is best treated as a side-effect of trades the trader would take anyway (e.g., run part of the directional exposure on Variational), not as a reason to churn volume. Wash-style churning at 1.8x on alts raises liquidation and spread costs.
- **Pendle YT is a different kind of bet.** YT on HYPE LSTs buys leveraged exposure to LST yield plus whatever points the issuer awards. With implied APYs near 2%, a YT costs only about 0.8–1% of notional for about 5 months. It pays only if those points programs (e.g., Kinetiq-related) are valuable, which is a different thesis from perp-DEX points.

### Gaps
- Variational's official points formula, current weekly eligible volume, OLP spread levels and whether Vietnam is an eligible jurisdiction could not be verified. No official docs were fetched; sources are secondary or affiliate-style.
- I found no October 2026 source with concrete points parameters for other perp DEXs.

## 5. Yield on idle USDC kept as reserve

### Takeaway
- **Native HyperCore USDC lending pays 3.55% APR** (78.9% utilization, borrow rate 5%).
- **HLP shows a 3.7% trailing APR, but its returns are lumpy.** It was nearly flat from mid-Feb to Sep 2026, with spikes on crash days (+$41M in Oct 2025, +$19M in Feb 2026) and occasional small drawdowns.
- **Mainstream alternatives pay about 4–8%:**
  - Aave v3 USDC: 2.3–5.7%.
  - Morpho/Felix USDC on HyperEVM: 6.6%.
  - Maple Syrup USDC: 5.2%.
  - Fluid USDC: 6.2–6.6%.
  - Pendle fixed (PT) rates are higher (e.g., PT-limUSD 9.3% to 26-Nov-26), with added issuer risk.

### Cited Findings
**HyperCore USDC lending (token 0)** — [HL info API `allBorrowLendReserveStates`](https://api.hyperliquid.xyz/info)
- Supply rate 3.549%, borrow 5.0%, utilization 78.86%, total supplied $548.0M, total borrowed $432.2M.
- HYPE as collateral: LTV 0.65. Token 197 (oracle $81,473, i.e. BTC): LTV 0.5.

**HLP vault** — [HL info API `vaultDetails`](https://api.hyperliquid.xyz/info)
- API field `apr` = 3.74%. Account value $177.8M (down from $583.8M on 2025-10-29). All-time PnL $138.7M. Last-30-day PnL +$573.5K (≈3.9% annualized, computed).
- PnL moves:
  - 2025-03-05 → 03-12: −$3.96M.
  - 2025-10-01 → 10-15: +$41.4M.
  - 2025-10-29 → 11-12: −$4.66M.
  - 2026-01-21 → 02-04: +$18.8M.
  - 2026-04-01 → 04-15: −$2.28M.
  - 2026-02-18 → 2026-10-17: +$0.49M in total, on $177–448M of account value.

**DefiLlama USDC rates (2026-10-17)** — [DefiLlama yields](https://yields.llama.fi/pools)
- Aave v3 USDC: Ethereum 5.58% (3.76% base + 1.82% Umbrella reward); Arbitrum 2.29%; Base 5.67% (3.79% + 1.88%).
- Felix USDC vault on Morpho (HyperEVM, "FEUSDCV2"): 6.57% (30-day mean 4.25%).
- Harmonix (HL L1) USDC: 6.60%. Liminal limUSD (basis): 8.07%.
- Maple Syrup USDC: 5.23% (TVL $2.78B).
- Fluid USDC: Ethereum 6.17%, Arbitrum 6.63%.
- Compound v3 USDC: 5.61%. Jupiter Lend USDC (Solana): 8.21%.

**Pendle PT fixed rates** — [Pendle API HyperEVM](https://api-v2.pendle.finance/core/v1/999/markets/active)
- PT-limUSD (2026-11-26): 9.26% implied fixed.
- Ethereum USD PTs mostly 5–20% (e.g., sUSDS 5.18%, USD3 15.08%, reUSD 12.11%) — [Pendle API Ethereum](https://api-v2.pendle.finance/core/v1/1/markets/active)

### Inferences
- **For a reserve that may be redeployed into a dip, use HyperCore lending.** At 3.55% it is the most convenient: same venue, no bridge. It pays about $230/yr on $6.4K.
- **Moving to Aave/Felix at about 5.6–6.6% adds only about $130–200/yr** on $6.4K, at the cost of bridge/smart-contract risk and slower redeployment. For a ~$7K account, convenience dominates.
- **HLP is not a cash substitute.**
  - Its return comes mostly from rare liquidation cascades.
  - It has negative-tail events (the 2025 incidents).
  - The API reports `maxWithdrawable` = 0 for a non-depositor; HL documents a lock-up for HLP deposits, which was not verified here.
  - It is a "short-volatility-ish" bet, not idle cash.
- **Note on utilization:** HyperCore USDC utilization near 79% means the supply rate rises when leverage demand rises, as in a bull leg. The reserve's yield is mildly pro-cyclical.

### Gaps
- HLP lock-up length and HyperCore lending withdrawal mechanics or limits were not re-verified this session.
- Whether lent USDC can simultaneously back perps under portfolio margin was not verified.
- HyperLend and HypurrFi rates were not captured. DefiLlama returned no qualifying USDC pools for them above a $5M TVL filter.

## 6. Position-sizing frameworks (Kelly under fat tails, risk of ruin, barbell/core-satellite, volatility targeting)

### Takeaway
- **Kelly says leverage on alts is hard to justify.** Kelly maths with realistic vols puts full-Kelly leverage at about 1–2.3x for BTC under a bullish 36% excess-return view (vol 40%), and at or below 1x for 60–90%-vol alts. Practitioners use ½ to ¼ Kelly because of fat tails and estimation error.
- **The trader's own numbers agree.** The simulations show 2x+ on HYPE/SOL/LIT carries double-digit ruin odds over 5 months unless the bull drift arrives.
- **Core-satellite fits better.** About 1x core plus a capped convex satellite (calls or small high-leverage) matches "aggressive but survivable" better than uniform 2x on alts.

### Cited Findings
- **Kelly maths (computed; `implied_probs.py`).** For a lognormal asset, f* = (μ − r)/σ².

| Excess return / vol | Full Kelly | Half Kelly |
|---|---|---|
| 36% / 40% | 2.25x | 1.12x |
| 36% / 60% | 1.0x | 0.5x |
| 36% / 90% | 0.44x | 0.22x |
| 56% / 60% | 1.56x | 0.78x |

- **Fractional Kelly in practice** — [MetricGate](https://metricgate.com/docs/kelly-criterion/), [TradingStrategy.ai](https://tradingstrategy.ai/docs/learn/risk-management.html) (practitioner sources)
  - Fat-tailed returns plus parameter uncertainty argue for fractional Kelly.
  - Practitioners typically use half or quarter Kelly. Half Kelly is described as giving about 75% of the growth rate with roughly half the drawdown.
  - Full Kelly "can lead to ruin" when estimates are wrong. Correlated crypto positions should be treated as partly one bet.
- **Current vol inputs** — [HL candles](https://api.hyperliquid.xyz/info); [Deribit options book](https://www.deribit.com/api/v2/public/get_book_summary_by_currency?currency=USDC&kind=option)
  - 30/90-day realized vol: BTC 37/38%, SOL 59/56%, HYPE 60/71%, LIT 96/107%, LINK 74/70%.
  - Implied vol: BTC about 37–38%, ETH about 50%, SOL about 55%, HYPE about 55–57% (Dec-26 ATM).
- **Risk-of-ruin evidence:** see the section 1 simulations (basket at 1.8x: 8.4% if flat, 25% at −30% drift; 2.7x: 34.9% if flat; 0.9x: 0%).

### Inferences
- **Volatility targeting.** To keep the satellite at, say, about 60% annualized vol, use leverage ≈ target/σ: BTC about 1.6x, SOL about 1.0–1.1x, HYPE about 0.85–1.0x, LIT about 0.6x. Uniform 2x on all three coins runs the account at roughly 110–200% vol.
- **Barbell / core-satellite** (for the report writer to evaluate):
  1. **Core:** ~1x net exposure in cross (BTC and/or HYPE/SOL), with extra USDC left in the account as a buffer and earning 3.55%.
  2. **Convex satellite:** 10–25% of the bankroll in long-dated calls (Mar-27 BTC; Dec-26 HYPE/SOL if Q4-focused), where the maximum loss equals the premium.
  3. **Optional kicker:** route some core trades through Variational for points.
- **Ladder entries; rely on low leverage instead of stops.** Laddered limit entries (as the trader does) are fine. Given "no stops", the protective variable is effective leverage, not entry price.
- **Correlation with the main holding.** The trader's BTC holding (~70% of net worth) is already a large long-crypto bet. The $7K account is a satellite on the same factor, and a 2x alt basket adds beta to an already concentrated book.

### Gaps
- No rigorous quantitative study of fractional Kelly under crypto fat tails was found; the sources are practitioner pages. The Kelly numbers above are textbook formulas with assumed returns, not estimates.

## 7. Vietnam taxes and regulation (only what affects venue choice)

### Takeaway
- **No crypto exchange is licensed in Vietnam yet** (as of late Aug–Oct 2026).
- **Decree 284/2026 (effective 1-Sep-2026) fines trading outside licensed providers VND 30–50M.** Sources conflict on whether the fine applies to individuals now or only after the 6-month transition that starts when the first license is issued.
- **Tax:** 0.1% per transfer, withheld by licensed providers only. Foreign venues fall outside withholding.
- **For a Q4 2026 – Q1 2027 horizon, offshore and on-chain venues remain usable in practice,** but the clock could start at any time.

### Cited Findings
**Resolution 05/2025/NQ-CP pilot**
- Licensees need VND 10 trillion (about $383M) of charter capital, at least 65% from institutions, foreign ownership at most 49%. Foreign organizations are not eligible — [crypto.news, 2026-08-30](https://crypto.news/vietnam-crypto-licenses-5-firms-clear-first-review/)
- Five applicants passed initial review, but "passing the initial assessment does not authorize any company to operate an exchange". No licensing deadline has been announced — same source.
- Vietnamnet names five applications assessed as valid in March 2026: VIX, Loc Phat, Vietnam Prosperity, Techcom and Vietnam Digital Asset. It is not confirmed that these are the same five that crypto.news says cleared first review — [Vietnamnet, 2026-07-27](https://vietnamnet.vn/en/vietnam-tightens-crypto-trading-rules-from-september-1-2539366.html)

**Decree 284/2026/ND-CP (effective 1-Sep-2026)**
- Fines of **VND 30–50M** for domestic investors trading without a Ministry of Finance-licensed provider — [VnExpress, 2026-07-18](https://vnexpress.net/giao-dich-tai-san-ma-hoa-qua-san-khong-phep-bi-phat-toi-50-trieu-dong-5098825.html); [Vietnamnet](https://vietnamnet.vn/en/vietnam-tightens-crypto-trading-rules-from-september-1-2539366.html)
- **Contradicted by** [crypto.news](https://crypto.news/vietnam-crypto-licenses-5-firms-clear-first-review/): domestic investors "will not be fined from September 1 solely for using an overseas or unlicensed platform". The penalty starts only with the licensed-platform requirement, which applies 6 months after the first provider is licensed (Resolution 05, Art. 7), and that clock has not started.

**Tax**
- Circular 32/2026/TT-BTC (effective 27-Mar-2026): 0.1% of transfer value per transaction for individuals; crypto transfers are VAT-exempt — [Viet An Law](https://vietanlaw.com/guide-to-declaring-tax-on-crypto-assets-under-resolution-05-2025-nq-cp/)
- Circular 41/2026/TT-BTC covers procedures; tax is withheld by the licensed provider — same source.
- "Transactions via foreign exchanges do not fall within the scope of tax deduction at source" — same source.
- VnExpress says crypto is taxed "like securities" pending a dedicated policy — [VnExpress](https://vnexpress.net/giao-dich-tai-san-ma-hoa-qua-san-khong-phep-bi-phat-toi-50-trieu-dong-5098825.html)

### Inferences
- **Venue choice.**
  - Through Q1 2027, the main legal risk of offshore or on-chain venues (HL, Deribit, OKX, Variational) is a first license being issued. That starts a 6-month countdown, after which unlicensed-venue trading could draw VND 30–50M fines (about $1.1–1.9K, a large share of a $7K account).
  - A license issued in Nov–Dec 2026 would put the cutoff around May–June 2027, after the planned horizon. Monitor licensing news.
- **Tax does not change venue choice.** The 0.1% transfer tax is small and applies through licensed venues, so it does not affect the choice between instruments. Self-declaration duties for offshore activity were not clarified in the sources.

### Gaps
- The official Decree 284 text (Article 9 wording on individuals and the grace period) was not fetched. Sources conflict, as noted above.
- Treatment of DeFi/on-chain venues (Hyperliquid, Variational) under the decree was not addressed in any source found.
