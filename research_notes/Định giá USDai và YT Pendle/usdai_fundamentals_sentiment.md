# USD.AI (USDai / sUSDai / CHIP): fundamentals, traction, team, token and sentiment, as of 2026-09-28

Research date: 2026-09-28. All figures carry a date. Items marked **[STALE]** are more than about 3 months old. Items marked **[UNVERIFIED]** come from a single, secondary or aggregator source. On-chain and API pulls were made by the researcher on 2026-09-28 (DefiLlama API, DefiLlama coins/stablecoins API, and an Arbitrum RPC `eth_call`).

**Headline correction to the brief:** the governance token **is already live**. The ticker is **CHIP**. The ICO ran on CoinList on Feb 22–27, 2026 at $0.03 per token ($300M FDV). TGE and exchange listings happened on **April 21–22, 2026**, slipping from the originally guided "late Q1 / March 2026". Season 2 ("Flatiron"), whose rewards are paid in CHIP airdrops, runs **until 2026-10-14**. That date is also the maturity of the October Pendle YT and the settlement date for "protected CHIP".

---

## 1. What USD.AI is and how USDai / sUSDai work

### Takeaway
USD.AI is a credit protocol built by Permian Labs and run by the USD.AI Foundation/DAO. It makes non-recourse, roughly 3-year amortizing loans in stablecoins to GPU/"neocloud" operators, secured by the GPUs themselves (max 80% LTV, insured by Barker). There are two tokens:
- **USDai** is a dollar token, today backed ~100% by PayPal's PYUSD (M0 in the genesis phase). It pays no yield.
- **sUSDai** is the ERC-4626-style staked version. It collects the loan interest plus reserve yield and is redeemed through 30-day epochs.

The protocol is on Arbitrum (home chain), Ethereum and Plasma. It expanded to Arc and Solana in September 2026.

