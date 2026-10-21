# Life cycles of past crypto narratives (2017 – Oct 2026): benchmarks for judging whether the 2025–26 stablecoin narrative is early, mid, late or finished

Method and labels (read first):
- **[computed]** means I calculated the figure. **[quoted]** means it comes from the linked source. Today is 2026-10-21; the last full daily close used is 2026-10-20.
- **Prices and market caps** come from CMC daily data, fetched in chunks of ≤350 days per token: [CMC historical API](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=52&convertId=2781&timeStart=1488326400&timeEnd=1546214400) (replace `id`; IDs were resolved with the [CMC map API](https://api.coinmarketcap.com/data-api/v3/map/all?listing_status=active,inactive,untracked&start=1&limit=10000)).
- **Fundamentals:**
  - DefiLlama: [total TVL](https://api.llama.fi/v2/historicalChainTvl), [protocol TVL](https://api.llama.fi/protocol/eigencloud), [chain TVL](https://api.llama.fi/v2/historicalChainTvl/Blast), [fees/revenue](https://api.llama.fi/summary/fees/hyperliquid?dataType=dailyFees), [stablecoins total](https://stablecoins.llama.fi/stablecoincharts/all), [per-stablecoin, e.g. USDe](https://stablecoins.llama.fi/stablecoin/146), [sUSDe yield](https://yields.llama.fi/chart/66985a81-9c51-46ca-9977-42b4fe7bc6df).
  - L2Beat: [L2 activity](https://l2beat.com/api/scaling/activity?range=max), [L2 TVS](https://l2beat.com/api/scaling/tvs?range=max), [per-chain activity, e.g. Base](https://l2beat.com/api/scaling/activity/base?range=max).
  - Deribit perpetual funding, hourly, from 2019-04-30: [Deribit funding API](https://www.deribit.com/api/v2/public/get_funding_rate_history?instrument_name=BTC-PERPETUAL&start_timestamp=1609459200000&end_timestamp=1612137600000).
  - CRCL equity: [Yahoo chart API](https://query1.finance.yahoo.com/v8/finance/chart/CRCL?range=10y&interval=1d).
- **Scripts and raw data:** `/tmp/claude-0/-home-user-test-claude/56cdb752-ecb2-5227-8372-2244ddf9f61a/scratchpad/scripts/` (`narratives.py`, `download.py`, `sectors.py`, `fund_report.py`, `extra.py`, `final_checks.py`, `events.py`); data is in `.../scratchpad/data/`.
- **Definitions:**
  - "Sector cap" is the sum of the CMC market caps of a hand-picked basket of tokens; it is a lower bound on any official category cap.
  - "Constant basket" freezes the tokens listed on the peak day, which removes the mechanical boost from later listings.
  - "EW" is an equal-weight price index (mean of price relatives).
  - "First close" is the first CMC daily close, used as the TGE/listing proxy.
  - Peaks are daily closes.
- **Caveats:**
  - First prints are meaningless for bonding-curve or fair-launch tokens (most memecoins and the AI-agent tokens VIRTUAL, AI16Z, AIXBT, GOAT, GRIFFAIN, ZEREBRO, ARC and COOKIE). They are excluded from listing-return statistics.
  - CMC early data has errors. TenX PAY's first print of $47.8 on 2017-06-27 is wrong, NPXS prints after 2021 are anomalous, and COMP's 2020-06-21 OHLC has high < close.
  - Monaco (MCO) and old VeChain (VEN) have no CMC history. "Untracked" tokens (FTM, MATIC, WTC, YAM, ANC, BAS, DSD and others) have data only to about 2023-11-14.
  - DefiLlama's derivatives-volume and raises endpoints are paywalled, so I used fees as the activity proxy, and VC data comes from news coverage.

## 1. Narrative scoreboard: trigger, months to peak, peak size, drawdown at +6 and +12 months

### Takeaway
Across about 20 narrative waves, the time from the visible trigger to the price peak ranged from 1.7 to about 14 months, with a median of about 8 months across 18 waves using price-based peaks.
- **Fast waves** peaked 1.7–3.6 months after a single speculative trigger: stablecoin 2025 (1.7 months to the equal-weight peak), DeFi leg 1, gaming/TON, AI agents, NFT leg 1 and alt-L1s.
- **Infrastructure-heavy waves** took 10–14 months: L2s (11.6), memecoins (12.0), BTCfi (12.8), RWA (13.2) and AI infra (14.3).

Without a second leg, constant-basket sector caps had a median of **−66% at +6 months (range −54% to −94%) and −82% at +12 months (range −60% to −94%)**. The exceptions were waves rescued by a second leg (DeFi 2020, NFT leg 1) and the HYPE-led perp sector.

The 2025 stablecoin token basket peaked 1.7 months (equal-weight incumbents, 2025-07-27) to 3.7 months (cap, 2025-09-27) after the CRCL IPO. At +6 months it was −69%, typical of past narratives. At +12 months it was −42% (cap) / −55% (EW), the **mildest 12-month reading in the sample**. That reflects a partial 2026 rebound and the weight of SKY and SYRUP; ex-SKY it was −54% (cap) / −64% (EW).

### Cited Findings
- Scoreboard [computed; CMC daily data; BTC columns use the same windows] — [CMC historical API](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1&convertId=2781&timeStart=1488326400&timeEnd=1792454400)

| Narrative (basket size) | Trigger (date) | Peak date (basis) | Months to peak | Peak basket cap | Multiple vs trigger | Constant basket +6m | Constant basket +12m | BTC: trigger→peak; +6m / +12m after peak |
|---|---|---|---|---|---|---|---|---|
| 2017–18 payment & enterprise coins (13) | 2017-03-01 baseline of alt/ICO run | 2018-01-07 (cap) | 10.2 | $167.1B (XRP-dominated) | 589x | −84% (EW −81%) | −89% (EW −94%) | +1,248%; −59% / −76% |
| DeFi Summer, leg 1 (24) | 2020-06-15 COMP liquidity mining | 2020-09-01 | 2.6 | $6.55B | 5.4x | +141% (second leg; +3m was −36%) | +144% | +27%; +304% / +308% |
| DeFi, leg 2 (22) | 2020-11-04 post-leg-1 trough | 2021-05-14 | 6.3 | $55.8B | 16.2x | −29% | −81% (+24m −85%) | +253%; +29% / −40% |
| Algorithmic stablecoins 2020–21 (8) | ESD (Nov 2020 on CMC), BAC launch 2020-12-02 | token peaks 0–44 days after each launch | ~0–1.5 | n/m (tiny) | n/m | median −95% at +180d from launch | median −99% at +365d | — |
| Curve wars / Terra (11) | 2021-05-17 Convex launch | 2022-04-04 (cap, LUNA) / 2022-01-01 (EW incumbents) | 10.6 / 7.5 | $46.6B | 6.1x (EW +176%) | −94% (EW −87%) | −94% (EW −86%) | +7%; −58% / −40% |
| NFT/metaverse, leg 1 (12) | 2021-01-01 (Top Shot/Beeple era) | 2021-04-16 | 3.4 | $25.7B | 10.8x | −14% (leg 2 under way; +3m −53%) | −22% | +110%; +0% / −34% |
| NFT/GameFi/metaverse, leg 2 (18) | 2021-07-01 (Axie summer) | 2021-11-25 | 4.8 | $53.7B | 5.0x (EW +1,515%) | −80% (EW −87%) | −88% (EW −92%) | +71%; −49% / −71% |
| 2021 alt-L1 rotation (16) | 2021-07-20 post-crash low | 2021-11-08 (cap) / 2022-01-16 (EW) | 3.6 | $249.6B | 6.2x (EW +534%) | −66% (EW −65%) | −82% (EW −84%) | +127%; −55% / −73% |
| AI infra 2023–24 (4) | 2023-01-01 (post-ChatGPT) | 2024-03-09 (EW FET/RENDER) / 2024-12-06 (cap) | 14.3 / 23.2 | $18.7B | EW +3,113% | −54% from cap peak | −70% | +501% to cap peak |
| L2 season (17) | 2023-03-23 ARB TGE | 2024-03-11 (EW OP/ARB/METIS) / 2024-12-08 (cap) | 11.6 / 20.6 | $22.7B | EW +172%; cap 8.7x | EW −74%; cap −66% | EW −86%; cap −69% | +257% to cap peak; +5% / −10% |
| Restaking / LRTs (7) | 2024-03-18 ETHFI TGE | 2024-12-16 (cap) | 9.0 | $1.98B | 5.5x (mostly new listings) | −60% (EW −75%) | −64% (EW −89%) | +57%; +1% / −17% |
| BTCfi / Bitcoin L2s (9) | 2023-03-08 BRC-20 launch | 2024-04-01 | 12.8 | $9.9B | 10.0x | −55% | −84% (+24m −95%) | +221%; −9% / +22% |
| 2024 gaming + TON tap-to-earn (12) | 2024-01-01 | 2024-03-21 (EW) / 2025-01-06 (cap) | 2.7 / 12.2 | $7.9B | EW +124% | −72% | −82% | +131%; +6% / −8% |
| AI agents (14) | 2024-10-10 GOAT/Truth Terminal | 2025-01-04 | 2.8 | $10.4B | 176x | −84% (+3m −91%) | −91% | +63%; +10% / −7% |
| Memecoins, new wave (15) | 2024-01-19 pump.fun launch | 2025-01-19 (TRUMP launch) | 12.0 | $28.8B | 15.0x | −29% | −77% | +143%; +16% / −8% |
| Memecoins incl. DOGE/SHIB (17) | 2024-01-19 | 2024-12-08 | 10.6 | $115.9B | 6.2x | −57% | −69% | +143%; +5% / −10% |
| RWA / tokenization (6) | 2024-01-18 ONDO TGE | 2025-02-23 (cap, OM-driven); ONDO peak 2024-12-15 | 13.2 | $12.2B | 26.3x | −66% (EW +39%) | −87% (EW −52%) | +133%; +18% / −33% |
| Perp DEXs ex-HYPE (9) | 2024-11-29 HYPE TGE | 2025-09-24 (ASTER TGE week) | 9.8 | $5.6B | 2.5x | −65% (EW −75%) | −60% (EW −75%) | +16%; −37% / −26% |
| Perp DEXs incl. HYPE (10) | 2024-11-29 | 2026-09-22 (HYPE ATH) | 21.7 | $28.0B | 12.3x | n/a (only 4 weeks old) | n/a | −12% to peak |
| **Stablecoin first leg 2025 (12)** | **2025-06-05 CRCL IPO** | **2025-07-27 (EW incumbents) / 2025-09-27 (cap, XPL listing)** | **1.7 / 3.7** | **$10.4B** | **EW +45%; cap 2.1x** | **−69% (EW −65%)** | **−42% (EW −55%)** | **+8% to cap peak; −40% / −23%** |
| Privacy (9) | 2025-09-01 ZEC breakout | 2026-09-26 | 12.8 | $39.9B | 6.7x | n/a (−16% by 2026-10-20) | n/a | −23% to peak |

- Basket constituents [computed], one row per narrative:
  - Payments: XRP, XLM, OMG, PAY, REQ, NPXS, ETN, XEM, WTC, TEL, UTK, CRPT, PPT.
  - DeFi leg 1: COMP, YFI, UNI, SUSHI, MKR, SNX, CRV, BAL, UMA, REN, BAND, LRC, ZRX, YAM, SWRV, PICKLE, CREAM, FARM, HEGIC, KP3R, ALPHA, BOND, BADGER, 1INCH. AAVE is excluded from leg 1 because CMC's AAVE series starts 2020-10-04, and LEND has no CMC data.
  - Algo-stables: AMPL, BAC, BAS, ESD, DSD, TRIBE, FXS, TITAN.
  - Curve wars: CRV, CVX, FXS, LUNA (classic), ANC, MIR, SPELL, ALCX, TOKE, BTRFLY, OHM.
  - Alt-L1: SOL, AVAX, LUNA, FTM, NEAR, ATOM, ALGO, ONE, MATIC, DOT, EGLD, CELO, HBAR, ICP, KSM, ROSE.
  - L2: OP, ARB, MNT, METIS, STRK, ZK, BLAST, MANTA, TAIKO, SCR, TIA, DYM, ALT, SAGA, MODE, AVAIL, ZETA.
  - Restaking: EIGEN, ETHFI, REZ, PUFFER, SWELL, KERNEL, LAYER.
  - AI agents: VIRTUAL, AI16Z, AIXBT, GOAT, GRIFFAIN, ZEREBRO, SWARMS, COOKIE, ARC, VVV, KAITO, SHELL, NIL, BIO.
  - Stablecoin 2025: ENA, USUAL, RESOLV, FF, XPL, STBL, SKY, STABLE, SYRUP, FXS (now FRAX), CRV, HUMA.

  Source: [narratives.py; CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=30171&convertId=2781&timeStart=1749081600&timeEnd=1792454400)
- Breadth at the top, measured as the share of basket tokens whose own ATH (within the window) fell within ±30 days of the sector peak [computed] — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=6783&convertId=2781&timeStart=1625097600&timeEnd=1672444800):
  - Synchronized blow-offs: payments 2018 11/13, DeFi leg 1 17/22, AI agents 10/14, NFT leg 1 9/12, NFT leg 2 10/18.
  - Staggered tops: alt-L1 5/16, L2 1/17, restaking 2/7, stablecoin 2025 4/12.
- Market-wide sizing:
  - CoinGecko-based reports put the AI-agent sector peak at about $15–15.7B in early January 2025 [quoted] — [Sherwood](https://www.sherwood.news/crypto/ai-agent-crypto-tokens-rise-traders-ride-the-ai-wave); [The Block](https://www.theblock.co/post/334213/ai-agent-tokens-reel-from-a-steep-market-correction).
  - The sector fell 16.6% to about $11.4B on 2025-01-13 [quoted] — [ForkLog](https://forklog.com/en/ai-agent-token-market-cap-drops-nearly-17/).
  - A later report has it down 77.5% from the peak to $4.4B; that article's date is unclear [quoted] — [BeInCrypto](https://beincrypto.com/ai-agents-market-loss/).
- Terra collapse size: estimates range from "almost $45 billion of market cap in a week" to $18–50B for LUNA+UST, and are often rounded to "$40B" [quoted] — [Blockcrunch](https://blockcrunch.substack.com/p/how-terra-luna-lost-40-billion); [Law Journal Newsletters](https://lawjournalnewsletters.com/2024/05/01/is-the-crypto-winter-over); [CFI](https://corporatefinanceinstitute.com/resources/cryptocurrency/what-happened-to-terra).

### Inferences
- **Fast waves top fast:**
  - Narratives with a single, sharp, speculative trigger peaked in 2–4 months: DeFi leg 1, NFT leg 1, alt-L1, AI agents and stablecoin 2025.
  - Those that needed infrastructure rollouts or a sequence of TGEs peaked in 10–14 months: L2, BTCfi, restaking, memecoins, RWA.
  - By elapsed time alone, a narrative that started in mid-2025 would have been "late" by late 2025 under either template.
- **Use price-based peaks, not cap-based peaks, for timing.** Cap-based peaks drift later because of unlocks and new listings: L2s by 9 months, AI infra by 9 months, stablecoin 2025 by 2 months. The gap is itself a late-stage symptom (Section 6).
- **The normal post-peak path.** Without a second leg, the median narrative basket lost about two-thirds within 6 months (−66%) and about four-fifths within 12 months (−82%). Only DeFi 2020 and NFT leg 1 recovered within 6 months, both helped by a broad bull market (BTC +300% after the DeFi leg-1 peak). The 2025 stablecoin basket's milder 12-month reading does not by itself indicate a second leg; see Section 5 for those conditions.

### Gaps
- No official, dated sector-cap time series (CoinGecko/CMC category history) could be retrieved without paid APIs; my sector caps are basket sums. Libra/Diem had no token, so it has no row (see Section 3).

## 2. When TGEs clustered within each cycle, and how late-cycle TGEs performed

### Takeaway
In most narratives studied, the majority of token launches came in the final third of the run-up or after the price peak. That was 67% of the 2017–18 payment ICOs, 87% of DeFi-summer tokens, 71% of restaking tokens, 83% of BTCfi tokens and 80% of stablecoin-2025 tokens. L2 TGEs split 50/50 around the March 2024 price peak, and the 2023–24 Solana/points airdrops came early. Late and post-peak TGEs then lost a median **−40% to −90%** at +180 days unless a broad bull market followed. In DeFi 2020, a broad bull did follow, and late TGEs were +57% to +155% at +180 days.

Recent base rates are bleak:
- 2023-11 to 2024-12 TGEs: 78% were below their first close at +180 days, and 98% are below it today.
- 2025–26 TGEs: 86% are below their first close today, and 62% made their ATH within 14 days of listing.
- Memento Research found 84.7% of 118 2025 TGEs below launch price, and **none of the 28 launches with FDV ≥ $1B** above it.

### Cited Findings
- TGE cohorts. "Early" means listed before the last third of the run-up. "Late" means listed in the last third or within 60 days before the sector peak. "Post" means listed after the peak. Returns are median, from the first close. [computed] — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=36645&convertId=2781&timeStart=1758758400&timeEnd=1792454400)

| Narrative | Early cohort (n): +180d | Late cohort (n): +180d / +365d | Post-peak cohort (n): +180d / +365d | All cohorts to 2026-10-20 |
|---|---|---|---|---|
| Payments 2017–18 | OMG, WTC, PPT (3): +1,871% | REQ, ETN, UTK (3): −67% / −75% | TEL, CRPT, NPXS* (3): −82% / −94% | −93% to −99% |
| DeFi 2020 (vs 2020-09-01 peak) | COMP, BAL (2): +24% | YFI, SUSHI, CRV, YAM, CREAM (5): +155% / +108% | UNI, SWRV, PICKLE, FARM, HEGIC, KP3R, ALPHA, BOND (8): +57% / +82% | −86% to −99% |
| Algo-stables | BAC, BAS, ESD, DSD, TRIBE, FXS, TITAN (7): −95% (+365d −99%) | — | — | −100% (FXS −93%) |
| NFT leg 1 (2021-04 peak) | FLOW (1): +169% | ALICE, TLM, ILV (3): −39% / −73% | — | −99% |
| NFT leg 2 (2021-11 peak) | YGG (1): +73% | IMX, MAGIC (2): +118% / −21% | APE, LOOKS, GMT (3): −39% / −48% | −73% to −98% |
| L2 (vs 2024-03-11 price peak) | ARB, MNT, TIA, MANTA, DYM, ALT, ZETA, STRK (8): −56% (+365d −68%) | — | SAGA, MODE, TAIKO, ZK, BLAST, AVAIL, SCR, LINEA (8): −64% / **−90%** | −97% / −98% |
| Restaking/LRT | ETHFI, REZ (2): −67% (+365d −85%) | EIGEN, PUFFER, SWELL (3): −77% / −86% | KERNEL, LAYER (2): −47% / −83% | −87% to −94% |
| BTCfi | ORDI (1): −61% | — | MERL, BABY, SOLV, BARD, DOG (5): −41% / −88% | −90% |
| Gaming/TON 2024 | PIXEL, PORTAL, XAI, NOT, DOGS (5): −74% (+365d −88%) | HMSTR, CATI, PENGU, ME (4): −76% / −90% | — | −96% to −99% |
| AI agents | — | SWARMS, BIO (2): −69% / −69% | VVV, KAITO, SHELL, NIL (4): −54% / −89% | −86% to −89% |
| Memecoins | (fair launches excluded) | PENGU, TRUMP, MELANIA (3): −66% / −82% | PUMP (1): −72% / −81% | −83% to −94% |
| RWA | ONDO (1): +390% | PLUME, SYRUP (2): −18% / −11% | — | ONDO +105%; late −56% |
| Perp DEXs ex-HYPE | — | ASTER, AVNT (2): +28% / +18% | LIT (1): −35% | +17% (late), +26% (LIT) |
| **Stablecoin 2025** | **RESOLV (1): −79% (+365d −95%)** | **XPL, STBL (2): −82% / −86%** | **FF, STABLE (2): −40% / −55% (FF only)** | **−95% / −87% / −41%** |

  *NPXS post-2021 prints are anomalous.
- Base rates from my samples [computed] — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=30171&convertId=2781&timeStart=1711929600&timeEnd=1792454400):
  - **2023-11 → 2024-12 TGEs (n=41: L2, points, restaking, gaming, TON, BTCfi, perps, ONDO, SYRUP):** median +180-day return −63%; 78% below the first close at +180d; today 40 of 41 (98%) are below the first close, with a median of −97%. Only ONDO (+105%) is above.
  - **2025–26 TGEs (n=37):**
    - Constituents: ASTER, LIT, AVNT, RESOLV, FF, XPL, STBL, WLFI, STABLE, HUMA, BABY, SOLV, BARD, KERNEL, LAYER, KAITO, SHELL, NIL, BIO, VVV, PLUME, MON, MEGA, BERA, ZORA, WCT, SOPH, INIT, PROVE, ZAMA, AZTEC, KITE, LMTS, PUMP, TRUMP, MELANIA, LINEA.
    - On 2026-10-20, 86% were below their first close, with a median of −83% (−90% from ATH).
    - The median gap from first close to ATH was **9 days**, and 23 of 37 peaked within 14 days of listing.
    - Only ASTER (+85%), ZAMA (+112%), KITE (+54%), LIT (+26%) and VVV (+14%) are above their first close.
- Memento Research tracked 118 2025 TGEs, with data as of 2025-12-20 [quoted] — [ForkLog](https://forklog.com/en/85-of-tokens-launched-in-2025-fell-below-initial-prices/):
  - 100 (84.7%) were below their opening price.
  - The median FDV fell 71% and the median market cap 67%.
  - None of the 28 launches with an initial FDV ≥ $1B were above their launch price, and their median drop was about 81%.
- Keyrock studied 62 airdrops across six chains in 2024: 88% of airdropped tokens declined, most within 15 days of listing. 88.7% were lower after 90 days. High FDV and thin liquidity were the main drivers [quoted] — [DL News](https://www.dlnews.com/articles/snapshot/keyrock-study-says-most-token-airdrops-crash-after-launch); [BeInCrypto](https://beincrypto.com/majority-airdrop-tokens-crash-within-15-days/)
- Binance Research, "Low Float & High FDV" (published 2024-05-17) [quoted] — [ForkLog](https://forklog.com/en/binance-highlights-155-billion-token-unlock-overhang/); [Cointelegraph](https://cointelegraph.com/news/binance-urges-small-medium-projects-high-fdv-trend); [CryptoPotato](https://cryptopotato.com/binance-doubles-down-on-low-float-high-fdv-calls-for-action/):
  - 2024 launches had an average MC/FDV of 12.3%, implying about $80B of new demand needed to absorb future supply. About $155B of tokens were due to unlock in 2024–2030.
  - Low-float tokens can rally fast in bull markets, but "this kind of price growth is unsustainable when a wave of token supply hits the market upon unlocking."
- CEX listing performance in 2024 [quoted]:
  - A May 2024 review found that 80% of Binance listings from the prior six months were below their listing price, with an average FDV above $4.2B — [Cointelegraph](https://cointelegraph.com/news/over-80-binance-token-listings-loss-red); [BeInCrypto](https://beincrypto.com/majority-binance-token-listing-decline-research/).
  - Animoca Research found that new 2024 CEX listings averaged a drop of about 49%; Binance listings averaged −27% with a median near −50% — [CryptoSlate](https://cryptoslate.com/tokens-display-up-to-negative-70-median-returns-after-cex-listing-animoca-research/).
- 2017–18 ICO timing [quoted] — [Finance Magnates](https://www.financemagnates.com/cryptocurrency/news/6-3-billion-ico-funding-q1-2018-already-surpassed-2017/); [e27](https://e27.co/tepid-merchant-acceptance-contributes-crypto-drag-coindesk-20180515/):
  - Q1 2018 ICO funding was about $6.3B (CoinDesk data), 118% of all of 2017, and $4.6B excluding Telegram.
  - Monthly totals: December 2017 $1.44B, January 2018 $1.79B, February 2018 $2.38B (peak), March 2018 $2.15B.
  - Other trackers put Q1 2018 at $5.0–5.8B.

### Inferences
- **Late launches have almost always lost money.**
  - "Late-cycle TGE" was a reliable negative signal except when a market-wide bull followed within about 3 months (DeFi Sept–Oct 2020). Even then, the late tokens were −97% to −99% by today.
  - The strongest pattern is L2: tokens launched after the March 2024 price peak lost a median −90% within a year, against −68% for pre-peak launches.
- **TGEs cluster after the crowd arrives.** Issuance clustered after the price peak: ICO money peaked a month after the January 2018 token top, and stablecoin-chain tokens (XPL, STBL, STABLE) launched 2–4 months after the stablecoin EW peak. This is the "supply chases demand" signature of a late narrative.
- **Peaking within days of listing is the norm, not a warning sign of one project.** Over 2023–26, 62% of the 2025–26 sample peaked within 14 days, so a narrative whose new TGEs repeatedly "peak at listing" is in distribution mode.

### Gaps
- I could not reconstruct FDV at TGE for my samples, because CMC history has circulating supply but not total supply. FDV-bucketed results therefore rely on Memento's study.
- Memento's full methodology, the tokens included and later updates were not retrieved; secondary coverage only. Keyrock's report was also read via secondary coverage.

## 3. How fundamentals evolved after the hype, compared with token prices

### Takeaway
Fundamentals usually peaked **after** token prices, often by months:
- DeFi TVL peaked 6 months after DeFi tokens.
- OpenSea fees peaked about 2 months after NFT tokens.
- USDe supply peaked 7 weeks after ENA's local high.
- L2 activity and TVS kept rising for 9–15 months after L2 tokens peaked.
- Total stablecoin supply set its ATH on 2026-05-17, about 10 months after the stablecoin token EW peak.

There were two exceptions. Fundamentals that collapsed together with tokens belonged to reflexive or incentive-funded designs: UST/Anchor, algo-stables, Axie, Blast, LRTs and Aster. In the second exception, the token tracked fundamentals in both directions: SOL 2023–25 and HYPE 2025–26.

### Cited Findings
- **DeFi** [computed] — [DefiLlama total TVL](https://api.llama.fi/v2/historicalChainTvl); [DefiLlama fees](https://api.llama.fi/summary/fees/uniswap?dataType=dailyFees):
  - TVL path: $1.12B (2020-06-15) → $8.62B (2020-09-01, leg-1 token peak) → $9.58B (2020-11-04) → $122.2B (2021-05-12, leg-2 token peak) → **peak $177.5B (2021-11-09)** → $51.8B (2022-06-30) → $38.3B (2022-12-31). It made a second TVL peak of $171.0B on 2025-10-07 and stood at $88.8B on 2026-10-20.
  - The DeFi leg-2 token basket was −94% EW from May 2021 to 2026-10-20.
  - Annual fees: Uniswap $1.58B (2021), $828M (2022), $598M (2023), $1.09B (2024), $1.05B (2025). Over the same span UNI fell from $43.16 (2021-05-04) to $7.43 (2026-10-20).
  - Aave: $253M (2021) → **$908M (2025)**; AAVE was $154.5 on 2026-10-20 vs a $632 ATH.
  - Compound: $353M (2021) → $20M (2026 YTD). Sushi: $522M (2021) → $8.6M (2026 YTD).
  - Curve: fees rose to a **record $254M in 2023, after CRV had fallen about 95%**, then fell to $60M (2025).
  - Uniswap protocol "revenue" is about zero until 2025 and $58.4M in 2026 YTD (fee switch).
- **Curve wars and algo-stables** [computed] — [DefiLlama protocol](https://api.llama.fi/protocol/convex-finance); [DefiLlama UST](https://stablecoins.llama.fi/stablecoin/3):
  - Curve TVL peaked at $24.3B and Convex at $21.2B, both on 2022-01-05, the same week CVX (2022-01-01) and FXS (2022-01-12) peaked. Abracadabra TVL also peaked then at $6.42B, and MIM supply at $3.64B.
  - Anchor TVL peaked at $17.15B on 2022-05-05 and UST supply at $18.77B on 2022-05-07, two days before the run. By 2022-05-15 Anchor TVL was $316M.
  - FEI's TVL of $2.61B and supply of $2.40B both peaked on launch day (2021-04-04/05). Iron Finance TVL was $2.29B on 2021-06-15, the day before TITAN went to zero.
  - On 2026-10-20 Curve TVL was $1.20B and Convex $0.58B.
- **Terra mechanics** [quoted]:
  - Anchor launched at a 19.45% rate — [Ajou Univ. repository](https://aurora.ajou.ac.kr/handle/2018.oak/36088).
  - Over 75% of UST supply was staked in Anchor before the collapse — [Genesis Research](https://genesisresearch.notion.site/Revisiting-the-Catastrophic-Downfall-of-LUNA-Part-2-The-Failing-Anchor-Protocol-b80a77becca34b47a034bb549e342235).
  - By 2022-05-11 UST was below $0.23 and LUNA was down about 86% in 24 hours — [ForkLog](https://forklog.com/en/luna-price-plunges-86-as-ust-stablecoin-slides/).
- **NFT/GameFi** [computed] — [DefiLlama Axie fees](https://api.llama.fi/summary/fees/axie-infinity?dataType=dailyFees); [DefiLlama OpenSea fees](https://api.llama.fi/summary/fees/opensea?dataType=dailyFees):
  - Axie 30-day fees peaked at $379.8M on 2021-08-21, about 2.5 months **before** AXS's price peak (2021-11-07), then fell to $19.1M by 2022-01-31.
  - OpenSea 30-day fees peaked at $383.3M on 2022-02-02, about 2 months **after** the NFT-token peak (2021-11-25). They were $16.1M by 2022-11-30 and $1.5M on 2026-10-20.
  - OpenSea's January 2022 volume was a record above $5B (Ethereum + Polygon, Dune), beating August 2021 [quoted] — [Decrypt](https://decrypt.co/91748/opensea-record-5b-ethereum-nft-market-swells?amp=1).
- **2021 alt-L1s** [computed] — [DefiLlama chain TVL](https://api.llama.fi/v2/historicalChainTvl/Solana); [DefiLlama Solana fees](https://api.llama.fi/summary/fees/solana?dataType=dailyFees):
  - TVL peaks lagged the 2021-11-08 token-cap peak by 0–6 months: Solana $10.03B (2021-11-09), Avalanche $11.49B (2021-12-02), Fantom $7.93B (2022-03-03), Terra $20.38B (2022-05-05).
  - By 2022-11-08 Solana TVL was $0.86B (−91%) and Avalanche $1.27B (−89%).
  - Solana's second leg had real fees behind it: chain fees were $23.5M (2023), $713M (2024) and $645M (2025). SOL went from $9.65 (2022-12-29) to $261.9 (2025-01-18).
- **L2s: usage up, revenue and tokens down** [computed] — [L2Beat activity](https://l2beat.com/api/scaling/activity?range=max); [L2Beat TVS](https://l2beat.com/api/scaling/tvs?range=max); [DefiLlama Arbitrum revenue](https://api.llama.fi/summary/fees/arbitrum?dataType=dailyRevenue); [DefiLlama Base revenue](https://api.llama.fi/summary/fees/base?dataType=dailyRevenue):
  - L2 transactions per day (30-day average) rose from 5.1M (2023-03-23) to 12.9M at the token price peak (2024-03-11), then 36.8M (2024-12-08) and 37.5M (2025-06-30). Later aggregate readings (182M/day in Oct 2026) are inflated by new high-throughput rollups.
  - Base went from 0.4M to 9.7M tx/day between Mar 2024 and Jun 2025.
  - TVS went from $11.4B to $46.1B (2024-03-11), peaked at $66.5B (2024-12-09), and was $41.2B on 2026-10-15.
  - Meanwhile the L2-token EW (OP, ARB, METIS) was −74% at +6m and −86% at +12m from March 2024. The 17-token L2 basket is −93% EW from its Dec 2024 cap peak.
  - Annual revenue (DefiLlama "revenue"):

    | Chain | 2024 | 2025 | 2026 YTD |
    |---|---|---|---|
    | Arbitrum | $22.2M | $17.6M | $4.8M |
    | OP Mainnet | $13.6M | $3.6M | $0.6M |
    | zkSync Era | $7.5M | $0.5M | $0.2M |
    | Starknet | $8.0M | $1.0M | $1.6M |
    | **Base (no token)** | **$76.5M** | **$74.4M** | **$39.1M** |

  - Celestia fees: $1.9M (2023), $1.1M (2024), $0.3M (2025).
- **Post-Dencun economics** [quoted]:
  - Token Terminal data shows Ethereum L1 revenue down about 99% from its March 2024 peak while L2 users and transactions roughly doubled — [Cointelegraph](https://cointelegraph.com/news/ethereum-network-revenue-collapses-third-quarter-2024).
  - Galaxy's 150-day review links part of the activity to bots, with failure rates peaking at 21% on Base, 15.4% on Arbitrum and 10.4% on OP Mainnet — [ForkLog](https://forklog.com/en/dencun-update-spurs-rise-in-failed-transactions-on-ethereums-l2-networks/amp).
  - Weekly blob-fee income fell more than 95% between mid-March and late March 2025 — [Cointelegraph](https://cointelegraph.com/news/ethereum-weekly-blob-fees-hit-2025-lows).
- **Restaking/LRTs** [computed] — [DefiLlama EigenLayer/EigenCloud](https://api.llama.fi/protocol/eigencloud); [DefiLlama Renzo](https://api.llama.fi/protocol/renzo):

  | Protocol | TVL peak (date) | TVL at or after the token event | TVL 2026-10-20 | Token |
  |---|---|---|---|---|
  | EigenLayer | $22.06B (2025-08-14, ETH-driven) | $11.86B (2024-03-18), $18.82B (2024-06-15), $11.96B (2024-10-01, EIGEN transferable) | $6.19B | EIGEN −96% from ATH |
  | ether.fi | $12.43B (2025-08-14) | grew after its TGE | $4.58B | ETHFI −91% from ATH |
  | Renzo | $4.05B (2024-05-28, a month after the REZ TGE) | $997M (2024-10-01) | $109M | REZ −98% |
  | Puffer | $1.84B (2024-06-06) | $462M (2024-12-16, two months after the PUFFER TGE) | $27M | PUFFER −95% |
  | Swell | $500M (2024-05-28) | — | $27.6M | SWELL −99% |

  - EigenLayer protocol revenue per DefiLlama is $0. Its fees (rewards) were $63M (2024) and $86.5M (2025).
  - ether.fi fees were $240M in 2025, with revenue of $57M.
- **BTCfi** [computed] — [DefiLlama Babylon](https://api.llama.fi/protocol/babylon-protocol):
  - Babylon TVL was $5.26B (2024-12-16), peaked at $7.14B (2025-10-07) and was $3.33B on 2026-10-20.
  - BABY is −85% vs its first close, MERL −98% and ORDI −96% from ATH.
- **AI agents** [computed] — [DefiLlama Virtuals revenue](https://api.llama.fi/summary/fees/virtuals-protocol?dataType=dailyRevenue):
  - Virtuals 30-day revenue peaked at $15.9M on 2025-01-17, fell to $0.4M by 2025-04-30 (−97% in about 3.5 months) and was $0.1M on 2026-10-20. VIRTUAL is −85% from ATH.
- **Memecoins** [computed] — [DefiLlama pump.fun revenue](https://api.llama.fi/summary/fees/pump?dataType=dailyRevenue); [DefiLlama pump DEX volume](https://api.llama.fi/summary/dexs/pump):
  - pump.fun 30-day revenue peaked at $145.5M on 2025-01-30, 11 days after the TRUMP-led meme peak. It was $55.2M on 2025-04-30, $36.3M around the PUMP ICO (2025-07-12) and **$68.7M on 2026-10-20**.
  - Annual revenue: $321M (2024), $652.5M (2025), $405M (2026 YTD).
  - pump.fun's 30-day DEX volume made a new high of $34.5B on 2026-02-13, yet the new-wave meme basket is −85% EW from its peak.
- **RWA** [computed] — [DefiLlama Maple](https://api.llama.fi/protocol/maple); [DefiLlama Maple fees](https://api.llama.fi/summary/fees/maple-finance?dataType=dailyFees):
  - Maple TVL went from $47M (2024-01-18) to a $3.25B peak (2025-10-30) and was $2.70B on 2026-10-20. Fees were $15.4M (2024), $71M (2025) and $88M (2026 YTD).
  - SYRUP is −68% from its 2025-06-28 ATH. ONDO is −78% from its 2024-12-15 ATH, though +105% vs its TGE.
- **Perp DEXs** [computed] — [DefiLlama Hyperliquid fees](https://api.llama.fi/summary/fees/hyperliquid?dataType=dailyFees); [DefiLlama Aster fees](https://api.llama.fi/summary/fees/aster?dataType=dailyFees); [DefiLlama Lighter fees](https://api.llama.fi/summary/fees/lighter?dataType=dailyFees):
  - Hyperliquid fees were $972M in 2025 (DefiLlama "revenue" $818M) and $698M in 2026 YTD. 30-day fees: $133.8M (2025-09-18) → $64.4M (2025-12-31) → $96.9M (2026-09-22).
  - HYPE moved with fees: $58.6 → $25.4 → $97.2 on the same dates.
  - Aster's 30-day fees peaked at $246.4M on 2025-10-21 and were $4.4M on 2026-10-20 (−98%). ASTER is −69% from ATH.
  - Lighter's 30-day fees peaked at $19.3M on 2025-11-26, before its TGE, and were $6.0M on 2026-10-20.
  - Aster's bridge TVL peaked at $1.57B (2025-10-09) and is now $479M. Hyperliquid's bridge TVL made a new high of $7.45B on 2026-09-23.
- **Libra / enterprise blockchain** [computed]. From the eve of the Libra news (2019-06-17) to 2019-06-26, BTC rose +40% while XRP rose +4% and XLM fell −6%. By 2019-12-31 the moves were BTC −23%, XRP −57%, XLM −65%; by 2020-03-12, XRP −69% and XLM −74% — [CMC XRP](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=52&convertId=2781&timeStart=1560729600&timeEnd=1584057600)
- **Libra / enterprise blockchain** [quoted]:
  - Libra was introduced in June 2019. Visa, Mastercard, PayPal and eBay dropped out as founding partners soon after. Diem's assets were sold to Silvergate for about $182M ($50M cash plus about 1.2M shares) after regulators made clear the project could not proceed — [Banking Dive](https://www.bankingdive.com/news/diem-to-end-crypto-project-sell-its-assets-to-silvergate-bank-for-182m/617839/); [Silicon Republic](https://siliconrepublic.com/?p=961462).
  - Gartner (2019-10-08) put blockchain "sliding into the Trough of Disillusionment", with most enterprise projects "stuck in experimentation mode" — [Gartner](https://www.gartner.com/en/newsroom/press-releases/2019-10-08-gartner-2019-hype-cycle-shows-most-blockchain-technologies-are-still-five-to-10-years-away-from-transformational-impact); [CIO Dive](https://www.ciodive.com/news/most-blockchain-applications-sunk-in-the-trough-of-disillusionment-gartn/564613/).

### Inferences
- **Fundamentals lag prices at the top.** Price is the leading indicator and fundamentals are coincident or lagging. A narrative's best-ever usage numbers commonly arrive when its tokens are already 30–60% off their highs: DeFi TVL in Nov 2021, OpenSea in Feb 2022, L2 TVS in Dec 2024, USDe in Oct 2025 and stablecoin supply in May 2026. "Record adoption" headlines are therefore not evidence that a token narrative is early.
- **Rewards-driven fundamentals collapse as fast as the tokens.** When the fundamental is itself bought with token emissions or reflexive yield, it dies with the token: Anchor, Iron, FEI, Axie, Blast, LRTs, Aster volume and Plasma deposits. When it is paid for by third parties (swap fees, borrow interest, trading fees, T-bill yield), it survives the token crash: Uniswap, Aave, Hyperliquid, Circle and Maple.

### Gaps
- I found no sourced 2018–2020 adoption series for payment coins (RippleNet/ODL volumes, Stellar anchors, Crypto.com users after the MCO swap). So the "2018 payment coins: adoption up, token down" analogue is documented only through prices and Gartner's enterprise-blockchain assessment.
- I did not retrieve tokenized-treasury (rwa.xyz) totals. DefiLlama's protocol entries for Ondo yield assets and BUIDL returned no TVL series.

## 4. "Fundamentals up, tokens down" vs "fundamentals and tokens both up": what separated them

### Takeaway
Tokens rose with fundamentals only when three conditions held:
1. Usage paid **the token** directly: buybacks or burns (HYPE), gas plus staking demand (SOL), or Aave/Uniswap only once fee switches or buybacks existed.
2. Circulating supply was not growing faster than revenue.
3. The broad market was in a bull phase.

Where usage accrued to an equity or a token-less entity, or where the token was governance-only with heavy unlocks, adoption grew while tokens fell 70–98%:
- Equities or token-less entities: Base, Circle, Coinbase, Ripple's banking clients.
- Governance-only tokens with heavy unlocks: OP, ARB, STRK, ZK, TIA, EIGEN, ENA before its fee switch.

The 2025 stablecoin wave matches the second group. Issuer revenue (Circle and Tether) rose, while the tokens that "own" stablecoin activity have weak direct claims on that revenue.

### Cited Findings
- Comparison by analogue [computed unless noted]. Sources: [DefiLlama fees](https://api.llama.fi/summary/fees/base?dataType=dailyRevenue); [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=11840&convertId=2781&timeStart=1679529600&timeEnd=1792454400).

| Analogue | Usage/fundamental path | Token path | Value-accrual and float facts in my data |
|---|---|---|---|
| L2 season 2023–26 | L2 tx/day 12.9M → 37.5M; TVS $46B → $66B peak | OP −97%, ARB −92%, STRK −98%, ZK −94% from ATH | Sequencer revenue went mostly to Base (no token): $74–77M a year in 2024–25. Revenue at token-issuing L2s collapsed after Dencun (OP $13.6M → $0.6M) |
| Celestia/modular | Fees $1.9M (2023) → $0.3M (2025) | TIA 8.7x in 100 days, then −97% | Fees immaterial relative to valuation |
| DeFi 2022–25 | Uniswap fees about $1.05–1.09B a year in 2024–25; Aave fees a record $908M (2025) | UNI −83%, AAVE −76% from 2021 ATHs | Uniswap protocol revenue was about $0 until 2025 (fee switch: $58M in 2026 YTD) |
| Curve 2022–23 | Fees a record $254M (2023) | CRV −95% to −97% | CRV emissions and veCRV bribes; founder-loan overhang (not quantified here) |
| Restaking 2024–26 | EigenLayer TVL $12–22B for two years | EIGEN −96% | Protocol revenue $0 (DefiLlama) |
| Ethena 2024–25 | USDe $1.56B (TGE) → $14.82B (2025-10-04) | ENA −51% from its 2024 ATH even at the 2025-08-14 high; −95% at the 2026-07-01 low | Fee switch still pending; buyback vote on 95% of net revenue in Aug–Sep 2026 [quoted, below] |
| Circle (equity) | Revenue (DefiLlama estimate) $1.39B (2024) → $2.24B (2025); 30-day revenue $181M (IPO week) → $213M (Oct 2026) | CRCL $263.45 (2025-06-23) → $87.18 (2026-10-21), −67% | Rate-sensitive earnings; supply flat in 2026 |
| pump.fun | Revenue $652.5M (2025), $405M (2026 YTD) | PUMP −38% vs first close (2025-07-12), about +22% vs the $0.004 ICO price | Revenue large; token sold at $4B FDV into a cooling sector |
| **Both up: DeFi 2020** | TVL $1.1B → $177B | Leg-2 EW +1,113% (Nov 2020 → May 2021) | New tokens with growing fees, BTC breaking its ATH, a broad bull |
| **Both up: SOL 2023–25** | Chain fees $23.5M (2023) → $713M (2024) | SOL 27x from the Dec 2022 low | Gas plus staking demand; FTX-overhang supply already cleared |
| **Both up: HYPE 2025–26** | Fees $972M (2025); 30-day fees made new highs into Sept 2026 | HYPE 16x from its TGE to the 2026-09-22 ATH, while BTC was below its ATH | DefiLlama "revenue" $818M (2025) is the revenue counted to holders/buybacks per DefiLlama methodology |

- Ethena fee-switch timeline [quoted]:
  - In Aug–Sep 2026, Ethena put to vote a proposal to use 95% of net revenue from its core businesses to buy ENA once USDe circulation reaches $7.5B. Voting closed on 2026-09-02 — [Cointelegraph](https://regional-front.cointelegraph.com/markets/ena-rises-10-ethena-token-buyback-proposal).
  - ENA fell 4.43% on 2026-09-03 after the vote closed — [Diario Bitcoin](https://www.diariobitcoin.com/analisis/ethena-ena-cae-un-443-este-3-de-septiembre-de-2026-tras-el-cierre-de-la-votacion-del-fee-switch/).
  - USDe supply was $4.68B on 2026-10-20 [computed] — [DefiLlama USDe](https://stablecoins.llama.fi/stablecoin/146).

### Inferences
- **The key test for the stablecoin narrative is "who gets paid".** Stablecoin float income accrues to issuers (Circle and Tether equity or private profits), distributors (exchanges, Coinbase) and, for synthetic dollars, to holders of the yield token. It goes to governance tokens only through explicit buybacks or fee switches. Analogues with that wiring (HYPE; ENA only conditionally) are the only ones where adoption and token prices moved together.
- **Supply growth can swamp revenue growth.** Unlock-heavy, low-float tokens (L2s, EIGEN, XPL) lost value even while usage rose, because circulating supply grew faster than any value captured.

### Gaps
- I did not re-verify buyback shares (for example, the HYPE Assistance Fund share, PUMP or AAVE buybacks) in this session. The DefiLlama "revenue" series depends on methodology: Ethena's revenue series drops from $233M (2024) to $12.8M (2025) while its fees were stable.

## 5. Second legs: which narratives had one, what enabled it, and how long between legs

### Takeaway
Second legs came in three forms:
- **Quick re-accelerations**, 2–5 months after the first top: DeFi Nov 2020, NFT Jul 2021, ENA Sep–Dec 2024, ZEC Mar–Sep 2026. These needed fundamentals that kept growing through the token drawdown, plus a fresh catalyst or a broad bull market.
- **Multi-year revivals**, after −90%+ drawdowns: SOL (about 3 years), XRP/XLM (about 7 years). These were triggered by a new catalyst: memecoin fee growth for SOL, the US regulatory and election shift for XRP/XLM.
- **Fee-driven stair-steps**: HYPE.

Most incentive-led narratives have had no second leg in 12–30 months: algo-stables, Curve-war tokens, L2s, LRTs, AI agents, TON/gaming, BTCfi L2s, Aster-style perps and stablecoin-chain tokens.

### Cited Findings
- Second-leg table [computed] — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=30171&convertId=2781&timeStart=1711929600&timeEnd=1792454400); [DefiLlama](https://stablecoins.llama.fi/stablecoin/146)

| Narrative / token | Leg-1 peak | Trough (depth) | Leg-2 peak | Gap between peaks | What preceded or enabled the second leg (data) |
|---|---|---|---|---|---|
| DeFi | 2020-09-01 ($6.55B cap) | Constant basket −36% at +3m; trough 2020-11-04 | 2021-05-14 ($55.8B; 16.2x from trough) | 8.4 months (restart about 2 months after leg-1 peak) | TVL kept rising ($8.62B → $9.58B in Sep–Nov 2020) and BTC rose +253% |
| NFT/metaverse | 2021-04-16 | Constant basket −53% at +3m | 2021-11-25 | 7.3 months (restart after about 2.5 months) | Axie 30-day fees $380M (Aug 2021); Meta rebrand (2021-10-28). From 2021-10-27 to 2021-11-25: MANA +627%, SAND +996% |
| ENA (Ethena), leg 2 | 2024-04-10 ($1.465) | 2024-09-06 ($0.2045; −86%) | 2024-12-16 ($1.184; +479%) | 8.2 months | USDe $2.55B (2024-09-30) → $5.86B (2024-12-16); sUSDe APY 4.4% (2024-08-15) → 26.6% (2024-12-16); USDtb launch (2024-12-16) |
| ENA, leg 3 | 2024-12-16 | 2025-06-22 ($0.2379; −80%) | 2025-08-14 ($0.7167; +201%) | 8 months | USDe $5.30B (2025-06-30) → $10.97B (2025-08-15); CRCL IPO and GENIUS signing. Still −51% below the 2024 ATH |
| XRP | 2018-01-04 ($3.197) | 2020-03-12 ($0.1396; −96%) | 2025-01-16 ($3.246); ATH close 2025-07-21 $3.556 | about 7 years | +532% between 2024-11-05 and 2025-01-16 |
| XLM | 2018-01-03 ($0.896) | 2020-03-12 ($0.0334; −96%) | 2024-11-23 ($0.515; never regained the 2018 high) | about 6.9 years | +451% in 18 days (2024-11-05 → 11-23) |
| SOL | 2021-11-06 ($258.9) | 2022-12-29 ($9.65; −96%) | 2025-01-18 ($261.9) | about 3.2 years | Chain fees 30x (2023 → 2024); TVL $0.44B → $10.4B |
| HYPE | 2024-12-16 ($27) | 2025-04-06 ($10.22; −62%) | 2025-09-18 ($58.58), then 2026-09-22 ($97.18) after a 2025-12-31 low of $25.43 (−57%) | 9 and 12 months | 30-day fees $35M (2025-04) → $134M (2025-09); $64M (2025-12) → $97M (2026-09) |
| ZEC (privacy) | 2025-11-07 ($642.8; +1,490% from $40.42 on 2025-08-31) | 2026-03-31 ($248.5; −61%) | 2026-09-26 ($1,650) | 10.6 months | See quoted catalysts below |
| Memecoins | 2025-01-19 | −68% at +3m | No new basket high; pump.fun 30-day DEX volume made a new high on 2026-02-13 ($34.5B) | — | Activity revived without token-index highs |

- **XRP's regulatory catalyst** (the SEC case and US election shift) is not documented in this session's sources and is shown here only as timing.
- **ZEC catalysts** [quoted]. On 2026-09-17, altFINS reported ZEC around $1,354, +178% in a month. It cited a breakout above the 2016-era range, a governance vote (NU7) for faster block times and a short squeeze. Its nominal 2016 high was $5,941, so "ATH" refers to the post-2016 range. This is a single source, but consistent with CMC — [altFINS](https://altfins.com/blog/zcash-zec-price-analysis-zec-breaks-its-2016-all-time-high); [Yahoo Finance](https://finance.yahoo.com/news/grayscale-pushes-zcash-zec-180-091824423.html)
- **USDtb** [quoted]. USDtb (over 90% backed by BlackRock's BUIDL) launched on 2024-12-16 — [The Block](https://www.theblock.co/post/331013/ethenas-much-anticipated-usdtb-stablecoin-backed-by-blackrocks-buidl-token-goes-live).
- **WLFI's ENA buy** [quoted; single source, unverified]. One report says World Liberty Financial bought about $500K of ENA, after which ENA rallied 25% over a weekend — [FXStreet](https://www.fxstreet.com/cryptocurrencies/news/ethena-rolls-out-usdtb-stablecoin-backed-by-blackrocks-buidl-fund-ena-eyes-new-all-time-high-202412161905)
- **Meta rebrand** [quoted]. After Facebook's Meta rebrand, MANA rose about 100% in a day to $3.39. By early November MANA had hit about $5.30 and SAND $7.22 — [Decrypt](https://decrypt.co/84914/metaverse-token-up-100-after-facebook-rebrands-to-meta); [Decrypt](https://decrypt.co/86768/ethereum-metaverse-tokens-keep-climbing-mana-sand-hit-all-time-highs).

### Inferences
- **What enabled second legs:**
  1. The core usage metric was still rising during the drawdown: DeFi TVL in autumn 2020, USDe from Sep to Dec 2024, Hyperliquid fees in 2025 and 2026.
  2. A new, distinct catalyst, not a repeat of the first: Meta for metaverse, USDtb plus funding for ENA, regulation for XRP.
  3. Market beta. DeFi and NFT second legs happened while BTC rose 70–250%. HYPE and ZEC are the rare cases with BTC below its ATH, and both had token-specific demand (buybacks; governance and short squeeze).
- **Second legs were led by the first-leg incumbents with cash flow,** not by the late launches: UNI, AAVE and YFI in 2021; SOL; HYPE. In stablecoin terms, a second leg would more likely be led by tokens with a direct claim on stablecoin revenue than by new chain tokens.
- **Typical timing.** The gap from leg-1 peak to leg-2 restart was 2–5 months in bull regimes. A narrative with no restart 12+ months after its peak, and fundamentals flat or down, has historically not come back within the same cycle: L2, LRT, AI agents, GameFi after 2022.

### Gaps
- No sourced data on what drove the 2024–25 XRP/XLM second leg; the timing is computed only.
- I did not establish whether the 2026 ZEC move had fundamental support (shielded-pool usage), because I did not retrieve that data.

## 6. Observable signals that historically marked a narrative's top or exhaustion

### Takeaway
The most reliable top or exhaustion markers in this sample were:
1. **A burst of new listings while incumbents stall.** Sector cap keeps rising because of new listings while the equal-weight index of existing tokens has already peaked (stablecoin 2025, L2s, AI infra).
2. **New TGEs peaking at listing.** 62% of 2025–26 TGEs peaked within 14 days, and post-peak cohorts lost −60% to −90%.
3. **TVL exits after TGE.** TVL fell 50–90% from its peak within 1–9 months of the token event:
   - Blast −49% one month after its TGE.
   - Puffer −67% two months after its TGE.
   - Renzo −75% in 4 months.
   - Plasma −68% in about 2 months.
   - Manta −92% in 9 months.
4. **Infrastructure tokens launching after the application tokens peaked.** Marketplaces, launchpads, RaaS/DA layers and stablecoin chains.
5. **Mainstream validation events, with prices peaking 0–30 days later.** Meta rebrand → 28 days; CRCL IPO → 18 days; GENIUS signing → 9 days.
6. **Capital-raising peaks lagging price peaks by 1–2 quarters.** ICOs in Feb 2018; VC deal count in Q2 2022.

Funding-rate extremes marked tops reliably in 2020–2024, with 30-day BTC funding above 20–45% annualized. They did not in 2025–26, when narrative tops occurred at median funding of 4–11%.

### Cited Findings
- **(a) New-listing-driven cap vs incumbents** [computed] — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=36645&convertId=2781&timeStart=1749081600&timeEnd=1792454400):

  | Narrative | Incumbent EW peak | Sector-cap peak | What pushed the cap peak later |
  |---|---|---|---|
  | Stablecoin 2025 | 2025-07-27 | 2025-09-27 | XPL listing (FDV about $10.4B at launch) |
  | L2 | 2024-03-11 | 2024-12-08 | Unlocks and listings |
  | AI infra | 2024-03-09 | 2024-12-06 | Supply growth |
  | Restaking | ETHFI 2024-03-27 | 2024-12-16 | Mostly new listings: EIGEN, PUFFER, SWELL |

  Plasma's launch facts [quoted] — [The Defiant](https://thedefiant.io/plasma-mainnet-beta-xpl-token-launch).
- **(b) Peak-at-listing and late-TGE damage:** see Section 2 [computed] — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=28480&convertId=2781&timeStart=1719360000&timeEnd=1792454400).
- **(c) Points fatigue and TVL exits after TGE** [computed] — [DefiLlama Blast chain](https://api.llama.fi/v2/historicalChainTvl/Blast); [DefiLlama Manta](https://api.llama.fi/v2/historicalChainTvl/Manta); [DefiLlama Linea](https://api.llama.fi/v2/historicalChainTvl/Linea):
  - **Blast:** TVL peaked at $2.26B on 2024-06-06. It was $1.74B on the TGE eve (2024-06-25), $1.16B a month later (2024-07-26), $760M at +3 months, $477M at +6 months, $92.5M at +12 months and $9.5M on 2026-10-20.
  - **Manta:** TVL peaked at $668M on 2024-03-09, 7 weeks after its TGE, and was $53.5M by 2024-12-08.
  - **Scroll:** $585M peak on 2024-10-17 (TGE 2024-10-11), $281M by 2024-12-08 and $7.8M now.
  - **Linea:** $1.68B peak on 2025-09-21 (TGE 2025-09-10) and $23.7M now.
  - **Taiko:** $341M peak on 2024-12-26 and $0.2M now.
  - **Renzo and Puffer:** see Section 3.
  - **Aster bridge:** $1.57B (2025-10-09) → $479M. **Lighter bridge:** $1.46B (2025-12-18, its TGE month) → $615M.
  - **Plasma:** stablecoins on the chain fell from $4.72B (2025-10-31) to $1.35B (2026-10-20), per the DefiLlama chain series also used by the market_overview note — [DefiLlama Plasma stablecoins](https://stablecoins.llama.fi/stablecoincharts/Plasma).
- **(c) Airdrop reactions** [quoted]:
  - Blast's TVL ATH was about $2.3B on 2024-06-05. BLAST opened at about a $2.9B valuation against $5–10B expectations, and Blast lost about 60% of its TVL less than two months after the airdrop — [The Defiant](https://thedefiant.io/news/defi/blast-struggles-after-its-highly-anticipated-airdrop).
  - After EigenLayer's airdrop announcement on 2024-04-29, about 14,000 wallets (about 13% of users) started withdrawals, though they held only about 0.25% of TVL. The backlash pushed an extra 28M EIGEN distribution — [The Defiant](https://thedefiant.io/news/defi/eigenlayer-withdrawals-accelerate-after-airdrop-backlash); [The Defiant](https://thedefiant.io/news/research-and-opinion/eigenlayer-airdrop-outcry-shows-how-points-are-raising-trader-expectations).
- **(d) "Picks-and-shovels" launches after the application peak** [computed] — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=17081&convertId=2781&timeStart=1641772800&timeEnd=1672444800):

  | Sector peak | Infrastructure token (listing date) | Days to ATH | Return |
  |---|---|---|---|
  | NFT top, 2021-11-25 | LOOKS (2022-01-10) | 9 | −85% at +180d |
  | NFT top | APE (2022-03-17) | 42 | −39% at +180d |
  | L2 price peak, 2024-03-11 | SAGA (2024-04-09) | 0 | −96% at +365d |
  | L2 price peak | AVAIL (2024-07-24) | 0 | −92% at +365d |
  | AI agents | ARC (2024-12-10) | — | −94% at +6m from ATH |
  | AI agents | SWARMS (2024-12-20) | — | −95% at +6m from ATH |
  | Memecoin top | PUMP launchpad ICO (2025-07-12), sold at $4B FDV | — | — |
  | Stablecoin EW peak, 2025-07-27 | XPL (2025-09-25) | — | −95% |
  | Stablecoin EW peak | STBL (2025-09-16) | — | −96% |
  | Stablecoin EW peak | STABLE (2025-12-07) | — | −21% vs first close |

  PUMP ICO terms [quoted] — [Cointelegraph](https://cointelegraph.com/news/pump-fun-ico-raises-500m-sells-out-minutes); [BitMEX](https://www.bitmex.com/blog/the-pumpfun-ico).
- **(e) Mainstream validation → peak lag** [computed] — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1966&convertId=2781&timeStart=1635292800&timeEnd=1638403200); [Yahoo CRCL](https://query1.finance.yahoo.com/v8/finance/chart/CRCL?range=10y&interval=1d):
  - **Meta rebrand (2021-10-28):** the metaverse/NFT cap peaked on 2021-11-25, 28 days later.
  - **CRCL IPO (priced 2025-06-04, trading 2025-06-05):** CRCL's close peaked on 2025-06-23, 18 days later.
  - **GENIUS Act signing (2025-07-18):** the stablecoin-token EW peaked on 2025-07-27, 9 days later.
  - **Libra (June 2019):** no follow-through for payment coins (Section 3).
  - **Gartner:** coverage says the 2018 Emerging Technologies cycle had blockchain at the "peak of inflated expectations" (the year of the Jan 2018 top), and the 2019 cycle had it "sliding into the trough" [quoted] — [CIO Dive](https://www.ciodive.com/news/most-blockchain-applications-sunk-in-the-trough-of-disillusionment-gartn/564613/).
- **(e) Validation-event facts** [quoted]:
  - Circle priced at $31, above its range, and raised about $1.05–1.1B — [Fortune](https://www.fortune.com/2025/06/04/circle-ipo-share-price-31); [Yahoo Finance](https://finance.yahoo.com/news/circle-raises-1-05-billion-230325081.html).
  - Trump signed the GENIUS Act at a White House ceremony on a Friday — [Fox 5 NY](https://www.fox5ny.com/news/genius-stablecoin-act-trump-signs-law). The one-year rulemaking deadline of 2026-07-18 implies enactment on 2025-07-18 — [The Block](https://www.theblock.co/post/408843/us-regulators-miss-genius-acts-one-year-deadline-for-final-stablecoin-rules).
- **(f) Capital-raising lag** [quoted]:
  - ICO funding peaked in February 2018 ($2.38B) and Q1 2018 ($6.3B), after the January 2018 token top — [Finance Magnates](https://www.financemagnates.com/cryptocurrency/news/6-3-billion-ico-funding-q1-2018-already-surpassed-2017/); [e27](https://e27.co/tepid-merchant-acceptance-contributes-crypto-drag-coindesk-20180515/).
  - Galaxy data shows crypto VC at about $8B in Q2 2022, falling to about $5.5B in Q3 2022 — [Blockworks](https://blockworks.com/news/crypto-venture-funding-hits-year-low-in-q3-2022-galaxy). Q2 2022 also held the record deal count, 775 deals — [The Block](https://www.theblock.co/post/303334/galaxy-digital-says-crypto-venture-capital-sentiment-continues-to-improve-despite-market-lull). Both came 6–9 months after the Nov 2021 alt/NFT top.
  - Plasma's deposit cap was raised to $1B and filled in about 30 minutes in June 2025, alongside a $50M sale at a $500M FDV — [The Block](https://www.theblock.co/post/357897/plasma-doubles-its-deposit-cap-clarifies-it-is-eyeing-50m-public-sale-at-500m-fdv).
  - ICE agreed to invest up to $2B in Polymarket on 2025-10-07, at about an $8B pre-money valuation — [The Defiant](https://thedefiant.io/news/defi/ice-invests-usd2-billion-in-polymarket).
- **(g) Funding/leverage at peaks** [computed; Deribit perpetual funding, 30-day average annualized; distribution = weekly samples Jun 2019 – Oct 2026 for BTC: median 4.2%, p90 24.3%, p99 48.3%, max 54.4%] — [Deribit funding API](https://www.deribit.com/api/v2/public/get_funding_rate_history?instrument_name=BTC-PERPETUAL&start_timestamp=1609459200000&end_timestamp=1612137600000):

  | Date (event) | BTC funding | ETH funding |
  |---|---|---|
  | 2020-09-01 (DeFi leg-1 peak) | 14.6% (82nd pct) | 21.2% |
  | 2021-04-13 (BTC top; NFT leg-1 peak 2021-04-16) | 46.1% (99th pct) | 55.5% |
  | 2021-05-12 (DeFi leg 2) | 15.2% | 29.0% |
  | 2021-11-08 (alt-L1/NFT leg 2) | 22.4% (88th pct) | 16.7% |
  | 2022-04-04 (LUNA peak) | 0.1% | 0.0% |
  | 2024-03-11 (L2/AI/points price peak) | 31.3% (>90th pct) | 26.7% |
  | 2024-12-08 (cap peaks) | 24.1% (90th pct) | 23.1% |
  | 2025-01-04 (AI agents) | 11.2% | 7.1% |
  | 2025-01-19 (TRUMP) | 14.0% | 6.9% |
  | 2025-07-27 (stablecoin EW peak) | 10.9% | 4.9% |
  | 2025-09-27 (stablecoin cap peak) | 5.2% | −2.1% |
  | 2025-10-06 (BTC ATH) | 9.6% | 0.7% |
  | 2025-11-07 (ZEC first peak) | 5.5% | 1.1% |
  | 2026-09-22 (HYPE ATH) | 4.4% | 5.2% |
  | 2026-10-20 (now) | 4.8% | 3.1% |

  sUSDe APY (Ethena) [computed] — [DefiLlama yields](https://yields.llama.fi/chart/66985a81-9c51-46ca-9977-42b4fe7bc6df): 55.9% max (2024-03-07); 43.4% (2024-03-15); 26.6% (2024-12-16); 7.3% (2025-08-15); 5.5% (2025-10-09); 3.6–4.8% through 2026.
- **(h) Exchange-listing frenzy:** Binance's 2024 listings were 80% below listing price in a May 2024 review; Animoca put the median 2024 CEX listing near −50% (Section 2) [quoted] — [Cointelegraph](https://cointelegraph.com/news/over-80-binance-token-listings-loss-red); [CryptoSlate](https://cryptoslate.com/tokens-display-up-to-negative-70-median-returns-after-cex-listing-animoca-research/)
- **(i) Mindshare and attention proxies** [quoted]:
  - CoinGecko's 2024 category-page traffic study gave memecoin categories about 31% of investor interest, AI 15.67% (12.58% direct), RWA 8.64% and AI agents 1.17% — [Cointelegraph](https://cointelegraph.com/news/memecoins-top-crypto-investor-interest-2024-coingecko); [ForkLog](https://forklog.com/en/coingecko-identifies-meme-coins-as-leading-trend-among-traders-in-2024/); [CryptoSlate](https://cryptoslate.com/memecoins-capture-31-of-investor-mindshare-in-2024-surging-4x-in-popularity/).
  - In 2025, AI was the second-most-popular narrative at 22.39% — [Crowdfund Insider](https://www.crowdfundinsider.com/?p=256317).
  - Academic work finds a feedback loop: prevalence of a narrative raises returns of related coins, and higher returns draw more searches for that narrative — [Nguyen, Nguyen & Do 2023, Finance Research Letters](https://ideas.repec.org/a/eee/finlet/v56y2023ics1544612323005469.html); [UTS repository](https://opus.lib.uts.edu.au/handle/10453/172387). A Google-attention "hype" factor is priced in crypto returns — [Ling & Zhu 2021](https://inderscience.com/filter.php?aid=117812).
- **(j) Yield compression as a bubble-deflation marker** [quoted]. In the September 2020 DeFi sell-off:
  - Yearn's yUSD vault yield fell from about 150% to 12%, and the average DeFi coin was about −70% from its ATH at the lows — [CryptoSlate](https://cryptoslate.com/defi-yields-crumble-as-curve-sushi-and-other-ethereum-coins-crater/).
  - SUSHI fell 53% in a day — [Decrypt](https://decrypt.co/40972/ethereums-12-plunge-batters-defi-tokens).
  - YAM collapsed within days of launch on a rebase bug — [The Defiant](https://thedefiant.io/yampocalypse-how-extreme-hubris-and).

### Inferences
- **Leverage readings now mislead.** After 2024, delta-neutral basis capital (Ethena-type products, ETF basis) compressed perp funding. Tops in 2025–26 occurred at about median funding, so "funding not extreme" should **not** be read as "not late". sUSDe APY and stablecoin yields are now the better leverage gauge: they collapsed from 26.6% to about 5% between the Dec 2024 and Aug–Oct 2025 tops.
- **The strongest composite top signal** is the combination of:
  - new listings carrying the sector cap while incumbents fall;
  - infrastructure tokens launching into a narrative whose application tokens already peaked;
  - TGE TVL halving within 90 days.

  All three were present in the 2025 stablecoin first leg: XPL, STBL and STABLE after the July peak; Plasma's stablecoin deposits down 70%.

### Gaps
- No Kaito mindshare time series or Kaito decay study was found. I used CoinGecko web-traffic shares and academic attention studies as proxies.
- No Google Trends series could be retrieved.
- VC funding by narrative (for example, stablecoin-infrastructure rounds in 2025–26) was not computed, because DefiLlama's raises endpoint is paid. Galaxy's Q1 2022 total was not found.

## 7. Research and frameworks on narrative cycles and token launches

### Takeaway
Published frameworks converge on four points:
1. Low-float/high-FDV supply overhang is the main structural reason token prices decouple from usage (Binance Research 2024).
2. Most recent TGEs and airdrops decline within weeks (Keyrock 2024; Memento 2025; Animoca 2024).
3. Hype cycles follow a peak-of-expectations to trough pattern that precedes real adoption (Gartner applied to blockchain in 2018–19).
4. Attention and returns reinforce each other, so narratives overshoot (academic attention literature).

I found no dedicated, citable Messari, Delphi or Kaito study of narrative life cycles in this session.

### Cited Findings
- **Binance Research (2024-05-17):** $155B of unlocks over 2024–2030; 2024 launches averaged 12.3% MC/FDV, implying about $80B of new demand needed. It advised judging tokens on FDV/revenue and TVL. Binance then adjusted listing criteria toward moderate float [quoted] — [ForkLog](https://forklog.com/en/binance-highlights-155-billion-token-unlock-overhang/); [Cointelegraph](https://cointelegraph.com/news/binance-urges-small-medium-projects-high-fdv-trend)
- **Memento Research (data to 2025-12-20):** 84.7% of 118 TGEs below launch; median FDV −71%; 0 of 28 launches with FDV ≥ $1B above launch, median −81% [quoted] — [ForkLog](https://forklog.com/en/85-of-tokens-launched-in-2025-fell-below-initial-prices/)
- **Keyrock (2024 airdrops):** 88% of 62 airdrops declined, most within 15 days. FDV management mattered more than airdrop size, and one token with a 70% airdrop allocation rose [quoted] — [DL News](https://www.dlnews.com/articles/snapshot/keyrock-study-says-most-token-airdrops-crash-after-launch); [BeInCrypto](https://beincrypto.com/majority-airdrop-tokens-crash-within-15-days/)
- **Gartner:** the 2019 Hype Cycle for Blockchain put blockchain sliding into the Trough of Disillusionment and expected a climb out from 2021, with full scalability by about 2028 [quoted] — [Gartner press release](https://www.gartner.com/en/newsroom/press-releases/2019-10-08-gartner-2019-hype-cycle-shows-most-blockchain-technologies-are-still-five-to-10-years-away-from-transformational-impact); [CIO Dive](https://www.ciodive.com/news/most-blockchain-applications-sunk-in-the-trough-of-disillusionment-gartn/564613/)
- **Narrative attention (academic):** Nguyen, Nguyen & Do (2023, FRL) document narrative-prevalence → returns → attention feedback, using the post-ChatGPT AI-token rally. Ling & Zhu (2021) build a market/size/hype three-factor model [quoted] — [IDEAS/RePEc](https://ideas.repec.org/a/eee/finlet/v56y2023ics1544612323005469.html); [Inderscience](https://inderscience.com/filter.php?aid=117812)
- **Galaxy's post-Dencun review:** bot-driven activity and high failure rates on L2s. The point is that adoption metrics can be inflated by automated, low-value activity [quoted] — [ForkLog](https://forklog.com/en/dencun-update-spurs-rise-in-failed-transactions-on-ethereums-l2-networks/amp)
- **Liquidity-mining origins (DeFi Summer):**
  - Compound began distributing COMP to lenders and borrowers in June 2020 (dated 15 June 2020 in some sources; others say May). Balancer and Rarible copied the model [quoted] — [DeFi Prime](https://defiprime.com/defi-yield-farming); [ConsenSys](https://consensys.io/blog/impact-of-liquidity-mining-on-defi-users).
  - CMC's first COMP close was $93.2 (2020-06-16) and its close was $337.0 on 2020-06-21, a 3.6x in 5 days, before COMP drifted lower [computed] — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=5692&convertId=2781&timeStart=1592179200&timeEnd=1596240000).

### Inferences
- **Mapping Gartner onto token narratives:**
  - "Innovation trigger" ≈ the first protocol or primitive (COMP mining, ARB TGE, CRCL IPO).
  - "Peak of inflated expectations" ≈ the synchronized ATH cluster and the mainstream validation event.
  - "Trough" ≈ the −80–95% drawdown while usage keeps rising.
  - "Slope of enlightenment" ≈ a second leg only where value accrual exists.

  On this map the 2025 stablecoin token cohort went through trigger and peak in June–September 2025 and the trough in 2026.

### Gaps
- Messari and Delphi narrative-cycle pieces, Kaito narrative-mindshare studies and the Gartner placements for NFTs and Web3 (2021–2023) were not found or retrieved in this session. I did not re-verify K33's long-run altcoin study from the earlier background note.

## 8. The 2025 first leg of the stablecoin wave (immediate predecessor of the 2026 period)

### Takeaway
The first stablecoin leg was a short, validation-driven wave:
- The CRCL IPO (2025-06-05) and the GENIUS signing (2025-07-18) produced an equity spike (CRCL 8.5x its IPO price in 18 days) and a token rally that peaked within 9 days of the signing.
- A late "infrastructure" TGE cluster followed (STBL 2025-09-16, XPL 2025-09-25, FF 2025-09-29, STABLE 2025-12-07). It pushed the sector cap to its peak on 2025-09-27, right before the 2025-10-06 BTC top and the 10/10 crash.
- Twelve months later the token basket is −42% (cap) / −55% (EW), XPL −95% and CRCL −67% from its peak.
- Fundamentals kept growing for another 2–8 months and then stalled: total stablecoin supply rose from $246.9B (IPO day) to $301.4B (2025-10-10), peaked at $315.5B (2026-05-17) and was $303.7B on 2026-10-20 (+0.8% year on year).

By the historical templates, the 2025 token leg is **finished**. Fundamentals are now at the "plateau after the peak" stage typical of DeFi in 2022 and L2s in 2025.

### Cited Findings
- **CRCL** [computed] — [Yahoo CRCL](https://query1.finance.yahoo.com/v8/finance/chart/CRCL?range=10y&interval=1d):
  - First close $83.23 on 2025-06-05 against a $31 IPO price; intraday high $103.75 that day.
  - **Peak close $263.45 on 2025-06-23** (intraday $298.99).
  - $223.78 on 2025-07-18 (GENIUS signing), $139.23 on 2025-08-14, $79.30 on 2025-12-31.
  - **Low close $50.23 on 2026-02-05 (−81%)**; $87.18 on 2026-10-21 (−67% from peak, +181% vs the IPO price).
- **CRCL IPO terms** [quoted]: priced at $31 on 2025-06-04, above a raised range ($24–26, then $27–28); 34M shares; about $1.05–1.1B raised — [Decrypt](https://decrypt.co/323795/stablecoin-giant-circle-raises-1-billion-ipo-nyse-debut?amp=1); [Yahoo Finance](https://finance.yahoo.com/news/circle-raises-1-05-billion-230325081.html)
- **Token basket** [computed] — [CMC ENA](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=30171&convertId=2781&timeStart=1749081600&timeEnd=1792454400); [CMC XPL](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=36645&convertId=2781&timeStart=1758758400&timeEnd=1792454400):
  - **Incumbents (ENA, USUAL, SKY, SYRUP, FXS, CRV, HUMA):** EW +45% to its peak on 2025-07-27; −60% at +6m and −75% at +12m.
  - From 2025-06-04 to 2025-07-27: ENA +113%, CRV +60%, SYRUP +37%, SKY +30%, FXS +21%, USUAL −7%.
  - From 2025-07-18 to 2025-10-20: CRV −44%, FXS −61%, USUAL −63%, SKY −30%, SYRUP −15%, ENA +16%.
  - **Full 12-token cap:** $4.91B (2025-06-05) → $10.41B (2025-09-27); constant basket −57% at +3m, −69% at +6m, −42% at +12m; $5.80B on 2026-10-20.
  - **ENA:** $0.2379 (2025-06-22) → $0.7167 (2025-08-14) → $0.547 (2025-10-09) → $0.369 (2025-10-11) → $0.20 (2025-12-31) → **$0.071 (2026-07-01; −95% from the 2024 ATH)** → $0.196 (2026-10-20).
  - **XPL:** first close $1.27 (2025-09-25) → $1.63 peak (2025-09-27) → $0.747 (2025-10-09, already −54% before the crash) → $0.161 (2025-12-31) → $0.078 (2026-10-20; −95%).
  - **STBL:** $0.57 peak (2025-09-24) → $0.025 (−96%). **WLFI:** $0.234 (2025-09-01) → $0.056 (−76%). **USUAL** (Nov 2024 TGE): ATH $1.44 (2024-12-19) → $0.0107 (−99%). **RESOLV:** its TGE day (2025-06-10) was its ATH, and it is −95%. **FF:** $0.283 (2025-09-29) → $0.111. **STABLE:** $0.033 (2025-12-07) → $0.026.
  - Best relative holders: **SKY** (+15% vs first close; −22% from its 2026-10-04 ATH) and **SYRUP** (−24% vs first close).
- **Plasma launch** [quoted]:
  - Mainnet beta and XPL launched on 2025-09-25 with a claimed TVL above $2B. At press time XPL was about $1, with a market cap of about $1.9B and an FDV of about $10.4B, on a 10B supply with about 1.8B circulating — [The Defiant](https://thedefiant.io/plasma-mainnet-beta-xpl-token-launch); [Blockworks](https://blockworks.co/news/plasma-announces-mainnet-beta).
  - The June 2025 public sale was $50M at a $500M FDV — [The Block](https://www.theblock.co/post/357897/plasma-doubles-its-deposit-cap-clarifies-it-is-eyeing-50m-public-sale-at-500m-fdv).
  - Plasma's stablecoin TVL fell about 68% from October to late November 2025 as farming reversed — [Phemex](https://phemex.com/news/article/plasma-xpl-plummets-85-amid-declining-tvl-and-stablecoin-supply-38743).
- **Fundamentals** [computed] — [DefiLlama stablecoins](https://stablecoins.llama.fi/stablecoincharts/all); [DefiLlama USDC](https://stablecoins.llama.fi/stablecoin/2); [DefiLlama USDe](https://stablecoins.llama.fi/stablecoin/146); [DefiLlama Circle fees](https://api.llama.fi/summary/fees/circle?dataType=dailyFees):
  - **Total supply:** $203.8B (2024-12-31) → $246.9B (2025-06-05) → $257.7B (2025-07-18) → $293.3B (2025-09-27) → $301.4B (2025-10-10) → $304.4B (2025-12-31) → **peak $315.5B (2026-05-17)** → $303.7B (2026-10-20).
  - **USDC:** $61.1B (2025-06-05) → $75.3B (2025-10-10) → peak $79.6B (2026-03-18) → $72.3B. **USDT:** $154.5B → $177.4B → peak $190.4B (2026-05-20) → $183.2B.
  - **USDe:** $5.30B (2025-06-30) → $10.97B (2025-08-15) → **peak $14.82B (2025-10-04)** → $9.56B (2025-10-31) → $6.30B (2025-12-31) → $4.68B (2026-10-20).
  - **Circle 30-day revenue (DefiLlama estimate):** $181M (2025-06-05) → $201M (2025-09-27) → $213M (2026-10-20). **Tether:** $5.71B for 2025.
  - The market_overview note in this folder (DefiLlama, slightly different aggregation) has the 2026 ATH at $317.1B on 17 May 2026 and 2026 YTD at +0.04%.
- **Market context** [computed] — [CMC BTC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1&convertId=2781&timeStart=1749081600&timeEnd=1792454400):
  - BTC: $101.6K (2025-06-05) → $118.0K (2025-07-18) → ATH close $124.8K (2025-10-06) → $87.5K (2025-12-31) → $58.6K (2026-06-30) → $82.9K (2026-10-20).
  - ETH peaked at $4,831 on 2025-08-22.
  - Deribit BTC funding was 10.9% at the stablecoin EW peak and 5.2% at the cap peak.

### Inferences
- **On every timing template, the 2025 token leg is complete.**
  - Its peak came 1.7–3.7 months after the trigger, the fast end.
  - Its infrastructure TGEs came after the incumbents' peak.
  - TVL at the new chains deflated within 2 months.
  - At +12 months the basket sits at −42% / −55%, the normal range for finished narratives.

  Whether a 2026 second leg is under way depends on the second-leg conditions in Section 5 (rising fundamentals during the drawdown plus a new catalyst). Supply growth stalling at about 0% year on year is the main **negative** reading on those conditions. GENIUS implementation, an ENA-style fee switch or new distribution channels would be candidate catalysts; other notes cover these.
- **The 2025 leg was heavily confounded by market beta.** Its token peak coincided with the cycle top (BTC ATH 2025-10-06, then 10/10). Any 2026 comparison should be expressed relative to BTC and ETH.

### Gaps
- I did not analyze 2026 stablecoin projects or their TGEs, by design; other researchers cover them. No sourced breakdown of stablecoin-sector VC funding for 2025–26 was retrieved.

## 9. Checklist: measurable "late-stage / exhaustion" and "second-leg" signals to apply to the stablecoin narrative in October 2026

### Takeaway
The table below turns the history into tests with thresholds. The historical benchmark column is sourced in Sections 1–8. The last column shows what the 2025 first leg or current market data read now, where I computed it. Other researchers should fill the 2026-project rows.

### Cited Findings
- Checklist [benchmarks computed or quoted in Sections 1–8; current readings computed from CMC, DefiLlama and Deribit as of 2026-10-20] — [CMC](https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=36645&convertId=2781&timeStart=1758758400&timeEnd=1792454400); [DefiLlama stablecoins](https://stablecoins.llama.fi/stablecoincharts/all); [Deribit](https://www.deribit.com/api/v2/public/get_funding_rate_history?instrument_name=BTC-PERPETUAL&start_timestamp=1789776000000&end_timestamp=1792454400000)

**A. Late-stage / exhaustion signals** (each "yes" adds weight)

| # | Signal | How to measure | Historical late-stage benchmark | Reading for stablecoin tokens, Oct 2026 (where known) |
|---|---|---|---|---|
| A1 | Elapsed time since trigger | Months since the narrative's trigger | Fast waves peaked 2–4 months after the trigger; slow, infrastructure-heavy ones 10–14 months | CRCL IPO plus 16.5 months |
| A2 | Incumbents vs sector cap | EW of tokens listed before the wave vs cap including new listings | Cap peak 2–9 months after the EW peak (stablecoin 2025, L2, AI infra) | 2025: EW peak 2025-07-27, cap peak 2025-09-27 |
| A3 | Share of TGEs launched late | Share of the narrative's TGEs in the last third of the run-up or after the peak | 67–87% in past waves | 4 of 5 of the 2025 cohort (80%) |
| A4 | Post-TGE returns of the latest 5–10 TGEs | Median +30/+90/+180-day return from first close; share below first close | Late or post cohorts −40% to −90% at +180d; 2025 base rate 84.7–86% below launch; 62% peak within 14 days | 2025 stablecoin TGEs: late cohort −82% at +180d; XPL −95%, STBL −96% |
| A5 | FDV at TGE | FDV vs fee run-rate | FDV ≥ $1B: 0 of 28 2025 TGEs above launch (Memento) | XPL launched at about $10.4B FDV |
| A6 | TVL/deposit retention after TGE | TVL at TGE + 30/90 days vs the pre-TGE peak | Blast −49% at +1m and −66% at +3m; Renzo −75% in 4 months; Linea −99% by Oct 2026 (13 months after its TGE) | Plasma stablecoins −71% ($4.72B on 2025-10-31 → $1.35B on 2026-10-20) |
| A7 | Infrastructure launches after the application peak | Launchpads, chains and frameworks listing after the application tokens' ATH | LOOKS/APE after the NFT top; SAGA/AVAIL after the L2 top; ARC/SWARMS after AI agents; PUMP after memes | XPL, STBL, STABLE after the July 2025 EW peak |
| A8 | Mainstream validation → peak | Days from the IPO, landmark law or Big-Tech move to the token or equity peak | 0–30 days (Meta 28, CRCL 18, GENIUS 9) | Done in 2025; watch for a "GENIUS effective date" or rule-finalization pop |
| A9 | Capital raising still rising while prices fall | VC deal count/size, IPO filings, mega-sales vs the token index | ICO peak 1 month after the token top; VC deal-count record 7 months after the 2021 top | Not computed for 2026 (gap) |
| A10 | Fundamentals momentum stalling | YoY and 3-month growth of the core metric, e.g. stablecoin supply | DeFi TVL peaked 6 months after tokens; USDe 7 weeks after ENA | Supply +0.8% YoY (2025-10-10 → 2026-10-20) vs +49% in 2025; USDe −68% from peak |
| A11 | Leverage/yield | Deribit 30-day funding; sUSDe APY | 2020–24 tops: BTC funding ≥ 20–46% (≥ 88th pct); sUSDe 27–56%. 2025–26 tops at median funding, so weak evidence | BTC 4.8%, ETH 3.1%, sUSDe 4.8%: no froth |
| A12 | Breadth blow-off | Share of sector tokens making ATHs within ±30 days | 71–85% at the synchronized tops (2018 payments 85%, DeFi leg 1 77%, NFT leg 1 75%, AI agents 71%) | 2025: 4 of 12 (staggered) |

**B. Second-leg signals** (historically needed together)

| # | Signal | How to measure | Historical benchmark | Reading, Oct 2026 |
|---|---|---|---|---|
| B1 | Core metric kept rising through the token drawdown | Stablecoin supply, issuer revenue, payments volume during the token bear | DeFi TVL +11% during the Sep–Nov 2020 drawdown; USDe +130% Sep–Dec 2024; HYPE fees rising | Supply flat to slightly down since May 2026; Circle 30-day revenue $213M, above its 2025 level |
| B2 | A new, distinct catalyst | A dated event not tied to the first leg's trigger | Meta (NFT leg 2), USDtb plus funding (ENA leg 2), regulatory shift (XRP 2024–25), NU7 (ZEC 2026) | Candidates (other notes): GENIUS final rules or effective date, fee switches |
| B3 | Direct value accrual turned on | A buyback, burn or fee switch funded by stablecoin revenue | HYPE (fees → buybacks) is the only "both up" case without a broad bull; UNI fee switch only in 2025–26 | ENA buyback vote closed 2026-09-02 (needs USDe ≥ $7.5B; USDe is $4.68B) |
| B4 | Leaders are cash-flow incumbents, not new chains | Relative strength of revenue-linked tokens vs new TGEs | Second legs were led by UNI/AAVE/YFI, SOL and HYPE | SKY and SYRUP held up best in 2025–26 |
| B5 | Timing | Months from leg-1 peak to the restart | Bull regimes: restart 2–5 months after the peak. No restart within 12 months → usually no same-cycle comeback (L2, LRT, AI agents) | Leg-1 peak Jul–Sep 2025, so 13–15 months without a basket high |
| B6 | Market beta | BTC above its prior ATH; BTC dominance falling | DeFi and NFT second legs came with BTC +70–250%; ZEC and HYPE are exceptions with token-specific demand | BTC $82.9K vs $124.8K ATH (−34%) |
| B7 | Yield/funding re-expansion | sUSDe APY and funding rising from lows | sUSDe 4.4% → 26.6% before ENA leg 2 (Aug → Dec 2024) | sUSDe 4.8%: not yet |

### Inferences
- **The 2025 token leg reads "finished".** Applying the checklist to what I measured, most late-stage tests are met: A1–A7 and A10. The leverage test (A11) and the breadth blow-off test (A12) are not, but A11 lost reliability after 2024.
- **Second-leg conditions are not yet met.** Fundamentals are flat, not rising (B1). Direct value accrual is pending (B3). The usual restart window has passed (B5). BTC is well below its ATH (B6). Yields have not re-expanded (B7).
- **What would change the read.** Historically, a "second leg" call for the stablecoin narrative would require two of the following:
  - supply growth re-accelerating (for example, more than 3–5% over 3 months);
  - a dated catalyst;
  - token-level buybacks funded by stablecoin revenue;
  - BTC beta;

  plus new 2026 TGEs that hold their listing price beyond 30–90 days, which is rare (14–16% base rate in 2025).

### Gaps
- Kaito mindshare, Google Trends and VC funding series for 2026 were not available. A9 and any mindshare-decay test therefore need other researchers' data.
- The 2026 project-level TGE readings (A3–A6 for 2026 launches) belong to the researchers covering current projects.
