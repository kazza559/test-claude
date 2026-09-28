# TGE valuation comps: Ethena (ENA), Usual (USUAL), OpenEden (EDEN), Falcon Finance (FF), Resolv (RESOLV)

Data pulled 2026-09-28 (UTC). The research date is 2026-09-28, and every "current" number carries that stamp unless noted otherwise.

**Methodology (applies to every table below)**
- **Prices** come from Binance spot USDT pairs (public kline API, `https://data-api.binance.vision/api/v3/klines?symbol=XXXUSDT&interval=1d|1h`). Binance was the main venue at every TGE.
  - **"Open price"** is the **volume-weighted average price of the first trading hour on Binance**. It is not the first print: Binance listing auctions print artificial first ticks of $0.30 for ENA, $0.0125 for USUAL, $0.15 for EDEN and $0.05 for FF.
  - The first-day close and the 24-hour VWAP are also given as a range.
  - **+1m, +3m, +6m and +12m** are Binance daily closes on TGE date + 30, 90, 180 and 365 days.
  - **ATH** is the Binance intraday high.
- **FDV = price × max supply**, using ENA 15B, USUAL 4B (the max supply at TGE per Binance), EDEN 1B, FF 10B and RESOLV 1B. Market cap = price × circulating supply at listing, as stated by Binance.
- **Current price, market cap and circulating supply** come from the CoinGecko `/coins/{id}` endpoint, `last_updated` 2026-09-28 ~11:45 UTC. Binance closes were used for the drawdowns.
- **Stablecoin supply** comes from DefiLlama stablecoins (`stablecoins.llama.fi/stablecoin/{id}`: USDe=146, USD0=195, USDO=241, USDf=246, USR=197, USDtb=221).
- **Protocol TVL** comes from `api.llama.fi/protocol/{slug}`.
- **Fees and revenue** come from `api.llama.fi/summary/fees/{slug}` (dailyFees / dailyRevenue).
- The public CoinGecko API now caps history at 365 days, so older price history uses Binance only.

---

## Q0. Master comparison table (summary of all key questions)

### Takeaway
At TGE, all five opened at **1.8x–5.5x FDV/stablecoin supply**.
- **Price:** four of the five are down **93–96%** from the TGE open as of Sep 2026. Ethena (−54%) is the exception. FF has lost 71%, but it TGE'd only 12 months ago and still holds $1.2B of USDf.
- **Peak FDV:** the 2025 cohort (RESOLV, FF, EDEN) printed its peak FDV in the **first trading hour**. Only the 2024 cohort (ENA, USUAL) rallied after listing.
- **Valuation vs private rounds:** where a comparable private or public-sale valuation exists, TGE FDV was **~10–29x** it.

### Cited Findings

**Table A — Timeline and TVL**

| Metric | Ethena (ENA) | Usual (USUAL) | Resolv (RESOLV) | OpenEden (EDEN) | Falcon (FF) |
|---|---|---|---|---|---|
| Stablecoin | USDe (delta-neutral synthetic $) | USD0 / USD0++ (T-bill RWA-backed) | USR (ETH/BTC delta-neutral + RLP junior tranche) | USDO / cUSDO (tokenized T-bills; + TBILL vault) | USDf / sUSDf (overcollateralized synthetic $) |
| First on-chain supply (DefiLlama) | 2023-12-11 | 2024-05-24 | 2024-06-05 (≈$9M until Dec-24) | USDO 2025-01-14 (TBILL earlier) | 2025-03-24 (closed beta) |
| Public launch | 2024-02-19 | 2024-07-10 (public pre-launch) | ~Sep 2024 | USDO ~Jan 2025 | 2025-04-30 |
| Points program start | Shards S1 2024-02-19 | Pills ~2024-07-10 | Points Epoch I ~2024-09-04 | Bills ~Mar 2025 | Miles 2025-04-30 |
| TGE (Binance spot) | 2024-04-02 08:00 UTC | 2024-11-19 ~10:00 UTC | 2025-06-11 ~14:00 UTC | 2025-09-30 ~11:00 UTC | 2025-09-29 13:00 UTC |
| Months, public launch → TGE | ~1.4 | ~4.3 | ~9 | ~8.5 (from USDO) | ~5.0 |
| Months of points before TGE | ~1.4 (S1 only; S2 ran after TGE) | ~4.2 | ~9 (S1) | ~6.5 | ~5.0 |
| Stablecoin supply at TGE | $1.56B | $375M | $217M (protocol TVL incl. RLP $350M) | USDO $235M (+ TBILL; ~$286M on 2025-08-14) | $1.90B |
| Peak supply (date) | $14.82B (2025-10-04) | $1.86B (2025-01-07) | $586M (2025-01-27, pre-TGE) | $299M (2025-07-21, pre-TGE) | $2.15B (2025-10-15) |
| Current supply (2026-09-28) | $4.95B (+ USDtb $0.54B) | $547M (DefiLlama protocol TVL only $88M) | ~$6M (post-exploit) | $14.5M | $1.21B |

**Table B — Listing, price path and valuation ratios**

