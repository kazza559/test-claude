# Perp DEX tokens with TGE between Jul 1 and Dec 31, 2025: FDV at TGE vs. maximum FDV after TGE (cohort 2025H2)

Data pulled Oct 27–28, 2026. Method notes, applied to every row below:
- **TGE / basis (a)** = first recorded price on DefiLlama (`coins.llama.fi/prices/first/coingecko:{id}`, sourced from CoinGecko). This can land a few hours after the real first trade, so the venue opening prints are listed next to it where I have them.
- **Basis (b)** = day-1 close. That is the DefiLlama price nearest 00:00 UTC after the TGE day (`coins.llama.fi/chart/...period=1d`), cross-checked against exchange daily candles where available.
- **ATH** = CoinGecko intraday ATH (`api.coingecko.com/api/v3/coins/{id}` or `/coins/markets?category=decentralized-perpetuals`). In several cases CoinGecko stamps the ATH before its own chart begins, i.e. on minute-one listing prints. These are flagged.
- **"After day 7"** = the highest DefiLlama daily close at least 7×24 h after the first print, divided by the day-1 close.
- **FDV** = price × max supply, unless stated otherwise.
- Exchange candles were pulled from public APIs: Binance spot via the data-api.binance.vision mirror, Gate, KuCoin, MEXC, Bitget, OKX, Coinbase, Upbit and Hyperliquid. Binance futures (HTTP 451) and Bybit (HTTP 403) were geo-blocked from this environment.
- Scripts are in /tmp/claude-0/-home-user-test-claude/2ad751b0-58d6-5348-a96a-1b74151bb386/scratchpad/cohortC1_scripts/. Raw downloads are in /tmp/claude-0/-home-user-test-claude/2ad751b0-58d6-5348-a96a-1b74151bb386/scratchpad/cohortC1_raw/, including analysis_rows.json with every computed metric.

## Which perp DEX tokens TGE'd between Jul 1 and Dec 31, 2025 (and which candidates are excluded)?

### Takeaway
I found 12 perp-DEX tokens and 9 borderline tokens whose first public trading fell inside the window.
- **Large caps:** Aster (ASTER), Avantis/now "Veranta" (AVNT) and Lighter (LIT).
- **Mid/small caps:** Tradoor (TRADOOR), Quanto (QTO), Superp (SUP), Full Moon/Moonlander (FM), DESK, Amped (AMPED), Artura (ARA), Nemesis (NEMESIS) and the meme-perp Degen Perp Dex (PDGN).
- **Borderline:** VOOI (perp aggregator), SparkDEX, Overlay, Lnfi, Nomina, Omnipair, Kodiak, PLUTO and Hyperbot.

Most seed-list names (edgeX, Paradex, GRVT, StandX, Pacifica, Ostium, Variational, Extended, Hibachi, Ethereal, Reya, Vest, Nado, Bullet, Perpl, Sunperp) either launched in 2026 or had no tradable token as of Oct 2026.

