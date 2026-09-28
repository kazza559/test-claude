# Historical realized outcomes of stablecoin / yield-dollar points programs and Pendle YT points farming (calibration for USD.AI Season 2), as of 2026-09-28

Conventions used in these notes:
- **[OFFICIAL]** = from the project's own docs/blog/announcement. **[SECONDARY]** = news/aggregator/search snippet. **[EST]** = my own calculation (formula shown). **[UNVERIFIED]** = seen only in a search-engine summary where the underlying page was not confirmed.
- $/point = (airdrop tokens to that points pool × token price) / (total points in pool).
- "Airdrop APR" for a plain depositor = $/point × (points per $1 per day) × 365. Where total points are unknown, I use a protocol-level proxy: airdrop $ value / (average TVL × season length in years). The proxy **overstates** what a plain 1x depositor got, because points are skewed toward multiplier holders (YT, LP, lockers, stakers).
- Prices are at the date stated; "TGE-day ATH" prices overstate what most recipients realized.

---

## Q1. Per-project realized outcomes: total points, airdrop %, TGE price/FDV, $/point, implied APR

### Takeaway
Across ~20 stablecoin/yield-dollar programs, the first-season airdrop was typically **~3–10% of supply (median ≈5%)**, and the realized $ value per point was far below mid-season expectations in most cases. The big winners were early, low-competition seasons (Ethena S1 at $0.64 ENA: ~$480M; Usual pills). From mid-2025 onwards the realized value collapsed: most tokens (FF, EDEN, GAIB, RESOLV, STABLE, XPL, HUMA) fell 60–96% from their TGE-day highs. Several programs paid little or nothing in tokens (Level: protocol sunset, no token; Cap: no token airdrop, the stablecoin "stabledrop" was cut from $12M to $4.2M; Strata: TGE missed by 5+ months). USD.AI's own Season 1 (3% of CHIP, $9M at the $0.03 ICO price) is the closest comparable, and CHIP is one of the few tokens still trading above its launch price.

### Cited Findings