| Metric | Ethena (ENA) | Usual (USUAL) | Resolv (RESOLV) | OpenEden (EDEN) | Falcon (FF) |
|---|---|---|---|---|---|
| Venue / mechanism | Binance Launchpool #50 (300M = 2%) | Binance Launchpool (300M = 7.5%) | Binance Alpha (6/10), HODLer Airdrop #21 (20M = 2%) | Binance HODLer Airdrop #47 (15M = 1.5%) | Binance HODLer Airdrop #46 (150M = 1.5%); Buidlpad sale |
| Max supply (used for FDV) | 15B | 4B at TGE (CoinGecko now: max 3B, total 1.958B) | 1B | 1B | 10B |
| Initial circulating | 1.425B (9.5%) | 494.6M (12.37%) | 155.75M (15.58%) | 183.87M (18.39%) | 2.34B (23.4%) |
| Open price (1st-hour VWAP) | $0.570 | $0.362 | $0.384 | $0.843 | $0.453 |
| Day-1 close / 24h VWAP | $0.775 / $0.714 | $0.285 / $0.315 | $0.343 / $0.365 | $0.401 / $0.547 | $0.282 / $0.322 |
| Opening FDV | **$8.55B** | **$1.45B** | **$384M** | **$843M** | **$4.53B** |
| Opening market cap | $813M | $179M | $60M | $155M | $1.06B |
| Peak FDV (date) | $22.8B (2024-04-11, +9d) | $6.61B (2024-12-20, +31d) | $430M (TGE hour) | $1.40B (TGE hour) | $5.80B (TGE hour) |
| FDV at +1m | $11.97B (+40%) | $5.77B (+299%) | $185M (−52%) | $130M (−85%) | $1.52B (−66%) |
| FDV at +3m | $7.58B (−11%) | $933M (−36%) | $154M (−60%) | $67M (−92%) | $930M (−79%) |
| FDV at +6m | $5.82B (−32%) | $530M (−63%) | $79M (−79%) | $26M (−97%) | $708M (−84%) |
| FDV at +12m | $4.96B (−42%) | $110M (−92%) | $17M (−96%) | n/a (listed <12m) | n/a |
| Current price (2026-09-28) | $0.263 | $0.0151 | $0.0186 | $0.0588 | $0.1298 |
| Current FDV / market cap | $3.95B / $2.66B | $60M on 4B ($29M on CoinGecko total) / $29M | $18.6M / $9.0M | $58.8M / $25.0M | $1.30B / $408M |
| Drawdown vs open / vs ATH | −54% / −83% | −96% / −99% | −95% / −96% | −93% / −96% | −71% / −78% |
| FDV at TGE ÷ supply at TGE | **5.5x** | **3.9x** | **1.8x** (1.1x vs TVL incl. RLP) | **3.6x** (USDO only) | **2.4x** |
| Current FDV ÷ current supply | 0.80x | 0.11x (0.69x vs $88M TVL) | ~3.0x | ~4.0x (USDO only) | 1.07x |
| FDV at TGE ÷ annualized fees (30d pre-TGE) | 18.6x (fees ann. $460M) | 88x ($16.5M) | 13x ($29.5M) | 72x ($11.7M) | n/a (no pre-TGE fee data) |
| Current FDV ÷ trailing-1y fees | 14.8x ($267M) | 4.4x ($13.6M); revenue $9.65M | n/m (fees ≈0 since exploit) | 16.9x ($3.5M); 92x revenue ($0.64M) | 227x ($5.7M, partial coverage) |

**Table C — Airdrop and fundraising**

| Metric | Ethena (ENA) | Usual (USUAL) | Resolv (RESOLV) | OpenEden (EDEN) | Falcon (FF) |
|---|---|---|---|---|---|
| Points airdrop, % supply | S1 5% (750M) | Pills 8.5% (7.5% + 1%) | S1 10% (100M); S2 4% | Bills 7.5% (75M) | Within 8.3% "Airdrops & Launchpad" bucket (Miles, Buidlpad, Yap2Fly); Miles split not disclosed |
| Airdrop value at open price | $428M | ~$123M (340M tokens × $0.362); ~$331M at claim-day VWAP ($0.97, 2024-12-18) | $38M | $63M | n/d |
| Airdrop ÷ opening FDV | 5% | 8.5% | 10% | 7.5% | — |
| Implied $ per point at open | ~$0.0012 per shard (360B shards; unverified) | n/d (total Pills not found) | ~$5.9e-6 per point (estimate) | n/d | n/d |
| Last private / public-sale valuation | $300M (Feb 2024 strategic) | undisclosed | undisclosed ($10M seed, Apr 2025) | undisclosed | Buidlpad public sale $350M / $450M FDV |
| TGE FDV ÷ last valuation | **~28.5x** | n/a | n/a | n/a | **~12.9x / ~10.1x** |