### Cited Findings
- **Discovery method.** CoinGecko categories "Perpetuals" (`decentralized-perpetuals`) and "Derivatives" (`decentralized-derivatives`) held 170 coins in total. Each was date-checked with DefiLlama's first-price endpoint. Sources: [CG perpetuals category](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=decentralized-perpetuals&order=market_cap_desc&per_page=250&page=1), [CG derivatives category](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=decentralized-derivatives&order=market_cap_desc&per_page=250&page=1), [DefiLlama first prices](https://coins.llama.fi/prices/first/coingecko:aster-2,coingecko:avantis,coingecko:lighter). I cross-checked against DefiLlama's protocol list (Derivatives/Options/Synthetics protocols that have a gecko_id) — [DefiLlama protocols](https://api.llama.fi/protocols).
- **In-window perp DEX tokens (first DefiLlama print, UTC).** Each date comes from `https://coins.llama.fi/prices/first/coingecko:{id}`.
  - [QTO](https://coins.llama.fi/prices/first/coingecko:quanto): 2025-07-10. Solana perp DEX, quanto.trade ([CG](https://api.coingecko.com/api/v3/coins/quanto)).
  - [DESK](https://coins.llama.fi/prices/first/coingecko:desk): 2025-07-25. Arbitrum perp infrastructure combining pool and order-book systems ([CG](https://api.coingecko.com/api/v3/coins/desk)).
  - [AMPED](https://coins.llama.fi/prices/first/coingecko:amped-finance): 2025-07-25. GMX-style spot+perps on Sonic, Base, LightLink, BNB, Berachain and Superseed ([DefiLlama](https://defillama.com/protocol/amped-finance)).
  - [SUP](https://coins.llama.fi/prices/first/coingecko:superp): 2025-08-05. "perp DEX for any meme, up to 10,000x", formerly Vanilla Finance, BNB Chain ([DefiLlama](https://defillama.com/protocol/superp)).
  - [FM](https://coins.llama.fi/prices/first/coingecko:full-moon): 2025-08-07. Moonlander, an oracle-based perp exchange on Cronos ([CG](https://api.coingecko.com/api/v3/coins/full-moon)).
  - [TRADOOR](https://coins.llama.fi/prices/first/coingecko:tradoor): 2025-09-04. TON "NDMM" perps up to 100x, Binance Alpha/Binance Wallet IDO ([CG](https://api.coingecko.com/api/v3/coins/tradoor)).
  - [AVNT](https://coins.llama.fi/prices/first/coingecko:avantis): 2025-09-09. Base, oracle/pool-based RWA perps. Now branded "Veranta" on CoinGecko and DefiLlama ([CG](https://api.coingecko.com/api/v3/coins/avantis), [DefiLlama](https://defillama.com/protocol/avantis)).
  - [ASTER](https://coins.llama.fi/prices/first/coingecko:aster-2): 2025-09-17. BNB Chain and other chains, perps. Rebrand/migration of APX (ApolloX) after the Astherus merger ([CG](https://api.coingecko.com/api/v3/coins/aster-2); [1inch](https://1inch.com/tokens/bsc/aster)).
  - [ARA](https://coins.llama.fi/prices/first/coingecko:ara): 2025-09-26. Artura, "Bitcoin's fastest perp DEX", synthetic model ([CG](https://api.coingecko.com/api/v3/coins/ara)).
  - [PDGN](https://coins.llama.fi/prices/first/coingecko:degen-perp-dex): 2025-10-14. Four.meme meme-perp DEX on BNB ([CG](https://api.coingecko.com/api/v3/coins/degen-perp-dex)).
  - [NEMESIS](https://coins.llama.fi/prices/first/coingecko:nemesis-2): 2025-10-31. Base perp DEX, nemesis.trade ([CG](https://api.coingecko.com/api/v3/coins/nemesis-2)).
  - [LIT](https://coins.llama.fi/prices/first/coingecko:lighter): 2025-12-30. Ethereum zk-rollup order book ([The Block](https://www.theblock.co/post/383940/lighter-native-token-lit)).
- **Borderline (data collected).**
  - [VOOI](https://coins.llama.fi/prices/first/coingecko:vooi): 2025-12-18. "a cross-chain perpetual DEX aggregator" ([OurCryptoTalk](https://ourcryptotalk.com/news/vooi-team-responds-after-86-percent-drop-after-tge)).
  - [SPRK](https://coins.llama.fi/prices/first/coingecko:sparkdex): 2025-07-30. Flare DeFi hub with a perp exchange plus spot ([CG](https://api.coingecko.com/api/v3/coins/sparkdex)).
  - [LN](https://coins.llama.fi/prices/first/coingecko:lnfi-network): 2025-07-25. Lightning multi-asset DeFi, tagged derivatives/perps ([CG](https://api.coingecko.com/api/v3/coins/lnfi-network)).
  - [OVL](https://coins.llama.fi/prices/first/coingecko:overlay-protocol): 2025-08-14. Long/short any data stream by minting/burning OVL; oracle-based, not classic perps ([CG](https://api.coingecko.com/api/v3/coins/overlay-protocol)).
  - [OMFG](https://coins.llama.fi/prices/first/coingecko:omnipair): 2025-08-20. Solana spot+margin, categorised "Lending" by DefiLlama ([DefiLlama](https://defillama.com/protocol/omnipair)).
  - [BOT/Hyperbot](https://coins.llama.fi/prices/first/coingecko:hyperbot): 2025-09-02. Hyperliquid trading bot.
  - [NOM](https://coins.llama.fi/prices/first/coingecko:nomina): 2025-10-01. Nomina, "unified trading platform … across DEXs". New token of the former Omni Network ([CG](https://api.coingecko.com/api/v3/coins/nomina)).
  - [PLUTO](https://coins.llama.fi/prices/first/coingecko:pluto-3): 2025-10-25. Identity unverified.
  - [KDK](https://coins.llama.fi/prices/first/coingecko:kodiak-finance): 2025-12-23. Berachain DEX listed in CoinGecko's Perpetuals category.
- **Tokens whose TGE was in 2026** (first DefiLlama print):
  - [edgeX EDGE](https://coins.llama.fi/prices/first/coingecko:edgex): 2026-03-31.
  - [Paradex DIME](https://coins.llama.fi/prices/first/coingecko:paradex): 2026-03-05 (the TGE was guided to late Feb/early Mar 2026 — [Decrypt/Chainwire](https://decrypt.co/356482/paradex-confirms-dime-tge-timeline-and-expands-airdrop-allocation-following-xp-season-2-conclusion)).
  - [GRVT](https://coins.llama.fi/prices/first/coingecko:grvt): 2026-07-30 ([KuCoin news](https://www.kucoin.com/news/flash/grvt-announces-tge-details-grvt-airdrop-claims-open-on-july-30)).
  - [LeverUp LV](https://coins.llama.fi/prices/first/coingecko:leverup): 2026-03-26.
  - [RollX ROLL](https://coins.llama.fi/prices/first/coingecko:roll-2): 2026-01-16.
  - [Ranger RNGR](https://coins.llama.fi/prices/first/coingecko:ranger): 2026-01-10.
  - [Fogo](https://coins.llama.fi/prices/first/coingecko:fogo): 2026-01-15.
  - [Infinex INX](https://coins.llama.fi/prices/first/coingecko:infinex-2): 2026-01-30.
  - [Rails](https://coins.llama.fi/prices/first/coingecko:rails): 2026-02-04.
  - [Flying Tulip FT](https://coins.llama.fi/prices/first/coingecko:flying-tulip): 2026-02-23.
  - [ETHGas GWEI](https://coins.llama.fi/prices/first/coingecko:ethgas-2): 2026-01-21.
- **Excluded because TGE predates the window:**
  - [MYX](https://coins.llama.fi/prices/first/coingecko:myx-finance): 2025-05-06. It later ran to an ATH of $19.03 on 2025-09-10 ([CG](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=myx-finance)).
  - [KiloEx](https://coins.llama.fi/prices/first/coingecko:kiloex): 2025-03-27.
  - [Flash Trade FAF](https://coins.llama.fi/prices/first/coingecko:flash-trade): 2025-04-16.
  - [Derive](https://coins.llama.fi/prices/first/coingecko:derive): 2025-01-15.
  - [Bluefin](https://coins.llama.fi/prices/first/coingecko:bluefin): 2024-12-11.
  - [SynFutures](https://coins.llama.fi/prices/first/coingecko:synfutures): 2024-12-06.
  - [Storm Trade](https://coins.llama.fi/prices/first/coingecko:storm-trade): 2024-10-18.
  - [Orderly](https://coins.llama.fi/prices/first/coingecko:orderly-network): 2024-08-25.
  - [Holdstation](https://coins.llama.fi/prices/first/coingecko:holdstation): 2023-11-27. Its new "holdstation-2" HOLD token was first priced on [2025-10-16](https://coins.llama.fi/prices/first/coingecko:holdstation-2), a migration I did not analyse (see Gaps).
  - ApeX: 2022, excluded per brief.
- **Excluded because not a perp DEX:**
  - [Sigma Money](https://defillama.com/protocol/sigma-money): CDP/tranching protocol, first print 2025-10-21.
  - [Kinetiq KNTQ](https://coins.llama.fi/prices/first/coingecko:kinetiq): HYPE liquid staking, first print 2025-11-27. Covered by a separate KNTQ researcher.
  - Nirvana ANA, SpookySwap BOO, Origami hOHM and Hyperion RION also appear in the category/search results but are not perp DEXs ([discovery rows](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=decentralized-derivatives&per_page=250)).
- **Seed names with no tradable token on CoinGecko as of Oct 27, 2026:**
  - Search returned no token: Pacifica, Ostium, Extended, Hibachi, Ethereal, Vest, Nado, Perpl, Sunperp, Decibel, GTE ([CG search](https://api.coingecko.com/api/v3/search?query=pacifica)).
  - CoinGecko page exists but has no price: Variational (VAR), Reya (REYA), Zeta (Z) ([CG search](https://api.coingecko.com/api/v3/search?query=variational)).
  - StandX: only its DUSD stablecoin is listed ([CG search](https://api.coingecko.com/api/v3/search?query=standx)).
  - Reya held a CoinList sale on Nov 25 – Dec 2, 2025 with a "Q4 2025" TGE target that slipped; as of Oct 2026 the TGE date is unconfirmed ([ICO Drops](https://icodrops.com/reya); [Bitrue](https://www.bitrue.com/blog/reya-airdrop-guide)).
  - edgeX's TGE on Mar 31, 2026 is also reported by [CoinCodeCap](https://coincodecap.com/best-perp-dex-airdrops-top-platforms-worth-farming).

### Inferences
- The window's large-cap perp DEX TGEs are just three tokens: AVNT, ASTER and LIT. The rest of the cohort is mostly sub-$50M FDV launches that CoinGecko lists but news rarely covers. Including them is what removes survivorship bias.
- Several of the "perp DEX wars" headline names (Pacifica, Variational, Extended, Ostium, Ethereal, StandX, Hibachi) had not launched tokens by late Oct 2026. Nothing in this cohort can speak for them.

### Gaps
- Not analysed (identified late, CoinGecko rate limits):
  - [Tea-REX TREX](https://coins.llama.fi/prices/first/coingecko:tea-rex) (Sei derivatives, first print 2025-11-29).
  - [Apollon APO](https://coins.llama.fi/prices/first/coingecko:apo) (Sei synthetics, 2025-07-30).
  - [BaseVol ATM](https://coins.llama.fi/prices/first/coingecko:a-t-m-by-basevol) (options, 2025-10-23).
  - The Holdstation HOLD v2 migration (2025-10-16).
- Perp tokens absent from CoinGecko's Perpetuals/Derivatives categories and from DefiLlama's Derivatives gecko_id mapping would have been missed. Coverage of tiny BNB/Solana launchpad perp tokens is incomplete.
- PLUTO's project identity is unverified. jojo-3, jojoworld, helix-2 and based-coin (first prints Aug–Oct 2025) were not classified.

## Per-token fact sheets: TGE price/FDV, peak FDV after TGE, peak after day 7, current FDV

### Takeaway
Only 4 of the 12 perp DEX tokens had a multi-x peak well after TGE: AVNT (11.6x day-1 close, ATH on day 12), TRADOOR (7.3x, ATH day 230), QTO (9.3x, ATH day 75) and ASTER (3.8x, ATH at 6.6 days). Three more (SUP, DESK, LIT) peaked at 2–3x. Five (AMPED, FM, ARA, NEMESIS, PDGN) peaked on day 0–2 and never closed above their day-1 close again.

As of Oct 27, 2026, every token except ASTER (1.12x) and LIT (1.11x) trades below its day-1 close. Most small caps are down 90–99.9%.

### Cited Findings

**Summary table: core perp DEX tokens** (FDV on max supply unless noted; "after-d7" = max daily close ≥7×24 h after first print ÷ day-1 close)

| Token | TGE (first print UTC) | (a) first print → FDV | (b) day-1 close → FDV | ATH (CoinGecko) → peak FDV, date, time after TGE | Peak × (a) / (b) | ATH ≤7d? | Max close after d7 (× d1) | Now (Oct 27, 2026) price → FDV; now ÷ d1 |
|---|---|---|---|---|---|---|---|---|
| ASTER (8B) | 2025-09-17 12:57 | $0.2134 → $1.71B | $0.631 → $5.05B | $2.41 → $19.28B, 2025-09-24, 158 h (6.6 d) | 11.3x / 3.82x | Y (borderline) | $2.31 (Sep 24 close) 3.66x | $0.707 → $5.66B (CG $5.51B on 7.79B total); 1.12x |
| AVNT (1B) | 2025-09-09 16:59 | $0.2306 → $231M | $0.2282 → $228M | $2.64 → $2.64B, 2025-09-21, 12.0 d | 11.45x / 11.57x | N | $2.36 (Sep 21) 10.3x | $0.108 → $108M; 0.47x |
| LIT (1B) | 2025-12-30 08:58 | $3.196 → $3.20B | $2.729 → $2.73B | $7.86 → $7.86B, 2025-12-30 01:05 (TGE day, uncorroborated); corroborated later peak ≈$5.57 on 2026-09-24 → $5.57B | 2.46x / 2.88x (CG); 1.74x / 2.04x (venue peak) | Y (CG ATH); real peak day 268 | $5.315 (2026-09-24) 1.95x | $3.02 → $3.02B (CG $2.97B on 981.9M total); 1.11x |
| TRADOOR (60M total, see notes) | 2025-09-04 12:59 | $0.7185 → $43.1M | $1.38 → $82.8M | $10.13 → $608M, 2026-04-22, 230 d | 14.1x / 7.34x | N | $8.42 (2026-04-21) 6.1x | $0.615 → $36.9M; 0.45x |
| QTO (1B) | 2025-07-10 12:57 | $0.0071 → $7.1M | $0.00718 → $7.2M | $0.067 → $67.0M, 2025-09-23, 75 d | 9.43x / 9.33x | N | $0.0403 (Sep 25) 5.61x | $0.0000577 → $57.6k; 0.008x |
| SUP (1B) | 2025-08-05 12:59 | $0.0472 → $47.2M | $0.0499 → $49.9M | $0.161 → $161M, 2025-10-04, 60 d | 3.41x / 3.23x | N | $0.1406 (Oct 8) 2.82x | $0.000249 → $249k; 0.005x |
| DESK (1B) | 2025-07-25 05:58 | $0.00117 → $1.17M | $0.00148 → $1.48M | $0.00475 → $4.75M, 2025-09-26, 63 d | 4.05x / 3.22x | N | $0.00349 (Oct 6) 2.36x | $0.0000472 → $47k; 0.03x |
| FM (20B) | 2025-08-07 07:34 | $0.0245 → $490M | $0.0305 → $610M | $0.0423 → $846M, 2025-08-09, 42 h | 1.73x / 1.39x | Y | $0.0254 0.83x | $0.00179 → $35.7M; 0.059x |
| ARA (1B) | 2025-09-26 17:03 | $0.0073 → $7.3M | $0.00868 → $8.7M | $0.0153 → $15.3M, 2025-09-27, 25 h | 2.09x / 1.76x | Y | $0.00656 0.76x | $0.0000261 → $26k; 0.003x |
| PDGN (1B) | 2025-10-14 16:37 | $0.000159 → $159k | $0.000158 → $158k | $0.000469 → $469k, 2025-10-16, 47 h | 2.96x / 2.96x | Y | 0.65x | $0.0000052 → $5.2k; 0.03x |
| NEMESIS (1B) | 2025-10-31 14:49 | $0.00669 → $6.7M | $0.00554 → $5.5M | $0.00762 → $7.6M, 2025-10-31 07:16 (before first DL print) | 1.14x / 1.38x | Y | $0.0040 (2026-01-08) 0.72x | $0.000631 → $631k; 0.11x |
| AMPED (100M) | 2025-07-25 20:58 | $0.0406 → $4.06M | $0.0409 → $4.09M | $0.0423 → $4.23M, 2025-07-25 12:24 (TGE day) | 1.04x / 1.04x | Y | $0.021 0.51x | $0.000644 → $64k; 0.016x |

Sources for every row: CoinGecko ATH/ATL/price/supply ([ASTER](https://api.coingecko.com/api/v3/coins/aster-2), [AVNT](https://api.coingecko.com/api/v3/coins/avantis), [LIT](https://api.coingecko.com/api/v3/coins/lighter), [TRADOOR](https://api.coingecko.com/api/v3/coins/tradoor), [QTO](https://api.coingecko.com/api/v3/coins/quanto), small caps via the [Perpetuals category markets endpoint](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=decentralized-perpetuals&order=market_cap_desc&per_page=250&page=1)). DefiLlama first prints ([ASTER](https://coins.llama.fi/prices/first/coingecko:aster-2), [AVNT](https://coins.llama.fi/prices/first/coingecko:avantis), [LIT](https://coins.llama.fi/prices/first/coingecko:lighter), [TRADOOR](https://coins.llama.fi/prices/first/coingecko:tradoor), [QTO](https://coins.llama.fi/prices/first/coingecko:quanto), [SUP](https://coins.llama.fi/prices/first/coingecko:superp), [DESK](https://coins.llama.fi/prices/first/coingecko:desk), [FM](https://coins.llama.fi/prices/first/coingecko:full-moon), [ARA](https://coins.llama.fi/prices/first/coingecko:ara), [PDGN](https://coins.llama.fi/prices/first/coingecko:degen-perp-dex), [NEMESIS](https://coins.llama.fi/prices/first/coingecko:nemesis-2), [AMPED](https://coins.llama.fi/prices/first/coingecko:amped-finance)). DefiLlama daily closes ([ASTER](https://coins.llama.fi/chart/coingecko:aster-2?start=1758153600&span=200&period=1d), [AVNT](https://coins.llama.fi/chart/coingecko:avantis?start=1757462400&span=200&period=1d), [LIT](https://coins.llama.fi/chart/coingecko:lighter?start=1767139200&span=200&period=1d), [TRADOOR](https://coins.llama.fi/chart/coingecko:tradoor?start=1757030400&span=200&period=1d), [QTO](https://coins.llama.fi/chart/coingecko:quanto?start=1752192000&span=200&period=1d), [SUP](https://coins.llama.fi/chart/coingecko:superp?start=1754438400&span=200&period=1d), [DESK](https://coins.llama.fi/chart/coingecko:desk?start=1753488000&span=200&period=1d), [FM](https://coins.llama.fi/chart/coingecko:full-moon?start=1754611200&span=200&period=1d), [ARA](https://coins.llama.fi/chart/coingecko:ara?start=1758931200&span=200&period=1d), [PDGN](https://coins.llama.fi/chart/coingecko:degen-perp-dex?start=1760486400&span=200&period=1d), [NEMESIS](https://coins.llama.fi/chart/coingecko:nemesis-2?start=1761955200&span=200&period=1d), [AMPED](https://coins.llama.fi/chart/coingecko:amped-finance?start=1753488000&span=200&period=1d)). For charts, use `span=200` repeated from `start+200d` for the later history.

**Borderline tokens (same method)**
- **VOOI (1B)**, sale price $0.1125 ([ICO Drops](https://icodrops.com/vooi/)):
  - (a) DefiLlama first print $0.1604 (Dec 18 12:57) → FDV $160M ([DL](https://coins.llama.fi/prices/first/coingecko:vooi)).
  - (b) Day-1 close: DefiLlama $0.0673 → $67M ([DL chart](https://coins.llama.fi/chart/coingecko:vooi?start=1766102400&span=200&period=1d)). Exchange day-1 closes were lower, $0.049–0.052 → $49–52M ([Gate](https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=VOOI_USDT&interval=1d&from=1766016000&to=1767052800), [KuCoin](https://api.kucoin.com/api/v1/market/candles?type=1day&symbol=VOOI-USDT&startAt=1766016000&endAt=1767052800)).
  - ATH $0.1759 (Dec 18 04:36, before exchange listings) → $176M ([CG](https://api.coingecko.com/api/v3/coins/vooi)). Peak = 1.10x (a), 2.61x (b, DefiLlama).
  - ATH within 7 days: yes. Max close after day 7 was $0.0305 (Dec 28) = 0.45x.
  - Now $0.0076 → $7.6M, which is 0.11x day-1 close and 0.07x the sale price.
- **SPRK (1B)**, [DL first print](https://coins.llama.fi/prices/first/coingecko:sparkdex), [DL chart](https://coins.llama.fi/chart/coingecko:sparkdex?start=1753920000&span=200&period=1d), [CG](https://api.coingecko.com/api/v3/coins/sparkdex):
  - First print $0.0204 (2025-07-30) → $20.4M. Day-1 close $0.0208 → $20.8M.
  - ATH $0.0473 (2025-08-07, 8.3 days) → $47.3M. Peak = 2.32x / 2.27x.
  - Max close after day 7: $0.0467 = 2.24x. Now $0.0057 → $5.7M (0.27x).
- **OVL (100M max)**, [DL first print](https://coins.llama.fi/prices/first/coingecko:overlay-protocol), [DL chart](https://coins.llama.fi/chart/coingecko:overlay-protocol?start=1755216000&span=200&period=1d), [CG](https://api.coingecko.com/api/v3/coins/overlay-protocol):
  - ATH $0.766 came on TGE day 2025-08-14 at 00:38 → $76.6M. First DefiLlama print $0.4898 → $49M. Day-1 close $0.2305 → $23.1M.
  - Max close after day 7: $0.313 (2025-09-24) = 1.36x. Now $0.0054 → $0.54M.
- **LN (1B)**, [DL first print](https://coins.llama.fi/prices/first/coingecko:lnfi-network), [DL chart](https://coins.llama.fi/chart/coingecko:lnfi-network?start=1753488000&span=200&period=1d):
  - ATH $0.0569 (2025-07-25 00:02, TGE minutes) → $56.9M. First print $0.0425. Day-1 close $0.0339 → $33.9M.
  - Max close after day 7: 0.69x. Now $0.0060 → $6.0M.
- **NOM (7.5B max)**, [DL first print](https://coins.llama.fi/prices/first/coingecko:nomina), [DL chart](https://coins.llama.fi/chart/coingecko:nomina?start=1759363200&span=200&period=1d):
  - First print $0.0403 (2025-10-01) → $302M. ATH $0.0454 on TGE day → $341M. Day-1 close $0.0398.
  - Max close after day 7: 0.77x. Now $0.00165 → $12.4M.
  - Predecessor Omni Network (OMNI) was not analysed.
- **OMFG (13.8M total, no max)**, [DL first print](https://coins.llama.fi/prices/first/coingecko:omnipair), [DL chart](https://coins.llama.fi/chart/coingecko:omnipair?start=1755734400&span=200&period=1d):
  - First print $0.42 → $5.8M. Day-1 close $0.439. ATH $1.86 (2025-10-04, 45 days) → $25.7M. Peak = 4.42x / 4.24x.
  - Max close after day 7: 4.04x. Now $0.187 → $2.6M.
- **KDK (100M)**, [DL first print](https://coins.llama.fi/prices/first/coingecko:kodiak-finance):
  - First print $0.378 (2025-12-23) → $37.8M. ATH $0.46 (20 h later) → $46M (1.22x / 1.19x).
  - Max close after day 7: 0.97x. Now $0.0835 → $8.3M.
- **PLUTO (1B)**, [DL first print](https://coins.llama.fi/prices/first/coingecko:pluto-3):
  - First print $0.000757 → $0.76M. ATH $0.00124 on TGE day. Max close after day 7: 0.21x. Now about $6.6k FDV.
- **BOT/Hyperbot (1B)**:
  - DefiLlama's first print of $9.32 (2025-09-02) is an obvious artifact ([DL](https://coins.llama.fi/prices/first/coingecko:hyperbot)), so the TGE price is unknown.
  - CoinGecko ATH $0.2005 (2025-09-20) → $200M. Now $0.000155 → $155k ([CG markets](https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=decentralized-perpetuals&per_page=250)).

**Per-token detail: ASTER** (predecessor APX/ApolloX; Astherus merger)
- **Launch venue and timing.** The TGE was Sep 17, 2025 on Aster's own spot venue, described as the "sole global venue" at launch ([press release via Cryptonews](https://cryptonews.net/news/altcoins/31645915/)).
- **First exchange listings (from candle data):**
  - Sep 19, 2025: Gate opened at 14:00 UTC at $0.6888 ([Gate](https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=ASTER_USDT&interval=1h&from=1758067200&to=1761667200)). Hyperliquid's perp opened the same day at $0.61 ([Hyperliquid info API, candleSnapshot ASTER](https://api.hyperliquid.xyz/info)). Binance Futures listed ASTERUSDT perps, 50x, on Sep 19 ([ChainCatcher](https://www.chaincatcher.com/en/article/2206945)).
  - Sep 24: KuCoin opened at $1.58 with a first-hour high of $2.50 ([KuCoin](https://api.kucoin.com/api/v1/market/candles?type=1hour&symbol=ASTER-USDT&startAt=1758672000&endAt=1758844800)).
  - Oct 6, 12:00 UTC: Binance spot (Seed tag) opened at $1.50, with a first-hour high of $3.00 and a day close of $2.063 ([Binance klines](https://data-api.binance.vision/api/v3/klines?symbol=ASTERUSDT&interval=1h&startTime=1759752000000&limit=24); [Altcoin Buzz](https://www.altcoinbuzz.io/cryptocurrency-news/binance-lists-aster-with-new-spot-pairs/)).
  - Oct 17: OKX ([OKX](https://www.okx.com/api/v5/market/history-candles?instId=ASTER-USDT&bar=1Dutc)). Nov 20: Coinbase ([Coinbase](https://api.exchange.coinbase.com/products/ASTER-USD/candles?granularity=86400)).
- **Opening price (sources disagree):**
  - $0.03015 opening with a $0.528 day high (Aster press release, [Cryptonews](https://cryptonews.net/news/altcoins/31645915/)).
  - "approximately $0.08", peaking at $0.52 in the first session ([Coinjournal via Cryptonews](https://cryptonews.net/news/altcoins/31645915/)).
  - TGE FDV $560M, implying $0.07 ([The Block](https://www.theblock.co/news/defi/2025-09-23-rebranded-aster-perps-dex-squares-up-against-hyperliquid-following-cz-endorsement-371690)).
  - DefiLlama first print $0.2134 at 12:57 UTC; hourly prices were $0.129 at 14:57, $0.661 at 23:51, and $1.23 on Sep 18 at 18:59 ([DL hourly](https://coins.llama.fi/chart/coingecko:aster-2?start=1758113861&span=192&period=1h)).
  - CoinGecko's ATL of $0.0997 (Sep 17 04:05 UTC) matches APX's last pre-migration price of about $0.097–0.100 (Sep 15–16 closes on the [APX/apollox-2 DefiLlama series](https://coins.llama.fi/chart/coingecko:apollox-2?start=1756684800&span=30&period=1d)). It is likely carried over from APX rather than a real ASTER trade.
- **TGE FDV at 8B:** $0.24B at $0.03015; $0.56–0.64B at $0.07–0.08; $1.71B at the DefiLlama first print; $5.05B at the day-1 close.
- **Predecessor APX.** Daily closes were $0.0762 (Jun 1, 2025), $0.0828 (Aug 1) and $0.0972 (Sep 16) ([DL apollox-2](https://coins.llama.fi/chart/coingecko:apollox-2?start=1748736000&span=120&period=1d)). APX's historical first print was $0.2057 on Dec 26, 2021 ([DL](https://coins.llama.fi/prices/first/coingecko:apollox-2)). CoinGecko says APX "migrated from their old contract to a new contract" ([CG apx page](https://www.coingecko.com/en/coins/apx-2/php)). I could not verify the conversion ratio.
- **Tokenomics:**
  - Max supply 8B ([1inch](https://1inch.com/tokens/bsc/aster)).
  - The TGE airdrop was 704M (8.8%), with the remaining airdrop spread over 80 months ([The Block](https://www.theblock.co/post/395724/)).
  - Allocation: airdrop 53.5%, ecosystem & community 30%, treasury 7%, team 5%, liquidity & listing 4.5% ([Tokenomist](https://tokenomist.ai/aster-2/claim)).
  - Circulating supply was 2.09B in a Dec 2025 snapshot, with 77.9M burned ([Tokenomist](https://tokenomist.ai/insights/deep-dive-aster-dex-aster-tokenomics-emissions-buybacks-burn-cycles)). CoinGecko now shows 2.51B circulating and 7.79B total ([CG](https://api.coingecko.com/api/v3/coins/aster-2)).
  - Initial circulating supply at TGE: not found (see Gaps).
- **Peak:**
  - CoinGecko ATH $2.41 at Sep 24, 2025 03:18 UTC ([CG](https://api.coingecko.com/api/v3/coins/aster-2)).
  - Venue highs on Sep 24: Gate $2.428, MEXC $2.436, Hyperliquid $2.436, KuCoin $2.50 ([Gate daily](https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=ASTER_USDT&interval=1d&from=1758240000&to=1761667200)).
  - Binance listing-hour print: $3.00 on Oct 6.
  - Peak FDV is $19.3B on CoinGecko's ATH and $24B on the single-venue Binance print. Decrypt reported an $18B FDV about a week after launch ([Decrypt](https://decrypt.co/341157/crypto-traders-aster-price-how-high-can-it-go)).
- **After day 7.** Gate daily close $2.078 on Oct 3 and intraday high $2.278 on Oct 4 — about 3.3x the day-1 close ([Gate daily](https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=ASTER_USDT&interval=1d&from=1758240000&to=1761667200)). So ASTER traded far above its day-1 close after day 7, even though the CoinGecko ATH landed at 6.6 days.
- **Lows.** Post-listing trading low about $0.403 on Feb 6, 2026 across Gate, OKX, Coinbase and Hyperliquid ([OKX daily](https://www.okx.com/api/v5/market/history-candles?instId=ASTER-USDT&bar=1Dutc)).

**Per-token detail: AVNT (Avantis → "Veranta")**
- **TGE Sep 9, 2025.** Binance Alpha opened at 13:00 UTC ([BitcoinWorld](https://bitcoinworld.co.in/binance-hodler-airdrop-avantis/)).
- **First-hour exchange opens (14:00 UTC)** were stale, thin prints: KuCoin $0.07 ([KuCoin](https://api.kucoin.com/api/v1/market/candles?type=1hour&symbol=AVNT-USDT&startAt=1757376000&endAt=1757980800)), Gate $0.0501 ([Gate](https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=AVNT_USDT&interval=1h&from=1757376000&to=1760976000)), Bitget $0.015. Better opening prints: Hyperliquid perp $0.2451 at 15:00 ([Hyperliquid info API](https://api.hyperliquid.xyz/info)) and Coinbase $0.276 at 18:00 ([Coinbase](https://api.exchange.coinbase.com/products/AVNT-USD/candles?granularity=3600&start=2025-09-09T00:00:00Z&end=2025-09-21T00:00:00Z)).
- **Day 1.** First-day highs were $0.41–0.48. First-day closes were $0.21 (Gate $0.2097, KuCoin $0.2117, Hyperliquid $0.2129) versus DefiLlama's $0.2282.
- **Tokenomics:**
  - Airdrop 12.5%, fully unlocked, to 65,000 onchain participants ([Binance Research](https://www.binance.com/vi/research/projects/avnt)). Binance HODLer airdrop of 10M AVNT (1%), the 40th HODLer project ([CryptoNinjas](https://www.cryptoninjas.net/news/binance-drops-10m-avantis-avnt-airdrop/); [CoinGabbar](https://www.coingabbar.com/en/crypto-currency-news/binance-avantis-airdrop-40th-hodler-project)).
  - Circulating supply estimates disagree: 263.5M (26.3%) on Sep 15 ([Binance Research](https://www.binance.com/vi/research/projects/avnt)); 209.22M on Sep 12 (MEXC); 18.5% (185M) unlocked at TGE ([Tokenomics.com](https://app.tokenomics.com/tokenomics/avantis)). That puts initial circulating market cap at about $42–60M on the day-1 close.
- **Funding.** $4M seed (Sep 2023, Pantera) plus an $8M Series A (Founders Fund and Pantera, announced Jun 2025). The valuation was undisclosed (equity plus token warrants) ([The Block](https://www.theblock.co/post/356775/peter-thiel-founders-fund-base-avantis-crypto-funding); [The Defiant](https://thedefiant.io/news/defi/avantis-raises-8-million-series-led-founders-fund-pantera-capital-to-expand-7-5b-de533de8)).
- **Pre-market.** No AVNT pre-market or Polymarket FDV market was found.
- **Run-up:**
  - Sep 15: Binance spot opened at 05:00 UTC at $0.81, hit $2.10 in the first hour and closed the day at $1.245 ([Binance klines](https://data-api.binance.vision/api/v3/klines?symbol=AVNTUSDT&interval=1h&startTime=1757912400000&limit=24)).
  - Sep 15: Upbit KRW/BTC/USDT listing at 13:30 KST, opening at ₩1,560 / $1.478 ([Upbit](https://api.upbit.com/v1/candles/days?market=USDT-AVNT&to=2025-10-01T00:00:00Z&count=20); [BeInCrypto via BTCC](https://www.btcc.com/en-US/square/Beincrypto/954359)).
  - Peak on the Sep 22 UTC daily candle: about $2.67–2.68 on Binance ($2.679), Coinbase ($2.683), Gate ($2.670) and Hyperliquid ($2.669) ([Binance daily](https://data-api.binance.vision/api/v3/klines?symbol=AVNTUSDT&interval=1d&startTime=1757894400000&limit=30)). Upbit's USDT book showed a $4.999 wick on Sep 21 — a thin-book anomaly.
  - OKX listed on Oct 7 ([OKX](https://www.okx.com/api/v5/market/history-candles?instId=AVNT-USDT&bar=1Dutc)).
- **Low.** $0.0776 on Aug 3, 2026 ([Binance daily](https://data-api.binance.vision/api/v3/klines?symbol=AVNTUSDT&interval=1d&startTime=1777000000000&limit=200)).

**Per-token detail: LIT (Lighter)**
- **Tokenomics.** 1B supply. Airdrop 25% (250M) to points seasons 1–2, sent directly with no lock. Ecosystem 50% in total, team 26%, investors 24% (1-year lock, 3-year linear vesting). The last private round was $68M at a $1.5B valuation in Nov 2025, led by Founders Fund and Ribbit ([The Block](https://www.theblock.co/post/383940/lighter-native-token-lit); [DL News](https://www.dlnews.com/articles/defi/lighter-airdrop-pushes-value-of-hyperliquid-rival-past-2bn/)).
- **Pre-market:**
  - A Hyperliquid pre-launch perp traded from Dec 22, 2025: first day $2.80–4.44, Dec 29 close $3.208 (≈$3.2B FDV) ([Hyperliquid info API](https://api.hyperliquid.xyz/info), candleSnapshot coin LIT).
  - CoinMarketCap pre-market ≈$3.20–3.25 ([CoinDesk](https://www.coindesk.com/markets/2025/12/30/traders-split-over-whether-lighter-s-lit-clears-usd3-billion-fdv-after-launch); [The Block](https://www.theblock.co/post/383940/lighter-native-token-lit)).
  - HyENA pre-market $3.38 ([search summary of MEXC news](https://www.mexc.com/news/371545)).
  - Polymarket gave "roughly even odds" of FDV above $3B one day after launch ([CoinDesk](https://www.coindesk.com/markets/2025/12/30/traders-split-over-whether-lighter-s-lit-clears-usd3-billion-fdv-after-launch)).
- **Opening (sources disagree):**
  - "opened above $3.30" ([DL News](https://www.dlnews.com/articles/defi/lighter-airdrop-pushes-value-of-hyperliquid-rival-past-2bn/)).
  - $2.34 at 1:55 a.m. ET ([The Block](https://www.theblock.co/post/383940/lighter-native-token-lit)).
  - Early range $2.30–4.04 ([Coin360](https://coin360.com/news/lighter-lit-airdrop-coinbase-listing-market-impact)).
  - CoinGecko's chart starts at 08:00 UTC at $2.726, with a market cap of $681.6M — i.e. 250M circulating ([CG range](https://api.coingecko.com/api/v3/coins/lighter/market_chart/range?vs_currency=usd&from=1767038400&to=1767103200)).
  - Gate opened at $4.80 at 09:00 UTC, with a first-hour high of $4.97 and a day close of $2.666 ([Gate](https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=LIT_USDT&interval=1h&from=1766966400&to=1770566400)).
  - Hyperliquid's LIT perp on Dec 30 ranged $2.24–3.34 ([Hyperliquid info API](https://api.hyperliquid.xyz/info)).
- **The $7.86 ATH.** CoinGecko stamps it at Dec 30 01:05 UTC, before its own chart begins ([CG](https://api.coingecko.com/api/v3/coins/lighter)). Decrypt also lists it ([Decrypt](https://decrypt.co/price/lighter)). No venue I checked corroborates it.
- **Later venues.** HTX listed on Jan 15, 2026 ([Newsfile](https://www.newsfilecorp.com/release/280606)). OKX, KuCoin, Bitget and Coinbase (LIGHTER-USD) daily candles all start Jan 15, 2026 ([Coinbase](https://api.exchange.coinbase.com/products/LIGHTER-USD/candles?granularity=86400)). Binance spot returned no LITUSDT data ([Binance klines](https://data-api.binance.vision/api/v3/klines?symbol=LITUSDT&interval=1d&startTime=1766966400000)).
- **Catalysts.**
  - Jan 5, 2026: buyback signals, +14% to about $3.04 ([The Block](https://www.theblock.co/post/384399/lighter-lit-buyback)).
  - Coinbase listing ([KuCoin news](https://www.kucoin.com/news/flash/coinbase-lists-lighter-s-lit-token-as-price-approaches-3)).
  - Low of $0.779 on Mar 31, 2026.
  - Sep 23–24, 2026 rally to about $5.57 (OKX $5.576, Gate $5.573, Hyperliquid $5.586) ([OKX daily](https://www.okx.com/api/v5/market/history-candles?instId=LIT-USDT&bar=1Dutc)). It was attributed to a Bitwise ETP on Xetra in a low-quality, AI-style summary ([AlphaMaven](https://alpha-maven.com/story/crypto/lighter-lit-surges-453-on-bitwise-etp-launch-coinmarketcap)).

**Per-token detail: VOOI**
- **Sale.** Legion/Cookie sale at $0.1125 = $112.5M FDV, Nov 17–20, 2025, 100% unlocked at TGE ([ICO Drops](https://icodrops.com/vooi/); [CoinLaunch](https://coinlaunch.space/events-rounds/vooi-legion-ico-round/)). Backed by YZi Labs plus an Echo round.
- **Allocation:** foundation 31%, community & market growth 27.82%, private/strategic 13.65%, airdrops & community sales 10.53%, contributors 17% ([MEXC/PANews](https://www.mexc.com/ru-RU/crypto-pulse/article/vooi-price-prediction-2026-57436)).
- **Expectations vs. reality.** Pre-market had "hinted at prices between $0.30 and $0.75", and Polymarket odds favoured a $300M+ FDV within 24 hours. Instead the price fell about 86% from $0.169 to under $0.03 ([OurCryptoTalk](https://ourcryptotalk.com/news/vooi-team-responds-after-86-percent-drop-after-tge)).
- **Launch day.** Binance Alpha listed first on Dec 18 ([HokaNews](https://www.hokanews.com/2025/12/vooi-listing-locked-in-binance-alpha.html)). Exchange listings at 13:00 UTC opened at Gate $0.12 and KuCoin $0.08, with day highs of $0.145–0.155. CoinGecko's first chart point had a $19.0M market cap at $0.1444, implying about 132M circulating ([CG range](https://api.coingecko.com/api/v3/coins/vooi/market_chart/range?vs_currency=usd&from=1766008800&to=1766073600)). MEXC cited about 244M circulating instead ([Bittime](https://www.bittime.com/en/blog/prediksi-harga-vooi)).
- **After day 7.** One wick on Jan 19, 2026 to $0.062–0.066 on Gate/KuCoin (about 1.25–1.33x the exchange day-1 close). No daily close after day 7 was above the day-1 close ([KuCoin daily](https://api.kucoin.com/api/v1/market/candles?type=1day&symbol=VOOI-USDT&startAt=1766016000&endAt=1793000000)).

**Per-token detail: TRADOOR**
- **Launch.** Binance Alpha and Binance Wallet IDO token, per CoinGecko's categories ([CG](https://api.coingecko.com/api/v3/coins/tradoor)). Binance Futures listed TRADOORUSDT perps (50x) on Sep 19, 2025 ([cryptonews.net](https://cryptonews.net/news/market/31651745/)).
- **Funding.** $3.2M total, reported May 2025 ([GlobeNewswire](https://www.globenewswire.com/news-release/2025/05/15/3081907/0/en/Tradoor-Unveils-Fastest-DEX-on-TON-Following-3-2m-in-Financing.html)).
- **Supply is inconsistent.** CoinGecko shows total supply 60M (its FDV basis), max supply 8B and circulating 14.35M ([CG](https://api.coingecko.com/api/v3/coins/tradoor)). FDVs in the table use 60M; on an 8B basis the figures would be absurd (a $81B peak).
- **Price path.** The first-week hourly high was $2.51 on Sep 9, 2025 ([DL hourly](https://coins.llama.fi/chart/coingecko:tradoor?start=1756990740&span=192&period=1h)). The ATH of $10.13 came on Apr 22, 2026, followed by an ATL of $0.337 on Jun 6, 2026 — a ~97% collapse in about 6 weeks, the classic low-float pump pattern.

**Oct 10–11, 2025 crash, single-day change in DefiLlama daily closes** ([DL charts as above](https://coins.llama.fi/chart/coingecko:avantis?start=1757462400&span=200&period=1d)):

| Token | Day change |
|---|---|
| TRADOOR | −35% |
| AVNT | −31% |
| QTO | −22% |
| ASTER | −21% |
| SUP | −20% |
| OMFG | −20% |
| SPRK | −11% |
| DESK | −7% |
| OVL | −7% |

### Inferences
- **Venue prints and CoinGecko ATHs are noisy on listing day.** CoinGecko ATHs stamped before its own chart begins (LIT $7.86, VOOI $0.1759, OVL, LN, NOM, AMPED, NEMESIS, PLUTO) and single-venue listing wicks (ASTER $3.00 on Binance, AVNT $4.999 on Upbit) can inflate "peak FDV". For LIT, the corroborated peak is ~$5.57B (Sep 2026), not $7.86B.
- **ASTER's peak multiple depends on the basis.** It ranges from about 3.8x (day-1 close) to 11x (DefiLlama first print) to 24–80x (APX carry-over or reported $0.03–0.10 opening prints). The day-1-close basis is the most reproducible.
- **Within the six-week Sep–Oct 2025 window, AVNT's run is the cleanest "low FDV pushed higher" case.** A $228M day-1 FDV went to a $2.64B peak, 12 days after TGE, helped by the Binance HODLer airdrop and spot listing plus the Upbit listing.

### Gaps
- ASTER's initial circulating supply and an authoritative first-trade price on Aster spot were not found; sources disagree ($0.03–0.21).
- LIT's exact first trade on Lighter spot was not captured (Lighter's candlestick API returned empty), and the source of CoinGecko's $7.86 is unverified. Binance Futures, Bybit and Binance Alpha prints were not checked (geo-blocked; Alpha has no API).
- TRADOOR's true max supply is unresolved (60M vs 8B on CoinGecko).
- Hyperbot's TGE price is unknown (DefiLlama artifact).
- Day-1 venues and tokenomics were not researched for the small caps (QTO, DESK, AMPED, SUP, FM, ARA, NEMESIS, PDGN).
- No private-round valuations were found except LIT ($1.5B) and VOOI's sale ($112.5M FDV); Avantis' Series A valuation was undisclosed.
- Pre-market data for ASTER and AVNT was not found.

## Cohort statistics: how many exceeded TGE FDV after TGE, how many only spiked in week 1, how many went straight down, and does lower TGE FDV go with a higher peak multiple?

### Takeaway
Measured robustly — the best daily close at least 7 days after TGE versus the day-1 close — only 7 of 12 perp DEX tokens ever traded meaningfully above their TGE FDV (AVNT, TRADOOR, QTO, ASTER, SUP, DESK, LIT). Five never did. Of the 8 borderline tokens with usable data, 3 did and 5 did not.

In this cohort, a lower TGE FDV did **not** go with a higher peak multiple. The rank correlation is weakly positive (higher FDV → higher multiple), the opposite of the hypothesis. The hypothesis is therefore not supported for the 2025H2 cohort.

### Cited Findings
All counts below are computed from the per-token table above (sources: CoinGecko and DefiLlama URLs listed there).
- **Peak (CoinGecko intraday ATH) vs day-1 close, 12 core tokens:**
  - Above day-1 close: 12/12. This is trivially true when comparing an intraday high to a close; AMPED is only 1.04x.
  - ≥1.5x: 9/12 (fails: AMPED 1.04x, NEMESIS 1.38x, FM 1.39x).
  - ≥2x: 8/12 (also fails: ARA 1.76x).
  - ≥5x: 3/12 (AVNT 11.6x, QTO 9.3x, TRADOOR 7.3x).
- **Peak vs first print (basis a):** ≥1.5x 10/12; ≥2x 9/12, or 8/12 if LIT's corroborated $5.57 peak replaces CoinGecko's $7.86; ≥5x 4/12 (AVNT, ASTER, QTO, TRADOOR).
- **Robust test: max daily close after day 7 ÷ day-1 close:**
  - ≥1.2x: 7/12 — AVNT 10.3x, TRADOOR 6.1x, QTO 5.6x, ASTER 3.7x, SUP 2.8x, DESK 2.4x, LIT 1.95x.
  - ≥2x: 6/12. ≥5x: 3/12.
  - Never above day-1 close after day 7: 5/12 — AMPED 0.51x, PDGN 0.65x, NEMESIS 0.72x, ARA 0.76x, FM 0.83x.
- **Borderline tokens (n=8; Hyperbot excluded for bad TGE data):**
  - After day 7 above 1.2x day-1 close: OMFG 4.0x, SPRK 2.2x, OVL 1.36x.
  - Never: VOOI 0.45x, LN 0.69x, NOM 0.77x, KDK 0.97x, PLUTO 0.21x.
- **ATH timing for core tokens:**
  - ATH within the first 7 days: 7/12 — LIT (CoinGecko print), ASTER (borderline, 6.6 days), FM, ARA, PDGN, NEMESIS, AMPED.
  - Of those 7, only ASTER (3.7x) and LIT (1.95x, nine months later) later closed meaningfully above day-1 close. The other 5 are pure "listing spike, then down".
  - ATH later than day 7: 5/12 — AVNT (day 12), SUP (day 60), DESK (day 63), QTO (day 75), TRADOOR (day 230).
- **"More or less straight down"** (ATH within about 2 days and never back above day-1 close): AMPED, NEMESIS, FM, ARA, PDGN among core tokens, plus VOOI, LN, NOM, KDK and PLUTO among borderline tokens — 10 of 20.
- **Now vs day-1 close, core tokens:** above day-1 close 2/12 (ASTER 1.12x, LIT 1.11x). The other 10 sit between 0.003x and 0.47x. Median current FDV ÷ day-1 FDV is about 0.05x (midpoint of FM 0.059x and PDGN 0.033x).
- **Correlation.** Spearman rank correlation between day-1-close FDV and peak multiple, across the 12 core tokens:
  - Peak = CoinGecko ATH ÷ day-1 close: ρ ≈ +0.28.
  - Peak = max close after day 7 ÷ day-1 close: ρ ≈ +0.52.
  - Both are positive, i.e. higher TGE FDV went with higher multiples, and neither is significant at n=12 (critical |ρ| ≈ 0.59 at p=0.05).
  - The day-1 FDVs being ranked: PDGN $0.16M, DESK $1.5M, AMPED $4.1M, NEMESIS $5.5M, QTO $7.2M, ARA $8.7M, SUP $50M, TRADOOR $83M, AVNT $228M, FM $610M, LIT $2.73B, ASTER $5.05B.

### Inferences
- **Strict reading.** "Pushed to a higher FDV at some point after TGE" is trivially true for nearly every token if any intraday print counts, including listing-day wicks. The hypothesis only says something when tested against a post-listing reference. On the day-7+ test it holds for about 58% of core tokens (7/12) and about 50% of core plus borderline tokens (10/20).
- **Low FDV was not a tailwind here.** The sub-$10M-FDV launches split: QTO and DESK ran, while AMPED, NEMESIS, ARA and PDGN did not. Meanwhile, mid/large launches with exchange and Binance support (AVNT, TRADOOR, ASTER) delivered most of the big multiples. What mattered more was listing and launch timing — before the Oct 10 crash versus after it.
- **Timing dominates.** Every core token whose peak was ≥2x the day-1 close in 2025 launched Jul–Sep 2025 and peaked Sep 21 – Oct 8, 2025. Every core token launched after Oct 1, 2025 either went straight down or (LIT) only recovered nine months later.

### Gaps
- n=12 core tokens is small, and sub-$1M-FDV tokens have noisy CoinGecko/DefiLlama data, so the statistics are indicative only.
- Post-day-7 intraday highs were checked only via exchange candles for ASTER, AVNT, LIT and VOOI; the other tokens use daily closes.

## What market conditions surrounded each TGE and each peak?

### Takeaway
The cohort launched into a late-cycle market. BTC traded around $110–116k from Jul to Sep 2025 and posted its highest daily close (~$124.7k) on Oct 6, 2025. The September "perp DEX wars" were led by Aster's CZ-endorsed launch.

Most 2025 peaks cluster on Sep 21 – Oct 8, 2025, just before the Oct 10–11 $19B liquidation crash. Tokens that launched after it faced a falling market (BTC ~$85k by late Nov 2025, ~$68–70k in Feb–Mar 2026), and their only later spikes were idiosyncratic: TRADOOR in Apr 2026 and LIT in Sep 2026.

### Cited Findings
- **BTC daily closes:**
  - Around TGEs: 2025-07-10 $115.9k; 2025-08-05 $114.1k; 2025-09-09 $111.5k; 2025-09-17 $116.4k.
  - Highest close $124.7k on 2025-10-06, then $110.8k after Oct 10.
  - Later: 2025-11-21 $85.1k; 2025-12-30 $88.4k; 2026-02-06 $70.5k; 2026-03-31 $68.2k; 2026-04-22 $78.2k; 2026-09-24 $84.4k; 2026-10-26 $80.0k ([DefiLlama BTC chart](https://coins.llama.fi/chart/coingecko:bitcoin?start=1751241600&span=200&period=1d)).
  - BTC hit a record above $126k days before the crash and fell from about $122k to about $105k during it ([CoinDesk](https://www.coindesk.com/markets/2026/10/10/bitcoin-s-usd19-billion-wake-up-call-one-year-later-has-crypto-learned-anything)).
- **Oct 10–11, 2025 crash.** About $19B of liquidations, the largest single-day event on record, triggered by the 100% China tariff announcement plus leverage and exchange failures ([CoinDesk research](https://www.coindesk.com/research/market-spotlight-the-19-billion-liquidation-that-shook-crypto); [CoinDesk Oct 10](https://www.coindesk.com/markets/2025/10/10/bitcoin-crashes-below-usd110k-cryptos-in-freefall-on-further-trump-tariff-on-china)).
- **Perp DEX narrative.** Monthly perp DEX volume topped $1T for the first time amid Hyperliquid–Aster–Lighter competition ([The Block](https://www.theblock.co/post/373210/perp-dex-monthly-trading-volume-1-trillion-usd-hyperliquid-aster-lighter)). 2025 perp DEX volume was $6.38T versus $1.50T in 2024, and total open interest peaked at $210.02B on Oct 7, 2025, just before "10.10" ([CoinGecko perps report 2026](https://www.coingecko.com/research/publications/state-of-crypto-perpetuals-report-2026)).
- **Aster catalysts:**
  - Price rose more than 10x from CZ's endorsement to $2 within four days ([The Block](https://www.theblock.co/news/defi/2025-09-23-rebranded-aster-perps-dex-squares-up-against-hyperliquid-following-cz-endorsement-371690)).
  - An XPL perp glitch led to reimbursements ([The Block](https://www.theblock.co/news/defi/2025-09-26-aster-compensates-traders-xpl-liquidations-372500)).
  - DefiLlama delisted Aster's perp volume over wash-trading concerns on Oct 5, 2025; ASTER fell ~10%, then the Binance listing reversed it ([The Block](https://www.theblock.co/news/ecosystems/2025-10-05-asters-token-drops-10-after-defillama-head-raises-wash-trading-concerns-delists-perpetuals-data-373458); [DL News](https://www.dlnews.com/articles/defi/aster-perp-volume-scrutinized-amid-defillama-delisting/)).
  - Binance spot listing Oct 6 ([Tekedia](https://www.tekedia.com/binance-lists-aster-amid-defillama-delisting-citing-wash-trading-suspicions/)).
  - CZ bought 2M ASTER on Nov 2, 2025, taking the price from $0.91 to a $1.26 peak ([Cointelegraph](https://cointelegraph.com/news/aster-token-surges-after-cz-buys-two-million-tokens); [DL News](https://www.dlnews.com/articles/defi/aster-jumps-after-binance-founder-cz-buys-2m-tokens/)).
  - Emissions moved to a staking-only model, cutting monthly unlocks by 97% ([The Block](https://www.theblock.co/post/395724/)).
  - A June 2026 buyback-and-burn upgrade gave a +10% pop that faded to about $0.68 ([CoinDesk](https://www.coindesk.com/markets/2026/06/18/aster-popped-over-10-on-radical-buyback-and-burn-upgrade-but-gains-were-short-lived)).
- **AVNT catalysts.**
  - Binance Alpha, HODLer airdrop and spot listing, Upbit KRW listing, plus early Coinbase, Bybit, Gate, Bitget and KuCoin listings ([CCN](https://www.ccn.com/analysis/crypto/avantis-crypto-avnt-price-rally-binance-upbit-listing/); [BeInCrypto via BTCC](https://www.btcc.com/en-US/square/Beincrypto/954359)).
  - Its peak (Sep 21–22, 2025) coincided with the ASTER mania week.
- **LIT context.**
  - It launched into a falling market with weekly Hyperliquid outflows above $430M as Lighter and Aster competed ([The Block](https://www.theblock.co/news/markets/2025-12-19-weekly-hyperliquid-outflows-430m-lighter-aster-tighten-perp-dex-competition-dune-383314)). Withdrawal issues were reported at launch ([The Defiant](https://thedefiant.io/news/defi/lighter-users-report-withdrawal-issues-after-lit-token-launch)).
  - The trough ($0.78, Mar 31, 2026) coincided with BTC at about $68k; the Sep 2026 rebound to about $5.57 came with BTC at about $84k (sources above).
- **TRADOOR.** The Apr 2026 pump to $10.13 came with BTC around $78k and was followed by a ~97% collapse by Jun 6, 2026 ([CG](https://api.coingecko.com/api/v3/coins/tradoor)). No news source was checked for its cause.

### Inferences
- The Sep 2025 cluster of peaks (AVNT, QTO, ASTER, DESK, SUP, OMFG) fits a narrative-plus-liquidity top. Perp-DEX mania (Aster/CZ, MYX's run to $19) peaked alongside record open interest and BTC's top. "Low FDV gets pushed higher" worked mainly for tokens that were already listed before that window.
- After Oct 10, launch FDVs were set by pre-markets and Polymarket (LIT about $3B; VOOI hopes of $300M+) and usually marked the high, at least for months.

### Gaps
- No causal sourcing for the QTO, DESK, SUP or OMFG run-ups, the TRADOOR Apr 2026 pump, or manipulation/unlock events at the small caps.
- An alt-season index (e.g. ETH or TOTAL3) was not pulled.
- LIT's Sep 2026 catalyst is sourced only from a low-quality AI summary.
