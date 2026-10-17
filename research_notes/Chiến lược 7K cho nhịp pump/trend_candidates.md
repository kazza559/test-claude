# Trending narratives & candidate coins for the next leg up (Q4 2026 – Q1 2027), as of 2026-10-17

## Q1. Which sectors showed the strongest relative strength (RS) since the 2026-07-01 BTC low and during Aug–Oct, and which held up best in the current pullback?

### Takeaway
Since the July low, **privacy (ZEC), revenue/"fee-switch" DeFi (PUMP, ENA, UNI) and interop/L2 infra (ZRO, STRK, ARB)** led on a 90-day basis, while **AI/agents (NEAR)** led from the August higher low onward. During the pullback (BTC −6% from its 2026-09-21 close), **interop/modular infra (ZRO, TIA, STRK, PYTH, ZK), AI (NEAR, GRASS, WLD) and Base DeFi (AERO)** actually *rose*. Memes, perp-DEX tokens other than HYPE, RWA/stablecoin tokens and low-float 2025–26 L1s were the weakest.

### Cited Findings
**Method and data (pulled 2026-10-17, 03:23–03:29 UTC; all prices are HL mark prices at 03:23 UTC unless noted)**
- I pulled the universe of 178 live HL perps (mark, OI, funding, 24h volume) plus daily candles from 2026-05-01 for the 107 perps with OI ≥ $1.5M. Returns are measured from daily closes (UTC). The "since Jul 1" base is the 2026-07-01 close. The "since Aug low" base is the 2026-07-31 close (BTC's August low of $62,237 printed on 2026-08-01). The "pullback" base is the 2026-09-21 close. RS = (1+coin return)/(1+BTC return) − 1. Sector buckets are my own classification, aggregated as equal-weighted medians, so small n applies. Scripts and data are in `/tmp/claude-0/-home-user-test-claude/8ec8a334-85ed-54af-babc-62d7e4c0704b/scratchpad/research/trends/` (data/hl_rs_table.csv) — [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- BTC reference points from the HL candles: 2026-07-01 intraday low **$57,768**; August low **$62,237** (2026-08-01); pullback top **2026-09-21** (close $86,662, intraday high **$87,471**); mark **$81,499** on 2026-10-17. BTC returns: **+35.8%** since the Jul-1 close, **+29.7%** since the Jul-31 close, **+25.9%** over 90 days, **−6.0%** since the Sep-21 close — [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- **Sector medians, RS vs BTC (%)**, computed from HL candles on 2026-10-17 (n = number of coins) — [Hyperliquid info API](https://api.hyperliquid.xyz/info)

| Sector (n) | since Jul 1 | since Aug low | 90d | 30d | Pullback since 9/21 | OI-weighted pullback RS |
|---|---|---|---|---|---|---|
| BTC ecosystem (STX only, 1) | +68 | +111 | +83 | +40 | +17 | +17 |
| Privacy (ZEC, XMR, DASH, AZTEC, NIL; 5) | +32 | +22 | +31 | +1 | −0.3 | −14 (dragged by ZEC) |
| L2/interop/infra (ZRO, STRK, ARB, PYTH, ZK, W, OP, …; 13) | +15 | +36 | +27 | +28 | **+14.5** | **+51** |
| DeFi/revenue (ENA, UNI, AAVE, AERO, MET, CRV, …; 15) | +20 | +16 | +23 | +3 | −0.6 | +3 |
| AI/agents/compute (NEAR, VVV, GRASS, TAO, WLD, FET, VIRTUAL, …; 11) | −0.5 | +33 | +10 | +11 | **+6.3** | **+17** |
| L1 large-cap/ETF alts (23) | −1 | +4 | +4 | +5 | +2.7 | −6 |
| Perp DEX/exchange (HYPE, LIT, ASTER, JUP, …; 8) | −10 | +12 | +2 | −11 | −7.8 | −11 |
| Majors (BTC, ETH) | +5.5 | 0 | +1 | −3.5 | −3.6 | −3 |
| Memes/launchpad (PUMP, FARTCOIN, kPEPE, WIF, …; 11) | −15 | −4 | −5 | −3 | **−11.5** | +1 (PUMP) |
| New L1s 2025–26 (MON, MEGA, BERA, TIA; 4) | −20 | −4 | −15 | +9 | +2 | +17 (TIA) |
| RWA/stablecoin/payments (ONDO, XPL, WLFI, CC, SYRUP, PAXG, STBL, LINK; 8) | **−25** | −17 | **−17** | −8 | −3 | −3 |

- **Top individual RS leaders over 90 days** (RS vs BTC): NEAR +110%, MET +100%, ZRO +97%, ENA +97%, STRK +94%, NIL +90%, PUMP +83%, STX +83%, ARB +68%, ZEC +67%, UNI +65%, TIA/VVV +57%, AERO +54% — [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- **Coins that rose during the pullback** (2026-09-21 → 2026-10-17, while BTC fell 6%): ZRO **+67%**, TIA **+62%**, STRK **+61%**, GRASS **+52%**, PYTH +34%, AERO **+26%**, AZTEC +25%, NIL +22%, NEAR **+19%**, FIL +17%, WLD +14%, INJ +13%, PUMP +5%, AAVE +6%. Notable losers: LIT −32%, VVV −28%, ZEC −22%, FARTCOIN −22%, UNI −19%, ARB −16%, HYPE −15%, ETH −13%, SOL −12% — [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- **Watchlist RS vs BTC** (since Jul 1 / pullback): SOL −1% / −6%; HYPE −6% / −10%; LIT +14% / −28%; LINK +23% / −1%; BNB −3% / −4%. HYPE remains the perp-DEX narrative leader: CoinGecko lists its ATH as **$97.96 on 2026-09-23**, with the price −18% from that ATH on 2026-10-17 — [Hyperliquid info API](https://api.hyperliquid.xyz/info); [CoinGecko markets API](https://api.coingecko.com/api/v3/coins/markets)
- **CoinGecko 24h category moves (2026-10-17 ~03:29 UTC):** Modular Blockchain **+15.6%**, Restaking +3.2%, BTCfi +1.8%; Privacy −3.3%, Privacy Coins −4.3%, Zero Knowledge −5.2%, Quantum-Resistant −5.6%, **Prediction Markets −7.4%**, AI −2.5%, AI Agents −3.6%. Category sizes: Privacy $55.2B, RWA $76.2B, Perpetuals $24.0B, AI $24.6B, x402 Ecosystem $10.45B, Prediction Markets $6.44B, AI Agents $3.51B — [CoinGecko categories API](https://api.coingecko.com/api/v3/coins/categories)
- **CoinGecko trending (2026-10-17):** coins DACITY, QTC, HYPE, NEAR, LIT, UNI, BTC, SOL, QNT, AERO, INJ, JUP, AVAX, CC, ENA; categories Binance Launchpad, Data Availability, Derivatives, Quantum-Resistant, Binance Launchpool, Perpetuals — [CoinGecko trending API](https://api.coingecko.com/api/v3/search/trending)
- **HL funding context:** HL funding includes a fixed interest component (0.01%/8h ≈ **+11% APR**), so "+11% APR" means neutral positioning. On 2026-10-17, most alts sat at this baseline. Shorts were paying (crowded shorts) on ARB **−35% APR**, LIT −13%, JUP −10%, MON −9%, W −27%, MET −25% and BERA −95% — [Hyperliquid funding docs](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/funding); [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- **Market backdrop (secondary sources, early Oct 2026):** no broad altseason yet. The altcoin-season index is cited at 35–59, against the 75 threshold. BTC dominance is about 57%. Prices fell in early October on rising bond yields and inflation worries — [Bitcoin Foundation](https://bitcoinfoundation.org/news/altcoins/understanding-altcoin-season-in-2026-what-are-altcoin-market-cycles/); [CoinCentral](https://coincentral.com/best-altcoins-to-watch-in-october-2026-solana-chainlink-and-xrp-top-the-list); [Tangem](https://tangem.com/en/blog/post/what-is-altseason/)

### Inferences
- The pullback leaders are mostly **deeply beaten-down 2024-vintage infra tokens** (ZRO −74%, TIA −96%, STRK −98%, PYTH −93% and GRASS −84% from their ATHs per CoinGecko). This looks like rotation and mean reversion, plus probable short-covering, into "cheap beta" as ZEC, UNI and LIT cooled. It is a real RS signal, but a fragile one: STRK already gave back 32% in 7 days.
- NEAR is the cleanest "leader that holds up": top-3 90-day RS, it rose in the pullback, and it has deep liquidity (OI $314M, 24h volume $174M).
- If BTC resumes up from about $81K, the likely leaders are the coins that showed pullback RS *and* have liquidity (NEAR, ZRO, AERO, TIA). High-beta laggards (PUMP, ZEC, HYPE, UNI, ENA) could snap back harder but are less predictable.

### Gaps
- Kaito, LunarCrush and Artemis sector indices were not accessed (authentication/paywall), so mindshare evidence rests on CoinGecko trending only.
- The CoinGecko categories API only gives 24h change, so multi-week sector RS is my own HL-perp-based construction. It is not an official index.

## Q2. Which narratives emerged or strengthened in 2026, and which are still early vs already crowded?

### Takeaway
2026's dominant winners were **privacy (ZEC)**, now mature and crowded, and **HL/HIP-3 tokenized-equity perps**, where HL activity hit new highs but the token beneficiary is mainly HYPE. Strengthening now: **AI-agent/intents infra (NEAR, with a spot ETF since 2026-09-29)** and the **interop/modular infra rotation (ZRO, TIA)**. Revenue/buyback tokens are mid-stage with mixed fundamentals. Prediction markets are early, but mostly a TGE/airdrop play with no liquid HL tokens. **RWA/stablecoin chains show strong activity but weak tokens.**

### Cited Findings
- **Privacy/ZEC (crowded, late-stage):** ZEC rose about 2,400% over the year to September 2026, from the $40s to above $1,100, and climbed from about #82 to #10 by market cap — [BIT Knowledge Hub](https://www.bit.com/knowledge-hub/zcash-rally-september-2026). Grayscale's spot ZEC ETF (ZCSH) launched 2026-08-25. ZEC then fell about 23% from its 2026-09-27 peak of $1,697 to about $1,335 in early October on Grayscale ETF outflows (per search-result summaries) — [Coin-Turk](https://en.coin-turk.com/zcash-surges-215yuzde-to-1500-driven-by-etf-inflows-and-nu7-mainnet-upgrade/); [investingLive](https://investinglive.com/cryptocurrency/zcash-pares-losses-amid-improved-risk-sentiment-as-focus-shifts-to-us-cpi-and-winklevoss-etf-approval/). On 2026-10-17, ZEC had HL OI of **$534M**, the 5th-largest of any HL perp, and was −21% over 30 days — [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- **AI agents/intents (strengthening):** Bitwise's spot NEAR ETF began trading on NYSE Arca on **2026-09-29** under ticker **NRR** (0.75% fee, intends to stake). Bitwise cites NEAR Intents volume of **>$32B vs <$1B a year earlier** — [Cointelegraph](https://cointelegraph.com/news/bitwise-launches-first-us-spot-near-etf-after-tokens-recent-surge); [Yellow](https://yellow.com/news/bitwise-near-etf-management-fee). Earlier 2026 NEAR legs (Feb–Mar NEARCON "User-Owned AI"; May–June squeeze plus AI rotation) — [Whale Alert](https://whale-alert.io/stories/d4b801f6f8d413/NEAR-Protocol-Rises-54-in-a-Week-on-Short-Squeeze-AI-Rotation-and-Growing-Institutional-Interest). The CoinGecko "AI Agents" category's top 3 are Venice (VVV), FET and VIRTUAL. VVV printed an ATH of **$34.53 on 2026-09-21** and is +1,403% over 1 year — [CoinGecko categories API](https://api.coingecko.com/api/v3/coins/categories); [CoinGecko markets API](https://api.coingecko.com/api/v3/coins/markets)
- **HL HIP-3 tokenized stocks/commodities/pre-IPO perps (strongest activity growth):** live HIP-3 OI on 2026-10-17 was **~$3.85B**. Breakdown: xyz dex $3.76B across 115 markets (top: SKHX $377M, SP500 $340M, XYZ100 $317M, GOLD $294M, SKHY $190M, BRENTOIL $187M, SILVER $160M, MU $158M); io dex $67.6M (pre-IPO perps **ANTH $40.9M**, OAI $7.0M, plus SNDK and NBIS); para $15.2M; mkts $9.4M — [Hyperliquid info API (perpDexs + metaAndAssetCtxs per dex)](https://api.hyperliquid.xyz/info). That compares with a reported record of about $2.38B around April 2026 — [CoinMarketCap Academy](https://coinmarketcap.com/academy/article/hyperliquid-tokenized-equity-open-interest-tops-dollar2-billion) — and $1.74B in March 2026 — [The Block](https://www.theblock.co/post/394820/hyperliquid-hip-3-open-interest-jumps)
- **Perp-DEX tokens other than HYPE are lagging:** ASTER RS −18% since Jul 1 (35% circulating, FDV $5.50B); LIT RS −28% in the pullback; Lighter Perps 30d revenue $2.8M (−16% vs the prior 30d), while Hyperliquid Perps 30d revenue was $69.0M (−16%) — [Hyperliquid info API](https://api.hyperliquid.xyz/info); [CoinGecko markets API](https://api.coingecko.com/api/v3/coins/markets); [DefiLlama revenue API](https://api.llama.fi/overview/fees?excludeTotalDataChart=true&dataType=dailyRevenue). Derivatives-category revenue was **+42%** 30d/30d, largely from a new protocol "Papertrade" ($55.2M of revenue in its first 7 days on DefiLlama) — [DefiLlama revenue API](https://api.llama.fi/overview/fees?excludeTotalDataChart=true&dataType=dailyRevenue)
- **Revenue/buyback tokens (mid-stage, mixed fundamentals):** pump.fun 30d revenue **$44.4M (+30%)**, holders revenue $30.5M (+21%); Uniswap V3 holders revenue $9.6M (**−39%**); Aerodrome Slipstream holders revenue $6.6M (**−50%**); Sky Lending holders revenue $5.9M (+42%); Chainlink Staking $5.5M (+24%); NEAR Intents holders revenue $2.5M (**+116%**) — [DefiLlama holders-revenue API](https://api.llama.fi/overview/fees?excludeTotalDataChart=true&dataType=dailyHoldersRevenue). SKY printed an ATH of $0.10087 on 2026-10-05 — [CoinGecko markets API](https://api.coingecko.com/api/v3/coins/markets)
- **Prediction markets (early; TGE-driven, no liquid tokens on HL):** CoinGecko Prediction Markets category $6.44B (top 3: rain, drift-protocol, dexsport), −7.4% in 24h. Polymarket International 30d revenue $14.4M (−21%) — [CoinGecko categories API](https://api.coingecko.com/api/v3/coins/categories); [DefiLlama revenue API](https://api.llama.fi/overview/fees?excludeTotalDataChart=true&dataType=dailyRevenue). Predict.fun is the near-term token event (see Q4).
- **RWA/stablecoins/payments (activity strong, tokens weak):** Tether 30d revenue $521.6M (+7%), Circle $211.9M (+8%), stablecoin-issuer category +8% 30d/30d — [DefiLlama revenue API](https://api.llama.fi/overview/fees?excludeTotalDataChart=true&dataType=dailyRevenue). The RWA/stablecoin token basket is the worst sector by RS since Jul 1 (−25% median). Examples: XPL −95% from ATH (45% circulating), STABLE 27% circulating (FDV $2.60B), CC −46% RS since Jul 1 — [Hyperliquid info API](https://api.hyperliquid.xyz/info); [CoinGecko markets API](https://api.coingecko.com/api/v3/coins/markets)
- **Base ecosystem (optionality, long-dated):** AERO is CoinGecko-trending. Polymarket gives "Base launches a token" **8% by 2026-12-31, 20% by 2027-06-30, 42% by 2027-12-31** — [Polymarket Gamma API](https://gamma-api.polymarket.com/events)
- **Interop "institutional rails":** LayerZero plans a new L1 called "Zero" for institutional markets, with ARK Invest and Citadel Securities support, targeted for **fall 2026**. A launch was not confirmed as of the latest sources — [Whale Alert](https://whale-alert.io/stories/af880117485a3f/LayerZero-unveils-Zero-Layer-1-with-Citadel-ICE-and-Google-Cloud-ZRO-jumps-40-to-250); [TradingView](https://www.tradingview.com/ideas/zero/)
- **Emerging, under-researched:** "Quantum-Resistant" is a CoinGecko trending category ($21.5B market cap, −5.6% 24h), and QNT is trending — [CoinGecko categories API](https://api.coingecko.com/api/v3/coins/categories); [CoinGecko trending API](https://api.coingecko.com/api/v3/search/trending)

### Inferences
- **Early:** prediction-market TGEs (Predict.fun), perp-DEX TGEs (Variational, Extended), Base token optionality, LayerZero "Zero" launch, quantum-resistance theme.
- **Mid:** AI/intents (NEAR has institutional validation but has already run +165% in 90d); revenue/buyback DeFi; modular/DA rotation (TIA).
- **Crowded/late:** ZEC/privacy (top-10 market cap, OI $534M, ETF outflows); HYPE/perp-DEX (narrative leader, but FDV $76.4B and 23% circulating); new L1s and memes are already in distribution.

### Gaps
- No Kaito/LunarCrush mindshare data. I could not identify "Papertrade" (a new derivatives protocol earning about $5M/day on DefiLlama), StonkFun ($20.6M 30d revenue, +51%) or Collector Crypt ($16.6M, +76%). These could hide TGE or token opportunities.
- I did not check whether Polymarket itself has announced a token: no "Polymarket token" market surfaced in my Gamma API scan.

## Q3. Candidate shortlist: 10 coins in 4 narratives, plus a perp-DEX/HIP-3 leader note (watchlist excluded)

### Takeaway
The best-supported candidates are **NEAR** (AI/intents leader with an ETF catalyst, liquid), **ZRO** and **TIA** (strongest pullback RS, interop/modular rotation), **PUMP** (real revenue and buybacks, deep HL liquidity, but unlock overhang), **ZEC** (dated NU7 catalyst, but crowded), and **AERO** (Base proxy that held up). VVV, GRASS, ENA and XMR are secondary or alternates. All are tradeable as HL perps with OI ≥ $10M; GRASS and AERO have thin 24h volume.

### Cited Findings
**Snapshot table, 2026-10-17.** Price, OI, volume, leverage and returns come from HL at 03:23 UTC. Market cap, FDV and circulating % come from CoinGecko at 03:29 UTC. Returns are vs the stated base close, with RS vs BTC in brackets — [Hyperliquid info API](https://api.hyperliquid.xyz/info); [CoinGecko markets API](https://api.coingecko.com/api/v3/coins/markets)

| Narrative | HL ticker | Price | Mcap | FDV | Circ % | HL OI | 24h vol | HL max lev | Since Jul 1 (RS) | Since Aug low (RS) | 90d (RS) | Pullback since 9/21 (RS) | From post-Jul high |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AI/intents | **NEAR** | 5.078 | $6.66B | ≈mcap* | ~100%* | $314M | $174M | 10x | +181% (+107) | +205% (+135) | +165% (+110) | **+19% (+26)** | −16% |
| AI/privacy-AI | **VVV** | 23.01 | $1.11B | $1.87B | 60% | $65M | $11M | 3x | +73% (+27) | +95% (+50) | +97% (+57) | −28% (−24) | −34% |
| AI data/DePIN | **GRASS** | 0.6309 | $441M | $630M | 70% | $30M | $2.4M | 3x | +35% (−1) | +101% (+55) | +76% (+40) | **+52% (+61)** | −29% |
| Interop | **ZRO** | 1.9635 | $785M | $1.96B | **40%** | $72M | $31M | 5x | +141% (+78) | +164% (+104) | +149% (+97) | **+67% (+77)** | −21% |
| Modular/DA | **TIA** | 0.7118 | $724M | $870M | 83% | $17M | $26M | 5x | +100% (+47) | +122% (+71) | +97% (+57) | **+62% (+72)** | −3% |
| Revenue/buyback | **PUMP** | 0.004608 | $2.13B | $3.80B | 56% | $174M | $115M | 10x | +233% (+145) | +123% (+72) | +130% (+83) | +5% (+12) | −32% |
| Base DeFi/revenue | **AERO** | 0.8802 | $885M | $1.77B | 50% | $34M | $6.5M | 3x | +87% (+38) | +112% (+63) | +94% (+54) | **+26% (+34)** | −11% |
| DeFi/stablecoin yield | **ENA** | 0.1981 | $2.66B | $2.98B | 89% | $98M | $38M | 10x | +178% (+105) | +147% (+90) | +148% (+97) | −7% (−1) | −33% |
| Privacy | **ZEC** | 1,151.2 | $19.57B | ≈mcap* | ~100%* | $534M | $299M | 10x | +176% (+103) | +152% (+94) | +110% (+67) | −22% (−17) | −32% |
| Privacy (defensive) | **XMR** | 555.95 | $10.46B | =mcap | 100% | $65M | $22M | 5x | +80% (+32) | +55% (+20) | +65% (+31) | −6% (0) | −12% |
| *Leader, watchlist* | HYPE | 79.91 | $17.79B | $76.40B | 23% | $1,588M | $314M | 10x | +28% (−6) | +52% (+17) | +31% (+4) | −15% (−10) | −18% |
| *Benchmark* | BTC | 81,499 | – | – | – | $3,354M | $2,841M | 40x | +36% | +30% | +26% | −6% | −7% |

\*CoinGecko reports FDV equal to market cap for NEAR (inflationary, no max supply) and ZEC (21M cap). Treat as approximate. Funding on 2026-10-17 was at the neutral ~+11% APR baseline for all of the above except ENA (+4%) and HYPE (+7.6%) — [Hyperliquid info API](https://api.hyperliquid.xyz/info)

#### Narrative A: AI agents / intents / "user-owned AI"
- **NEAR (HL: NEAR)**: L1 positioned as AI-agent and chain-abstraction infrastructure, via NEAR Intents.
  - Why now: Bitwise spot NEAR ETF (NRR) has traded since **2026-09-29**. NEAR Intents volume is >$32B vs <$1B a year earlier — [Cointelegraph](https://cointelegraph.com/news/bitwise-launches-first-us-spot-near-etf-after-tokens-recent-surge). NEAR Intents holders revenue was $2.5M over 30d (+116%) — [DefiLlama](https://api.llama.fi/overview/fees?excludeTotalDataChart=true&dataType=dailyHoldersRevenue). NEAR is CoinGecko-trending, and Data Availability (NEAR is the top constituent) is a trending category — [CoinGecko trending](https://api.coingecko.com/api/v3/search/trending).
  - Levels: one analyst read put support at **$4.70/$4.50** and resistance at **$5.30** around the ETF launch — [CoinGape](https://coingape.com/markets/near-protocol-price-prediction-after-bitwise-launches-first-spot-etf/).
  - Bitwise's own long-range scenarios (2030: bear $1.63, base $155.85, max $562.81) are issuer marketing, not evidence — [BeInCrypto](https://beincrypto.com/bitwise-near-etf-launch-price-targets/).
  - 1y +128%; −75% from its 2022 ATH ($20.44) — [CoinGecko](https://api.coingecko.com/api/v3/coins/markets).
- **VVV (HL: VVV)**: Venice, a private/uncensored AI platform token. ATH **$34.53 on 2026-09-21**, now −33% from it; 1y +1,403% — [CoinGecko](https://api.coingecko.com/api/v3/coins/markets). DefiLlama tracks Venice holders revenue at $1.0M per 30d (+20%) — [DefiLlama](https://api.llama.fi/overview/fees?excludeTotalDataChart=true&dataType=dailyHoldersRevenue). The top constituent of CoinGecko's AI Agents category — [CoinGecko categories](https://api.coingecko.com/api/v3/coins/categories). Catalyst date: not found (see Gaps).
- **GRASS (HL: GRASS)**: AI training-data/DePIN network. Strongest pullback RS in AI (+61%), but HL 24h volume is only $2.4M against $30M OI, so it is crowded and illiquid; max leverage 3x — [Hyperliquid info API](https://api.hyperliquid.xyz/info). Catalyst: not found.

#### Narrative B: Interop & modular-infra rotation ("institutional rails")
- **ZRO (HL: ZRO)**: LayerZero, the cross-chain messaging protocol.
  - Why now: the "Zero" institutional L1 (ARK Invest, Citadel Securities; headline also cites ICE and Google Cloud) is targeted for **fall 2026**. The launch is not yet confirmed — [Whale Alert](https://whale-alert.io/stories/af880117485a3f/LayerZero-unveils-Zero-Layer-1-with-Citadel-ICE-and-Google-Cloud-ZRO-jumps-40-to-250); [TradingView](https://www.tradingview.com/ideas/zero/).
  - Best pullback performer among liquid alts (+67%), but −9% on 2026-10-17 alone — [Hyperliquid info API](https://api.hyperliquid.xyz/info).
  - Risks:
    - Only **40% circulating** (FDV $1.96B vs $785M market cap) — [CoinGecko](https://api.coingecko.com/api/v3/coins/markets).
    - KelpDAO rsETH bridge exploit on 2026-04-18/19 (~$292M) hit LayerZero's reputation — [ThreatCluster](https://threatcluster.io/cluster/layerzero-faces-fallout-from-kelpdao-exploit-zro-token-drops-6ed5a96d).
    - Alameda-linked wallets moved 7.93M ZRO (~$15.3M) to Wintermute in April 2026 — [CoinMarketCap AI updates](https://www.coinmarketcap.com/cmc-ai/layerzero/latest-updates/).
    - Data conflict: Trust Wallet lists ZRO at $2.01 with a "$1.91B market cap" on 2026-10-10, which is closer to CoinGecko's FDV than to its market cap — [Trust Wallet](https://trustwallet.com/vi/price/layerzero).
- **TIA (HL: TIA)**: Celestia, the modular data-availability layer. HL 24h change **+17.7%** on 2026-10-17. Trading within 3% of its post-July high, with +62% in the pullback — [Hyperliquid info API](https://api.hyperliquid.xyz/info). CoinGecko 7d +45%, 30d +103%; "Modular Blockchain" category +15.6% in 24h — [CoinGecko](https://api.coingecko.com/api/v3/coins/categories). Earlier 2026 catalysts: a Commonware chain on Celestia promising 10x faster blocks drove a ~40% bounce from about $0.295 in June 2026, and TIA hit a 90-day high on 2026-05-25 — [MEXC news (syndicated)](https://www.mexc.com/news/1165308); [Baselight](https://baselight.app/daily-insights/crypto/2026-05-27/tia-usd-90d-high-volume-surge-may25). The October driver is unidentified. −96% from its 2024 ATH.

#### Narrative C: Revenue, buybacks & Base DeFi
- **PUMP (HL: PUMP)**: pump.fun, the Solana memecoin launchpad with buyback-and-burn.
  - Revenue: 30d revenue $44.4M (+30%), holders revenue $30.5M (+21%), 1y revenue $325M — [DefiLlama](https://api.llama.fi/overview/fees?excludeTotalDataChart=true&dataType=dailyRevenue).
  - Buyback policy: started at 100% of revenue, then moved to a 50/50 split in April 2026 — [Brainsum/analysis](https://san-1510.aid.brainsum.com/news/analysis/pump-absorbs-148mn-unlock-supply-risk-lingers). The Block reported a $370M PUMP burn and a commitment of 50% of future revenue to buyback-burn — [The Block](https://www.theblock.co/post/399288/pump-fun-burns-370-million-pump). About $350M had been spent on buybacks since July 2025 — [Techleap](https://finder.techleap.nl/news/feed/pump-fun-spends-350m-on-buybacks-but-token-still-81-below-peak).
  - Unlocks: the first team/investor unlock was ~82.5B PUMP (~8.25% of total, ~20% of circulating) on **2026-07-12/13** — [KuCoin/Odaily](https://www.kucoin.com/news/flash/pump-faces-1-25m-unlock-pressure-amid-shrinking-buybacks). Insiders kept ~92% of the July unlock — [4Pillars](https://research.4pillars.io/en/data/content/pump-insiders-kept-92-of-the-july-unlock). The next tranche, **6.875B PUMP** (team 4.17B + investors 2.71B), unlocked on **2026-08-12** — [KuCoin/CryptoBriefing](https://www.kucoin.com/news/flash/pump-fun-faces-pressure-as-6-875b-pump-unlock-approaches). That tranche is worth ~$31.7M at the 2026-10-17 price (~1.5% of market cap; my calculation).
  - Polymarket "Pump.fun airdrop by 2026-12-31": **16%** — [Polymarket Gamma API](https://gamma-api.polymarket.com/events).
  - Liquidity: third-largest alt OI on HL ($174M).
- **AERO (HL: AERO)**: Aerodrome, the dominant Base DEX (ve(3,3) model). +26% in the pullback; CoinGecko-trending — [Hyperliquid info API](https://api.hyperliquid.xyz/info); [CoinGecko trending](https://api.coingecko.com/api/v3/search/trending). Fundamentals are weakening: Aerodrome Slipstream holders revenue $6.6M over 30d (−50%) — [DefiLlama](https://api.llama.fi/overview/fees?excludeTotalDataChart=true&dataType=dailyHoldersRevenue). Optionality: Base token odds 8% by end-2026 and 42% by end-2027 — [Polymarket Gamma API](https://gamma-api.polymarket.com/events). 50% circulating; HL max leverage 3x; volume only $6.5M per 24h.
- **ENA (HL: ENA)**: Ethena (USDe synthetic dollar). +148% over 90d, but −33% from its post-July high and −7% in the pullback; 89% circulating, so low remaining unlock overhang — [Hyperliquid info API](https://api.hyperliquid.xyz/info); [CoinGecko](https://api.coingecko.com/api/v3/coins/markets). CoinGecko-trending. Catalyst: not found.

#### Narrative D: Privacy
- **ZEC (HL: ZEC)**: Zcash, the 2026 narrative leader.
  - Dated catalysts:
    - NU7 testnet activation on 2026-10-04 to 10-06 (25-second blocks, fee-sustainability mechanism) — [Pluang](https://pluang.com/en/news-feed/zcash-nu7-aktif-di-testnet-dengan-blok-25-detik).
    - **Mainnet go/no-go decision around 2026-10-20**; **mainnet activation targeted for 2026-11-05** — [Pluang](https://pluang.com/en/news-feed/zcash-tetapkan-target-nu7-mainnet-upgrade-november-5); [Crypto.com](https://crypto.com/en/market-updates/best-altcoins-to-watch-october-2026).
    - **Winklevoss spot ZEC ETF filing on 2026-10-06** (approval would be a second catalyst) — [investingLive](https://investinglive.com/cryptocurrency/zcash-pares-losses-amid-improved-risk-sentiment-as-focus-shifts-to-us-cpi-and-winklevoss-etf-approval/).
  - Risks:
    - Crowding: OI $534M and HL 24h change −5.9% on 2026-10-17.
    - ETF outflows drove the fall from the $1,697 high.
    - NU7 disables v4 transactions, which affects old Sprout funds.
    - MEXC flags that the Grayscale application decision and a fragile alt market are risks — [MEXC analysis](https://www.mexc.com/crypto-pulse/article/zec-is-up-1-200-here-s-exactly-why-zcash-exploded-in-2026-114408).
  - No token unlocks; PoW issuance only.
- **XMR (HL: XMR)**: Monero, a lower-beta privacy alternative. ATH **$797.73 on 2026-01-14**; flat RS in the pullback, +7% over 7d — [CoinGecko](https://api.coingecko.com/api/v3/coins/markets); [Hyperliquid info API](https://api.hyperliquid.xyz/info). Catalyst: not found.

#### Perp DEX / HIP-3 (leader is on the watchlist)
- HYPE is the leader (ATH 2026-09-23), with live HIP-3 OI of ~$3.85B, a new high vs the ~$2.38B record reported around April 2026 — see Q2. No non-watchlist perp-DEX token shows RS: ASTER −18%, JUP −5%, APEX −36% and DYDX −37% RS since Jul 1 — [Hyperliquid info API](https://api.hyperliquid.xyz/info). Exposure to this narrative is better taken through HYPE (watchlist) or upcoming perp-DEX TGEs (Variational, Extended; see Q4).

### Inferences
**Aggressive vs conservative takes.** These are opinions, not advice. Leverage figures assume the trader's ~$6.4K alt sleeve.
- **NEAR**:
  - Aggressive: core trend long; add on dips into $4.5–4.7 and invalidate on a daily close below ~$4.2 (my level).
  - Conservative: small size only after a retest holds, because it is +165% in 90d and ETF flows can reverse.
- **ZRO**:
  - Aggressive: momentum long into the "Zero" launch with a tight stop. It had the best pullback RS among liquid alts.
  - Conservative: wait until the unlock calendar is verified (40% circulating) and a Zero launch date is confirmed. "Sell the news" is likely.
- **TIA**:
  - Aggressive: breakout momentum while it holds near highs; small size, because OI is only $17M and it just printed a +17.7% day.
  - Conservative: skip until the October driver is known.
- **PUMP**:
  - Aggressive: high-beta revenue play; buy pullbacks while revenue grows; watch the ~12th-of-month tranches and buyback size.
  - Conservative: avoid, because insiders hold a large share, it is −32% from its post-July high and 7d momentum is negative.
- **AERO**:
  - Aggressive: Base-beta with pullback RS, but 3x max leverage and thin volume.
  - Conservative: avoid, because revenue is −50% m/m.
- **ZEC**:
  - Aggressive: event trade only. Dip-buy ahead of the ~Oct 20 decision and Nov 5 activation, then take profit into the event.
  - Conservative: do not chase. It is the most crowded alt on HL outside HYPE and SOL, and ETF flows are negative.
- **ENA**:
  - Aggressive: high-beta DeFi rebound with low unlock overhang.
  - Conservative: wait for a catalyst.
- **XMR**: conservative privacy beta with the lowest drawdown in the group.
- **VVV and GRASS**: aggressive-only, small, low-leverage satellites. Both cap at 3x on HL, and GRASS is illiquid.

**Ranking for a 1–3 coin add.**
1. NEAR (liquidity, leadership and a catalyst).
2. ZRO or TIA (pullback RS, with higher risk).
3. PUMP or ZEC as a tactical high-beta snapback/event trade.

### Gaps
- **Unlock calendars could not be verified.** DefiLlama emissions returned 402/403, and Tokenomist needs a key. From pre-2026 knowledge, unverified and to be checked on Tokenomist before trading:
  - ZRO: monthly unlocks of ~25.7M on the 20th through mid-2027 (≈$50M/month).
  - ARB: 92.65M on the 16th through Mar 2027.
  - STRK: 127M on the 15th through Mar 2027.
  - ENA: ~172M on the 2nd.
  - NEAR: ~2.5%/yr inflation.
  - TIA: remaining core-contributor vesting into late 2026.
  - PUMP: monthly ~6.9B tranches after Aug 2026 are inferred, not confirmed.
- Catalysts with dates for VVV, GRASS, ENA, XMR, AERO and TIA's October move were not found.
- 6-month unlock totals per coin are not available.

## Q4. Upcoming TGEs, airdrops and points programs (Q4 2026 – Q1 2027)

### Takeaway
The only near-term, high-probability TGE is **Predict.fun** (Polymarket: 78% by 2026-11-30, 90% by year-end; FDV > $1B 43%). Perp-DEX TGEs **Variational** (FDV > $1B 58%, market runs to 2027) and **Extended** (FDV > $150M 66%, resolves by 2027-01-01) are next. Big-brand tokens (MetaMask, Base, OpenSea, Tempo, Arc) are unlikely before 2027, and an HL "season 2" airdrop is priced at only 8% for 2026.

### Cited Findings
All odds below are Polymarket "Yes" prices from the Gamma API on 2026-10-17 — [Polymarket Gamma API](https://gamma-api.polymarket.com/events)
- **Predict.fun** (prediction market):
  - Token launch by 2026-10-31 **20%**, by 11-30 **78%**, by 12-31 **90%**, by 2027-03-31 94%.
  - FDV one day after launch: >$300M 89%, >$500M 79%, >$800M 55%, **>$1B 43%**, >$1.5B 26%, >$2B 21%. Market volume $7.0M.
  - A "Soon" teaser showing a coin marked "P" was posted on X on **2026-10-06**. A Predict Points program is live, but no airdrop, snapshot or allocation has been announced, and the docs do not say points carry token entitlement — [Bitrue (2026-10-07)](https://www.bitrue.com/blog/predict-fun-token-launch); [Bitrue airdrop guide](https://www.bitrue.com/blog/predict-fun-airdrop).
  - Earlier estimates put the season-1 airdrop at 5–20% of supply (speculative) — [Odaily](https://www.odaily.news/en/post/5213277).
- **Variational** (perp DEX), FDV one day after launch: >$300M 93%, >$500M 86%, >$800M 72%, **>$1B 58%**, >$2B 28%, >$3B 14% (market ends 2028-01-01).
- **Extended** (perp DEX), FDV one day after launch: >$150M **66%**, >$300M 38%, >$500M 20%, >$1B 5% (market ends 2027-01-01, implying an expected launch around year-end).
- **Ink** (Kraken L2): FDV >$100M 28%, >$1B 8% (ends 2027-01-01). **Puffpaw**: FDV >$50M 25%, >$100M 22%. **StandX**: about 1% across brackets (launch unlikely by the deadline).
- **Big brands:**
  - MetaMask token by 2026-12-31: **8%** ($8.7M volume).
  - Base token: **8%** by 2026-12-31, **20%** by 2027-06-30, **42%** by 2027-12-31. Base FDV markets: >$1B 38%, >$5B 28%, >$10B 16%.
  - OpenSea token by 2026-12-31: 8%.
  - Tempo (Stripe): 4% by end-2026, 16% by end-2027.
  - Arc (Circle): 8% by end-2026, **42% by 2027-06-30**, 71% by end-2027.
  - fomo.family: 4% / 20%. Abstract: about 4%.
- **Airdrops:** **Hyperliquid airdrop** 8% by 2026-12-31, 24% by 2027-06-30, 48% by 2027-12-31. **MegaETH airdrop** 12% by 2026-12-31. **Pump.fun airdrop** 16% by 2026-12-31.
- **Pre-IPO and equity perps on HL:** io:ANTH (Anthropic) OI $40.9M, io:OAI $7.0M — [Hyperliquid info API](https://api.hyperliquid.xyz/info). Related Polymarket markets: "Largest IPO in 2026" SpaceX 64%, Anthropic 36%; "No OpenAI IPO by 2026-12-31" 97% — [Polymarket Gamma API](https://gamma-api.polymarket.com/events)

### Inferences
- For a small HL account, the realistic angle is **trading new listings after launch**: HL usually lists hyped TGEs (often first as pre-launch/hyperps). Farming is also possible: Predict.fun points could be farmed cheaply before a likely November TGE, but there is no confirmed entitlement.
- Polymarket's Variational/Extended FDV distributions give a rough "fair launch FDV" anchor for fading or buying the first days of trading.

### Gaps
- Points-program details and timing for Variational and Extended were not researched.
- No Polymarket market was found for a Polymarket (POLY) token, Kalshi, Phantom or Backpack in this scan.
- No source gives dates for HL-listed pre-market (hyperp) launches.

## Q5. Crowded coins/narratives and unlock overhang to avoid

### Takeaway
Avoid **low-float 2025–26 L1/infra launches** (MON, MEGA, STABLE, XPL, WLFI, ASTER), **fresh meme/launchpad listings** (PONS, CASHCAT, USELESS) and **RWA/stablecoin tokens** (CC, XPL, ONDO). Do not chase **ZEC** or **STRK**. Treat **ARB** as a two-way short-squeeze trap. On the watchlist, **LIT** looks weakest.

### Cited Findings
- **Low float / high FDV and weak RS** (CoinGecko circulating % and FDV; HL RS since Jul 1):
  - MON: 12% circulating, FDV $2.30B, RS −17%, funding −9% APR.
  - MEGA: 11% circulating, FDV $469M, −78% from its 2026-04-30 ATH.
  - STABLE: 27% circulating, FDV $2.60B.
  - XPL: 45% circulating, −95% from ATH, RS −34%.
  - WLFI: 32% circulating, FDV $5.70B, RS −27%.
  - ASTER: 35% circulating, FDV $5.50B, RS −18%.
  - 2Z: −96% from ATH.
  - Sources: [CoinGecko markets API](https://api.coingecko.com/api/v3/coins/markets); [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- **New meme/launchpad listings dumping:**
  - PONS: listed on HL 2026-08-31; −47% in the pullback; −67% from its 2026-09-05 ATH. Pons V2 launchpad revenue −72% 30d/30d — [DefiLlama](https://api.llama.fi/overview/fees?excludeTotalDataChart=true&dataType=dailyRevenue).
  - CASHCAT: −34% in the pullback, −65% from ATH.
  - USELESS: −42%.
  - KAITO (InfoFi): −68% over 90d.
  - Sources: [Hyperliquid info API](https://api.hyperliquid.xyz/info); [CoinGecko](https://api.coingecko.com/api/v3/coins/markets)
- **RWA/stablecoin token basket:** worst sector RS since Jul 1 (−25% median). CC RS −46% and ONDO RS +3% since Jul 1 — [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- **Crowded/broken momentum:**
  - ZEC: OI $534M, −32% from its post-July high; ETF outflows (see Q3).
  - STRK: +145% over 90d, but −32% over 7d and −16.7% in 24h on 2026-10-17.
  - ARB: funding −35% APR (shorts crowded), RS −11% in the pullback.
  - Source: [Hyperliquid info API](https://api.hyperliquid.xyz/info)
- **Watchlist flags:**
  - LIT: RS −28% in the pullback, −43% from its post-July high, 25% circulating (FDV $3.22B), Lighter revenue −16% m/m, funding −13% APR.
  - HYPE: FDV $76.40B with 23% circulating, so ongoing unlock overhang despite leadership.
  - Sources: [Hyperliquid info API](https://api.hyperliquid.xyz/info); [CoinGecko](https://api.coingecko.com/api/v3/coins/markets); [DefiLlama](https://api.llama.fi/overview/fees?excludeTotalDataChart=true&dataType=dailyRevenue)

### Inferences
- The recurring pattern in 2026 is that token value accrues where there is **real revenue plus buybacks (HYPE, PUMP) or an institutional wrapper (ZEC ETF, NEAR ETF)**. It does not accrue to low-float VC launches or to sectors whose economics flow to equity or issuers (stablecoins, RWA).
- Negative-funding coins (ARB, LIT, MON) can squeeze violently on a BTC bounce. That makes them better as short-term squeeze trades than as holds.

### Gaps
- No verified 6-month unlock calendar (Tokenomist/DefiLlama paywalled). Check Tokenomist before entering ZRO, ARB, STRK, PUMP, HYPE or LIT.