Data sources for these tables:
- Binance klines ([ENA](https://data-api.binance.vision/api/v3/klines?symbol=ENAUSDT&interval=1d), [USUAL](https://data-api.binance.vision/api/v3/klines?symbol=USUALUSDT&interval=1d), [RESOLV](https://data-api.binance.vision/api/v3/klines?symbol=RESOLVUSDT&interval=1d), [EDEN](https://data-api.binance.vision/api/v3/klines?symbol=EDENUSDT&interval=1d), [FF](https://data-api.binance.vision/api/v3/klines?symbol=FFUSDT&interval=1d)).
- CoinGecko ([ethena](https://api.coingecko.com/api/v3/coins/ethena), [usual](https://api.coingecko.com/api/v3/coins/usual), [resolv](https://api.coingecko.com/api/v3/coins/resolv), [openeden](https://api.coingecko.com/api/v3/coins/openeden), [falcon-finance-ff](https://api.coingecko.com/api/v3/coins/falcon-finance-ff)).
- DefiLlama stablecoins ([USDe](https://stablecoins.llama.fi/stablecoin/146), [USD0](https://stablecoins.llama.fi/stablecoin/195), [USR](https://stablecoins.llama.fi/stablecoin/197), [USDO](https://stablecoins.llama.fi/stablecoin/241), [USDf](https://stablecoins.llama.fi/stablecoin/246), [USDtb](https://stablecoins.llama.fi/stablecoin/221)).
- DefiLlama fees ([ethena](https://api.llama.fi/summary/fees/ethena?dataType=dailyFees), [usual](https://api.llama.fi/summary/fees/usual?dataType=dailyFees), [resolv](https://api.llama.fi/summary/fees/resolv?dataType=dailyFees), [openeden](https://api.llama.fi/summary/fees/openeden?dataType=dailyFees), [falcon-finance](https://api.llama.fi/summary/fees/falcon-finance?dataType=dailyFees)).
- Qualitative sources are cited in the sections below.

### Inferences
- **Opening FDV/TVL band.** A reasonable comp band for a new yield-bearing stablecoin TGE on Binance is **~2x–5.5x FDV/stablecoin supply**, with a median of ~3.6x across the five. Ethena, the category-defining asset in a bull market, sat at the top at 5.5x. RESOLV sat at the bottom at 1.8x, TGE'ing after its supply had already fallen 63% from peak.
- **Where the peak lands.** Post-2025 Binance HODLer-style listings peaked in the first hour and then bled 50–85% within a month. Using the open as "fair value" for a comp therefore overstates sustainable value. The **+1m FDV** is likely the more robust anchor: ENA $12.0B, USUAL $5.8B, FF $1.5B, RESOLV $185M, EDEN $130M. At +1m, FDV/TVL was ~5.2x, ~5.6x, ~0.75x, ~0.82x and ~0.58x respectively.
- **What survives.** Protocols whose stablecoin kept growing after TGE (Ethena; Usual until the USD0++ depeg) held or expanded their FDV for 1–3 months. Those whose supply fell after TGE (OpenEden USDO, Resolv) saw the steepest token declines.

### Gaps
- Total points distributed are not published for Usual (Pills), Falcon (Miles) or OpenEden (Bills). Resolv's total is only derivable from a secondary-source example.
- Private-round valuations for Usual, Resolv, OpenEden and Falcon (WLFI and M2 rounds) are undisclosed.
- OpenEden TBILL TVL at TGE and today could not be pulled: the DefiLlama protocol TVL series for OpenEden is empty, and CoinGecko returns zero market cap for TBILL.

---

## Q1. Stablecoin product, yield source, and launch → points → TGE timeline

### Takeaway
Time from public launch to TGE ranged from **~1.4 months (Ethena) to ~9 months (Resolv)**. The 2025 cohort (Resolv, OpenEden, Falcon) ran **5–9 months** of points farming before TGE, versus ~1.4 months (Ethena S1) and ~4 months (Usual) in 2024.

### Cited Findings

**Ethena (ENA)**
- **Product:** USDe is a delta-neutral synthetic dollar (staked ETH / BTC / stables collateral hedged with short perps). Yield comes from funding and basis plus staking, paid to sUSDe.
- **Launch and funding:** USDe publicly launched in Feb 2024 alongside a $14M raise at a $300M valuation — [The Block](https://www.theblock.co/post/277565/ethena-usde-stablecoin-funding-valuation-paypal-brevan-howard-others).
- **First supply:** DefiLlama shows first USDe supply on 2023-12-11 (private phase) — [DefiLlama USDe](https://stablecoins.llama.fi/stablecoin/146).
- **Shards campaign:**
  - Ran Feb 19 → Apr 1, 2024 (~40 days) — [search summary of oneclick.fi case study](https://www.oneclick.fi/blog/ethena-season-1-airdrop-case-study). That URL now 404s; the dates were also reported via [CoinJournal](https://coinjournal.net/news/ethena-labs-announces-750-million-ena-airdrop-for-its-community/).
  - DL News describes the six-week campaign as "February 19 – March 13" and says S1 ended when supply hit $1B — [DL News](https://www.dlnews.com/articles/defi/ethena-500m-airdrop-leads-defi-project-to-plan-the-next-one/). **These end dates conflict.** The snapshot / TGE end is generally given as Apr 1.
- **TGE:** Binance listed ENA on 2024-04-02 08:00 UTC — [Binance announcement](https://www.binance.com/en/support/announcement/introducing-ethena-ena-on-binance-launchpool-farm-ena-by-staking-bnb-and-fdusd-6c216f219f0e42adb1849759dee3fbd9).

**Usual (USUAL)**
- **Product:** USD0 is a stablecoin backed by T-bill RWAs. USD0++ is a 4-year locked "bond" version that earned USUAL emissions. USUAL is a revenue-redistribution token — [Crowdfund Insider](https://www.crowdfundinsider.com/2024/12/234605-stablecoin-project-usual-raises-10m-series-a-led-by-binance-labs-kraken-ventures/).
- **Launch:** Public pre-launch opened on 2024-07-10, after a private phase that raised $75M in TVL commitments — [Chainwire](https://chainwire.org/2024/07/10/usual-labs-announces-public-pre-launch-phase-after-securing-75m-in-tvl-for-usd0-during-private-phase/).
- **Pills:** The pre-launch period ended mid-November 2024. Pills: 5 per USD0++ issued, with a Final Boost starting at 1x and growing 2% per day — [Usual Docs](https://docs.usual.money/archive/usual-airdrop/pills-campaign-rules).
- **TGE:** Binance Launchpool farming ran Nov 15–18; listing followed on 2024-11-19 — [NFTevening](https://nftevening.com/usual-binance-launchpool/).

**Resolv (RESOLV)**
- **Product:** USR is a delta-neutral stablecoin backed by ETH and BTC and hedged with perps. RLP is a junior insurance tranche that absorbs losses and earns levered yield — [DefiLlama raises metadata](https://api.llama.fi/protocol/resolv-usr); [Bybit Learn](https://www.bybit.com/en/learn/stablecoin/what-is-resolv-crypto).
- **Launch:** Public launch in Sep 2024.
- **Points:** Epoch I ran until 2024-10-04 (one month, i.e. starting ~early Sep 2024) with a +150% boost — [Resolv Medium](https://medium.com/@ResolvLabs/introducing-resolv-points-program-cbcd94b77be1) (via search summary).
- **Season 1:**
  - Lasted nine months and culminated in the Genesis airdrop in May 2025 — [Resolv Docs S1](https://docs.resolv.xyz/litepaper/using-resolv/resolv-points/seasons/season-1).
  - Rates: USR 30 points per $ per day; RLP 10; stUSR 5.
- **TGE:** Binance Alpha listing 2025-06-10; Binance spot 2025-06-11 — [CryptoNinjas](https://www.cryptoninjas.net/news/binance-launches-20m-resolv-airdrop-for-bnb-holders-ahead-of-major-token-listing/); Binance klines.

**OpenEden (EDEN)**
- **Product:** TBILL is a tokenized short-term US Treasury vault, the first tokenized T-bill product rated 'A' by Moody's. USDO is a yield-bearing stablecoin backed by tokenized T-bills and issued by Bermuda-regulated OpenEden Digital — [OpenEden blog](https://openeden.com/news/openeden-eden-token-tokenized-rwa-ecosystem/).
- **USDO launch:** DefiLlama shows first USDO supply on 2025-01-14 — [DefiLlama USDO](https://stablecoins.llama.fi/stablecoin/241).
- **Bills campaign:** Ran from March 2025. The Curve Stability Vault offered 30x Bills from 2025-09-01, and EDEN pre-farming began 2025-09-15 — [OpenEden OpenSeason](https://openeden.com/news/openseason-next-phase-bills-points-eden-rewards/) (via search summary); [PANews](https://www.panewslab.com/en/articles/85acffc7-f9f6-4fd9-be3d-aca2375d1b6a).
- **TGE:** 2025-09-30 on Binance — [PANews](https://www.panewslab.com/en/articles/22c47f7b-cdf5-4024-9e34-13f5903267ff).

**Falcon Finance (FF)**
- **Product:** USDf is an overcollateralized synthetic dollar. Collateral includes USDT, USDC, ETH, BTC, TON, NEAR and more (and later tokenized Treasuries). sUSDf is the yield-bearing staked version.
- **Launch and Miles:** Public launch and the Falcon Miles points program both began on 2025-04-30, after a closed beta with >$200M TVL — [Chainwire](https://chainwire.org/2025/04/30/falcon-finance-opens-to-the-public-and-launches-falcon-miles-points-program/). DWF Labs backed the project.
- **Miles rates (examples):** holding USDf 6x; minting against non-stable collateral 8x — [Falcon Docs](https://docs.falcon.finance/falcon-miles).
- **TGE:** Sep 29, 2025 — [Falcon blog](https://falcon.finance/news/falcon-finance-enters-its-next-chapter-with-the-launch-of-ff-token); Binance spot 13:00 UTC — [CryptoNinjas](https://www.cryptoninjas.net/news/binance-unveils-150m-falcon-finance-airdrop-ahead-of-sept-29-listing/).

### Inferences
- Months-to-TGE is not predictive of outcome on its own. Ethena's short farm preceded the best-performing token; Resolv's long farm preceded one of the worst.
- Supply momentum at TGE matters more. Resolv's supply had already fallen 63% from peak before TGE.

### Gaps
- **Resolv:** the exact USR public-launch day is unconfirmed (Sep 2024 per secondary sources).
- **OpenEden:** the exact Bills start date ("since March 2025") comes from a search summary, not a primary page read in full. The TBILL launch date was not verified.

---

## Q2. TVL / supply at TGE, peak, current, and post-TGE "mercenary capital" outflows

### Takeaway
- **Largest post-points outflows: OpenEden USDO and Usual USD0.** USDO lost 62% within 60 days and 94% to date. USD0 fell 65% from peak within ~4 months after the USD0++ depeg.
- **Ethena and Falcon kept growing for 1–3 months after TGE,** because points (Ethena S2, Falcon Miles S2 / sFF) continued.
- **Resolv's farmers left before TGE.** A March 2026 exploit then collapsed USR.

### Cited Findings
Unless noted, all figures are from DefiLlama stablecoin supply.

**Ethena USDe** ([source](https://stablecoins.llama.fi/stablecoin/146))
- Path: $1.56B at TGE (2024-04-02) → $2.31B at +30d (+48%) → $3.61B at +90d.
- It fell to $2.54B by 2024-10-01 (−30% from the July 2024 level) after S2 ended on 2024-09-02 and funding rates compressed.
- It peaked at **$14.82B on 2025-10-04**, then dropped to $9.37B (Nov-1) after the Oct-10-2025 crash.
- **Current: $4.95B (2026-09-28)**, −67% from peak. Ethena's USDtb adds $0.54B.
- USDe crossed $2B within two months of public launch — [The Block](https://www.theblock.co/post/286640/ethena-usde-stablecoin-crosses-2-billion-supply).

**Usual USD0** ([source](https://stablecoins.llama.fi/stablecoin/195))
- Path: $375M at TGE → $1.03B at +30d → **peak $1.86B on 2025-01-07** (+397% vs TGE, driven by USUAL emissions to USD0++).
- It then fell to $651M by 2025-05-01 (−65% from peak) and **$547M now** (−71%).
- DefiLlama protocol TVL for usual-usd0 is only **$88M now** vs a $1.87B peak (−95%) — [DefiLlama](https://api.llama.fi/protocol/usual-usd0). This supply-vs-TVL discrepancy is unexplained; it may be a methodology change.

**Resolv USR** ([source](https://stablecoins.llama.fi/stablecoin/197))
- Path: **peak $586M on 2025-01-27** → $217M at TGE (−63% before TGE) → $225M at +30d → $315M at +90d → $176M at +180d.
- It rebounded to ~$407M on 2026-01-30, then collapsed after the exploit. **Current ≈ $6M.**
- Protocol TVL (USR + RLP) was $350M at TGE and peaked at $685M on 2025-02-20 — [DefiLlama](https://api.llama.fi/protocol/resolv-usr).
- **Exploit (March 22–23, 2026):**
  - An attacker minted ~80M unbacked USR through a flaw in the minting contract: a single-key privileged account, no oracle or amount checks, and no mint cap.
  - The attacker extracted ~$23–25M. USR fell ~70–73% to ~$0.27, as low as $0.025 on DEXs.
  - The protocol was paused — [CoinDesk](https://www.coindesk.com/markets/2026/03/23/resolv-stablecoin-drops-70-after-usd80-million-exploit-after-attacker-mints-usr); [Bitcoin.com](https://news.bitcoin.com/resolv-labs-pauses-protocol-after-23m-exploit-triggers-usr-stablecoin-depeg/).

**OpenEden USDO** ([source](https://stablecoins.llama.fi/stablecoin/241))
- Path: **peak $299M on 2025-07-21** → $288M 30 days pre-TGE → $235M at TGE (−21% vs peak) → $224M at +30d → **$90M at +60d (−62%)** → $77M at +90d → $48M at +180d.
- **Current: $14.5M (−94% vs TGE).**
- As of 2025-08-14, OpenEden reported USDO at $277M and TBILL at $286M TVL — [OpenEden](https://openeden.com/news/openeden-eden-token-tokenized-rwa-ecosystem/).

**Falcon USDf** ([source](https://stablecoins.llama.fi/stablecoin/246))
- Path: $1.90B at TGE → $2.03B at +30d (+7%) → **peak $2.15B on 2025-10-15** → $2.11B at +90d → $1.64B at +180d (−14% vs TGE).
- **Current: $1.21B** (−36% vs TGE, −44% vs peak).
- Falcon cited "nearly $2B TVL, 1.9B USDf" at launch — [Falcon](https://falcon.finance/news/falcon-finance-enters-its-next-chapter-with-the-launch-of-ff-token).

### Inferences
- **Scale of "mercenary" outflow.** Where the points program effectively ended at or near TGE and yields were ordinary (T-bill-based USDO), 60–90-day outflow was **~60–70%**.
- **Where incentives continued, supply held or grew for 1–3 months.** Ethena ran S2; Usual ran USUAL emissions; Falcon ran Miles S2 with sFF multipliers of 160x/80x. The drawdown came later and was tied to market events: the funding compression of summer 2024, the USD0++ depeg of Jan 2025, and the Oct-10-2025 crash.
- **For a new protocol's comp,** assume a ~20–60% supply decline within 6 months of TGE unless incentives continue.

### Gaps
- No clean "points-ended" date exists for Ethena or Falcon, because seasons roll continuously. Mercenary outflow therefore cannot be cleanly separated from market-driven outflow.
- Current OpenEden TBILL TVL is not available from DefiLlama or CoinGecko.

---

## Q3. TGE listing details and price / FDV path

### Takeaway
- **Venue:** every token listed first on Binance — Launchpool for ENA and USUAL; HODLer Airdrop for RESOLV, EDEN and FF.
- **Initial float** rose from 9.5% (ENA) to 23.4% (FF).
- **ATH timing:** the 2024 listings made their ATH 9 days (ENA) and 31 days (USUAL) after TGE. The 2025 listings made their ATH in the first trading hour.

### Cited Findings

**ENA**
- Listing terms:
  - Max supply 15B; Launchpool 300M (2%); initial circulating 1.425B (9.5%).
  - Pairs: ENA/BTC, USDT, BNB, FDUSD, TRY; Seed Tag applied — [Binance](https://www.binance.com/en/support/announcement/introducing-ethena-ena-on-binance-launchpool-farm-ena-by-staking-bnb-and-fdusd-6c216f219f0e42adb1849759dee3fbd9).
- Price path (Binance):
  - First-hour VWAP $0.570; high $1.523 on 2024-04-11.
  - +30d $0.798; +90d $0.505; +180d $0.388; +365d $0.331.
  - Low $0.0699 on 2026-06-10. Current $0.263.
- CoinGecko ATH is $1.52 (2024-04-11), and CoinGecko circulating is now 10.10B — [CoinGecko](https://api.coingecko.com/api/v3/coins/ethena).

**USUAL**
- Listing terms: total/max supply 4B; Launchpool 300M (7.5%; BNB pool 255M, FDUSD pool 45M); circulating at listing 494.6M (12.37%) — [NFTevening](https://nftevening.com/usual-binance-launchpool/).
- Price path (Binance):
  - First-hour VWAP $0.362; ATH $1.652 on 2024-12-20.
  - +30d $1.442; +90d $0.233; +180d $0.132; +365d $0.0276. Current $0.0151.
- **Current supply figures differ from TGE.** CoinGecko now lists total supply 1.958B and max 3.0B, with circulating 1.937B — [CoinGecko](https://api.coingecko.com/api/v3/coins/usual). The reason for the change from 4B was not verified.

**RESOLV**
- Listing terms:
  - Supply 1B; HODLer airdrop 20M (2%); circulating at listing 155.75M (15.58%) — [CryptoNinjas](https://www.cryptoninjas.net/news/binance-launches-20m-resolv-airdrop-for-bnb-holders-ahead-of-major-token-listing/). This is a secondary source quoting Binance.
  - HODLer eligibility was May 28–31 BNB subscriptions; there were 5 spot pairs.
- Price path (Binance):
  - First-hour VWAP $0.384; ATH $0.4299 (first hour).
  - +30d $0.185; +90d $0.154; +180d $0.079; +365d $0.0172.
  - Low $0.0142 on 2026-06-20. Current $0.0186.

**EDEN**
- Listing terms:
  - Supply 1B; HODLer 15M (1.5%); circulating at listing 183.87M (18.39%) — [PANews](https://www.panewslab.com/en/articles/22c47f7b-cdf5-4024-9e34-13f5903267ff); [CryptoNinjas](https://www.cryptoninjas.net/news/binance-airdrops-15m-eden-tokens-as-openeden-debuts-with-1b-supply/).
  - Pairs: USDT, USDC, BNB, FDUSD, TRY.
- Price path (Binance):
  - First-hour VWAP $0.843; ATH $1.401 (first hour); day-1 close $0.4005.
  - +30d $0.130; +90d $0.0667; +180d $0.0261. Current $0.0588.
- Tokenomist shows circulating supply of 425.2M (42.5%) — [Tokenomist](https://tokenomist.ai/openeden/tokenomics).

**FF**
- Listing terms:
  - Supply 10B; HODLer 150M (1.5%); circulating at listing 2.34B (23.4%); Binance spot at 13:00 UTC on 2025-09-29.
  - Pairs: USDT, USDC, BNB, FDUSD, TRY — [CryptoNinjas](https://www.cryptoninjas.net/news/binance-unveils-150m-falcon-finance-airdrop-ahead-of-sept-29-listing/); [Falcon Docs](https://docs.falcon.finance/ff-token/ff-tokenomics).
- Price path (Binance):
  - First-hour VWAP $0.453; ATH $0.58 (first hour).
  - +30d $0.152; +90d $0.093; +180d $0.071. Current $0.1298.
- Current circulating supply is 3.14B — [CoinGecko](https://api.coingecko.com/api/v3/coins/falcon-finance-ff).

**Listings on other venues** (Bybit, OKX, Bitget, etc.) were not individually verified in this pass. The price series above is Binance-only.

### Inferences
- **The first print is not the open.** In HODLer-style listings the first 1–24 hours are extremely volatile: EDEN traded between $0.15 and $1.40 in its first hour. A comp should therefore state which "open" it uses. The first-hour VWAP vs the 24h VWAP changes opening FDV by up to ~35% for EDEN and ~30% for FF.
- **Only FF has partly recovered.** It is +83% from its Mar-2026 level, even though USDf supply is down.

### Gaps
- Exact first-trade timestamps and per-exchange opening prices on Bybit and OKX are not collected.
- The RESOLV circulating supply at listing (15.58%) should be confirmed against the original Binance announcement.

---

## Q4. Valuation ratios: FDV/TVL and FDV/fees

### Takeaway
- **FDV/TVL:** opening FDV/stablecoin supply clustered at **1.8x–5.5x**. Today, survivors trade at **~0.8–1.1x FDV/supply** (ENA, FF), while failed or shrunk protocols trade at a 0.1x–4x distorted ratio on tiny TVL.
- **FDV/fees:** FDV/annualized fees at TGE ranged from **~13x (RESOLV) and ~19x (ENA) up to ~70–90x (EDEN, USUAL)**.

### Cited Findings
Fees below are 30 days pre-TGE, annualized, from DefiLlama fees ([ethena](https://api.llama.fi/summary/fees/ethena?dataType=dailyFees), [usual](https://api.llama.fi/summary/fees/usual?dataType=dailyFees), [resolv](https://api.llama.fi/summary/fees/resolv?dataType=dailyFees), [openeden](https://api.llama.fi/summary/fees/openeden?dataType=dailyFees), [falcon-finance](https://api.llama.fi/summary/fees/falcon-finance?dataType=dailyFees)).

**Ratios at TGE**
- **ENA:** $8.55B FDV / $1.56B USDe = **5.5x**. Fees were $460M annualized → **18.6x FDV/fees**. DefiLlama "revenue" equalled fees at the time.
- **USUAL:** $1.45B / $375M = **3.9x**. Fees were $16.5M annualized → **~88x**; DefiLlama revenue was ~0 pre-TGE.
- **RESOLV:** $384M / $217M USR = **1.8x**, or 1.1x vs the $350M TVL including RLP. Fees were $29.5M annualized → **13x**. Protocol revenue was ~0; nearly all fees go to USR/RLP holders.
- **EDEN:** $843M / $235M USDO = **3.6x**, or ~1.6x if TBILL of ~$286M (Aug-2025) is added, with possible double counting. Fees were $11.7M annualized → **72x**. Revenue was $0.8M → ~1,000x.
- **FF:** $4.53B / $1.90B USDf = **2.4x**. There is no DefiLlama fee data before 2025-10-29.

**Ratios now (2026-09-28)**
- **ENA:** FDV $3.95B vs USDe $4.95B = **0.80x** (0.72x incl. USDtb).
  - Trailing-1y fees are $267M → **14.8x**.
  - DefiLlama shows trailing-1y "revenue" of only $2.7M, versus $333M all-time. This implies nearly all yield now goes to sUSDe holders or the methodology changed; treat it with caution.
- **USUAL:** FDV $60M (on 4B) or $29M (CoinGecko total) vs USD0 $547M = **0.05–0.11x**. Against the $88M DefiLlama TVL it is 0.3–0.7x.
  - 1y fees are $13.6M (**2–4x**); 1y revenue is $9.65M (**3–6x**).
- **FF:** FDV $1.30B vs USDf $1.21B = **1.07x**. DefiLlama 1y fees are $5.7M (→227x), with revenue shown as 0. **DefiLlama coverage of Falcon fees looks incomplete**: $5.7M/yr on $1.2–2B TVL is implausibly low for a yield product.
- **EDEN:** FDV $58.8M vs USDO $14.5M = ~4.0x. 1y fees are $3.5M (16.9x); 1y revenue is $0.64M (92x).
- **RESOLV:** FDV $18.6M vs USR ~$6M = ~3x. Fees have been ≈0 in the last 30 days (data ends 2026-09-03); trailing-1y fees are $10.8M, mostly pre-exploit.

### Inferences
- **Fee-yield vs points-yield products.** Tokens whose underlying fee yield was high relative to FDV at TGE — ENA and RESOLV at ~13–19x — were priced like fee businesses. RWA T-bill products (USUAL, EDEN) had thin margins and were priced at 70–90x fees. That premium compressed hardest: −93% to −96%.
- **Conservative anchor for a new TGE:** FDV of ~2–4x TVL, and ≤20–30x annualized protocol fees.

### Gaps
- There is no consistent, protocol-reported revenue series across all five. DefiLlama "revenue" definitions differ, especially for Ethena's reserve-fund and fee-switch treatment and for Falcon's missing coverage.
- Treat the Falcon and Ethena revenue multiples as low confidence.

---

## Q5. Airdrop design, $ per point, and implied airdrop APR

### Takeaway
Pre-TGE points airdrops equalled **5–10% of supply**. At opening prices they were worth ~$38M (RESOLV) to ~$428M (ENA). The implied farming APR ranged from **hundreds of % (Ethena S1, short 6-week campaign) to single digits (Resolv S1 base rate, 9-month campaign)**.

### Cited Findings

**Ethena (S1 "Shards")**
- **Allocation:** 750M ENA = 5% of 15B.
- **Vesting:**
  - Non-top wallets: 100% at TGE.
  - Top 2,000 wallets: 50% upfront, 50% vested over 6 months.
  - ~428M ENA was immediate and ~322M vested. Claim ratio was 96.3% (722M claimed) — [search summary of oneclick.fi case study (URL now 404)](https://www.oneclick.fi/blog/ethena-season-1-airdrop-case-study).
- **Totals:** 360B shards across 45,835 claimers were reported in the same aggregator summary — **unverified against a primary source**.
- **Rates and example:**
  - Rates were 5–20 shards per $ per day (holding USDe 5/day; locked Curve LP 20/day).
  - >90,000 users participated.
  - Example: a user who locked **$10,000 on day one received ~9,000 ENA** — [DL News](https://www.dlnews.com/articles/defi/ethena-500m-airdrop-leads-defi-project-to-plan-the-next-one/).
- **Seasons:** further seasons followed, e.g. S2 ended 2024-09-02 and S3 ended 2025-03-23 — [CoinGecko Learn](https://www.coingecko.com/learn/ethena-labs-airdrop-shard-campaign).
- **Computed values:**
  - 750M × $0.570 = **$428M airdrop value at open**.
  - If there were 360B shards: **~$0.00119 per shard**, i.e. 480 shards per ENA.
  - Using the DL News example, $1,000 locked from day one → ~900 ENA → $513 at open → **~51% over ~6 weeks ≈ ~450% simple APR**.
  - $1,000 held at the base 5x rate for 42 days → 210K shards → ~437 ENA → $249 → **~215% APR** (estimate relying on the 360B figure).

**Usual (Pills)**
- **Allocation:** 7.5% of TGE supply plus a 1% bonus for Pills collectors = **8.5%** — [CoinGecko Learn](https://www.coingecko.com/learn/what-is-usual-crypto-rwa-usual-airdrop); [Usual Docs](https://docs.usual.money/archive/usual-airdrop/pills-campaign-rules).
- **Unlocks (98.5% / 1.5% of wallets):**
  - 98.5% of wallets: instant claim with no conditions.
  - Top 1.5% of wallets: 10% instant, 90% either vested monthly from 2025-01-18 to 2025-06-18 or exited early via a DAO-treasury contribution that decreases linearly over 6 months.
- **Unlocks (share of supply):**
  - "Fair Unlock" 1.70% = 20% of 8.5%.
  - "Instant reward for biggest holders" 0.80% = 10% of 80% of 8.5%.
  - The blog gives the claim / spot date as **December 18, 11:00 UTC** — [Usual blog](https://usual.money/blog/airdrop-the-genesis-of-ownership).
- **Computed values:**
  - 8.5% × 4B = 340M USUAL → **~$123M at the TGE open ($0.362)**.
  - **~$331M at the 2024-12-18 Binance VWAP ($0.97).** USUAL made its ATH of $1.65 two days later.
- Total Pills were not found, so $ per Pill cannot be computed.

**Resolv (Points)**
- **Allocation:** S1 = **10% (100M RESOLV)**; S2 = 4% — [Tokenomist](https://tokenomist.ai/resolv); [ChainCatcher](https://www.chaincatcher.com/en/article/2180331).
- **Claim terms:**
  - Claimed as **stRESOLV (staked)**, with a 14-day unstake cooldown — [Bitget News](https://www.bitget.com/news/detail/12560604778982); [Resolv Docs](https://docs.resolv.xyz/litepaper/resolv-token/resolv-token-airdrop).
  - Claim windows: S1 May 27–Jun 27 (2025), S2 Sep 19–Oct 19, S3 Dec 16, 2025 – Jan 16, 2026.
  - Top wallets were subject to a short unlock schedule — [ChainCatcher](https://www.chaincatcher.com/en/article/2180331).
- **Example:** "a user with 1.67B points is eligible for 25,693 RESOLV" — [Bitget Academy](https://web3.bitget.com/en/academy/resolv-airdrop-guide-how-to-participate-and-claim-resolv-rewards) (via search summary). The same source mentions a small-holder floor (up to 250 RESOLV for wallets under 2M points).
- **Computed values (estimate):**
  - 1.54e-5 RESOLV per point → an implied ~6.5T total points if linear → **~$5.9e-6 per point** at the $0.384 open.
  - $1,000 in USR at the base 30 points/day for ~270 days → 8.1M points → ~125 RESOLV → **~$48 → ~6.4% APR**, before epoch boosts (+150% / +100% early) and the small-wallet floor.
  - By claim close (Jun 27) RESOLV was $0.158, so the realized value was ~60% lower.

**OpenEden (Bills)**
- **Allocation:** **7.5% (75M EDEN)**, distributed under the EDEN HODLers Bonus Mechanism (EHBM) — [PANews](https://www.panewslab.com/en/articles/85acffc7-f9f6-4fd9-be3d-aca2375d1b6a).
- **EHBM mechanics:**
  - A starting portion is claimable at TGE.
  - The remainder is subject to a holding window with linearly decreasing forfeiture, and forfeited tokens are redistributed. The reward pool base is 2.5M EDEN — [OpenEden EHBM](https://openeden.com/news/eden-hodlers-bonus-mechanism-token-reward-distribution/).
  - Wallets with under 100K Bills were ineligible. For wallets under 10M Bills, the starting portion was raised from 20% to 80%.
- **Other allocations:** Early Adopters 6% — [Tokenomist](https://tokenomist.ai/openeden/tokenomics).
- **Value:** 75M × $0.843 = **~$63M at open**, or ~$41M at the 24h VWAP.

**Falcon (Miles)**
- **Allocation:** "Community Airdrops & Launchpad Sale" = **8.3%**, covering Miles, the Buidlpad sale and Kaito Yap2Fly. The Miles S1 share is not disclosed — [Falcon Docs](https://docs.falcon.finance/ff-token/ff-tokenomics).
- **Claim terms:**
  - Claims ran Sep 29 – Dec 28, 2025.
  - Staking ≥50% of the claim at claim time gave a 1.1x bonus; staking ≥80% gave 1.25x.
  - sFF earned 160x Miles in week 1, then 80x — [Falcon](https://falcon.finance/news/falcon-finance-enters-its-next-chapter-with-the-launch-of-ff-token).

### Inferences
- **Headline APRs depend on campaign length.** Ethena S1 paid enormous returns because the campaign was short and supply at snapshot was small (~$1–1.5B). Resolv's 9-month S1 diluted the per-dollar reward; by the time of TGE its FDV/TVL was the lowest in the set.
- **Pricing points for a new protocol:** set the implied $/point using a conservative +1m price rather than the open. Post-listing declines of 50–85% within a month were typical in 2025.
- **Staked / forfeiture claims** (Resolv stRESOLV, OpenEden EHBM, Falcon staking bonus) did not prevent 85–97% declines by +6m.

### Gaps
- Total points are missing for Usual Pills, Falcon Miles and OpenEden Bills, and the Miles S1 FF allocation is also missing.
- Ethena's 360B total shards comes only from a secondary summary.
- Resolv's total points are inferred from a single example and may be non-linear because of the small-holder floor.

---

## Q6. Fundraising and TGE FDV vs last private valuation

### Takeaway
Only Ethena and Falcon have a disclosed valuation to compare against:
- **Ethena:** TGE FDV was ~**28.5x** its $300M Feb-2024 strategic round.
- **Falcon:** TGE FDV was ~**10–13x** its Buidlpad public-sale FDV of $350M / $450M.
- **Others:** Usual, Resolv and OpenEden did not disclose valuations.

### Cited Findings

**Ethena**
- $14M strategic round at a **$300M valuation**, closed mid-Feb 2024 as a SAFE with token warrants. It was co-led by Dragonfly and Maelstrom, and was oversubscribed at $50M+ — [The Block](https://www.theblock.co/post/277565/ethena-usde-stablecoin-funding-valuation-paypal-brevan-howard-others).
- Post-TGE, it ran a $100M private ENA sale (Dec 2024; investors included Franklin Templeton, Polychain, Pantera, Dragonfly and F-Prime) — [The Block](https://www.theblock.co/post/342955/ethena-100-million-usd-private-ena-token-sale-new-chain-institutional-product).
- Ratio: $8.55B open FDV / $300M = **28.5x**; at the peak FDV of $22.8B, **76x**.

**Usual**
- $7M strategic round (Apr 2024, led by IOSG and Kraken Ventures).
- $1.5M community round via Echo (Nov 2024).
- $10M Series A (Dec 2024, post-TGE, led by Binance Labs and Kraken Ventures).
- Valuations were not disclosed — [DefiLlama raises](https://api.llama.fi/protocol/usual-usd0); [Crowdfund Insider](https://www.crowdfundinsider.com/2024/12/234605-stablecoin-project-usual-raises-10m-series-a-led-by-binance-labs-kraken-ventures/).

**Resolv**
- $10M seed (Apr 2025, led by Cyber.Fund and Maven 11, with Coinbase Ventures, Arrington, Robot Ventures and others). The valuation was not disclosed — [DefiLlama raises](https://api.llama.fi/protocol/resolv-usr); [Lucidity Insights](https://lucidityinsights.com/news/resolv-labs-secures-10m-seed-round).
- Token split: investors 22.4% and team 26.7% of supply — [Tokenomist](https://tokenomist.ai/resolv).

**OpenEden**
- $5M raised per Tokenomist — [Tokenomist](https://tokenomist.ai/openeden/tokenomics). Tracxn describes a $5M round in May 2023 — [Tracxn](https://tracxn.com/d/companies/openeden/__YzjzJhgCfYNQUTd0vl-ZisyHgYcKevVnDBB96WqfEvM/funding-and-investors).
- Binance Labs invested in Sep 2024 (amount undisclosed) — [Binance Blog](https://www.binance.com/en/blog/ecosystem/binance-labs-invests-in-openeden-to-drive-the-growth-of-tokenized-realworld-assets-in-defi-1181406981252457328).
- A post-TGE strategic round in Dec 2025 (Ripple, Lightspeed Faction, Gate Ventures, FalconX, Anchorage and others) had its size and valuation undisclosed — [Blockhead](https://www.blockhead.co/2025/12/03/openeden-draws-new-backers-as-tokenized-treasury-demand-grows/).
- Investors hold 15.28% of supply.

**Falcon**
- $10M from World Liberty Financial (Jul 2025) — [DefiLlama raises](https://api.llama.fi/protocol/falcon-finance).
- Buidlpad community sale: **$4M at $350M or $450M FDV** depending on staking tier, 28x oversubscribed, 100% unlocked at TGE — [TipRanks](https://www.tipranks.com/news/newswire/falcon-finance-announced-ff-and-community-sale-on-buidlpad).
- $10M from M2 Capital and Cypher Capital (Oct 2025, post-TGE) — [Falcon](https://falcon.finance/news/m2-capital-and-cypher-capital-invest-10m-in-falcon-finance-to-accelerate-universal-collateralization-infrastructure).
- Token split: investors 4.5%; team 20% (1-year cliff, 3-year vest) — [Falcon](https://falcon.finance/news/introducing-ff-tokenomics).
- Ratio: $4.53B open FDV / $350M = **12.9x**, or 10.1x vs $450M. At +3m ($930M) the ratio was 2.1–2.7x. Now ($1.30B) it is **2.9–3.7x the Buidlpad FDV**.

### Inferences
- **Ratio compression after TGE.** Opening premiums of 10–30x over the last round collapsed. Ethena now trades at ~13x its $300M round. Falcon trades at ~3x its public-sale FDV.
- **Implication for a new stablecoin TGE:** a ~3–5x step-up over the last round is a more durable 6–12-month outcome than the 10–30x day-one step-up.

### Gaps
- Ethena's July-2023 seed round, reported elsewhere as ~$6M, was not verified in this pass.
- Valuations for Usual, Resolv, OpenEden and Falcon's WLFI / M2 rounds are undisclosed, so TGE FDV ÷ private valuation cannot be computed for them.
