# Perp DEX tokens that TGE'd Jan 1 – Oct 27, 2026: FDV at TGE vs highest FDV after TGE

Notes compiled 2026-10-27. Price data comes from the CoinGecko public API (one `/coins/markets` snapshot pulled on 2026-10-27 that holds ATH, ATL, supply and current price) and from the DefiLlama coins API (first recorded price, daily points near 00:00 UTC, and hourly points for the first 9 days). Raw files are in `/tmp/claude-0/-home-user-test-claude/2ad751b0-58d6-5348-a96a-1b74151bb386/scratchpad/cohortC2_raw/` and scripts in `/tmp/claude-0/-home-user-test-claude/2ad751b0-58d6-5348-a96a-1b74151bb386/scratchpad/cohortC2_scripts/`.

Conventions used throughout:
- "First trade" means the first price DefiLlama/CoinGecko recorded. It may come from a thin first venue. Where a news or exchange source gives an opening print, both are shown.
- "Day-1 close" means the DefiLlama price at about 23:59 UTC on the TGE day.
- "Peak FDV" means CoinGecko intraday ATH × supply. "Best daily close" is the highest DefiLlama daily point.
- Supply basis is CoinGecko max supply (1B unless stated) unless noted.
- Main citation URLs:
  - CG snapshot = https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=edgex,paradex,backpack,grvt,roll-2,based-one,genius-3,infinex-2,rails,ranger,tread-fi,bullbit,flying-tulip,gtr-trade,leverup,lighter,hyperliquid (retrieved 2026-10-27)
  - DL-first = https://coins.llama.fi/prices/first/coingecko:{id}
  - DL-daily and DL-hourly = the per-token chart URLs given in each fact sheet

## Q1. Which perp DEX tokens TGE'd between Jan 1 and Oct 27, 2026? (discovery)

### Takeaway
After screening the CoinGecko Perpetuals/Derivatives categories, the DefiLlama Derivatives registry and news, only 5 tokens qualify as core perp-DEX TGEs in the window:
- RollX ROLL (Jan 16)
- Paradex DIME (Mar 5)
- edgeX EDGE (Mar 31)
- Bullbit BUBI (Jun 23)
- GRVT (Jul 30)

Nine borderline tokens also TGE'd in the window: perp aggregators or terminals, Hyperliquid front-ends, a CEX, a hybrid exchange, and multi-product DeFi. About 20 pump-style micro-caps tagged "Perpetuals" also launched. Most well-known names (Variational, Pacifica, Extended, Ostium, Hibachi, Ethereal, Reya, Nado, Decibel and others) had still not launched a token by Oct 27, 2026. StandX cancelled its TGE.

