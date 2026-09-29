# OnRe Finance (ONyc): Fundamentals as of 2026-09-29

Research date: 2026-09-29. Every metric carries its date. "API" means data pulled directly from OnRe's public NAV API or DefiLlama's API on 2026-09-29. Official OnRe sources (blog, docs, API) are self-reported. Allez Labs is paid by OnRe (its fee does not depend on the rating), so its reports are "independent but client-commissioned".

---

## Q1. What is OnRe / ONyc, how is yield produced, what is the APY/NAV history, and what are the redemption terms?

### Takeaway
ONyc is a non-rebasing token priced at NAV. It gives a pro-rata claim on a Bermuda segregated account that collateralizes short-duration reinsurance, plus reserve/collateral yield. It is explicitly **not a stablecoin**. NAV went from ~$1.009 (May 28, 2025) to **$1.1506 (Sep 29, 2026)**. Realized yield has been steady at **~10–12% APY** (live APY **11.02%** on 2026-09-29), with a max NAV drawdown of −0.24%. Exits run through a 25 bp-fee on-chain RFQ/redemption vault backed by a ~15% liquidity layer, plus DEX liquidity. Primary redemption requires KYC/AML.

### Cited Findings
**What it is**
- ONyc "represents a proportional share of a regulated segregated account used for underwriting short-duration insurance and reinsurance contracts… held in a legally ring-fenced structure in Bermuda." "It is not a stablecoin… and is not corporate credit or a tokenized hedge fund." Yield accrues through NAV appreciation, not distributions. — [OnRe Docs: ONyc](https://docs.onre.finance/introduction/onre-tokenized-reinsurance-onyc)
- FAQ: "ONyc is not designed to maintain a fixed $1 peg. It is a NAV-based, yield-bearing asset"; "ONyc is a non-rebasing token." Target: "10-12% base APY from underwriting performance", with additional collateral yield on top. — [OnRe Docs FAQ](https://docs.onre.finance/technical-resources/frequently-asked-questions)
- Co-founder explainer (Nov 4, 2025): capital "cannot be used for operations or development"; OnRe keeps "roughly 20 percent of our capital unallocated to help stabilize secondary markets." — [OnRe blog](https://www.onre.finance/blog/understanding-solanas-highest-yielding-dollar-asset)
- Product lineage: launched as **ONe** on May 21, 2025 (sUSDe deposits, "projected returns of up to 40.35%" including token incentives). Evolved into **ONyc** on Jul 3, 2025, a multi-collateral asset with a "16% base APY" target. — [OnRe launch post](https://www.onre.finance/blog/onre-backed-by-ethena-solana-ventures-and-rockawayx-launches-structured-yield-product-combining-real-world-stability-and-on-chain-upside); [ONe→ONyc post](https://www.onre.finance/blog/onre-evolves-one-into-onyc-to-power-stablecoin-adoption-across-defi-and-traditional-markets)
- ONyc mint: 5Y8NV33Vv7WbnLfq3zBcKSdYPrk7g2KoiQoe7M2tcxp5 (Solana SPL). Mint is against USDC/USDG with no mint fee. NAV is computed on-chain from contract parameters (base price, annual rate, time), and a max-supply cap is checked on every mint. Pyth/Chainlink feeds are provided for integrators. — [Docs: Token Configuration](https://docs.onre.finance/technical-resources/token-configuration-and-reference); [Docs: Minting](https://docs.onre.finance/for-capital-providers/minting-onyc)

**Yield sources**
- There are two streams: (1) reinsurance premiums, "paid upfront and earned over the life of the contract" (e.g., "a policy returning 17% over six months annualizes to 34%"); (2) collateral yield. Actuarial projections assume only T-bill-level collateral rates. — [Docs: Portfolio Makeup](https://docs.onre.finance/reinsurance-framework/portfolio-makeup); [Docs: Yield Mechanisms](https://docs.onre.finance/introduction/yield-mechanisms)
- Reserve assets listed: T-Bills, sUSDe, syrupUSDC, USCC (Bitwise Crypto Carry), USDv, USDC, USDG, sUSDS, USYC. — [Docs: Collateral Composition](https://docs.onre.finance/for-capital-providers/collateral-composition)
- Allez (Jul 31, 2026): $144.34M deployed to underwriting (Bound $130.89M + Offered $13.45M; 58.3% of AUM) at a "blended ~13.6% APY on that leg". There is a Liquidity Layer of $37.12M (15% floor) and $66.01M "Available Capital". The reported 11.64% APY is blended across all three buckets. USDG made up ~31% of AUM (up from ~20% in June). — [Allez ONyc Asset Risk Assessment, Jul 31 2026](https://allez.xyz/reports/onre/ONyc_Asset_Risk_Assessment_260731.pdf)
- Portfolio ROL (rate on line) was 16.93% on ~$165.09M gross exposure, with 13 active and 6 allocated contracts (Jul 31, 2026). — [Allez](https://allez.xyz/reports/onre/ONyc_Asset_Risk_Assessment_260731.pdf)
- Older/marketing yield framing: "reinsurance underwriting premiums (producing 8–10% annually)" plus collateral, giving a "9–15% APY" blended base. — [Solana Compass, Sep 2026](https://solanacompass.com/news/onre-surpasses-300m-aum-as-onyc-compounding-interest-rewards-season-1-opens-september-27). The Rhodium Re post (Jan 14, 2026) still cites "targets a 16% base return". — [OnRe blog](https://www.onre.finance/blog/onre-delegates-150m-to-middle-east-mga-partner-rhodium-re-to-expand-global-underwriting-distribution-for-onyc)

**APY history (OnRe monthly reviews; month-end)**
- Nov 2025: base yield raised to **13.35%** after two new deals — [Nov 2025 review](https://www.onre.finance/blog/onre-in-review-november-2025)
- Dec 2025: **10.87%**, NAV $1.0641 — [Dec 2025 review](https://www.onre.finance/blog/onre-in-review-december-2025)
- Jan 2026: **9.27%**, NAV $1.0731 — [Jan 2026 review](https://www.onre.finance/blog/onre-in-review-january-2026)
- Feb 2026: **10.25%**, NAV $1.0805 — [Feb 2026 review](https://www.onre.finance/blog/onre-in-review-february-2026)
- Mar 2026: **~10.22%**, NAV $1.0894 — [Mar 2026 review](https://www.onre.finance/blog/onre-in-review-march-2026)
- Apr 2026: **10.13%**, NAV $1.0981 — [Apr 2026 review](https://www.onre.finance/blog/onre-in-review-april-2026)
- May 2026: **11.87%**, NAV $1.1086 — [May 2026 review](https://www.onre.finance/blog/onre-in-review-may-2026)
- Jun 2026: **11.76%**, NAV $1.1189 — [Jun 2026 review](https://www.onre.finance/blog/onre-in-review-june-2026)
- Jul 2026: **11.64%**, NAV $1.1294 — [Jul 2026 review](https://www.onre.finance/blog/onre-in-review-july-2026)
- Sep 29, 2026: live APY **11.02%**, live NAV **$1.15055451** — [OnRe API live-apy](https://core.api.onre.finance/data/live-apy); [live-nav](https://core.api.onre.finance/data/live-nav)
- Oct 2025, secondary yield markets: RateX PT-ONyc fixed **16.05%** APY, and "Leverage up to 156x with YT-ONyc". — [Oct 2025 review](https://www.onre.finance/blog/onre-in-review-october-2025)
- Exponent PT-ONyc (Sep 10, 2026 maturity) fixed **14.4%** APY as of Jul 31, 2026, up from ~13.2% at the Jun 17 open. — [Allez](https://allez.xyz/reports/onre/ONyc_Asset_Risk_Assessment_260731.pdf)

**NAV-implied returns, computed from the OnRe daily NAV API (489 daily points, 2025-05-28 → 2026-09-29)** — [OnRe NAV API](https://core.api.onre.finance/data/nav)
- NAV $1.00897 (2025-05-28) → $1.0166 (2025-07-01) → $1.03527 (2025-10-01) → $1.0641 (2026-01-01) → $1.08977 (2026-04-01) → $1.11926 (2026-07-01) → $1.14112 (2026-09-01) → $1.15055 (2026-09-29).
- Annualized NAV growth to 2026-09-29: 7d 11.02%, 30d 11.35%, 90d 11.83%, 180d 11.57%, 365d 11.20%. Since inception it is about +14.0% over ~16 months.
- Only 4 daily NAV declines ever recorded, all in Jul 2025 (e.g., Jul 6, 2025: 1.01661 → 1.01413). None since Aug 1, 2025.
- Allez: inception APY 10.07% (429 days, net); 30-day NAV-implied 11.69%; "Max NAV drawdown −0.24%… zero negative months." — [Allez](https://allez.xyz/reports/onre/ONyc_Asset_Risk_Assessment_260731.pdf)

**Redemption / lockups / liquidity**
- On-chain redemption through the OnRe app, quoted in USDG. The fee is **25 bps**, and the price is further discounted by a "convex power curve" based on available liquidity and net demand per epoch. Execution is atomic, with minimum output. Only KYC/AML-verified wallets can redeem, so secondary-market buyers must complete AML first. — [Docs: Redemptions & Onchain Liquidity](https://docs.onre.finance/technical-resources/redemptions-and-onchain-liquidity)
- "About 15% of the capital" is carved out for redemption liquidity, and part of it sits in an on-chain "redemption vault". Buy flow can auto-refill the vault up to a target. — [Docs: Redemptions](https://docs.onre.finance/technical-resources/redemptions-and-onchain-liquidity); [Liquidity Engine post, Sep 24 2026](https://www.onre.finance/blog/introducing-onres-liquidity-engine-powered-by-titan)
- FAQ: redeem to USDC/USDG "subject to redemption windows, holding periods, and liquidity availability"; secondary liquidity 24/7 via Orca, Raydium, Jupiter. — [Docs FAQ](https://docs.onre.finance/technical-resources/frequently-asked-questions)
- Allez (Jul 31, 2026) describes three paths:
  - Monthly best-effort off-chain redemption from the OnRe Liquidity Layer (25 bp fee, waived for market makers; "often processed within hours"; queued if the layer is short).
  - **Quarterly off-chain redemption with no fee, max 10% of AUM per quarter (~$24.75M)**.
  - DEX exit, mainly the Orca ONyc-USDC pool: DEX TVL $8.92M; ~$2.14M of sell-side depth at 2% slippage. — [Allez](https://allez.xyz/reports/onre/ONyc_Asset_Risk_Assessment_260731.pdf)
- ONyc buybacks are discretionary. They are funded from operating revenue, premiums allocated to the liquidity layer, and unallocated reserves. — [Docs: Buybacks](https://docs.onre.finance/onyc-in-defi/onyc-buybacks). Cumulative buybacks: $5.2M+ (Nov 2025), $20.86M (Mar 2026), $45.41M (Apr 2026). — [Nov 2025](https://www.onre.finance/blog/onre-in-review-november-2025), [Mar 2026](https://www.onre.finance/blog/onre-in-review-march-2026), [Apr 2026](https://www.onre.finance/blog/onre-in-review-april-2026) reviews
- Liquidity Engine (Sep 24, 2026): the on-chain RFQ is backed by OnRe's own capital (~15%) and routed through Titan. The aim is for it "to become the primary source of liquidity for ONyc across DeFi." — [OnRe blog](https://www.onre.finance/blog/introducing-onres-liquidity-engine-powered-by-titan)
- Access paths: "Open Access" is permissionless, runs through app.onre.finance/earn, and "does not involve interaction with OnRe's regulated entities". "Institutional Access" requires KYC/KYB. — [Docs: Open vs Institutional](https://docs.onre.finance/for-capital-providers/open-access-vs-institutional-access)

### Inferences
- ONyc behaves like a **yield-bearing fund token or "yield-bearing dollar"**, not a stablecoin. NAV accrual has been almost linear, which suggests the NAV is driven by contract parameters (base price × annual rate × time) and periodically re-marked. Realized volatility is therefore artificially low until a loss event forces a re-mark.
- APY has converged to ~11% (range 9.3–13.4% since Nov 2025), well below the 16% target at launch and the ">30% bull market" ONe marketing.

### Gaps
- OnRe's own fee take (management/performance/spread between gross premium and holder APY) is not disclosed in the docs I found. Only the 25 bp redemption fee and the zero mint fee are stated.
- I could not find a precise statement of the NAV re-marking cadence after a claim, beyond "APY absorption" in the FAQ.

---

## Q2. Team, entity, and license

### Takeaway
OnRe is the trading name of **On Re SAC Ltd.** (Bermuda segregated accounts company). It holds a BMA **Class IIGB** insurer licence and a **Class F DABA** licence, BMA registration no. 55347. The company is a restructured continuation of **Nayms** (founded 2018/2019). CEO Dan Roberts carried over from Nayms. Senior reinsurance hires in 2025–26 came from Fidelis and similar firms.

### Cited Findings
- "OnRe is a trading name of On Re SAC Ltd., which is authorised and regulated by the Bermuda Monetary Authority. OnRe holds a Class F licence under the Digital Asset Business Act 2018 and a Class IIGB licence under the Insurance Act 1978." "ONyc is intended for eligible accredited investors." — [OnRe blog, Jul 3 2025](https://www.onre.finance/blog/onre-evolves-one-into-onyc-to-power-stablecoin-adoption-across-defi-and-traditional-markets)
- Registration Number 55347. The IIGB licence authorizes general insurance "in an innovative manner, including the use of digital assets." — [Docs: Regulatory Framework](https://docs.onre.finance/for-insurers/regulatory-framework)
- **Dan Roberts**, Co-Founder & CEO (X: @onredan). He was previously co-founder & CEO of Nayms. — [OnRe Series A post](https://www.onre.finance/blog/forward-industries-and-rockawayx-co-lead-strategic-investment-in-onre-to-accelerate-onchain-reinsurance-on-solana); [Insurtech Gateway](https://www.insurtechgateway.com/portfolio/onre/)
- **Ayyan Rahman**, Co-Founder & Chief Growth Officer, joined Jun 20, 2025. He was co-founder/COO of Gateway (acquired by Circle), led its $4.2M seed, and later worked at Circle on tokenization. — [OnRe blog](https://www.onre.finance/blog/welcoming-ayyan-rahman-as-co-founder-and-chief-growth-officer-at-onre)
- **Tunde Olowofila**, Head of Reinsurance, joined Jul 28, 2025. He has ~2 decades in reinsurance (London, Bermuda, Dubai) and is the primary BMA underwriting liaison. — [OnRe blog](https://www.onre.finance/blog/welcoming-tunde-olowofila-as-head-of-reinsurance)
- **Ben Fortune**, Chief Underwriting Officer, joined May 12, 2026. He was previously CUO at The Fidelis Partnership (Bermuda), with 9 years at Fidelis from its 2015 founding; before that Leadenhall Capital Partners, Aon, Lockton. At his hire OnRe was "currently managing $170 million". — [OnRe blog](https://www.onre.finance/blog/welcoming-ben-fortune-as-chief-underwriting-officer-at-onre)
- Sarah George is Head of Operations and author of the monthly reviews. — [Aug 2026 review](https://www.onre.finance/blog/onre-in-review-august-2026)
- Insurtech Gateway profile lists **Theodore Georgas (CTO)**, 20 years of software engineering at Deutsche Bank, Merrill Lynch and Lehman Brothers. It also says Nayms was "incubated… in 2018" and "rebranded to OnRe in May 2025". — [Insurtech Gateway](https://www.insurtechgateway.com/portfolio/onre/)
- Nayms→OnRe restructuring: by end-2024 Nayms was "in a pretty bad position". It was "completely restructured… new name, new team, new tech, new investors" and relaunched in May 2025. RockawayX provided "reset funding" and $10M of seed TVL. — [Insurtech Gateway, May 29 2025](https://www.insurtechgateway.com/2025/05/29/insurance-incubator-to-on-chain-reinsurer/)
- Compliance: SOC 2 Type II (Feb 3, 2026) — [OnRe blog](https://www.onre.finance/blog/onre-achieves-soc-2-type-ii-certification-setting-a-new-standard-for-onchain-reinsurance). Apex Group gives monthly NAV/treasury attestations; reports are published for Nov 2025 through Jul 2026. — [Docs: Attestations](https://docs.onre.finance/security-and-verification/independent-attestations)
- Custody: Squads v4 multisig ("Boss Account" 45Ynz…3jaJ5), Clarien Trust (BNY Mellon sub-custody), Coinbase Prime (USYC custody and fiat off-ramp). Allez flags a "single-operator dependency" and notes "the underwriting team controls deal selection and NAV estimation without an external review layer." — [Allez](https://allez.xyz/reports/onre/ONyc_Asset_Risk_Assessment_260731.pdf)

### Inferences
- Regulatory positioning (BMA dual licence plus SAC ring-fencing) is the main moat and scored "AA+" in Allez's regulatory sub-component. A governance/utility token would, however, have to sit outside the regulated insurer's economics, or it risks securities-law questions. The permissionless "Open Access" wrapper that does not touch the regulated entity is a precedent for that kind of separation.

### Gaps
- I could not confirm whether Theodore Georgas is still CTO after the 2025 "new team" restructuring. The Allez report references a "CTO sign-off" without naming the person.
- No headcount disclosed.

---

## Q3. Funding rounds, investors, and strategic partners

### Takeaway
The only disclosed OnRe-era priced round is a **$5M Series A (May 5, 2026)** co-led by **Forward Industries (NASDAQ: FWDI)** and **RockawayX**. Forward also committed up to $25M of ONyc deployment. The May 2025 relaunch was "backed by" Ethena Labs, Solana Ventures/Solana Foundation and RockawayX, with undisclosed amounts. The predecessor Nayms raised about **$12M in total through Apr 2023, including a token sale at an $80M valuation**. It then ran a NAYM public sale in Oct 2024 at $0.05 (implied $50M FDV), and NAYM has since collapsed about 99.9%.

### Cited Findings
- **Series A, May 5, 2026:** "The two firms co-led OnRe's $5 million Series A round. Separately, Forward intends to deploy up to $25 million into ONyc." Proceeds go to scaling underwriting capacity, integrations and team. RockawayX CEO Viktor Fischer: "We seeded OnRe, validated it as an early underwriter, and provided initial liquidity through our credit division, before scaling capital through our curated vaults." Valuation not disclosed. — [OnRe blog](https://www.onre.finance/blog/forward-industries-and-rockawayx-co-lead-strategic-investment-in-onre-to-accelerate-onchain-reinsurance-on-solana); [GlobeNewswire](https://www.globenewswire.com/news-release/2026/05/05/3287676/0/en/forward-industries-and-rockawayx-co-lead-strategic-investment-in-onre-to-accelerate-onchain-reinsurance-on-solana.html)
- DefiLlama raises data lists only: Series A, $5M, 2026-05-05, leads RockawayX and Forward Industries, valuation null. — [DefiLlama API](https://api.llama.fi/protocol/onre)
- **Relaunch, May 21–22, 2025:** "OnRe, Backed by Ethena, Solana Ventures, and RockawayX". Amounts and valuation were not disclosed. — [The Block](https://www.theblock.co/post/355248/solana-backed-onre-taps-ethena-for-first-one-token-and-pool-targets-750-billion-reinsurance-market); [PR Newswire via Manila Times](https://www.manilatimes.net/2025/05/22/tmt-newswire/pr-newswire/onre-backed-by-ethena-solana-ventures-and-rockawayx-launches-structured-yield-product-combining-real-world-stability-and-on-chain-upside/2118717)
- RockawayX published an investment thesis post. — [RockawayX: Why We're Backing OnRe](https://www.rockawayx.com/insights/why-were-backing-onre-real-yield-built-on-chain)
- Solana Compass lists investors as "Solana Ventures, Ethena, RockawayX, Coinbase Ventures, Maven11". — [Solana Compass](https://solanacompass.com/news/onre-surpasses-300m-aum-as-onyc-compounding-interest-rewards-season-1-opens-september-27). Caveat: Coinbase Ventures and Maven11 were **Nayms-era** investors (see below), and I found no OnRe-era announcement naming them.
- **Nayms history:**
  - Jan 2021 seed of £1.5M (~$2–2.1M) led by XBTO with Coinbase Ventures, Maven11, the Synthetix founders and Insurtech Gateway. — [search summary of Bermuda Reinsurance Magazine / Insurtech Gateway](https://www.bermudareinsurancemagazine.com/news/how-nayms-is-set-to-transform-the-cryptocurrency-insurance-space)
  - Jun 2021: $6M for the future NAYM token from XBTO, Maven11, Coinbase Ventures, Spartan, DFG, LD Capital, Cadenza, Woodstock and others. — [Insurtech Gateway, Jun 23 2021](https://www.insurtechgateway.com/2021/06/23/nayms-secures-an-additional-6m/); [Nayms Medium](https://medium.com/nayms/nayms-secures-an-additional-6m-for-future-naym-token-bc698c733c5c)
  - Apr 2023: private token sale led by UDHC (ex-Maker Foundation team), with New Form, Tokentus and Keyrock, at an **$80M valuation**, bringing total raised to **$12M**. — [FinSMEs](https://www.finsmes.com/2023/04/nayms-raises-funding-at-80m-valuation.html); [Nayms Medium](https://medium.com/nayms/nayms-raises-at-80m-valuation-in-a-private-funding-round-led-by-udhc-478340eef2ad)
- **NAYM token:** public sale went live Oct 23, 2024 at **$0.05/token, 3% of supply (30M of 1B)**, which implies a $50M FDV. It is a Base-chain governance token. Per the search summary of CoinGecko and CoinMarketCap pages, it hit an ATH of $0.0436 on Dec 9, 2024 and now trades around $0.00005. — [TradingView/GlobeNewswire, Oct 23 2024](https://www.tradingview.com/news/reuters.com,2024-10-23:newsml_GNXbY3K1j:0-naym-token-public-sale-goes-live-giving-participants-access-to-230-billion-reinsurance-market/); [CoinGecko NAYM](https://www.coingecko.com/en/coins/naym); [CoinMarketCap NAYM](https://coinmarketcap.com/currencies/naym/) (CMC preview page: 1B max supply, 66.12M circulating)
- **Strategic partners and capital allocators:**
  - Ethena: sUSDe was the original collateral. — [launch post](https://www.onre.finance/blog/onre-backed-by-ethena-solana-ventures-and-rockawayx-launches-structured-yield-product-combining-real-world-stability-and-on-chain-upside)
  - RockawayX: curator of the Ethereum "OnRe Core Vault". — [OnRe blog, Jun 3 2026](https://www.onre.finance/blog/onres-uncorrelated-reinsurance-backed-yield-is-now-available-on-ethereum-for-the-first-time)
  - Rhodium Re (Dubai MGA): $150M underwriting delegation, Jan 14, 2026. — [OnRe blog](https://www.onre.finance/blog/onre-delegates-150m-to-middle-east-mga-partner-rhodium-re-to-expand-global-underwriting-distribution-for-onyc)
  - Radix ILS: ~$30M ILS fund-of-fund sleeve. — [Allez](https://allez.xyz/reports/onre/ONyc_Asset_Risk_Assessment_260731.pdf)
  - Perena USD*: inaugural RWA partner, Jan 5, 2026. — [OnRe blog](https://www.onre.finance/blog/onre-partners-with-perena-to-power-usd-with-reinsurance-yield)
  - Elemental: fund/vault and market maker, Feb 11, 2026. — [OnRe blog](https://www.onre.finance/blog/the-elemental-edge)
  - Titan: native NAV minting (Jan 26, 2026) and Liquidity Engine (Sep 24, 2026). — [OnRe blog](https://www.onre.finance/blog/onre-launches-native-minting-on-titan-exchange)
  - Allez Labs: risk partner, Jun 22, 2026. — [OnRe blog](https://www.onre.finance/blog/onre-selects-allez-labs-as-its-independent-risk-partner)
  - Paxos USDG integration, Dec 2, 2025. — [OnRe blog](https://www.onre.finance/blog/onre-integrates-usdg-to-expand-real-world-yield-access-on-solana)

### Inferences
- OnRe-era disclosed equity is tiny ($5M Series A) relative to ~$290–300M AUM. The likely pre-Series A cap-table overhang includes Nayms-era equity and SAFT/token investors (XBTO, Coinbase Ventures, Maven11, UDHC, etc.) and NAYM holders. Any future ONRE token would have to reconcile these legacy claims. Treat that as an **unquantified FDV/unlock risk** and a reputational factor, since the team's prior token lost about 99.9% from its sale price.
- Forward Industries (a listed Solana treasury company) plus RockawayX adds distribution and credibility. A $5M round at an undisclosed valuation implies an equity valuation probably in the tens of millions, but this is speculative.

### Gaps
- No valuation disclosed for any OnRe-era round. Amounts for Ethena and Solana Ventures participation are undisclosed.
- No public statement on how NAYM token holders or Nayms-era token investors are treated in OnRe, or whether they have rights to any future ONRE token.
- Crunchbase and CryptoRank pages were blocked (403).

---

## Q4. TVL / AUM / ONyc supply / market cap / holders over time

### Takeaway
AUM grew from ~$15M (Jul 1, 2025) to a peak of **$302.6M (Sep 21, 2026, OnRe API)**; DefiLlama's TVL peak was **$309.5M on Sep 11, 2026**. On Sep 29, 2026 AUM is **$290.3M** (API) or **$294.8M** (DefiLlama), with **252.3M ONyc** outstanding. TVL rose about 43% over 90 days but only about 3.5% over 30 days. Supply has fallen 4.3% since the Sep 21 peak, the first sustained net outflow. Holders numbered ~8,804 in mid-Sep 2026, and the points leaderboard shows 23,899 wallets.

### Cited Findings
**DefiLlama TVL (category RWA, Solana only, listed 2025-07-14)** — [DefiLlama API](https://api.llama.fi/protocol/onre); [DefiLlama page](https://defillama.com/protocol/onre)
- 2025-07-15 $34.96M; 2025-08-01 $19.39M; 2025-09-01 $24.43M; 2025-10-01 $29.46M; 2025-11-01 $33.68M; 2025-12-15 $51.67M; 2026-01-01 $68.23M; 2026-02-01 $87.08M; 2026-03-01 $116.21M; 2026-04-01 $146.22M; 2026-05-01 $143.86M; 2026-06-01 $191.41M; 2026-07-01 $205.82M; 2026-08-01 $247.56M; 2026-09-01 $287.71M; 2026-09-15 $299.85M; **2026-09-29 $294.77M**.
- Changes to 2026-09-29: 7d −2.6%; 30d +3.5% (from $284.73M); 60d +19.2%; 90d +43.2% (from $205.82M); 180d +101%; 365d +912% (from $29.13M). ATH $309.55M on 2026-09-11.
- DefiLlama flags "misrepresentedTokens: true" and "audits: 0". The audit field is stale versus the docs.

**OnRe API (AUM / circulating supply / NAV)** — [OnRe NAV API](https://core.api.onre.finance/data/nav)

| Date | NAV | AUM ($M) | Supply (M ONyc) |
|---|---|---|---|
| 2025-07-01 | 1.0166 | 15.22 | 14.97 |
| 2025-10-01 | 1.0353 | 29.48 | 28.47 |
| 2026-01-01 | 1.0641 | 73.51 | 69.09 |
| 2026-02-01 | 1.0729 | 92.83 | 86.53 |
| 2026-03-01 | 1.0808 | 116.35 | 107.65 |
| 2026-04-01 | 1.0898 | 140.61 | 129.03 |
| 2026-05-01 | 1.0985 | 157.29 | 143.19 |
| 2026-06-01 | 1.1090 | 183.48 | 165.44 |
| 2026-07-01 | 1.1193 | 205.95 | 184.01 |
| 2026-08-01 | 1.1298 | 246.50 | 218.18 |
| 2026-09-01 | 1.1411 | 280.23 | 245.57 |
| **2026-09-21 (peak)** | 1.1479 | **302.58** | **263.59** |
| 2026-09-29 | 1.1506 | 290.31 | 252.32 |

- Supply change to 2026-09-29: 7d −3.7%; 30d +3.8%; 90d +37.1%; 180d +108%. About 11.3M ONyc (~$13M) was net redeemed between Sep 21 and Sep 29, 2026. That window includes the Liquidity Engine launch (Sep 24) and the Season 1 opening (Sep 27); causality is unknown.

**Official monthly reviews (AUM / DeFi markets / holders / utilization)**
- Oct 2025: AUM $34.76M (+18.03% MoM) — [Oct 2025](https://www.onre.finance/blog/onre-in-review-october-2025)
- Nov 2025: AUM crossed $40M (+22%) — [Nov 2025](https://www.onre.finance/blog/onre-in-review-november-2025)
- Dec 2025: AUM $72.54M (+70.88%); DeFi markets $80.36M; utilization 65.06%; holders 3,588; GWP $6.40M — [Dec 2025](https://www.onre.finance/blog/onre-in-review-december-2025)
- Jan 2026: AUM $92.29M; DeFi $114.54M; holders 4,328; utilization 77.31% — [Jan 2026](https://www.onre.finance/blog/onre-in-review-january-2026)
- Feb 2026: AUM $116.17M; DeFi $178.19M; holders 4,783; utilization 80.53%; GWP $7.49M — [Feb 2026](https://www.onre.finance/blog/onre-in-review-february-2026)
- Mar 2026: AUM $143.1M; DeFi $193.27M; holders 5,429; utilization 88.56%; GWP $10.68M — [Mar 2026](https://www.onre.finance/blog/onre-in-review-march-2026)
- Apr 2026: AUM $143.71M; DeFi $198.09M; holders 5,664; utilization 88.75%; GWP $17.28M — [Apr 2026](https://www.onre.finance/blog/onre-in-review-april-2026)
- May 2026: AUM $185.80M; DeFi $268.46M; holders 6,384; utilization 77.01%; reinsurance capital $112.71M — [May 2026](https://www.onre.finance/blog/onre-in-review-may-2026)
- Jun 2026: AUM $204.48M; DeFi $292.34M; holders 6,692; utilization 79.33%; capital on risk $108.21M; written premium $21.49M — [Jun 2026](https://www.onre.finance/blog/onre-in-review-june-2026)
- Jul 2026: AUM $245.81M; DeFi $357.21M; holders 7,452; utilization 94.65%; capital on risk $154.63M; net premium $32.55M; 29 bound deals; $11.65M yield distributed — [Jul 2026](https://www.onre.finance/blog/onre-in-review-july-2026)
- Aug 2026: AUM $279.84M (+13.84%); "ecosystem TVL crossed $400 million"; "#18 among asset managers globally by RWA value"; ~90% utilization; capital on risk $152.72M; net premium $32.95M; "total bound deals to 28"; $13.51M yield distributed to date — [Aug 2026](https://www.onre.finance/blog/onre-in-review-august-2026)
- Sep 16, 2026: $300M AUM all-time high; ONyc market cap $302M (Sep 17); **8,804 unique holder wallets**; NAV $1.108 (Jun 1) → $1.146 (Sep 16) — [Solana Compass](https://solanacompass.com/news/onre-surpasses-300m-aum-as-onyc-compounding-interest-rewards-season-1-opens-september-27)
- Sep 2, 2026: ONyc is the **#1 RWA on Solana by DeFi Active TVL** (>$225M, ~45% of Solana's ~$507M RWA DeFi active TVL) and #7 across all chains. It has ~$279M "active market cap", second on Solana behind BlackRock BUIDL, with >80% deployed in DeFi. — [OnRe blog](https://www.onre.finance/blog/onyc-is-the-1-real-world-asset-on-solana-by-defi-active-tvl)
- Jan 2026 (older): "OnRe ranks 9th… among Solana RWA protocols by TVL, with $92 million." — [RockawayX guide (search snippet; page later 404)](https://rockawayx.com/insights/the-ultimate-guide-to-onre-2026-reinsurance-yield-meets-defi)

**CoinGecko (2026-09-29 06:14 UTC)** — [CoinGecko ONyc](https://www.coingecko.com/en/coins/onyc)
- Price $1.15; **market cap $105.95M based on a 92.26M "circulating" figure**; **FDV $294.27M** (256.2M total supply); 24h volume $2.51M; ATH $1.17; ATL $1.005; rank #276. Categories: Solana Ecosystem, RWA, Yield-Bearing Stablecoin.
- Caveat: CoinGecko's circulating supply (92M) disagrees with OnRe's API (252M), probably because it excludes venue/contract holdings. FDV ≈ AUM is the meaningful number.

**Holder concentration (Allez, Jul 31, 2026)** — [Allez](https://allez.xyz/reports/onre/ONyc_Asset_Risk_Assessment_260731.pdf)
- 7,426 direct addresses and 7,798 look-through entities. The Kamino reserve vault holds **52.6%** of supply, Exponent contracts 16.7%, Loopscale 14.7%.
- Look-through concentration: largest entity 15.8%, top-10 48.8%, top-50 72.2%, top-100 81.1%, Gini 0.977. 5,749 entities with under $1K each hold ~0.2% of supply.
- Holder-count discrepancy: Allez says 6,461 in June, while OnRe's June review says 6,692.

### Inferences
- Growth rate is decelerating. Monthly AUM growth was +20–26% through spring 2026, fell to +13.8% in August, and reversed to roughly −3% from Sep 21 to Sep 29. The Kamino market cap raise (150M ONyc) and the new "compounding interest" rewards look like attempts to re-accelerate or retain capital.
- For FDV benchmarking, use AUM ≈ $290–300M, cumulative yield distributed ≈ $13.5M (Aug 2026), and annualized net premium of ~$33M (Aug 2026 NWP figure). OnRe's own revenue take is not disclosed.

### Gaps
- rwa.xyz, Dune (dune.com/onre_finance/transparency-dashboard), Solscan and Artemis were not queried directly. The OnRe API and DefiLlama served as primary series.
- The Aug review's "28 bound deals" is inconsistent with July's "29". Yield-distributed figures are also inconsistent: May says $16.83M "cumulative", while Jun, Jul and Aug report $8.75M, $11.65M and $13.51M. Definitions probably changed.

---

## Q5. Integrations and cross-chain expansion

### Takeaway
ONyc is deeply integrated in Solana DeFi. Kamino is the core venue (about 53% of supply), followed by Loopscale, Exponent (PT/YT plus senior/junior risk tranching), Orca/Raydium/Meteora DEX pools, RateX, Carrot, Titan and the Jupiter routers. Cross-chain reach so far is a single Ethereum USDC vault (Accountable + RockawayX, via Chainlink CCIP). Positions stay on Solana, and there is no native ONyc on EVM.

### Cited Findings
- Timeline from the OnRe blog index — [OnRe blog](https://www.onre.finance/blog):
  - Orca DEX pool (Jun 5, 2025); Chainlink NAV (Jul 10, 2025)
  - Kamino (Aug 5, 2025); Loopscale vault (Aug 20, 2025); Kamino Multiply (Aug 21, 2025)
  - Exponent (Sep 4, 2025); points program (Sep 11, 2025); Global Access permissionless flow (Oct 1, 2025)
  - RateX (Oct 16, 2025); JitoSOL×ONyc (Oct 20, 2025); USDG (Dec 2, 2025); Carrot Boost (Dec 31, 2025)
  - Perena USD* (Jan 5, 2026); Titan native minting (Jan 26, 2026); Elemental vault (Feb 11, 2026)
  - Exponent v2 fixed-rate and auto vaults (May 29, 2026); Ethereum Core Vault (Jun 3, 2026); Exponent risk tranching srONyc/jrONyc (Jun 24, 2026)
  - Titan Liquidity Engine (Sep 24, 2026)
- Kamino, one-year stats (Aug 4, 2026): $205.58M total market; $130.5M ONyc collateral (31.9% of Kamino's RWA collateral); $70.85M borrowed across 2,594 loans; 2,254 active users; $1.33B cumulative volume; capacity 2M → 120M ONyc; "53% of OnRe protocol AUM is deployed on Kamino". Max LTV 66% (2.9x). Average first-year supply APY: USDC 6.09%, USDG 8.29%. — [OnRe blog](https://www.onre.finance/blog/the-onre-market-on-kamino-one-year-of-reinsurance-as-productive-collateral)
- Aug 31, 2026: the OnRe Market on Kamino passed $250M total size with >$160M ONyc supplied, and the cap was raised to 150M ONyc. Exponent ONyc market passed $40M deposits and became the "second largest holder of ONyc". Tranching cap raised from $4M to $10M. Loopscale OnRe deposits passed $90M, and srONyc became live as collateral. — [Aug 2026 review](https://www.onre.finance/blog/onre-in-review-august-2026)
- Sep 2, 2026 deployment: Kamino $166.6M, Loopscale $49.3M, Exponent $6.4M, plus Orca/Raydium and others. — [OnRe blog](https://www.onre.finance/blog/onyc-is-the-1-real-world-asset-on-solana-by-defi-active-tvl)
- Ethereum: "OnRe Core Vault", curated by RockawayX and verified by Accountable. It takes USDC on Ethereum, routes it via Chainlink CCIP, and keeps "all underlying positions… on Solana". It targets 11–13% gross USDC APY and earns 4x OnRe points. — [OnRe blog, Jun 3 2026](https://www.onre.finance/blog/onres-uncorrelated-reinsurance-backed-yield-is-now-available-on-ethereum-for-the-first-time)
- Docs FAQ: "OnRe currently operates on Solana." — [Docs FAQ](https://docs.onre.finance/technical-resources/frequently-asked-questions)
- DEX liquidity (Jul 31, 2026): Orca ONyc-USDC is "in practice, the only pool with real two-sided depth". Raydium USDG-ONyc holds $3.04M TVL but shows $0 usable depth; Orca ONyc-jitoSOL and Meteora ONyc-USDC are dormant. Market maker Elemental's wallet dominates concentrated liquidity. — [Allez](https://allez.xyz/reports/onre/ONyc_Asset_Risk_Assessment_260731.pdf)

### Inferences
- Exponent is a major ONyc venue. The PT/YT markets (ONYC-JAN2027 and SRONYC-JAN2027 appear in the points API) are where points-speculation is priced; YT earns 5x points per the docs. This matters for the parent project's YT-Exponent analysis.

### Gaps
- Drift and Jupiter Lend integrations: no evidence found. Jupiter appears only as a secondary-liquidity router.

---

## Q6. Official statements on a governance/utility token, points, seasons, airdrop, TGE

### Takeaway
OnRe **officially referenced a "$ONRE protocol token" at launch (May 2025)**, and The Block reported that depositors would get "allocation in the eventual ONRE token". Since then, **no tokenomics, allocation or TGE date has been published** (as of 2026-09-29). The docs say points "do not represent any entitlement to tokens". A new "ONyc Compounding Interest Rewards Season 1" opened Sep 27, 2026 for positions held 60+ days; its full mechanics were "expected in the lead-up". Community sites describe any airdrop as unconfirmed.

### Cited Findings
- May 21, 2025 official launch post: "In bullish conditions, elevated on-chain funding rates and token incentives from sUSDe and the **$ONRE protocol token** offer meaningful upside potential." Projected returns of "up to 40.35%" included "token incentives". — [OnRe blog](https://www.onre.finance/blog/onre-backed-by-ethena-solana-ventures-and-rockawayx-launches-structured-yield-product-combining-real-world-stability-and-on-chain-upside)
- The Block (May 21, 2025): depositors receive "incentives and allocation in the **eventual ONRE token**". ONe was projected at ">30%" in bull markets and "~8%" in bear markets. — [The Block](https://www.theblock.co/post/355248/solana-backed-onre-taps-ethena-for-first-one-token-and-pool-targets-750-billion-reinsurance-market)
- Dec 30, 2025 "2026 Outlook" (official): "governance and utility tokens are forced to earn their place. Tokens tied to allocation, risk decisions, and real economic control matter. Tokens that exist purely for narrative don't." — [OnRe blog](https://www.onre.finance/blog/2026-outlook)
- Points program launched Sep 11, 2025 with multipliers 1x hold, 2x LP, 3x lend, 4x YT. Ayyan Rahman: "This isn't about short-term incentives." — [OnRe blog](https://www.onre.finance/blog/onre-introduces-points-program-rewarding-onyc-participation-across-defi)
- Current docs:
  - "Points have no monetary value, are not transferable, and do not represent any entitlement to tokens, assets, or financial rewards… your standing may influence future benefits, incentives, and program rewards at OnRe's discretion."
  - Current multipliers: Hodl 1x; LP 2x; Lend/Deposit 3–4x; **Yield Tokens 5x**; Loop/Leverage 6x. PTs earn no points.
  - Referrals: +10% to the referrer, +5% to the referee. "Points Are Never Clawed Back."
  - Public API: rewards.api.onre.finance. — [Docs: OnRe Points Program](https://docs.onre.finance/onyc-in-defi/onre-points-program)
- Campaigns:
  - Oct 1–16, 2025 Global Access launch: 10x on Oct 1, then 3x daily. — [OnRe blog](https://www.onre.finance/blog/introducing-onyc-global-access-the-permissionless-path-to-onchain-institutional-yield)
  - Oct 2025 totals: "12,325,124 points earned through the 10x Launch campaign; 151,431,377 points through the 3x Daily Multiplier." — [Oct 2025 review](https://www.onre.finance/blog/onre-in-review-october-2025)
  - Aug 2026: "New maturities for ONyc and srONyc went live with limited-time points boosts." — [Aug 2026 review](https://www.onre.finance/blog/onre-in-review-august-2026)
- **Points leaderboard snapshot (pulled 2026-09-29 from the public API):** 23,899 wallets; **~240.9B total points**. Top 1 wallet holds 8.1%, top 10 27.4%, top 100 52.3%, top 1,000 84.7%, top 5,000 98.4%. Median wallet has ~72K points. 345 wallets have ≥100M points and 23 have ≥1B. — [OnRe Points API](https://rewards.api.onre.finance/api/v1/points/leaderboard?page=0&size=20)
- **Season 1 (Sep 2026):** "ONyc Compounding Interest Rewards Season 1 opening September 27 for positions maintained 60 days or longer." "Full mechanics and reward rates for Season 1 are expected in the lead-up to the start date." The 60-day threshold is meant "to reward capital that stays committed through an underwriting cycle." Solana Compass notes "No airdrop, TGE, or governance token mentioned." — [Solana Compass, Sep 16–17 2026](https://solanacompass.com/news/onre-surpasses-300m-aum-as-onyc-compounding-interest-rewards-season-1-opens-september-27). I could not find this on the OnRe blog or docs; it is probably an X announcement.
- Third-party status checks:
  - MEXC blog (May 12, 2026): "No official $ONRE token launch details, total supply, or TGE timeline have been announced as of April 2026." — [MEXC](https://blog.mexc.com/token-reviews/onre-airdrop-2026-how-to-earn-onre-by-depositing-into-the-worlds-first-on-chain-reinsurance-protocol-on-solana/)
  - airdrops.io (updated Jul 18, 2026): "OnRe has not explicitly confirmed that points will lead to a token airdrop." — [airdrops.io](https://airdrops.io/onre/)
  - A community "OnRe Airdrop Calculator" exists (by @heronjr_x) with no stated assumptions. — [onrepoints.xyz](https://www.onrepoints.xyz/)
- **Unverified rumor:** one search-engine summary said "5% of FDV is allocated to points distribution". I could not trace this to any OnRe source; the likely origin, airdropbee.com, was bot-blocked. Treat it as unconfirmed.
- Podcasts found:
  - 0xResearch (Blockworks), "Why Reinsurance Could Become DeFi's Best Collateral", with Ayyan Rahman and Ryan Connor (RockawayX), ~late Sep 2026. — [Apple Podcasts](https://podcasts.apple.com/us/podcast/0xresearch/id1651683074)
  - Solana is Global with Alex Scott, featuring Ayyan Rahman. — [Solana podcasts](https://solana.com/podcasts/solana-is-global-with-alex-scott/episodes/dc245817-8063-4c7c-bf3d-562143d7734b)
  - I did not obtain transcripts, so token remarks in these episodes are unknown.

### Inferences
- The token has been signalled since May 2025 ("$ONRE protocol token" / "eventual ONRE token"), and the points program has now run for ~12.5 months. However, OnRe's messaging since late 2025 has leaned "real yield, not emissions", and the docs legally disclaim any token entitlement.
- The new "Season 1" is a compounding *interest* reward with a 60-day hold requirement, not a points season. That suggests OnRe is experimenting with cash/ONyc-denominated retention incentives, which could delay a TGE or be structured as pre-TGE loyalty. It is unconfirmed either way.
- A 60-day minimum hold starting Sep 27, 2026 means the first qualifying date is about Nov 26, 2026. It also coincides with the end of the Atlantic hurricane season (Nov 30). A TGE before end-Nov 2026 would sit awkwardly with that framing; this is speculative.
- Precedent: the same CEO previously launched a governance token (NAYM, Oct 2024) that collapsed. The team may be cautious, and the market may apply a discount.

### Gaps
- I could not access OnRe's X posts (@onrefinance, @onredan) directly. The exact Season 1 announcement wording and any follow-up details after Sep 27 are unknown.
- No official tokenomics, supply, allocation or vesting.

---

## Q7. Key risks: reinsurance loss exposure, NAV drawdowns, concentration, smart contracts, audits, regulation

### Takeaway
ONyc has **never paid a catastrophe claim** (429 days to Jul 31, 2026; one $142K specialty claim). The 2026 Atlantic season has been exceptionally quiet so far (as of Sep 14: 5 named storms, 0 hurricanes, ACE ~93% below normal). The tail is real, though: Allez models a **Sandy-grade event at −13.1% to −22.1% of NAV** and a 2017-style season at about −16%. The main non-cat risks are:
- the Kamino/Loopscale leverage cascade on thin DEX depth;
- multisigs with no timelock;
- self-reported NAV and deal selection;
- USDG concentration;
- holder concentration.

Smart contracts have been audited 6 times (Quantstamp ×4, Ackee, OtterSec), and an Immunefi bounty of up to $100K is live.

### Cited Findings
**Loss history and cat exposure**
- "The vault has now run 429 days without a peg break or a reinsurance claim paid to date." Claims paid to Jun 30, 2026: $142K on one specialty financial-loss policy against $153K premium (~93% loss ratio); "$0 catastrophe". Four closed treaties (~$12.7M exposure) realized full NWP with zero claims. — [Allez](https://allez.xyz/reports/onre/ONyc_Asset_Risk_Assessment_260731.pdf)
- Portfolio mix (Jul 31, 2026, by deal type): Retrocession XoL 36.0%; direct XoL 32.3%; ILS fund (Radix, North American perils, ~$30M) 18.2%; ILW 9.6% (Japan, USA, Australia+USA); Contingency (European lottery) 4.0%. By region: Worldwide/multi-peril 52.1%, USA/North America 40.4%, Europe 4.0%, Australia 2.0%, Japan 1.5%. — [Allez](https://allez.xyz/reports/onre/ONyc_Asset_Risk_Assessment_260731.pdf)
- Docs say the book targets "roughly a 50/50 split" between specialty programs and property-cat ILWs. — [Docs: Portfolio Makeup](https://docs.onre.finance/reinsurance-framework/portfolio-makeup). This conflicts with the Allez snapshot, which is dominated by XoL/retro cat layers.
- Stress: "Hurricane Sandy… produces a Sandy-grade NAV impact in the −13.1% to −22.1% range, with XL 5 (Wind & EQ, USA) alone contributing −8.1% at its full $20.0M limit." A "2017-style scenario at 80% utilization produces a ~−16% drawdown"; concentrated ILS funds lost 20–40% in 2005 and 2017. "The tail is not bounded without a full observed cat cycle." — [Allez](https://allez.xyz/reports/onre/ONyc_Asset_Risk_Assessment_260731.pdf)
- Only one XoL deal carries a reinstatement (a single one at 100%). Several deals had "TBD expected loss ratios" (an open item). — [Allez](https://allez.xyz/reports/onre/ONyc_Asset_Risk_Assessment_260731.pdf)
- Docs risk appetite: "Reducing loss probability to ~0.5%." — [Docs: Claims & Risk Management](https://docs.onre.finance/reinsurance-framework/claims-and-risk-management)
- 2026 season (official, Sep 14, 2026): "As of September 14, the Atlantic had produced five named storms and no hurricanes. Accumulated Cyclone Energy (ACE) stood at 4.4, approximately 93% below the 1991-2020 normal." "During the first half of 2026, $46 billion of insured natural catastrophe losses occurred." — [OnRe blog](https://www.onre.finance/blog/managing-catastrophe-risk-through-peak-peril-season)
- The FAQ describes a "4-layer" loss framework: reserves, then "APY absorption" ("adjustment happens in yield, not principal"), then cross-contract support, then the reserve buffer. — [Docs FAQ](https://docs.onre.finance/technical-resources/frequently-asked-questions). This conflicts with Allez: "a major cat loss would compress NAV by the net claims paid."

**DeFi / liquidity risk**
- DEX sell-side depth of ~$2.14M at 2% slippage against $166.6M of ONyc posted as lending collateral (Kamino $130.2M, Loopscale $36.4M). Kamino book LTV ~54.4%, and the book is "more concentrated near its liquidation threshold than it was" in June. In a Sandy-grade cascade (−20% NAV) the combined liquidations sell $17.27M of collateral against a $37.12M liquidity layer (2.15x coverage). Bad debt stays zero to −30% NAV and reaches $3.30M beyond that. — [Allez](https://allez.xyz/reports/onre/ONyc_Asset_Risk_Assessment_260731.pdf)
- ONyc absorbed "four DeFi-side stress events without issue, including the April 2026 Kelp DAO incident." In Nov 2025, "ONyc held its peg to NAV" during a broad crypto drawdown, helped by ~$4M of buybacks that month. — [Allez](https://allez.xyz/reports/onre/ONyc_Asset_Risk_Assessment_260731.pdf); [Nov 2025 review](https://www.onre.finance/blog/onre-in-review-november-2025)

**Smart contract / governance**
- Audits: Quantstamp Offer & Redemption spec (Apr 2025; certificate URL still carries "nayms-on-re"); Quantstamp OnRe Solana program (May 2025); Quantstamp diff review (Sep 2025); Ackee (Nov 2025); Quantstamp re-audit v3 (Jan 2026); **OtterSec OnRe App Solana (Aug 2026)**. HT Digital Ltd audited the FY2025 financial statements (Sep 2025). — [Docs: Independent Audits](https://docs.onre.finance/security-and-verification/independent-audits)
- Immunefi bug bounty, up to $100K for critical bugs (May 11, 2026). — [OnRe blog](https://www.onre.finance/blog/onre-launches-bug-bounty-program-with-immunefi)
- Governance keys: mint authority is a program PDA ("no unilateral EOA mint possible"). Program upgrade authority and freeze authority sit with two Squads v4 **3-of-6** multisigs; "time_lock = 0 on both multisigs, verified July 31"; a timelock is "in progress and road-mapped". A sixth audit (buffer yield pool, MarketStats PDA) was still in progress on Jul 31. — [Allez](https://allez.xyz/reports/onre/ONyc_Asset_Risk_Assessment_260731.pdf)
- Allez overall rating: "High Quality Collateral" (Jul 31, 2026). The docs also cite an initial overall **A−** with a Regulatory sub-rating of **AA+**. Weaker areas: Liquidity Infrastructure, Stress Performance, Centralization and Incident Response were all rated "Adequate". — [Docs: Independent Risk Analysis](https://docs.onre.finance/security-and-verification/independent-risk-analysis); [Allez](https://allez.xyz/reports/onre/ONyc_Asset_Risk_Assessment_260731.pdf)

**Concentration / counterparty / regulatory**
- USDG made up ~31% of AUM on Jul 31, 2026 (a dependency risk). About 90.5% of AUM was documented (~50% verified on-chain by Allez, ~40% attested by custodians or third parties). — [Allez](https://allez.xyz/reports/onre/ONyc_Asset_Risk_Assessment_260731.pdf)
- About 53% of supply sits in Kamino, and the look-through top-10 entities hold 48.8% (see Q4). — [Allez](https://allez.xyz/reports/onre/ONyc_Asset_Risk_Assessment_260731.pdf)
- Regulatory: institutional ONyc is "intended for eligible accredited investors", and an excluded-jurisdictions list exists. — [Docs: Excluded Jurisdictions](https://docs.onre.finance/legal/onyc-excluded-jurisdictions). The permissionless "Open Access" route "does not involve interaction with OnRe's regulated entities". — [Docs](https://docs.onre.finance/for-capital-providers/open-access-vs-institutional-access)

### Inferences
- **Hurricane-season timing matters for TGE:** the Atlantic season runs through Nov 30, 2026 and has been benign so far. Several cat layers (the Radix sleeve's obligations "pass before end of 2026") release risk in Q4 2026. A TGE after the risk period closes, i.e. Dec 2026 or later, would let OnRe show a clean second season. This is speculative.
- A single US wind/quake event at the level of Sandy (~$19B PCS) could cut NAV by double digits. It would also trigger Kamino/Loopscale liquidations with thin DEX exits. That would damage both ONyc TVL and any token valuation, which makes the protocol's TVL a fat-tailed input for FDV.

### Gaps
- I could not read the Apex attestation PDFs (Google Drive) or the full reinsurance deals table (rendered as an image in the docs).
- No realized loss event yet exists to calibrate the actual NAV-response mechanics, so there is a conflict between the FAQ's "yield not principal" framing and Allez's "NAV compresses" framing.
