# Tori Finance on Pendle: YT markets, live data, and cost per Core (snapshot 2026-09-28 11:42 UTC)

Data retrieval timestamp: **2026-09-28T11:42:47Z** (Pendle API `priceUpdatedAt` 2026-09-28T11:42:30Z; `dataUpdatedAt` 11:42:00Z; hourly data point 11:00Z). All Pendle figures are pulled directly from the public Pendle API (primary source). "u" = underlying APY. "T" = days to maturity = **58.512 days** (2026-09-28 11:42:47 UTC to 2026-11-26 00:00 UTC); t = T/365 = **0.160307 yr**.

API endpoints used (all live, HTTP 200):
- All markets (803 markets on 13 chains, active and expired): [api-v2.pendle.finance/core/v1/markets/all](https://api-v2.pendle.finance/core/v1/markets/all)
- Market detail: [core/v1/1/markets/0xac02…eaddb](https://api-v2.pendle.finance/core/v1/1/markets/0xac028348c46d3455899a2b9b50077c11960eaddb), [core/v1/1/markets/0xfcf0…c947](https://api-v2.pendle.finance/core/v1/1/markets/0xfcf009cb3135da12a6eb1f73f3ee05392a7bc947)
- Market data: [core/v2/1/markets/0xac02…/data](https://api-v2.pendle.finance/core/v2/1/markets/0xac028348c46d3455899a2b9b50077c11960eaddb/data), [core/v2/1/markets/0xfcf0…/data](https://api-v2.pendle.finance/core/v2/1/markets/0xfcf009cb3135da12a6eb1f73f3ee05392a7bc947/data)
- Points: [core/v1/markets/points-market](https://api-v2.pendle.finance/core/v1/markets/points-market)
- Spot swap rates: [core/v1/sdk/1/markets/0xac02…/swapping-prices](https://api-v2.pendle.finance/core/v1/sdk/1/markets/0xac028348c46d3455899a2b9b50077c11960eaddb/swapping-prices), [core/v1/sdk/1/markets/0xfcf0…/swapping-prices](https://api-v2.pendle.finance/core/v1/sdk/1/markets/0xfcf009cb3135da12a6eb1f73f3ee05392a7bc947/swapping-prices)
- Execution quotes (price impact): `https://api-v2.pendle.finance/core/v2/sdk/1/convert?tokensIn=<trUSD>&amountsIn=<1k/10k/50k>&tokensOut=<YT>&slippage=0.01&enableAggregator=false`
- History: [core/v2/1/markets/0xac02…/historical-data?time_frame=day](https://api-v2.pendle.finance/core/v2/1/markets/0xac028348c46d3455899a2b9b50077c11960eaddb/historical-data?time_frame=day), [same for 0xfcf0…](https://api-v2.pendle.finance/core/v2/1/markets/0xfcf009cb3135da12a6eb1f73f3ee05392a7bc947/historical-data?time_frame=day); YT OHLCV: [core/v4/1/prices/0xc4bb…/ohlcv](https://api-v2.pendle.finance/core/v4/1/prices/0xc4bb3ec6588ff14d7676445a40f2716e690a3203/ohlcv?time_frame=day), [core/v4/1/prices/0x1fcd…/ohlcv](https://api-v2.pendle.finance/core/v4/1/prices/0x1fcdb1e747419bb8d1a029c4d1f83b41e8afe8ce/ohlcv?time_frame=day)

## Which Tori Pendle markets exist (active and expired), on which chains, with what maturities?

### Takeaway
Exactly **two** Tori markets exist on Pendle, both on **Ethereum mainnet (chainId 1)**, both **active**, both maturing **26 Nov 2026**: **strUSD** (staked, yield-bearing) and **trUSD** (the base synthetic dollar, no native yield). No expired Tori markets and no Tori markets on any other chain (Arbitrum, Base, BSC, Mantle, Sonic, Plasma, HyperEVM, Berachain, Optimism, Monad-143, X Layer-196, 4663) were found.

### Cited Findings
- Scanning all 803 Pendle markets returned by the all-markets endpoint (includes expired markets back to 2024; per-chain count: Ethereum 494, Arbitrum 92, HyperEVM 50, BSC 41, Base 37, Plasma 28, Sonic 17, Berachain 14, 4663: 10, 143: 9, Mantle 7, Optimism 2, 196: 2) for "tori" (case-insensitive, any field) returns only two markets, both `protocol: "Tori"`, chainId 1 — [Pendle API markets/all](https://api-v2.pendle.finance/core/v1/markets/all); Pendle's supported chain list is 1, 56, 143, 196, 999, 4663, 8453, 9745, 42161, 10, 146, 5000, 80094 — [Pendle API chains](https://api-v2.pendle.finance/core/v1/chains)
- **Market 1: strUSD** — market (LP) `0xac028348c46d3455899a2b9b50077c11960eaddb`; PT-strUSD-26NOV2026 `0x74299580811e1c3c1a2831db079ba0a8f513998f`; YT-strUSD-26NOV2026 `0xc4bb3ec6588ff14d7676445a40f2716e690a3203`; SY-strUSD `0x7e8a16e87fa6b0f2e657db47f3dbfe2e981ef211`; underlying strUSD `0x280839980a7ed0d7717f64125fe241012e5f5815`; accounting asset trUSD `0xd0580192e98ea6ceb9c7b6191ed2e27560911697` (pyUnit "trUSD staked in Tori Finance", i.e., 1 PT/YT = 1 trUSD-worth of strUSD); expiry 2026-11-26T00:00Z; market created 2026-07-19T18:15:59Z; whitelisted Pro 2026-07-27T14:45Z; categories stables/points/lp-with-no-il; fee rate 0.22098%; yield range 6%–30% — [Pendle API market detail](https://api-v2.pendle.finance/core/v1/1/markets/0xac028348c46d3455899a2b9b50077c11960eaddb)
- **Market 2: trUSD** — market `0xfcf009cb3135da12a6eb1f73f3ee05392a7bc947`; PT-trUSD-26NOV2026 `0x7191878f1fe834b28f4d0cead0e4375b814c4abb`; YT-trUSD-26NOV2026 `0x1fcdb1e747419bb8d1a029c4d1f83b41e8afe8ce`; SY-trUSD `0xa09482f2f6cb5f2177b05144bc276d06b8b818eb`; underlying/accounting asset trUSD `0xd058…1697`; expiry 2026-11-26T00:00Z; created 2026-07-19T18:16:11Z; categories stables/points; fee rate 0.16657%; yield range 5%–28% — [Pendle API markets/all](https://api-v2.pendle.finance/core/v1/markets/all), [Pendle API market detail](https://api-v2.pendle.finance/core/v1/1/markets/0xfcf009cb3135da12a6eb1f73f3ee05392a7bc947)
- Pendle's newsletter announced "@tori_finance's trUSD and strUSD now available on Pendle" and listed "Tori strUSD (Nov 2026)" and "Tori trUSD (Nov 2026)"; it also pitched Pendle LP as giving "MORE points" and "MORE yield" than holding — [Pendle Print #122, Aug 3 2026](https://pendlefi.substack.com/p/pendle-print-122)
- Term Labs offers fixed-rate borrowing for "carry looping for the @pendle_fi PT of @tori_finance strUSD" — [Pendle Print #123, Aug 17 2026](https://pendlefi.substack.com/p/pendle-print-123)
- CoinGecko (updated Aug 20 2026) reported PT-strUSD at 11.56% and PT-trUSD ~9.51% fixed, ~33x YT leverage, ~$19M combined liquidity and ~$270K daily volume at the time — [CoinGecko Learn](https://www.coingecko.com/learn/pendle-tori-trusd-strusd-institutional-yield)
- Tori tokens are on Ethereum mainnet; cross-chain via Chainlink CCIP with Ethereum as hub — [Tori docs FAQ](https://docs.tori.finance/faq/general)

### Inferences
- Because Tori has only one maturity (26 Nov 2026) and no expired series, there is no prior-series history to learn from; any points strategy on Pendle ends Nov 26 unless Pendle lists a new maturity.
- The CoinGecko "~$19M combined liquidity" in Aug vs today's $9.77M combined liquidity (or $14.44M combined TVL) suggests either shrinking pools or a different definition (TVL vs liquidity); treat the Aug figure as not directly comparable.

### Gaps
- Could not load the Pendle app UI (app.pendle.finance) to confirm the exact label it renders for the points (e.g., "30 Cores/day per trUSD"); values below come from the API that feeds the UI.
- No Pendle X/Twitter listing announcement was fetched; listing dates come from API timestamps.

## What are the current YT price, implied APY, underlying APY, liquidity, and points multiplier for each?

### Takeaway
YT-strUSD trades at **$0.017184** (implied **11.42%** vs underlying **11.18%**, so almost no points premium; Pendle "long yield ROI" **−5.25%**) with **$7.20M** liquidity; it earns **6 Cores per asset** (LP 9). YT-trUSD trades at **$0.013731** (implied **9.01%**, underlying **0%** – it is a pure points token, YT ROI −100%) with **$2.57M** liquidity; it earns **30 Cores per asset** (LP 45). Neither market has non-PENDLE incentives.

### Cited Findings
Live snapshot table (Pendle API; USD prices at 2026-09-28T11:42:30Z). Sources: [strUSD detail](https://api-v2.pendle.finance/core/v1/1/markets/0xac028348c46d3455899a2b9b50077c11960eaddb), [strUSD data](https://api-v2.pendle.finance/core/v2/1/markets/0xac028348c46d3455899a2b9b50077c11960eaddb/data), [trUSD detail](https://api-v2.pendle.finance/core/v1/1/markets/0xfcf009cb3135da12a6eb1f73f3ee05392a7bc947), [trUSD data](https://api-v2.pendle.finance/core/v2/1/markets/0xfcf009cb3135da12a6eb1f73f3ee05392a7bc947/data), [points](https://api-v2.pendle.finance/core/v1/markets/points-market), [swapping prices strUSD](https://api-v2.pendle.finance/core/v1/sdk/1/markets/0xac028348c46d3455899a2b9b50077c11960eaddb/swapping-prices), [swapping prices trUSD](https://api-v2.pendle.finance/core/v1/sdk/1/markets/0xfcf009cb3135da12a6eb1f73f3ee05392a7bc947/swapping-prices)

| Field | strUSD market (0xac02…eaddb) | trUSD market (0xfcf0…c947) |
|---|---|---|
| Chain | Ethereum (1) | Ethereum (1) |
| Maturity / days left | 2026-11-26 / 58.51 d | 2026-11-26 / 58.51 d |
| trUSD price (accounting asset) | $0.99990711 | $0.99990711 |
| Underlying price | strUSD $1.026201 (= 1.0263 trUSD) | trUSD $0.999907 |
| YT price (USD, mid) | **$0.0171841** | **$0.0137307** |
| YT price in accounting asset (trUSD) | 0.0171857 trUSD | 0.0137320 trUSD |
| YT price in underlying token | 0.016745 strUSD | 0.013732 trUSD |
| YT small-size buy rate (swapping-prices) | 58.568 YT per strUSD (→ 0.017523 trUSD/YT incl. fee); sell 0.016396 strUSD/YT | 71.44 YT per trUSD (→ 0.013997 trUSD/YT); sell 0.013469 trUSD/YT |
| PT price (USD) | $0.982723 (PT discount 1.7186%) | $0.986176 (PT discount 1.3732%) |
| PT + YT (USD) | 0.99991 = 1 trUSD (check) | 0.99991 = 1 trUSD (check) |
| Implied APY | **11.420%** (v2 data; 11.417% v1) | **9.008%** |
| Underlying APY ("yield back") | **11.180%** (all interest, 0 reward APY) | **0%** |
| Long-yield APY (ytFloatingApy) | −28.71% | −100% |
| Long-yield ROI (ytRoi) | **−5.254%** (v1) / −5.285% (list) | **−100%** |
| PT fixed ROI to maturity (ptRoi) | +1.748% | +1.392% |
| Liquidity (USD) | **$7,200,408** | **$2,572,792** |
| Total TVL (USD) | $8,880,240 | $5,559,641 |
| 24h volume (USD) | **$72,880** (+1,045% d/d) | **$35,691** |
| Pool: PT / SY / LP supply | 1,710,556 PT / 5,378,482 SY / 3,111,650 LP | 515,951 PT / 2,064,165 SY / 1,010,159 LP |
| LP price | $2.3140 | $2.5469 |
| Points (Pendle `points-market`) | **Cores, type points-per-asset: YT/"basic" = 6; LP = 9** (`perDollarLp: false`) | **Cores, points-per-asset: YT/"basic" = 30; LP = 45** (`perDollarLp: false`) |
| LP APY (aggregated / max boosted) | 11.378% / 11.551% = underlying 8.570% + PT fixed 2.666% + swap fee 0.026% + PENDLE 0.115% | 2.625% / 3.141% = PT fixed 1.782% + swap fee 0.500% + PENDLE 0.344% |
| PENDLE emissions to pool | 9.502 PENDLE/day (PENDLE $2.3952) | 10.122 PENDLE/day |
| Other incentives | None listed (`underlyingRewardApyBreakdown` and `lpRewardApyBreakdown` empty) | None listed |
| Limit orders | Whitelisted (`isWhitelistedLimitOrder: true`) | Whitelisted (`isWhitelistedLimitOrder: true`) |

- Pendle takes "a 5% fee from all yield accrued (including points) by all YT in existence"; swap fee = (fee tier/365) × days to maturity — [Pendle docs: Fees](https://docs.pendle.finance/pendle-v2/ProtocolMechanics/Mechanisms/Fees). Reconciliation: Pendle's ytRoi for strUSD is reproduced only when this 5% fee is applied: 0.95 × [(1.111804)^0.160307 − 1] / 0.0171857 − 1 = 0.95 × 0.0171350 / 0.0171857 − 1 = **−5.27%** vs API −5.25% (without the fee it would be −0.29%).
- Implied APY reconciliation: YT = 1 − (1+implied)^(−t): strUSD 1 − 1.1142^(−0.160307) = 0.0171856 trUSD (API 0.0171857); trUSD 1 − 1.09008^(−0.160307) = 0.0137319 (API 0.0137320) — [Pendle API](https://api-v2.pendle.finance/core/v2/1/markets/0xac028348c46d3455899a2b9b50077c11960eaddb/data)
- Tori's own app API shows strUSD **APY 10.21%** (source "slot"), share price **1.026297** trUSD, strUSD vault total assets **47,085,873 trUSD**, strUSD supply **45,879,371**, weekly profit **102,580 trUSD** — [Tori app API /api/apy](https://app.tori.finance/api/apy). Tori states the displayed APY is "the trailing 7 days of realized performance, annualized with daily compounding" — [Tori FAQ](https://docs.tori.finance/faq/general)
- Tori solvency endpoint: total reserves $75,322,475 vs trUSD supply 74,886,300 (collateralization 100.58%, net +$436,175) — [Tori app API /api/solvency](https://app.tori.finance/api/solvency)
- trUSD has "No native yield"; staking to strUSD earns; strUSD unstake has a 7-day cooldown — [Tori FAQ](https://docs.tori.finance/faq/general), [Tori strUSD docs](https://docs.tori.finance/products/strusd)
- Tori Cores base rate: "During Season 1's pre-deposit phase, the rate was 30 Cores per dollar per day"; pre-deposit carried a "2x boost, the highest planned for the program. The phase has ended"; "Emission rates are set per season"; referral = +10% of referees' Cores — [Tori docs: Cores](https://docs.tori.finance/resources/cores). Third-party guides read this as 30/$/day base, doubled to 60 in pre-deposit — [usethebitcoin, updated Jul 2 2026](https://usethebitcoin.com/airdrop/tori-finance/) (conflicting interpretation; Tori's wording implies 30 was the pre-deposit rate).
- Tori app DeFi hub text: "Cores multipliers are illustrative until the table publishes Jul 27", "Tori points, per dollar deployed", with rows "Hold trUSD / Hold strUSD / Pendle PT / Pendle YT / Pendle LP", plus a "YT Lock" feature: "Lock for boosted cores multipliers" and "Failed to sync yield from Pendle" claim flow — [app.tori.finance/defi](https://app.tori.finance/defi) (the numeric table is loaded client-side and could not be extracted).

### Inferences
- Pendle's "points-per-asset" values are most plausibly **Cores per day per 1 unit of underlying exposure** (1 YT = 1 trUSD-equivalent). The trUSD YT value (30) equals Tori's documented 30 Cores/$/day, so YT-trUSD likely earns the same as holding trUSD (1x), and strUSD holding likely earns ~6 Cores/$/day (1/5 of trUSD, since strUSD also earns yield). LP gets 1.5x of YT's per-asset value in both markets (45/30, 9/6). These are interpretations: the API has no time unit, and Tori does not publish post-pre-deposit rates.
- If the strUSD market's "asset" is 1 strUSD rather than 1 trUSD, Cores per YT = 6 × (1/1.0263) = 5.85/day (−2.6%); if Pendle's 5% YT fee is also applied to points (Pendle docs say "including points"), YT Cores are ×0.95.
- YT-strUSD implied (11.42%) is only 0.24 pp above Pendle's underlying (11.18%) but 1.21 pp above Tori's own 7d APY (10.21%); the market is paying little for Cores in this YT. YT-trUSD's entire 9.01% implied APY is the market price of Cores.
- The small-size buy price already embeds ~2% over mid for YT-strUSD (0.017523 vs 0.017186 trUSD) because Pendle's fee is applied as a rate add-on (11.42% → ~11.66%), which is large relative to YT's small price.

### Gaps
- Exact post-pre-deposit Cores rates for native trUSD/strUSD holding, and the Tori app's "Cores multiplier" table values (incl. YT Lock boost), were not retrievable (client-side rendered); report Pendle-API values and flag as unverified vs Tori's table.
- The 24h volume is the market figure; YT-only volume for last 24h is ~$0.25k (strUSD, partial day) and ~$25k (trUSD) per OHLCV.
- No partner points (other than Cores) or Tori-token incentives exist on either market per the API.

## What is the net cost per point (USD per Core) for YT under base and bearish assumptions (u falls, entry slippage at $1k/$10k/$50k)?

### Takeaway
At $1k size, YT-strUSD costs about **$0.0041 per 1,000 Cores** (net cost ≈ $80 per $1,000 at u = 11.18%) versus **$0.0084 per 1,000 Cores** for YT-trUSD (full $1,000 lost, but 6x the Cores). YT-strUSD's advantage disappears if strUSD's APY falls below ~**10.1%** (Tori's own 7d APY is already 10.21%); at −30%/−50% APY it costs **$0.0175 / $0.0267 per 1,000 Cores**. Slippage is severe: at $50k, YT-strUSD loses ~30% and YT-trUSD ~58% to price impact.

### Cited Findings
Execution quotes (input trUSD, `enableAggregator=false`, 1% slippage) from [Pendle SDK convert](https://api-v2.pendle.finance/core/v2/sdk/1/convert):

| Size (trUSD in) | YT-strUSD out | API priceImpact | fee (USD) | YT-trUSD out | API priceImpact | fee (USD) |
|---|---|---|---|---|---|---|
| 1,000 | 56,490.44 | −2.98% | $19.64 | 67,945.66 | −6.70% | $17.86 |
| 10,000 | 543,155.35 | −6.71% | $188.68 | 494,303.94 | −32.12% | $129.22 |
| 50,000 | 2,035,051.17 | −30.10% | $702.48 | 1,527,018.20 | −58.06% | $394.09 |

Formulas (all per $1,000 invested; trUSD price p = 0.99990711; T = 58.512 d; t = 0.160307):
- N (YT units = trUSD-units of underlying exposure) = 1000 / YT price (mid), or = YT_out × 1000 / (size × p) for executed quotes.
- Net yield-back per YT (trUSD) = 0.95 × [(1+u)^t − 1] (0.95 = Pendle 5% YT fee). At u = 11.1804%: (1.111804)^0.160307 − 1 = 0.0171350 → ×0.95 = 0.0162783.
- Yield-back ($) = N × 0.0162783 × p. Net cost = 1000 − yield-back (YT → 0 at maturity).
- Cores/day = N × rate (6 for YT-strUSD, 30 for YT-trUSD). Total Cores = Cores/day × 58.512. $ per 1,000 Cores = net cost / total × 1000. ("net" column also divides Cores by 0.95 fee on points.)

YT-strUSD (u scenarios: Pendle live 11.180%; Tori app 7d 10.21%; Pendle 30-day avg 10.510%; −30% = 7.826%; −50% = 5.590%):

| Entry | N per $1k | Cores/day | Total Cores to maturity | u=11.18%: yield-back / net cost / $ per 1k Cores | u=10.21% | u=10.51% | u −30% (7.83%) | u −50% (5.59%) |
|---|---|---|---|---|---|---|---|---|
| Mid (no fees) | 58,193 | 349,159 | 20.43M | $947.20 / $52.80 / **0.00258** | $131.76 / 0.00645 | $107.26 / 0.00525 | $328.23 / 0.01607 | $515.87 / 0.02525 |
| $1k exec | 56,496 | 338,974 | 19.83M | $919.57 / $80.43 / **0.00406** | $157.09 / 0.00792 | $133.30 / 0.00672 | $347.82 / 0.01754 | $529.99 / 0.02672 |
| $10k exec | 54,321 | 325,923 | 19.07M | $884.16 / $115.84 / **0.00607** | $189.54 / 0.00994 | $166.67 / 0.00874 | $372.93 / 0.01956 | $548.09 / 0.02874 |
| $50k exec | 40,705 | 244,229 | 14.29M | $662.54 / $337.46 / **0.02361** | $392.69 / 0.02748 | $375.55 / 0.02628 | $530.11 / 0.03710 | $661.36 / 0.04628 |

(Scenario cells after the first show net cost / $ per 1,000 Cores. With the 5% points haircut, multiply $/Core by 1/0.95 = 1.0526, e.g., $1k base 0.00427.)

YT-trUSD (u = 0; no yield-back; net cost = $1,000 in all u scenarios):

| Entry | N per $1k | Cores/day | Total Cores | $ per 1k Cores (gross / after 5% points fee) |
|---|---|---|---|---|
| Mid | 72,829 | 2,184,881 | 127.84M | **0.00782** / 0.00823 |
| $1k exec | 67,952 | 2,038,559 | 119.28M | **0.00838** / 0.00882 |
| $10k exec | 49,435 | 1,483,050 | 86.78M | **0.01152** / 0.01213 |
| $50k exec | 30,543 | 916,296 | 53.61M | **0.01865** / 0.01963 |

Break-evens (computed):
- strUSD u at which YT-strUSD net cost = 0 (yield-back repays full price): **11.83%** at mid, **12.21%** at $1k execution.
- strUSD u at which YT-strUSD $/Core equals YT-trUSD $/Core: **9.87%** (mid vs mid), **10.09%** ($1k vs $1k).
- Market-implied price of Cores at mid: YT-trUSD = 0.0137307 / (30 × 58.512) × 1000 = **$0.00782 per 1,000 Cores**; YT-strUSD = (0.0171841 − 0.0162783 × p)/(6 × 58.512) × 1000 = $0.00258 (u 11.18%), $0.00645 (u 10.21%).
- Source data for u: Pendle underlying APY 11.1804% — [Pendle API data](https://api-v2.pendle.finance/core/v2/1/markets/0xac028348c46d3455899a2b9b50077c11960eaddb/data); Tori 10.21% — [Tori app API](https://app.tori.finance/api/apy); 30-day average 10.51% from [Pendle history](https://api-v2.pendle.finance/core/v2/1/markets/0xac028348c46d3455899a2b9b50077c11960eaddb/historical-data?time_frame=day)

### Inferences
- YT-strUSD is a leveraged bet on strUSD's realized APY with Cores as a kicker: at $1k it gives ~56.5k units of exposure per $1,000 (~56x), and ~92% of the outlay comes back as yield only if strUSD sustains ~11.2% for 58 days. Using Tori's own 10.21% figure, net cost roughly doubles ($157 vs $80 per $1k).
- YT-trUSD has no yield risk (cost is known: 100% of premium) but ~2x higher $/Core at base case; it becomes the cheaper Cores source whenever strUSD APY < ~10.1% (at $1k size) — i.e., roughly today's Tori-reported APY. The two YTs are therefore priced close to parity; the choice is a view on strUSD APY.
- Sizing: YT-trUSD is only efficient up to ~$1k–$2k per trade (32% impact at $10k); YT-strUSD tolerates ~$10k (6.7% impact) but not $50k (30%). Larger buyers should split orders over time or use Pendle limit orders (both markets `isWhitelistedLimitOrder: true`).
- Cores' dollar value is unknown (no token/TGE/conversion announced), so "$ per Core" is only comparable across venues, not to a payout.

### Gaps
- Pendle's points values have no explicit time unit in the API; "per day" is assumed from Tori's "per dollar per day" wording.
- Whether Pendle's 5% YT fee actually reduces Cores credited by Tori (depends on Tori's off-chain accounting of Pendle positions) is unknown; both gross and net are shown.
- Quotes are one-shot at 11:4x UTC; price impact varies with pool state.

## How does YT compare to holding the staked token directly or LPing on Pendle, in terms of cost per point?

### Takeaway
Per dollar of capital, YT dwarfs every alternative in Cores (YT-trUSD ≈ 2.04M Cores/day per $1k vs 30k for holding trUSD), but in cost per Core the options are close: YT-strUSD ~$0.0041, **trUSD LP ~$0.0049–0.0061**, YT-trUSD ~$0.0084, holding trUSD ~$0.0098, per 1,000 Cores (opportunity cost vs strUSD yield). strUSD LP and holding strUSD earn Cores at zero/negative cost (they pay ~11% APY) but only ~6–9k Cores/day per $1k.

### Cited Findings
Per $1,000 over the 58.512 days to Pendle maturity (strUSD growth over T at u = 11.1804% = 1.71350%; opportunity cost measured vs holding strUSD; Cores rates as per Pendle API and assumed equal for native holding):

| Strategy | Cores/day per $1k | Total Cores (58.5 d) | Yield earned (58.5 d) | Opportunity cost vs strUSD | $ per 1,000 Cores |
|---|---|---|---|---|---|
| Hold strUSD (assumed 6/$/day) | 6,000 | 351,072 | +$17.14 | 0 | ~0 (paid to hold) |
| Hold trUSD (assumed 30/$/day) | 30,000 | 1,755,359 | $0 | $17.14 | **0.00976** |
| Switch strUSD → trUSD (marginal +24/$/day) | +24,000 | +1,404,287 | −$17.14 | $17.14 | 0.01220 (marginal) |
| strUSD LP (9/asset; SY share 76.65%) | 6,899 (A) / 9,000 (B) | 403,666 (A) / 526,608 (B) | +$17.42 (LP APY 11.378%) | −$0.29 (LP out-earns) | ~0 (negative) |
| trUSD LP (45/asset; SY share 80.22%) | 36,101 (A) / 45,000 (B) | 2,112,305 (A) / 2,633,038 (B) | +$4.16 (LP APY 2.625%) | $12.97 | **0.00614 (A) / 0.00493 (B)** |
| YT-strUSD, $1k, u 11.18% | 338,974 | 19.83M | yield-back $919.57 | net cost $80.43 | **0.00406** |
| YT-strUSD, $1k, u 10.21% | 338,974 | 19.83M | $842.91 | $157.09 | 0.00792 |
| YT-trUSD, $1k | 2,038,559 | 119.28M | 0 | $1,000 | **0.00838** |

(A) = Pendle convention that LP earns points only on the SY share of the pool (SY share = totalSy × SY price / liquidity: strUSD 5,378,482 × 1.026201 / 7,200,408 = 76.65%; trUSD 2,064,165 × 0.999907 / 2,572,792 = 80.22%). (B) = LP value read as Cores per $1 of LP. Sources: [Pendle API data strUSD](https://api-v2.pendle.finance/core/v2/1/markets/0xac028348c46d3455899a2b9b50077c11960eaddb/data), [Pendle API data trUSD](https://api-v2.pendle.finance/core/v2/1/markets/0xfcf009cb3135da12a6eb1f73f3ee05392a7bc947/data), [Pendle points](https://api-v2.pendle.finance/core/v1/markets/points-market).

- Pendle's own pitch to Tori holders: LP gives "MORE points" and "MORE yield" — [Pendle Print #122](https://pendlefi.substack.com/p/pendle-print-122)
- Tori: points accrue by holding trUSD, staking strUSD, and "participating in integrated DeFi protocols"; Cores "are not a promise of any token or payment" — [Tori docs: Cores](https://docs.tori.finance/resources/cores)
- No token, TGE date, or Cores conversion rate has been announced — [usethebitcoin](https://usethebitcoin.com/airdrop/tori-finance/); [Tori FAQ](https://docs.tori.finance/faq/general) ("That has not been announced yet")
- strUSD LP category "lp-with-no-il" per Pendle; LP APY breakdown as in the table above — [Pendle API markets/all](https://api-v2.pendle.finance/core/v1/markets/all)

### Inferences
- For a points farmer who values capital efficiency (small capital, maximum Cores), YT-trUSD is the highest Cores-per-dollar instrument (~6x YT-strUSD, ~68x holding trUSD) with a fixed, known cost; YT-strUSD is cheaper per Core only while strUSD APY stays ≥ ~10.1%.
- For a capital-rich, risk-averse farmer, trUSD LP looks like the cheapest *low-risk* Cores source (~$0.005–0.006 per 1k Cores, principal retained, 1.2–1.5x holding-trUSD Cores plus 2.6% APY), and strUSD LP is "free" Cores (yield ≈ strUSD) at a low rate.
- Holding trUSD outright is dominated by trUSD LP (more Cores and more yield), assuming the Pendle-listed LP values are credited by Tori.
- All comparisons ignore: Pendle LP exit price risk before maturity, smart-contract risk (Tori + Pendle), trUSD peg risk, 7-day strUSD cooldown, gas, and referral +10%.

### Gaps
- Native post-pre-deposit Cores rates for "Hold trUSD" and "Hold strUSD" are not published in Tori docs; the comparison assumes they equal Pendle's YT/basic values (30 and 6). If native rates differ, the "hold" rows scale proportionally.
- Tori's "YT Lock" boosted multiplier (in-app) could materially lower YT $/Core; its multiplier and lock terms could not be retrieved.

## Historical implied APY trend (is YT getting more expensive as TGE approaches?)

### Takeaway
No. Both YTs have become **cheaper**, not more expensive: YT-strUSD implied APY peaked at 12.89% (Aug 3) and is 11.42% now, with the premium over underlying collapsing from +1.8 pp to +0.24 pp; YT-trUSD (pure points) implied peaked at 14.04% (Jul 28 daily point; 13.18% on Aug 3), bottomed at 8.04% (Aug 13), and has ranged ~8.6–10.0% since, 9.01% now. No TGE date exists to anchor a "TGE approach" effect.

### Cited Findings
Daily history (00:00 UTC points; YT close in USD from OHLCV) — [Pendle history strUSD](https://api-v2.pendle.finance/core/v2/1/markets/0xac028348c46d3455899a2b9b50077c11960eaddb/historical-data?time_frame=day), [Pendle history trUSD](https://api-v2.pendle.finance/core/v2/1/markets/0xfcf009cb3135da12a6eb1f73f3ee05392a7bc947/historical-data?time_frame=day), [YT-strUSD OHLCV](https://api-v2.pendle.finance/core/v4/1/prices/0xc4bb3ec6588ff14d7676445a40f2716e690a3203/ohlcv?time_frame=day), [YT-trUSD OHLCV](https://api-v2.pendle.finance/core/v4/1/prices/0x1fcdb1e747419bb8d1a029c4d1f83b41e8afe8ce/ohlcv?time_frame=day)

| Date | strUSD implied | strUSD underlying | spread (pp) | YT-strUSD close | strUSD pool liquidity | trUSD implied | YT-trUSD close | trUSD pool liquidity |
|---|---|---|---|---|---|---|---|---|
| 2026-07-20 | 12.00% | 13.71% | −1.71 | $0.0390 | $1,991 (seed) | 8.70% | $0.0290 | $1,989 (seed) |
| 2026-07-27 | 11.83% | 13.06% | −1.23 | $0.0364 | $3.08M | 11.68% | $0.0360 | $1.02M |
| 2026-08-03 | 12.89% | 11.11% | +1.78 | $0.0372 | $5.49M | 13.18% | $0.0379 | $2.15M |
| 2026-08-10 | 11.50% | 11.17% | +0.33 | $0.0314 | $7.11M | 8.77% | $0.0243 | $2.77M |
| 2026-08-17 | 11.67% | 10.88% | +0.79 | $0.0298 | $7.05M | 9.34% | $0.0242 | $2.74M |
| 2026-08-24 | 11.80% | 10.94% | +0.86 | $0.0280 | $7.07M | 8.62% | $0.0208 | $2.66M |
| 2026-08-31 | 11.59% | 10.64% | +0.95 | $0.0255 | $7.08M | 9.39% | $0.0209 | $2.63M |
| 2026-09-07 | 11.70% | 10.49% | +1.21 | $0.0237 | $7.17M | 10.03% | $0.0205 | $2.62M |
| 2026-09-14 | 11.70% | 10.30% | +1.40 | $0.0216 | $7.20M | 9.82% | $0.0183 | $2.62M |
| 2026-09-21 | 11.46% | 10.47% | +0.99 | $0.0191 | $7.20M | 9.94% | $0.0167 | $2.57M |
| 2026-09-25 | 11.19% | 10.56% | +0.63 | $0.0176 | $7.19M | 8.70% | $0.0138 | $2.57M |
| 2026-09-28 | 11.42% | 11.18% | +0.24 | $0.0172 | $7.20M | 9.01% | $0.0137 | $2.57M |

- Range since Jul 21 (excluding seed day): strUSD implied 11.19% (Sep 23) – 12.89% (Aug 3); trUSD implied 8.04% (Aug 13) – 14.04% (Jul 28). 30-day averages: strUSD implied 11.60%, underlying 10.51%; trUSD implied 9.64% — computed from [Pendle history](https://api-v2.pendle.finance/core/v2/1/markets/0xac028348c46d3455899a2b9b50077c11960eaddb/historical-data?time_frame=day)
- strUSD underlying APY (Pendle) drifted from 13.7% at launch to 10.3–10.6% in mid/late Sept, recovering to 11.18% on Sep 28 (+2.04% relative d/d) — [Pendle API](https://api-v2.pendle.finance/core/v1/1/markets/0xac028348c46d3455899a2b9b50077c11960eaddb)
- YT trading volume since launch (sum of daily OHLCV volume): YT-strUSD ≈ $1.91M total, $1.09M last 30 days, $534k last 7 days (incl. $395k on Sep 22); YT-trUSD ≈ $1.99M total, $601k last 30 days, $114k last 7 days (incl. a drop to $0.0132 low on Sep 24 when implied fell ~1.3 pp) — [YT OHLCV](https://api-v2.pendle.finance/core/v4/1/prices/0xc4bb3ec6588ff14d7676445a40f2716e690a3203/ohlcv?time_frame=day)
- CoinGecko snapshot (Aug 20): PT-strUSD 11.56%, PT-trUSD ~9.51% — consistent with the API series — [CoinGecko](https://www.coingecko.com/learn/pendle-tori-trusd-strusd-institutional-yield)

### Inferences
- The YT price decline (strUSD $0.039 → $0.0172; trUSD $0.029 → $0.0137) is mostly time decay (fewer days of yield/points left), not a change in the market's valuation; implied APY is flat-to-down since the Aug 3 peak.
- The market-implied value of Cores (from YT-trUSD) has fallen from ~13–14% implied in late July/early August to ~9% now, i.e., the market is pricing Cores ~30% cheaper per unit of time than at peak — no evidence of TGE anticipation bidding up YT.
- The shrinking strUSD implied-minus-underlying spread (+1.8 pp → +0.24 pp) means YT-strUSD buyers currently pay almost nothing for Cores if strUSD APY holds at 11.18%, which is why its base-case $/Core is lowest; the flip side is exposure to APY drops (Tori's 7d figure 10.21% is already below Pendle's).

### Gaps
- No announced Tori TGE, token, Season 1 end date, or Cores-to-token conversion — so "as TGE approaches" cannot be tested; any new TGE/season news could reprice YT-trUSD abruptly.
- Hourly/intraday implied-APY history was not pulled; daily granularity only.
