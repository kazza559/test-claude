# SOL and HYPE: market context, fundamentals, and spot-DCA mechanics on Hyperliquid (as of 30 September 2026)

Source legend: all API figures were pulled live on 2026-09-30 (Hyperliquid info API 10:17–10:20 UTC; CoinGecko last_updated 10:19:50 UTC; DefiLlama series end 2026-09-29; Solana mainnet RPC epoch 1046; Jito API 09:03 UTC). "[S]" marks a claim taken from a search-result summary whose page was not opened in full. Treat it with more caution than claims from pages that were fetched and read. Figures dated earlier than September 2026 are flagged with their date.

## 1. Price context: current prices, ranges, ATH drawdowns, realized volatility, max drawdowns, correlations, and distance of the HYPE $80/$70/$60 rungs (with SOL equivalents)

### Takeaway
HYPE trades at about $86.4, 11.7% below its 23 Sep 2026 all-time high (~$97.9), after roughly quadrupling from its 21 Jan 2026 low of $20.5. SOL trades at about $119.3, about 60% below its Jan 2025 ATH (~$293–295), after doubling from its 6 Jun 2026 low of about $60. HYPE's realized volatility (69–73% annualized over 30/90 days) is higher than SOL's (55–62%). Their daily returns are highly correlated (ρ≈0.72–0.75 over 30–90 days; 0.57 over 365 days), and both are high-beta to BTC. The HYPE rungs at $80/$70/$60 sit −7.4%/−19.0%/−30.6% below spot. SOL rungs with the same percentage drop are ≈$110/$97/$83; volatility-scaled equivalents are ≈$112/$102/$90.

### Cited Findings

