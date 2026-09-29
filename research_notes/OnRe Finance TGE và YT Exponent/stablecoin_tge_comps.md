# Stablecoin / Synthetic-Dollar / RWA-Yield TGE Comparables for OnRe (ONyc) — data as of 2026-09-29

Method note (applies to all sections): "Current" prices/FDV = CoinGecko API snapshot 2026-09-29 ~11:50 UTC ([CoinGecko API](https://api.coingecko.com/api/v3/coins/re)). Day-1 prices = UTC daily candles from Binance ([data-api.binance.vision klines](https://data-api.binance.vision/api/v3/klines?symbol=RESOLVUSDT&interval=1d&startTime=0&limit=5)), Gate ([api.gateio.ws](https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=SLX_USDT&interval=1d)), KuCoin ([api.kucoin.com](https://api.kucoin.com/api/v1/market/candles?type=1day&symbol=CAP-USDT)), MEXC ([api.mexc.com](https://api.mexc.com/api/v3/klines?symbol=CAPUSDT&interval=1d)). Day-1 "open" prints are listing-auction artifacts (0.01–0.30), so FDV at TGE uses the **day-1 close** x total/max supply. TVL = DefiLlama protocol TVL ([api.llama.fi/protocol/…](https://api.llama.fi/protocol/re)) or DefiLlama stablecoin circulating supply ([stablecoins.llama.fi](https://stablecoins.llama.fi/stablecoins)) as labelled. Items marked (est.) are my estimates.

## Q1. Comparables table: TGE date, TVL at TGE, points length, airdrop %, FDV at TGE vs now, FDV/TVL, listings, post-TGE narrative

### Takeaway
Of 17 stablecoin/yield/RWA tokens that TGE'd in 2025–2026 with usable price data, the median token trades **-68% below its day-1 close** (13 of 17 are below), and the median drawdown from ATH is **-89%**. Day-1 FDV/TVL clustered around **~1.4x (median)** and is **~1.1x now**. The closest OnRe comp, Re Protocol (RE, onchain reinsurance), launched 2026-06-18 at a **$436M day-1-close FDV on $258M TVL (1.7x)**, and on 2026-09-29 sits at **$479M FDV on $390M TVL (1.2x), +10% vs day-1 close**.

### Cited Findings
**Master table** (FDV in $M; TVL in $M; % chg = current price vs day-1 close; "pts mo" = months from points launch to TGE, mostly est.)

| Token (project) | TGE / 1st trade | Pts mo | S1 / community airdrop % | Day-1 close ($) | FDV day-1 close | Current px 09-29 | Current FDV | % chg vs d1 | TVL at TGE | TVL now | FDV/TVL TGE | FDV/TVL now | ATH (date) / from ATH | Listings at TGE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ENA (Ethena) | 2024-04-02 | 1.4 | 5% S1 shards (750M) | 0.775 | 11,625 | 0.2542 | 3,810 | -67% | 1,560 | 5,344 | 7.45 | 0.71 | 1.52 (2024-04-11) / -83% | Binance Launchpool+spot; Gate, KuCoin, MEXC same day |
| USUAL (Usual) | 2024-11-19 | ~4–6 (est.) | 7.5% Pills + 7.5% Binance Launchpool | 0.285 | ~1,141 (4B max then) | 0.0144 | 28 | -95% | 379 | 91 (USD0 supply 547) | 3.0 | 0.3 | 1.61 (2024-12-19) / -99% | Binance Launchpool + pre-market; Gate pre-mkt; KuCoin/MEXC 2024-12-18 |
| ONDO (Ondo) | 2024-01-18 | n/a | n/q | 0.221 | 2,210 | 0.5248 | 5,248 | +137% | n/a | n/a | n/a | n/a | 2.14 (2024-12-15) / -75% | Gate, KuCoin, MEXC; Binance only 2025-04-11 |
| SYRUP (Maple) | 2024-11-14 (Gate) | n/q | Drips (n/q) | 0.225 | ~280 | 0.2501 | 311 | +11% | 316 | 3,016 | 0.88 | 0.10 | 0.653 (2025-06-25) / -62% | Gate; KuCoin/MEXC ~11-25; Binance 2025-05-06 |
| AVL (Avalon) | 2025-02-12 | ~8 (est.) | n/q (Avalon Points + USDa bounty) | 0.414 | 414 | 0.0226 | 23 | -95% | 1,794 | 251 | 0.23 | 0.09 | 0.787 (2025-03-07) / -97% | Bybit spot (+launchpool), Gate |
| PLUME (Plume, RWA chain) | 2025-01-21 | n/q | n/q | 0.156 | 1,557 | 0.0192 | 192 | -88% | n/a | 3 (chain) | n/a | n/a | 0.248 (2025-03-19) / -92% | Gate/KuCoin/MEXC; Binance 2025-08-18 |
| ELX (Elixir, deUSD) | 2025-03-07 | ~14 (est.) | 7% potions (S1 1.25/S2 3.0/S3 2.75) | 0.389 | 389 | 0.0012 | 1 | -100% | 63 | ~0 | 6.2 | n/a | 0.735 (2025-03-10) / -100% | MEXC Innovation, Bitget Launchpool, Gate |
| HUMA (Huma, Solana PayFi) | 2025-05-26 | ~1.5 (est.) | 5% S1 (500M) + 2.5% Binance Launchpool | 0.0669 | 669 | 0.0290 | 290 | -57% | n/a | 382 | n/a | 0.76 | 0.116 (2025-05-26) / -75% | Binance Launchpool #70 + spot 13:00 UTC; Gate/KuCoin/MEXC |
| RESOLV (Resolv, USR) | 2025-06-10 (Binance 06-11) | ~8.8 (est.) | 10% S1 | 0.351 | 351 | 0.0193 | 19 | -95% | 351 | 14 | 1.00 | 1.38 | 0.409 (2025-06-11) / -95% | Binance HODLer + spot; Gate/KuCoin/MEXC/OKX |
| SPK (Spark/Sky) | 2025-06-17 | n/q | 3% Ignition + 2% HODLer | 0.0576 | 576 | 0.0240 | 240 | -58% | 6,273 | 7,267 | 0.09 | 0.03 | 0.184 (2025-07-23) / -87% | Binance HODLer #23 + spot |
| TREE (Treehouse) | 2025-07-29 | n/q | n/q | 0.672 | 672 | 0.0465 | 46 | -93% | 560 | 77 | 1.20 | 0.60 | 1.36 (2025-07-29) / -97% | Binance HODLer + spot |
| DAM (Reservoir, rUSD) | 2025-08-18 | ~9 | 10% S1 (= 20B points) | n/a (Alpha only) | n/a | 0.0023 | 2 | n/a | 54 | 72 | n/a | 0.03 | 0.149 (2025-09-18) / -98% | Binance Alpha + Binance futures only |
| XPL (Plasma chain) | 2025-09-25 | 3.5 | 25M XPL (0.25%) deposit drop + 10% sale @ $500M FDV | 1.277 | 12,773 | 0.1020 | 1,020 | -92% | 2,052 (stables on chain) | 1,475 | 6.2 | 0.69 | 1.68 (2025-09-27) / -94% | Binance spot + majors |
| FF (Falcon, USDf) | 2025-09-29 | ~6 | ≤8.3% (Miles + Buidlpad sale + Kaito 0.3%) + 1.5% HODLer | 0.282 | 2,817 | 0.1206 | 1,206 | -57% | 1,899 (USDf) | 1,213 | 1.48 | 0.99 | 0.771 (2025-09-29) / -84% | Binance HODLer + spot 13:00 UTC; Gate/KuCoin/MEXC |
| EDEN (OpenEden, USDO/TBILL) | 2025-09-30 | ~8.5 (est.) | 7.5% Bills + 1.5% HODLer | 0.4005 | 400 | 0.0635 | 64 | -84% | 235 (USDO) | 15 | 1.70 | 4.23 | 1.31 (2025-09-30) / -95% | Binance HODLer #47 + spot 11:00 UTC |
| YB (Yield Basis) | 2025-10-15 | n/q | n/q | 0.670 | 670 | 0.0932 | 70 | -86% | 153 | 138 | 4.38 | 0.51 | 0.819 (2025-10-15) / -89% | Binance spot + majors |
| STABLE (Stable chain) | 2025-12-08 | ~2–5 (est.) | 10% Genesis (testnet + pre-deposit) | 0.0215 | 2,150 | 0.0290 | 2,902 | +35% | 706 (stables on chain, peak 12-16) | 25 | 3.0 | 116 | 0.0432 (2026-05-14) / -33% | Binance Alpha airdrop; Bybit, Bitget, Backpack; no Binance/Coinbase spot |
| UP (Unitas, Solana/BNB USDu) | 2026-03-13 | ~9 (est.) | 3% Booster (Alpha users); 45% eco & community total | 0.060 (TGE sale $0.005) | 60 (sale: $5M) | 0.2393 | 239 | +298% | 81 | 58 | 0.74 | 4.13 | 0.523 (2026-08-31) / -54% | Binance Wallet Exclusive TGE #44 / Alpha; MEXC |
| CHIP (USD.AI) | 2026-04-21 | ~7 (est.) | 3% (300M; paid to airdrop cohort in USDC) + 7% ICO @ $300M | 0.0613 | 613 | 0.0452 | 452 | -26% | 281 (USDai) | 226 | 2.18 | 2.00 | 0.140 (2026-04-23) / -68% | Binance, Coinbase, Upbit, Bybit + 8 more spot |
| SLX (Solstice, Solana USX) | 2026-05-25 | ~8 | 8.5% S1 Flares | 0.207 | 207 | 0.0655 | 66 | -68% | 401 (USX) | 215 | 0.52 | 0.30 | 0.658 (2026-06-27) / -90% | Binance Alpha first; Gate, Bitget, OKX, Kraken; MEXC 05-26 |
| **RE (Re Protocol, reinsurance)** | **2026-06-18** | **10.5** | **7% S1 (70M RE); S2 ≥3.5%** | **0.436** | **436** | **0.4794** | **479** | **+10%** | **258** | **390** | **1.69** | **1.23** | **1.079 (2026-06-20) / -56%** | **Binance spot (USDT/USDC/TRY), KuCoin "world premiere", MEXC** |
| CAP (Cap, cUSD) | 2026-06-26 | ~10.5 | $4.2M "stabledrop" in cUSD; 5% sale @ $106M FDV | 0.0293 | 293 (Defiant: 325) | 0.0581 | 581 | +98% | 221 | 292 | 1.33 | 1.99 | 0.0783 (2026-08-14) / -26% | KuCoin, MEXC; Coinbase/Upbit/Bybit/Kraken now listed |

Supporting citations for table rows (dates, allocations, listings, launch facts):
- ENA: S1 Shards ran ~6 weeks from Feb 19 2024; 750M ENA (5%) airdrop; ENA launched ~$1B mcap — [The Defiant](https://thedefiant.io/news/defi/ethena-labs-ena-launches-at-usd1-billion-post-airdrop-as-sats-campaign-kicks-off); S2 Sats to Sep 2 2024 = 5% — [Binance Square](https://www.binance.com/en/square/post/6273119441873); S3 3.5% — [Airdrop Alert](https://airdropalert.com/airdrops/ethena-season-3/); S4 3.5% — [The Defiant](https://thedefiant.io/news/defi/ethena-season-4-rewards-go-live); S5 2% — [KuCoin](https://www.kucoin.com/blog/how-to-claim-ethena-season-5-airdrop). ENA ATL $0.0702 on 2026-06-30 (CoinGecko API).
- USUAL: Binance Launchpool Nov 15–19 2024, 300M USUAL = 7.5% of 4B supply; pre-market Nov 19 — [Coinspeaker](https://www.coinspeaker.com/binance-introduces-usual-launchpool-pre-market-trading-soon/); Pills = 7.5% of supply minted at TGE; top 1.5% wallets 10% instant — [CoinGecko Learn](https://www.coingecko.com/learn/what-is-usual-crypto-rwa-usual-airdrop), [Usual blog](https://usual.money/blog/airdrop-the-genesis-of-ownership)
- ELX: TGE 2025-03-07, MEXC 10:00 UTC; Bitget Launchpool incl. deUSD pool — [CoinMarketCap Academy](https://coinmarketcap.com/academy/article/how-to-claim-elixir-elx-token-airdrop-step-by-step-guide); potions S1 1.25%/S2 3.00%/S3 2.75% — [Elixir mirror](https://mirror.xyz/0x25832C2fC7B7380E5B74Ea280ea2D2C98a0d5644/XXZuIQ1Awjzn2KkNGENrJcl1zvsj2RVUWKunVHFq2rA)
- AVL: TGE/Bybit spot 2025-02-12; 1B supply — [Decrypt](https://decrypt.co/305462/avalon-labs-announces-avl-token-and-bybit-listing), [Bybit Learn](https://learn.bybit.com/en/daily-bits/avalon-labs-launches-avl-token)
- HUMA: 70th Binance Launchpool May 23 (3 days), 250M = 2.5%; Binance spot May 26 13:00 UTC — [ChainCatcher](https://www.chaincatcher.com/en/article/2182643); 500M (5%) S1 airdrop, 325M to Feathers LPs, snapshot May 18 — [Bitget Academy](https://www.bitget.com/academy/human-finance-huma-airdrop-listing-date-investor-guide); "HUMA falls over 45%, erasing post-launch gains" — [crypto.news](https://crypto.news/huma-finance-token-falls-over-45-erasing-post-launch-gains/)
- RESOLV: 1B supply, 10% S1 airdrop (as stRESOLV) — [Resolv docs](https://docs.resolv.xyz/litepaper/resolv-token/resolv-token-airdrop); Binance HODLer + spot 2025-06-11 — [ChainCatcher](https://www.chaincatcher.com/en/article/2185644)
- SPK: Binance 23rd HODLer 200M (2%), spot 2025-06-17 09:00 UTC, 17% circulating; Ignition 300M (3%) — [Crypto.ro](https://crypto.ro/en/news/binance-announces-spark-spk-its-23rd-hodler-airdrops-project/), [CoinCarp](https://www.coincarp.com/events/spark-fi-new-listing-on-binance-hodler-airdrops/)
- DAM: Binance Alpha first platform, spot+futures 2025-08-18 — [Chainplay](https://chainplay.gg/blog/binance-alpha-launch-reservoir-dam-aug-18/), [ChainCatcher](https://www.chaincatcher.com/en/article/2198259); S1 20B points = 10% of DAM — [Reservoir X](https://x.com/reservoir_xyz/status/1929636144125563386)
- XPL: TGE 2025-09-25; $500M FDV sale; 25M XPL equally to verified depositors; 19% of supply at TGE — [The Defiant](https://thedefiant.io/news/blockchains/plasma-mainnet-beta-xpl-token-launch), [Bitget Academy](https://www.bitget.com/academy/plasma-tge-september-25-2025-xpl-token-mainnet-beta-launch)
- FF: Binance HODLer 150M (1.5%), spot 2025-09-29 — [CryptoNewsZ](https://www.cryptonewsz.com/binance-falcon-finance-as-49th-hodler-airdrop/); Community Airdrops & Launchpad Sale 8.3%, 2.34B (23.4%) circulating at TGE — [Falcon tokenomics](https://falcon.finance/news/introducing-ff-tokenomics); Kaito 0.3% — [Bitget](https://www.bitget.com/news/detail/12560604992603); Buidlpad $350M/$450M FDV tiers — [Dropstab](https://dropstab.com/research/alpha/falcon-finance-ff-token-sale-what-participants-need-to-know); "FF loses over 70% on suspected team selling" — [Cryptopolitan](https://www.cryptopolitan.com/falcon-finance-loses-suspected-team-selling/)
- EDEN: 1B supply; 7.5% Bills airdrop (21.3% unlocked at TGE) — [OpenEden docs](https://docs.openeden.com/openeden-foundation/eden/eden-token-distribution); Binance 47th HODLer 15M (1.5%), trading 2025-09-30 11:00 UTC — [Coinfomania](https://coinfomania.com/binance-eden-47th-hodler-airdrop-15m-tokens/)
- STABLE: mainnet+TGE 2025-12-08; 10% Genesis Distribution; >$1.8B pre-deposit commitments; Bitget/Backpack/Bybit spot, no Binance/Coinbase spot at launch — [PANews](https://www.panewslab.com/en/articles/2050e827-52be-412e-9b7a-5cf172897c6b), [HTX](https://www.htx.com/news/stable-tge-tonight-will-the-market-still-buy-into-the-stable-Uv72EXhY/); ~$0.046 TGE → $0.0092 low on 2025-12-24 (-80% in 16 days) — [CoinEx](https://www.coinex.com/en/academy/detail/4326-stable-token-price-prediction?pId=2&sId=5)
- UP: Binance Wallet Exclusive TGE #44, 2026-03-13; 1B supply; 12.6% circulating; TGE price $0.005; 30M UP (3%) Booster — [PANews](https://www.panewslab.com/en/articles/019cdbd7-3251-72b7-8df5-b95b83c655b2), [BingX](https://bingx.com/en/flash-news/post/binance-wallet-launches-unitas-up-booster-and-tge-with-up-airdrop), [MEXC blog](https://blog.mexc.com/news/what-is-unitas-labs-up-yield-bearing-stablecoin-earning-8-15-apy-binance-tge-march-13/); TVL surged past $100M when airdrop campaign announced mid-Jan 2026 — [Solana Compass](https://solanacompass.com/projects/unitas)
- CHIP: live 2026-04-21 on 12 spot venues incl. Binance, Coinbase, Upbit, Bybit; ICO protected-CHIP settles at $270M/$190M FDV; airdrop cohort paid USDC 2026-04-20; Allo S2 to 2026-10-14 — [USD.AI blog](https://usd.ai/insights/chip-is-live); 3% airdrop / 7% ICO at $300M FDV — [KuCoin news](https://www.kucoin.com/news/flash/usd-ai-to-conduct-30m-fdv-token-sale-on-coinlist), [CryptoRank](https://cryptorank.io/ico/usd-ai)
- SLX: TGE 2026-05-25 on Binance Alpha, Gate, Bitget, OKX; >40% loss within hours; post-selloff $0.20, mcap $64M, FDV $198.3M — [cryptonews.net](https://cryptonews.net/news/analytics/32917942/); 8.5% airdrop, 99.68% of users in lowest tier sharing 0.49% of pool, surprise vesting, Kraken listing — [SolanaFloor](https://solanafloor.com/news/solstice-slx-launch-sparks-backlash-from-airdrop-farmers-over-surprise-vesting); tokenomics 1B, Airdrops 10%, ~24% circulating at TGE; Sept-2026 re-phasing of 75M SLX (7.5%) into Sept 2026 release — [Solstice docs](https://docs.solstice.finance/solstice-for-users/slx/tokenomics.md)
- RE: TGE/claims 2026-06-18; 159.6M RE circulating at TGE; KuCoin RE/USDT 14:00 UTC; Binance RE/USDT, RE/USDC, RE/TRY — [TradingView/CoinMarketCal Binance](https://www.tradingview.com/news/coinmarketcal:5429a86fc094b:0-re-binance-listing-18-june-2026/), [TradingView/CoinMarketCal KuCoin](https://www.tradingview.com/news/coinmarketcal:57d07696e094b:0-re-kucoin-listing-18-june-2026/); 1B fixed supply, 50% ecosystem, governance-only (no revenue claim) — [Re tokenomics](https://docs.re.xyz/governance-and-tokenomics/re-tokenomics.md); S1 2025-08-03→2026-05-31 = 7% of supply; S2 from 2026-06-01 ≥3.5% — [About Re Points](https://docs.re.xyz/re-points/about-re-points.md); claim/vesting formula (≤150M points 100% liquid; e.g. 1B pts → 23.5% at TGE; rest 6 semiannual tranches with TVL-holding requirements) — [Re vesting](https://docs.re.xyz/re-points/vesting-+-tvl-requirements.md); pre-TGE: $409M premiums written since inception, ~4,000 onchain capital participants — [InsuranceNewsNet](https://insurancenewsnet.com/oarticle/resilience-foundation-to-launch-the-re-governance-token)
- CAP: auction 5.5x oversubscribed, $16.4M from 1,002 bids at $0.011 = $106M FDV; launched 2026-06-26; first-day close $325M FDV — [The Defiant](https://thedefiant.io/news/defi/cap-labs-cap-token-auction-106m-fdv-oversubscription), [The Defiant](https://thedefiant.io/news/defi/cap-token-climbs-to-2-lending-borrowing-protocol-by-volume-10-days-after-launch); 10B supply, ~15.6% circulating at TGE — [Bitget](https://www.bitget.com/asia/amp/news/detail/12560605474641); stabledrop cut from $12M to $4.2M after backlash — [The Defiant](https://thedefiant.io/news/defi/cap-cuts-its-stabledrop-airdrop-to-usd4-2m-from-usd12m-as-backlash-mounts)
- TVL figures: DefiLlama API for [ethena](https://api.llama.fi/protocol/ethena), [usual](https://api.llama.fi/protocol/usual), [resolv](https://api.llama.fi/protocol/resolv), [elixir](https://api.llama.fi/protocol/elixir), [avalon-labs](https://api.llama.fi/protocol/avalon-labs), [cap](https://api.llama.fi/protocol/cap), [maple-finance](https://api.llama.fi/protocol/maple-finance), [spark](https://api.llama.fi/protocol/spark), [treehouse-protocol](https://api.llama.fi/protocol/treehouse-protocol), [yield-basis](https://api.llama.fi/protocol/yield-basis), [unitas](https://api.llama.fi/protocol/unitas), [reservoir-protocol](https://api.llama.fi/protocol/reservoir-protocol), [re](https://api.llama.fi/protocol/re), [huma](https://api.llama.fi/protocol/huma), [onre](https://api.llama.fi/protocol/onre); stablecoin supply for USDe (id 146), USDf (246), USDO (241), USDai (309), USX (310), reUSD (339) — [DefiLlama stablecoins](https://stablecoins.llama.fi/stablecoin/339); chain stablecoins for [Plasma](https://stablecoins.llama.fi/stablecoincharts/Plasma) and [Stable](https://stablecoins.llama.fi/stablecoincharts/Stable)

**Post-TGE price path (close vs day-1 close; UTC daily candles, venues as above):**
- ENA: +60% d7 → +3% d30 → -35% d90 → -50% d180 → -57% d365 → -67% now. Held up best among big launches thanks to USDe growth to $14.8B peak (Oct 2025), but fell with the 2026 bear market (ATL $0.070 on 2026-06-30).
- USUAL: +406% d30 (Binance listing mania, ATH $1.61 Dec 2024) → -18% d90 → -95% now; TVL collapsed from $1.87B peak (Jan 2025) to $91M after the Jan 2025 USD0++ redemption-floor change.
- RESOLV: -57% d30 → -79% d180 → -95% now; USR supply $220M at TGE → $6.1M now.
- ELX: -68% d30 → ~-100% now; deUSD wound down (DefiLlama TVL ≈ $0).
- AVL: 0% d30 → -64% d180 → -95% now; TVL $1.79B → $251M.
- HUMA: -52% d30 → -63% d180 → -57% now (stable around $0.025–0.03 for a year; TVL now $382M).
- SPK: +3% d90 → -63% d180 → -58% now, despite Spark TVL rising to $7.3B (token decoupled from TVL; FDV/TVL 0.03x).
- TREE: -42% d30 → -86% d180 → -93% now.
- XPL: -69% d30 → -90% d90 → -92% now. CoinDesk: $1.67 peak to $0.309 by 2025-10-30, only material activity a $676M lending vault — [CoinDesk](https://www.coindesk.com/business/2025/10/30/plasma-s-xpl-token-crashes-80-as-hype-fades-amid-woeful-debut); stablecoins on Plasma fell from >$6B to <$2B within two months as ~65% had been farming XPL in lending markets — [Yahoo Finance/CoinDesk](https://finance.yahoo.com/news/plasma-xpl-token-crashes-80-111909476.html)
- FF: -46% d30 → -75% d180 → -57% now (rebounded +32% in last 30d); USDf supply $1.90B → $1.21B.
- EDEN: -68% d30 → -93% d180 → -84% now; USDO supply $235M → $15M.
- YB: -36% d30 → -82% d180 → -86% now.
- STABLE: -34% d30 → +23% d90 → +58% d180 → +35% now (ATH $0.0432 on 2026-05-14) even though stablecoins on the Stable chain fell from $706M (2025-12-16) to $25M — price/TVL completely decoupled (FDV/TVL 116x).
- UP (Unitas): +229% d30 → +550% d90 → +604% d180 → +298% now (ATH $0.523 on 2026-08-31) while TVL fell $81M → $58M; launched from an extremely low $5M sale FDV. (Pine Analytics thread titled "$UP at $5M FDV: The Math Doesn't Work" — [X](https://x.com/PineAnalytics/status/2031911500927938840), content not retrievable.)
- CHIP: +12% d7 (d2 close $0.113, ATH $0.140 on 04-23) → -22% d30 → -51% d90 → -26% now.
- SLX: +57% d30 (ATH $0.658 on 2026-06-27, ~3x day-1) → -67% d90 → -68% now; ATL $0.0578 on 2026-09-16; USX supply $401M → $215M.
- RE: -9% d30 (after spiking to $1.08 on 06-20, +148% vs day-1 close) → +1% d90 → +10% now; ATL $0.357 on 2026-07-20; Re TVL kept rising to an all-time high $390M on 2026-09-29.
- CAP: -23% d30 (ATL $0.0155 on 07-12) → +71% d90 → +98% now; $862M cumulative volume in first 10 days — [The Defiant](https://thedefiant.io/news/defi/cap-token-climbs-to-2-lending-borrowing-protocol-by-volume-10-days-after-launch)
- Market backdrop (Binance closes): BTC $124.7k (2025-10-06) → $87.6k (2025-12-31) → $58.6k (2026-06-30) → $83.5k (2026-09-28); ETH $4,684 → $1,572 → $2,689; SOL $232 → $74 → $119 — [Binance klines](https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=1d)

**Pre-TGE / no-token comps (as of 2026-09-29):** No governance token found on CoinGecko for Perena (TVL $13.9M), Noble, Agora, Midas, Level (lvlUSD; TVL $150M in Jun 2025 → $0.46M now), Neutrl (S1 1.1T+ points, $230M peak AUM; S2 runs Jun 4 → mid-Sep 2026 into TGE — [Today in DeFi](https://news.todayindefi.com/p/airdrop-alpha-re-protocol-announced), [search summary](https://coinlaunch.space/projects/neutrl-finance/)), Exponent (TVL $80M). Apyx (apxUSD $317M supply) TGE scheduled 2026-10-13; S1 4% / S2 6% of supply — [Today in DeFi](https://news.todayindefi.com/p/airdrop-alpha-re-protocol-announced). Older comps Sky (SKY, $1.95B FDV, converted from MKR — not a points TGE), Frax (FRAX ex-FXS, $0.317, $31.6M FDV), f(x) (FXN $31.9, $39M FDV) are not points-driven TGEs and are included only as context (CoinGecko API).

### Inferences
- Median FDV/TVL at day-1 close for 2025–26 yield/stablecoin protocol tokens (excl. chains XPL/STABLE/PLUME; n=12: RESOLV, AVL, ELX, TREE, FF, EDEN, YB, UP, CHIP, SLX, RE, CAP) = **~1.4x** (range 0.23x–6.2x); current median ≈ **1.1x**. Applied to OnRe's $295M TVL (DefiLlama, 2026-09-29): ~1.1x → ~$325M; 1.4x → ~$410M; Re-like 1.7x at TGE → ~$500M; Solstice-like 0.5x → ~$150M. These are framing ranges, not forecasts.
- Tokens that launched at modest FDVs relative to TVL (UP $60M, CAP $293M after a $106M auction, RE $436M) have held or gained; mega-FDV launches (XPL $12.8B, FF $2.8B, ENA $11.6B) and heavily-farmed launches with post-TGE TVL flight (RESOLV, EDEN, TREE, ELX, AVL) lost 57–100%.
- For Re specifically, TVL growth after TGE (+51%) plus a governance-only token seems to have anchored price near the day-1 level; the Season 2 (≥3.5%) and TVL-holding requirements on vested S1 tranches likely reduced post-TGE TVL flight — a design worth noting for OnRe.

### Gaps
- Day-1 price for DAM (Binance Alpha-only listing) not found; CoinGecko 365-day window starts 2025-09-30.
- Huma TVL at TGE (May 2025): DefiLlama series for "huma" only starts 2026-05-27; Messari report blocked (403).
- OpenEden TVL at TGE uses USDO supply only (TBILL not included — DefiLlama now shows $0 for OpenEden RWA products); Ondo TVL not available in DefiLlama protocol API.
- Whether ENA/RE/CAP were on Coinbase/OKX/Bybit on day 1 not fully verified (MEXC headline lists "MEXC, KuCoin, Binance, OKX, Coinbase" for RE — [MEXC news](https://www.mexc.com/news/1155257), page returned 410).
- Conflicting RE allocation summaries in secondary sources (50/13/17/20 vs 50/22.5/18/12.8); only 50% ecosystem and 7% S1 confirmed by Re docs.

## Q2. Typical Season-1 airdrop allocation (% of supply)

### Takeaway
Season-1 points airdrops for farmed stablecoin/yield protocols cluster at **5–10% of total supply, median ≈7%** (Re 7%, Solstice 8.5%, OpenEden 7.5%, Usual Pills 7.5%, Resolv 10%, Reservoir 10%, Stable 10%, Huma 5%, Ethena 5%, Elixir 7% over 3 seasons, USD.AI 3%, Spark Ignition 3%), usually topped up by a 1.5–2.5% Binance HODLer/Launchpool slice and followed by Season 2 at ~3.5–6%.

### Cited Findings
- Ethena S1 5% (750M ENA); S2 5%; S3 3.5%; S4 3.5%; S5 2% — [The Defiant](https://thedefiant.io/news/defi/ethena-labs-ena-launches-at-usd1-billion-post-airdrop-as-sats-campaign-kicks-off), [Airdrop Alert](https://airdropalert.com/airdrops/ethena-season-3/), [KuCoin](https://www.kucoin.com/blog/how-to-claim-ethena-season-5-airdrop)
- Re S1 7% (S2 ≥3.5%) — [Re docs](https://docs.re.xyz/re-points/about-re-points.md)
- Solstice S1 8.5% of supply (Airdrops bucket 10% total) — [SolanaFloor](https://solanafloor.com/news/solstice-slx-launch-sparks-backlash-from-airdrop-farmers-over-surprise-vesting), [Solstice docs](https://docs.solstice.finance/solstice-for-users/slx/tokenomics.md)
- Resolv S1 10% — [Resolv docs](https://docs.resolv.xyz/litepaper/resolv-token/resolv-token-airdrop)
- OpenEden Bills 7.5% + Binance HODLer 1.5% — [OpenEden docs](https://docs.openeden.com/openeden-foundation/eden/eden-token-distribution), [Coinfomania](https://coinfomania.com/binance-eden-47th-hodler-airdrop-15m-tokens/)
- Usual Pills 7.5% + Launchpool 7.5% — [CoinGecko Learn](https://www.coingecko.com/learn/what-is-usual-crypto-rwa-usual-airdrop), [Coinspeaker](https://www.coinspeaker.com/binance-introduces-usual-launchpool-pre-market-trading-soon/)
- Huma S1 5% + Launchpool 2.5% — [Bitget Academy](https://www.bitget.com/academy/human-finance-huma-airdrop-listing-date-investor-guide), [ChainCatcher](https://www.chaincatcher.com/en/article/2182643)
- Reservoir S1 10% (20B points) — [Reservoir X](https://x.com/reservoir_xyz/status/1929636144125563386)
- Stable Genesis 10% — [HTX](https://www.htx.com/news/stable-tge-tonight-will-the-market-still-buy-into-the-stable-Uv72EXhY/)
- Elixir potions S1 1.25% + S2 3.00% + S3 2.75% — [Elixir mirror](https://mirror.xyz/0x25832C2fC7B7380E5B74Ea280ea2D2C98a0d5644/XXZuIQ1Awjzn2KkNGENrJcl1zvsj2RVUWKunVHFq2rA)
- USD.AI 3% airdrop / 7% ICO — [KuCoin news](https://www.kucoin.com/news/flash/usd-ai-to-conduct-30m-fdv-token-sale-on-coinlist)
- Spark Ignition 3% + HODLer 2% — [Crypto.ro](https://crypto.ro/en/news/binance-announces-spark-spk-its-23rd-hodler-airdrops-project/)
- Falcon: Community Airdrops & Launchpad Sale combined 8.3% + HODLer 1.5% — [Falcon](https://falcon.finance/news/introducing-ff-tokenomics)
- Plasma: only 25M XPL (0.25%) free airdrop to depositors; main reward was the right to buy in the 10% sale at $500M FDV — [The Defiant](https://thedefiant.io/news/blockchains/plasma-mainnet-beta-xpl-token-launch)
- Apyx S1 4%, S2 6% — [Today in DeFi](https://news.todayindefi.com/p/airdrop-alpha-re-protocol-announced)
- Binance HODLer/Launchpool slices: FF 1.5%, EDEN 1.5%, SPK 2%, HUMA 2.5%, USUAL 7.5% (Launchpool); Unitas Booster 3% — sources above

### Inferences
- A median ~7% S1 (range 5–10%) plus ~1.5–2.5% exchange-program slice is the "market standard" an OnRe S1 would be benchmarked against; Re's 7% S1 + ≥3.5% S2 is the most directly comparable structure.
- 2026 launches increasingly add anti-dump mechanics (Re TVL-holding vesting; Solstice 3-month vesting tied to TVL; Usual/Re caps on whales; Cap paying in cUSD instead of tokens; USD.AI paying airdrop cohort in USDC) — farmers' realized value is falling.

### Gaps
- S1 % for Falcon Miles alone, Avalon, Treehouse, Yield Basis, Unitas (S1 farmer share within 45% community), Maple Drips not found.

## Q3. Realized $ value per point / per $1k TVL-day farmed

### Takeaway
Outside Ethena's 2024 S1 outlier (**$15 per $1k TVL-day**, ~550% APR-equivalent), realized airdrop value for stablecoin/yield points programs in 2024–2026 was **~$0.2–0.7 per $1k of TVL per day (≈7–26% APR-equivalent at day-1 close)**, median ≈ **$0.44/$1k-day (~16% APR)**; after typical post-TGE declines, value realized a few months later was roughly one-third to one-half of that. Re's S1 paid roughly **$0.6+/$1k-day (~22%+ APR)** at day-1 close.

### Cited Findings
Computed = airdrop tokens x day-1 close ÷ (average DefiLlama TVL x days in season). TVL series from DefiLlama API (links in Q1); prices from exchange klines (Q1 method note); allocations from sources in Q2.
- Ethena S1 shards (2024-02-19→04-01, 43d, avg Ethena TVL $899M): 750M x $0.775 = $581M → **$15.0/$1k-day** (~549% APR)
- Ethena S2 sats (2024-04-02→09-02, 154d, avg USDe $2.93B): 750M x $0.208 (claim-date close 2024-09-05) = $156M → **$0.35/$1k-day** (~12.6% APR)
- Ethena S3 (2024-09-03→2025-03-24, 203d, avg USDe $4.45B): 525M (3.5%) x $0.369 (2025-04-01) = $194M → **$0.22/$1k-day** (~7.8% APR)
- Resolv S1 (~2024-09-17→2025-05-15, 241d, avg $331M): 100M x $0.351 = $35.1M → **$0.44/$1k-day** (~16% APR)
- OpenEden Bills (USDO, 2025-01-14→09-29, 259d, avg $173M): 75M x $0.40 = $30.0M → **$0.67/$1k-day** (~24.5% APR)
- Elixir Apothecary S1–S3 (2024-01→2025-02, 425d, avg $123M): 70M x $0.389 = $27.3M → **$0.52/$1k-day** (~19% APR)
- Solstice S1 (USX supply, 2025-10-01→~2026-04-20, 202d, avg $308M): 85M x $0.207 = $17.6M → **$0.28/$1k-day** (~10% APR); at current $0.0655 → ~$0.09 (~3%)
- USD.AI Allo S1 (USDai, 2025-09-28→2026-03-31, 185d, avg $550M): 300M x $0.0613 = $18.4M → **$0.18/$1k-day** (~6.6% APR)
- Re S1 (Re protocol TVL; DefiLlama data starts 2025-12-01, avg of available data $165M applied over 302 days): 70M x $0.436 = $30.5M → **~$0.61/$1k-day (~22% APR)**; at day-3 close ~$1.00 → ~$1.4/$1k-day. Re TVL path: $85.8M (2025-12-01) → $124M (2026-02-01) → $166M (2026-04-01) → $281.5M (2026-05-31) → $258M (TGE) → $390M (2026-09-29) — [DefiLlama Re](https://api.llama.fi/protocol/re)
- Plasma: 25M XPL x $1.277 = ~$32M free airdrop split equally (9,304 XPL per verified depositor, "$1 = $10,000" for minimum depositors) — [KuCoin Square](https://www.kucoin.com/square/post/content_6ab808fc003e86000766b240), [Bankless](https://www.bankless.com/read/news/plasma-launches-mainnet-beta-with-surprise-10k-bonus)
- Reservoir: 20B S1 points → 100M DAM = 0.005 DAM/point; at $0.078 (CoinGecko, 2025-09-30) ≈ $0.00039/point; at ATH $0.149 ≈ $0.00074/point; at current $0.0023 ≈ $0.000012/point (DAM data: CoinGecko API)
- Solstice anecdote: "many users saw 3k–6k+ SLX (≈$300–600 at $100M FDV)" (low-reliability blog) — [Medium](https://medium.com/@thecryptect/unlock-the-solstice-airdrop-fortune-your-step-by-step-guide-to-earning-4-5-figure-rewards-9fb2ec5d6906)
- Point-accrual references: Re 5x hold / 6.5x Pendle YT / 12x Pendle LP / 20x Curve LP (10k reUSD → 50k points/day) — [Airdrop Alert](https://airdropalert.com/airdrops/re-protocol/); Falcon 1 point/$/day on stables — [search summary of Falcon guides](https://cryptorank.io/drophunting/falcon-finance-activity930); OnRe 1x hold, 2x LP (Kamino/Orca/Raydium), 3x lending/borrowing, 4x yield trading, live since 2025-09-11 — [OnRe blog](https://www.onre.finance/blog/onre-introduces-points-program-rewarding-onyc-participation-across-defi)

### Inferences
- OnRe's points program has accrued ~**$53.4B of TVL-days** (DefiLlama "onre" avg TVL $139M x 384 days, 2025-09-11→2026-09-29, before multipliers). Mapping comp ratios: Solstice-like $0.28 → ~$15M airdrop value; Resolv-like $0.44 → ~$23M; Re-like $0.61 → ~$33M; OpenEden-like $0.67 → ~$36M. At a 7% S1, those imply FDVs of roughly ~$215M, ~$335M, ~$470M, ~$510M respectively — useful as a cross-check against the FDV/TVL method in Q1.
- Per-point dollar values are rarely published; $/TVL-day (or APR-equivalent) is the more robust comp metric.

### Gaps
- Total points issued not found for Ethena S2 (only a speculative pre-season estimate of 10.1T sats — [Binance Square](https://www.binance.com/en/square/post/6273119441873)), Resolv, Solstice, Re, OpenEden, Falcon, USD.AI; so exact $/point cannot be computed except Reservoir.
- Computations ignore multipliers/boosts, partner-protocol TVL, referral points and non-TVL cohorts (e.g. Solstice presale/Xeet cohorts; Plasma sale allocation), so they are order-of-magnitude.

## Q4. Time from points launch to TGE (median months)

### Takeaway
For 2025–2026 comps the points-launch-to-TGE lag is **~8.5 months median** (range ~1.5–14), lengthening in 2026 (Re ~10.5, Cap ~10.5, Unitas ~9, Solstice ~8). OnRe's program has been live **~12.6 months** (since 2025-09-11), already longer than most comps.

### Cited Findings
- Ethena: S1 shards ~6 weeks (from 2024-02-19) before 2024-04-02 TGE — [The Defiant](https://thedefiant.io/news/defi/ethena-labs-ena-launches-at-usd1-billion-post-airdrop-as-sats-campaign-kicks-off)
- Re: S1 2025-08-03 → 2026-05-31 (301 days); TGE 2026-06-18 → ~10.5 months — [Re docs](https://docs.re.xyz/re-points/about-re-points.md)
- Solstice: Flares S1 from September/October 2025 launch; TGE originally targeted December 2025, actually 2026-05-25 (~8 months) — [CoinChapter](https://coinchapter.com/airdrop_post/flares-airdrop-opens-path-to-slx-token-rewards-on-solana/), [SolanaFloor](https://solanafloor.com/news/solstice-slx-launch-sparks-backlash-from-airdrop-farmers-over-surprise-vesting)
- Plasma: deposit campaign June 2025 → TGE 2025-09-25 (~3.5 months) — [Bitget Academy](https://www.bitget.com/academy/plasma-tge-september-25-2025-xpl-token-mainnet-beta-launch)
- Cap: DefiLlama TVL begins 2025-08-14; TGE targeted Q1 2026 "if internal targets are met" — [Bitget](https://www.bitget.com/news/detail/12560605158875), actual 2026-06-26 (~10.5 months)
- Unitas: DefiLlama TVL from 2025-06-20; airdrop campaign announced mid-Jan 2026; TGE 2026-03-13 (~9 months from launch) — [Solana Compass](https://solanacompass.com/projects/unitas)
- Reservoir: TVL from 2024-11-11; S1 recap June 2025; TGE 2025-08-18 (~9 months) — [Reservoir X](https://x.com/reservoir_xyz/status/1929636144125563386)
- Elixir: Apothecary seasons over 2024 → TGE 2025-03-07 (~14 months, est.) — [Elixir mirror](https://mirror.xyz/0x25832C2fC7B7380E5B74Ea280ea2D2C98a0d5644/XXZuIQ1Awjzn2KkNGENrJcl1zvsj2RVUWKunVHFq2rA)
- Neutrl: S2 June 4 → mid-Sep 2026 "directly into TGE" (TGE not yet happened as of 2026-09-29); Apyx: S2 ends 2026-10-11, TGE 2026-10-13 — [Today in DeFi](https://news.todayindefi.com/p/airdrop-alpha-re-protocol-announced)
- OnRe points live since 2025-09-11 — [OnRe blog](https://www.onre.finance/blog/onre-introduces-points-program-rewarding-onyc-participation-across-defi)

### Inferences
- Estimated lags (months): HUMA ~1.5, STABLE ~2–5, XPL 3.5, FF ~6, CHIP ~7, SLX ~8, EDEN ~8.5, RESOLV ~8.8, DAM ~9, UP ~9, RE ~10.5, CAP ~10.5, ELX ~14 → median ≈ 8.5 months. Several teams (Solstice, Cap) slipped their announced TGE by 4–6 months, typically waiting for TVL targets or better markets.

### Gaps
- Exact points-start dates for Resolv, Huma (Feathers), OpenEden (Bills), Falcon (Miles), USD.AI (Allo), Stable are estimated from DefiLlama first-TVL dates or launch news, not official announcements.

## Q5. Is the stablecoin TGE narrative cooling? (drawdowns, launch-FDV trend)

### Takeaway
Yes on valuations, but it is mixed on post-TGE performance. Median day-1-close FDV fell from **~$1.7B (2024 cohort)** to **~$0.5B (H1 2025)**, then **~$0.67B for H2 2025 protocols** (excl. the Plasma/Stable chains) and **~$0.29B in 2026** (UP $60M, SLX $207M, CAP $293M, RE $436M, CHIP $613M). The 2025 cohorts lost a median **-42% (H1) / -70% (H2) by day 90**. The smaller, cheaper 2026 cohort is roughly flat at day 90 (median +1%; UP +550%, CAP +71%, RE +1%, CHIP -51%, SLX -67%). That result is flattered by the Q3-2026 market rebound: BTC went from $58.6k on 2026-06-30 to $83.5k on 2026-09-28.

### Cited Findings
- Median current price vs day-1 close across 17 tokens launched 2025–2026: **-68%** (mean -33%, skewed by UP +298%); 13 of 17 below day-1 close; median drawdown from ATH **-89%** (computed; Q1 sources)
- Median price change vs day-1 close by horizon (17 non-2024 tokens): d7 **-27%**, d30 **-36%**, d90 **-51%**, d180 **-68%** (n=13), d365 **-91%** (n=8) (computed from exchange klines)
- By cohort at d90: 2024 (ENA, USUAL, ONDO, SYRUP) median -27%; H1 2025 (RESOLV -53, ELX -78, AVL -31, HUMA -60, SPK +3, PLUME +9) median **-42%**; H2 2025 (EDEN -83, FF -67, XPL -90, STABLE +23, TREE -73, YB -38) median **-70%**; 2026 (CAP +71, SLX -67, CHIP -51, UP +550, RE +1) median **+1%** (computed)
- Day-1-close FDV by cohort: 2024 median $1.68B (ENA $11.6B, ONDO $2.2B, USUAL ~$1.1B, SYRUP ~$0.28B); H1 2025 median $495M (AVL 414, PLUME 1,557, ELX 389, HUMA 669, RESOLV 351, SPK 576); H2 2025 median $1.41B incl. chains (XPL $12.8B, FF $2.8B, STABLE $2.15B, TREE 672, YB 670, EDEN 400) or ~$671M protocols-only; 2026 median $293M (computed)
- Post-TGE TVL retention (TVL now ÷ TVL at TGE): RESOLV 0.04, EDEN (USDO) 0.06, AVL 0.14, TREE 0.14, SLX 0.54, FF 0.64, UP 0.71, XPL (chain stables) 0.72, CHIP 0.80, YB 0.90, SPK 1.16, CAP 1.32, DAM 1.33, RE 1.51; ELX ~0, Stable chain 0.04 vs Dec-2025 peak; median ≈ **0.68** (computed from DefiLlama)
- Market context: BTC $124.7k (2025-10-06) → $58.6k (2026-06-30) → $83.5k (2026-09-28); SOL $232 → $74 → $119 (Binance klines); "Crypto fell hard in 2026. Stablecoin supply barely moved" — [Coinmonks/Medium](https://medium.com/coinmonks/crypto-fell-hard-in-2026-stablecoin-supply-barely-moved-what-broke-the-link-98e3e8abfd12); (unverified web-search summaries, exact source page not confirmed:) yield-bearing stablecoin supply outpaced the broader market by >15x from mid-Oct 2025, and in Q1 2026 tokenized treasuries added $2.12B vs stablecoins $1.19B — see [Bitget news](https://www.bitget.com/news/detail/12560605151213), [Coinmonks/Medium](https://medium.com/coinmonks/crypto-fell-hard-in-2026-stablecoin-supply-barely-moved-what-broke-the-link-98e3e8abfd12)
- Farmer backlash is a recurring 2026 theme: Solstice surprise vesting (99.68% of users in lowest tier) — [SolanaFloor](https://solanafloor.com/news/solstice-slx-launch-sparks-backlash-from-airdrop-farmers-over-surprise-vesting); Cap stabledrop cut from $12M to $4.2M — [The Defiant](https://thedefiant.io/news/defi/cap-cuts-its-stabledrop-airdrop-to-usd4-2m-from-usd12m-as-backlash-mounts); Unitas: an analyst view (web-search summary, likely Pine Analytics) that "75%+ of the protocol's current TVL exists because of airdrop farming and will leave shortly after the token launches" — [Pine Analytics X](https://x.com/PineAnalytics/status/2031911500927938840) (not directly retrievable); realized: Unitas TVL $106M peak (2026-04-21) → $58M now (DefiLlama)

### Inferences
- The market has re-priced stablecoin/yield governance tokens. Launch FDVs have fallen about 5x since 2024, and 2025 launches mostly round-tripped to 5–15% of their day-1 value. The 2026 names that held up launched cheaply (UP $5M sale; CAP $106M auction) or kept TVL growing after TGE (RE, CAP). The ones that dumped (SLX, CHIP) had bigger airdrop overhang and TVL outflows.
- For OnRe, a "stablecoin narrative" discount is real, but the relevant comp set (RWA/real-yield: RE, CAP, HUMA, CHIP) has performed better than synthetic-dollar/basis names (RESOLV, ELX, USUAL, SLX) and chain tokens (XPL).
- Survivorship caveat: 2026 launches are only 3–6 months old, and ages differ across cohorts. Compare at equal horizons (d30/d90), not "now".

### Gaps
- No independent aggregate index of stablecoin-token performance was found; the statistics above are my own computations on the sample.
- The sample is not exhaustive (e.g. Apyx and Neutrl have not TGE'd; Level, Perena, Agora, Noble and Midas have no token).

## Q6. Which comps are closest to OnRe (Solana, RWA/reinsurance yield, similar TVL)?

### Takeaway
The closest comp is **Re Protocol (RE)**: same onchain-reinsurance thesis, $258M TVL at TGE versus OnRe's ~$295M now, a 10-month points season, a 7% S1, a $436M day-1 FDV and $479M now. Next come the Solana yield-dollar launches **Solstice (SLX)** (Exponent integration, $401M TVL, 8.5% S1, $207M → $66M FDV) and **Unitas (UP)**, then RWA-yield **Huma (HUMA; Solana)**, **Cap (CAP)**, **USD.AI (CHIP)** and **OpenEden (EDEN)**.

### Cited Findings
- OnRe: ONyc TVL $294.8M on 2026-09-29 (peak $309.5M on 2026-09-11; $16.2M on 2025-07-14) — [DefiLlama OnRe](https://api.llama.fi/protocol/onre); ONyc on CoinGecko as "OnRe Tokenized Reinsurance" (id onyc) — [CoinGecko](https://www.coingecko.com/en/coins/onyc); OnRe points since 2025-09-11 with a 4x yield-trading multiplier — [OnRe blog](https://www.onre.finance/blog/onre-introduces-points-program-rewarding-onyc-participation-across-defi); Exponent TVL $80M (peak $136M on 2026-08-19) — [DefiLlama Exponent](https://api.llama.fi/protocol/exponent)
- Re: reinsurance marketplace; $409M premiums written since inception, 30+ insurance partners — [Today in DeFi](https://news.todayindefi.com/p/airdrop-alpha-re-protocol-announced); RE TGE 2026-06-18, day-1 close $0.436 ($436M FDV), ATH $1.08 on 06-20, now $0.479 ($479M FDV, $76.5M mcap on 159.6M circulating); TVL $258M → $390M (Q1 sources); Binance spot + KuCoin + MEXC listings — [TradingView](https://www.tradingview.com/news/coinmarketcal:5429a86fc094b:0-re-binance-listing-18-june-2026/)
- Solstice: Solana; Flares partner protocols Orca, Raydium, Kamino, Exponent, including an "Exponent Loyalty" cohort for the eUSX market — [Solstice S1 docs](https://docs.solstice.finance/solstice-for-users/flares/season-1.md); USX $401M at TGE → $215M
- Unitas: Solana + BNB synthetic dollar (Jupiter Perps hedging); $81M TVL at TGE — [Solana Compass](https://solanacompass.com/projects/unitas)
- Huma: Solana PayFi/RWA credit; TVL now $382M; $669M day-1 FDV → $290M
- Cap: covered-credit cUSD backed by USDC/PYUSD/BUIDL/BENJI; $221M TVL at TGE — [search summary/The Defiant](https://thedefiant.io/news/defi/cap-labs-cap-token-auction-106m-fdv-oversubscription)
- USD.AI: GPU-backed credit yield dollar, "$225M in loans, $1.2B approved facilities" — [USD.AI](https://usd.ai/insights/chip-is-live)

### Inferences
- A comp-anchored OnRe range: Re (FDV/TVL 1.2–1.7x) implies ~$350–500M on $295M TVL. The Solana yield-dollar comps (SLX 0.3–0.5x, UP 0.7x at TGE) imply ~$90–220M. The RWA-credit comps (CAP 1.3–2.0x, CHIP 2.0–2.2x, HUMA ~0.8x now) imply ~$230–650M. The Re comp is the most directly analogous but launched with a Binance spot listing. Whether OnRe secures Binance spot or only Alpha/Wallet will likely shift where in the range it lands: Alpha-only launches (SLX, DAM, UP) had the lowest launch FDVs.
- OnRe's ~12.6-month points program and $53.4B TVL-days are larger than Re's S1 (~$50B TVL-days, est.), so at a similar % allocation, per-$ rewards would be similar or somewhat lower unless OnRe's FDV exceeds Re's.

### Gaps
- No other tokenized-reinsurance protocol with a live token was found beyond Re (e.g. no Nexus-style reinsurance yield-token launches in 2025–26 in the searches).
- Perena (Solana stable-swap/USD*) has no TGE, so it cannot be used as a valuation comp.
