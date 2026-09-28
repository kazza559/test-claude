# Tori Finance (tori.finance): Fundamentals Profile, as of 2026-09-28

Identity check: this file covers the synthetic-dollar protocol at tori.finance (docs at docs.tori.finance, app at app.tori.finance, X @tori_finance). I confirmed it three ways: DefiLlama's `tori-finance` entry points to url `https://tori.finance/` and twitter `tori_finance` ([DefiLlama API](https://api.llama.fi/protocol/tori-finance)); the docs list the same token contracts that I queried on-chain ([Contracts](https://docs.tori.finance/resources/contracts)); and the stablecoin listing links to the same docs and X account ([DefiLlama stablecoin API](https://stablecoins.llama.fi/stablecoin/401)). Do not confuse it with **Teritori ($TORI)**, a separate Cosmos project that shows up in airdrop search results ([airdrops.io Teritori](https://airdrops.io/teritori/)). It is also unrelated to "Satori" on DefiLlama. Note too that "Pharos" means two things below: **pharos.watch** is a stablecoin analytics site, and **Pharos** is also an L1 chain that trUSD is bridged to.

All metrics carry dates. "On-chain (my query)" means I read the value myself with `eth_call` against the verified Ethereum contracts on 2026-09-28 at about 11:44 UTC (block ~26,075,735), using a public archive RPC. Contracts: trUSD [0xd058…1697](https://etherscan.io/address/0xd0580192E98eA6CEB9c7b6191Ed2E27560911697), strUSD [0x2808…5815](https://etherscan.io/address/0x280839980a7eD0D7717F64125fE241012E5F5815), trUSD Silo [0xF7c0…60B4](https://etherscan.io/address/0xF7c0d8853E69DCD37ee7599c6280d2632F3360B4), etrUSD (Tori Ecosystem Vault) [0x6f20…592d](https://etherscan.io/address/0x6f20aE2C98c2D34e6A57f3411f2C5Af92E32592d), CCIP strUSD Lock/Release pool [0xb12E…c38B](https://etherscan.io/address/0xb12E0794fB2191672bA7A1811eDC9713C8c2c38B).

---

## 1. What is Tori Finance, how does trUSD/strUSD work, what are the yield sources, and what is the current strUSD APY?

### Takeaway
Tori is an Ethena-style two-token synthetic dollar. **trUSD** is the base token and pays no yield. **strUSD** is the staked ERC-4626 token and earns yield. The backing is not mainly crypto perp-funding basis. It is mostly **off-chain TradFi strategies held with custodian banks**: about 70% "money market instruments" (per RockawayX, emerging-market money markets FX-hedged to USD), about 9% delta-neutral *equity* arbitrage, about 9.5% FX collateral, and about 11% on-chain USDC/USDT buffer (Accountable/Tori solvency feed, 2026-09-28). strUSD realized roughly **10–13.7% APY** from July to September 2026: about 10.5% annualized since inception, 11.2% on the trailing 7 days as of 2026-09-28, and 12.0% per DefiLlama.

### Cited Findings
**Product and mechanism (official docs)**
- Self-description: "Tori Finance is a synthetic dollar protocol that brings institutional-grade, market-neutral strategies on-chain." trUSD is "backed by trading positions, which is different from fiat-backed stablecoins like USDC or USDT" — [Docs: Introduction](https://docs.tori.finance/index)
- Two tokens. **trUSD** is "the base synthetic dollar" and is not rewarded when unstaked. **strUSD** ("Staked trUSD", ticker strUSD) is an ERC-4626 vault receipt whose trUSD exchange rate rises as rewards arrive. It does not rebase. Staking is instant and unstaking has a **7-day cooldown** — [Docs: strUSD](https://docs.tori.finance/products/strusd); [Docs: trUSD](https://docs.tori.finance/products/trusd)
- Retail access means swapping USDC/USDT for trUSD on secondary markets "No verification required". Direct mint and redeem at NAV is open only to KYC/AML-verified, whitelisted participants and costs a **10 bps fee** on each side ("covers the costs … of entering and exiting the underlying backing positions. It is not protocol revenue") — [Docs: Minting & Redemption](https://docs.tori.finance/resources/institutional)
- The peg relies on arbitrage by verified minters and redeemers at NAV: "The bound is redemption, not market depth" — [Docs: Peg Mechanism](https://docs.tori.finance/solution/peg-mechanism)
- Fees: staking and unstaking are free. "The protocol keeps a share of that gross carry as protocol revenue, which funds operations and the reserve fund, and pays rewards to strUSD out of the remainder." The published rate is net. The size of the share is **not disclosed** — [Docs: strUSD](https://docs.tori.finance/products/strusd)
- Legal wrapper: the issuer is **Tori (BVI) Limited**, and a **Tori Foundation** is also named. Buying trUSD "is a final sale transaction, not a deposit… Tori becomes the owner of any assets you transfer". Holding trUSD/strUSD confers no "ownership interest, governance rights, dividend rights, or profit-sharing rights" — [Docs: General Risk Disclosures](https://docs.tori.finance/legal/risk); [Docs: trUSD Protocol User Agreement](https://docs.tori.finance/legal/trusd-protocol)
- Access is restricted in some jurisdictions, "including the United States and the EU/EEA" — [Docs: Market Landscape](https://docs.tori.finance/resources/comparison)

**Yield sources (official)**
- There are three market-neutral strategy types. **Money markets** are "usually our largest allocation… institutional short-term lending rates… any non-USD exposure is hedged". **Futures arbitrage** is cash-and-carry; the docs' worked example uses AAPL spot and futures. **Calendar spreads** trade near versus far expiries. "New strategies get added when the risk-reward clears the bar" — [Docs: Strategy Overview](https://docs.tori.finance/strategy/overview)
- RockawayX, which curates the Tori Ecosystem Vault, describes the money-market leg as "selected emerging-market money markets", with "the FX exposure… hedged back to USD through forward contracts". It lists "FX hedge and rollover risk" among the key risks. No percentage allocation or backtest is published — [RockawayX investment thesis & risk disclosure](https://www.rockawayx.com/insights/rockawayx-tori-ecosystem-vault-investment-thesis-risk-disclosure)
- Founder quote: "The yield is generated from real economic activity, not from recycling crypto-native capital. The trade itself is not proprietary. The hard part is access." — [The Defiant PR, 2026-07-27](https://thedefiant.io/news/press-releases/tori-brings-institutional-trades-on-chain-fills-50m-before-launch)
- Homepage: "we harness market opportunities that exist everywhere, from New York to Tokyo". It also says off-chain collateral "is held with BitGo, Anchorage Digital and Cactus Custody in segregated accounts" — [tori.finance homepage, scraped 2026-09-28](https://tori.finance/)

**Live reserve composition (Tori/Accountable solvency feed, 2026-09-28 11:34 UTC)** — [app.tori.finance/api/solvency](https://app.tori.finance/api/solvency) (it backs [app.tori.finance/transparency](https://app.tori.finance/transparency) and [tori.accountable.capital](https://tori.accountable.capital))
- Total reserves were **$75,322,475** against a liability supply of **74,886,300 trUSD**. Collateralization was **100.58%**, a net surplus of $436,175.
- Breakdown:
  - **Money Markets**: $52.97M (70.3%)
  - **On-chain Liquidity**: $8.56M (11.4%), made up of USDC in Morpho $6.11M, USDC $2.34M and USDT $0.11M
  - **Cash & Equivalents**: $7.15M (9.5%), almost all labelled "FX Collateral"; "OTC & Exchange Reserve" was $0
  - **Delta-Neutral Equity Arbitrage**: $6.64M (8.8%)
- Custody split: "Regulated custodian banks" 90.5%, "Regulated investment banks" 9.5%, "On-chain custody" 0%. Weighted-average maturity was **7 days** (as of 2026-09-25). Pricing sources listed are "Regulated Asset Manager", "Execution Venue Marks" and "NAV / Share Price". Proof flags (merkle root, Nitro TEE, zk liabilities, zk collateral) are all set to true.
- Conflict: aggregator and AI summaries describe trUSD as "capturing funding rate on perpetual hedges", and pharos.watch's generic "synthetic delta-neutral" template text describes perp shorts. Tori's own docs and the solvency feed show **no crypto perp/funding bucket**; the arbitrage bucket is labelled *equity* arbitrage. pharos.watch's own static profile also adds "options strategies" — [pharos.watch trUSD](https://pharos.watch/stablecoin/trusd-tori/)

**strUSD APY**
- The app's APY is "the trailing 7 days of realized performance, annualized with daily compounding" — [Docs: General FAQ](https://docs.tori.finance/faq/general)
- Solvency feed `apyTimeline`, hourly from 2026-07-09 to 2026-09-28:
  - Range 10.16%–13.73%, peaking about 13.7% around 2026-07-22 and bottoming about 10.27% around 2026-09-16
  - Daily closes: 12.9% on Jul 15, 13.08% on Jul 27, 11.33% on Aug 1, 10.74% on Aug 14, 10.64% on Aug 31, 10.49% on Sep 7, 10.30% on Sep 14, 10.46% on Sep 21, **11.17% on Sep 28**
  - Source: [app.tori.finance/api/solvency](https://app.tori.finance/api/solvency)
- DefiLlama yields, strUSD pool, 2026-09-28: **APY 12.02%**, 30-day mean **10.64%**, pool TVL $47.09M, poolMeta "7 days unstaking" — [DefiLlama yields pools](https://yields.llama.fi/pools); history at [yields chart](https://yields.llama.fi/chart/e7fdda30-ce71-5dea-8b3a-dd43de77ce55)
- On-chain exchange rate (my query) of trUSD per strUSD:
  - 1.000000 (06-25), 1.000902 (07-05), 1.004023 (07-15), 1.009031 (07-30), 1.013460 (08-14), 1.017790 (08-29), 1.020315 (09-07), 1.022244 (09-14), 1.024200 (09-21), 1.025310 (09-25), **1.026298 (09-28)**
  - Implied: **~10.1% APR / 10.5% APY since inception** (95 days). By window: 12.0–12.9% APY in mid-to-late July, 10.9–11.3% in August, 10.35–10.6% in early September, 11.26% for 09-21→09-28.
  - Source: [strUSD contract](https://etherscan.io/address/0x280839980a7eD0D7717F64125fE241012E5F5815)
- Advertised rates over time:
  - "~15%" at the 2026-03-24 announcement ([pharos.watch timeline citing Tori's X post](https://pharos.watch/stablecoin/trusd-tori/); [PANews, "up to approximately 15%"](https://panews.io/articles/019d24a9-7508-7621-9040-5569a9715caf))
  - "12% APY" at the 2026-07-27 launch PR ([The Defiant](https://thedefiant.io/news/press-releases/tori-brings-institutional-trades-on-chain-fills-50m-before-launch))
  - 10.2%/10.6% displayed on the homepage on 2026-09-28 ([tori.finance](https://tori.finance/))
- RockawayX vault targets were "Phase 1: Points APY 8.73% • Real APY 8% • Total 16.73%" and "Phase 2: 6.9% points + 10% real = 16.9%". The methodology for the points value is **not disclosed** — [RockawayX thesis](https://www.rockawayx.com/insights/rockawayx-tori-ecosystem-vault-investment-thesis-risk-disclosure)
- Reserve fund: it is funded by "a portion of the share of gross carry" plus "Seed capital allocated at launch". It is used only for "extraordinary events", not to smooth normal drawdowns. Its size is disclosed only inside the attestations — [Docs: Reserve Fund](https://docs.tori.finance/solution/reserve-fund). pharos.watch says "the size of the protocol reserve fund is undisclosed" — [pharos.watch](https://pharos.watch/stablecoin/trusd-tori/)

### Inferences
- Economically, trUSD looks less like Ethena (crypto perp basis) and more like a tokenized TradFi carry desk. Its largest risk is an FX-hedged EM money-market carry trade. The Istanbul-based founder, RockawayX's "emerging-market money markets", the "FX Collateral" bucket, and the BiLira Pro flows traced by pharos.watch (see §5) together *suggest* Turkish lira money markets hedged with USD/TRY forwards. **This is an inference, not an official statement.**
- Because the yield is not tied to crypto funding rates, strUSD APY should be less correlated with crypto market sentiment. It is more exposed to EM rate and FX-forward pricing and to counterparty and convertibility risk.
- Realized strUSD yield has been a stable 10–11% since August, below the ~15% advertised in March and the 12% at launch. The docs acknowledge "rewards may compress as the protocol scales."

### Gaps
- The protocol's share of gross carry (the performance fee) is not published.
- There is no per-market or per-currency breakdown of the "Money Market Instruments" bucket, and custodian bank and counterparty names for the 90.5% bucket are not given (see the conflict in §5).
- The size of the reserve fund could not be extracted from the public API fields I saw.
- A web-search summary claimed "one partner with over 25 years running similar strategies for pension funds… managing $10-20 billion". I could not find the original source, so treat it as **unverified**.

---

## 2. TVL, circulating supply, and growth history

### Takeaway
trUSD supply went from zero to about $50M in the first week of the pre-deposit phase (from 2026-06-23). It held flat at the $50M cap until late July, grew to about $66M by the end of August, and reached **$73.06M (DefiLlama) / 75.19M (on-chain totalSupply)** on 2026-09-28. That is about +46–50% since early July and +10.4% over 30 days. About 47.1M trUSD (≈63%) is staked as strUSD. Separately, about **10.8M trUSD sits in the unstaking silo** after a large unstake request around 2026-09-22/24.

### Cited Findings
- DefiLlama lists the protocol as **Category "Basis Trading"**, chain **Ethereum**, methodology "Supply of trUSD", listedAt 2026-06-24. Current TVL is **$73,063,328** (2026-09-28 10:16 UTC) — [DefiLlama API: protocol/tori-finance](https://api.llama.fi/protocol/tori-finance) / [DefiLlama page](https://defillama.com/protocol/tori-finance)
- DefiLlama daily TVL, $M:

  | Date | TVL ($M) |
  |---|---|
  | 06-26 | 45.85 |
  | 06-30 | 49.51 |
  | 07-02 | 49.99 |
  | 07-15 | 50.08 |
  | 07-28 | 50.25 |
  | 07-29 | 51.53 |
  | 07-30 | 54.39 |
  | 08-01 | 54.80 |
  | 08-07 | 58.77 |
  | 08-10 | 61.07 |
  | 08-14 | 63.82 |
  | 08-21 | 64.34 |
  | 08-27 | 66.15 |
  | 09-01 | 66.23 |
  | 09-08 | 66.45 |
  | 09-13 | 67.83 |
  | 09-21 | 67.91 |
  | 09-23 | 69.66 |
  | 09-24 | 71.93 |
  | 09-26 | 73.03 |
  | 09-28 | 73.06 |

  Month-ends: **Jun 49.5 → Jul 54.8 → Aug 66.2 → Sep (28th) 73.1** — [DefiLlama API](https://api.llama.fi/protocol/tori-finance)
- DefiLlama stablecoin "Tori trUSD" (id 401, pegMechanism "crypto-backed", gecko_id `tori-trusd`): circulating **$73.06M**, prior week $67.96M, prior month $66.17M. Chains are Ethereum ($73.06M), Monad (~$6) and Pharos (~$1.4). Price $1.0002 — [DefiLlama stablecoins API](https://stablecoins.llama.fi/stablecoins?includePrices=true); [DefiLlama trUSD page](https://defillama.com/stablecoin/tori-trusd)
- pharos.watch shows supply 73.05M, **+7.49% over 7 days and +10.39% over 30 days**, and "Issued … 24 Jun 2026" — [pharos.watch](https://pharos.watch/stablecoin/trusd-tori/)
- On-chain history (my query):

  | Date | trUSD supply | strUSD supply | Silo (trUSD) | etrUSD supply | strUSD locked in CCIP pool |
  |---|---|---|---|---|---|
  | 06-15 | 1,000 | 0 | 0 | 0 | 0 |
  | 06-25 | 42.72M | 20.00M | 0 | 45.14M | 0 |
  | 07-05 | 50.02M | 25.01M | 0 | 50.00M | 0 |
  | 07-15 | 50.11M | 25.01M | 0 | 50.00M | 0 |
  | 07-30 | 54.40M | 35.43M | 2.3K | 49.15M | 0 |
  | 08-14 | 63.96M | 44.62M | 6.3K | 45.75M | 0 |
  | 08-29 | 66.15M | 47.46M | 8.2K | 44.81M | 0 |
  | 09-07 | 66.45M | 48.38M | 82K | 44.29M | 0 |
  | 09-14 | 67.84M | 49.96M | 2.1K | 44.08M | 0 |
  | 09-21 | 67.94M | 49.98M | 15K | 43.99M | ~0 |
  | 09-25 | 72.55M | 44.16M | **10.78M** | 43.78M | 6.14M |
  | **09-28** | **75.19M** | **45.88M** (= **47.09M trUSD** totalAssets) | **10.77M** | **44.08M** | **6.15M** |

  Sources: [trUSD](https://etherscan.io/address/0xd0580192E98eA6CEB9c7b6191Ed2E27560911697), [strUSD](https://etherscan.io/address/0x280839980a7eD0D7717F64125fE241012E5F5815), [Silo](https://etherscan.io/address/0xF7c0d8853E69DCD37ee7599c6280d2632F3360B4), [etrUSD](https://etherscan.io/address/0x6f20aE2C98c2D34e6A57f3411f2C5Af92E32592d), [CCIP strUSD pool](https://etherscan.io/address/0xb12E0794fB2191672bA7A1811eDC9713C8c2c38B)
- The solvency feed's reserve/supply timeline:

  | Date | Reserves | Supply |
  |---|---|---|
  | 06-25 | $45.90M | 45.17M |
  | 07-06 | $50.18M | 50.02M |
  | 07-29 | $54.66M | 54.40M |
  | 08-14 | $64.20M | 63.96M |
  | 09-01 | $66.46M | 66.25M |
  | 09-22 | $68.51M | 67.94M |
  | 09-24 | $72.34M | 71.95M |
  | 09-28 (11:34) | $75.32M | 74.89M |

  Reserves were ≥100% of supply at every point shown — [app.tori.finance/api/solvency](https://app.tori.finance/api/solvency)
- Pre-deposit phase:
  - Cap $50M, USDC/USDT only, Ethereum, LP token etrUSD, 30-day hard lock, fees waived, curated by RockawayX via Upshift — [Docs: Pre-Deposit Vault](https://docs.tori.finance/resources/pre-deposit)
  - "$44M" came in during the first 24 hours — [CoinGecko Learn (sponsored), 2026-08-20](https://www.coingecko.com/learn/pendle-tori-trusd-strusd-institutional-yield)
  - The cap "filled in seven days" — [The Defiant PR, 2026-07-27](https://thedefiant.io/news/press-releases/tori-brings-institutional-trades-on-chain-fills-50m-before-launch)
- Homepage on 2026-09-28 showed "TVL $75.2M" — [tori.finance](https://tori.finance/)

### Inferences
- The TVL ran in three steps: a $50M pre-deposit cap (late June), public launch plus integrations (Jul 27 to mid-Aug, +$14M), and a slow grind in late August and September (+$2M a month) until a +$7M jump on 2026-09-22/28. The last jump coincides with the Monad and Pharos CCIP lanes going live, and about 6.15M strUSD is now locked in the Ethereum CCIP pool, mostly used on Monad per DefiLlama (see §4).
- The 10.77M trUSD in the Silo (about 14% of supply) appeared between 09-21 and 09-25. The 7-day cooldown means those unstakes mature around 2026-09-29 to 10-01. Whether they are redeemed out, restaked, or simply left unclaimed will be a useful near-term flow signal. This is my reading of on-chain data; the docs describe the Silo only as the cooldown holding contract.
- Concentration: the RockawayX/Upshift Ecosystem Vault (etrUSD, 44.08M supply) was essentially the entire initial TVL, and it still has a supply equal to about 59% of trUSD supply. The vault holds no trUSD or strUSD directly at its token address (my query returned 0 for both). Its positions sit in DeFi venues, and its Phase 2 targets are Curve and Pendle LPs. Much of Tori's TVL is therefore one curated, points-motivated pool of capital.

### Gaps
- Month-by-month holder counts and Dune dashboards were not found.
- CoinGecko market-chart data was rate-limited (HTTP 429).
- The ~300K gap between the solvency feed's "totalSupply" (74.886M) and on-chain totalSupply (75.186M) at nearly the same time is unexplained. It may be protocol-held or excluded tokens.

---

## 3. Team, investors, funding rounds, and any exchange-affiliated backers

### Takeaway
Tori has one disclosed **seed round led by Delphi Ventures**, announced 2026-03-24/25, with **amount and valuation undisclosed**. Named participants differ by source: QInvest, CMCC Global and Bering Waters in one; ScaleX Ventures and QInvest in another. The only publicly identified founder is **Samed Düzçay** (Istanbul). I found **no** exchange-affiliated investor such as Binance Labs/YZi, Coinbase Ventures or OKX Ventures.

### Cited Findings
- Delphi's Tommy Shaughnessy posted on 2026-03-24 (21:03 UTC per the X snowflake ID): "Delphi Ventures is extremely excited to lead the seed round for @tori_finance… packaging institutional delta-neutral strategies into a composable, yield-bearing token: strUSD" — [X post](https://x.com/Shaughnessy119/status/2036549390886903837)
- PANews on the seed round (March 25): Delphi Ventures leads; "The specific amount raised and valuation in this round were not disclosed"; strUSD targets "up to approximately 15%" — [PANews](https://panews.io/articles/019d24a9-7508-7621-9040-5569a9715caf)
- DefiLlama raises data: Seed, dated 2026-03-24, amount **null**, lead "Delphi Digital", valuation null — [DefiLlama API](https://api.llama.fi/protocol/tori-finance). Crypto-Fundraising lists "Raised Mar 2026 · TBD · Seed" — [crypto-fundraising.info](https://crypto-fundraising.info/projects/tori-finance/)
- Participants per the pharos.watch timeline, citing Cryip on 2026-03-25: "Delphi Ventures leads seed round; QInvest, CMCC Global, Bering Waters also participate" — [pharos.watch](https://pharos.watch/stablecoin/trusd-tori/) (original: [Cryip](https://cryip.co/tori-secures-backing-from-delphi-ventures-for-on-chain-yield-protocol/), not fetched directly). RockawayX instead says "backed by Delphi Ventures with additional support from **ScaleX Ventures and QInvest**" — [RockawayX thesis](https://www.rockawayx.com/insights/rockawayx-tori-ecosystem-vault-investment-thesis-risk-disclosure). The two lists differ, so treat the full syndicate as uncertain.
- RockawayX is also described as "anchor LP" and risk curator ("manages over $2B in digital assets") — [CoinGecko Learn, 2026-08-20](https://www.coingecko.com/learn/pendle-tori-trusd-strusd-institutional-yield); [The Defiant PR](https://thedefiant.io/news/press-releases/tori-brings-institutional-trades-on-chain-fills-50m-before-launch)
- Founder: **Samed Düzçay**, listed as founder with contact sam@tori.finance on the Amsterdam-datelined PR — [The Defiant PR](https://thedefiant.io/news/press-releases/tori-brings-institutional-trades-on-chain-fills-50m-before-launch)
  - LinkedIn: "Samed Düzçay - Tori Labs" — [LinkedIn](https://www.linkedin.com/in/smddzcy/)
  - Podcast and search summaries describe him as Istanbul-based, a Boğaziçi University graduate, with a prior SaaS company he built and exited — [Apple Podcasts episode](https://podcasts.apple.com/in/podcast/samed-d%C3%BCz%C3%A7ay-accessing-institutional-yield-strategies/id1438148082?i=1000766231320); GitHub [smddzcy](https://github.com/smddzcy)
- Team background per RockawayX: "comes from quantitative trading and structured products". No other names are given — [RockawayX thesis](https://www.rockawayx.com/insights/rockawayx-tori-ecosystem-vault-investment-thesis-risk-disclosure)
- Entities: Tori (BVI) Limited (the trUSD issuer, "Tori BVI"), Tori Foundation, and "Tori Labs" (LinkedIn) — [Docs: Risk](https://docs.tori.finance/legal/risk); [Docs: trUSD Terms](https://docs.tori.finance/legal/trusd-terms)
- Exchange touchpoints (not investors): pharos.watch's on-chain tracing of the minting custodian wallet found collateral flowing to **BiLira Pro and Binance deposit addresses** — [pharos.watch](https://pharos.watch/stablecoin/trusd-tori/). The homepage links regional communities "Tori 中文" and "Tori KOREA" and is localized into zh/ja/ko/vi/id/hi/pt/es — [tori.finance](https://tori.finance/)

### Inferences
- With no disclosed round size, an undisclosed valuation, and a Delphi-led seed, this is likely a small-to-mid seed, typically $3–10M for comparable 2025–26 stablecoin seeds. That range is speculation, not sourced.
- No Tier-1 exchange venture arm appears on the cap table, so there is no direct listing-venue hint from investors. The Chinese and Korean community channels and the Binance deposit flows are weak hints of Asian retail and exchange orientation. They are not evidence of a listing.

### Gaps
- Messari (HTTP 429) and CryptoRank (HTTP 403) funding pages could not be fetched, and PitchBook is paywalled. The round amount and valuation are not found anywhere public.
- No team page lists a CTO or other executives.

---

## 4. Official statements on a governance token, TGE, airdrop, or "Season" dates, and on the points (Cores) program

### Takeaway
**No token, TGE, airdrop, or Season 1 end date has been officially announced** as of 2026-09-28. The docs explicitly state: "Cores are not a promise of any token or payment". The only dated fact is that **Season 1 began June 23, 2026**. "Future seasons will define how the protocol recognizes" contributions. Several signals still point to a points-to-token path: a YT-Lock contract for "boosted Cores", "Season" language, a RockawayX "Points APY", and Pendle pricing about 9% implied APY on a trUSD YT that has zero underlying yield.

### Cited Findings (official docs, verbatim)
- Cores page: "Cores represent your contribution to Tori. As the protocol evolves, they will factor into how early supporters are recognized. **The form that takes has not been decided, and Cores are not a promise of any token or payment.**" — [Docs: Cores](https://docs.tori.finance/resources/cores)
- Also on the Cores page: "Season 1 began June 23, 2026 with the pre-deposit phase, which carried the largest boost the program plans to offer. That phase is complete: the vault has converted to the Ecosystem Vault." and "Emission rates are set per season. During Season 1's pre-deposit phase, the rate was **30 Cores per dollar per day**." and "During the pre-deposit phase, Cores earned a **2x boost, the highest planned for the program**." — [Docs: Cores](https://docs.tori.finance/resources/cores)
- General FAQ, "What will Cores be used for?": "**That has not been announced yet.** Cores record your contribution, and **future seasons** will define how the protocol recognizes it. They are not a promise of any token or payment." — [Docs: General FAQ](https://docs.tori.finance/faq/general) (sitemap lastmod 2026-09-20)
- Referral: 10% of referees' Cores, with no cap — [Docs: Referral](https://docs.tori.finance/resources/referral)
- How to earn: hold trUSD, stake strUSD, use DeFi integrations — [Docs: Cores](https://docs.tori.finance/resources/cores). App strings describe holding trUSD as "Mint 1:1. No rewards, maximum cores while you decide." — [app.tori.finance (app i18n bundle)](https://app.tori.finance/activities)
- A **YT-Lock** contract exists. It is one of the core contracts governed by the Owner/Admin Safe and the Timelock (upgrades are timelocked) — [Docs: Roles, Multisig and Timelocks](https://docs.tori.finance/security/roles). App UI strings: "Lock Pendle YT-strUSD for boosted Cores", "Lock YT-trUSD for Cores", "Lock for boosted cores multipliers", "**Once locked, YT cannot be withdrawn.**" — [app.tori.finance](https://app.tori.finance/activities)
- More app UI strings:
  - "Illustrative until Jul 27 — the final multiplier table publishes at launch. Multiplies the Cores your deployed dollars earn."
  - "Post-launch, no date committed"
  - "Cores on your YT balance" for YT-strUSD and YT-trUSD
  - "Cores on the SY portion of your LP" for Pendle LP
  - "No Cores on PT" for Morpho PT collateral
  - Source: [app.tori.finance](https://app.tori.finance/activities)
  - The current multiplier values were not retrievable without a wallet session.
- The legal docs say trUSD/strUSD confer no "governance rights" — [Docs: Risk Disclosures](https://docs.tori.finance/legal/risk). DefiLlama shows no governance token (symbol "-", gecko_id null for the protocol) — [DefiLlama API](https://api.llama.fi/protocol/tori-finance)
- RockawayX: "Predeposits will receive the highest points boost in the Tori points program". The vault's target APY splits into "Points APY 8.73%" (Phase 1) and "6.9%" (Phase 2), with no methodology given — [RockawayX thesis](https://www.rockawayx.com/insights/rockawayx-tori-ecosystem-vault-investment-thesis-risk-disclosure)
- Third-party airdrop trackers, which are not official: "Tori has not announced a token, a TGE date, or a conversion rate from Cores to any future asset… the app references them in the airdrop flow, but the allocation formula remains unannounced" — [usethebitcoin](https://usethebitcoin.com/airdrop/tori-finance/); also [airdrops.io](https://airdrops.io/tori-finance/), [CryptoRank drophunting](https://cryptorank.io/drophunting/tori-finance-activity1224)
- The Defiant launch PR (2026-07-27) and CoinGecko's sponsored piece (2026-08-20) make no mention of a token, TGE, or airdrop — [The Defiant](https://thedefiant.io/news/press-releases/tori-brings-institutional-trades-on-chain-fills-50m-before-launch); [CoinGecko Learn](https://www.coingecko.com/learn/pendle-tori-trusd-strusd-institutional-yield)
- Pendle markets, via the Pendle API at 2026-09-28 11:00 UTC. Both markets were created 2026-07-19, both expire **2026-11-26**, and both carry category tags "stables" and "points":
  - **strUSD market** ([0xac02…addb](https://api-v2.pendle.finance/core/v2/1/markets/0xac028348c46d3455899a2b9b50077c11960eaddb/data)): liquidity $7.20M, total TVL $8.88M, implied APY **11.41%**, underlying APY 11.18%, 24h volume $74.6K
  - **trUSD market** ([0xfcf0…c947](https://api-v2.pendle.finance/core/v2/1/markets/0xfcf009cb3135da12a6eb1f73f3ee05392a7bc947/data)): liquidity $2.57M, total TVL $5.56M, implied APY **9.01%**, **underlying APY 0**, ytFloatingApy −100%
  - Source: [Pendle active markets API](https://api-v2.pendle.finance/core/v1/1/markets/active)
  - On 2026-08-20 CoinGecko reported PT-strUSD at 11.56%, PT-trUSD at about 9.51%, YT leverage about 33x, and combined TVL about $19M — [CoinGecko Learn](https://www.coingecko.com/learn/pendle-tori-trusd-strusd-institutional-yield)

### Inferences
- There is no dated catalyst. Season 1 has no end date, and the pre-deposit boost ("highest planned") is over, so Cores accrual per dollar is now lower than in June and July. A reasonable guess is that Season 1 runs at least until the Pendle 26-Nov-2026 maturity, since the YT-Lock product and the Pendle markets are built around that date. **This is speculation.**
- YT-trUSD has zero underlying yield yet trades at about 9% implied, and RockawayX modeled about 7–9% "Points APY". Both show that the market and Tori's own curator assign meaningful value to Cores despite the "not a promise of any token" disclaimer.
- The docs repeat "not a promise of any token or payment" in several places. That is standard legal hedging, and it also means holders have no enforceable claim if a token never launches or Cores convert on unfavourable terms.

### Gaps
- I did not read any official X/Discord statement giving TGE timing, a Season 1 end date, or a Cores-to-token ratio. X was not directly readable. The community and social researcher's file (`tori_community_social.md` in the same folder) may cover X posts.
- Total Cores issued and the current multiplier table (the app needs a wallet session) are unknown.

---

## 5. Partners, integrations, audits, chains, and roadmap

### Takeaway
Tori launched with a large institutional-looking stack:
- **Audits**: Sherlock and Nethermind
- **Monitoring**: Hypernative
- **Proof of reserves**: Accountable (real-time)
- **Pre-deposit cover**: Nexus Mutual
- **Vault curation**: RockawayX via Upshift
- **Institutional custody**: Anchorage, BitGo and Cactus
- **Cross-chain**: Chainlink CCIP, with Monad and Pharos live

DeFi use is concentrated in Morpho, Pendle, Curve and Fluid on Ethereum, plus Morpho on Monad.

### Cited Findings
- **Audits**:
  - Sherlock collaborative audit, January 15–22, 2026 (report dated 2026-02-10) — [PDF](https://github.com/sherlock-protocol/sherlock-reports/blob/main/audits/2026.02.10%20-%20Final%20-%20Tori%20Finance%20Collaborative%20Audit%20Report%201770734349.pdf)
  - Nethermind security review, March 24–26, 2026 — [PDF](https://github.com/NethermindEth/PublicAuditReports/blob/main/NM_0854_Tori.pdf)
  - "Every finding… either fixed in code or formally acknowledged"
  - Bug bounty: up to **$1,000,000** for critical, $10K–50K for high
  - Source: [Docs: Audits](https://docs.tori.finance/security/audits)
- **Security stack**: Hypernative monitoring; Accountable continuous PoR at [tori.accountable.capital](https://tori.accountable.capital); keys held in Safes, MPC vaults and a 24-hour timelock — [Docs: Security Overview](https://docs.tori.finance/security/overview). Nexus Mutual cover for the pre-deposit vault (smart contract and oracle risk) — [Docs: Pre-Deposit](https://docs.tori.finance/resources/pre-deposit); [Nexus product 446](https://app.nexusmutual.io/cover/product/446)
- **Ecosystem Vault**: RockawayX curates it on Upshift (LP token etrUSD). After pre-deposit it has a soft lock and a 7-day withdrawal period — [Docs: Integrations](https://docs.tori.finance/resources/integrations). Vault fees: performance "0% at launch; 10% from Phase 2", management ramping to 0.3%. Vault governance is a "4-of-6 multisig (RockawayX, Tori, Upshift), 24h timelock". Phase 2 indicative allocation: strUSD-trUSD Curve LP 32.5%, trUSD-USDC Curve LP 27.5%, strUSD Pendle LP 20%, trUSD Pendle LP 20% — [RockawayX thesis](https://www.rockawayx.com/insights/rockawayx-tori-ecosystem-vault-investment-thesis-risk-disclosure)
- **Institutional custody support for holding trUSD/strUSD**: Anchorage Digital Bank N.A., BitGo Bank & Trust N.A., and Cactus Custody (Matrix Trust Company, HK; part of BIT, formerly Matrixport) — [Docs: Institutional Custody](https://docs.tori.finance/resources/institutional-custody)
- **Day-one integrations** at strUSD launch on July 27: Pendle, Morpho, Curve, Royco. "PT-trUSD can already be used as collateral on Morpho" — [CoinGecko Learn](https://www.coingecko.com/learn/pendle-tori-trusd-strusd-institutional-yield). The launch PR mentions Morpho, Pendle and Curve — [The Defiant](https://thedefiant.io/news/press-releases/tori-brings-institutional-trades-on-chain-fills-50m-before-launch)
- **Live DeFi pools** per DefiLlama yields on 2026-09-28 — [DefiLlama yields](https://yields.llama.fi/pools):

  | Pool | TVL | APY / note |
  |---|---|---|
  | Morpho strUSD market (Ethereum) | $15.96M | — |
  | Morpho "ROXTORI" USDC vault (RockawayX Tori vault) | $13.51M | 6.16% |
  | Morpho strUSD on **Monad** | $6.31M | 1.5% reward APY |
  | Fluid DEX USDC-trUSD | $5.48M | — |
  | Morpho sbaUSD-TORI-MON (Monad) | $5.48M | — |
  | Morpho etrUSD market | $4.21M | — |
  | Curve strUSD-trUSD | $4.08M | — |
  | Curve frxUSD-trUSD | $3.06M | — |
  | Morpho PT-trUSD-26NOV2026 | $2.73M | — |
  | Morpho PT-strUSD-26NOV2026 | $0.82M | — |
  | Pendle strUSD | $7.20M liquidity | — |
  | Pendle trUSD | $2.57M liquidity | — |

- **App catalog strings** (UI, including demo/"est. at launch" entries, so **not all are confirmed live**) — [app.tori.finance](https://app.tori.finance/activities):
  - Euler strUSD and PT-strUSD collateral
  - Gearbox LP loop
  - Convex and Stake DAO Curve-LP staking
  - IPOR Fusion
  - Kamino lend/multiply strUSD
  - Keyrock-curated strUSD strategy
  - Morpho vaults by kpk (USDT), Steakhouse (USDC) and RockawayX (USDC)
  - Royco senior/junior tranches
  - ROWA managed vault
  - Concrete vault
  - Strata pre-deposit
  - Term Finance and TermMax fixed-rate
  - Curvance on Monad
  - strUSD entries on Base, BNB Chain, Solana, Stellar, Ink and Pharos
- **Chains**:
  - Ethereum is the hub. trUSD and strUSD bridge natively via **Chainlink CCIP (CCT standard)**, using Lock & Release on Ethereum and Burn & Mint elsewhere. "Monad and Pharos are live" (Monad chain ID 143, Pharos chain ID 1672).
  - Lane limit: 1.5M tokens per lane, refilled over 6 hours.
  - Source: [Docs: Contracts](https://docs.tori.finance/resources/contracts)
  - DefiLlama first shows trUSD on Monad from 2026-09-16 and on Pharos from 2026-09-26 — [DefiLlama stablecoin API](https://stablecoins.llama.fi/stablecoin/401)
  - On testnet, pharos.watch reported Sepolia and Base Sepolia with LayerZero OFT around 2026-05-31 — [pharos.watch](https://pharos.watch/stablecoin/trusd-tori/)
- **Governance change**: a new Timelock (0xA952…6ef4) "replaced the original timelock (0x7af35ab3…) on 15 September 2026" — [Docs: Contracts](https://docs.tori.finance/resources/contracts)
- **Timeline**:
  - 2026-01-15/22: Sherlock audit
  - 2026-03-24: trUSD/strUSD announced on X, with "contracts not yet deployed as of early April" ([pharos.watch timeline](https://pharos.watch/stablecoin/trusd-tori/))
  - 2026-03-24/25: Delphi seed
  - 2026-03-24/26: Nethermind review
  - 2026-06-23: pre-deposit and Cores Season 1 start
  - 2026-06-24: mainnet contracts live
  - About 2026-06-30/07-02: $50M cap reached
  - 2026-07-19: Pendle markets created
  - 2026-07-27: public launch, PR and integrations
  - 2026-09-15: timelock migration
  - Mid/late September 2026: Monad and Pharos lanes
  - Sources: [Docs](https://docs.tori.finance/resources/cores); [Pendle API](https://api-v2.pendle.finance/core/v1/1/markets/active); [DefiLlama](https://api.llama.fi/protocol/tori-finance)
- **Roadmap items stated officially**: strategy set "can expand as conditions change"; more chains ("the list grows as new chains are added"); "future seasons" of Cores; publication of attested MPC thresholds ("which we intend to publish alongside our proof-of-reserves data") — [Docs: Strategy](https://docs.tori.finance/strategy/overview); [Docs: trUSD FAQ](https://docs.tori.finance/faq/trusd); [Docs: Roles](https://docs.tori.finance/security/roles)

### Inferences
- The app catalog is broad, but actual liquidity is concentrated in Morpho (≈$25M+ across markets and vaults, including the RockawayX vault), Pendle (≈$14M TVL), Curve (≈$7M) and Fluid (≈$5.5M). Much of this is looped or recursive use of the same trUSD base, so DeFi TVL figures overlap with the $73–75M supply.
- The multi-chain push (Monad, Pharos, and catalog entries for Base, BNB Chain and Solana) and the new Timelock in mid-September suggest that preparation for a growth phase or next season is under way. There is no official roadmap document with dates.

### Gaps
- There is no public roadmap with quarter targets.
- Live status for the Base, BNB Chain, Solana, Stellar and Ink entries is unconfirmed; the docs list only Monad and Pharos as live.

---

## 6. Key risks: depeg history, centralization, custody, strategy, audits, incidents

### Takeaway
The peg has held tightly: daily DefiLlama prices ranged $0.99909–$1.00042 from July 27 to September 26, with no known incidents. The main risks are **CeFi/counterparty and opacity**:
- About 100% of reserves are off-chain with unnamed banks.
- pharos.watch traced collateral flows to exchanges and to BiLira Pro.
- EM money-market and FX-hedge risk.
- Permissioned mint/redeem priced by the backend.
- An uncapped `reportLoss()` path on strUSD.
- Upgradeable contracts and a blacklist.
- A track record under 4 months on mainnet.
- A concentrated, points-driven TVL.

pharos.watch rates trUSD **C- (54/100)**.

### Cited Findings
- **Peg history**: DefiLlama daily price for trUSD from 2026-07-27 to 2026-09-26 had a minimum of **$0.99909 (2026-09-17)** and a maximum of $1.00042 (2026-07-27). No day deviated by more than 0.2% — [DefiLlama coins chart API](https://coins.llama.fi/chart/ethereum:0xd0580192e98ea6ceb9c7b6191ed2e27560911697?start=1782345600&span=95&period=1d). pharos.watch: "a peg that has held at par since launch" — [pharos.watch](https://pharos.watch/stablecoin/trusd-tori/)
- **Rating**: "trUSD holds a C- Safety Score grade (54/100)… Pharos does not consider it clearly safe". Its classification is "CeFi-Dependent · Crypto-Collateralized", minting "Permissioned", freeze "Yes" (summary facts as of 2026-09-07) — [pharos.watch](https://pharos.watch/stablecoin/trusd-tori/)
- **Custody opacity and conflict**:
  - pharos.watch: "Tori's Accountable dashboard attributes ~90% of backing to unnamed 'regulated custodian banks' and ~10% to 'regulated investment banks', with names withheld for operational security. Independent on-chain tracing of the sole minting custodian wallet shows collateral flowing to BiLira Pro and Binance deposit addresses and a large USDT balance in an unlabeled externally owned account" — [pharos.watch](https://pharos.watch/stablecoin/trusd-tori/)
  - The Tori homepage, by contrast, says off-chain collateral "is held with BitGo, Anchorage Digital and Cactus Custody" — [tori.finance](https://tori.finance/)
  - The solvency feed shows on-chain custody at 0% — [solvency API](https://app.tori.finance/api/solvency)
- **Mint/redeem controls**: "primary NAV mint and redeem are KYC-whitelisted in the contract itself… Mint and redemption quotes are also set by Tori's own backend with no on-chain price feed" — [pharos.watch](https://pharos.watch/stablecoin/trusd-tori/). The docs confirm "Mint and redeem are whitelist-gated at the contract". Minter and Redeemer are **3 EOAs each**, bounded by user-signed EIP-712 orders and per-block limits — [Docs: Roles](https://docs.tori.finance/security/roles)
- **Loss path on strUSD**: the Rewarder role (a Safe plus the Distributor contract) can call `transferInRewards` and `reportLoss` — [Docs: Roles](https://docs.tori.finance/security/roles). pharos.watch: `reportLoss()` burns trUSD in the vault "without a proportional cap or timelock", which lowers the strUSD exchange rate — [pharos.watch](https://pharos.watch/stablecoin/trusd-tori/). Docs: "Can rewards go negative? They can… reported on-chain through the same distribution path" — [Docs: General FAQ](https://docs.tori.finance/faq/general)
- **Admin powers**:
  - trUSD and strUSD are upgradeable proxies. Upgrades, new collateral, new custodian addresses, and raising the stablecoin delta limit go through a **24h timelock**.
  - Owner/Admin is a 3-of-5 Safe. Gatekeeper, Whitelister, Collateral Manager, Executor and Canceller are MPC vaults (2-of-4 per the solvency feed); Reward Operator is 3-of-4 MPC.
  - strUSD has a Blacklist Manager.
  - "MPC thresholds are held in the custody provider's policy engine rather than on-chain."
  - Sources: [Docs: Roles](https://docs.tori.finance/security/roles); [solvency API controlAddresses](https://app.tori.finance/api/solvency)
- **Strategy risks (RockawayX's list)**: strategy yield, custody/counterparty, smart contracts (Tori, Upshift and the DeFi layers), oracle/valuation, peg/liquidity, **FX hedge and rollover**, phase transition, and regulatory — [RockawayX thesis](https://www.rockawayx.com/insights/rockawayx-tori-ecosystem-vault-investment-thesis-risk-disclosure). Docs risk text includes "Currency and Cross-Market Exposure" and "Adverse movements in interest rates, exchange rates" — [Docs: General Risk Disclosures](https://docs.tori.finance/legal/risk)
- **Holder legal position**: "Tori BVI becomes the owner of all assets you transfer… You have no continuing claim, interest, or right in the transferred assets." — [Docs: trUSD Protocol User Agreement](https://docs.tori.finance/legal/trusd-protocol). Neither token is insured (no FDIC or private policy) — [Docs: General FAQ](https://docs.tori.finance/faq/general)
- **Liquidity and exit**: the 7-day strUSD cooldown exists because "Redemptions are met by unwinding backing positions" — [Docs: strUSD](https://docs.tori.finance/products/strusd). On-chain (my query), 10.77M trUSD was sitting in the unstaking Silo on 2026-09-28, up from about 15K on 2026-09-21 — [Silo](https://etherscan.io/address/0xF7c0d8853E69DCD37ee7599c6280d2632F3360B4)
- **Track record**: "track record is still under six months" as of 2026-09-07. Mainnet has been live since 2026-06-24 — [pharos.watch](https://pharos.watch/stablecoin/trusd-tori/)
- **Incidents**: I found no reported exploit, depeg, pause, or loss report (no `reportLoss` event was surfaced in any source) in the sources reviewed. The strUSD exchange rate has risen monotonically at every sampled date (see §1) — [strUSD contract](https://etherscan.io/address/0x280839980a7eD0D7717F64125fE241012E5F5815)

### Inferences
- The tail risks behind the peg sit off-chain: counterparty or custodian failure, EM FX convertibility or hedge failure, and fraud or mismarking. Smart-contract risk matters less. Accountable's attestation depends on API feeds from an asset manager, CEX and payment rail (verification level 4 of 6 for those sources in the feed), not on on-chain proof of the bank holdings.
- The TVL is points-motivated and concentrated: a RockawayX vault started it, and much of it is looped through Morpho and Pendle. That creates reflexive exit risk once a TGE happens or Cores incentives fall, and the 7-day cooldown plus KYC-only redemption could push secondary trUSD/strUSD below NAV during a rush.
- The Silo jump (about 14% of supply) right before the reporting date needs watching. If it is redeemed rather than restaked, it will test the redemption and unwind process in the week of 2026-09-29.

### Gaps
- No independent confirmation of which banks and brokers hold the 90.5% "custodian bank" bucket.
- The reserve fund size could not be verified.
- I did not see a pharos.watch full-note PDF or the auditors' finding counts and severities (I did not open the audit PDFs).
- An hourly or intraday peg record was not obtained; CoinGecko was rate-limited.