**Ethena (Shards S1 → Sats S2 → sENA/Sats S3–S6)**
- S1: 750M ENA = 5% of the 15B supply, allocated by Shards accumulated through April 1, 2024; airdropped on April 2, 2024 [OFFICIAL via press] — [The Block](https://www.theblock.co/post/285212/ethena-labs-to-airdrop-750-million-ena-tokens-on-april-2); [CoinMarketCap Academy](https://coinmarketcap.com/academy/article/ethereum-defi-protocol-ethena-labs-plans-750-million-airdrop-of-ena-token)
- The Shard campaign ran 40 days (Feb 19 – Apr 1, 2024). 722M of the 750M ENA were claimed (96.3% claim ratio) [SECONDARY] — [CoinGecko Learn](https://www.coingecko.com/learn/ethena-labs-airdrop-shard-campaign)
- ENA launched at $0.64: about $1B market cap and >$10B FDV (Apr 2024) [SECONDARY] — [The Defiant](https://thedefiant.io/news/defi/ethena-labs-ena-launches-at-usd1-billion-post-airdrop-as-sats-campaign-kicks-off)
- **[EST] S1 airdrop value at launch = 750M × $0.64 ≈ $480M.**
- S2 (Sats): 750M ENA (5%), Apr 2 – Sep 2, 2024 (ended early if USDe supply reached $5B) [SECONDARY] — [The Defiant](https://thedefiant.io/news/defi/ethena-labs-ena-launches-at-usd1-billion-post-airdrop-as-sats-campaign-kicks-off); [Bitrue FAQ](https://support.bitrue.com/hc/en-001/articles/30696710198425-Ethena-Airdrop-Season-2-Sats-Campaign)
- S2 rates: holding USDe earned 20 sats/$/day and sUSDe 5x. Mid-season (spring 2024), analysts projected "25% return … equivalent to an annualized return of 72%" for USDe holders. 1.76T sats had been issued at the time, with ~10T expected by season end [SECONDARY] — [Foresight News on Binance Square](https://www.binance.com/en/square/post/6273119441873); [Gate Learn](https://www.gate.com/learn/articles/detailed-explanation-of-ethena-s-three-strategies-in-season-2-and-their-potential-rewards/2709) (projected 10.1T sats; projected ROI of 25.93% for holding USDe, 118.55% for Pendle YT, 162.56% for ENA lock + USDe YT)
- On May 22, 2024, Ouroboros expected "~50% APY on average" for S2, based on an assumed $3.5B average TVL [SECONDARY] — [Ouroboros Research](https://ouroborosresearch.substack.com/p/ouroboros-market-update-1-ethena)
- During S2, USDe supply grew from $1.3B to just under $3B. TVL peaked at $3.612B in early July and fell to $2.92B before the season ended [SECONDARY] — [NullTX](https://nulltx.com/ethena-season-2-airdrop-event-a-week-to-go-but-challenges-persist/)
- S2 claim opened the week of Sep 30, 2024. For the top 2,000 addresses, 50% was liquid and 50% vested linearly over 6 months [SECONDARY] — [X @Airdrop_Adv](https://x.com/Airdrop_Adv/status/1830743545554321843?lang=en)
- After S2 claims, ENA went from $0.28 to $0.42 within days (Oct 2024) [SECONDARY] — [AirdropAlert](https://airdropalert.com/blogs/ethena-ena-price-surge-after-airdrop/)
- **[EST] S2 value = 750M × $0.28–$0.42 ≈ $210M–$315M.** Using the 10.1T projected total sats (not a final official figure): ENA/sat ≈ 750M / 10.1T ≈ 7.4e-5, so a plain USDe holder at 20 sats/$/day earned about 20 × 7.4e-5 × 365 ≈ 0.54 ENA per $1 per year. That is **≈15% APR at $0.28 and ≈23% at $0.42, against the ~50–72% projected mid-season.** An sUSDe holder at 5 sats/day got ≈4–6% APR from the airdrop, on top of sUSDe yield.
- S3: 3.5% of supply (525M ENA), Sep 2, 2024 – Mar 23, 2025. sENA got 40x. Worth about $178.5M when the claim opened on May 1, 2025. The top 2,000 wallets had 50% vested over 6 months [SECONDARY] — [X @Airdrop_Adv](https://x.com/Airdrop_Adv/status/1917709309632471225); [oneclick.fi](https://www.oneclick.fi/blog/ethena-airdrop-guide)
- **[EST] Implied ENA price at the S3 claim = $178.5M / 525M ≈ $0.34.**
- S4: "at least 3.5%" of supply, running until Sep 24, 2025. One source says "1.5% of the total supply is now open for claim," so the S4 figures are ambiguous [SECONDARY/CONFLICTING] — [AirdropAlert S4](https://airdropalert.com/airdrops/ethena-season-4/)
- S5: 2% of supply (~300M ENA), tracked Sep 25, 2025 – Mar 25, 2026. Claim opened May 5, 2026, with top-2,000 vesting of 50% over 6 months. ENA market cap was near $840M in early May 2026, with ~60% of supply unlocked [SECONDARY] — [KuCoin](https://www.kucoin.com/blog/how-to-claim-ethena-season-5-airdrop); [CoinMarketCap](https://coinmarketcap.com/top-stories/69f9cf10f473f7351fe0e7e4/)
- **[EST] S5 value ≈ 300M × (~$840M / ~9B circulating ≈ $0.093) ≈ $28M.** That is about 17x less in $ than S1, driven by both a smaller % and a lower ENA price.
- Caution: a MEXC table (Mar 22, 2026) lists S3 and S4 as "50M ENA", which contradicts the 3.5% figures. I treat it as unreliable — [MEXC](https://blog.mexc.com/news/ethena-airdrop-guide-before-the-season-5-deadline/)

**Usual (Pills → USUAL; YT-USD0++)**
- Pills airdrop = 7.5% of the USUAL supply minted at TGE [SECONDARY] — [CoinMarketCap Academy](https://coinmarketcap.com/academy/article/understanding-usual-a-guide-to-earning-pills-for-the-usual-airdrop). Other sources say 8.5% (7.5% plus a 1% "Believer's bonus"); another snapshot showed $358M TVL and 12,280 holders [SECONDARY] — [Linity](https://linity.com/opportunities/usual)
- Earning rates: 1 pill per $ instantly, then 3 pills/$/day for holding USD0++, plus a multiplier that grew 2%/day (>10.5x after 4 months) [SECONDARY] — [CoinMarketCap Academy](https://coinmarketcap.com/academy/article/understanding-usual-a-guide-to-earning-pills-for-the-usual-airdrop); [Usual docs](https://docs.usual.money/pre-launch-rules/pills-campaign-rules)
- Distribution design [OFFICIAL] — [Usual Blog](https://usual.money/blog/airdrop-the-genesis-of-ownership):
  - 98.5% of wallets could claim instantly.
  - The top 1.5% received 10% immediately and 90% vested over 6 months (Jan 18 – Jun 18, 2025), with an option to pay to skip vesting.
  - 11.6% of supply was liquid on day 1, and spot trading launched Dec 18, 2024.
  - The same blog lists Binance Launchpool at 7.5%, which may be conflated with the pills figure.
- At listing, USUAL traded at about $0.70 with a $242M market cap [SECONDARY] — [CoinGape](https://coingape.com/will-usual-price-hit-1-as-binance-to-commence-spot-trading/). USUAL's low was $0.0159 on Oct 10, 2025 [UNVERIFIED snippet] — [CoinGecko](https://www.coingecko.com/en/coins/usual)
- YT-USD0++ outcome: "almost ALL of YT buyers have profited greatly … airdropped amount is worth much more than the initial cost of buying YT-USD0++." Pendle had guided 3–4x ROI; farmers expected around 5x, and some reports claim >10x [SECONDARY] — [AirdropMeta](https://www.airdropmeta.com/projects/pendle); [Gate Learn](https://www.gate.com/learn/articles/annualized-393-an-in-depth-analysis-of-the-real-yield-and-risks-of-the-pendle-yt-leverage-points-strategy/9296) (mentions EtherFi/Usual YT >10x)
- Pendle Print #39 (Oct 21, 2024): "short-term exposure to Pills alone before end of Usual's pre-launch would be enough to recover most if not all of the YT costs" — [Pendle Print #39](https://pendlefi.substack.com/p/the-pendle-print-39)
- Usual also ran a "Golden YT" lottery for YT holders: >5B pills across 10 draws, Oct 25 – Nov 1, 2024 [OFFICIAL] — [Usual Blog](https://usual.money/blog/golden-yt-winners)
- Gap: total pills and an official $/pill were not found.

**Resolv (Points → RESOLV)**
- S1 lasted 9 months and ended with the Genesis Airdrop: **10% of the 1B supply (100M RESOLV)**, fully unlocked at TGE except "small vesting for large recipients" [SECONDARY] — [BingX Academy](https://bingx.com/en/learn/article/what-is-resolv-protocol-and-how-to-claim-your-resolv-token-airdrop); [Resolv docs S1](https://docs.resolv.xyz/litepaper/using-resolv/resolv-points/seasons/season-1)
- Points collected before May 2, 2025 counted. Claim window was May 27 – June 27, 2025. Tokens were distributed as **stRESOLV (staked) with a 2-week unstake cooldown** [OFFICIAL] — [Resolv docs – airdrop](https://docs.resolv.xyz/litepaper/resolv-token/resolv-token-airdrop)
- S1 point rates: USR 30 pts/$/day, RLP 10, stUSR 5; boosts of +20–75% [OFFICIAL] — [Resolv docs S1](https://docs.resolv.xyz/litepaper/using-resolv/resolv-points/seasons/season-1)
- Trading began June 10, 2025 on Binance Alpha. Pre-launch projection: FDV $360M at $0.30 with ~120M circulating. ATH was $0.4075–0.4108 on June 11, 2025 [SECONDARY] — [Bitget Academy](https://web3.bitget.com/en/academy/resolv-resolv-listing-details-binance-launch-time-and-price-prediction); [CryptoRank](https://cryptorank.io/price/resolv)
- RESOLV is now about **-95.8% from ATH** [SECONDARY, snippet date ≈ Sep 2026] — [CryptoRank](https://cryptorank.io/price/resolv)
- TVL was $349M in mid-June 2025 [OFFICIAL] — [Resolv weekly Jun 16](https://resolvlabs.substack.com/p/resolv-weekly-june-16)
- The S3 airdrop claim ran Dec 16, 2025 – Jan 16, 2026, so later seasons also converted [OFFICIAL] — [Resolv docs](https://docs.resolv.xyz/litepaper/resolv-token/resolv-token-airdrop)
- **[EST] S1 value = 100M × $0.30–0.41 ≈ $30–41M at launch; ≈ $1.7M at today's price (−95.8% from ATH).**
- Gap: total S1 points were not published.

**Falcon Finance (Falcon Miles → FF)**
- FF supply is 10B. "Community Airdrops & Launchpad Sale" is 8.3%, covering the Miles program, the Buidlpad sale and Kaito Yap2Fly [OFFICIAL] — [Falcon tokenomics](https://falcon.finance/news/introducing-ff-tokenomics)
- The free airdrop program totals 150M FF (~1.5% of supply), split across Falcon Miles, Kaito stakers and the top 200 Yap2Fly rankers. About 23.4% of supply circulated at TGE [SECONDARY] — [Bittime](https://www.bittime.com/en/blog/airdrop-falcon-finance-ff); [airdrops.io](https://airdrops.io/falcon-finance/)
- Claim ran Sep 29 – Dec 28, 2025, and FF trading opened Sep 29, 2025 [SECONDARY] — [Hokanews](https://www.hokanews.com/2025/09/falcon-finance-airdrop-goes-live.html)
- FF peaked at $0.75 and hit a low of $0.17 (−76%) by Sep 30, 2025, amid "delayed claims, influencer and possibly team selling." Claim-page rollouts were uneven, and Kaito participants got disproportionate allocations [SECONDARY] — [Cryptopolitan](https://www.cryptopolitan.com/falcon-finance-loses-suspected-team-selling/)
- "Started at $6.7B FDV and fell 85.83% to $949.7M" [UNVERIFIED snippet, date unclear]
- Pendle claimed 2.32M FF (≈$294K) from Miles Season 1 on Oct 10, 2025 [SECONDARY] — [Phemex/Lookonchain](https://phemex.com/news/article/pendle-claims-294k-in-falcon-finance-airdrop-25424). **[EST] Implied FF price = $294K / 2.32M ≈ $0.127.**
- Falcon ran Miles multipliers up to 60x/day for USDf and 36x for sUSDf on the Pendle SY portion. Newer pools (Jan 29, 2026 maturity) offered 72x for YT-sUSDf and LP for two weeks [SECONDARY] — [Falcon deep dive](https://falcon.finance/news/falcon-finance-deep-dive-usdf-miles--yap2fly-)
- USDf supply was ~$1.8–2B around TGE [OFFICIAL/SECONDARY] — [Falcon tokenomics](https://falcon.finance/news/introducing-ff-tokenomics)
- **[EST] The whole 150M FF pool is worth $19M at $0.127 and $112M at the $0.75 peak.** The Miles share is only part of it, so the airdrop yield per $ of USDf was likely low single digits unless the recipient held multiplier positions.

**Huma (Feathers → HUMA)**
- HUMA supply is 10B. Season 0 = 5% (500M HUMA): 65% to LPs pro-rata to Feathers, 25% to ecosystem partners, 10% to community. **Total Feathers at the May 18, 2025 snapshot: 2,682,116,734.** LPs were fully unlocked except institutional LPs. Claim opened May 26, 2025. Season 1 = 2.1% [OFFICIAL] — [Huma blog](https://blog.huma.finance/huma-airdrop-payfi-decentralized)
- HUMA traded at $0.06812 when the claim went live [SECONDARY] — [X @Airdrops_one](https://x.com/Airdrops_one/status/1927019585074602404)
- **[EST] HUMA per Feather = (500M × 65%) / 2,682,116,734 ≈ 0.121. $/Feather ≈ 0.121 × $0.06812 ≈ $0.0083.**
- Gate reports HUMA spiked to about $0.12 and then fell 78% (to $0.02566 by "May 29"). Its dates are internally inconsistent (it says "May 26, 2026"), so treat it with caution — [Gate Blog](https://www.gate.com/blog/huma-tge-price-drop-payfi-narrative-token-unlock-sell-pressure-analysis)

**Spark (SPK)**
- SPK supply is 10B. Ignition airdrop: 300M SPK (3%), claimable Jun 17 – Jul 29, 2025. Binance ran a separate 2% HODLer airdrop [SECONDARY] — [Gate Learn](https://www.gate.com/learn/articles/spark-airdrop-spk-airdrop-beginners-complete-claim-guide-ignition-overdrive-pre-farming-layer3-all-in-one/10900); [BingX](https://bingx.com/en/learn/article/spark-protocol-airdrop-guide-eligibility-and-how-to-claim-spk-tokens)
- Pre-farming [OFFICIAL] — [Spark docs](https://docs.spark.finance/airdrop/pre-farm):
  - S1 (Aug 20, 2023 – May 20, 2024): 130,434,783 SPK.
  - S2 (May 20, 2024 – Jun 16, 2025): 14,478,261 SPK/month on SparkLend plus 7,239,130/month on Aave.
  - Claim window: Jun 17 – Dec 17, 2025.
- SPK listed at $0.0745 on Jun 17, 2025 [SECONDARY] — [CCN](https://www.ccn.com/analysis/crypto/spark-spk-airdrop-price/). CCN's headline calls it an "$18 Million Airdrop". ATH was $0.19354 on Jul 23, 2025, and SPK is now −87% from ATH [SECONDARY] — [CoinGecko](https://www.coingecko.com/en/coins/spark)
- **[EST] Ignition value = 300M × $0.0745 ≈ $22M at listing.** This conflicts with CCN's "$18M" headline, which may use a lower price.
- Anecdote: a YT trader lost 86% on the position (excluding airdrop), then received 5,295 SPK on a $122 investment [UNVERIFIED, search summary].

**OpenEden (Bills → EDEN)**
- EDEN supply is 1B. Bills Airdrop = 7.5% (75M EDEN); Early Adopters 6%; Ecosystem & Community 41.22% [SECONDARY] — [Tokenomist](https://tokenomist.ai/openeden/tokenomics); [Bitget Academy](https://web3.bitget.com/en/academy/openeden-airdrop-guide-how-to-participate-and-claim-eden-rewards)
- Claim opened Sep 30, 2025 [SECONDARY] — [BingX](https://bingx.com/en/learn/article/openeden-airdrop-guide-how-to-claim-eden-tokens)
- ATH was $1.74 on Sep 30, 2025 (TGE day). Recent price ≈ $0.062 and FDV ≈ $63.8M, which is **−96% from ATH** [SECONDARY snippet] — [CoinMarketCap](https://coinmarketcap.com/currencies/openeden/)
- **[EST] Bills pool = 75M × $1.74 ≈ $130M at the TGE-day high, versus 75M × $0.062 ≈ $4.7M now.**

**GAIB (Spice → GAIB), the closest AI/GPU-dollar comparable**
- Spice base rate: 1 Spice per $1 per day. Bonuses: 1.25x for AID migration and 2x for sAID (Oct 31 – Nov 6). Galxe snapshot Nov 10, 2025. TGE Nov 19, 2025, 11:00 UTC. **Wallets receiving >1,000 tokens got 30% at TGE and 70% vested over 90 days** [OFFICIAL] — [GAIB blog](https://blog.gaibfoundation.org/gaib-token-launch-and-aid-alpha-airdrop/)
- GAIB supply is 1B: Community 40%, Ecosystem 19.5%, Core 20.7%, Backers 19.82%. About 26.3% was unlocked at TGE. $15M raised [SECONDARY] — [ICO Drops](https://icodrops.com/gaib/)
- The airdrop is "up to 10%" of supply [SECONDARY/UNVERIFIED] — [CoinGecko](https://www.coingecko.com/en/coins/gaib)
- ATH was $0.3402 on Nov 19, 2025 (TGE day). GAIB is now **−95.9%**, about $0.030, with FDV around $30–35M [SECONDARY] — [CoinGecko](https://www.coingecko.com/en/coins/gaib); [ICO Drops](https://icodrops.com/gaib/)
- **[EST] If the pool was 10% (100M GAIB), it was worth $34M at the TGE-day high and ≈ $3M at $0.030.** Because 70% of large allocations vested over 90 days during a ~90% decline, large holders realized far less than the TGE mark.
- Gap: total Spice issued and $/Spice were not found.

**USD.AI Season 1 (Allo → CHIP), the direct precedent for S2**
- S1 airdrop: 300M CHIP (3% of the 10B supply). ICO: 700M CHIP (7%) at $0.03 per CHIP, i.e. a $300M FDV. Both were 100% unlocked at TGE. S1 (the "Allo Game") ended Feb 18, 2026. The CoinList sale ran Feb 22–27, 2026. Team and investors have a 12-month cliff [SECONDARY] — [MEXC blog](https://blog.mexc.com/usdai-airdrop-guide-chip-eligibility-yield-strategies-and-season-2-opportunities/); [Tekedia](https://www.tekedia.com/usd-ai-releases-ico-and-airdrop-details/)
- Unaligned points were burned at the Feb 18, 2026 cutoff. TGE was Mar 30, 2026, and the claim deadline was May 30, 2026 [SECONDARY] — [MEXC Learn](https://www.mexc.com/learn/article/what-is-usd-ai-crypto-usdai-susdai-chip-token-and-allo-points-explained/1)
- CHIP tokenomics: 27.5% "Ecosystem Bootstrapping." "The first 10% was distributed during Season 1 … The remaining allocation will fund … airdrops, upcoming incentive programs" [OFFICIAL] — [USD.AI docs](https://docs.usd.ai/governance/tokenomics.md)
- CHIP listing and price path [SECONDARY] — [CoinGabbar](https://www.coingabbar.com/en/price-prediction/chip-price-prediction-usd-ai-buy-the-dip-or-exit):
  - Listed Apr 21, 2026 at $0.03.
  - ATH $0.1189 on Apr 22 (+296%).
  - $0.0789 around Apr 25.
- Latest CHIP price ≈ $0.04425 (late Sep 2026) [SECONDARY] — [CMC AI](https://coinmarketcap.com/cmc-ai/usd-ai/latest-updates/)
- TVL: peak $701M (Nov 2025); $450M on Mar 5, 2026 [SECONDARY] — [Whales Market](https://whales.market/blog/usd-ai-chip-fdv-prediction/)
- **[EST] S1 airdrop value** = 300M × $0.03 = $9.0M at the ICO price; ×$0.1189 = $35.7M at ATH; ×$0.0789 = $23.7M on Apr 25; ×$0.04425 = $13.3M now.
- **[EST] Protocol-level airdrop APR**, assuming ~$450M average TVL over ~0.75 years (the S1 start date was not verified): 9.0 / (450 × 0.75) ≈ **2.7% at the ICO price**, 3.9% now, 7.0% on Apr 25, and 10.6% at ATH. A plain sUSDai 2x holder's share was smaller than this proxy.

**USD.AI Season 1 case study (added at the coordinator's request)**
- **Structure: two paths for S1 Allo points.**
  - ICO path: "brown points at 5x multiplier." These gave the right to buy part of the 700M CHIP (7%) at $0.03 ($300M FDV).
  - Airdrop path: "teal points" at a "2x multiplier with native yield from sUSDai staking." These shared 300M free CHIP (3%).
  - Split of token value: 70% ICO / 30% airdrop. All S1 tokens were fully unlocked at TGE.
  - Sources [SECONDARY]: [Tekedia](https://www.tekedia.com/usd-ai-releases-ico-and-airdrop-details/); [PANews](https://panews.io/articles/c5b49d4c-f3f4-4e1c-8544-0451c0e4097b); [MEXC](https://blog.mexc.com/usdai-airdrop-guide-chip-eligibility-yield-strategies-and-season-2-opportunities/)
- Points had to be "aligned" to one path by Feb 18, 2026; **unaligned points were burned** [SECONDARY] — [MEXC Learn](https://www.mexc.com/learn/article/what-is-usd-ai-crypto-usdai-susdai-chip-token-and-allo-points-explained/1); [X @USDai_Official "How to Switch Alignment"](https://x.com/USDai_Official/status/2001338117580611883)
- **Pendle YT multipliers were cut mid-season.** YT-USDai holders' Allo multiplier went from **30x to 15x on Nov 18, 2025**, and YT-USDai volume fell 21.45% in 24h. Earlier cuts to deposit-related rewards had preceded this [SECONDARY, CMC AI summary] — [CoinMarketCap USDai analysis](https://coinmarketcap.com/cmc-ai/usdai/price-analysis/) (page 404 on fetch; content from search summary, so [UNVERIFIED])
- Before the cut, YTs got "12×–15× base Allo points" with a "25×–30× alignment multiplier" [UNVERIFIED snippet]. Pendle YT on Arbitrum earned "Allo points 30x faster" [SECONDARY] — [Blockchain.news](https://blockchain.news/flashnews/usdai-stablecoin-on-plasma-earn-allo-points-30x-faster-via-pendle-yt-on-arbitrum-for-ico-allocation)
- USDai "had just 32 holders before Pendle Boost Vaults launched on Aug 25, 2025"; USD.AI then ran 25x Allo multipliers on Pendle [UNVERIFIED snippet of Dune blog] — [Dune – The Pendle Effect](https://dune.com/blog/the-pendle-effect)
- Other data points:
  - At one point, sUSDai staking yielded 13.22% and USDai traded at about $1.03 [SECONDARY, undated ~Aug–Sep 2025] — [PANews](https://panews.io/articles/c5b49d4c-f3f4-4e1c-8544-0451c0e4097b)
  - A Pendle YT-USDai market maturing Nov 19, 2025 existed on Arbitrum — [Pendle app](https://app.pendle.finance/trade/markets/0x8e101c690390de722163d4dc3f76043bebbbcadd?view=yt&chain=arbitrum)
- **Total S1 Allo points and an official CHIP-per-point ratio were NOT found** in any public source reviewed: docs, MEXC, Tekedia, CoinGabbar, CryptoRank, airdrops.io. Exact $/point therefore cannot be computed; see Gaps.
- **[EST] Total value delivered to S1 points holders** (airdrop pool plus the ICO-path discount; formula: 300M × P + 700M × (P − $0.03)):
  - At P = $0.03 (ICO/TGE reference): $9.0M + $0 = **$9.0M**
  - At P = $0.1189 (ATH, Apr 22, 2026): $35.7M + $62.2M = **≈ $97.9M**
  - At P = $0.0789 (Apr 25, 2026): $23.7M + $34.2M = **≈ $57.9M**
  - At P = $0.04425 (late Sep 2026): $13.3M + $9.98M = **≈ $23.3M**
  - Caveat: the ICO path required paying $0.03/CHIP in cash, so its value is a discount, not a free airdrop.
- **[EST] $/point scaling.** Because total points are unknown, the airdrop-path value per point scales as $/point_now ≈ $/point_TGE × (P_now / $0.03) ≈ **1.475x the value at the ICO price** (and ≈3.96x at ATH). Whatever break-even a YT buyer computed at a $300M FDV improved by ~48% at today's price. The ICO path's value per point moved from $0 to (P − $0.03) per CHIP of allocation.
- **Was buying YT-USDai/YT-sUSDai in S1 profitable? (inference; no ROI dataset exists)**
  - Pre-TGE (Mar 5, 2026), YT farmers who bought "at elevated premiums … need FDV considerably above $300M to recover their cost" [SECONDARY] — [Whales Market](https://whales.market/blog/usd-ai-chip-fdv-prediction/)
  - Realized FDV was ≈$1.19B at the Apr 22 ATH, ≈$790M on Apr 25, and ≈$440M in late Sep 2026 (P × 10B).
  - So YT buyers who sold within the first days after listing very likely beat the "well above $300M" hurdle. Those who held to late Sep 2026 are near that hurdle ($440M ≈ 1.47x $300M), so the result depends on entry price. Buyers who entered before the Nov 18, 2025 multiplier cut (30x) earned twice the points per $ of YT that later buyers (15x) did.
  - The Level Up program offered "refund rights, discounted pricing, or a premium buyout" for locked YTs, which limited downside for participants who opted in [OFFICIAL] — [USD.AI Level Up guide](https://usd.ai/insights/allo-game-to-flatiron-level-up-guide)
  - **Net inference: S1 YT buyers were plausibly profitable if they entered early (30x era) and/or sold near listing. Late (15x-era) buyers holding to today are roughly break-even to modestly positive.** This cannot be quantified without total points and YT entry prices.

**Cap (caps → no token airdrop)**
- On Jan 31, 2026 the co-founder said "the CAP token will not be distributed via airdrop." Frontier users instead get a stablecoin "Stabledrop," and nearly 100% of circulating supply goes through a public sale [SECONDARY] — [Phemex](https://phemex.com/news/article/cap-cofounder-confirms-no-airdrop-for-cap-token-public-sale-to-distribute-supply-57230)
- The Frontier phase ended Feb 4, 2026 with a promised $12M cUSD stabledrop, later **cut to $4.2M (−65%)**. The founder apologized for committing "before the funding … was fully secured" [SECONDARY] — [The Defiant](https://thedefiant.io/news/defi/cap-airdrops-usd12-million-in-stablecoins-to-early-users); [The Defiant](https://thedefiant.io/news/defi/cap-cuts-its-stabledrop-airdrop-to-usd4-2m-from-usd12m-as-backlash-mounts)
- Homestead ran Jan 29 – Jul 23, 2026 at 10 caps/cUSD/day, including YT cUSD and LP [SECONDARY] — [Cryptoast](https://cryptoast.fr/cap-comment-farmer-airdrop-protocole-stablecoins/)
- A June 17, 2026 newsletter warned of "significant points dilution from long farming history" and said a cUSD stabledrop would follow the CAP TGE [SECONDARY] — [Today in DeFi](https://news.todayindefi.com/p/airdrop-alpha-re-protocol-tge-tomorrow)
- CAP auction ran Jun 8–18, 2026 at $0.0106 ($106M FDV), 5.5x oversubscribed. Day-1 close was a $325M FDV [OFFICIAL PR, Jul 7, 2026] — [GlobeNewswire](https://www.globenewswire.com/news-release/2026/07/07/3323565/0/en/cap-token-debuts-with-nearly-900m-in-10-day-volume-closing-at-a-325m-fdv-in-first-24-hours.html)

**Level (XP → no token)**
- Level was sunset after the team joined Sky/Grove (announced Sep 2025). Minting paused, final yield was Oct 2, 2025, and the frontend closed Dec 15, 2025. **The announcement says nothing about XP compensation or a token** [OFFICIAL] — [Level docs](https://level-money.gitbook.io/level-documentation); [X @levelusd](https://x.com/levelusd/status/1971274925357814188)
- lvlUSD peaked at a $185M market cap [OFFICIAL] — [X @levelusd](https://x.com/levelusd/status/1971274925357814188)

**Strata (points → STRATA, delayed)**
- On Jan 7, 2026 Strata said "Season 1 concludes in April 2026, followed by the $STRATA token launch." It advertised stacking 30x Strata + 30x Ethena points, with LP-srUSDe at 60x Strata + 35x Ethena [OFFICIAL/SECONDARY] — [Strata Paragraph](https://paragraph.com/@strata/stratas-next-phase-multi-market-expansion-and-the-road-to-tge); [AirdropAlert](https://airdropalert.com/airdrops/strata-markets/)
- The April 2026 target was missed. A later flag pointed to mid-September, with no new date given [SECONDARY] — [airdrops.io](https://airdrops.io/strata/)

**infiniFi (points → token, pending)**
- S1 ran six months from Jun 1, 2025 and issued ~5.6M points. TGE is confirmed for Q4 2026. S1 and the completed part of S2 carry fixed, non-diluting allocations, and activity from late Aug 2026 to TGE draws from a separate fixed pool [SECONDARY] — [Alea Research](https://alearesearch.substack.com/p/infinifi-season-1-points-and-2026); [KuCoin](https://www.kucoin.com/blog/infinifi-3m-seed-funding-electric-capital)

**Kinetiq (kPoints → KNTQ; HYPE LST, Hyperliquid-adjacent)**
- **24% of the 1B supply went to kPoints holders** (program Jul 15 – Nov 12, 2025), plus 1% to Hypurr holders. Recipients had to accept the ToS by Nov 21, 2025 [OFFICIAL via press] — [Blocmates](https://www.blocmates.com/news-posts/kinetiq-foundation-announces-kntq-token-launch-allocating-24-to-kpoints-holders); [Cryptonomist](https://en.cryptonomist.ch/2025/10/23/kinetiq-tokenomics-airdrop-kntq-governance-token/)
- KNTQ launched Nov 27, 2025 at $0.13 ($130M FDV), then about $0.17 ($170M FDV) shortly after, while protocol TVL fell 60% [SECONDARY] — [The Defiant](https://thedefiant.io/news/defi/hyperliquid-based-kinetiq-s-kntq-token-trades-at-usd130-million-valuation); [Bitget News](https://www.bitget.com/news/detail/12560605089581)
- **[EST] Pool value = 240M × $0.13–0.17 ≈ $31–41M.**

**Plasma (XPL; deposit/sale, not points)**
- 25M XPL was split equally among 2,687 verified depositors (9,304 XPL each), regardless of deposit size, so "some users … deposited as little as $0.1." Peak XPL was $1.45 (Sep 25–26, 2025), making each share worth more than $13,000 [SECONDARY] — [PANews](https://panews.io/articles/1237e3c6-812c-46b4-b0f8-8a30a3ddc7dc)
- XPL fell >80% by late October 2025, was near $0.20 by late November, and ~$0.075 by mid-August 2026. Stablecoins on Plasma dropped from >$6B to <$2B within two months [SECONDARY] — [Datawallet](https://www.datawallet.com/crypto/what-is-plasma-chain)

**Stable (STABLE; pre-deposit)**
- 10% (10B of 100B) went to the "Genesis Distribution" (airdrops, liquidity, exchange campaigns, depositors, including Pendle/Morpho/Uniswap deployers). TGE was Dec 8, 2025, and claims ran until Mar 2, 2026. Pre-deposits exceeded $1.1B [SECONDARY] — [EGW News](https://egw.news/crypto/news/30966/stable-launches-mainnet-and-tge-on-december-8-pJpu-XC9t); [Phemex](https://phemex.com/news/article/stable-launches-mainnet-and-distributes-stable-token-airdrop-42994)
- STABLE launched with a $0.046 ATH and was at $0.0157 on Dec 9, 2025 (−58.9% in 24h) [SECONDARY snippet] — [CoinMarketCap](https://coinmarketcap.com/currencies/stable/)

**Reservoir (points → DAM)**
- DAM launched on Binance Alpha on Aug 18, 2025. Each season guarantees at least 5% of supply. S3 began Dec 3, 2025 and runs 6 months [SECONDARY] — [CoinGabbar](https://www.coingabbar.com/en/crypto-currency-news/reservoir-airdrop-claim-and-listing-date-dam-price-prediction)
- DAM trades at about $0.0018 now [SECONDARY snippet] — [CoinGecko](https://coingecko.com/en/coins/reservoir)
- Gap: DAM's launch price was not found.

**Avalon (points → AVL)**
- AVL listed on Bybit Feb 12, 2025. 20% of supply goes to users and backers, mostly through Avalon Points [SECONDARY] — [Decrypt](https://decrypt.co/305462/avalon-labs-announces-avl-token-and-bybit-listing)
- Stage 2 required **holding USDa worth 15x the airdrop amount for 180 days** (three 60-day epochs from Mar 15, 2025). FDV was $53.7M on Feb 13, 2025 [SECONDARY] — [Boxmining](https://www.boxmining.com/avalon-labs-avl-token-airdrop-guide/)

**Elixir (potions → ELX; deUSD collapse)**
- In Nov 2025, deUSD collapsed after Stream Finance's $93M loss. Elixir had lent $68M (65% of deUSD reserves) to Stream. deUSD fell >97% in 24h to about $0.015–0.025, then Elixir sunset deUSD and targeted 1:1 USDC claims [SECONDARY] — [The Block](https://www.theblock.co/post/377961/elixir-sunsets-deusd-synthetic-stablecoin-following-stream-finance-unwinding-aims-full-redemptions); [FXStreet](https://www.fxstreet.com/cryptocurrencies/news/elixir-deusd-stablecoin-collapse-stream-finance-loss-2025-202511071458); [Pharos](https://pharos.watch/learn/case-studies/stream-elixir-contagion-2025/)

### Inferences
- **The $ value per season is shrinking.** Ethena's seasonal pool went from ≈$480M (S1) to ≈$210–315M (S2), ≈$178M (S3) and ≈$28M (S5, est.) as the % allocated fell (5% → 5% → 3.5% → 2%) and ENA's price fell. Mature programs pay far less per point than first seasons.
- Protocol-level airdrop APR for plain holders in 2025–26 programs appears to fall mostly in the **~2–15% range** at realistic sell prices. That is well below the 30–70%+ often projected mid-season. Ethena S2's projected 72% versus a realized ≈15–23% is the cleanest documented example of a 3–5x shortfall.
- **USD.AI S1 is the most directly relevant data point.** It was a small airdrop (3%, $9M at the ICO price) and roughly a 3–4% APR proxy at the late-Sep 2026 price. CHIP has held up better than almost every comparable: +47% vs ICO, while EDEN, GAIB and RESOLV are at −95%.

### Gaps
- Official total points were not found for Ethena (sats/shards), Usual (pills), Resolv, Falcon Miles, GAIB Spice or USD.AI Allo. $/point for those is therefore estimated from projections or a TVL proxy.
- No sourced data for f(x) Protocol or Elixir's potion → ELX conversion values.
- The exact Ethena S4 distributed amount is ambiguous (≥3.5% vs 1.5%).
- USD.AI S1 start date and average TVL were not verified, so the APR proxy is assumption-based.

---

## Q2. Realized value vs. Pendle YT market-implied value; share of YT points markets that were profitable; published analyses

### Takeaway
There is **no published aggregate** (Dune, Pendle, Steakhouse, Delphi, Messari) that systematically scores realized ROI across YT points markets. The Dune "Pendle Ethena ROI Dashboard" exists but could not be reviewed. Case evidence suggests clear YT winners were concentrated in 2024 first seasons (Usual YT-USD0++, Ethena S1). For the 2025–26 cohort of stablecoin YT points markets, most mid-season YT buyers likely lost money: many are down 90%+ from TGE-day highs, and several paid no token or a reduced amount (Level, Cap, Strata, Ethena S2). This is inference, not a measured statistic.

### Cited Findings
- YT mechanics: 1 YT earns the same points as 1 unit of underlying but costs a fraction of it, which gives leveraged points exposure [OFFICIAL] — [Pendle docs](https://docs.pendle.finance/pendle-v2/ProtocolMechanics/YieldTokenization/YT)
- A worked example (article last updated 2026-03-31) prices YT-sUSDe at 0.0161 USDe (≈62x leverage) and derives 415.8% APY from points minus a 22% yield loss, for **"393% APY."** The assumptions were ENA at $0.359 and a 3.5% airdrop. This is a projection, not a realized figure — [Gate Learn](https://www.gate.com/learn/articles/annualized-393-an-in-depth-analysis-of-the-real-yield-and-risks-of-the-pendle-yt-leverage-points-strategy/9296)
- Point-value formula used by analysts: "Single Point Value = Total Supply × airdrop% ÷ Final Total Points × FDV." Implied FDV is backed out of YT prices [SECONDARY] — [ChainCatcher](https://www.chaincatcher.com/en/article/2292254)
- Usual YT-USD0++: "almost ALL of YT buyers have profited greatly." Expected 3–4x, reported 5x to >10x [SECONDARY] — [AirdropMeta](https://www.airdropmeta.com/projects/pendle); [Gate Learn](https://www.gate.com/learn/articles/annualized-393-an-in-depth-analysis-of-the-real-yield-and-risks-of-the-pendle-yt-leverage-points-strategy/9296)
- Ethena S2 mid-season projections: Pendle YT strategy ROI 118.55%; ENA lock + USDe YT 162.56% (APY 454%) [SECONDARY] — [Gate Learn](https://www.gate.com/learn/articles/detailed-explanation-of-ethena-s-three-strategies-in-season-2-and-their-potential-rewards/2709). The realized plain-holder airdrop APR was ≈15–23% vs the 72% projected (see Q1 [EST]).
- USD.AI S1: YT farmers "who acquired Allo points by purchasing yield tokens at elevated premiums … need FDV considerably above $300M to recover their cost" (Mar 5, 2026) [SECONDARY] — [Whales Market](https://whales.market/blog/usd-ai-chip-fdv-prediction/) (quoted via search summary; the fetched page did not quantify the break-even)
- USD.AI "Level Up" (Feb 26, 2026): locking Pendle YTs (≈0.18 YT-USDai or ≈0.40 YT-sUSDai per $1 of CHIP allocation) gives "refund rights, discounted pricing, or a premium buyout on your CHIP allocation." There is an Overlock bonus: "20% bonus up to 2x of your Level Up Score" plus a Flatiron (S2) points multiplier [OFFICIAL] — [USD.AI Level Up guide](https://usd.ai/insights/allo-game-to-flatiron-level-up-guide)
- Airdrop-path participants could "commit Season 2 Pendle YTs for guaranteed cash at $350M–$420M FDV at TGE" [SECONDARY] — [Tekedia](https://www.tekedia.com/usd-ai-releases-ico-and-airdrop-details/)
- Spark: anecdote of an 86% loss on a YT position excluding airdrop, which the SPK airdrop only partly offset [UNVERIFIED].
- Pendle claimed 2.32M FF (~$294K) for Falcon Miles S1 on Oct 10, 2025, i.e. at ≈$0.127/FF, 83% below FF's $0.75 peak [SECONDARY] — [Phemex](https://phemex.com/news/article/pendle-claims-294k-in-falcon-finance-airdrop-25424)
- The points meta is cyclical. Pendle TVL fell from $6.7B to $1.9B (−71%) when the "Point Meta" cooled in the earlier cycle [SECONDARY] — [Gate Learn](https://www.gate.com/learn/articles/pendle-beyond-the-point-meta/5053)
- A later search snippet says Pendle TVL fell from $13.38B (Sep 2025) to $3.44B (Jan 2026), −74.2% [UNVERIFIED].
- Commentators note that "whales and sophisticated farmers" farm at 20x+ leverage via YT and that YT is "the most misunderstood asset in airdrops" — [FIP Crypto on X](https://x.com/fipcrypto/status/1956731358073569415)
- Available dashboards: [Dune – Pendle Ethena ROI Dashboard](https://dune.com/ahkek/pendle-ethena-roi-dashboard); [Dune blog – The Pendle Effect](https://dune.com/blog/the-pendle-effect). Neither was rendered or reviewed.

### Inferences
- **YT break-even formula**, for use in the report: YT cost per $1 notional ≈ (1 − PT price). Expected payoff = underlying yield to maturity + (points per $ per day × multiplier × days to maturity × $/point).
  - Break-even $/point = (YT cost − expected yield) / (points per YT over its life).
  - Break-even FDV = break-even $/point × total points ÷ airdrop % ÷ total supply.
- **Scorecard (qualitative, inference; not a measured statistic):**
  - Likely profitable for mid-season YT buyers: Usual YT-USD0++ (2024); Ethena S1 (2024).
  - Plausibly profitable if sold near listing: USD.AI S1, given CHIP's 4x day-1 move and the Level Up buyout at $350–420M FDV.
  - Likely unprofitable or heavily diluted: Ethena S2 (≈3x realized shortfall vs projection); Falcon (1.5% airdrop pool, −76% day 1); Spark (anecdotal 86% loss); OpenEden, GAIB, Resolv (−95%+ from TGE highs, except for holders who sold instantly); Level (no token); Cap (no token; stabledrop cut 65%); Strata (TGE delayed 5+ months while YT decayed).
  - Rough share: fewer than 1 in 3 of the 2025–26 stablecoin YT points markets reviewed appear to have been clearly profitable for mid-season buyers. Treat this as a directional judgment only.
- Realized value versus market-implied value (inference): YT markets systematically overpriced points mid-season in 2025–26. The drivers were implicit FDV assumptions anchored on bull-market comparables, underestimated late-season point inflation, and TGE-day prices that did not hold.

### Gaps
- No published quantitative study of "share of YT points markets profitable" was found from Pendle, Steakhouse, Kairos, Delphi or Messari.
- No archived mid-season YT prices or implied FDVs were retrieved for specific markets (e.g., YT-sUSDai, YT-USDf, YT-RLP). Direct implied-vs-realized comparisons are therefore qualitative, except for Ethena S2's projection vs realized APR.

---

## Q3. Typical gap between season end/snapshot and TGE; typical % of supply to first seasons

### Takeaway
The snapshot-to-claim gap is usually **1 day to 6 weeks** (median ≈3–4 weeks). Some programs slip badly: Strata was 5+ months late with no date, infiniFi's TGE came ~10 months after S1 ended, and Level never launched. The first-season airdrop is typically **3–10% of supply (median ≈5%)**. Ethena's later seasons fell to 2–3.5%, and USD.AI S1 was 3%.

### Cited Findings
- Ethena S1: campaign ended Apr 1, 2024, and the airdrop landed Apr 2, 2024 (≈1 day) — [The Block](https://www.theblock.co/post/285212/ethena-labs-to-airdrop-750-million-ena-tokens-on-april-2)
- Ethena S2: ended Sep 2, 2024; claim opened ~Sep 30 (≈4 weeks) — [X @Airdrop_Adv](https://x.com/Airdrop_Adv/status/1830743545554321843?lang=en)
- Ethena S3: ended Mar 23, 2025; claim May 1, 2025 (≈5.5 weeks) [SECONDARY] — [X @Airdrop_Adv](https://x.com/Airdrop_Adv/status/1917709309632471225)
- Ethena S5: ended Mar 25, 2026; claim May 5, 2026 (≈6 weeks) — [KuCoin](https://www.kucoin.com/blog/how-to-claim-ethena-season-5-airdrop)
- Resolv: points cutoff May 2, 2025; claim May 27 (≈3.5 weeks); trading Jun 10 (≈5.5 weeks) — [BingX](https://bingx.com/en/learn/article/what-is-resolv-protocol-and-how-to-claim-your-resolv-token-airdrop); [Bitget](https://web3.bitget.com/en/academy/resolv-resolv-listing-details-binance-launch-time-and-price-prediction)
- Huma: snapshot May 18, 2025; claim May 26 (8 days) — [Huma blog](https://blog.huma.finance/huma-airdrop-payfi-decentralized)
- GAIB: snapshot Nov 10, 2025; TGE Nov 19 (9 days) — [GAIB blog](https://blog.gaibfoundation.org/gaib-token-launch-and-aid-alpha-airdrop/)
- Kinetiq: kPoints ended Nov 12, 2025; KNTQ launched Nov 27 (15 days) — [Cryptonomist](https://en.cryptonomist.ch/2025/10/23/kinetiq-tokenomics-airdrop-kntq-governance-token/); [The Defiant](https://thedefiant.io/news/defi/hyperliquid-based-kinetiq-s-kntq-token-trades-at-usd130-million-valuation)
- Spark: pre-farm S2 ended Jun 16, 2025; TGE Jun 17 (1 day) — [Spark docs](https://docs.spark.finance/airdrop/pre-farm)
- USD.AI: S1 ended Feb 18, 2026; TGE Mar 30 (≈6 weeks); exchange listing Apr 21 (≈9 weeks) — [MEXC](https://blog.mexc.com/usdai-airdrop-guide-chip-eligibility-yield-strategies-and-season-2-opportunities/); [CoinGabbar](https://www.coingabbar.com/en/price-prediction/chip-price-prediction-usd-ai-buy-the-dip-or-exit)
- Usual: Binance pre-market Nov 19, 2024 → spot Dec 18, 2024 → vesting to Jun 18, 2025 — [Usual Blog](https://usual.money/blog/airdrop-the-genesis-of-ownership); [CoinGape](https://coingape.com/will-usual-price-hit-1-as-binance-to-commence-spot-trading/)
- Strata: TGE promised for April 2026, missed, no date as of mid-Sep 2026 — [Strata](https://paragraph.com/@strata/stratas-next-phase-multi-market-expansion-and-the-road-to-tge); [airdrops.io](https://airdrops.io/strata/)
- infiniFi: S1 ended around Dec 2025; TGE "Q4 2026" — [Alea Research](https://alearesearch.substack.com/p/infinifi-season-1-points-and-2026)
- First-season % of supply:
  - Ethena 5% (S2 5%, S3 3.5%, S4 ≥3.5%, S5 2%) — [The Block](https://www.theblock.co/post/285212/ethena-labs-to-airdrop-750-million-ena-tokens-on-april-2); [KuCoin](https://www.kucoin.com/blog/how-to-claim-ethena-season-5-airdrop)
  - Usual 7.5% of TGE supply (8.5% per some) — [CMC Academy](https://coinmarketcap.com/academy/article/understanding-usual-a-guide-to-earning-pills-for-the-usual-airdrop)
  - Resolv 10% — [BingX](https://bingx.com/en/learn/article/what-is-resolv-protocol-and-how-to-claim-your-resolv-token-airdrop)
  - Huma S0 5% (3.25% to LPs), S1 2.1% — [Huma blog](https://blog.huma.finance/huma-airdrop-payfi-decentralized)
  - Spark: Ignition 3% plus ~1.3% pre-farm S1 plus monthly S2 — [Spark docs](https://docs.spark.finance/airdrop/pre-farm)
  - Falcon ~1.5% free airdrop, inside an 8.3% community-plus-sale bucket — [Falcon](https://falcon.finance/news/introducing-ff-tokenomics); [Bittime](https://www.bittime.com/en/blog/airdrop-falcon-finance-ff)
  - OpenEden 7.5% — [Tokenomist](https://tokenomist.ai/openeden/tokenomics)
  - GAIB "up to 10%" [UNVERIFIED]
  - Kinetiq 24% — [Blocmates](https://www.blocmates.com/news-posts/kinetiq-foundation-announces-kntq-token-launch-allocating-24-to-kpoints-holders)
  - Avalon 20% (users plus backers, conditional) — [Decrypt](https://decrypt.co/305462/avalon-labs-announces-avl-token-and-bybit-listing)
  - Stable 10% genesis (broad bucket) — [EGW](https://egw.news/crypto/news/30966/stable-launches-mainnet-and-tge-on-december-8-pJpu-XC9t)
  - Reservoir ≥5% per season — [CoinGabbar](https://www.coingabbar.com/en/crypto-currency-news/reservoir-airdrop-claim-and-listing-date-dam-price-prediction)
  - USD.AI S1 3% (plus a 7% ICO) — [MEXC](https://blog.mexc.com/usdai-airdrop-guide-chip-eligibility-yield-strategies-and-season-2-opportunities/)
  - Cap 0%: stablecoin stabledrop instead — [Phemex](https://phemex.com/news/article/cap-cofounder-confirms-no-airdrop-for-cap-token-public-sale-to-distribute-supply-57230)

### Inferences
- **[EST]** Median first-season % for the stablecoin-specific set, sorted (Falcon 1.5, USD.AI 3, Spark ~4.3, Ethena 5, Huma 5, Reservoir 5, Usual 7.5, OpenEden 7.5, Resolv 10, GAIB ~10): **median = 5%**. Second and later seasons are typically smaller: Ethena went 5 → 3.5 → 2; Huma 5 → 2.1.
- USD.AI's S1 (3%) was already below the median. If S2 follows the Ethena/Huma pattern, **2–3% of supply** is a reasonable base case; this is inference, since the S2 % has not been disclosed. The source is the remaining ~17.5% of the 27.5% Ecosystem Bootstrapping bucket, per [USD.AI docs](https://docs.usd.ai/governance/tokenomics.md).
- USD.AI S2 ("Flatiron") ends **2026-10-14**. This comes from a search snippet and was confirmed by the coordinator's context. Sources disagree on the S1 "TGE" date: some list the TGE event/claim start as Mar 30, 2026 ([MEXC Learn](https://www.mexc.com/learn/article/what-is-usd-ai-crypto-usdai-susdai-chip-token-and-allo-points-explained/1)), while exchange trading began Apr 21–22, 2026 ([CoinGabbar](https://www.coingabbar.com/en/price-prediction/chip-price-prediction-usd-ai-buy-the-dip-or-exit)). CHIP is already liquid, so the S2 distribution needs no new TGE. By Ethena's pattern for live tokens (claims 4–6 weeks after season end), an S2 claim around mid-Nov to late-Nov 2026 would be typical (inference). Delays of months happen elsewhere (Strata, infiniFi).

### Gaps
- USD.AI S2 allocation % and claim date were not confirmed from an official page. The end date of 2026-10-14 is per the coordinator plus a search snippet.
- USD.AI S1 total Allo points and CHIP-per-point were not published in any source found. The S1 YT entry prices and implied APYs (e.g., the Nov 19, 2025 YT-USDai market) were not retrievable, because Pendle app pages are not readable by fetch.

---

## Q4. Typical post-TGE drawdown (first 30/90 days) and effect on realized value when vested/locked

### Takeaway
The base rate is harsh. **84.7% of 118 tokens launched in 2025 trade below their TGE price, with a median FDV drawdown of −71%** (Memento Research, Dec 2025). Stablecoin and yield-dollar comparables were mostly −60% to −96% from TGE-day highs, often within days to weeks. Vesting or lock-ups (Usual top 1.5%, Ethena top 2,000, GAIB 70%/90 days, Resolv stRESOLV cooldown, Avalon's 180-day USDa hold) push realized value further below the TGE mark. CHIP (USD.AI) and CAP are notable exceptions that trade above their ICO/auction prices.

### Cited Findings
- Memento Research (Dec 21, 2025): 84.7% (100 of 118) of 2025 TGEs are below TGE price; median −71% FDV and −67% market cap; Plasma XPL −89.93% — [crypto.news](https://crypto.news/new-crypto-tokens-failing-in-2025-85-below-tge-prices/)
- FF: $0.75 peak to $0.17 low (−76%) within about a day (Sep 29–30, 2025) — [Cryptopolitan](https://www.cryptopolitan.com/falcon-finance-loses-suspected-team-selling/)
- STABLE: $0.046 to $0.0157 in 24h (−58.9%, Dec 8–9, 2025) — [CoinMarketCap](https://coinmarketcap.com/currencies/stable/)
- XPL: debuted Sep 25, 2025, peaked ~$1.68, **−80% by late October (≈30 days)**, ~$0.20 by late November (≈60 days), ~$0.075 by mid-August 2026 — [Datawallet](https://www.datawallet.com/crypto/what-is-plasma-chain)
- EDEN: ATH $1.74 on the Sep 30, 2025 TGE day; ~$0.062 now (−96%) — [CoinMarketCap](https://coinmarketcap.com/currencies/openeden/)
- GAIB: ATH $0.3402 on the Nov 19, 2025 TGE day; now −95.9% — [CoinGecko](https://www.coingecko.com/en/coins/gaib)
- RESOLV: ATH Jun 11, 2025 (day after listing); now −95.8% — [CryptoRank](https://cryptorank.io/price/resolv)
- SPK: listed at $0.0745 (Jun 17, 2025), rallied to a $0.194 ATH (Jul 23, 2025), now −87% from ATH — [CCN](https://www.ccn.com/analysis/crypto/spark-spk-airdrop-price/); [CoinGecko](https://www.coingecko.com/en/coins/spark)
- HUMA: reported −78% from its early peak within days (dates inconsistent in source) — [Gate Blog](https://www.gate.com/blog/huma-tge-price-drop-payfi-narrative-token-unlock-sell-pressure-analysis)
- ENA after S2 claim: +50% ($0.28 → $0.42, Oct 2024), a counter-example — [AirdropAlert](https://airdropalert.com/blogs/ethena-ena-price-surge-after-airdrop/)
- KNTQ: $0.13 → ~$0.17 shortly after launch (Nov 2025) — [Bitget News](https://www.bitget.com/news/detail/12560605089581)
- CHIP (USD.AI): $0.03 ICO → $0.1189 ATH (Apr 22, 2026) → $0.0789 (Apr 25) → ~$0.044 (late Sep 2026). That is −63% from ATH but +47% vs the ICO price — [CoinGabbar](https://www.coingabbar.com/en/price-prediction/chip-price-prediction-usd-ai-buy-the-dip-or-exit); [CMC AI](https://coinmarketcap.com/cmc-ai/usd-ai/latest-updates/)
- CAP: auction at $0.0106 → day-1 FDV $325M (≈3x the auction price) — [GlobeNewswire](https://www.globenewswire.com/news-release/2026/07/07/3323565/0/en/cap-token-debuts-with-nearly-900m-in-10-day-volume-closing-at-a-325m-fdv-in-first-24-hours.html)
- Vesting terms that reduce realized value:
  - Usual top 1.5%: 10% now, 90% over 6 months — [Usual](https://usual.money/blog/airdrop-the-genesis-of-ownership)
  - Ethena top 2,000: 50% vested 6 months — [KuCoin](https://www.kucoin.com/blog/how-to-claim-ethena-season-5-airdrop)
  - GAIB >1,000 tokens: 70% vested 90 days — [GAIB](https://blog.gaibfoundation.org/gaib-token-launch-and-aid-alpha-airdrop/)
  - Resolv: staked with a 2-week cooldown — [Resolv docs](https://docs.resolv.xyz/litepaper/resolv-token/resolv-token-airdrop)
  - Huma ecosystem partners: ⅓ at TGE, ⅔ at 3/6 months — [Huma](https://blog.huma.finance/huma-airdrop-payfi-decentralized)

### Inferences
- **[EST] Worked example for GAIB-style vesting.** Take 30% at TGE and 70% linearly over 90 days, with the price falling ~90% over that window. Realized value ≈ 0.30 × P0 + 0.70 × (average price over 90 days ≈ 0.3–0.4 × P0) ≈ **0.5–0.6 × P0** at best, and less if the price falls front-loaded. Tokens held past 90 days are worth ~0.05–0.1 × P0.
- For calibration, a reasonable prior for a stablecoin-protocol token's 90-day return from its TGE-day price is **−50% to −90%**. The earlier and more heavily farmed the airdrop (large YT/points overhang), the worse. USD.AI's CHIP is already trading and past TGE, so S2 recipients face ordinary market risk rather than TGE-discovery risk. But the S2 airdrop plus the April 2027 investor/team cliff unlock are known supply overhangs.

### Gaps
- Precise 30-day and 90-day prices after TGE were not retrieved for most tokens (FF, EDEN, GAIB, RESOLV, HUMA, SPK). Figures above are mostly peak-to-now.

---

## Q5. Common pitfalls (documented cases)

### Takeaway
Every pitfall the brief lists has at least one documented stablecoin-points case in 2024–26. The most damaging for YT buyers were: no token / program cancelled (Level, Cap), allocation cut after the fact (Cap −65%), much smaller % than expected (Falcon ~1.5%; USD.AI 3%), token dumps on TGE day (FF, STABLE, EDEN, GAIB), TGE delays (Strata), and depeg or collateral blow-ups (Elixir deUSD).

### Cited Findings
- **Late-season point inflation.** Ethena S2 sats were projected to grow from 1.76T to ~10T by season end — [Foresight News](https://www.binance.com/en/square/post/6273119441873); [Gate Learn](https://www.gate.com/learn/articles/detailed-explanation-of-ethena-s-three-strategies-in-season-2-and-their-potential-rewards/2709). Cap warned of "significant points dilution from long farming history" — [Today in DeFi](https://news.todayindefi.com/p/airdrop-alpha-re-protocol-tge-tomorrow). Falcon ran 72x Miles boosts on new Pendle pools — [Falcon](https://falcon.finance/news/falcon-finance-deep-dive-usdf-miles--yap2fly-)
- **Airdrop % lower than expected, and shrinking by season.** Falcon's free airdrop was ~1.5% of supply — [Bittime](https://www.bittime.com/en/blog/airdrop-falcon-finance-ff). Ethena went 5% → 2% by S5 — [KuCoin](https://www.kucoin.com/blog/how-to-claim-ethena-season-5-airdrop). USD.AI S1 was 3% — [MEXC](https://blog.mexc.com/usdai-airdrop-guide-chip-eligibility-yield-strategies-and-season-2-opportunities/)
- **Mid-season multiplier cuts for YT holders.** USD.AI cut the Allo multiplier for YT-USDai from 30x to 15x on Nov 18, 2025, and YT-USDai volume fell 21.45% in 24h [UNVERIFIED, CMC AI summary] — [CoinMarketCap](https://coinmarketcap.com/cmc-ai/usdai/price-analysis/). YT bought just before a cut earns half the expected points for the rest of its life.
- **No token or a changed reward form.** Cap's CAP was not airdropped; points were paid in stablecoins and the payout was cut from $12M to $4.2M — [Phemex](https://phemex.com/news/article/cap-cofounder-confirms-no-airdrop-for-cap-token-public-sale-to-distribute-supply-57230); [The Defiant](https://thedefiant.io/news/defi/cap-cuts-its-stabledrop-airdrop-to-usd4-2m-from-usd12m-as-backlash-mounts). Level was sunset with no XP compensation mentioned — [Level docs](https://level-money.gitbook.io/level-documentation)
- **Vesting and claim frictions.**
  - Usual top 1.5%: 90% vested 6 months, with a pay-to-skip option — [Usual](https://usual.money/blog/airdrop-the-genesis-of-ownership)
  - GAIB: 70% vested 90 days — [GAIB](https://blog.gaibfoundation.org/gaib-token-launch-and-aid-alpha-airdrop/)
  - Resolv: forced staking with a 2-week cooldown — [Resolv](https://docs.resolv.xyz/litepaper/resolv-token/resolv-token-airdrop)
  - Avalon: holding 15x the airdrop amount in USDa for 180 days to receive Stage 2 — [Boxmining](https://www.boxmining.com/avalon-labs-avl-token-airdrop-guide/)
  - USD.AI: points had to be "aligned" by Feb 18, 2026 or were burned — [MEXC Learn](https://www.mexc.com/learn/article/what-is-usd-ai-crypto-usdai-susdai-chip-token-and-allo-points-explained/1)
  - Kinetiq: recipients had to accept the ToS by a deadline — [Blocmates](https://www.blocmates.com/news-posts/kinetiq-foundation-announces-kntq-token-launch-allocating-24-to-kpoints-holders)
  - Short claim windows with forfeiture: Falcon until Dec 28, 2025, "unclaimed tokens will be permanently forfeited" — [Hokanews](https://www.hokanews.com/2025/09/falcon-finance-airdrop-goes-live.html); Ethena ~30-day windows — [MEXC](https://blog.mexc.com/news/ethena-airdrop-guide-before-the-season-5-deadline/)
- **Sybil and allocation-design surprises.** Plasma's equal split (9,304 XPL to every verified depositor) rewarded $0.1 deposits as much as whales' — [PANews](https://panews.io/articles/1237e3c6-812c-46b4-b0f8-8a30a3ddc7dc). Falcon's allocations were skewed toward Kaito participants — [Cryptopolitan](https://www.cryptopolitan.com/falcon-finance-loses-suspected-team-selling/). Cap's founder denied steering rewards to a wallet linked to his former employer — [The Defiant](https://thedefiant.io/news/defi/cap-cuts-its-stabledrop-airdrop-to-usd4-2m-from-usd12m-as-backlash-mounts)
- **TGE delays.** Strata missed its April 2026 target — [airdrops.io](https://airdrops.io/strata/). infiniFi's TGE is around 10 months after S1 ended — [Alea](https://alearesearch.substack.com/p/infinifi-season-1-points-and-2026)
- **Price dumps after TGE.** FF −76% day 1; STABLE −59% in 24h; XPL −80% in ~30 days; EDEN/GAIB/RESOLV −95%+ (see Q4) — [Cryptopolitan](https://www.cryptopolitan.com/falcon-finance-loses-suspected-team-selling/); [Datawallet](https://www.datawallet.com/crypto/what-is-plasma-chain); [crypto.news](https://crypto.news/new-crypto-tokens-failing-in-2025-85-below-tge-prices/)
- **Underlying/collateral risk that wipes YT and PT holders regardless of points.** Elixir deUSD fell >97% in 24h in Nov 2025 after 65% of reserves were lent to Stream Finance — [The Block](https://www.theblock.co/post/377961/elixir-sunsets-deusd-synthetic-stablecoin-following-stream-finance-unwinding-aims-full-redemptions); [Pharos](https://pharos.watch/learn/case-studies/stream-elixir-contagion-2025/)
- **Carry/leverage unwind.** Pendle's points-driven TVL "collapse was mechanical once incentives ended and yield compressed below borrowing costs" [UNVERIFIED snippet].

### Inferences
- For USD.AI S2, the specific risks to price into YT are:
  - A small S2 % (base case 2–3%).
  - Heavy multiplier concentration: locked YTs, Overlock bonuses and looping are "the primary points mechanism" in Flatiron, per the [USD.AI Level Up guide](https://usd.ai/insights/allo-game-to-flatiron-level-up-guide). This dilutes plain holders and late YT buyers.
  - Possible alignment, KYC or claim-deadline frictions, as in S1.
  - CHIP supply overhang: the S2 claim plus the April 2027 cliff unlock of investor/team tokens (33% at month 12).
- Mitigants specific to USD.AI:
  - The token is already liquid, so there is no TGE-discovery risk.
  - The Level Up buyout/refund mechanics offer something like a floor for committed YTs.
  - CHIP has outperformed its comparables since TGE.
- **[EST] Order-of-magnitude illustration only.** If S2 = 2–3% of 10B CHIP and CHIP stays ≈ $0.044 (FDV ≈ $440M), the S2 pool ≈ 200–300M × $0.044 ≈ **$8.8–13.2M**. Against a ~$450M+ average TVL over the season, that is a protocol-level airdrop yield in the low single digits, before multiplier skew.

### Gaps
- No verified official S2 allocation for USD.AI.
- No retrieved S2 YT-USDai/YT-sUSDai prices to compute an implied FDV. Both are needed to judge whether today's YT pricing is rich or cheap relative to these base rates.