### Cited Findings
**Mechanism and tokens**
- USD.AI is a yield-bearing synthetic dollar protocol; users deposit USDai into vaults, receive sUSDai, and earn the base Treasury rate (~4–5%) plus interest from loans to AI infrastructure operators — [Pine Analytics](https://pineanalytics.substack.com/p/the-bear-case-for-chip) / [ICO Drops summary](https://icodrops.com/usd-ai/) (Jan 2026) **[STALE on yield figures]**
- In the genesis phase, USDai reserves were "U.S. Treasury Bills" held through an M0 integration. The design moves through a "Sprawl" phase into a mature state "predominantly composed of hardware-backed loans". — [Stablewatch deep dive, 2025-10-23](https://www.stablewatch.io/research/usd-ai-deep-dive) **[STALE]**; [M0 Research](https://research.m0.org/research/usdai-uses-m0s-stablecoin-platform-to-launch-composable-synthetic-dollar)
- Current reserve: DefiLlama's protocol adapter shows the Arbitrum TVL held **100% in PYUSD** ($218.6M PYUSD on 2026-09-28). — [DefiLlama API /protocol/usd-ai](https://api.llama.fi/protocol/usd-ai) (pulled 2026-09-28). USD.AI announced a "PYUSD Integration and Incentive Program" ("$1 Billion Customer Incentive Program" with PayPal). — [USD.AI Insights index](https://usd.ai/insights)
- Roadmap item: migrate the collateral backing from PYUSD to PayPal's **PYUSDx** in Q4 2026. On 2026-09-11 USD.AI was named an expected issuer on PayPal's PYUSDx custom-stablecoin platform. — [CoinMarketCap AI updates](https://coinmarketcap.com/cmc-ai/usd-ai/latest-updates/) **[UNVERIFIED — aggregator]**
- Loans are "non-recourse ... secured solely by computing hardware" purchased with the financing. — [CoinDesk, 2025-08-13](https://www.coindesk.com/business/2025/08/13/usd-ai-raises-usd13m-to-expand-gpu-backed-stablecoin-lending) **[STALE]**
- The loans run **three years and amortize monthly**, while capital can enter and exit sUSDai on a much shorter cycle. That structural duration mismatch is why USD.AI took a $40M revolving facility collateralized by sUSDai. — [PR Newswire, K3 Capital, 2026-09-15](http://www.prnewswire.com/news-releases/usdai-secures-40m-stablecoin-based-revolving-debt-facility-from-k3-capital-302879442.html)

**CALIBER / collateral**
- CALIBER is a "standardized legal and technical framework for tokenizing physical assets" built on UCC Article 7 bailment/warehouse receipts. Its NFT-based ownership claims are called **GPU Warehouse Receipt Tokens (GWRTs)**. Hardware must sit in an "insurable, top-tier data center". — [Stablewatch, 2025-10-23](https://www.stablewatch.io/research/usd-ai-deep-dive); [USD.AI "GWRTs" and "CALIBER Deep Dive" posts](https://usd.ai/insights)
- **Wilmington Trust** acts as escrow agent, so yield starts "at loan signing, not server installation". Escrowed loans can earn a lower rate: the Texas B200 loan paid 7% in escrow versus 11.5% after deployment (July 2026). — [USD.AI Insights index](https://usd.ai/insights); [USD.AI July 2026 recap](https://usd.ai/insights/usdai-july-recap-81m-deployed-loans)

**Loss absorption and insurance**
- **Loss absorption changed on 2026-02-06.** USD.AI dropped "FiLo" (First-Loss, a junior tranche posted by curators) for new loans and moved to **Barker** insurance. Barker "warrants 80% of independently assessed collateral value", which matches the protocol's **max 80% LTV**. It is backed by an unnamed "A-rated institutional reinsurer". The first loan under this structure went to QumulusAI. — [USD.AI, "Upgrading to a Fully Insured sUSDai"](https://usd.ai/insights/upgrading-fully-insured-susdai)
- The insurance/reinsurance layer costs about **150 bps per year**. — [Stablewatch](https://www.stablewatch.io/research/usd-ai-deep-dive) **[STALE, pre-Barker wording]**; [search summary citing Barkr 150 bps](https://www.stablewatch.io/research/usd-ai-deep-dive)
- **sCHIP backstop:** staked CHIP (sCHIP) can be used to cover shortfalls ("loan losses exceeding reserves"). Unstaking has a cooldown set by governance. — [docs.usd.ai/governance/chip](https://docs.usd.ai/governance/chip); [USD.AI Foundation announcement, 2026-01-27](https://usd.ai/insights/usdai-foundation-chip)

**Redemption**
- sUSDai redemptions go into a **FIFO queue processed on fixed dates every 30 days**. The wait depends on when you submit relative to the next window. During high utilization, queues "may extend across multiple epochs". — [docs.usd.ai sUSDai / FAQ](https://docs.usd.ai/faq/usdai-and-susdai-101); [docs.usd.ai/depositor/susdai](https://docs.usd.ai/depositor/susdai)
- **QEV (Queue Extractable Value)** is planned: an auction in which exiting holders bid a fee to jump the redemption queue. Natural liquidity from loan amortization is about **3–4% of outstanding principal per month**. — [Stablewatch](https://www.stablewatch.io/research/usd-ai-deep-dive); [USD.AI QEV post](https://usd.ai/insights)
- sUSDai uses two prices: a "redemption share price" and a "deposit share price". The deposit price prorates expected loan repayments so depositors cannot time entry around known NAV jumps. — [docs.usd.ai sUSDai withdrawal estimates](https://docs.usd.ai/depositor/susdai/susdai-withdrawal-estimates)
- There is also **secondary-market exit liquidity**: a $100M Fluid liquidity facility for sUSDai (June 2026), Curve pools (the sUSDai/USDC pool on Arbitrum held about $1.49M of liquidity, date unclear), and planned sUSDai trading pairs on Bullish Exchange. — [USD.AI Insights](https://usd.ai/insights); [GeckoTerminal](https://www.geckoterminal.com/arbitrum/pools/0xa7cf5543a27badc3a74d51ea0a02e84799140e4e); [CoinDesk, 2026-08-28](https://www.coindesk.com/business/2026/08/28/bullish-backs-usd-ai-with-usd100-million-gpu-stablecoin-financing)

**Yield**
- sUSDai net APY was **7.20%** at end-August 2026. — [USD.AI August 2026 recap](https://usd.ai/insights/august-recap-100m-facility-susdai-ath)
- July 2026: **8.61% gross / 7.46% net**. — [USD.AI July recap](https://usd.ai/insights/usdai-july-recap-81m-deployed-loans)
- 2026 YTD average yield was 7.0%. The protocol projects **12.4%** at full deployment. — [USD.AI Lighthouse 2026 YTD report](https://usd.ai/insights/usdai-2026-ytd-report-lighthouse) (mid-2026)
- Individual loan coupons, per the Jul–Aug 2026 recaps:
  - QumulusAI $15.3M, NVIDIA B300: **15% fixed**
  - Corvex $7.5M, B200: **10% fixed**
  - Hydra Host $54.4M: **10%**
  - Texas B200: 11.5% after deployment
  - Sources: [Aug recap](https://usd.ai/insights/august-recap-100m-facility-susdai-ath); [July recap](https://usd.ai/insights/usdai-july-recap-81m-deployed-loans)
- The on-chain sUSDai share price, `convertToAssets(1e18)` on Arbitrum, was **1.11532 USDai** on 2026-09-28 (block 509,697,543). — Arbitrum RPC call by researcher on contract 0x0B2b2B2076d95dda7817e785989fE353fe955ef9
- DefiLlama coins API prices for sUSDai: 1.07329 (2026-03-27), 1.08633 (2026-05-26), 1.10724 (2026-08-24), 1.11393 (2026-09-23), 1.11546 (2026-09-28). — [DefiLlama coins API](https://coins.llama.fi/prices/current/coingecko:susdai)
- A Jupiter Earn promotion says sUSDai loops can reach "up to 35% APY". That is a leveraged, incentive-subsidized figure, not the base yield. — [Solana Compass, 2026-09-24](https://solanacompass.com/news/usdais-gpu-backed-usdai-and-susdai-go-live-on-solana-with-kamino-and-jupiter-markets)

**Chains**
- DefiLlama lists USDai on **Arbitrum, Plasma, Ethereum**. — [DefiLlama stablecoins API id 309](https://stablecoins.llama.fi/stablecoin/309)
- **Solana** went live on 2026-09-24: an isolated Kamino sUSDai market curated by Allez Labs (80% max LTV, liquidation at 85%) and three Jupiter Lend sUSDai vaults. — [Solana Compass](https://solanacompass.com/news/usdais-gpu-backed-usdai-and-susdai-go-live-on-solana-with-kamino-and-jupiter-markets); [The Defiant](https://thedefiant.io/news/defi/kamino-opens-gpu-loan-linked-susdai-collateral-market-on-solana)
- **Arc** (Circle's chain): USD.AI was a "Day 1 launch partner, with Bitwise leading liquidity curation on Morpho" (September 2026). — [USD.AI Insights index](https://usd.ai/insights)
- The CHIP contract is 0x0C1c1C109FE34733fca54b82d7B46B75CFb71F6e on Ethereum and Arbitrum. — [Binance announcement](https://www.binance.com/en/support/announcement/detail/c8d2380a71ee4b56980cf7798d2e3d8f)

**DeFi integrations**
- Aave ARFC passed on 2026-07-24 to onboard USDai/sUSDai to Aave V3 Arbitrum.
- PT-USDai markets launched on Morpho on 2026-07-01.
- Pendle YT lock vaults exist.
- Flatiron lists Curve, Gamma, Aerodrome, Balancer, Fluid, Maverick, Euler, Silo, Morpho and Gearbox integrations.
- Sources: [July recap](https://usd.ai/insights/usdai-july-recap-81m-deployed-loans); [CHIP is live](https://usd.ai/insights/chip-is-live)

**Audits and oracle**
- DefiLlama lists 2 audits ([docs.usd.ai audits](https://docs.usd.ai/technical-overview/audits)), including a Cantina audit of the USDai stablecoin ([Cantina](https://cantina.xyz/portfolio/23dbab18-bbea-4184-8eb5-584faaf80903)).
- Chainlink is the official oracle ([USD.AI Insights](https://usd.ai/insights)).
- Independent "Proof of Loans" attestation by **The Network Firm LLP**, published 2026-09-01 with an as-of date of 2026-07-15. It covers NVIDIA H200, B200, B300 and RTX PRO 6000 systems in the US, Canada and Sweden. — [USD.AI Proof of Loans](https://usd.ai/insights/proof-of-loans-independent-attestation-report)

### Inferences
- In practice sUSDai is a senior claim on a pool of about 3-year, 10–15% fixed-rate GPU loans, plus PYUSD liquidity. Net yield of about 7–7.5% today means a large share of the pool still sits in low-yield PYUSD or in escrow at a lower rate. Yield should rise toward the 12.4% target only as loans actually deploy.
- The 30-day epoch queue, 3-year loans and new sUSDai-collateralized credit lines (K3, Bullish) show the protocol is actively managing a duration/liquidity mismatch, not eliminating it.

### Gaps
- There is no public figure for current queue length or wait time. The docs page gives mechanics only.
- The Barker reinsurer's name and the exact current premium are not disclosed.
- Terms, status and date of the PYUSD reserve yield arrangement (whether PYUSD reserves earn yield for the protocol, and how much) were not found.
- QEV had not been confirmed live as of the latest docs read.

---

## 2. Metrics: TVL, supply, loan book, revenue, trend 2025–2026, incidents

### Takeaway
DefiLlama "TVL" only counts idle PYUSD. **Idle $218.6M plus loans outstanding ("borrowed") of $401.4M makes the total about $620M on 2026-09-28.**
- USDai supply peaked at **$663.2M on 2026-01-20**, during Season 1 farming. It fell about 76% to $158.7M by 2026-08-01, partly through outflows after the airdrop/TGE and partly because PYUSD was converted into loans.
- The loan book grew from about $1M (Jan 2026) to **$401M (Sep 28, 2026)**. The $128.9M GB200 loan booked on 2026-09-24 is the single largest.
- Fees are about **$1.7M per 30 days**.
- There are no reported defaults. USDai has had only minor peg deviations in 2026, with the lowest at $0.984.

### Cited Findings
**DefiLlama protocol TVL (idle reserves) vs "borrowed" (loans outstanding), $M** — [DefiLlama API](https://api.llama.fi/protocol/usd-ai), pulled 2026-09-28:

| Date | Idle TVL | Borrowed (loans) | Sum |
|---|---|---|---|
| 2025-07-01 | 29.5 | 0 | 29.5 |
| 2025-09-01 | 110.2 | 1.3 | 111.5 |
| 2025-10-01 | 505.0 | 1.2 | 506 |
| 2025-11-22 (ATH) | 702.0 | ~0.6 | ~703 |
| 2026-01-01 | 684.4 | 1.1 | 685.4 |
| 2026-03-01 | 467.0 | 7.8 | 474.8 |
| 2026-04-01 | 310.9 | 17.8 | 328.7 |
| 2026-05-01 | 249.8 | 105.9 | 355.7 |
| 2026-07-01 | 196.3 | 115.5 | 311.8 |
| 2026-08-01 | 159.6 | 236.1 | 395.8 |
| 2026-09-01 | 228.1 | 264.1 | 492.2 |
| 2026-09-23 | 329.7 | 272.5 | 602.2 |
| 2026-09-24 | 207.0 | 401.3 | 608.4 (the $128.9M loan funded) |
| 2026-09-28 | 218.6 | 401.4 | 620.0 |

**Supply**
- DefiLlama hallmarks: deposit caps raised to $250M (2025-09-12) and to $500M (2025-09-26). — [DefiLlama API](https://api.llama.fi/protocol/usd-ai)
- Season 2 (Flatiron, from April 2026) says "Deposit caps are removed". — [Level Up guide](https://usd.ai/insights/allo-game-to-flatiron-level-up-guide)
- USDai circulating supply (DefiLlama stablecoins): 503.4M (2025-10-01), 653.5M (2026-01-01), **peak 663.2M (2026-01-20)**, 460.5M (2026-03-01), 308.7M (2026-04-01), 247.5M (2026-05-01), 192.8M (2026-07-01), 158.7M (2026-08-01), 227.7M (2026-09-01), 328.6M (2026-09-23), **216.7M (2026-09-28)**. — [DefiLlama stablecoin 309](https://stablecoins.llama.fi/stablecoin/309)
- On-chain Arbitrum `totalSupply` on 2026-09-28: USDai **217.61M**; sUSDai **316.82M shares**, about $353M at 1.1153. sUSDai `totalAssets()` returned **513.0M**. This does not reconcile with shares × price, and the researcher could not resolve it; it may include loan NAV accounting. — Arbitrum RPC (researcher)
- The project reports sUSDai supply "$400+ million (93% growth since March)" at end-August 2026 ([Aug recap](https://usd.ai/insights/august-recap-100m-facility-susdai-ath)) and an sUSDai ATH of $349.5M on 2026-08-04 ([July recap](https://usd.ai/insights/usdai-july-recap-81m-deployed-loans)). These numbers conflict with each other and with the on-chain ~$353M. Treat them with caution.

**Project-reported TVL (idle plus loans)**
- $398M TVL and $202M deployed in the June 2026 Lighthouse report. — [Lighthouse YTD](https://usd.ai/insights/usdai-2026-ytd-report-lighthouse)
- $436.8M (early August 2026). — [July recap](https://usd.ai/insights/usdai-july-recap-81m-deployed-loans)
- **$492.1M at end-August 2026**. — [Aug recap](https://usd.ai/insights/august-recap-100m-facility-susdai-ath)
- CoinDesk reported more than $225M locked (idle) on 2026-08-28. — [CoinDesk](https://www.coindesk.com/business/2026/08/28/bullish-backs-usd-ai-with-usd100-million-gpu-stablecoin-financing)
- Jupiter called sUSDai "the $600M+ yield-bearing dollar" on 2026-09-24. — [Solana Compass](https://solanacompass.com/news/usdais-gpu-backed-usdai-and-susdai-go-live-on-solana-with-kamino-and-jupiter-markets)

**Loan book**
- At end-August 2026: **lifetime deployed capital $281.8M**; **16 financings across 13 borrowers**; 4 publicly listed neoclouds in the portfolio; 1 early repayment; cumulative yield generated $22.4M; August deployments $22.8M. — [Aug recap](https://usd.ai/insights/august-recap-100m-facility-susdai-ath)
- June 2026 (Lighthouse): 13 active loans, average size $15.8M, total collateral $283M, $205M deployed YTD. Pipeline: 394 leads reviewed, $13.0B pipeline, **26 term sheets signed worth $817M**. — [Lighthouse YTD](https://usd.ai/insights/usdai-2026-ytd-report-lighthouse)
- Earlier claims: "$225 million in loans with over $1.2 billion in approved facilities" at TGE in April 2026 ([CHIP is live](https://usd.ai/insights/chip-is-live)). In January 2026: "$1.5B+ loan pipeline" and "$100M GPU-backed loans expected Q1 2026" ([Foundation post](https://usd.ai/insights/usdai-foundation-chip)). **[STALE]**
- The Jan-2026 figures show a gap between the headline pipeline and actual deployment. Pine Analytics (2026-01-28) reported TVL of $656M with about $70M of loans (~10% utilization) and "~99% in U.S. Treasuries". — [Pine Analytics](https://pineanalytics.substack.com/p/the-bear-case-for-chip) **[STALE, but useful as baseline]**

**Named loans and facilities**

| Date | Borrower / counterparty | Size | Collateral / terms | Source |
|---|---|---|---|---|
| 2025–26 | QumulusAI (Nasdaq: QMLS) | Up to $500M facility; draws incl. $15.3M on 2026-07-13 | $15.3M draw on B300 at 15% | [Insights](https://usd.ai/insights); [July recap](https://usd.ai/insights/usdai-july-recap-81m-deployed-loans) |
| 2025–26 | Sharon AI | Up to $500M | — | [Insights](https://usd.ai/insights) |
| 2025–26 | Quantum Solutions (Japan) | $200M guidance facility | — | [Insights](https://usd.ai/insights) |
| H1 2026 | Crucible Capital | $26.8M | 576 NVIDIA B300, Washington State | [Insights](https://usd.ai/insights) |
| H1 2026 | NexGen Cloud | $34M | B200, Sweden | [Insights](https://usd.ai/insights) |
| June 2026 | Duos Edge AI | $98.1M, 3-year | 2,304 NVIDIA B300 | [Lighthouse](https://usd.ai/insights/usdai-2026-ytd-report-lighthouse); [PR, 2026-09-23](https://www.prnewswire.com/news-releases/usdai-announces-128-9m-gpu-financing-facility-its-largest-to-date-302888224.html) |
| 2026-07-20 | Hydra Host | $54.4M at 10% | 1,040 B300 | [July recap](https://usd.ai/insights/usdai-july-recap-81m-deployed-loans) |
| July 2026 | Texas B200 | $11.3M | 256 GPUs | [July recap](https://usd.ai/insights/usdai-july-recap-81m-deployed-loans) |
| Aug 2026 | Corvex | $7.5M at 10% | B200 | [Aug recap](https://usd.ai/insights/august-recap-100m-facility-susdai-ath) |
| 2026-09-23 | Undisclosed "publicly-listed GPU cloud provider" | **$128.9M, the largest to date** | 32 NVIDIA GB200 NVL72, British Columbia; multi-year contract with a "blue-chip investment-grade counterparty"; tenor and rate undisclosed | [PR Newswire](https://www.prnewswire.com/news-releases/usdai-announces-128-9m-gpu-financing-facility-its-largest-to-date-302888224.html) |

**Liquidity and funding facilities**
- $100M Fluid liquidity facility for sUSDai DEX liquidity (June 2026). — [Insights](https://usd.ai/insights)
- BSQ Capital Partners JV (2026-06-30): $300M APAC GPU financing, upsizable to $1B on milestones, senior secured term loans. — [PR Newswire](https://www.prnewswire.com/news-releases/usdai-and-bsq-capital-partners-form-joint-venture-to-finance-300m-of-ai-compute-across-asia-pacific-302813765.html)
- **Bullish $100M stablecoin debt facility** (2026-08-28), with Bullish Exchange planning sUSDai pairs. — [CoinDesk](https://www.coindesk.com/business/2026/08/28/bullish-backs-usd-ai-with-usd100-million-gpu-stablecoin-financing)
- **K3 Capital $40M revolving facility** collateralized by sUSDai (2026-09-15). — [PR Newswire](http://www.prnewswire.com/news-releases/usdai-secures-40m-stablecoin-based-revolving-debt-facility-from-k3-capital-302879442.html)

**Fees and revenue**
- DefiLlama, pulled 2026-09-28:
  - Fees: all-time **$25.54M**; last 30 days **$1.69M**; last 7 days $1.03M.
  - Revenue: all-time **$7.35M**; last 30 days $0.17M.
  - Monthly fees ($M): 2025-10 1.73; 2025-12 2.03; 2026-01 2.00; 2026-03 1.63; 2026-04 3.09; 2026-05 1.46; **2026-06 4.35**; 2026-07 1.40; 2026-08 1.41; 2026-09 1.71.
  - Monthly revenue spikes in April 2026 ($1.87M) and June 2026 ($3.08M) likely reflect origination fees on large loans.
  - Source: [DefiLlama fees API](https://api.llama.fi/summary/fees/usd-ai)
- Project figures:
  - "$1.19M in 30-day fees" and "Top 10 stablecoin by TVL" in the May 2026 recap. — [Insights index](https://usd.ai/insights)
  - ARR of $1.1M in 2025, Q1-2026 ARR $4.0M, "YTD ARR" $14.3M, and "Q2 2026 Annualized DAO ARR: $30M". The last number looks like an origination-fee-inflated annualization. — [Lighthouse YTD](https://usd.ai/insights/usdai-2026-ytd-report-lighthouse)
  - #2 by revenue on Arbitrum in May 2026. — [CoinMarketCap AI](https://coinmarketcap.com/cmc-ai/usdai/price-prediction/) **[UNVERIFIED]**
  - Foundation post (2026-01-27) projects "$30M annual revenue at $1B originations". — [Foundation post](https://usd.ai/insights/usdai-foundation-chip)
- Trading volume: "$7.7B+ sUSDai traded in 2025" ([Foundation post](https://usd.ai/insights/usdai-foundation-chip)); "$18B" USDai plus sUSDai volume YTD by mid-2026 ([Lighthouse](https://usd.ai/insights/usdai-2026-ytd-report-lighthouse)).

**Peg and incidents**
- USDai's 2026 daily minimum was **$0.9844 (2026-05-22)** and there was a dip to $0.9933 on 2026-06-06. The price was otherwise within ±0.5%. — [DefiLlama coins API](https://coins.llama.fi/chart/coingecko:usdai)
- In Oct 2025, USDai traded at a **premium** of $1.03–1.06 while mint caps were binding. — same source
- A reported USDai ATL of **$0.7698 on 2025-09-27** ([CoinStats/CMC summary](https://coinstats.app/ai/a/fundamental-analysis-usdai)) is **not corroborated** by DefiLlama daily data (~$1.005 that day). It is likely a thin-pool wick or data error. **[UNVERIFIED]**
- **No loan default** has been publicly reported. The Aug 2026 recap notes "one early repayment ahead of schedule". — [Aug recap](https://usd.ai/insights/august-recap-100m-facility-susdai-ath)
- Operational events:
  - "USDai $100m Cap Raise for Euler Unwind" (late 2025): a cap increase to allow orderly unwinding of looped positions on Euler.
  - AutoUSDai/AutoSUSDai vaults sunset on Nov 24, 2025.
  - "Allo Points API and Audit — Six fixes made. Net +10.2% gain. No user lost points" (May 2026).
  - Sources: [Insights index](https://usd.ai/insights)
- An Aug 12, 2026 product update "fixed token claim/withdrawal issues and dashboard stability problems". — [CMC AI updates](https://coinmarketcap.com/cmc-ai/usd-ai/latest-updates/) **[aggregator]**

### Inferences
- The TVL decline from about $685M in January 2026 to about $312M on 2026-07-01 (sum of idle and loans) coincided with the end of Season 1 (Feb 18, 2026), the ICO and the TGE. It is consistent with post-airdrop mercenary outflows of roughly 55%. The Pine Analytics bear case predicted this (it cited typical 15–30% outflows; the actual outflow was larger).
- Since August 2026, total TVL has recovered to about $620M, near the old peak. The mix is now very different: about 65% loans versus about 0% in January.
- Concentration: the single $128.9M loan is about **32% of the ~$401M loan book** on 2026-09-28. The top three (roughly $128.9M, $98.1M and $54.4M) are about 70%, assuming they are still outstanding and not amortized much.
- Annualized fees run at about **$20M** (30-day fees × 12.2). Trailing-12-month protocol revenue (DefiLlama "revenue") is about **$7.2M** (Oct 2025–Sep 2026).

### Gaps
- There is no official, reconciled figure for sUSDai supply versus loan book versus NAV. The on-chain `totalAssets` of $513M and the shares × price of $353M differ.
- The Proof of Loans attestation's loan-level data (LTVs, delinquencies) was not extracted; the page summary did not disclose it.
- Loan-level amortization status and current outstanding balances per borrower are not public in the sources read.
- No Dune or rwa.xyz figures were retrieved.

---

## 3. Team and investors

### Takeaway
Permian Labs was founded in 2021. Its founders are **David Choi (CEO)**, **Conor Moore (COO)** and **Ivan Sergeev** (hardware/FPGA). It raised a **$13.4M Series A led by Framework Ventures (Aug 2025)**, followed by undisclosed strategic checks from **YZi Labs (Aug 2025)**, **Bullish (~$4M, Sep 2025, per DefiLlama)** and **Coinbase Ventures (Nov 2025)**. One source puts total equity raised at about $38M. The CHIP ICO then raised about $19.4M. No valuation for the equity rounds is disclosed.

### Cited Findings
**Founders and advisors**
- Founders David Choi, Conor Moore and Ivan Sergeev; founded 2021. — [gen.xyz profile](https://gen.xyz/blog/permianlabs-xyz); [Datawallet](https://www.datawallet.com/crypto/usd-ai-chip-explained)
- David Choi (CEO): ex-Deutsche Bank investment banking; early investing via Taureon (Memeland, Ethena, Chainflip).
- Conor Moore (COO): ex-Rockpoint Group PE, Eastdil Secured and Deutsche Bank.
- Ivan Sergeev: ex-DRW, Kumu Networks and Nuand.
- Background sources: [search summary of gen.xyz / RootData](https://gen.xyz/blog/permianlabs-xyz); [RootData Conor Moore](http://www.rootdata.com/member/Conor%20Moore?k=MjUyODA%3D)
- The wider team's backgrounds include DRW, MIT, BNP Paribas, Nansen, Balancer, Magic Eden, Synthetix and Deutsche Bank. — [permianlabs.xyz/background](https://www.permianlabs.xyz/background)
- **Evan Meagher, former CoreWeave CFO**, joined as Senior Advisor (early 2026). — [USD.AI Insights index](https://usd.ai/insights)
- In 2026 press releases, David Choi is quoted as CEO and Conor Moore as COO/co-founder. — [CoinDesk, 2026-08-28](https://www.coindesk.com/business/2026/08/28/bullish-backs-usd-ai-with-usd100-million-gpu-stablecoin-financing); [BSQ PR, 2026-06-30](https://www.prnewswire.com/news-releases/usdai-and-bsq-capital-partners-form-joint-venture-to-finance-300m-of-ai-compute-across-asia-pacific-302813765.html)

**Funding rounds**
- **Series A: $13M (USD.AI's own post says $13.4M)**, announced 2025-08-13/14, led by Framework Ventures. Participants included Dragonfly, Arbitrum and others. — [CoinDesk, 2025-08-13](https://www.coindesk.com/business/2025/08/13/usd-ai-raises-usd13m-to-expand-gpu-backed-stablecoin-lending); [USD.AI post](https://usd.ai/insights)
- **YZi Labs** (ex-Binance Labs) strategic investment announced on Aug 26 (2025), amount undisclosed. — [Yahoo Finance](https://finance.yahoo.com/news/yzi-labs-backs-usd-ai-185621852.html)
- **Coinbase Ventures** investment, amount undisclosed. DefiLlama dates it 2025-11-17. — [ChainCatcher](https://www.chaincatcher.com/en/article/2221052); [DefiLlama raises field](https://api.llama.fi/protocol/usd-ai)
- **Bullish** strategic investment of $4M, dated 2025-09-22, per DefiLlama's raises field. — [DefiLlama API](https://api.llama.fi/protocol/usd-ai) **[UNVERIFIED — single source; no press release found]**
- Investor list on the Permian Labs site: NVIDIA Inception (an accelerator program, not an equity investor), PayPal, Coinbase Ventures, Framework, YZi Labs, DCG, Dragonfly, Ethereal, Nascent, Alliance and Delphi. — [permianlabs.xyz/background](https://www.permianlabs.xyz/background). Fintech Collective is also mentioned. — [search summary / IQ.wiki](https://iq.wiki/wiki/usdai)
- Total raised of "$38m" across investors. — [gen.xyz](https://gen.xyz/blog/permianlabs-xyz) **[UNVERIFIED]**
- The investor allocation is **29.6% of CHIP** (see Section 4). — [Datawallet](https://www.datawallet.com/crypto/usd-ai-chip-explained)

### Inferences
- If investors paid about $38M for 29.6% of the token supply (a big assumption), their implied entry FDV is about $128M. That is below the $300M ICO FDV and the current FDV of about $442M. This is an illustrative inference only; no round valuation is disclosed.

### Gaps
- There is no disclosed valuation for the Series A or the strategic rounds.
- There is no seed-round detail.
- The exact YZi, Coinbase and Bullish amounts are unconfirmed.

---

## 4. Token (CHIP): sale, tokenomics, TGE, current market data

### Takeaway
- **Supply and sale:** CHIP has a 10B total supply. The ICO sold 700M CHIP (7%) at **$0.03, $300M FDV** on CoinList (Feb 22–27, 2026). It raised about **$19.4M against a $21M target**, i.e. it was **undersubscribed**. The airdrop was 300M (3%).
- **TGE:** April 21–22, 2026, with 2.0B (20%) circulating. Listings included Binance, Coinbase, Upbit, Bithumb, Bybit, OKX, KuCoin and others, plus perps on Binance, OKX, Bitget and Hyperliquid.
- **Price path:** ATH about $0.14 on 2026-04-23. ATL about $0.0216 around 2026-08-10.
- **Now (2026-09-28):** about **$0.0443, market cap about $88.5M, FDV about $442M**.
- **Unlocks:** the first investor/team cliff is about **April 2027** (month 12).
- **Value accrual:** CHIP "does not entitle holders to protocol revenue".

### Cited Findings
**Sale**
- Terms: CoinList, Feb 22–27, 2026; $0.03 per CHIP; FDV $300,000,000; 700,000,000 CHIP for sale; total supply 10,000,000,000; 100% unlocked at TGE; U.S. accredited buyers have a 1-year lock-up. Whitelist-only for Allo Game participants; minimum $100; payment in USDC/USDT (ERC-20). — [CoinList blog](https://blog.coinlist.co/announcing-the-usd-ai-token-sale-on-coinlist/)
- ICO = 7% of supply, estimated $21M raise. KYC Feb 10–27. Non-accredited U.S. residents excluded. — [USD.AI "CHIP ICO, Airdrop, and What's Next", 2026-02-09](https://usd.ai/insights/chip-ico-airdrop)
- **Result:** about $19.4M committed against the $21M target. Mid-sale reports showed only about $1.9M raised, with late large wallets filling most of it. — [Tekedia](https://www.tekedia.com/usd-ai-successfully-closed-its-chip-token-sale-raising-over-19-4m/); [Bitget News](https://www.bitget.com/news/detail/12560605236405); [Atomic Wallet](https://atomicwallet.io/academy/articles/what-is-usd-ai)

**Allocation**
- 7% ICO plus 3% airdrop (300M CHIP) = 10% distributed for Season 1. — [CMC AI](https://coinmarketcap.com/cmc-ai/usdai/price-prediction/); [search summary of docs](https://docs.usd.ai/governance/tokenomics)
- Ecosystem Bootstrapping is **27.5%**, which includes the 10% already distributed in Season 1. The rest (about 17.5%, ~1.75B CHIP) is for "airdrops, upcoming incentive programs". — [docs.usd.ai tokenomics](https://docs.usd.ai/governance/tokenomics)
- Full split: Ecosystem **27.5%**, Investors **29.6%**, Contributors **23.5%**, Reserve **19.5%**. — [Datawallet](https://www.datawallet.com/crypto/usd-ai-chip-explained). The docs fetch returned **Reserve 19.8%**, which conflicts. 27.5+29.6+23.5+19.5 = 100.1%, so there is a rounding issue somewhere. Flag this.
- **Vesting for Contributors and Investors:** "0% vests before month 12, 33% vests at month 12, and the remaining 67% vests in equal monthly installments over the following 24 months". — [docs.usd.ai tokenomics](https://docs.usd.ai/governance/tokenomics)

**TGE and listings**
- Original guidance: "ICO: Q1 2026, TGE: late Q1 2026" ([Foundation post, 2026-01-27](https://usd.ai/insights/usdai-foundation-chip)) and "TGE expected March 2026" ([CoinList](https://blog.coinlist.co/announcing-the-usd-ai-token-sale-on-coinlist/)).
- Actual TGE and trading were **2026-04-21 / 04-22** (the official post says April 22), so the TGE slipped about 3–4 weeks.
- Venues: Binance, Coinbase, Upbit, Bybit, KuCoin, Gate and others; perps on Binance, OKX, Bitget and Hyperliquid. — [USD.AI "$CHIP Is Live"](https://usd.ai/insights/chip-is-live); [CMC/aggregator summary: also Bithumb, MEXC, HTX](https://coinmarketcap.com/cmc-ai/usd-ai/latest-updates/)
- **Binance HODLer Airdrops** (announced 2026-04-28): 25,000,000 CHIP (0.25% of supply). "Circulating Supply at Listing: 2,000,000,000 CHIP (20%)". — [Binance announcement](https://www.binance.com/en/support/announcement/detail/c8d2380a71ee4b56980cf7798d2e3d8f)

**"Protected CHIP", ICO refund and Pendle YT linkage** (directly relevant to YT valuation)
- ICO participants who "Leveled Up" by locking Pendle YTs received **protected CHIP** that unlocks at **YT maturity (June 17, 2026 and Oct 14, 2026)**. At unlock it "will be settled at $270M / $190M FDV. The price difference will be refunded in USDC." — [USD.AI "$CHIP Is Live"](https://usd.ai/insights/chip-is-live)
- Before maturity, holders can either (a) claim early and trade freely, forfeiting the USDC refund right, or (b) "Request a USDC refund at 300M FDV at any time", forfeiting CHIP. — same source
- USDC was "sent directly to eligible wallets on April 20, 2026"; the amount is undisclosed. — same source
- **Level Up mechanism** (timeline Feb 18–27, 2026):
  - Paths: "Own" (ICO) and "Earn" (airdrop), each with Boost/Max strategies and 4-month or 8-month maturities.
  - YT required per CHIP: about **0.18 YT-USDai** or about **0.40 YT-sUSDai**. sUSDai YT "earns 4.5% yield during lock".
  - **Overlock Bonus:** a Flatiron point multiplier, first priority on unsold ICO CHIP, and a 20% bonus on all YTs up to 2× the Level Up Score.
  - Source: [USD.AI Level Up guide](https://usd.ai/insights/allo-game-to-flatiron-level-up-guide)
- Locked YTs "stop receiving any yield on Pendle". Holders get yield through USD.AI's contract instead, plus Allo rewards in batches about every 20 days. The multiplier decays over time and blends at the wallet level (example: 500k at 22× plus 500k at 20× = 21×). — [docs.usd.ai Pendle YT locks](https://docs.usd.ai/depositor/faq/pendle-yield-yt-locks)
- In Season 1, the Allo multiplier for Pendle YT-USDai was **cut from 30× to 15× on 2025-11-18**, and Pendle YT-USDai volume fell 21.45% in 24 hours. — [CMC USDai analysis / search summary](https://coinmarketcap.com/cmc-ai/usdai/price-analysis/) **[aggregator]**

**Market data**
- **Current (CoinGecko, 2026-09-28):** price **$0.04425** (−10.3% over 24h); market cap **$88.48M** (rank #310); **FDV $442.4M**; 24h volume $10.3M; circulating 2.0B of 10B.
- **All-time range:** ATH $0.1402 (−68.4% from peak); ATL $0.02162.
- **Recent change:** 7d −4.9%, 30d +8.7%.
- **Top venues by volume:** Binance CHIP/USDT ($2.3M), Upbit KRW ($2.1M), Coinbase ($493K).
- Source: [CoinGecko](https://www.coingecko.com/en/coins/usd-ai)
- DefiLlama price $0.04428 and mcap $88.5M on 2026-09-28. — [DefiLlama coins](https://coins.llama.fi/prices/current/coingecko:chip-2)
- **ATH conflicts:** $0.1189 (Apr 22), $0.1383/$0.1384 (Apr 23), $0.1402 (CoinGecko). — [Datawallet](https://www.datawallet.com/crypto/usd-ai-chip-explained); [CoinGabbar](https://www.coingabbar.com/en/price-prediction/chip-price-prediction-usd-ai-buy-the-dip-or-exit)
- **Price path (DefiLlama daily):**
  - Apr 2026: 0.061 (04-22 open), 0.113 (04-23), 0.073 (04-27)
  - May–Jul 2026: 0.059 (05-04), 0.040 (05-29), 0.031 (06-19), ~0.030 (mid-July), 0.026 (07-28)
  - Aug 2026: **~0.022 (08-10 low)**, 0.039 (08-28)
  - Sep 2026: **0.059 (09-06, local high)**, 0.0365 (09-17), 0.050 (09-26), ~0.044–0.047 (09-28)
  - Source: [DefiLlama coins chart](https://coins.llama.fi/chart/coingecko:chip-2)
- August 2026 was +53% (low $0.022 on Aug 10, $0.047 by Aug 28). — [search summary of CMC/crypto media](https://coinmarketcap.com/currencies/usd-ai/)

**Governance and value accrual**
- CHIP governs collateral eligibility, rate tiers, borrower criteria, fee parameters (origination, NIM spread, QEV redemption fees) and upgrades. — [docs.usd.ai/governance/chip](https://docs.usd.ai/governance/chip)
- "**CHIP does not entitle holders to protocol revenue**". — [Foundation post, 2026-01-27](https://usd.ai/insights/usdai-foundation-chip)
- sCHIP staking is live and earns points/Allo. — [CHIP is live](https://usd.ai/insights/chip-is-live)
- No buyback or fee-switch proposal was found.
- Messari published a valuation report ("A Valuation of USD.AI ($CHIP)") using scenario analysis on origination throughput, NIM and "governance-contingent value routing". It was paywalled/429, so scenario numbers were not retrieved. A Chinese translation is on the USD.AI site. — [Messari](https://messari.io/report/a-valuation-of-usdai-chip)

### Inferences
- **Unlock overhang:** Investors plus Contributors = 53.1% of supply (5.31B CHIP).
  - At month 12 (**~2026-04-21 → ~2027-04-21**), 33% of that unlocks, about **1.75B CHIP (17.5% of supply)**. That is roughly **88% of today's 2.0B circulating supply**.
  - After that, about 148M CHIP unlocks per month (1.48% of supply) for 24 months.
  - The remaining Ecosystem (~17.5%) and Reserve (~19.5%) allocations are not scheduled in public docs and may be released at the Foundation's discretion. The Season 2 airdrop will draw on Ecosystem.
- **Multiples:** at FDV $442M, FDV / annualized fees (~$20M) ≈ 22×. FDV / trailing-12-month DefiLlama revenue (~$7.2M) ≈ 61×. FDV / total TVL (~$620M) ≈ 0.71×. Pine Analytics' comparables were Ethena at 0.38× and Maple at 0.16× (January 2026).
- **Protected-CHIP settlement:** CHIP currently trades at about $442M FDV, well above the $270M/$190M settlement FDVs and the $300M refund FDV. Only a crash below about $0.019–0.027 per CHIP before Oct 14 would trigger USDC top-ups or make the refund attractive. Conversely, the Oct 14 unlock of protected CHIP could add sell pressure from ICO/Level-Up participants.
- **Polymarket check:** the "USD.AI FDV above ___ one day after launch" market had heavy "No" on $2B. With the price around $0.10–0.11 on the day after launch, the 10B-supply FDV was about $1.0–1.1B. Resolution depends on Polymarket's exact definition (see Section 6).

### Gaps
- There is no official, verified full allocation table with exact token amounts (Reserve 19.5% vs 19.8%).
- The Season 2 (Flatiron) CHIP reward pool size is not disclosed.
- The number of CHIP airdrop recipients and the amount of USDC paid out on Apr 20, 2026 are unknown.
- Messari scenario FDVs were not retrieved.
- No confirmation was found of a Season 3 or of any post-Flatiron program after Oct 14, 2026.

---

## 5. Official statements on seasons, points and the timeline

### Takeaway
**Season 1 ("Allo Game")** ran from 2025 to **2026-02-18** and converted into the ICO (7%) and airdrop (3%) through the "Level Up" YT-lock mechanism. **Season 2 ("Flatiron")** started **2026-04-21**. All rewards are CHIP airdrops, spread across 4 strategy types with **1×–40× multipliers**, and it runs **through 2026-10-14**. Caps were removed and looping is the thematic focus. No Season 2 pool size, snapshot mechanics or claim date has been published.

### Cited Findings
- **Foundation post, 2026-01-27:** "The Allo Game concludes and transitions immediately to the new season, ICO, Airdrop, and subsequent TGE in late Q1." — [USD.AI Foundation post](https://usd.ai/insights/usdai-foundation-chip); [ICO Drops](https://icodrops.com/usd-ai/)
- **Level Up timeline:**
  - Feb 18: Allo Game ends and CHIP allocations are finalized.
  - Feb 19: Plasma YTs unlock.
  - Feb 18–25: ICO/airdrop offer window.
  - Feb 22–27: CoinList ICO.
  - March (TBD): TGE, which actually happened in April.
  - Source: [Level Up guide](https://usd.ai/insights/allo-game-to-flatiron-level-up-guide)
- "Alignment at the end of the Allo Game is the gating condition" for ICO and airdrop eligibility (participation in strategies marked "ICO" or "Airdrop"). — [CHIP ICO & Airdrop post, 2026-02-09](https://usd.ai/insights/chip-ico-airdrop)
- **Flatiron rules:**
  - "All rewards will be distributed through $CHIP airdrops".
  - Four strategies: (1) stake CHIP or add DEX liquidity; (2) LP/stake USDai/sUSDai on Curve, Gamma, Aerodrome, Balancer, Fluid, Maverick; (3) supply USDai/sUSDai on Fluid, Euler, Silo, Morpho, Gearbox; (4) "Buy or lock YTs and LPTs on Pendle".
  - "Multipliers range from 1x to 40x". "Flatiron runs through Oct 14, 2026".
  - Source: [CHIP is live](https://usd.ai/insights/chip-is-live)
- Flatiron is a "single points system with rewards distributed entirely through airdrops". "Deposit caps are removed; looping strategies become fully supported." — [Level Up guide](https://usd.ai/insights/allo-game-to-flatiron-level-up-guide)
- **Flatiron Referral Boost:** a creator tier earns "up to 20% on every point your referrals generate". — [Insights index](https://usd.ai/insights)
- The July recap reiterates: "Season 2 $CHIP airdrop points campaign through October 14, 2026". — [July recap](https://usd.ai/insights/usdai-july-recap-81m-deployed-loans)

### Inferences
- Season 2 airdrop CHIP must come from the remaining ~17.5% Ecosystem bucket (≤1.75B CHIP). Pool size is undisclosed. If the Foundation gave Season 2 the same 3% it gave Season 1's airdrop (300M CHIP ≈ $13M at $0.0443), that would be a modest reward relative to about $600M of TVL. **This is speculative.**
- Oct 14, 2026 stacks three events: Flatiron ends, Pendle Oct-14 YTs mature, and protected CHIP settles or unlocks. Expect TVL and point-farming outflows plus CHIP supply around that date. This is a key event risk for YT pricing and for CHIP.

### Gaps
- The Season 2 CHIP pool, points-to-CHIP conversion, snapshot and claim date, vesting of the S2 airdrop (if any), and any Season 3 were not found in official sources.
- Discord and Telegram announcement channels were not directly accessible.

---

## 6. Community sentiment (X, Reddit, media, prediction markets)

### Takeaway
Sentiment is split.
- **Bulls** point to the AI-capex/"compute credit" narrative, blue-chip facilities (Bullish, K3, BSQ, PayPal, Coinbase) and a real loan book that has grown about 4× since April.
- **Bears and critics** point to the no-revenue governance token, the roughly 80% locked supply with a big April 2027 cliff, borrower concentration, a points-driven TVL that bled about 55% after Season 1, and an ICO that struggled to fill.
- **Market:** CHIP is down about 68% from its ATH and trades about 48% above its ICO price.

### Cited Findings
**Bear views**
- **Pine Analytics, 2026-01-28:**
  - At $300M FDV, CHIP was 0.46× FDV/TVL versus Ethena 0.38× and Maple 0.16×, implying 17%–65% downside on compression.
  - "~99% of backing remains in Treasuries"; growth is "points farming driving growth"; borrowers are "smaller, riskier, and more cyclical".
  - "If $CHIP rallies on narrative momentum... we view it as a short opportunity."
  - Source: [Pine Analytics](https://pineanalytics.substack.com/p/the-bear-case-for-chip)
- **@RepublikRupiah (X), 2026-04-24:** flagged overvaluation at "100x" current revenue with 80% of supply locked. — [CMC AI updates](https://coinmarketcap.com/cmc-ai/usd-ai/latest-updates/) **[single KOL]**
- **@Naqib_Noor (X), 2026-06-02:** holders vote on hardware eligibility and rates, but protocol yield is not captured by the token. — [CMC AI updates](https://coinmarketcap.com/cmc-ai/usd-ai/latest-updates/) **[single KOL]**
- **CoinResearch Medium write-up:**
  - "Two borrowers represent nearly the entire loan pipeline. A single default is a protocol event."
  - "Top 2 addresses controlled ~96% of CHIP supply at TGE" (likely Foundation/vesting wallets).
  - Bull case FDV of $500M–$1B in 18–24 months.
  - Source: [CoinResearch Medium](https://coinresearch.medium.com/usd-ai-chip-financing-the-ai-gpu-supercycle-with-on-chain-credit-and-real-yield-950ab06166a2) **[UNVERIFIED]**
- **Farmer complaints:**
  - The Allo multiplier cut on Pendle YT-USDai (30× → 15×, Nov 18, 2025) hit YT farmers. — [CMC USDai](https://coinmarketcap.com/cmc-ai/usdai/price-analysis/)
  - The points audit found six accounting bugs (May 2026). — [Insights](https://usd.ai/insights)
  - Deposit caps ($250M → $500M in Sept 2025) pushed USDai to a 3–6% premium in Oct 2025. — [DefiLlama](https://api.llama.fi/protocol/usd-ai)
- **ICO demand was weak at first:** only about $1.9M was committed mid-sale and the final total fell short of target ($19.4M of $21M). — [Bitget News](https://www.bitget.com/news/detail/12560605236405); [Tekedia](https://www.tekedia.com/usd-ai-successfully-closed-its-chip-token-sale-raising-over-19-4m/)
- **Post-listing crash** was attributed to CoinList buyers taking profit at 150–200% gains. Early on, "24-hour trading volume consistently exceeds its market cap by 5-10x". — [CoinGabbar](https://www.coingabbar.com/en/price-prediction/chip-price-prediction-usd-ai-buy-the-dip-or-exit); search summary

**Bull views**
- **Reddit r/CryptoCurrency, u/Slow-Set-2856, ~2026-07-03:** "someone has to finance all that hardware"; banks cannot underwrite GPU collateral; CHIP is a bet on AI capex. Also: "Do your own read on the collateral mechanics and the tokenomics." — [CoinSpectator repost](https://coinspectator.com/mainstream/2026/07/03/usd-ai-chip-the-ai-capex-supercycle-needs-financing-not-just-compute-heres-my-thesis/)
- **@MannuelBTC (X), 2026-09-25:** bullish technical setup, entry $0.048–0.05, target $0.10. — [CMC AI updates](https://coinmarketcap.com/cmc-ai/usd-ai/latest-updates/) **[single KOL, TA]**
- **Media framing:**
  - Bullish financing: "Compute is becoming a credit market in its own right" (David Choi). — [CoinDesk, 2026-08-28](https://www.coindesk.com/business/2026/08/28/bullish-backs-usd-ai-with-usd100-million-gpu-stablecoin-financing)
  - Kamino: "compute-backed credit" on Solana. — [The Defiant](https://thedefiant.io/news/defi/kamino-opens-gpu-loan-linked-susdai-collateral-market-on-solana)
- On 2026-09-24 AI tokens fell 4.58%, and USD.AI's GPU-loan model was described as differentiated. — [CMC AI](https://coinmarketcap.com/cmc-ai/usd-ai/latest-updates/)
- **Trending:** CHIP hit #1 on CoinGecko trending within 48 hours of launch. — [search summary](https://www.coingecko.com/en/coins/usd-ai)

**Prediction markets and pre-market**
- Polymarket's "USD.AI FDV above ___ one day after launch?" had 14 outcomes and **about $5.5M volume**. More than $314K went into the $2B bucket, mostly on "No", with the crowd centred near $300M. There were 101 USD.AI-related markets. The resolution rule used "price at 4:00 PM ET on the day after launch". — [Crypto Briefing](https://cryptobriefing.com/polymarket-usdai-chip-2b-fdv-prediction-market/); [Polymarket event](https://polymarket.com/event/usdai-fdv-above-one-day-after-launch)
- Whales Market published a pre-TGE FDV prediction post; its content was not retrieved. — [Whales Market blog](https://whales.market/blog/usd-ai-chip-fdv-prediction/)
- **Current derivatives:** CHIP perps trade on Binance, OKX, Bitget and Hyperliquid. — [CHIP is live](https://usd.ai/insights/chip-is-live)

### Inferences
- The narrative has shifted from "points farm with T-bills" (early 2026) to "real GPU credit book with institutional facilities" (Aug–Sep 2026). CHIP's rebound from $0.022 (Aug 10) to about $0.044–0.059 in September tracks the Bullish, K3 and $128.9M-loan headlines.
- Retail sentiment appears heavily Korean-exchange driven (Upbit KRW is the #2 venue by volume).

### Gaps
- Discord and Telegram content could not be accessed directly.
- No systematic X sentiment data (volume, mindshare) or Kaito mindshare figures were found.
- No current Polymarket market on CHIP price or TGE-related events was found.
- Whales Market and Aevo pre-market prices from before TGE were not retrieved.

---

## 7. Key risks

### Takeaway
The main risks are:
- **Concentrated neocloud credit risk:** the largest loan is about 32% of the book, with 13 borrowers.
- **GPU depreciation and liquidation costs** on 3-year loans.
- **Liquidity/duration mismatch:** 30-day queue versus 3-year amortizing loans, bridged by credit lines.
- **Dependence on PYUSD/PayPal and on the Barker reinsurance counterparty.**
- **Untested UCC Article 7 legal structure.**
- **Regulatory risk** (sUSDai as a possible security).
- For CHIP specifically: **no revenue rights plus a large 2027 unlock cliff.**

### Cited Findings
- Stablewatch (2025-10-23) lists these risks — [Stablewatch](https://www.stablewatch.io/research/usd-ai-deep-dive) **[STALE but structural]**:
  - "Accelerated depreciation of GPU collateral" from NVIDIA product cycles.
  - "Untested application of UCC Article 7".
  - "High likelihood that its yield-bearing sUSDai token will be classified as a security in key jurisdictions".
  - Operational dependence on curators for offchain enforcement.
  - U.S. export controls removing China from secondary GPU markets, which could create a supply glut.
  - CUDA-moat erosion (AMD ROCm).
  - IT asset disposition fees of "around 30% of the gross sale price" on liquidation.
- Barker covers a shortfall only up to 80% of the assessed collateral value. Losses beyond that, and correlated counterparty or reinsurer failure, remain. — [USD.AI insured sUSDai](https://usd.ai/insights/upgrading-fully-insured-susdai)
- Duration mismatch is explicitly acknowledged: 3-year monthly-amortizing loans versus the shorter sUSDai cycle, which the K3 credit line is meant to bridge. — [K3 PR](http://www.prnewswire.com/news-releases/usdai-secures-40m-stablecoin-based-revolving-debt-facility-from-k3-capital-302879442.html)
- "sUSDai is not instantly redeemable at par value"; queues can extend across multiple epochs. — [docs.usd.ai](https://docs.usd.ai/faq/usdai-and-susdai-101)
- Datawallet lists nine risk categories: credit quality, collateral depreciation, liquidity constraints, smart contract, borrower repayment capacity, valuation accuracy, yield variability, concentration and token volatility. — [Datawallet](https://www.datawallet.com/crypto/usd-ai-chip-explained)
- Borrower concentration: "two borrowers represent nearly the entire loan pipeline" (earlier stage). — [CoinResearch Medium](https://coinresearch.medium.com/usd-ai-chip-financing-the-ai-gpu-supercycle-with-on-chain-credit-and-real-yield-950ab06166a2) **[UNVERIFIED]**. The top announced facilities are QumulusAI and Sharon AI at $500M each. — [Insights](https://usd.ai/insights)
- The largest new loan ($128.9M) goes to an undisclosed borrower. Its tenor and rate are undisclosed. — [PR Newswire, 2026-09-23](https://www.prnewswire.com/news-releases/usdai-announces-128-9m-gpu-financing-facility-its-largest-to-date-302888224.html)
- Regulatory: the ICO excluded non-accredited U.S. persons, and U.S. accredited buyers face a 1-year lock. — [CoinList](https://blog.coinlist.co/announcing-the-usd-ai-token-sale-on-coinlist/); [USD.AI ICO post](https://usd.ai/insights/chip-ico-airdrop)
- Token-level risks: CHIP has no revenue entitlement ([Foundation post](https://usd.ai/insights/usdai-foundation-chip)); 80% of supply is locked ([Binance](https://www.binance.com/en/support/announcement/detail/c8d2380a71ee4b56980cf7798d2e3d8f)).

### Inferences
- Leverage: new credit lines total $140M (Bullish $100M plus K3 $40M) against sUSDai or protocol assets. They add a senior claim, or at least a liquidity dependency, ahead of or alongside sUSDai holders in stress. Their seniority terms are undisclosed.
- **Pendle YT holders (sUSDai/USDai)** are exposed to:
  - (a) points-to-CHIP value, which depends on CHIP price and the undisclosed Season 2 pool;
  - (b) the Oct 14, 2026 maturity cliff;
  - (c) sUSDai yield actually realized (about 7.2% net, versus a 12.4% target).

### Gaps
- No public data on loan delinquency or impairment, or on LTV drift since origination.
- Seniority and covenants of the Bullish and K3 facilities are unknown.
- No details of any exploit or security incident were found. None appear to have occurred.