### Cited Findings
**Discovery method.**
- The CoinGecko "Perpetuals" (`decentralized-perpetuals`), "Derivatives" (`decentralized-derivatives`), "Options", Hyperliquid, Monad and MegaETH category lists were pulled (447 unique coins) and cross-checked against DefiLlama first-price timestamps — [CG category list](https://api.coingecko.com/api/v3/coins/categories/list); [CG Perpetuals markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=decentralized-perpetuals&per_page=250&page=1); [CG Derivatives markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=decentralized-derivatives&per_page=250&page=1); [DL-first batch](https://coins.llama.fi/prices/first/coingecko:edgex)
- The DefiLlama protocol registry (8,844 protocols, 540 in Derivatives/Options) was checked for `gecko_id` (token) status. In the Derivatives category, only LeverUp (LV), RollX (ROLL) and Vooi have a token first priced after Dec 1, 2025 — [DefiLlama protocols API](https://api.llama.fi/protocols)

**Core perp DEX TGEs in the window (verified):**
- **RollX (ROLL)** — Base perp DEX. TGE/airdrop on Jan 16, 2026 "at 19:00" (timezone not stated; the first DefiLlama print is 11:40 UTC) — [Phemex](https://phemex.com/news/article/rollx-launches-token-roll-and-airdrop-on-base-network-53995); [DL-first](https://coins.llama.fi/prices/first/coingecko:roll-2)
- **Paradex (DIME)** — Starknet-based perp appchain. Trading started Mar 5, 2026 at 14:00 UTC, initially only on Paradex — [Coin Academy](https://coinacademy.fr/actu/paradex-airdrop-tge-dime-revenus-buyback/); first DL print 2026-03-05 16:32 UTC — [DL-first](https://coins.llama.fi/prices/first/coingecko:paradex)
- **edgeX (EDGE)** — Amber Group-backed perp DEX, moving to "EDGE Chain" (Ethereum L2). TGE/listing on Mar 31, 2026 at 20:30 Beijing time (12:30 UTC) — [The Defiant](https://thedefiant.io/news/defi/amber-group-backed-perp-dex-edgex-to-launch-token-on-march-31); [MEXC News](https://www.mexc.com/news/975187)
- **Bullbit (BUBI)** — Base perp DEX. TGE on Jun 23, 2026 with BingX spot listing — [Cointelegraph PR](https://cointelegraph.com/press-releases/bullbit-launches-bubi-building-toward-a-comprehensive-ecosystem); [BingX notice](https://bingx.com/en/support/articles/16561414962575). CoinGecko/DefiLlama price history only starts 2026-09-12 — [DL-first](https://coins.llama.fi/prices/first/coingecko:bullbit)
- **GRVT (GRVT)** — hybrid DEX on a ZKsync-powered app-chain. TGE and airdrop claims on Jul 30, 2026 — [KuCoin News](https://www.kucoin.com/news/flash/grvt-announces-tge-details-grvt-airdrop-claims-open-on-july-30); [The Block](https://www.theblock.co/post/393389/)

**Borderline TGEs in the window (labelled "borderline"):**
- **Ranger (RNGR)**, Jan 10 — Solana perp aggregator, MetaDAO ICO — [Phemex](https://phemex.com/news/article/ranger-finance-to-liquidate-return-504m-usdc-to-token-holders-65724)
- **Infinex (INX)**, Jan 30 — multi-chain trading app; DefiLlama lists "Infinex Perp" as an Interface — [The Block](https://www.theblock.co/post/380545/kain-warwicks-infinex-builds-on-67-7m-patron-nft-round-with-sonar-sale-ahead-of-inxs-2026-tge); [DL-first](https://coins.llama.fi/prices/first/coingecko:infinex-2)
- **Rails (RAILS)**, Feb 4, on Kraken — regulated perps-only hybrid exchange — [Bitrue](https://www.bitrue.com/blog/rails-tge-4-february-kraken-listing-buy-rails-token); [Yahoo/Fortune](https://finance.yahoo.com/news/rails-launches-perps-only-crypto-130000563.html)
- **Flying Tulip (FT)**, Feb 23 — Andre Cronje's multi-product DeFi; perps are one module — [The Defiant](https://thedefiant.io/news/markets/andre-cronje-flying-tulip-token-trades-near-usd1b-fdv-floor)
- **Backpack (BP)**, Mar 23 — DefiLlama classifies it as a CEX with perps, not a DEX — [KuCoin News](https://www.kucoin.com/news/flash/backpack-to-launch-bp-token-tge-on-march-23-2026); [DefiLlama protocols API](https://api.llama.fi/protocols)
- **Based (BASED)**, first print Mar 30 — Hyperliquid front-end ("BasedApp Perps" is an Interface on DefiLlama) — [DL-first](https://coins.llama.fi/prices/first/coingecko:based-one)
- **Genius (GENIUS)**, Apr 13 — YZi Labs-backed multi-chain trading terminal (spot and perps) on BNB Chain — [HackerNoon](https://hackernoon.com/genius-terminal-lists-on-cmc-launch-ahead-of-april-13th-$genius-tge)
- **GTR.trade (GTR)**, Jul 25 — micro-cap Hyperliquid perps interface — [DL-first](https://coins.llama.fi/prices/first/coingecko:gtr-trade)
- **Tread.fi (TREAD)**, Sep 16 13:00 UTC — trading terminal and Hyperliquid builder — [MEXC News](https://www.mexc.com/news/1206573)

**Out of window (TGE in 2025, note only):**
- Lighter (LIT): Dec 30, 2025 — [bex.co](https://bex.co/blog/2026/04/28/perp-dex-cohort-2026-lighter-airdrop-hyperliquid-long-tail); [DL-first](https://coins.llama.fi/prices/first/coingecko:lighter)
- LeverUp (LV, Monad): CAKE.PAD IDO Dec 17–18, 2025 at $0.01 — [EGW News](https://egw.news/crypto/news/31130/pancakeswap-announces-new-ido-on-cakepad-kaDYXzNT4); CMC lists an ATL on Dec 18, 2025, so trading began in 2025 — [CMC](https://coinmarketcap.com/currencies/leverup/). CoinGecko's first price is only 2026-03-26 — [DL-first](https://coins.llama.fi/prices/first/coingecko:leverup)
- Vooi (perp aggregator): Dec 18, 2025 — [CG Perpetuals markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=decentralized-perpetuals&per_page=250&page=1)
- Kinetiq (KNTQ): first price Nov 27, 2025 — [DL-first](https://coins.llama.fi/prices/first/coingecko:kinetiq)
- Aster: Sep 17, 2025 ATL date — [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=aster-2)
- Avantis: TGE Sep 15, 2025 — [airdropalert](https://airdropalert.com/blogs/edgex-review/)

**In a CG derivatives category but not a perp DEX (excluded):**
- ETHGas (GWEI): blockspace/gas derivatives, first price Jan 21, 2026 — [DL-first](https://coins.llama.fi/prices/first/coingecko:ethgas-2)
- Ascend (ASCEND): DefiLlama lists Ascend as liquid staking on 0G — [DefiLlama protocols API](https://api.llama.fi/protocols)

**Micro-caps tagged "Perpetuals/Derivatives/Options" on CoinGecko and launched in 2026** (FDV mostly under $50K now; probably pump-style launches, identity unverified): TROVE, LIQUID, AMARA, PERK, PUMPPERPS, FFX, CRACKROCK, ALT, PARQ, NEXUS, PERPAD, SKEW, YARROW, HPERP, PERPEX, TALIS, EMPIREX, LABS, BYNOMO, K9, THRONE — [CG Perpetuals markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=decentralized-perpetuals&per_page=250&page=1); [CG Derivatives markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=decentralized-derivatives&per_page=250&page=1)

**Third-party cohort view.** A May 23, 2026 recap (data credited to CryptoRank and Wu Blockchain) counted seven perp-DEX tokens launched Sep 2025–Mar 2026 and said only ASTER (+269%) and EDGE (+114%) gained. The others fell: BASED −32%, ROLL −34%, BP −41%, LIT −48%, DIME −55% — [HOKANEWS](https://www.hokanews.com/2026/05/7-perp-dex-tokens-launched-only-2.html)

**Chain coverage:**
- Monad: LeverUp TGE'd in Dec 2025. Perpl and Kuru have no token — [DefiLlama protocols API](https://api.llama.fi/protocols)
- Aptos: Decibel (TVL $29.3M) has no token — [DefiLlama protocols API](https://api.llama.fi/protocols)
- Sui: DipCoin Perps, ZO Perps and Aftermath Perps have no token — [DefiLlama protocols API](https://api.llama.fi/protocols)
- Sei: Citrex has no token — [DefiLlama protocols API](https://api.llama.fi/protocols)
- MegaETH: no perp DEX token found in the CG MegaETH category (15 coins) — [CG MegaETH markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=megaeth-ecosystem&per_page=250&page=1)
- Solana: Ranger (borderline) and Backpack (CEX). Pacifica, BULK, Phoenix Perp and Bullet have no token — [DefiLlama protocols API](https://api.llama.fi/protocols)
- Base: RollX and Bullbit — [DefiLlama protocols API](https://api.llama.fi/protocols)
- BNB Chain: Genius (borderline) — [HackerNoon](https://hackernoon.com/genius-terminal-lists-on-cmc-launch-ahead-of-april-13th-$genius-tge)
- Hyperliquid HIP-3 deployers (tradeXYZ, Ventuals, Felix Perps, HYENA) have no token. Only front-end tokens launched (BASED, TREAD, GTR) — [DefiLlama protocols API](https://api.llama.fi/protocols)

### Inferences
- The truly comparable 2026 perp-DEX cohort is tiny: 4 core tokens with usable TGE price data (ROLL, DIME, EDGE, GRVT), plus BUBI without TGE-day data. Statistics in Q3 therefore also use a wider 13-token set that includes borderline names. Any conclusion is low-confidence.
- 2026 was largely a "pre-token" year for the big names. Several high-profile perp DEXs pushed TGEs into Q4 2026 or later, or cancelled them. That limits what the 2026 cohort can say.

### Gaps
- CryptoRank TGE calendars and Binance Alpha/HODLer announcement archives were not fetched directly. Discovery relied on CoinGecko/DefiLlama registries plus news, so a perp DEX token that neither registry tags, and that got no news coverage, could be missing.
- The identity and product of the micro-caps K9 and THRONE were not verified.
- Tread.fi, Genius and Based are classified as borderline from DefiLlama "Interface" categories and project descriptions. No independent architecture review was done.

## Q2. Per-token fact sheets

### Takeaway
Across the 13 tokens with usable data:
- TGE FDVs ran from about $2M (GTR) and $19M (RNGR) to about $657M (EDGE). FT is about $1B on its 10B max-supply basis.
- Peak/TGE multiples on the day-1-close basis ranged from 1.06x (RNGR) to 7.38x (BP).
- Seven of 13 set their ATH within 7 days of TGE. Late peaks (BP, DIME, FT, TREAD, EDGE) came mostly in May (EDGE) or Sep–Oct 2026.
- Today 10 of 13 trade below their day-1 close.

### Cited Findings

#### Summary table (prices in USD; FDV = price × supply basis; x = Peak FDV / TGE FDV)

| Token (class) | TGE date / days since | Supply basis | First trade → FDV | Day-1 close → FDV | Pre-market / sale | ATH (date, day #) → Peak FDV | Peak x (first / d1) | ATH ≤7d? | Best daily close after d7 ÷ d1 close | ATL (date) | Current px → FDV; cur/d1 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ROLL (core) | 2026-01-16 / 284 | 1B (CG); Phemex says 180M | $0.07846 → $78.5M | $0.08048 → $80.5M | none found | $0.18368 (01-19, d3) → $183.7M | 2.34x / 2.28x | Y | 1.91x (07-20) | $0.0211 (05-16) | $0.0624 → $62.4M; 0.78x |
| DIME (core) | 2026-03-05 / 236 | 1B | $0.07219 → $72.2M (thin print); next update $0.0446 (03-06) → $44.6M | DL day-1 point = same $0.07219 print | none found | $0.10226 (10-11, d220) → $102.3M | 1.42x (vs $0.072) / 2.29x (vs $0.0446) | N | 0.95x vs $0.072 (1.54x vs $0.0446), 10-10 | $0.0076 (06-28) | $0.0456 → $45.6M; 0.63x vs $0.072 |
| EDGE (core) | 2026-03-31 / 210 | 1B | $0.6965 (first post-TGE hourly, 14:00 UTC) → $696.5M; pre-TGE DL prints $0.51–0.53 | $0.6567 → $656.7M | Binance pre-market ~$0.70 (~$700M) | $1.54 (05-22, d52) → $1.54B | 2.21x / 2.35x | N | 2.30x (05-21) | $0.2375 (07-05) | $0.3334 → $333.4M; 0.51x |
| GRVT (core) | 2026-07-30 / 89 | 1B | $0.3833 → $383.3M | $0.2444 → $244.4M | pre-market valuation ">$320M"; Polymarket ~$200M | $0.45446 (07-30, d0) → $454.5M | 1.19x / 1.86x | Y | 1.35x (08-11) | $0.1457 (09-02) | $0.2159 → $215.9M; 0.88x |
| BUBI (core) | 2026-06-23 (BingX) / 126 | 4B | not available (CG data from 09-12: $0.04848 → $193.9M) | n/a | none found | $0.05147 (09-14) → $205.9M (since CG listing) | n/a | n/a | n/a | $0.0221 (10-27) | $0.0224 → $89.6M |
| RNGR (borderline) | 2026-01-10 / 290 | 25.625M max | $0.7336 → $18.8M | $0.7588 → $19.4M | MetaDAO ICO $0.60 (~$15.4M) | $0.80496 (01-10, d0) → $20.6M | 1.10x / 1.06x | Y | 1.01x (03-06) | ~$1e-8 (08-05) | ~$0 (wound down) |
| INX (borderline) | 2026-01-30 / 270 | 10B | $0.02153 → $215.3M | $0.02145 → $214.5M | Sonar sale $99.99M FDV; Bybit pre-market $0.031–0.032 | $0.03339 (01-30, d0) → $333.9M | 1.55x / 1.56x | Y | 0.92x (04-13) | $0.00387 (10-18) | $0.00483 → $48.3M; 0.23x |
| RAILS (borderline) | 2026-02-04 / 265 | 65M | $0.2326 → $15.1M | $0.4200 → $27.3M | none found | $1.091 (02-04, d0; wick) → $70.9M | 4.69x / 2.60x | Y | 0.83x (02-28) | $0.0202 (09-03) | $0.0253 → $1.6M; 0.06x |
| FT (borderline) | 2026-02-23 / 246 | 10B (sale docs); CG 516.9M | sale/opening ~$0.10 → ~$1.0B (DL first print $0.2998 looks anomalous) | $0.1004 → $1.004B ($51.9M on CG supply) | CoinList $0.10 (FDV $1B) | $0.16869 (10-12, d231) → $1.69B ($87.2M CG) | 1.69x / 1.68x | N | 1.62x (10-12) | $0.0670 (04-22) | $0.1261 → $1.26B ($65.2M CG); 1.26x |
| BP (borderline, CEX) | 2026-03-23 / 218 | 1B | $0.2747 → $274.7M (Yellow: debut $0.31) | $0.2236 → $223.6M | Polymarket 58% for >$300M on launch day | $1.65 (10-01, d192) → $1.65B | 6.01x / 7.38x | N | 6.04x (09-28) | $0.1179 (05-25) | $0.9562 → $956.2M; 4.28x |
| BASED (borderline) | 2026-03-30 / 211 | 1B | $0.1456 → $145.6M | $0.1187 → $118.7M | none found | $0.32159 (04-16, d17; wick) → $321.6M | 2.21x / 2.71x | N | 1.39x (04-16) | $0.0414 (10-14) | $0.0527 → $52.7M; 0.44x |
| GENIUS (borderline) | 2026-04-13 / 197 | 1B max (CG total 895M) | $0.1965 → $196.5M (thin; $0.58 within ~2h) | $0.5320 → $532.0M | none found | $0.95329 (04-18, d5) → $953.3M | 4.85x / 1.79x | Y | 1.36x (05-24) | $0.2715 (10-15) | $0.3084 → $308.4M; 0.58x |
| GTR (borderline micro) | 2026-07-25 / 94 | 1B | $0.002612 → $2.6M | $0.001907 → $1.9M | none found | $0.003587 (07-25, d0) → $3.6M | 1.37x / 1.88x | Y | 1.02x | $0.000178 (10-27) | $0.000182 → $0.18M; 0.10x |
| TREAD (borderline) | 2026-09-16 / 41 | 100M | $0.4739 → $47.4M | $0.3902 → $39.0M | none found | $1.36 (09-27, d11) → $136.0M | 2.87x / 3.49x | N | 3.08x (10-03) | $0.3265 (09-16) | $0.7686 → $76.9M; 1.97x |

- Table sources:
  - ATH, ATL, supply, circulating supply and current prices: [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=edgex,paradex,backpack,grvt,roll-2,based-one,genius-3,infinex-2,rails,ranger,tread-fi,bullbit,flying-tulip,gtr-trade,leverup,lighter,hyperliquid)
  - First trade, day-1 close and best daily closes: DefiLlama per-token URLs in the fact sheets below
  - Pre-market and sale figures: sources in each fact sheet

#### Core: RollX (ROLL), Base perp DEX
- RollX describes itself as a Base perp DEX with spot and perps and up to 1000x leverage — [CMC AI](https://coinmarketcap.com/cmc-ai/rollx/what-is); [Phemex](https://phemex.com/news/article/rollx-launches-token-roll-and-airdrop-on-base-network-53995)
- TGE and genesis airdrop: Jan 16, 2026, 19:00 (timezone not given). 25% unlocked at TGE and 75% linearly over 6 months. Eligibility: Trade & LP points users plus Galxe and Binance Wallet campaigns. First-batch claim deadline Jan 26 — [Phemex](https://phemex.com/news/article/rollx-launches-token-roll-and-airdrop-on-base-network-53995)
- A Binance Alpha ROLL airdrop event cost 15 Alpha points per claim — [ChainCatcher](https://www.chaincatcher.com/en/article/2237972)
- Supply conflict: Phemex says "total supply of 180 million tokens", while CoinGecko lists total and max supply of 1B with 155M circulating now — [Phemex](https://phemex.com/news/article/rollx-launches-token-roll-and-airdrop-on-base-network-53995); [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=roll-2). On a 180M basis, TGE FDV would be about $14M.
- Prices — [DL-first](https://coins.llama.fi/prices/first/coingecko:roll-2); [DL-daily](https://coins.llama.fi/chart/coingecko:roll-2?start=1768608000&span=287&period=1d&searchWidth=14400); [DL-hourly](https://coins.llama.fi/chart/coingecko:roll-2?start=1768563616&span=216&period=1h&searchWidth=1800); [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=roll-2):
  - First $0.07846 at 11:40 UTC Jan 16; day-1 close $0.08048
  - Daily closes rose to $0.1698 on Jan 19; CG ATH $0.18368 on Jan 19 (day 3)
  - Bottomed at $0.0211 on May 16, then rallied to a $0.1539 daily close on Jul 20 (1.91x day-1 close)
  - Now $0.0624 (FDV $62.4M, MC $9.7M)
- Initial circulating supply is not documented beyond "25% unlock at TGE" of the airdrop pool.

#### Core: Paradex (DIME), Starknet perp appchain
- Airdrop: 25% of fully diluted supply to XP holders at TGE, fully unlocked (20% Season 2 + 5% Pre-Season/Season 1). 80% of the team allocation unlocks on performance milestones over 4 years — [Decrypt](https://decrypt.co/356482/paradex-confirms-dime-tge-timeline-and-expands-airdrop-allocation-following-xp-season-2-conclusion?amp=1)
- Timing and venue: TGE Mar 5, 2026. Claims opened 07:00 UTC, trading started 14:00 UTC, initially only on Paradex. Revenue funds buybacks — [Coin Academy](https://coinacademy.fr/actu/paradex-airdrop-tge-dime-revenus-buyback/)
- Later the main active market was on Hyperliquid (DropsTab, undated) — [DropsTab](https://dropstab.com/coins/paradex)
- TGE pricing is ambiguous:
  - DefiLlama/CoinGecko first print was $0.07219 (16:32 UTC) and stayed flat until the next update of $0.04461 at 13:00 UTC Mar 6 — [DL-hourly](https://coins.llama.fi/chart/coingecko:paradex?start=1772728331&span=216&period=1h&searchWidth=1800)
  - Daily points: $0.0453 on Mar 9 and $0.0260 on Mar 26 — [DL-daily](https://coins.llama.fi/chart/coingecko:paradex?start=1772755200&span=239&period=1d&searchWidth=14400)
  - A Mar 8 PANews item, citing CoinGecko, put FDV at only about $43M and said DIME was not yet on major exchanges — reported via [MEXC News](https://www.mexc.com/news/878738) (attribution of the republished page not fully verified)
  - CMC never recorded the $0.072 print; its ATH is $0.04401 on Mar 10 and ATL $0.007515 on Jun 26 — [CMC](https://coinmarketcap.com/currencies/paradex/)
  - DefiLlama's token page lists ATH $0.072 (Mar 5) and ATL $0.0076 (Jun 28) — [DefiLlama token page](https://defillama.com/token/dime)
- July snapshot: $0.0108, FDV $11.0M (MEXC tokenomics page dated Jul 22, 2026) — [MEXC](https://www.mexc.com/price/paradex/tokenomics)
- October rally: CoinGecko's current ATH is $0.102264 on 2026-10-11 (about 13x off the June low). Price is now $0.0456 (FDV $45.6M, MC $8.3M, circulating 181M per CG) — [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=paradex)
- Initial circulating MC: about $18.0M (250M × $0.07219), or about $11.2M on the $0.0446 basis — derived from [Decrypt](https://decrypt.co/356482/paradex-confirms-dime-tge-timeline-and-expands-airdrop-allocation-following-xp-season-2-conclusion?amp=1) and [DL-hourly](https://coins.llama.fi/chart/coingecko:paradex?start=1772728331&span=216&period=1h&searchWidth=1800)
- Messari covered the DIME TGE (report not read in full) — [Messari](https://messari.io/report/paradex-privacy-first-perp-dex-and-the-dime-tge)

#### Core: edgeX (EDGE)
- Supply and allocation: 1B fixed supply. 25% airdropped at TGE plus up to 5% for Pre-TGE Season participants; the remaining 70% goes to Ecosystem & Community, Core Contributors and Foundation. The TGE coincided with a move to "EDGE Chain", an Ethereum L2 — [crypto.news](https://crypto.news/edgex-set-to-launch-edge-token-amid-transparency-concerns/); [The Defiant](https://thedefiant.io/news/defi/amber-group-backed-perp-dex-edgex-to-launch-token-on-march-31)
- 25% went to the community fully unlocked — [airdropalert](https://airdropalert.com/blogs/edgex-review/)
- Pre-market:
  - Binance pre-market spot and airdrop claims opened Mar 19. Binance Futures listed EDGEUSDT pre-market perps at up to 5x — [The Defiant](https://thedefiant.io/news/defi/amber-group-backed-perp-dex-edgex-to-launch-token-on-march-31); [crypto.news](https://crypto.news/edgex-set-to-launch-edge-token-amid-transparency-concerns/)
  - Pre-market price about $0.70, implying about $700M FDV — [crypto.news](https://crypto.news/edgex-set-to-launch-edge-token-amid-transparency-concerns/)
  - DefiLlama prints before the 12:30 UTC TGE were $0.5255 (08:05 UTC), $0.5126 and $0.5132. The source is probably a pre-market feed — [DL-hourly](https://coins.llama.fi/chart/coingecko:edgex?start=1774944306&span=216&period=1h&searchWidth=1800)
- Early trading:
  - First post-TGE hourly point $0.6965 (14:00 UTC); day-1 close $0.6567 (FDV $656.7M, matching HOKANEWS' "approximately $656 million" starting FDV) — [DL-hourly](https://coins.llama.fi/chart/coingecko:edgex?start=1774944306&span=216&period=1h&searchWidth=1800); [HOKANEWS](https://www.hokanews.com/2026/05/7-perp-dex-tokens-launched-only-2.html)
  - Apr 3 spike: hourly high $1.161 — [DL-hourly](https://coins.llama.fi/chart/coingecko:edgex?start=1774944306&span=216&period=1h&searchWidth=1800). MEXC reported a +49.4% day to about $1.07 (FDV about $1.07B) — [MEXC News](https://www.mexc.com/news/1003367)
- Airdrop controversy: on-chain monitors alleged the team kept most of a "$195M" airdrop; the team then bought back and burned more than $2M — [AMBCrypto](https://ambcrypto.com/195m-edgex-airdrop-under-fire-what-it-means-for-edge-prices/)
- Peak: ATH $1.54 on May 22, 2026 (day 52), Peak FDV $1.54B — [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=edgex)
  - Odaily reported EDGE broke $1.52 on May 22, "approximately 300%" above its TGE opening price. Drivers it cited: the edgeX V2 upgrade, TradFi-segment volume, buybacks, and new OKX and Kraken listings — [Odaily](https://www.odaily.news/en/newsflash/483270)
  - HOKANEWS put the peak FDV at about $1.4B as of its May 23 write-up — [HOKANEWS](https://www.hokanews.com/2026/05/7-perp-dex-tokens-launched-only-2.html)
- Best daily close $1.513 on May 21 (2.30x day-1 close) — [DL-daily](https://coins.llama.fi/chart/coingecko:edgex?start=1775001600&span=213&period=1d&searchWidth=14400)
- Later: ATL $0.2375 on Jul 5. Now $0.3334 (FDV $333.4M, MC $116.7M, circulating 350M) — [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=edgex)
- Initial circulating MC: about $164M (250M × $0.6567), or about $197M if the extra 5% was included — derived from [crypto.news](https://crypto.news/edgex-set-to-launch-edge-token-amid-transparency-concerns/) and [DL-daily](https://coins.llama.fi/chart/coingecko:edgex?start=1775001600&span=213&period=1d&searchWidth=14400)

#### Core: GRVT
- Tokenomics: 1B fixed supply. Community/airdrop share raised to 28% from 22% (Season 2 portion up to 18% from 12%). GRVT raised a $19M Series A in late 2025. The token first trades on GRVT's own spot market, with tier-one CEX listings sought — [The Block (Mar 12, 2026)](https://www.theblock.co/post/393389/)
- TGE Jul 30, 2026. 280M tokens distributed in batches over 12 months — [KuCoin News](https://www.kucoin.com/news/flash/grvt-announces-tge-details-grvt-airdrop-claims-open-on-july-30)
- Initial circulating supply 114.31M (11.4%) — [azat.tv](https://azat.tv/en/grvt-token-launch-exchanges-price-prediction-tokenomics/). CG shows 114.3M circulating now — [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=grvt)
- Pre-market and venues: a Jul 31 CMC post cites a pre-market valuation above $320M, a Polymarket estimate of about $200M, and Coinbase adding GRVT to its asset roadmap — [CMC (es)](https://coinmarketcap.com/es/cmc-ai/grvt/latest-updates/)
  - CMC AI on Jul 31: +80.59% to $0.271 in 24h on Bitget and MEXC listings — [CMC AI](https://coinmarketcap.com/cmc-ai/grvt/price-analysis/)
  - Coinbase shows an ATH of €0.2745 on Aug 1 on its own data — [Coinbase](https://www.coinbase.com/en-pt/price/grvt-eth)
- Prices — [DL-hourly](https://coins.llama.fi/chart/coingecko:grvt?start=1785413878&span=216&period=1h&searchWidth=1800); [DL-daily](https://coins.llama.fi/chart/coingecko:grvt?start=1785456000&span=92&period=1d&searchWidth=14400); [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=grvt):
  - First print $0.3833 at 12:17 UTC; $0.2291 by 16:00 UTC; day-1 close $0.2444
  - CG ATH $0.454464 on Jul 30 (opening minutes)
  - Daily closes climbed to $0.3290 on Aug 11 (1.35x day-1 close); ATL $0.1457 on Sep 2
  - Now $0.2159 (FDV $215.9M, MC $24.7M)
- Initial circulating MC: about $27.9M on the day-1-close basis ($43.8M on the first print) — derived from [azat.tv](https://azat.tv/en/grvt-token-launch-exchanges-price-prediction-tokenomics/) and [DL-hourly](https://coins.llama.fi/chart/coingecko:grvt?start=1785413878&span=216&period=1h&searchWidth=1800)

#### Core: Bullbit (BUBI), Base perp DEX
- TGE Jun 23, 2026. 4B max supply, ERC-20 on Base. 300M (7.5%) circulating at TGE. Allocation: 55% ecosystem and airdrop, 13% team, 32% staking/treasury/liquidity/advisors. Airdrop claims opened 3 hours after TGE for Genesis Points holders — [Cointelegraph PR](https://cointelegraph.com/press-releases/bullbit-launches-bubi-building-toward-a-comprehensive-ecosystem)
- BingX listed BUBI/USDT on Jun 23 — [BingX](https://bingx.com/en/support/articles/16561414962575)
- No Binance Alpha listing was found — [CoinStats](https://coinstats.app/news/8b3c4e3aa45423b25b937e6a2a4b705c87046dfd5eb6ffe5069be9c24bbfda6f_Binance-Alpha-Launches-BUBB-and-AGON-Tokens-in-Latest-PreListing-Showcase)
- CoinGecko price history starts Sep 12, 2026 at $0.04848 (FDV $193.9M). ATH since then $0.051473 on Sep 14. Now $0.0224 (FDV $89.6M, MC $9.3M) — [DL-first](https://coins.llama.fi/prices/first/coingecko:bullbit); [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bullbit)

#### Borderline fact sheets (condensed)

**Ranger (RNGR), Solana perp aggregator**
- MetaDAO ICO at $0.60, with 10M RNGR in the round (about 39% of supply). TGE Jan 10, 2026 — [Blockworks](https://blockworks.co/news/rangers-ico-metadao); [0xResearch](https://blockworks-research.beehiiv.com/p/ranger-s-ico) (ICO terms per search summaries of these pages)
- First trade $0.7336 (1.22x the ICO price); ATH $0.805 on day 0; daily closes never exceeded $0.767 — [DL-daily](https://coins.llama.fi/chart/coingecko:ranger?start=1768089600&span=293&period=1d&searchWidth=14400)
- Holders accused the team of misleading ICO metrics — [Crypto Times](https://www.cryptotimes.io/2026/03/03/rngr-token-holders-challenge-ranger-finance-over-misleading-claims/)
- In March 2026 holders voted to liquidate; about $5.04M USDC was returned — [Phemex](https://phemex.com/news/article/ranger-finance-to-liquidate-return-504m-usdc-to-token-holders-65724); [CoinStats](https://coinstats.app/news/b216cdd3c4b5c03db1eb4e7929b3b7d2b6fd3cf0e24d2367607f2f2248f624b8_Ranger-Finance-Winds-Down-After-Treasury-Vote-And-Drift-Shock)
- Price now about $1e-8 — [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ranger)

**Infinex (INX)**
- Sonar sale on Jan 3–6, 2026 of 5% of supply. FDV cut from $300M to $99.99M (about $0.0099 per token) — [Tapbit](https://www.tapbit.com/en/news/articles/infinex-founder-adjusts-inx-token-sonar-sale-valuation-down-to-99-99-million); [The Block](https://www.theblock.co/post/380545/kain-warwicks-infinex-builds-on-67-7m-patron-nft-round-with-sonar-sale-ahead-of-inxs-2026-tge)
- A Bybit pre-market contract traded at $0.031–0.032 (about $310–320M FDV). The early-unlock price was set at a $300M FDV, declining over a year — reported in search summaries of [ChainCatcher](https://www.chaincatcher.com/en/article/2232635) and [Tapbit](https://www.tapbit.com/en/news/articles/infinex-founder-adjusts-inx-token-sonar-sale-valuation-down-to-99-99-million) (exact page attribution not verified)
- First trade $0.02153 at 00:00 UTC Jan 30; ATH $0.0334 the same day; hourly max over the first 7 days only $0.0228 (so the ATH looks like a thin wick) — [DL-hourly](https://coins.llama.fi/chart/coingecko:infinex-2?start=1769731200&span=216&period=1h&searchWidth=1800)
- Now $0.00483 (FDV $48.3M), below the $99.99M sale FDV — [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=infinex-2)

**Rails (RAILS)**
- US perps-only exchange. $14M token warrants within $20M of funding. Registered with CIMA, NFA registration pending — [Yahoo/Fortune](https://finance.yahoo.com/news/rails-launches-perps-only-crypto-130000563.html); [CMCC](https://www.cmcc.vc/insights/rails-the-first-compliant)
- TGE Feb 4, 2026 on Kraken — [Bitrue](https://www.bitrue.com/blog/rails-tge-4-february-kraken-listing-buy-rails-token)
- 65M supply: 40% user rewards, 30% investors and team, 15.25% token sale, 14.76% foundation — [CoinGabbar](https://www.coingabbar.com/en/crypto-currency-news/rails-airdrop-phase-2-end-rails-listing-date-february-2026)
- First trade $0.2326; $0.397 within about an hour; CG ATH $1.091 the same day (the DefiLlama hourly max in the first week was only $0.4927, so it was a wick) — [DL-hourly](https://coins.llama.fi/chart/coingecko:rails?start=1770224319&span=216&period=1h&searchWidth=1800)
- Now $0.0253 (FDV $1.6M) — [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=rails)

**Flying Tulip (FT)**
- CoinList sale on Feb 3–6 at $0.10. 2B FT sold, equal to 20% of supply, implying a 10B max supply and $1B FDV. Buyers got an on-chain "perpetual put" (burn FT to redeem principal) — [KuCoin](https://www.kucoin.com/es/news/articles/andre-cronje-project-flying-tulip-ft-lands-on-coinlist-a-new-era-for-defi-investor-protection)
- $225.5M raised from institutions, including $75.5M at a $1B token valuation — [The Block](https://www.theblock.co/post/387720/andre-cronje-flying-tulip-additional-funding-token-crypto)
- Became transferable Feb 23; dipped to about $0.08 and then traded near $0.10 (~$1B FDV) — [The Defiant](https://thedefiant.io/news/markets/andre-cronje-flying-tulip-token-trades-near-usd1b-fdv-floor)
- CG supply is only 516.9M. Its ATH is $0.168686 on Oct 12 (day 231) and the price is now $0.126 — [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=flying-tulip)
- DefiLlama's first print of $0.2998 sits above CG's ATH, so it is treated as anomalous — [DL-first](https://coins.llama.fi/prices/first/coingecko:flying-tulip)

**Backpack (BP), CEX plus wallet**
- 1B supply. 25% (250M) airdropped on points; 75% held by the treasury; no team allocation at launch — [Datawallet](https://datawallet.beehiiv.com/p/backpack-exchange-launches-bp-token-with-25-airdrop)
- TGE Mar 23. Pre-launch Polymarket odds favoured an FDV above $100M with a lower chance above $200M — [KuCoin News](https://www.kucoin.com/news/flash/backpack-to-launch-bp-token-tge-on-march-23-2026)
- Polymarket showed 58% for more than $300M FDV on launch day — [CertiK Skynet](https://skynet.certik.com/projects/backpack)
- Opening: debuted at $0.31 and fell 25.8% within 24h. The article's "$3.1B FDV" is a decimal error for about $310M — [Yellow (pl)](https://yellow.com/pl/research/wewnątrz-startu-tokena-backpack-o-wartości-31-mld-usd-który-napędza-airdrop–metę-na-solanie)
- First DefiLlama print $0.2747; day-1 close $0.2236 — [DL-hourly](https://coins.llama.fi/chart/coingecko:backpack?start=1774270712&span=216&period=1h&searchWidth=1800)
- Rally: ATL $0.1179 on May 25, then ATH $1.65 on Oct 1 — [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=backpack)
  - The catalyst cited was an SEC "Innovation Exemption" on Sep 17 for limited on-chain trading of tokenized stocks. BP was below $0.50 in mid-September — [Crypto Briefing](https://cryptobriefing.com/backpack-bp-token-all-time-high-sec-exemption/)
  - BP was up 130.5% over 7 days to Sep 26, with MC at $323.3M — [CoinStats](https://coinstats.app/ai/a/latest-news-for-backpack.md)
- Now $0.956 (FDV $956M) — [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=backpack)

**Based (BASED), Hyperliquid front-end**
- XP and points convert to BASED at TGE, with an optional lock of up to 6 months for a boosted allocation — [CoinEx Academy](https://www.coinex.com/en/academy/detail/3490-based-based-airdrop-guide-free-token-how-to-participate)
- First print $0.1456 on Mar 30; day-1 close $0.1187; about $0.054 by Apr 9; a one-day spike to $0.1647 close on Apr 16 (CG intraday ATH $0.3216) — [DL-daily](https://coins.llama.fi/chart/coingecko:based-one?start=1774915200&span=214&period=1d&searchWidth=14400); [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=based-one)
- Now $0.0527 — [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=based-one)

**Genius (GENIUS)**
- Points-based allocation through CMC Launch; 1B max supply — [MEXC News](https://www.mexc.com/news/1032879)
- Spot on MEXC and perps on Aster. A press release said FDV "briefly tops $800M" — [ACN Newswire](https://www.acnnewswire.com/press-release/english/106551/genius-foundation's-genius-token-surges-following-tge,-briefly-tops-$800-million-fdv)
- About 335M (33.5%) circulating in late May — [Binance Research](https://www.binance.com/lo-LA/research/analysis/genius)
- First print $0.1965, then $0.58 within about 2 hours; day-1 close $0.532 — [DL-hourly](https://coins.llama.fi/chart/coingecko:genius-3?start=1776092471&span=216&period=1h&searchWidth=1800)
- ATH $0.953 on Apr 18; now $0.308 — [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=genius-3)

**Tread.fi (TREAD)**
- Genesis event Sep 16, 2026 at 13:00 UTC. Genesis distribution 15.2M TREAD (15.2% of 100M) — [MEXC News](https://www.mexc.com/news/1206573); [airdrops.io](https://airdrops.io/tread-fi/)
- Initial circulating MC at least about $5.9M (15.2M × $0.390) — derived from [MEXC News](https://www.mexc.com/news/1206573) and [DL-daily](https://coins.llama.fi/chart/coingecko:tread-fi?start=1789603200&span=44&period=1d&searchWidth=14400)
- ATH $1.36 on Sep 27 — [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=tread-fi)

**Out-of-window context**
- Lighter LIT: Dec 30, 2025. 25% airdrop. Opened above $3.30 and settled around $2.50 (FDV just over $2.5B) — [bex.co](https://bex.co/blog/2026/04/28/perp-dex-cohort-2026-lighter-airdrop-hyperliquid-long-tail)
  - CG ATH $7.86 (day 0), ATL $0.779 on Mar 31, 2026, now $3.02 — [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=lighter)
  - Best 2026 daily close $5.32 on Sep 24 — [DL-daily](https://coins.llama.fi/chart/coingecko:lighter?start=1767139200&span=304&period=1d&searchWidth=14400)
- LeverUp LV: $0.01 IDO ($10M FDV) — [EGW News](https://egw.news/crypto/news/31130/pancakeswap-announces-new-ido-on-cakepad-kaDYXzNT4)
  - CG ATH $0.0887 on Oct 2, 2026; now $0.054 — [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=leverup)
  - CMC instead shows an ATH of about $0.075 on May 10 — [CMC](https://coinmarketcap.com/currencies/leverup/)
- ETHGas (GWEI, excluded as not a perp DEX): first $0.02642 on Jan 21, 2026 (FDV $264M on 10B); ATH $0.2466 on Jun 29 (9.3x); now $0.0213 — [DL-first](https://coins.llama.fi/prices/first/coingecko:ethgas-2); [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethgas-2)

### Inferences
- **The choice of TGE price changes multiples a lot.** Several first prints are thin first-venue prints: DIME's single $0.072 print, GENIUS at $0.1965, FT at $0.30, RAILS at $0.23. Several CoinGecko ATHs are intraday wicks: RAILS $1.091, BASED $0.32, INX $0.033, GRVT's opening $0.454. Best-daily-close multiples are the more robust measure of a re-rating.
- **Pre-market was a decent guide.** EDGE pre-market (~$700M) was close to its day-1 FDV ($657M). GRVT's ">$320M" pre-market sat above its $244M day-1 close. INX's Bybit pre-market (~$310–320M) was above its realised ~$215M. BP's Polymarket odds ($300M) were near its $275M first print. Pre-market tended to sit at or above the day-1 close, not below.

### Gaps
- The exact opening print on the main venue is missing for ROLL (Binance Alpha/DEX), DIME (Paradex spot), GRVT (GRVT spot/Bitget/MEXC), BASED, GENIUS, TREAD and GTR. The DefiLlama/CoinGecko first-recorded price is used instead.
- BUBI has no price data from its Jun 23 BingX TGE until CoinGecko coverage began on Sep 12. Its TGE FDV and peak multiple are unknown.
- ROLL's total supply is disputed (1B per CoinGecko vs 180M per Phemex). I infer that the 180M figure probably describes the airdrop pool, but this is unverified.
- No catalyst was found for DIME's Oct 11 ATH or FT's Oct 12 ATH. BASED's TGE announcement and distribution percentage were not found.
- Last private-round valuations were not found for edgeX, Paradex, RollX, Bullbit, Based, Genius or Tread.fi. GRVT has only "$19M Series A, late 2025" with no valuation — [The Block](https://www.theblock.co/post/393389/)

## Q3. Within the cohort: how many exceeded TGE FDV after TGE, by how much, and does lower TGE FDV mean a higher peak multiple?

### Takeaway
On the intraday ATH:
- 13 of 13 analysable tokens exceeded their TGE FDV at some point after TGE.
- 11 of 13 reached at least 1.5x their day-1-close FDV, 6 of 13 at least 2x, and 1 of 13 (BP) at least 5x.

Much of that came from listing-week wicks, though:
- Seven of 13 made their ATH within 7 days.
- On best daily closes, only 5 of 13 reached 1.5x and 4 of 13 reached 2x.
- Four tokens (RNGR, INX, RAILS, GTR) spiked early and then went more or less straight down.

Lower TGE FDV showed no association with higher peak multiples (Spearman ρ ≈ 0.0–0.1 on ATH multiples, +0.42 on close-based multiples, n=13). For the 4 core perp DEXs, all exceeded TGE FDV, 2 of 4 (ROLL, EDGE) reached at least 2x, none reached 5x, and all 4 trade below their day-1 close today.

### Cited Findings
All counts below are computed from the per-token values in Q2. Sources: [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=edgex,paradex,backpack,grvt,roll-2,based-one,genius-3,infinex-2,rails,ranger,tread-fi,bullbit,flying-tulip,gtr-trade) and the DefiLlama per-token chart URLs listed in Q2. Calculation script: `/tmp/claude-0/-home-user-test-claude/2ad751b0-58d6-5348-a96a-1b74151bb386/scratchpad/cohortC2_scripts/final_stats.py`.

**Sample:** 13 tokens = 4 core (ROLL, DIME, EDGE, GRVT) + 9 borderline (RNGR, INX, RAILS, FT, BP, BASED, GENIUS, GTR, TREAD). Excluded: BUBI (no TGE-day price), ETHGas and Ascend (not perps), and pump-style micro-caps (treated separately below).

**Exceeded TGE FDV at any time (intraday ATH):**

| Threshold | vs day-1 close | vs first trade |
|---|---|---|
| >1.0x | 13/13 | 13/13 (FT on its $0.10 opening/sale basis) |
| ≥1.2x | 12/13 (fails: RNGR 1.06x) | 11/13 |
| ≥1.5x | 11/13 (fails: RNGR, DIME 1.42x) | 9/13 (fails: RNGR 1.10x, GRVT 1.19x, GTR 1.37x, DIME 1.42x) |
| ≥2x | 6/13 | 7/13 |
| ≥5x | 1/13 (BP 7.38x) | 1/13 (BP 6.01x) |

- The ≥2x tokens on the day-1-close basis: ROLL 2.28x, EDGE 2.35x, RAILS 2.60x, BASED 2.71x, TREAD 3.49x, BP 7.38x
- The ≥2x tokens on the first-trade basis: ROLL 2.34x, EDGE 2.21x, BASED 2.21x, TREAD 2.87x, RAILS 4.69x, GENIUS 4.85x, BP 6.01x

**Using best daily close instead of intraday ATH (vs day-1 close):**
- Above 1.0x: 10/13. RAILS, INX and DIME never closed a day above their TGE-day level.
- ≥1.5x: 5/13 — FT 1.62x, ROLL 2.11x, EDGE 2.30x, TREAD 3.08x, BP 6.04x
- ≥2x: 4/13
- ≥5x: 1/13 (BP)

**Core perp DEXs only (n=4):**
- All 4 exceeded TGE FDV on both bases.
- ≥1.5x: 3/4 on the day-1 basis (ROLL, EDGE, GRVT) and 2/4 on the first-trade basis.
- ≥2x: 2/4 (ROLL, EDGE). ≥5x: 0/4.
- DIME counts as ≥2x only if its TGE basis is the $0.0446 Mar-6 price (2.29x) rather than the $0.072 first print (1.42x).

**ATH timing:**
- Within the first 7 days: 7/13 — RNGR d0, INX d0, RAILS d0, GRVT d0, GTR d0, ROLL d3, GENIUS d5
- Later: 6/13 — TREAD d11, BASED d17, EDGE d52, BP d192, DIME d220, FT d231

**Of the 7 listing-week ATHs, did they later trade more than 1.2x above the day-1 close (on daily closes) after day 7?**
- Yes: ROLL (1.91x on Jul 20), GENIUS (1.36x on May 24), GRVT (1.35x on Aug 11)
- No, spike only: RNGR (1.01x), INX (0.92x), RAILS (0.83x), GTR (1.02x)

**More or less straight down:**
- RAILS (−94% vs day-1 close), GTR (−90%), INX (−77%), RNGR (liquidated, about −100%)
- BUBI is −54% since CoinGecko coverage began

**Current FDV vs day-1 close:**
- Median 0.58x; only 3 of 13 are above (BP 4.28x, TREAD 1.97x, FT 1.26x)
- Core: ROLL 0.78x, DIME 0.63x (vs $0.072), EDGE 0.51x, GRVT 0.88x

**Low vs high TGE FDV:**
- Spearman rank correlation between TGE FDV and peak multiple:
  - +0.01 on the day-1 basis
  - +0.12 on the first-trade basis
  - +0.42 using best-daily-close multiples
- Tokens with day-1 FDV under $100M (n=6: GTR, RNGR, RAILS, TREAD, DIME, ROLL): median ATH multiple 2.08x, median best-close multiple 1.09x
- Tokens at $100M or more (n=7: BASED, INX, BP, GRVT, GENIUS, EDGE, FT): median ATH multiple 1.86x, median best-close multiple 1.41x

**Days since TGE:** TREAD 41, GRVT 89, GTR 94, BUBI 126 (BingX TGE); all others 197–290 days. Recent launches have had less time to peak.

**Micro-cap appendix (21 pump-style tokens in CG Perpetuals/Derivatives/Options, launched in 2026)** — [CG Perpetuals markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=decentralized-perpetuals&per_page=250&page=1); [CG Derivatives markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=decentralized-derivatives&per_page=250&page=1)
- 20 of 21 made their ATH within about 7 days of their first print. Typical peaks were 1.0–2.7x the first print; outliers were PARQ at 10.9x on day 1 and K9 at 7.8x on day 133.
- Almost all now trade at 0.2–15% of their first print. K9 is at 0.76x and NEXUS at 0.49x.

**External cross-check:** As of May 23, 2026, only 2 of 7 perp-DEX tokens launched Sep 2025–Mar 2026 were above their launch level — [HOKANEWS](https://www.hokanews.com/2026/05/7-perp-dex-tokens-launched-only-2.html)

### Inferences
- **Literal hypothesis.** Read literally ("pushed to a higher FDV at some point after TGE"), the hypothesis holds almost trivially in this cohort: every analysable token printed above its TGE FDV at least once. But the main mechanism was listing-day or listing-week volatility, not a later re-rating. With a 1.5–2x threshold on daily closes, the "pushed higher" share falls to about 30–40% (4–5 of 13).
- **"Low FDV" part.** The data does not support the low-FDV part of the hypothesis. The tokens with the biggest sustained re-ratings had mid-to-high TGE FDVs (BP ~$224M, EDGE ~$657M), plus one low-FDV name (TREAD ~$39M). Several of the lowest-FDV launches (RNGR, RAILS, GTR) never re-rated after day 1.
- **Later peaks were catalyst- and sector-driven.** BP had the SEC tokenized-stock exemption; EDGE had V2, buybacks and OKX/Kraken listings. Both also rode the H2-2026 perp-DEX sector rally (see Q4), not a mechanical "low FDV" effect.
- **Core sample.** The core perp-DEX sample (n=4) matches the "spike then fade" pattern: 2 of 4 reached about 2.3x, but all 4 now trade 12–49% below their day-1 close.

### Gaps
- n is very small: 4 core, 13 including borderline. No statistical test is meaningful, and conclusions are directional only.
- Intraday highs after day 7 were not measured. Only daily closes and CoinGecko's overall ATH were used, so the ">1.2x after day 7" test may under-count brief spikes (e.g., DIME's Oct 11 intraday $0.102 vs a $0.0687 daily point).
- BUBI's peak multiple could not be computed.
- Recent TGEs (TREAD, GRVT, GTR) have had under 100 days, so their peak multiples are provisional.

## Q4. Market conditions in 2026 around each TGE and peak

### Takeaway
- **H1 2026 was risk-off.** BTC fell from a $96.9K high on Jan 15 to a $58.6K low on Jul 1, and ETH fell from $3,355 to $1,565. Most cohort TGEs (Jan–Apr) launched into that decline, which fits their early fades.
- **Q3 brought a strong rotation into perp-DEX tokens.** HYPE went from a $20.9 low on Jan 20 to a $97.2 high on Sep 23; LIT went from $0.81 on Mar 30 to $5.32 on Sep 24; BTC recovered to about $83.6K by Oct 1.
- The cohort's late peaks cluster in that window: TREAD Sep 27, BP Oct 1, DIME Oct 11, FT Oct 12, plus LV (Dec-2025 TGE) on Oct 2. EDGE's May 22 peak came during a mid-cycle BTC bounce to about $75–79K.

### Cited Findings
**BTC daily (00:00 UTC), 2026:**
- $87,515 on Jan 1; 2026 high $96,940 on Jan 15
- $78,630 on Feb 1; $66,990 on Mar 1; $68,230 on Apr 1; $76,290 on May 1; $73,570 on Jun 1
- 2026 low $58,558 on Jul 1
- $78,550 on Sep 1; $83,580 on Oct 1; $80,029 on Oct 27
- Sources: [DefiLlama BTC chart Jan–May](https://coins.llama.fi/chart/coingecko:bitcoin?start=1767225600&span=150&period=1d&searchWidth=14400); [DefiLlama BTC chart Jun–Oct](https://coins.llama.fi/chart/coingecko:bitcoin?start=1780185600&span=150&period=1d&searchWidth=14400)

**ETH, 2026:** $2,967 on Jan 1; high $3,355 on Jan 15; low $1,565 on Jun 25; $2,321 on Oct 27 — [DefiLlama ETH chart](https://coins.llama.fi/chart/coingecko:ethereum?start=1767225600&span=150&period=1d&searchWidth=14400); [DefiLlama ETH chart Jun–Oct](https://coins.llama.fi/chart/coingecko:ethereum?start=1780185600&span=150&period=1d&searchWidth=14400)

**Perp-DEX sector proxies:**
- HYPE: $25.44 on Jan 1; low $20.92 on Jan 20; $72 on Jun 1; high $97.19 on Sep 23; $78.22 on Oct 27 — [DefiLlama HYPE chart](https://coins.llama.fi/chart/coingecko:hyperliquid?start=1767225600&span=150&period=1d&searchWidth=14400); [DefiLlama HYPE chart Jun–Oct](https://coins.llama.fi/chart/coingecko:hyperliquid?start=1780185600&span=150&period=1d&searchWidth=14400)
  - CoinGecko lists HYPE's ATH at $97.96 on 2026-09-23 — [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=hyperliquid)
- LIT: $2.48 on Jan 1; low $0.81 on Mar 30; high $5.32 on Sep 24; $3.01 on Oct 26 — [DefiLlama LIT chart](https://coins.llama.fi/chart/coingecko:lighter?start=1767225600&span=150&period=1d&searchWidth=14400)
- ASTER stayed in a $0.47–0.79 range all year ($0.71 on Oct 26) — [DefiLlama ASTER chart](https://coins.llama.fi/chart/coingecko:aster-2?start=1767225600&span=150&period=1d&searchWidth=14400)

**BTC on each TGE date** (from the same DefiLlama BTC series):

| Date | Event | BTC |
|---|---|---|
| Jan 10 | RNGR TGE | $90.5K |
| Jan 16 | ROLL TGE | $95.6K |
| Jan 30 | INX TGE | $84.6K |
| Feb 23 | FT TGE | $67.6K |
| Mar 5 | DIME TGE | $72.7K |
| Mar 23 | BP TGE | $70.9K |
| Mar 30 | BASED TGE | $66.0K |
| Mar 31 | EDGE TGE | $66.7K |
| Apr 13 | GENIUS TGE | $74.5K |
| Jun 23 | BUBI TGE | $62.7K |
| Jul 30 | GRVT TGE | $64.7K |
| Sep 16 | TREAD TGE | $75.6K |

**BTC at the late peaks:** EDGE ATH (May 22) $75.5K; BP ATH (Oct 1) $83.6K; DIME ATH (Oct 11) $82.9K — [DefiLlama BTC chart](https://coins.llama.fi/chart/coingecko:bitcoin?start=1767225600&span=150&period=1d&searchWidth=14400); [DefiLlama BTC chart Jun–Oct](https://coins.llama.fi/chart/coingecko:bitcoin?start=1780185600&span=150&period=1d&searchWidth=14400)

**Narrative context:**
- EDGE's May ATH was framed as part of a rotation into perp-DEX and RWA-infrastructure tokens while BTC and ETH stayed well below their highs — [Odaily](https://www.odaily.news/en/newsflash/483270)
- BP's Sep–Oct run was tied to the SEC's Sep 17 "Innovation Exemption" for on-chain tokenized-stock trading — [Crypto Briefing](https://cryptobriefing.com/backpack-bp-token-all-time-high-sec-exemption/)
- StandX's shutdown note says perp-DEX activity was booming mid-2026, with StandX itself at about $700M daily volume in July — [KuCoin/Biteye](https://www.kucoin.com/news/flash/standx-cancels-tge-and-shuts-down-amid-perp-dex-boom)

### Inferences
- The 2026 cohort is heavily confounded by timing. Tokens launched in Jan–Apr faced a 30–40% BTC drawdown into July. Those still alive by Q3 got a sector tailwind (HYPE roughly 4.6x from its January low), which produced several late ATHs (BP, DIME, FT, TREAD).
- Q3 TGEs (GRVT on Jul 30, TREAD on Sep 16) caught the recovery: TREAD reached 3.5x its day-1 close within 11 days. This suggests market regime at and after TGE explains more of the peak multiple than TGE FDV does.

### Gaps
- No independent 2026 market recap (CoinDesk/The Block) was retrieved. Market conditions are described from DefiLlama price series and token-specific news only.
- Funding rates, open interest and perp-DEX volume share by month were not collected.

## Q5. Notable perp DEXs with no TGE as of Oct 27, 2026, and implied FDVs

### Takeaway
Several of the most-watched perp DEXs remained tokenless on Oct 27, 2026:
- Variational (TGE guided for Q4 2026), Pacifica, Extended, Ostium, Hibachi, Ethereal, Reya, Nado (points convert to $INK), Decibel, Perpl, BULK, Hotstuff, RISEx, Bullet, and the HIP-3 deployers tradeXYZ and Ventuals.
- StandX cancelled its TGE and is shutting down.

Market-implied valuations are thin and mostly stale:
- Variational: pre-market implied about $610–690M after its May 2026 Series A.
- Reya: last sale at a $150M valuation.
- Ostium: last private round at $250M.
- Pacifica: Polymarket markets priced only a modest chance of more than $300M.

### Cited Findings
**No-token status:** DefiLlama's registry shows `gecko_id = null` (no token) for Extended Perps (TVL $110.8M), Decibel (Aptos, $29.3M), RISEx ($20.6M), Reya Perps ($9.7M), BULK ($8.3M), Ostium ($3.7M), Perpl ($3.2M), Ethereal DEX, Pacifica Perps, Hibachi, Nado Perps, StandX Perps, Bullet Perps, Hotstuff Perps, Variational, tradeXYZ, Ventuals and Felix Perps (TVL values as of retrieval) — [DefiLlama protocols API](https://api.llama.fi/protocols)

**Variational (VAR):**
- TGE planned for Q4 2026. Tokenomics: 32% genesis airdrop (unlocked at TGE), 18% ecosystem, 50% team and investors (12-month lock, then at least 3 years of unlocking) — [Crypto Briefing](https://cryptobriefing.com/variational-var-token-launch-airdrop/)
- CoinGecko has a placeholder VAR listing with no price — [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=variational)
- After the May 20, 2026 Series A, pre-market trading implied about $610–690M FDV — [Octagon AI](https://www.octagonai.co/markets/crypto/fdv/variational-fdv-above-one-day-after-launch/)
- Polymarket "FDV one day after launch" snapshots (Apr 2026, possibly stale): >$200M about 75¢, >$300M about 56¢, >$800M about 10¢, >$2B about 3¢ — [Octagon AI](https://www.octagonai.co/markets/crypto/fdv/variational-fdv-above-one-day-after-launch/); [SimpleFunctions >$300M](https://simplefunctions.dev/markets/0x1aabd7e8fe19085c7ba902d5002d1fbb9116473fb89bdfcd3be5478017916013)
- Estimated value per point: about $44.5–59.2 — [Odaily](https://www.odaily.news/en/post/5213139)

**Pacifica (Solana):**
- No token, self-funded per airdrop guides — [airdropalert](https://airdropalert.com/blogs/pacifica-review/)
- Polymarket "FDV one day after launch" (resolves NO if no token by Dec 31, 2026):
  - >$300M at about 12¢ on Apr 3, 2026 (about 23¢ in a later snapshot) — [Lines](https://www.lines.com/prediction-markets/crypto/pacifica-fdv-above-one-day-after-launch)
  - >$1B at about 5¢ — [SimpleFunctions](https://simplefunctions.dev/markets/pacifica-fdv-above-one-day-after-launch-1b-polymarket-0x2b5d5dd6cb)
  - >$2B at 94% "No" as of Jun 24 — [Polyguana](https://polyguana.com/market/716653)

**Reya:**
- CoinList sale in Nov 2025 at a $150M valuation; 50% unlocks at TGE and 50% vests linearly over 6 months — [ICO Drops](https://icodrops.com/reya)
- TGE still "not officially confirmed" as of Oct 12, 2026 — [Bitrue](https://www.bitrue.com/blog/reya-airdrop-guide)
- Limitless market on REYA FDV >$200M one day after launch — [LaikaLabs](https://laikalabs.ai/app/prediction-markets/limitless/reya-fdv-above-200m-one-day-after-launch-2027-01-01)
- CoinGecko lists REYA with 8B supply but no price — [CG snapshot](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=reya)

**Ostium:** raised more than $20M in Dec 2025 at a $250M valuation; Delphi treats a TGE at that FDV as the bear case — [Delphi Digital](https://members.delphidigital.io/feed/ostium-airdrop-points-napkin-math)

**Hibachi:** an Apr 2026 Polymarket snapshot priced a token launch by Jun 30, 2026 at about 8%. None occurred per DefiLlama — [SimpleFunctions](https://simplefunctions.dev/markets/0xb25f40bb52538e79ce94a4173681f2b8f603548e4d83b78c0c5a561d504da67c); [DefiLlama protocols API](https://api.llama.fi/protocols)

**Ethereal:** an Ethena governance proposal promises ENA holders 15% of any future Ethereal token. It is in mainnet alpha with no token — [The Block](https://www.theblock.co/post/318633/spot-and-perps-dex-named-ethereal-proposed-to-be-built-on-ethena-network); [The Defiant](https://thedefiant.io/news/defi/ethena-community-approved-dex-ethereal-launches-mainnet-alpha)

**Extended:** ex-Revolut team, live on Starknet mainnet since Aug 2025; no token — [The Block](https://www.theblock.co/post/366529/ex-revolut-team-perp-dex-extended-live-on-starknet); [DefiLlama protocols API](https://api.llama.fi/protocols)

**StandX:** cancelled its TGE and is ceasing development (announced Oct 15, 2026)
- Pays a one-time DUSD airdrop with no lock-up: inquiries from Oct 26, claims Nov 1–Dec 31, 2026
- Never took VC funding
- About $700M daily volume in Jul 2026
- Source: [KuCoin/Biteye](https://www.kucoin.com/news/flash/standx-cancels-tge-and-shuts-down-amid-perp-dex-boom)

### Inferences
- The pending pipeline's implied valuations ($150–690M) sit in the same range as the 2026 core cohort's TGE FDVs ($45–657M on day-1 bases). If the 2026 pattern repeats (spike, then fade, with re-ratings depending on sector regime), those pre-market levels are not obviously "low FDV" launches.
- StandX shows survivorship risk among points programs: a high-volume perp DEX ended with no token at all.

### Gaps
- No live Oct 2026 Polymarket, Whales Market or Hyperliquid pre-launch prices were retrieved for Variational, Pacifica, Extended, Ethereal or Nado. The quoted odds are April–June 2026 snapshots.
- Nado's points-to-$INK conversion appeared in a Feb-2026 farming roundup returned by search, but the exact page could not be pinned down ([CoinCodeCap](https://coincodecap.com/best-perp-dex-airdrops-top-platforms-worth-farming) or [DropsTab](https://dropstab.com/research/alpha/top-perpetual-dex-platforms-for-point-farming)). Treat it as unverified.
- No expected TGE date or valuation was found for Extended, Decibel, Perpl, BULK, Hotstuff or RISEx.