#### Method and data provenance
- Prices and candles come from the Hyperliquid info API (`candleSnapshot`, interval 1d, UTC-midnight candles; `allMids`; `l2Book`), pulled 2026-09-30 10:17–10:20 UTC — [Hyperliquid info API](https://api.hyperliquid.xyz/info); [API docs](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint).
  - HYPE uses the HYPE/USDC spot pair `@107`, with candles from 2024-11-29 (the first candle's $2.0 open is a genesis artefact; CoinGecko lists the ATL as $3.81 on 2024-11-29 — [CoinGecko API](https://api.coingecko.com/api/v3/coins/hyperliquid)).
  - SOL uses the Hyperliquid SOL perpetual, with candles from 2022-12-01, because the spot USOL pair only exists from 2025-05-10. Over the last 90 days the USOL spot vs SOL perp daily-close basis averaged −2.1 bps (range −20.6 to +10.6 bps), and the daily-return correlation was 1.000, so the perp is a faithful proxy — [Hyperliquid info API](https://api.hyperliquid.xyz/info).
  - BTC and ETH use the Hyperliquid perps.
- Calculations performed:
  - Realized volatility: population standard deviation of daily close-to-close log returns over the last N completed days (today's partial candle excluded), annualized ×√365.
  - Ranges: min intraday low and max intraday high of daily candles over trailing windows.
  - Max drawdown: peak-to-trough on daily closes.
  - Correlation: Pearson on daily log returns over matched dates.
  - Beta: cov/var(second asset).
  - Touch probability model: driftless log-price Brownian motion, P(touch L within T) = 2·N(ln(L/S)/(σ√T)), using 90-day realized volatility.
  - Empirical touch frequency: share of all historical start days on which the lowest intraday low over the next N days was at or below (start close × (1 − x%)).

  All computed by me from the API data above — [Hyperliquid info API](https://api.hyperliquid.xyz/info).

#### Current prices (snapshot 2026-09-30 ~10:17–10:20 UTC)
- HYPE/USDC spot mid ≈ $86.42–86.51. The perp mark was $86.38 and the daily candle close used for statistics was $86.438 — [Hyperliquid info API](https://api.hyperliquid.xyz/info).
- SOL perp ≈ $119.29–119.41, and USOL/USDC spot ≈ $119.25–119.39 — [Hyperliquid info API](https://api.hyperliquid.xyz/info).
- BTC ≈ $83,657–83,685 and ETH ≈ $2,690 — [Hyperliquid info API](https://api.hyperliquid.xyz/info).
- CoinGecko (10:19 UTC):
  - HYPE: $86.47, market-cap rank 11, market cap $19.23B, FDV $82.59B, 24h volume $0.65B. Changes: 7d −9.6%, 30d +6.4%, 60d +66.1%, 1y +96.6%.
  - SOL: $119.36, rank 7, market cap $70.19B, FDV $75.8B, 24h volume $3.57B. Changes: 30d +15.8%, 60d +63.9%, 1y −42.0%.

  Sources: [CoinGecko HYPE](https://api.coingecko.com/api/v3/coins/hyperliquid); [CoinGecko SOL](https://api.coingecko.com/api/v3/coins/solana).

#### Ranges and ATH (computed from Hyperliquid daily candles)

| Metric | HYPE (spot @107) | SOL (HL perp) | BTC (HL perp) |
|---|---|---|---|
| Current (daily close in progress) | $86.44 | $119.29 | $83,685 |
| 30-day low / high | $74.48 (09-17) / $97.89 (09-23) | $95.75 (09-15) / $124.95 (09-27) | $74,903 (09-15) / $87,471 (09-21) |
| 30-day change | +2.7% | +15.8% | +6.5% |
| 90-day low / high | $51.11 (08-02) / $97.89 (09-23) | $70.55 (08-01) / $124.95 (09-27) | $61,264 (07-03) / $87,471 (09-21) |
| 90-day change | +29.2% | +47.7% | +35.9% |
| 365-day low / high | $20.50 (2026-01-21) / $97.89 (2026-09-23) | $60.06 (2026-06-06) / $237.80 (2025-10-06) | $57,768 (2026-07-01) / $126,297 (2025-10-06) |
| 365-day change | +91.2% | −42.8% | −26.6% |
| ATH (intraday) | $97.885 on 2026-09-23 | $295.43 on 2025-01-19 | $126,297 on 2025-10-06 |
| Drawdown from ATH | −11.7% | −59.6% | −33.7% |
| Low since ATH | $84.87 (2026-09-29), −13.3% | $60.06 (2026-06-06), −79.7% | $57,768 (2026-07-01), −54.3% |

Source: [Hyperliquid info API](https://api.hyperliquid.xyz/info). CoinGecko's aggregated ATHs are close: HYPE $97.96 (2026-09-23, −11.7%) and SOL $293.31 (2025-01-19, −59.3%) — [CoinGecko HYPE](https://api.coingecko.com/api/v3/coins/hyperliquid); [CoinGecko SOL](https://api.coingecko.com/api/v3/coins/solana). ETH is −45.8% from its $4,960 ATH (2025-08-24) — [Hyperliquid info API](https://api.hyperliquid.xyz/info).

- Month-end closes from the HL candles, showing the path:

  | Month-end | HYPE | SOL | BTC |
  |---|---|---|---|
  | Dec 2025 | 25.43 | 124.61 | 87,632 |
  | Jan 2026 | 30.98 | 105.44 | 78,728 |
  | Feb 2026 | 31.23 | 84.30 | 66,931 |
  | Mar 2026 | 36.59 | 83.16 | 68,244 |
  | Apr 2026 | 39.72 | 83.04 | 76,300 |
  | May 2026 | 72.05 | 82.42 | 73,658 |
  | Jun 2026 | 64.98 | 73.64 | 58,603 |
  | Jul 2026 | 52.50 | 72.83 | 62,856 |
  | Aug 2026 | 84.16 | 102.99 | 78,574 |
  | Sep 30, 2026 (partial) | 86.44 | 119.29 | 83,685 |

  HYPE's +81% month in May 2026 coincided with the first US spot HYPE ETF launches (see section 2) — [Hyperliquid info API](https://api.hyperliquid.xyz/info).
- HYPE/SOL price ratio: 0.72 now, versus 0.22 one year ago (2025-09-30). It peaked at 1.04 on 2026-06-03, when HYPE briefly traded above SOL — [Hyperliquid info API](https://api.hyperliquid.xyz/info).

#### Realized volatility (annualized, close-to-close)

| Window | HYPE | SOL | BTC | ETH |
|---|---|---|---|---|
| 30d | 68.7% | 62.5% | 40.8% | 43.6% |
| 90d | 72.9% | 55.2% | 38.2% | 53.0% |
| 365d | 93.1% | 68.2% | 45.0% | 63.8% |
| Full sample | 108.6% (since 2024-11) | 84.1% (since 2022-12) | 46.0% | 62.5% |

Source: [Hyperliquid info API](https://api.hyperliquid.xyz/info).
- An implied 1-sigma 30-day move from 30-day volatility is ≈ ±19.8% for HYPE and ≈ ±18.0% for SOL (σ/√12) — computed from the [Hyperliquid info API](https://api.hyperliquid.xyz/info) data.

#### Historical max drawdowns (daily closes, episodes of 30% or more)
- HYPE:
  - −68.0%: $32.03 (2024-12-21) → $10.25 (2025-04-06)
  - −64.2%: $58.60 (2025-09-18) → $20.97 (2026-01-20)
  - −30.0%: $74.51 (2026-06-03) → $52.14 (2026-08-01)

  Source: [Hyperliquid info API](https://api.hyperliquid.xyz/info).
- SOL:
  - −76.3%: $262.20 (2025-01-18) → $62.16 (2026-06-06). SOL has not regained that peak.
  - Earlier episodes: −38.4% (Mar → Sep 2024), −30.9% (Dec 2023 → Jan 2024), −44.9% (Feb → Jun 2023), −35.4% (Jul → Sep 2023).

  Source: [Hyperliquid info API](https://api.hyperliquid.xyz/info).
- BTC: −53.0% on closes, $124,711 (2025-10-06) → $58,603 (2026-06-30) — [Hyperliquid info API](https://api.hyperliquid.xyz/info).

#### Correlations of daily log returns (ρ; β of first asset vs second)

| Pair | 30d | 90d | 365d | Full sample |
|---|---|---|---|---|
| SOL–HYPE | 0.748 (β 0.68) | 0.716 (β 0.54) | 0.574 (β 0.42) | 0.532 (since 2024-11-30) |
| SOL–BTC | 0.857 (β 1.31) | 0.835 (β 1.21) | 0.869 (β 1.32) | 0.735 (β 1.34, since 2022-12) |
| HYPE–BTC | 0.679 (β 1.14) | 0.666 (β 1.27) | 0.514 (β 1.06) | 0.509 (β 1.27) |
| SOL–ETH | 0.893 | 0.815 | 0.887 | — |
| HYPE–ETH | 0.735 | 0.729 | 0.558 | — |

Source: [Hyperliquid info API](https://api.hyperliquid.xyz/info).

#### Ladder-level distances and fill likelihood

HYPE spot reference $86.438.

| HYPE rung | vs spot | SOL same-% level | SOL vol-scaled level (90d σ ratio 0.552/0.729) | Model touch probability, HYPE, 30/90/180d | Empirical HYPE touch frequency, 30/90d | Last date HYPE traded at or below | Days in last 365 HYPE closed at or below |
|---|---|---|---|---|---|---|---|
| $80 | −7.4% | $110.41 | $112.50 | 71% / 83% / 88% | 73% / 81% | 2026-09-17 | 334 |
| $70 | −19.0% | $96.60 | $101.68 | 31% / 56% / 68% | 39% / 56% | 2026-08-20 | 313 |
| $60 | −30.6% | $82.80 | $90.48 | 8% / 31% / 48% | 16% / 36% | 2026-08-19 | 273 |

Source: computed from the [Hyperliquid info API](https://api.hyperliquid.xyz/info).
- For the same percentage dips, SOL's empirical touch frequencies (history since Dec 2022) are similar to HYPE's:
  - −7.4%: 70% within 30 days / 84% within 90 days
  - −19.0%: 38% / 64%
  - −30.6%: 19% / 42%

  Source: [Hyperliquid info API](https://api.hyperliquid.xyz/info).
- Candidate round-number SOL rungs (model touch probability 30/90/180d; empirical 30/90d; last date touched; days closed at or below in the last 365):

  | SOL rung | vs spot | Model 30/90/180d | Empirical 30/90d | Last touched | Days closed at or below (365d) |
  |---|---|---|---|---|---|
  | $110 | −7.8% | 61/77/83% | 69/84% | 2026-09-20 | 230 |
  | $105 | −12.0% | 42/64/74% | 57/77% | 2026-09-18 | 226 |
  | $100 | −16.2% | 26/52/65% | 45/69% | 2026-09-17 | 209 |
  | $95 | −20.4% | 15/41/56% | 35/62% | 2026-08-26 | 197 |
  | $90 | −24.6% | 7/30/47% | 27/55% | 2026-08-22 | 182 |
  | $85 | −28.7% | 3/22/38% | 21/46% | 2026-08-20 | 132 |

  Source: [Hyperliquid info API](https://api.hyperliquid.xyz/info).
- Both assets set their 30-day lows on 15–17 Sep 2026, around the September FOMC rate hike (see section 5) — [Hyperliquid info API](https://api.hyperliquid.xyz/info); [CoinDesk, 18 Sep 2026 [S]](https://www.coindesk.com/markets/2026/09/18/bitcoin-weathers-september-storm-as-rate-hikes-and-clarity-act-setback-test-bulls).
- Perp positioning at the snapshot:
  - HYPE perp: open interest $1.77B (20.46M HYPE), 24h volume $417M, funding −0.00048%/hr (slightly negative, i.e. shorts paying longs).
  - SOL perp: open interest $679M, 24h volume $216M, funding +0.00125%/hr (the baseline rate).

  Source: [Hyperliquid info API](https://api.hyperliquid.xyz/info) (`metaAndAssetCtxs`).

### Inferences
- The $80 rung is well within one month's 1-sigma move (−7.4% against ≈±20%), so under both the model and history it is more likely than not to fill within 30 days. The $70 rung is about a 1-sigma monthly move: roughly a coin-flip within a quarter. The $60 rung is about 1.5 sigma: roughly a one-in-three chance within 90 days, and below 50% even over 180 days on the driftless model. A ladder at $80/$70/$60 will therefore probably deploy the first tranche and possibly the second. It carries meaningful risk that the third tranche sits in cash for months, or never fills if the rally resumes.
- The HYPE rungs are not "deep value" relative to the past year: HYPE closed at or below $60 on 273 of the last 365 days, and traded at $60–70 as recently as 19–20 Aug 2026. However, the fundamental and flow backdrop has changed since then (ETFs, AQA v2, treasury buying; see section 2). A retest of $60 would mean giving back the whole late-August breakout.
- Equivalent SOL rungs:
  - Same percentage dips: about $110 / $97 / $83.
  - Volatility-adjusted: about $112 / $102 / $90, which matches the probability profile of the HYPE ladder better because SOL is less volatile.
  - A round-number $110 / $100 / $90 ladder is close to the vol-scaled version.
- The SOL–HYPE correlation of about 0.72–0.75 over the last three months means splitting $4,000 across both diversifies little in a sell-off. Both would likely hit their lower rungs together in a BTC-led drawdown (SOL β≈1.2–1.3 and HYPE β≈1.1–1.3 to BTC). Over 365 days the correlation is lower (0.57), so the assets have decoupled at times; HYPE's idiosyncratic drivers are ETFs, unlocks and buybacks.
- Starting points differ. HYPE is near its ATH after a ~4x rally, so trend and momentum are stronger but so is mean-reversion risk. SOL is about 60% below its ATH and has recovered roughly 2x from the June low, so drawdown risk from here is arguably lower in percentage terms but its trend has been weaker for longer.

### Gaps
- Only daily-candle statistics were computed. Intraday wick behaviour (which matters for resting limit fills) is only captured through daily lows.
- Correlations and touch probabilities are backward-looking. HYPE's sample is short (~22 months) and covers one full bear/bull cycle at most.
- The touch model ignores drift, fat tails and volatility clustering. It is a rough guide only.

## 2. HYPE fundamentals: supply and unlocks, Assistance Fund buybacks, volume/revenue/OI and market share, HIP-3 and catalysts, ETFs and treasuries, staking APR and LSTs

### Takeaway
HYPE has about 222M (CoinGecko) or about 299M (protocol) tokens circulating out of about 955–999M total. Core contributors receive a scheduled 9.92M HYPE (~$860M) on the 6th of each month through about late 2027, though only small fractions have actually been claimed. Buybacks (AF revenue of about $48M/month in Q3 2026) absorb only about 6% of the scheduled unlock at today's price. Hyperliquid's fee revenue in 2026 is running about 40–45% below its Q3 2025 peak, partly because HIP-3/RWA perps (now about half of volume) pay ≥90% lower fees. Meanwhile HYPE demand has come from US spot ETFs (~$502M AUM), treasury companies (~31.4M HYPE) and the AQA v2 reserve-yield buybacks, whose first payment is due 3 Oct 2026. Native staking yields about 2.2%.

### Cited Findings

#### Supply
- The protocol `tokenDetails` for HYPE on 2026-09-30 shows:
  - maxSupply 1,000,000,000
  - totalSupply 998,897,234
  - circulatingSupply 298,672,361
  - futureEmissions 411,144,779
  - Non-circulating balances: address `0x43e9abea1910387c4292bca4b94de81462f8a251` with 241,495,237 HYPE; the Assistance Fund address `0xfefe…fefe` with 47,583,180 HYPE; the zero address with 1,674; `0x…dead` with 2.7.

  Source: [Hyperliquid info API](https://api.hyperliquid.xyz/info).
- CoinGecko shows circulating 222,445,714, total 955,307,079 and max 1B, giving a market cap of $19.23B and FDV of $82.59B — [CoinGecko API](https://api.coingecko.com/api/v3/coins/hyperliquid).
- The protocol circulating figure (298,676,567) and CoinGecko's (222,445,714) differ because of how foundation and team addresses are treated (as of 27 Aug 2026) — [CryptoTicker, 27 Aug 2026](https://cryptoticker.io/en/hyperliquid-hype-unlock-dilution/). CoinDesk also used "222 million" circulating in Aug 2026 — [CoinDesk, 9 Aug 2026](https://www.coindesk.com/business/2026/08/09/hyperliquid-s-rwa-perps-boom-is-eating-into-the-revenue-that-backs-hype).

#### Core-contributor unlocks
- The core-contributor allocation is about 238M HYPE, vesting linearly at about 9.92M per month over 24 months — [CryptoTicker, 27 Aug 2026](https://cryptoticker.io/en/hyperliquid-hype-unlock-dilution/). CF Benchmarks describes the vesting as running "through 2027" — [CF Benchmarks, 10 Jun 2026](https://www.cfbenchmarks.com/blog/pricing-the-perp-dex-leader-a-valuation-framework-for-hyperliquid).
- The next unlock is 6 Oct 2026: 9,916,666 HYPE (~$829.6M) to core contributors — [KuCoin News (Tokenomist data) [S]](https://www.kucoin.com/news/flash/hyperliquid-faces-860m-hype-token-unlock-on-october-6); [Tokenomist](https://tokenomist.ai/hyperliquid/unlock-events).
- The 6 Sep 2026 unlock was about 9.92M HYPE (~$820M at $82.60; 0.99% of max supply) — [crypto.news, 7 Sep 2026](https://crypto.news/hyperliquid-hype-token-unlock-820m-misleading/). The 6 Aug unlock was about 10M HYPE (~$550M) — [CoinDesk, 9 Aug 2026](https://www.coindesk.com/business/2026/08/09/hyperliquid-s-rwa-perps-boom-is-eating-into-the-revenue-that-backs-hype).
- Actual claims have been small:
  - March 2026: only 173,217 HYPE of the 9.92M scheduled were claimed (1.75%) — [CryptoTicker, 27 Aug 2026](https://cryptoticker.io/en/hyperliquid-hype-unlock-dilution/). crypto.news frames the same figure as "about 1.75% of unlocked tokens moved to exchange deposit addresses within the first month" — [crypto.news](https://crypto.news/hyperliquid-hype-token-unlock-820m-misleading/).
  - September 2026: the actual release was about 0.19% of released supply (≈$36.56M) against a 2.32% scheduled allocation — [KuCoin News [S]](https://www.kucoin.com/news/flash/hyperliquid-faces-860m-hype-token-unlock-on-october-6).
- Conflicting reports:
  - crypto.news also reports a "29 Aug 2026 unlock" of 14.18M HYPE (~$1.2B), and a RootData/ChainCatcher item cites a "29 Sep" 9.92M unlock. Both conflict with the 6th-of-month cadence used by Tokenomist and CoinDesk — [crypto.news](https://crypto.news/hyperliquid-hype-token-unlock-820m-misleading/); [ChainCatcher [S]](https://www.chaincatcher.com/en/article/2291428).
  - Unlock value comparison (my calculation): the scheduled monthly unlock of 9.9167M HYPE is worth about $857M at $86.47. The Q3 2026 average monthly revenue of $48.2M buys about 0.56M HYPE, or about 5.6% of the scheduled unlock — computed from [DefiLlama revenue](https://api.llama.fi/summary/fees/hyperliquid?dataType=dailyRevenue) and [CoinGecko](https://api.coingecko.com/api/v3/coins/hyperliquid).

#### Assistance Fund (AF) and buybacks
- The AF (`0xfefe…fe`) automatically converts fees to HYPE, which is then burned. "Fees are entirely directed to the community (HLP, the assistance fund, and deployers)" — [Hyperliquid docs: Fees](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees).
- The AF held 47,583,180 HYPE on 2026-09-30 — [Hyperliquid info API](https://api.hyperliquid.xyz/info). Hyperliquid News (X) says the AF surpassed 47.5M HYPE bought for about $1.32B — [X/HyperliquidNews [S]](https://x.com/HyperliquidNews/status/2103796259853095393). By May 2026 more than $1.3B had been deployed — [AMINA Research [S]](https://aminagroup.com/research/hyperliquid-hype-etf-buyback-staking-yield-institutional-access-2026/).
- The December 2025 proposal to treat AF HYPE as burned (~13% of circulating supply at the time; more than 37M HYPE then) — [The Defiant [S]](https://thedefiant.io/news/tokens/hyperliquid-proposes-burning-13-percent-of-circulating-token-supply).
- AF buyback run-rate: about $290M in Q3 2025 versus about $149M in Q2 2026 (roughly −50%). Total HYPE retired was 44.5M as of Aug 2026 — [CoinDesk, 9 Aug 2026](https://www.coindesk.com/business/2026/08/09/hyperliquid-s-rwa-perps-boom-is-eating-into-the-revenue-that-backs-hype).
- AQA v2:
  - Validators passed it around 11 Jun 2026. Coinbase became Hyperliquid's official USDC treasury deployer, and reserve yield on the Coinbase-managed portion is shared with Hyperliquid (after issuer costs) and funds AF buybacks.
  - Yield accrual started 26 Aug; the first AF payment is 3 Oct 2026, then every 30 days.
  - No dollar amounts were disclosed.

  Source: [Yahoo Finance, 12 Jun 2026](https://finance.yahoo.com/markets/crypto/articles/hyperliquid-passes-aqa-v2-fund-182853467.html).
- DefiLlama's "Hyperliquid Bridge" TVL is $7.16B (2026-09-30), up from $3.98B (2025-12-26) and $5.49B (2025-08-28) — [DefiLlama API](https://api.llama.fi/protocol/hyperliquid-bridge).

#### Revenue and fees
- Hyperliquid monthly protocol revenue (DefiLlama, series through 2026-09-29):

  | Month | Revenue | Month | Revenue |
  |---|---|---|---|
  | Jul 2025 | $90.8M | Mar 2026 | $51.5M |
  | Aug 2025 | $113.9M (peak) | Apr 2026 | $42.4M |
  | Sep 2025 | $85.2M | May 2026 | $46.3M |
  | Oct 2025 | $97.2M | Jun 2026 | $60.0M |
  | Nov 2025 | $77.7M | Jul 2026 | $38.4M |
  | Dec 2025 | $51.2M | Aug 2026 | $51.5M |
  | Jan 2026 | $59.8M | Sep 2026 | $54.6M |
  | Feb 2026 | $54.0M | | |

  - Quarterly: Q3 2025 $289.8M, Q4 2025 $226.1M, Q1 2026 $165.3M, Q2 2026 $148.6M, Q3 2026 $144.5M.
  - Full-year 2025: $817.8M; 2026 year to date: $458.5M.

  Source: [DefiLlama revenue API](https://api.llama.fi/summary/fees/hyperliquid?dataType=dailyRevenue).
- Fees (gross): Q3 2025 $356.7M, Q2 2026 $201.8M, Q3 2026 $193.0M — [DefiLlama fees API](https://api.llama.fi/summary/fees/hyperliquid?dataType=dailyFees). These match CoinDesk's figures (~$357M in Q3 2025 vs ~$202M in Q2 2026, −43%) — [CoinDesk, 9 Aug 2026](https://www.coindesk.com/business/2026/08/09/hyperliquid-s-rwa-perps-boom-is-eating-into-the-revenue-that-backs-hype).
- The "$106M August revenue record" results that appear in searches refer to August 2025, not 2026 — [The Block (2025)](https://www.theblock.co/post/368995/hyperliquids-revenue-all-time-high). CoinGecko data cited by KuCoin says Hyperliquid leads 2026 on-chain revenue with $429.04M — [KuCoin News [S]](https://www.kucoin.com/news/flash/hyperliquid-leads-2026-crypto-revenue-with-429m).
- Valuation multiples (my calculation from the sources above, using Q3 2026 annualized revenue of $578M and fees of $772M):
  - Market cap (CoinGecko circulating) / revenue ≈ 33x; protocol-circulating market cap / revenue ≈ 45x; FDV / revenue ≈ 143x; FDV / fees ≈ 107x.
  - Implied buyback yield ≈ 3.0% of the CoinGecko market cap, or 2.2% of the protocol-circulating market cap.

  Sources: [DefiLlama](https://api.llama.fi/summary/fees/hyperliquid?dataType=dailyRevenue); [CoinGecko](https://api.coingecko.com/api/v3/coins/hyperliquid).
- CF Benchmarks (10 Jun 2026) used annualized fees of $1.06B, trailing-twelve-month earnings of $0.88B, FDV of about $53.7B (61x trailing P/E on FDV), and monthly buybacks of about $74M. These are higher than DefiLlama's revenue series, so the methodologies differ — [CF Benchmarks](https://www.cfbenchmarks.com/blog/pricing-the-perp-dex-leader-a-valuation-framework-for-hyperliquid).

#### Open interest, volume and HIP-3 (live, 2026-09-30)
- Main dex: 234 perps, open interest $12.55B, 24h volume $6.02B. HIP-3 builder dexes: 10 dexes, open interest $3.88B, 24h volume $2.16B. Total open interest is therefore about $16.4B — [Hyperliquid info API](https://api.hyperliquid.xyz/info) (`metaAndAssetCtxs`, `perpDexs`).
- HIP-3 by dex:
  - `xyz` (Trade.xyz): 128 markets, open interest $3.79B (≈98% of HIP-3), 24h volume $2.10B. Top markets are BRENTOIL (24h volume $262M), CL/crude ($236M), XYZ100 ($181M, open interest $215M) and SP500 ($171M, open interest $364M).
  - `io` (EntropyIO): open interest $59M. `para` (Paragon): $19M. `mkts` (Markets by Kinetiq): $8.7M.
  - `flx`, `vntl`, `hyna`, `km`, `abcd` and `cash` showed zero open interest and volume at pull time. This could be inactive markets or a data artefact; unverified.

  Source: [Hyperliquid info API](https://api.hyperliquid.xyz/info).
- Growth of builder-deployed markets:
  - They rose from about 2% of Hyperliquid perp volume at the start of 2026 to about 50% by July 2026, and Trade.xyz holds more than 90% of HIP-3 open interest.
  - RWA perps reached a record $3.6B in open interest in July. In the week of 13–19 Jul, tokenized stocks and commodities traded $25B, 52% of volume.
  - Cost of revenue rose from under 6% (Q2 2025) to 18% (Q2 2026).
  - Hyperliquid's global perp market share (including CEXs) was about 9% (up from under 7% in May). 30-day volume was about $178B, and peak 2026 open interest was $11B (13 Jul).

  Source: [CoinDesk, 9 Aug 2026](https://www.coindesk.com/business/2026/08/09/hyperliquid-s-rwa-perps-boom-is-eating-into-the-revenue-that-backs-hype).
- HIP-3 "growth mode" gives a ≥90% reduction in all-in fees (baseline taker 0.0045%–0.009%) — [Hyperliquid docs: Fees](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees).

#### Market share versus Aster, Lighter and others (conflicting data)
- In September 2025 Aster briefly took about 70% of perp-DEX share, but by April 2026 Hyperliquid was back to about 44% and Aster was about 15% — [Bitget News [S]](https://www.bitget.com/news/detail/12560605371452); [CoinDesk, Sep 2025](https://www.coindesk.com/markets/2025/09/23/hyperliquid-s-perpetual-share-collapses-to-38-as-aster-and-lighter-gain-ground).
- Other 2026 figures conflict widely and are undated or low-quality:
  - "31.9% of tracked perp-DEX activity, $172.6B 30-day volume" — [Datawallet [S]](https://www.datawallet.com/crypto/hyperliquid-statistics).
  - "~58% of tracked perp-DEX volume, ~$200B/month". The same source puts Lighter at about $1B daily volume with $1.2B open interest, and Aster at about $1.5B daily — [AirdropAlert [S]](https://airdropalert.com/blogs/best-perp-dex/).
- CF Benchmarks flags Lighter (zero-fee, built by ex-Citadel engineers) as taking share — [CF Benchmarks](https://www.cfbenchmarks.com/blog/pricing-the-perp-dex-leader-a-valuation-framework-for-hyperliquid). CoinDesk flags Robinhood Chain clearing more than $600M in daily DEX volume as competition — [CoinDesk, 9 Aug 2026](https://www.coindesk.com/business/2026/08/09/hyperliquid-s-rwa-perps-boom-is-eating-into-the-revenue-that-backs-hype).

#### ETFs
- The first US spot HYPE ETFs launched in May 2026: 21Shares THYP, Bitwise BHYP, and Grayscale HYPG (0.29% sponsor fee, "lowest-fee"). A 2x leveraged 21Shares product (TXXH) started on 30 Apr 2026. Nearly $160M flowed in within days of launch.

  Sources: [CoinDesk, 3 Jun 2026 [S]](https://www.coindesk.com/markets/2026/06/03/grayscale-launches-lowest-fee-u-s-hyperliquid-etf-as-competition-heats-up-around-hype); [21Shares THYP](https://www.21shares.com/en-us/products-us/thyp); [21Shares TXXH [S]](https://www.21shares.com/en-us/products-us/txxh); [CNBC, 6 Jun 2026 [S]](https://www.cnbc.com/2026/06/06/bitcoin-price-crash-crypto-hype-hyperliquid-etfs.html).
- Late-September totals: net assets about $502M and cumulative net inflows about $342M. The ~$160M gap reflects price appreciation.

  Sources: [24/7 Wall St., 26 Sep 2026 [S]](https://247wallst.com/investing/cryptocurrency/2026/09/26/what-changed-for-hyperliquid-etfs-in-september/); [KuCoin News [S]](https://www.kucoin.com/news/flash/hype-spot-etfs-see-9-25m-net-inflow-in-week-through-sept-25).
- September 2026 weekly flows:
  - 7–11 Sep: −$26.4M (BHYP −$20.1M, THYP −$6.3M) — [Crypto Briefing [S]](https://cryptobriefing.com/hype-etf-outflows-26-million-september-2026/).
  - Week to 25 Sep: +$9.25M (HYPG +$3.90M, BHYP +$3.19M) — [KuCoin News [S]](https://www.kucoin.com/news/flash/hype-spot-etfs-see-9-25m-net-inflow-in-week-through-sept-25).
  - The first-ever weekly outflow was about $7M, in the week ending 17 Jul — [CoinDesk, 9 Aug 2026](https://www.coindesk.com/business/2026/08/09/hyperliquid-s-rwa-perps-boom-is-eating-into-the-revenue-that-backs-hype).

#### Treasury companies
- CoinGecko's public-treasury list totals 31,399,812 HYPE ($2.71B):
  - Hyperliquid Strategies (PURR): 29,275,085
  - Hyperion DeFi (HYPD): 1,930,000
  - Lion Group (LGHL): 194,727

  Source: [CoinGecko treasury API](https://api.coingecko.com/api/v3/companies/public_treasury/hyperliquid).
- Hyperliquid Strategies:
  - It stakes 100% of its HYPE. Its average cost is about $26 per HYPE, and its balance rose by 11.68M HYPE on 27 Aug 2026 — [CoinGecko treasuries page [S]](https://www.coingecko.com/en/treasuries/companies/hyperliquid-strategies-inc); [The Block, 27 Aug 2026 [S]](https://www.theblock.co/news/business/2026-08-27-purr-jumps-hyperliquid-strategies-1-9-billion-hype-treasury-fortress-balance-sheet-412926).
  - For the fiscal year ended 30 Jun 2026 it reported more than $2.0B in assets, no debt and about $150M in cash — [Investing.com transcript [S]](https://uk.investing.com/news/stock-market-news/earnings-call-transcript-hyperliquid-strategies-posts-strong-q4-2026-results-stock-rises-premarket-93CH-4850019).
  - Stanley Druckenmiller bought PURR — [Motley Fool, 24 Aug 2026 [S]](https://www.fool.com/investing/2026/08/24/stanley-druckenmiller-just-bought-a-company-that-h/).
- The validator "Hyperliquid Strategies x Unit" has 34.45M HYPE delegated — [Hyperliquid info API](https://api.hyperliquid.xyz/info) (`validatorSummaries`).

#### Native staking and LSTs
- 441.1M HYPE is staked across 35 validators (27 active and unjailed). The stake-weighted predicted APR net of commission is 2.17% (range 2.01%–2.23%; gross ≈2.23%). Commissions range from 0% to 100%, with a median of 3%. The four Hyper Foundation validators hold about 196M HYPE; Anchorage by Figment holds 27.2M — [Hyperliquid info API](https://api.hyperliquid.xyz/info) (`validatorSummaries`).
- Staking mechanics:
  - The reward rate is inversely proportional to √(total staked), about 2.37% at 400M staked.
  - Rewards accrue each minute, are paid daily and auto-compound.
  - The spot→staking transfer is instant; each delegation has a 1-day lockup; staking→spot has a 7-day unstaking queue (max 5 pending withdrawals).
  - Each validator must self-delegate 10k HYPE, locked for one year.
  - There is no automatic slashing, only jailing.

  Source: [Hyperliquid docs: Staking](https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/staking).
- LSTs: Kinetiq's kHYPE (launched July 2025) is the dominant HYPE liquid-staking token, and stHYPE also exists. An aggregator quotes kHYPE at about 1.99% APY and "Staked HYPE" at about 4.00%, with kHYPE at about $777M. These numbers are low-confidence aggregator data — [Stacky.fi [S]](https://stacky.fi/compare/assets/kinetic-staked-hype-vs-staked-hype); [DefiLlama Kinetiq [S]](https://defillama.com/protocol/kinetiq).

#### Catalysts named by others
- Hyperliquid Strategies management cites US market access, AQA v2, stablecoin growth and permissionless markets. The same report projects 75% of volume from RWAs by 2027, up from 52% in mid-2026 — [Investing.com [S]](https://uk.investing.com/news/stock-market-news/earnings-call-transcript-hyperliquid-strategies-posts-strong-q4-2026-results-stock-rises-premarket-93CH-4850019).

### Inferences
- The unlock overhang is large on paper: about 9.92M HYPE per month, or about 3.3% of protocol-circulating supply (about 4.5% of CoinGecko circulating) every month through about 2027. The observed low claim rates (1.75% in March; about 0.4M HYPE in September) suggest actual selling has been far smaller. The 241.5M HYPE still sitting in the non-circulating address `0x43e9…a251` is consistent with most contributor tokens remaining undistributed, but I could not verify what that address is. The overhang is a latent rather than realized supply risk, and the market reacts to the 6th-of-month dates. The next is 6 Oct 2026.
- The buyback flywheel has weakened relative to price. Revenue is about 45–50% below its 2025 peak while HYPE is up about 4x from January, so multiples have expanded sharply. Current gains are driven by flows (ETFs, treasuries, AQA v2) more than fee growth. AQA v2 is a new, rate-dependent buyback source: every 1% of net yield on about $7B of USDC equals about $70M a year, roughly 12% of current annualized AF revenue. The actual share passed to the AF is undisclosed.
- HIP-3 growth is a double-edged catalyst: it grows open interest and volume (RWA/commodity perps), but at lower fees per unit of volume, so it adds less to buybacks.
- The native staking yield (about 2.2%) is modest. It adds about $87 a year on $4,000, and the 7-day unstaking queue reduces flexibility for DCA re-allocation.

### Gaps
- The identity of the address `0x43e9abea…a251` (241.5M non-circulating HYPE) could not be confirmed. It is plausibly the core-contributor or foundation vesting address.
- The exact end date of the contributor vesting and the total remaining could not be verified from Tokenomist or DefiLlama; DefiLlama unlocks returned 403.
- The AQA v2 dollar amounts and the share of yield passed to the AF are undisclosed.
- No reliable, dated September 2026 perp-DEX market-share dataset was accessible. DefiLlama perps endpoints are paywalled (HTTP 402).
- Individual HYPE ETF AUMs and staking policies were not verified.
- LST APYs come from aggregators only.

## 3. SOL fundamentals: spot ETF status and flows, staking yield and LSTs, inflation schedule, network activity and revenue, Alpenglow and Firedancer, treasuries, Q4 2026 catalysts and risks

### Takeaway
SOL has strong institutional flow momentum: US spot SOL ETFs had record inflows in late September 2026 (~$1.9B AUM), and treasury companies hold about 19.6M SOL. Governance has voted for faster disinflation (SIMD-0550), and Alpenglow finished its testnet handoff on 24 Sep 2026. On the other side, on-chain fee revenue is down about 90% from the Jan 2025 peak, SOL remains about 60% below its ATH, and it is the higher-beta asset to BTC in a tightening macro environment. Native staking yields about 5.2%; JitoSOL yields about 4.9%.

### Cited Findings

#### ETFs
- Bitwise BSOL (a staking ETF, launched 28 Oct 2025) passed $1B in AUM in August 2026, holding about 9.33M SOL (26 Aug). It accounts for about 77–80% of all inflows into the nine US spot SOL products. At that point category AUM was about $1.49B and cumulative net inflows were over $1.3B since October 2025 — [KuCoin News [S]](https://www.kucoin.com/news/flash/bitwise-solana-staking-etf-surpasses-1-billion-in-aum-in-10-months); [The Defiant [S]](https://thedefiant.io/converge/markets/bitwise-solana-etf-is-first-to-cross-1-billion).
- September 2026 flows:
  - A record weekly inflow of $188.2M on 21–25 Sep 2026, including $86.67M on 25 Sep. The same report says all seven funds gained, which conflicts with the "nine products" count above — [The Cryptonomist, 28 Sep 2026 [S]](https://en.cryptonomist.ch/2026/09/28/solana-etf-inflows-record/); [Daily Hodl, 28 Sep 2026 [S]](https://dailyhodl.com/2026/09/28/solana-etfs-smash-record-with-188100000-in-weekly-inflows/).
  - 12 consecutive weekly inflows by mid-September — [24/7 Wall St., 19 Sep 2026 [S]](https://247wallst.com/investing/cryptocurrency/2026/09/19/solana-etfs-experience-12-consecutive-weeks-of-inflows-while-bitcoin-has-its-quietest-week-on-record/).
  - Early-September slowdown: from $153.87M (week to 28 Aug) to $6.18M (week to 4 Sep) — [24/7 Wall St., 8 Sep 2026 [S]](https://247wallst.com/investing/cryptocurrency/2026/09/08/solana-etf-inflows-fell-96-in-a-week-from-153-87-million-to-6-18-million-what-changed/).
  - SOL ETFs overtook XRP products with $1.93B in net assets, and 30-day net inflows were $278.2M — [CoinMarketCap updates [S]](https://coinmarketcap.com/cmc-ai/solana/latest-updates/).
- Farside's SOL flow table returned HTTP 403 and could not be read — [Farside](https://farside.co.uk/sol/).

#### Staking and supply (Solana mainnet RPC, epoch 1046, 30 Sep 2026)
- Current inflation is 3.624%, all to validators. The inflation governor is set to initial 8%, taper 0.15 and terminal 1.5% — [Solana RPC](https://api.mainnet-beta.solana.com) (`getInflationRate`, `getInflationGovernor`).
- Total supply is 634,996,332 SOL, with 588,005,960 circulating — [Solana RPC](https://api.mainnet-beta.solana.com) (`getSupply`).
- Active stake is 440.4M SOL, or 69.4% of supply, across 673 current validators (10 delinquent) — [Solana RPC](https://api.mainnet-beta.solana.com) (`getVoteAccounts`).
- My calculation: the implied base staking yield is 3.624% / 0.694 ≈ 5.22%, before commission and excluding MEV and priority fees. Annual issuance is about 23.0M SOL (≈$2.75B). 21Shares puts the current staking yield at about 5.25% (Aug 2026) — [21Shares, 26 Aug 2026](https://www.21shares.com/en-us/insights/solana-simd-550-simd-553-staking-yield).
- JitoSOL: APY 4.85%, pool TVL about 10.4M SOL, JitoSOL supply about 7.98M (2026-09-30 09:03 UTC) — [Jito API](https://kobe.mainnet.jito.network/api/v1/stake_pool_stats).

#### Inflation changes
- SIMD-0550 doubles the annual disinflation rate from −15% to −30%, reaching the 1.5% terminal rate around H1 2029 instead of 2032. Projected staking yields fall to about 4.34% in year 1, 3% in year 2 and 2.25% in year 3 — [21Shares](https://www.21shares.com/en-us/insights/solana-simd-550-simd-553-staking-yield); [Helius [S]](https://www.helius.dev/blog/simd-550-solana-disinflation).
- SGP-0002 (the governance vote for SIMD-0550) passed with 67.001% on 28 Aug 2026. The activation epoch is not scheduled: it needs SIMD-0607 merged, client implementation, and a feature gate at 95% of stake. "Nothing changes today" — [Solana Compass [S]](https://solanacompass.com/news/simd-0607-must-merge-before-solanas-disinflation-rate-can-activate-anza-says); [crypto.news [S]](https://crypto.news/solana-inflation-cut-clears-vote-with-67-support/); [P2P.org [S]](https://p2p.org/economy/sgp-0002-solana-disinflation-vote-results/). The RPC governor still showing taper 0.15 is consistent with this.
- SIMD-0553 (Temporal) adds a compute-unit burn fee, raising daily burns from 600–800 SOL to 7,500–9,000 SOL at current activity. It was "formally approved and merged" on 20 Jul 2026; mainnet activation status is not verified — [21Shares](https://www.21shares.com/en-us/insights/solana-simd-550-simd-553-staking-yield).

#### Network activity and revenue
- DefiLlama Solana chain fees:
  - Monthly: $241.4M (Jan 2025) → $42.7M (Aug 2025) → $18.1M (Dec 2025) → $11.5M (Jun 2026, the low) → $22.2M (Aug 2026) → $23.9M (Sep 2026, through the 29th).
  - Quarterly: Q1 2025 $345.0M, Q2 2026 $41.1M, Q3 2026 $61.9M.
  - Chain "revenue" (burned base fees) is only about $1.5–2.8M a month in 2026.

  Sources: [DefiLlama Solana fees](https://api.llama.fi/summary/fees/solana?dataType=dailyFees); [DefiLlama Solana revenue](https://api.llama.fi/summary/fees/solana?dataType=dailyRevenue).
- 21Shares, January 2026: of about $10M in daily ecosystem fees, only up to $100k reaches the protocol (<10%). Solana held about $15B in stablecoins, processed about 2.2B transactions a week, and had about 4% inflation with about 70% staked — [21Shares, 26 Jan 2026](https://www.21shares.com/en-eu/insights/solana-2026-outlook-scale-is-proven-value-capture-is-not).

#### Upgrades
- Alpenglow:
  - It targets finality of about 150 ms (versus about 12 s). Its testnet handoff completed on 24 Sep 2026 at slot 444,625,255, with mainnet expected after an observation period. The original target was Q1 2026 — [Crowdfund Insider, Sep 2026 [S]](https://www.crowdfundinsider.com/2026/09/313498-solana-sol-update-anza-turns-on-alpenglow-testnet-and-devnet-switch-to-100-150ms-finality/); [CoinMarketCap Academy [S]](https://coinmarketcap.com/academy/article/solana-alpenglow-upgrade-enters-community-validator-testing); [Solana.com](https://solana.com/upgrades/alpenglow).
  - Anatoly Yakovenko and Roger Wattenhofer denied rumors of a 28 Sep mainnet activation — [KuCoin News [S]](https://www.kucoin.com/news/flash/solana-developers-deny-alpenglow-mainnet-activation-on-september-28).
- Firedancer: the full Firedancer mainnet launch was announced on 12 Dec 2025 at Breakpoint Abu Dhabi. By mid-2026 about 14% of stake ran full Firedancer and about 26% ran Frankendancer, against a target of 50% Firedancer by Q2–Q3 2026 — [RPC Fast blog [S]](https://rpcfast.com/blog/what-is-firedancer-solana-validator-client).

#### Treasury companies
- Forward Industries (FWDI) held about 8.16M SOL on 21 Sep 2026 (~1.39% of circulating supply), all staked — [GlobeNewswire/company PR, 21 Sep 2026](https://www.globenewswire.com/news-release/2026/09/21/3365847/0/en/forward-industries-sol-holdings-rise-to-approximately-8-16-million-sol.html).
- CoinGecko's list totals 19.61M SOL ($2.34B, 3.33% of market cap):

  | Company | SOL held (CoinGecko) |
  |---|---|
  | Forward Industries (FWDI) | 7.55M (stale versus the company PR) |
  | DeFi Development (DFDV) | 2.49M |
  | Upexi (UPXI) | 2.17M |
  | SkyAI, formerly Sharps (SKYA) | 2.08M |
  | Solana Company (HSDT) | 2.06M |
  | Galaxy (GLXY) | 0.78M |

  Source: [CoinGecko treasury API](https://api.coingecko.com/api/v3/companies/public_treasury/solana).
- Solana Company's holdings had decreased to 2,071,127 SOL as of its May 2026 10-Q — [Yahoo Finance [S]](https://finance.yahoo.com/news/5-largest-publicly-traded-solana-132838567.html).

#### Q4 2026 calendar
- Breakpoint 2026 runs 15–17 Nov 2026 at Olympia London — [Solana Compass [S]](https://solanacompass.com/news/solana-breakpoint-2026-comes-to-london-for-the-first-time-november-15-17-at-olympia); [solana.com/breakpoint](https://solana.com/breakpoint).

### Inferences
- The main Q4 2026 upside catalysts for SOL are:
  - an Alpenglow mainnet date;
  - scheduling of the SIMD-0550 activation epoch;
  - continued ETF inflows (record week 21–25 Sep);
  - Breakpoint (15–17 Nov).
- The main risks are:
  - a weak fee and value-capture trend (Q2 2026 chain fees were about 88% below Q1 2025);
  - the Alpenglow timeline slipping again;
  - macro tightening hitting a high-beta asset;
  - potential treasury-company selling (at least one, HSDT, has reduced holdings).
- A DCA buyer holding SOL natively can earn about 4.9–5.2% (JitoSOL or native), roughly $195–210 a year on $4,000. This is more than double HYPE's native yield. Yields will fall if SIMD-0550 activates.

### Gaps
- Primary ETF flow tables (Farside, SoSoValue) could not be accessed (403). ETF figures come from news aggregators and conflict on the fund count (seven vs nine).
- Stablecoin supply on Solana and app revenue for September 2026 were not pulled.
- Firedancer stake share comes from a secondary blog and dates from mid-2026.
- SIMD-0553 mainnet activation status is unverified.
- The SOL ETF total AUM of $1.93B comes from an AI-summary page.

## 4. Hyperliquid spot mechanics: which SOL token, deposit and withdrawal, fees, spread and depth for ~$1,200 orders, resting ladder orders, HYPE staking, risks; comparison with Jupiter plus an LST

### Takeaway
On Hyperliquid, "SOL" spot is Unit's USOL ("Unit Solana"), traded against USDC as pair `@156`. HYPE is native, pair `@107`. Resting GTC or post-only limit orders at each rung cost 0.04% as maker (≈$0.48 per $1,200). Spread and slippage for $1,200 are under 1 bp on both books. The trade-offs are Unit's 2-of-3 guardian custody for USOL, and the fact that USOL earns no native staking yield on Hyperliquid. Buying SOL on Jupiter costs about 0.1% but gives native, stakeable SOL (~4.9–5.2%).

### Cited Findings

#### Instruments
- HYPE/USDC is spot pair `@107` (spot asset ID 10107). Other HYPE pairs:
  - HYPE/USDT0 (`@207`): $70k in 24h volume.
  - HYPE/USDE (`@255`): $165k.
  - HYPE/USDH (`@232`): no 24h volume.

  Source: [Hyperliquid info API](https://api.hyperliquid.xyz/info) (`spotMetaAndAssetCtxs`).
- USOL:
  - Token index 254, fullName "Unit Solana". It was deployed on 2025-04-11 by `0xf036…6155`, with max supply 500M, szDecimals 3 and HyperEVM contract `0x068f321fa8fb9f0d135f290ef6a3e2813e1c8a29`.
  - It trades as USOL/USDC `@156` (asset ID 10156), with candles from 2025-05-10.
  - 24h notional volume is $5.93M (30-day average about $8.6M a day), versus HYPE/USDC at $77.7M (30-day average about $87M a day).

  Source: [Hyperliquid info API](https://api.hyperliquid.xyz/info).
- Spot assets are referenced as 10000 + their index in `spotMeta.universe` — [Hyperliquid docs: Exchange endpoint](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/exchange-endpoint).

#### Funding the account
- USDC:
  - Native USDC via Circle CCTP is "the preferred method"; the legacy Arbitrum bridge is deprecated.
  - Legacy bridge deposits have a minimum of 5 USDC; smaller amounts are "lost forever".
  - Deposits are credited in under a minute and withdrawals arrive in 3–4 minutes. Withdrawals need only a user signature on Hyperliquid, and validators handle the Arbitrum side.

  Source: [Hyperliquid docs: USDC](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/usdc).
- Bridge security (secondary source): withdrawals require signatures from more than 2/3 of validator staking power, with a 5-minute dispute window — [Eco support article [S]](https://eco.com/support/en/articles/15082533-hyperliquid-arbitrum-bridge).
- Moving USDC between the perp and spot balances uses the `usdClassTransfer` action — [Hyperliquid docs: Exchange endpoint](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/exchange-endpoint).

#### SOL deposits and withdrawals via Unit
- Minimum deposit and withdrawal is 0.12 SOL. Unit also supports SPL tokens PUMP, FART, SPX and BONK — [Unit docs: Supported assets](https://docs.hyperunit.xyz/unit/about-unit/supported-assets.md).
- Solana deposits need 32 confirmations, about 13 seconds — [Unit docs: API](https://docs.hyperunit.xyz/developers/api.md).
- Unit "does not collect revenue from deposits or withdrawals". Fees are only the source and destination network costs — [Unit docs: Fees FAQ](https://docs.hyperunit.xyz/faq/how-do-fees-on-unit-work.md).
- Users deposit from their own wallet to a Unit-generated address and withdraw to any native-chain address — [Unit docs](https://docs.hyperunit.xyz/).

#### Unit custody risk
- Unit uses 2-of-3 MPC threshold signing (TSS) among "Guardians". Key shares are encrypted at rest (KMS) and combined only inside secure enclaves.
- The documentation does not name the guardians, mention insurance, or address 2-of-3 collusion.

  Source: [Unit docs: Security](https://docs.hyperunit.xyz/architecture/security.md).

#### Fees
- Base spot fees are 0.070% taker and 0.040% maker; base perp fees are 0.045% taker and 0.015% maker.
- Volume tiers use 14-day volume = perp volume + 2 × spot volume. Tier 1 (over $5M) spot fees are 0.060% taker and 0.030% maker.
- Staking discounts:

  | HYPE staked | Discount |
  |---|---|
  | >10 | 5% |
  | >100 | 10% |
  | >1,000 | 15% |
  | >10,000 | 20% |
  | >100,000 | 30% |
  | >500,000 | 40% |

- "Aligned quote assets" get 20% lower taker fees; stablecoin-to-stablecoin pairs are 80% lower.

  Sources: [Hyperliquid docs: Fees](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees); confirmed by the live `userFees` schedule (referral discount 4%) — [Hyperliquid info API](https://api.hyperliquid.xyz/info).
- Cost per order (my calculation): $1,200 costs $0.48 as maker or $0.84 as taker. The full $4,000 costs $1.60 as maker or $2.80 as taker. With a 10% staking discount, the maker fee on $1,200 is $0.43.

#### Order books (snapshot 2026-09-30 10:19:58 UTC)

| Book | Spread | Slippage vs mid: $1,200 | $4,000 | $25,000 | Other |
|---|---|---|---|---|---|
| HYPE/USDC `@107` | 0.12 bps | 0.06 bps | 0.06 bps | 0.45 bps | Top-20-level ask depth ≈ $115k, all within 0.1% |
| USOL/USDC `@156` | 0.84 bps | 0.66 bps | 1.08 bps | 1.76 bps | Visible depth within ±0.5%: ≈$360k asks / $309k bids |
| SOL perp (comparison) | — | — | — | — | Visible depth within ±0.1%: ≈$2.0M asks / $2.9M bids |

Source: [Hyperliquid info API](https://api.hyperliquid.xyz/info) (`l2Book`, 20 levels per side).

#### Placing the ladder
- Time-in-force options are "Gtc" (rests until cancelled), "Alo" (post-only, cancelled rather than taking liquidity) and "Ioc". Trigger orders and TWAP orders are also available.
- The minimum order value is $10.

  Source: [Hyperliquid docs: Exchange endpoint](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/exchange-endpoint).
- Prices can have up to 5 significant figures and no more than (8 − szDecimals) decimals for spot. Sizes round to szDecimals — HYPE 2 decimals (0.01 HYPE), USOL 3 decimals (0.001 USOL) — [Hyperliquid docs: Tick and lot size](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/tick-and-lot-size); [Hyperliquid info API](https://api.hyperliquid.xyz/info).

#### Staking spot HYPE on Hyperliquid
- `cDeposit` moves HYPE from spot to staking, `tokenDelegate` delegates to a validator (1-day lockup), and `cWithdraw` moves staking back to spot (7-day queue) — [Hyperliquid docs: Exchange endpoint](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/exchange-endpoint).
- The APR is about 2.17% net, compounded daily, as above — [Hyperliquid info API](https://api.hyperliquid.xyz/info); [Hyperliquid docs: Staking](https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/staking).

#### Venue risks (HLP and market manipulation)
- March 2025: an ETH whale liquidation cost HLP about $4M — [The Block, 2025](https://www.theblock.co/post/345866/hype-drop-hlp-vault-loss-hyperliquid-whale-liquidation).
- "Trader torches $3M to punch a $5M hole in Hyperliquid's vault" — [Cointelegraph via TradingView [S]](https://www.tradingview.com/news/cointelegraph:09c51f126094b:0-trader-torches-3m-to-punch-a-5m-hole-in-hyperliquid-s-vault/) (date not verified).
- A reported 9 Apr 2026 Fartcoin manipulation cost HLP $1.5M — [SmartContractsHacking [S], low-quality source](https://smartcontractshacking.com/hacks/hyperliquid-hack-2026).
- Hyperliquid has said such events were "no protocol exploit or hack" — [DL News [S]](https://www.dlnews.com/articles/defi/hyperliquid-denies-hack-after-investors-suffer-hlp-loss/).

#### Jupiter alternative
- Limit orders (V2) cost 0.03% on stable pairs and 0.1% on other pairs, plus a possible routing fee. Recurring (DCA) orders cost 0.1% per execution. Each execution also pays a small Solana transaction fee.

  Sources: [Jupiter developer docs [S]](https://developers.jup.ag/docs/trigger); [Jupiter support FAQ [S]](https://support.jup.ag/hc/en-us/sections/18432822685340-FAQs); [Jupiter Recurring](https://jup.ag/recurring).
- My calculation: $4,000 costs about $4.00 on Jupiter (0.1%) versus $1.60 as maker on Hyperliquid.
- Native or LST staking after buying: JitoSOL APY 4.85% — [Jito API](https://kobe.mainnet.jito.network/api/v1/stake_pool_stats). The implied native base yield is about 5.22% before commission — [Solana RPC](https://api.mainnet-beta.solana.com).

#### ETF alternative
- US brokerage users can hold BSOL (a staking ETF) or the HYPE ETFs THYP, BHYP or HYPG (HYPG sponsor fee 0.29%) — [KuCoin News [S]](https://www.kucoin.com/news/flash/bitwise-solana-staking-etf-surpasses-1-billion-in-aum-in-10-months); [CoinDesk [S]](https://www.coindesk.com/markets/2026/06/03/grayscale-launches-lowest-fee-u-s-hyperliquid-etf-as-competition-heats-up-around-hype).

### Inferences
- Practical ladder workflow on Hyperliquid:
  1. Fund with native USDC via CCTP.
  2. Move the USDC to the spot balance with `usdClassTransfer`.
  3. Place three post-only (Alo) or GTC limit bids per asset, for example about $1,200–1,333 each. For HYPE use `@107` at $80/$70/$60; for SOL use `@156` at equivalent levels.
  4. Leave the orders resting.
  5. Optionally move filled HYPE into staking (`cDeposit` + `tokenDelegate`).
  6. Optionally withdraw USOL to native SOL through Unit (at least 0.12 SOL; network fees only) and stake it as an LST.
- For orders this size, execution cost is driven almost entirely by the fee tier, not by depth. Both books absorb $1,200 with under 1 bp of slippage, and the USOL book is thinner but still ample for $1,200–4,000.
- For HYPE, Hyperliquid spot is the natural venue: native asset, deepest spot book, native staking.
- For SOL, choosing Hyperliquid (USOL) over Jupiter saves about 0.06% in fees (≈$2.40 on $4,000). In exchange the buyer takes Unit guardian custody risk and forgoes about 5% staking yield unless they withdraw to Solana. Over a holding period of more than a few weeks, the lost yield outweighs the fee saving: about $17 a month on $4,000 at 5%.
- Not verified here: whether resting spot bids lock ("hold") USDC. If they do, that USDC cannot earn yield while it waits for deep rungs.

### Gaps
- The Hyperliquid bridge and validator signer-set details for 2026 were only confirmed through a third-party article, and the Hyperliquid bridge docs page returned 404.
- The Unit guardian identities are not disclosed in the docs.
- Not verified: whether the Hyperliquid UI labels USOL as "SOL", and whether USOL can be staked or lent on HyperEVM.
- Jupiter fee details come from search summaries. The "ultra routing fee 0–0.5%" wording is unverified.
- Not verified from docs: the spot order "hold" mechanics and open-order count limits.

## 5. Q4 2026 sentiment and outlook: bull and bear cases for SOL and HYPE (reported, not endorsed)

### Takeaway
The macro backdrop has tightened: the Fed hiked in September 2026 and signals one more hike. Crypto nevertheless had its first positive quarter since Q3 2025. For HYPE, reputable frameworks span roughly $40 (bear) to $172 (bull), with the debate centred on fee dilution, unlock overhang and valuation versus flow-driven demand. For SOL, Standard Chartered's end-2026 target is $250 and 21Shares' 2026 range is $95–$197. The debate centres on institutional flows and upgrades versus weak value capture.

### Cited Findings

#### Macro
- The Fed raised rates 25 bps to 3.75%–4.00% in September 2026, its first hike since July 2023, in a unanimous vote.
- Updated projections imply one more 25 bp hike in 2026.
- Chair Kevin Warsh's Jackson Hole speech shifted hike odds.
- BTC was up about 32% for Q3, heading for its first positive quarterly close since Q3 2025.
- There was a "Clarity Act setback".

Sources: [CoinDesk, 18 Sep 2026 [S]](https://www.coindesk.com/markets/2026/09/18/bitcoin-weathers-september-storm-as-rate-hikes-and-clarity-act-setback-test-bulls); [The Cryptonomist, 28 Sep 2026 [S]](https://en.cryptonomist.ch/2026/09/28/bitcoin-price-outlook-fed-data/); [Yahoo Finance [S]](https://finance.yahoo.com/markets/crypto/articles/fed-rate-hike-odds-hit-092724315.html).

#### HYPE: bull case
- CF Benchmarks (10 Jun 2026), probability-weighted 20/60/20:
  - Bull: 7% share, ~$164B FDV, about $172 per token.
  - Base: 5% share, ~$102B FDV, about $106.
  - Fair value about $101B FDV.

  Source: [CF Benchmarks](https://www.cfbenchmarks.com/blog/pricing-the-perp-dex-leader-a-valuation-framework-for-hyperliquid).
- Bitwise argues Hyperliquid "could power future finance" as HYPE ETFs gain traction — [CoinDesk, 28 May 2026 [S]](https://www.coindesk.com/coindesk-news/2026/05/28/bitwise-bets-hyperliquid-could-power-future-finance-as-hype-etfs-gain-traction).
- Further bull drivers:
  - RWA/HIP-3 expansion, projected at 75% of volume by 2027 — [Investing.com [S]](https://uk.investing.com/news/stock-market-news/earnings-call-transcript-hyperliquid-strategies-posts-strong-q4-2026-results-stock-rises-premarket-93CH-4850019).
  - AQA v2 yield-funded buybacks from 3 Oct — [Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/hyperliquid-passes-aqa-v2-fund-182853467.html).
  - Treasury and ETF demand (section 2).
- ARK has noted Hyperliquid at 67% of crypto app revenue (together with Pump.fun), and Grayscale has compared its model to AWS — [CoinDesk, 9 Aug 2026](https://www.coindesk.com/business/2026/08/09/hyperliquid-s-rwa-perps-boom-is-eating-into-the-revenue-that-backs-hype).
- DCo (13 Mar 2026) argued HYPE deserves about $60 even under a bearish framework — [AO Trading blog [S]](https://aotrading.io/blogs/hyperliquid-hype-bear-case-rally-priced-in-april-2026).

#### HYPE: bear case
- CF Benchmarks bear case: 3% share, ~$38B FDV, about $40 per token (−30% from June levels).
- CF Benchmarks' named risks:
  - Lighter's zero-fee competition.
  - Contributor vesting (about 238M over 24 months) "exceeds buyback absorption capacity through 2027".
  - CFTC and regulatory exposure.
  - The buyback is "a protocol rule, not a contractual obligation, and could change".

  Source: [CF Benchmarks](https://www.cfbenchmarks.com/blog/pricing-the-perp-dex-leader-a-valuation-framework-for-hyperliquid).
- HIP-3/RWA volume is "eating into the revenue that backs HYPE": gross revenue fell 43% from Q3 2025 to Q2 2026, and AF buybacks halved — [CoinDesk, 9 Aug 2026](https://www.coindesk.com/business/2026/08/09/hyperliquid-s-rwa-perps-boom-is-eating-into-the-revenue-that-backs-hype).
- In April 2026 HYPE traded at 167x FDV/annualized revenue and 39x market cap/revenue — [AO Trading [S]](https://aotrading.io/blogs/hyperliquid-hype-bear-case-rally-priced-in-april-2026). My Q3 2026 calculation gives about 143x FDV/revenue (section 2).
- Seeking Alpha published a bearish piece on the treasury vehicle, "Hyperliquid Strategies: Fade The Crypto HYPE" — [Seeking Alpha [S]](https://seekingalpha.com/article/4885831-hyperliquid-strategies-fade-the-crypto-hype).
- HYPE ETF flows turned negative in early September (−$26.4M in one week) — [Crypto Briefing [S]](https://cryptobriefing.com/hype-etf-outflows-26-million-september-2026/).

#### SOL: bull case
- Standard Chartered (Geoffrey Kendrick, 3 Feb 2026):
  - End-2026 target $250, cut from $310.
  - Longer-term path: $400 (2027), $700 (2028), $1,200 (2029), $2,000 (2030).
  - Thesis: a shift from memecoins toward stablecoin micropayments.

  Sources: [The Block, 3 Feb 2026 [S]](https://www.theblock.co/news/markets/2026-02-03-standard-chartered-cuts-solana-2026-target-shift-memecoins-micropayments-388248); [CoinDesk, 3 Feb 2026 [S]](https://www.coindesk.com/markets/2026/02/03/this-analyst-expects-solana-to-reach-usd2-000-by-2030-despite-cutting-his-2026-target).
- 21Shares (26 Jan 2026): bull case $197 (rising protocol fees, institutional stablecoin settlement, multi-client resilience); base case $150 — [21Shares](https://www.21shares.com/en-eu/insights/solana-2026-outlook-scale-is-proven-value-capture-is-not).
- 21Shares (26 Aug 2026): lower issuance from SIMD-550/553 is structurally supportive, and precedents (EIP-1559, Cosmos Prop 848) saw positive near-term performance — [21Shares](https://www.21shares.com/en-us/insights/solana-simd-550-simd-553-staking-yield).
- Flows: record ETF week (section 3).

#### SOL: bear case
- 21Shares bear case of $95: protocol capture fails to improve, competition, weaker staking demand, stablecoin growth stalls or rotates to other chains, centralization and governance concerns — [21Shares](https://www.21shares.com/en-eu/insights/solana-2026-outlook-scale-is-proven-value-capture-is-not).
- Standard Chartered's cut reflected skepticism about how fast Solana converts throughput into sustained fee-generating activity — [DL News [S]](https://www.dlnews.com/articles/markets/solana-price-target-dropped-in-2025-but-raised-for-2030-standard-chartered/).
- Chain fees are down about 90% from the January 2025 peak — [DefiLlama](https://api.llama.fi/summary/fees/solana?dataType=dailyFees).
- Low-quality aggregator data put 2026 forecasts anywhere from $61 to $306, and prediction-market end-2026 odds at about 12% for $200 — [CoinMarketCap/Yahoo roundup [S], low-quality](https://finance.yahoo.com/markets/crypto/articles/high-could-solana-sol-realistically-164124502.html).

### Inferences
- Positioning into Q4:
  - HYPE enters Q4 near its highs, with strong flows and high expectations. Scheduled events are the 3 Oct first AQA v2 payment and the 6 Oct, 6 Nov and 6 Dec unlocks.
  - SOL enters Q4 in recovery mode with improving flows and pending catalysts (Alpenglow mainnet, SIMD-0550 scheduling, Breakpoint 15–17 Nov).
  - Both remain hostage to BTC and Fed direction: SOL β≈1.2–1.3 and HYPE β≈1.1–1.3 to BTC.
- Price versus published reference points:
  - HYPE at $86 sits between CF Benchmarks' bear ($40) and base ($106) cases.
  - SOL at $119 sits between 21Shares' bear ($95) and base ($150) cases, well below Standard Chartered's $250.
  - The ladder rungs are within the historical noise band for both. HYPE $60 and SOL around $83–90 would roughly correspond to the respective bear or support zones.

### Gaps
- Few reputable, dated September 2026 analyst notes specifically on Q4 2026 were found. Most HYPE and SOL "prediction" pages are low-quality and were excluded or flagged.
- Not researched here: options-implied volatility and skew (e.g., Deribit SOL; HYPE options), which would give forward-looking touch probabilities.
- The macro facts come from search summaries of CoinDesk, Yahoo and Cryptonomist, not full reads.
