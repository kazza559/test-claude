# Axis (axis.to): project fundamentals as of 2026-09-28

Scope note: "Axis" here means the quantitative-yield / synthetic-dollar protocol at axis.to (X: @AxisFDN; issuer of USDx and sUSDx on Ethereum). It is a different project from Axis Finance (auctions), Axie Infinity/AXS, Axis Robotics (an AI data-task airdrop project), AXiS ALiVE (an unrelated "AXIS" ticker on CoinGecko), and Stables Labs "USDX" (a different synthetic dollar that de-pegged in Nov 2025). All on-chain numbers below were pulled by me on 2026-09-28 (Ethereum block ~26,075,763) unless another date is given.

## 1. What exactly is Axis? (product, mechanism, collateral, custody, chains, redemption, peg)

### Takeaway
Axis is a Singapore-based (Coordinate Labs Pte. Ltd.) team that runs a CEX-heavy market-neutral arbitrage book. It sells access to that book through two Ethereum tokens: USDx, a synthetic dollar that pays no yield on its own, and sUSDx, an ERC-4626/7540 staking vault that pays the yield. It works like Ethena, but the yield comes from multi-strategy arbitrage (cross-venue, cross-currency, funding, OTC) instead of a pure perp basis trade. The backing sits off-chain on exchanges and is not held off-exchange. Its own docs say plainly that "USDx is not a stablecoin." There is no Axis token yet.

### Cited Findings
**Identity and entity**
- Axis describes itself as "a global liquidity provider for tokenized markets" that uses "proprietary high-frequency trading systems" to capture arbitrage and stream profits to token holders. Products listed on the homepage: USDx, the Origin Vault, BTCx and GOLDx ("coming soon") and Axis Prime (institutional liquidity) — [axis.to homepage, fetched 2026-09-28](https://axis.to/)
- CoinGecko's description names the operating company as "Coordinate Labs Pte. Ltd. in Singapore" — [CoinGecko API, coins/axis-usd, fetched 2026-09-28](https://www.coingecko.com/en/coins/axis-usd)
- The team started Axis in 2025. It had previously run the same strategy as a proprietary firm (2018–2021) and then as a licensed fund with outside LPs (2022–2025). In 2025 the team "redeemed its LPs" and moved to a protocol — [docs: Origin, fetched 2026-09-28](https://docs.axis.to/start-here/origin.md); [docs: Track Record](https://docs.axis.to/susdx-the-rewards-vault/how-axis-earns-yield/historical-track-record.md)

**Tokens**
- **USDx ("Axis Dollar")** is an upgradeable ERC-20 at `0xa1fA7777974312f7d801A8880714a218F76233f8` on Ethereum. The docs call it a "dollar-denominated, over-collateralized synthetic dollar". Holding it earns nothing — [docs: What is USDx?](https://docs.axis.to/usdx-the-synthetic-dollar/usdx.md); [docs: Contract Addresses](https://docs.axis.to/reference/contract-addresses.md)
- **sUSDx ("Axis Rewards Vault")** is an ERC-4626 vault with ERC-7540 async redemption at `0xEB892628D1E58BC475A6dCB7F5dBC4F591632AA4`. Rewards arrive as USDx through `fundRewards` and vest linearly — [docs: Stake & Unstake](https://docs.axis.to/susdx-the-rewards-vault/stake-and-unstake.md)
- **ogUSDx** was the receipt token for the Origin Vault pre-deposit, hosted on Upshift. When the vault matured, deposits were "used to mint USDx and automatically stake half of it" — [Axis insight "How the Origin Vault Works", 2026-07-23](https://axis.to/insights/How-the-Origin-Vault-Works)
- **BTCx and GOLDx** are announced as "coming soon" but have not launched — [The Axis Roadmap, 2026-07-10](https://axis.to/insights/The-Axis-Roadmap)
- **Legacy V1 on Plasma** (private beta): `AxisUSD` at `0xA1FA77779e6866fa3eF48FC0720657E042158387`, plus StakedAxisUSDV2 and others. The docs mark it "deprecating" and say it serves existing beta holders only. The docs also warn that the V1 and V2 addresses share their first 8 hex characters — [docs: Contract Addresses](https://docs.axis.to/reference/contract-addresses.md)

**Yield source**
- The docs name four trading categories: cross-venue arbitrage, cross-currency arbitrage, funding-rate arbitrage and OTC/RFQ. They add: "Funding is one component (and can be the larger share in a given period)". The docs also say "None of these return sources is risk-free" — [docs: Welcome](https://docs.axis.to/readme.md); [docs: What is Axis?](https://docs.axis.to/start-here/what-is-axis.md)
- The two sources contradict each other on funding rates. The Origin Vault FAQ says "Our strategy does not rely on funding rates, we profit from spot price dislocations" — [docs: Origin Vault](https://docs.axis.to/origin-vault/origin-vault.md). The core docs say funding "can be the larger share in a given period" — [docs: What is Axis?](https://docs.axis.to/start-here/what-is-axis.md)
- Reported venue concentration: a third-party review quotes Binance 19.8%, Bybit 13.5% and Upbit 13.3% of exposure, taken from Axis data-room material — [Axis × Turtle.Club review (HackMD, by "Manna nebesnaya × Codex"), 2026-07-29](https://hackmd.io/@DoMnolkQRGOjIqhl46A13A/rJ59uLvSfx)
- The docs say realized profits are either kept in reserves (to build over-collateralization) or paid into the sUSDx vault, and "The split is a decision, not a formula" — [docs: Reward Distribution](https://docs.axis.to/susdx-the-rewards-vault/reward-distribution.md)

**Collateral and custody**
- The backing is "digital and tokenized assets first, plus traditional assets, plus the corresponding futures and hedge positions". Spot assets are "held at centralized liquidity venues (exchanges and trading venues) rather than in onchain custody". The docs state: "Axis does **not** currently use off-exchange settlement or off-exchange custody" — [docs: Backing, Custody & Transparency](https://docs.axis.to/backing-reserves-and-transparency/backing-custody-transparency.md)
- USDC and USDT are the accepted mint collateral on Ethereum. A custodian deposit address `0x0D04…F519` is registered, and on 2026-09-28 it held 0 USDx — [docs: Contract Addresses](https://docs.axis.to/reference/contract-addresses.md); [my RPC query, 2026-09-28](https://etherscan.io/address/0x0D0491260f18281CA59EF110F907fA69dA0FF519)
- The homepage lists Fireblocks and Fordefi for custody, and Chainlink and Accountable for on-chain attestations — [axis.to, fetched 2026-09-28](https://axis.to/)

**Chains**
- Ethereum mainnet only for V2. The docs say "Token contracts on chains other than Ethereum are not yet deployed" — [docs: Contract Addresses](https://docs.axis.to/reference/contract-addresses.md)
- The Dec 2025 funding PR had promised a launch on Plasma and Ethereum — [The Block, 2025-12-03](https://www.theblock.co/post/381215/axis-5-million-usd-round-galaxy-ventures-onchain-yield-protocol-usd-bitcoin-gold). Plasma now hosts only the deprecating V1 beta.

**Mint and redeem**
- Only whitelisted "approved counterparties" can mint or redeem directly. Individuals must pass accredited-investor checks. The minimum is US$1,000,000, onboarding takes about 2 weeks, and US persons and sanctioned jurisdictions are excluded. Everyone else has to buy USDx on the secondary market — [docs: Eligibility & Onboarding](https://docs.axis.to/resources-and-legal/eligibility-and-onboarding.md); [docs: FAQ](https://docs.axis.to/resources-and-legal/faq.md)
- Orders are signed EIP-712 messages that a KMS-secured operator settles. "There is no onchain oracle: settlement trusts the operator-signed minimum output amount" (from the OpenZeppelin scope notes) — [docs: Audit Reports](https://docs.axis.to/backing-reserves-and-transparency/audits.md)
- Indicative redemption fees:

  | Option | Target fee | Max fee |
  |---|---|---|
  | Instant, up to 2% of the book per day | 10 bps | 30 bps |
  | 7d, aggregate redemptions ≤10% | 10 bps | 15 bps |
  | 7d, aggregate >10–50% | 10–18 bps | 25 bps |
  | 7d, aggregate >50–100% | 18–35 bps | 50 bps |

  — [docs: USDx Primary Market](https://docs.axis.to/usdx-the-synthetic-dollar/mint-and-redeem.md)
- Unstaking sUSDx has a 7-day cooldown (a governance-set parameter), after which a protocol `REDEMPTION_SERVICER_ROLE` must service the request — [docs: Stake & Unstake](https://docs.axis.to/susdx-the-rewards-vault/stake-and-unstake.md)
- USDx has pause and address-restriction (freeze) roles. The docs say restricted funds are "frozen, never seized" — [docs: What is USDx?](https://docs.axis.to/usdx-the-synthetic-dollar/usdx.md); [docs: Governance](https://docs.axis.to/technical-and-architecture/governance.md)

**Peg history**
- CoinGecko data for USDx: price $0.999285 on 2026-09-28. All-time high $1.002 (2026-09-04, the day the Origin Vault lock expired). All-time low $0.99614 (2026-09-15, during the post-lock outflows). No material de-peg is recorded. The only CoinGecko tickers are Curve USDx/USDT and sUSDx/USDx, with ~$0.3M of 24h volume — [CoinGecko API coins/axis-usd, fetched 2026-09-28](https://www.coingecko.com/en/coins/axis-usd)
- A Foresight News piece reposted by WEEX says "USDX synthetic fell below $0.60 in November 2025". That event was **Stables Labs USDX**, a different protocol with 0 TVL on DefiLlama, not Axis. Axis USDx V2 did not exist in Nov 2025 — [WEEX/Foresight News, 2026-07-31](https://www.weex.com/news/detail/why-is-axiss-arbitrage-story-attractive-filling-50-million-in-22-hours-bmt0wyj8yfr851h4t17bcnuq); [DefiLlama API /protocols, "Stables Labs USDX" listing, fetched 2026-09-28](https://api.llama.fi/protocols)

### Inferences
- Economically, sUSDx is closer to a tokenized share of a CEX-based market-neutral fund than to a stablecoin. The HackMD review draws the same conclusion ("closer to a stake in a crypto market-neutral fund"). The counterparty profile resembles Ethena's before off-exchange settlement, and is arguably worse: Axis has no off-exchange custody, and part of its book sits on regional venues such as Upbit.
- Only approved counterparties can mint or redeem, with a $1M minimum. For retail holders, the peg therefore rests on Curve liquidity (~$5M across the two Curve pools) plus a small group of arbitrageurs. That is thin if there is ever a run.
- Because the team decides how much profit goes to the vault, the sUSDx rate is a managed number. The team could lift it during a points season.

### Gaps
- I could not see the live Transparency Dashboard (app.axis.to/transparency) or the Accountable proof-of-solvency page. The app is geo-blocked for US IPs, and the Accountable page returned only a header. So I have no current collateralization ratio, reserve breakdown or venue breakdown.
- I found no current, dated split of how much yield comes from funding versus spot arbitrage.

## 2. Team and backers

### Takeaway
The team is named and credible. Its core is the Korean quant fund Alphanonce (CEO Chris Kim, CIO Changsung Kim, CTO Justin Im), plus Velodrome co-founder Jimmy Xue as COO and ex-Tether/Ondo/Maple BD lead Ashwin Khosa. The only public round is a $5M private round in Dec 2025, led by Galaxy Ventures and described as 4x oversubscribed. The valuation was not disclosed. That is small next to Ethena, Usual, Resolv or Falcon, and implies a low VC cost basis.

### Cited Findings
- **Chris Kim**, co-founder and CEO: "Co-founded Alphanonce and was first hire at QCP Capital. Built a hedge fund and OTC desk from the ground up." — [axis.to/about, fetched 2026-09-28](https://axis.to/about); [LinkedIn](https://sg.linkedin.com/in/chriskyk)
- **Jimmy Xue**, co-founder and COO: "Co-founded Velodrome… Started at Blackstone in advanced analytics." — [axis.to/about](https://axis.to/about)
- **Ashwin Khosa**, co-founder and CSO: senior revenue/partnerships roles at "Tether, Ondo and Maple… over 7 years since 2018." — [axis.to/about](https://axis.to/about)
- **Changsung Kim**, CIO and co-founder: co-founded Alphanonce, previously at Trexquant. **Justin Im**, CTO: former Alphanonce CTO and early Upbit engineer. **Hyeonshik Ji**, Head of Operations: Alphanonce FinOps, previously PwC and Deloitte — [axis.to/about](https://axis.to/about)
- Claimed Alphanonce record: "36% annualized historical returns, 4.9 Sharpe, $400M peak AUM" — [axis.to](https://axis.to/); [The Axis Roadmap, 2026-07-10](https://axis.to/insights/The-Axis-Roadmap)
- The docs give 360.7% cumulative gross return over 77 months (Jul 2018–Dec 2024), with annual returns of 39.2% (2020), 37.5% (2021), −7.0% (2022), 17.9% (2023) and 27.0% (2024). The worst month was −10.3% (May 2022). The figures are gross of fees, with "no net-of-fees figure… published", and 2025 monthly data is "not published… pending reconciliation" — [docs: Track Record](https://docs.axis.to/susdx-the-rewards-vault/how-axis-earns-yield/historical-track-record.md); [docs: 2018–2025 Composite](https://docs.axis.to/susdx-the-rewards-vault/how-axis-earns-yield/historical-track-record/long-run-composite.md)
- **Funding round**: $5M private round announced 2025-12-03 and led by Galaxy Ventures. Participants were OKX Ventures, CMT Digital, FalconX, GSR, Maven 11, CMS Holdings and Marc Zeller (Aave Chan Initiative). The round was "four times oversubscribed" and no valuation was disclosed. At that point Axis said $100M of LP capital had been deployed in a closed beta and cited a 4.9 Sharpe — [The Block, 2025-12-03](https://www.theblock.co/post/381215/axis-5-million-usd-round-galaxy-ventures-onchain-yield-protocol-usd-bitcoin-gold); [RootData news](https://www.rootdata.com/news/449508)
- OKX Ventures confirmed publicly that it backed @AxisFDN as an early investor — [OKX Ventures on X, 2025-12-03](https://x.com/OKX_Ventures/status/1996206746470395973)
- The docs FAQ lists backers as "Galaxy, OKX, FalconX, CMT Digital, and Steakhouse". Steakhouse does not appear in The Block's list, so it may be a later or strategic addition — [docs: FAQ](https://docs.axis.to/resources-and-legal/faq.md). The Telegram channel also names Serotonin, a marketing and advisory firm, among partners — [t.me/s/AxisFDN, fetched 2026-09-28](https://t.me/s/AxisFDN)

### Inferences
- A $5M raise at an undisclosed valuation (plausibly a sub-$100M post-money seed) gives VCs a low cost basis. At any meaningful token FDV they would be deep in profit, which is a potential source of sell pressure after unlocks.
- The Alphanonce record is self-reported and gross of fees. The monthly data stops in Dec 2024, and the 2025 months are held back "pending reconciliation", which is a mild red flag. The 36% annualized figure also came from a much smaller, private book than a public $1B vault would be.

### Gaps
- I found no valuation, token warrant or token-allocation terms for the seed round. The CryptoRank ICO page returned HTTP 403, and I did not access Crunchbase or Messari.
- I found no second or strategic round beyond the $5M.

## 3. Traction: TVL, supply, APY, holders, integrations

### Takeaway
Traction is modest. USDx supply is about $56.4M and sUSDx holds about $36.1M. Supply peaked near $67.7M at the end of August and fell about 17–20% after the Origin Vault lock expired on 2026-09-04. It has held flat at about $54–56M since. sUSDx has earned roughly 20–22% annualized since launch (exchange rate 1.0000 to 1.0296 over about 60 days). USDx has 686 holder addresses and sUSDx has 235. The protocol is one to two orders of magnitude smaller than Ethena, Usual, Falcon or Resolv.

### Cited Findings
**Supply and TVL**
- DefiLlama lists "Axis" (category "Basis Trading", Ethereum), added 2026-08-20. TVL counts USDx supply and excludes sUSDx and the Upshift vault to avoid double counting. The series: $67.55M (08-20), $67.67M (08-27), $67.78M (09-03), $66.70M (09-10), $56.32M (09-17), $56.03M (09-24), $56.33M (09-28) — [DefiLlama API protocol/axis, fetched 2026-09-28](https://api.llama.fi/protocol/axis); [defillama.com/protocol/axis](https://defillama.com/protocol/axis)
- My on-chain snapshot via RPC (block ~26.08M, 2026-09-28): USDx totalSupply 56,358,179; sUSDx totalSupply 35,042,058 shares; sUSDx totalAssets 36,079,559 USDx; exchange rate 1.029607 USDx per sUSDx — [USDx on Etherscan](https://etherscan.io/token/0xa1fA7777974312f7d801A8880714a218F76233f8); [sUSDx on Etherscan](https://etherscan.io/token/0xEB892628D1E58BC475A6dCB7F5dBC4F591632AA4)
- Historical on-chain values (archive RPC, eth.drpc.org; dates are approximate from block offsets, ±1 day):

  | Date (approx.) | USDx supply | sUSDx assets | sUSDx rate |
  |---|---|---|---|
  | Jul 30 | 33.29M | ~0 (vault just deployed) | 1.0000 |
  | Aug 9 | 67.35M | 33.70M | 1.0021 |
  | Aug 19 | 67.51M | 33.87M | 1.0073 |
  | Aug 29 | 67.73M | 34.05M | 1.0126 |
  | Sep 7 | 66.39M | 25.61M | 1.0175 |
  | Sep 14 | 60.83M | 27.91M | 1.0221 |
  | Sep 21 | 54.36M | 31.65M | 1.0258 |
  | Sep 28 | 56.36M | 36.08M | 1.0296 |

  — [my RPC queries against USDx](https://etherscan.io/token/0xa1fA7777974312f7d801A8880714a218F76233f8) and [sUSDx](https://etherscan.io/address/0xEB892628D1E58BC475A6dCB7F5dBC4F591632AA4)
- Earlier milestones: the first $10M tranche of USDx was minted on 2026-04-08 in private testing. By 2026-07-09 Axis reported "$40m+ in TVL" and an APY of 10.7% — [The Axis Roadmap, 2026-07-10](https://axis.to/insights/The-Axis-Roadmap); [Binance Square repost](https://www.binance.com/en/square/post/310638930998993)
- A third-party review, quoting data-room material, reports "Capital as of May 19: $32.5M" over a 41-day sample period — [Turtle.Club review, 2026-07-29](https://hackmd.io/@DoMnolkQRGOjIqhl46A13A/rJ59uLvSfx)

**Origin Vault**
- The vault opened on 2026-07-29 with a $50M cap that filled in about 22 hours. The cap was then raised to $100M — [WEEX/Foresight News, 2026-07-31](https://www.weex.com/news/detail/why-is-axiss-arbitrage-story-attractive-filling-50-million-in-22-hours-bmt0wyj8yfr851h4t17bcnuq)
- It closed on 2026-08-05 with "$67,248,750 deposited across 1,857 wallets", short of the $100M cap. Axis said ogUSDx had earned "11.58% annualized" since close. The 30-day lock expired on 2026-09-04 at 14:00 UTC — [Axis insight "What's Next for USDx and Coordinates", 2026-09-01](https://axis.to/insights/Whats-Next-for-USDx-and-Coordinates); [Axis on X, 2026-08-05](https://x.com/AxisFDN/status/2085012835428692280)
- The homepage still shows "$67M raised for Origin Vault", "TVL $56.4M", "21.6% Net APY", ">$110B volume traded" and "14 venues covered" — [axis.to, fetched 2026-09-28](https://axis.to/)

**APY**
- DefiLlama yields for the Axis sUSDx pool: TVL $35.94M, current APY 26.38%, 30-day mean 22.70%. The daily series (starting 2026-09-06) ranges from 17.85% to 35.2% — [DefiLlama yields pool edf44260, fetched 2026-09-28](https://yields.llama.fi/chart/edf44260-d78f-5dab-853a-f89c4f523169)
- My own calculation from the on-chain exchange rate: about 20.4% simple annualized over the last ~30 days (1.0126 to 1.0296), about 19.6% over the last 7 days, and about 20% simple over ~50 days since early August — [derived from sUSDx convertToAssets queries, 2026-09-28](https://etherscan.io/address/0xEB892628D1E58BC475A6dCB7F5dBC4F591632AA4)
- The docs FAQ frames the base return as "a verifiable 10-20%… net range" — [docs: Origin Vault](https://docs.axis.to/origin-vault/origin-vault.md)

**Holders and distribution**
- Etherscan on 2026-09-28: USDx has 686 holder addresses and 63 transfers in 24h (down 72%). sUSDx has 235 holders — [Etherscan USDx](https://etherscan.io/token/0xa1fA7777974312f7d801A8880714a218F76233f8); [Etherscan sUSDx](https://etherscan.io/token/0xEB892628D1E58BC475A6dCB7F5dBC4F591632AA4)
- USDx balances on 2026-09-28: 36.57M in the sUSDx vault (~65% of supply) and 5.63M in Pendle SY-USDx — [my RPC balanceOf queries](https://etherscan.io/token/0xa1fA7777974312f7d801A8880714a218F76233f8)

**Integrations**
- **Pendle**: USDx and sUSDx markets with a 2026-12-03 maturity went live around 2026-09-02 to 09-04. Pendle's announcement said the markets come "with the highest multiplier for Axis points." Snapshot on 2026-09-28:

  | Market | Liquidity | Implied APY |
  |---|---|---|
  | PT/YT-sUSDx | $5.86M | 19.28% |
  | PT/YT-USDx | $2.24M | 15.01% |

  — [Pendle on X, 2026-09-04](https://x.com/pendle_fi/status/2095738643793207563); [Pendle API markets/active, fetched 2026-09-28](https://api-v2.pendle.finance/core/v1/1/markets/active)
- **Curve**: the USDx/USDT pool holds $3.05M and the sUSDx/USDx pool $2.01M — [DefiLlama yields, fetched 2026-09-28](https://yields.llama.fi/pools)
- **Upshift**: hosted the Origin Vault, which became the "Ecosystem Vault" after 2026-09-04 with a 7-day withdrawal period — [docs: Origin Vault](https://docs.axis.to/origin-vault/origin-vault.md)
- **Morpho, Aave and Euler**: I found no Axis USDx or sUSDx pools in DefiLlama yields on 2026-09-28. Several "USDX" or "sUSDX" pools listed there belong to other projects, including Clearpool on Flare, Lista on BSC and YieldNest ynUSDx, and should not be attributed to Axis — [DefiLlama yields, fetched 2026-09-28](https://yields.llama.fi/pools)
- **Turtle.Club**: a private deal offered a claimed 15–18% total (about 10% base plus 5–8% "points and future Axis tokens") with a 90-day liquidity hold — [Turtle.Club review, 2026-07-29](https://hackmd.io/@DoMnolkQRGOjIqhl46A13A/rJ59uLvSfx)

### Inferences
- The Origin Vault added roughly $34M of new USDx (33.3M to 67.4M). After unlock, about $11–13M (~17–20% of peak supply) left between about Sep 5 and Sep 21. That points to a mercenary component among pre-depositors. Supply has only partly recovered, to $56.4M. Put simply, the flagship campaign pulled in $67M of retail commitments against a $100M cap, then lost about a fifth once the lock ended.
- The high sUSDx APY (~20%+) is partly a leverage effect. Only about 64% of USDx is staked, and the team decides how much profit goes to the vault. If the ~21% on $36M were spread across all $56M of USDx, it would be about 13–14% on total backing (my estimate). That is in line with the "10–20%" pitch and with the 11.58% ogUSDx figure.
- The Pendle maturity (2026-12-03) matches the end of Coordinates Season 1 (2026-09-04 plus 90 days = 2026-12-03), so the Pendle markets were built around Season 1.

### Gaps
- I could not access the Dune dashboards, DeBank or the Coordinates leaderboard (app.axis.to is geo-blocked from the US). The total Coordinates issued and the Season 1 multipliers for Pendle YT/LP, sUSDx, USDx and Curve positions are unknown to me beyond Pendle's "highest multiplier" claim and the Ecosystem Vault's flat 10x.
- The exact dates of the historical supply snapshots are block-based approximations.

## 4. Audits, security, transparency and key risks

### Takeaway
The smart-contract layer is reasonably professional. There are three audits, and V2 is behind a 3-of-5 Safe plus a 48h timelock, both verified on-chain. The dominant risks sit off-chain: the backing is held on centralized exchanges with no off-exchange custody, verification of reserves depends on Accountable's read-only attestations, yield distribution is discretionary, mint and redeem are permissioned, USDx can be frozen or paused, and the product cannot be sold to US persons.

### Cited Findings
**Audits**

| Version | Auditor | Date | Commit | Findings |
|---|---|---|---|---|
| V2 | OpenZeppelin | July 2026 | 6db59ec | 25 total: 0 critical, 2 high, 7 medium, 13 low, 3 informational |
| V1 | Plainshift | Jan 2026 | 98849c5 | 9 total: 0 critical/high, 1 medium |
| V1 | Zellic | Aug 2025 | 845d765 | 10 total: 2 critical, 1 high, 4 medium |

- The docs warn: "These reports should not be summarized as 'no outstanding critical or high findings' without reconciling…" — [docs: Audit Reports](https://docs.axis.to/backing-reserves-and-transparency/audits.md); [OpenZeppelin audit](https://www.openzeppelin.com/news/axis-coordinate-v2-contracts-audit)
- The audits exclude "custodian solvency and physical custody, offchain operator policy and pricing". The docs state: "No report audits strategy execution, exchange solvency, custody operations, performance reporting, or legal structure." — [docs: Audit Reports](https://docs.axis.to/backing-reserves-and-transparency/audits.md)

**Governance and admin**
- DEFAULT_ADMIN_ROLE sits with a governance Safe (`0xdeB5…6D`), and proxy upgrades go through a TimelockController (`0xd6BB…0b`). My on-chain check on 2026-09-28 found the Safe threshold at 3 with 5 owners, and the timelock `getMinDelay` at 172,800 seconds (48h) — [docs: Contract Addresses](https://docs.axis.to/reference/contract-addresses.md); [my RPC query of Safe](https://etherscan.io/address/0xdeB538917b1C1AE6B81550a6C42A66d818cc6d6D)
- On 2026-07-29 the third-party review had reported the ProxyAdmin under a 1-of-3 Safe. That appears to have been fixed by late September — [Turtle.Club review, 2026-07-29](https://hackmd.io/@DoMnolkQRGOjIqhl46A13A/rJ59uLvSfx)
- Non-upgrade admin actions carry "no automatic delay window". These include cap increases, adding custodians or collateral, and granting roles — [docs: Governance](https://docs.axis.to/technical-and-architecture/governance.md)
- There is "no formal onchain governance today": no token voting and no onchain proposal system — [docs: Governance](https://docs.axis.to/technical-and-architecture/governance.md)

**Transparency**
- Accountable has "read-only access to the exchange accounts" and attests reserves. A Transparency Dashboard exists at app.axis.to/transparency. The docs caution: "Token supply and custody routes do not by themselves establish a live collateralization ratio or Proof of Reserves… once published." — [docs: Backing, Custody & Transparency](https://docs.axis.to/backing-reserves-and-transparency/backing-custody-transparency.md)

**Regulatory and access**
- Interfaces are geo-blocked in the US and 13 other jurisdictions, and USDx and sUSDx are "not offered to US persons" — [docs: FAQ](https://docs.axis.to/resources-and-legal/faq.md)
- The docs insist that Axis "is a protocol, not a fund" — [docs: FAQ](https://docs.axis.to/resources-and-legal/faq.md). The HackMD reviewer disagrees and calls it closer to a fund stake, and notes that direct USDC/USDT redemption requires identity verification — [Turtle.Club review](https://hackmd.io/@DoMnolkQRGOjIqhl46A13A/rJ59uLvSfx)

**Media-flagged risks**
- Press coverage lists CEX counterparty exposure, "Strategy opacity (trade secrets withheld)", APY compression as AUM grows, and de-peg risk — [WEEX/Foresight News, 2026-07-31](https://www.weex.com/news/detail/why-is-axiss-arbitrage-story-attractive-filling-50-million-in-22-hours-bmt0wyj8yfr851h4t17bcnuq)

**Incidents**
- I found no reports of hacks, exploits or de-pegs of Axis USDx through 2026-09-28. The CoinGecko all-time low is $0.99614 — [CoinGecko](https://www.coingecko.com/en/coins/axis-usd)

### Inferences
- The main tail risk is an FTX-style venue failure or a freeze on Binance, Bybit or Upbit. Ethena's peers now reduce that risk with off-exchange settlement, which Axis does not use. Capacity is a second risk: cross-venue arbitrage returns shrink as AUM grows, and the fund's peak was only $400M.
- The 2 critical findings in the Zellic V1 audit (Aug 2025) are historical and concern contracts that are now deprecated. They still say something about how mature the codebase was at that time.

### Gaps
- I could not see any dated Accountable attestation figures, such as reserves versus liabilities or a collateralization ratio.
- I found no public bug bounty (for example on Immunefi) and did not verify one.

## 5. Official communications: token, TGE, seasons, roadmap

### Takeaway
Axis has made no official statement of a token ticker, TGE date or airdrop. The Dec 2025 PR promised a "public token sale and full protocol launch early next year" (early 2026), and that has not happened. The live incentive program is "Coordinates" (points). Season 1 runs from 2026-09-04 for 90 days, to about 2026-12-03. Third-party material citing Axis data rooms puts the token window at Q1–Q2 2027.

### Cited Findings
- In Dec 2025 Axis planned an "initial Origin Vault in Q1 2026 with a target of up to $1 billion in deposits ahead of a public token sale and full protocol launch early next year". In practice the Origin Vault launched in late July 2026 (about 4 months late) and raised $67M against that $1B target — [The Block, 2025-12-03](https://www.theblock.co/post/381215/axis-5-million-usd-round-galaxy-ventures-onchain-yield-protocol-usd-bitcoin-gold); [Axis insight, 2026-09-01](https://axis.to/insights/Whats-Next-for-USDx-and-Coordinates)
- The pre-deposit terms said "10 Coordinates per day for every dollar deposited", with a 2x multiplier for the first $50M and 1.75x for the second $50M. The worked example: "$10,000 deposit… 6,000,000 Coordinates" over the 30-day lock. The referral program is branded "Beacon"/"Triangulate" — [Axis insight "How the Origin Vault Works", 2026-07-23](https://axis.to/insights/How-the-Origin-Vault-Works); [docs: Origin Vault](https://docs.axis.to/origin-vault/origin-vault.md)
- Season 1 of Coordinates "launches September 4, 2026 and runs for 90 days". The pre-deposit boost ended, vault positions moved to a "flat 10x multiplier", and "same capital counts only once" — [Axis insight, 2026-09-01](https://axis.to/insights/Whats-Next-for-USDx-and-Coordinates)
- Pendle's announcement: USDx and sUSDx markets maturing 2026-12-03 "with the highest multiplier for Axis points" — [Pendle on X, 2026-09-04](https://x.com/pendle_fi/status/2095738643793207563)
- The roadmap has Phase 1 "Scalable Engine" (live), Phase 2 USDx, BTCx and GOLDx (USDx live from 2026-04-08, BTCx and GOLDx "coming soon"), and Phase 3 "Dual-Purpose Yield & Liquidity" with no date. It says nothing about a token — [The Axis Roadmap, 2026-07-10](https://axis.to/insights/The-Axis-Roadmap)
- Axis Prime launched around 2026-08-31 to 09-01 as an institutional liquidity and OTC product. Claims: support for 15+ currencies, 25M+ pricing paths, spreads below 10 bps, and an OTC order executed for "a major centralized exchange" — [Crypto Briefing, 2026-08-31](https://cryptobriefing.com/axis-prime-institutional-liquidity-launch/); [Axis insight "Introducing Axis Prime", 2026-09-01](https://axis.to/insights/Introducing-Axis-Prime)
- None of the Axis blog posts I reviewed (Jul 10, Jul 23 and Sep 1, 2026) mentions a token, TGE, airdrop or exchange listing — [axis.to/insights list, fetched 2026-09-28](https://axis.to/insights)
- Third-party claims about the token:
  - The Turtle.Club HackMD review (2026-07-29) says "Ориентир Axis — Q1–Q2 2027 года" ("Axis's target is Q1–Q2 2027") and "no fixed TGE date in available materials". It adds that total supply, allocation, points-to-token conversion, valuation and vesting are all undisclosed. It cites data-room and internal Axis material — [HackMD](https://hackmd.io/@DoMnolkQRGOjIqhl46A13A/rJ59uLvSfx)
  - Foresight News reports "official hints at future governance token allocations; no economic model or timeline disclosed" — [WEEX/Foresight News, 2026-07-31](https://www.weex.com/news/detail/why-is-axiss-arbitrage-story-attractive-filling-50-million-in-22-hours-bmt0wyj8yfr851h4t17bcnuq)
  - A search summary of a pre-launch waitlist said it included "participation in its governance token allocation program" — [CryptoRank drophunting page (surfaced in search; not fetched directly)](https://cryptorank.io/drophunting/axis-activity1030)
- **Telegram** @AxisFDN is a broadcast channel with 732 subscribers on 2026-09-28. Its posts cover the seed round, the Origin Vault (the 22-hour fill, the 2x Coordinates multiplier) and Axis Prime (a "first 6-figure OTC transaction"). None mentions a token — [t.me/s/AxisFDN, fetched 2026-09-28](https://t.me/s/AxisFDN)

### Inferences
- The token timeline has already slipped. The Dec 2025 plan pointed to early 2026, and the latest third-party guidance says Q1–Q2 2027. Season 1 ending around Dec 3, 2026 and the lack of any official tokenomics make a 2026 TGE unlikely. The earliest plausible window is after Season 1, in Q1 2027 or later, and a Season 2 could push it further.
- There is no official points-to-token conversion. Holders of Coordinates, including buyers of Pendle YT, carry full uncertainty over supply, allocation and FDV.

### Gaps
- I could not access X posts directly beyond search snippets, and I could not access Discord. I found no Discord server linked from the official site; the site links only X, Telegram and LinkedIn.
- There is no official statement on the size of Season 1's Coordinates pool, on a Season 2, or on the share of tokens set aside for the airdrop.

## 6. Community and KOL sentiment

### Takeaway
The community is small and campaign-driven. There are about 1,857 Origin Vault wallets, 686 USDx holders, 235 sUSDx holders and 732 Telegram subscribers. Most coverage is neutral to positive. KOL threads and Asian crypto media amplified the "filled $50M in 22 hours" story and the story of a real, non-emission yield. Critics focus on CEX counterparty risk, strategy opacity and scalability. I found no major controversy, but the post-unlock outflows and the missed $100M cap suggest momentum faded after the pre-deposit.

### Cited Findings
- Media amplification: "Axis Fills $50 Million Retail Vault in 22 Hours" (Bit.Fan), "Why is Axis's Arbitrage Story Attractive…" (Foresight News/WEEX, 2026-07-31), and "Axis Protocol Raises $50M in 22 Hours" (Woofun) — [Bit.Fan](https://www.bit.fan/en/news/list/axis-origin-vault-arbitrage-yield-stablecoin-report-en-7d1aba5d-en-keyName-0e3b7208); [WEEX](https://www.weex.com/news/detail/why-is-axiss-arbitrage-story-attractive-filling-50-million-in-22-hours-bmt0wyj8yfr851h4t17bcnuq); [Woofun](https://test.woofun.io/en/news/detail/103061)
- A KOL thread framed Axis around "market inefficiencies can become a sustainable source of yield" — [THE ANGEL (@TheDeFiAngel) on X, 2026-08-04](https://x.com/TheDeFiAngel/status/2084663474643243506)
- A farmer and KOL flagged the unlock: "Axis pre-deposits will be withdrawable tomorrow, September 4, 2026 at 14:00 UTC… 7 day cooldown for free withdrawals or 30 bps fee for instant" — [@coinfoin_ on X, 2026-09-03](https://x.com/coinfoin_/status/2095495871769219348)
- A critical third-party review rated the deal "5.8/10 — Suitable only for limited, higher-risk allocations" — [Turtle.Club HackMD review, 2026-07-29](https://hackmd.io/@DoMnolkQRGOjIqhl46A13A/rJ59uLvSfx)
- Engagement proxies (2026-09-28): Telegram 732 subscribers, USDx holders 686, sUSDx holders 235. USDx transfers fell 72% day-on-day — [t.me/s/AxisFDN](https://t.me/s/AxisFDN); [Etherscan USDx](https://etherscan.io/token/0xa1fA7777974312f7d801A8880714a218F76233f8)
- Upshift pre-announced the vault as "Another institutional DeFi vault coming to Upshift" — [Upshift on X, 2026-07-22](https://x.com/upshift_fi/status/2080073947895235057)

### Inferences
- The cap raise from $50M to $100M ended with only $67M filled, and the vault then lost about 17–20% of supply at unlock. Early demand was strong but has not turned into sustained growth, so hype looks flat to fading after the pre-deposit. The Pendle launch and Season 1 (10x vault multiplier) are the current levers to re-engage farmers.
- Small holder counts plus multiplier-heavy points mean Coordinates are probably concentrated among whales and Pendle YT buyers. That raises the chance of "points dilution" complaints later, but I found none yet.

### Gaps
- I could not fetch X search or timelines directly, and Reddit and Discord returned nothing relevant. I found no evidence of sybil or farming controversies or dilution complaints; absence of evidence here is weak because of those access limits.

## 7. TGE timing evidence and pre-market pricing

### Takeaway
There is no pre-market for an Axis token on Whales Market, Hyperliquid or Aevo that I could find. Polymarket runs a thin "Will Axis launch a token by ___?" market that resolves on @AxisFDN. On 2026-09-28 it priced about 21.5% for a launch by 2026-12-31, about 58.5% by 2027-06-30 (with a wide spread) and about 64.5% by 2027-12-31. No implied FDV exists anywhere public.

### Cited Findings
- **Polymarket** "Will Axis launch a token by ___?" was created 2026-07-29, the same day the Origin Vault opened. Its resolution source is https://x.com/AxisFDN, and "Stablecoins… synthetic tokens will not count." Snapshot on 2026-09-28:

  | Deadline | Yes price | Bid / ask | Volume |
  |---|---|---|---|
  | By Dec 31, 2026 | 0.215 | 0.21 / 0.22 | $6.6K |
  | By Jun 30, 2027 | 0.585 | 0.48 / 0.69 | $1.1K |
  | By Dec 31, 2027 | 0.645 | 0.45 / 0.84 | $964 |

  Total event volume is about $8.7K, with about $3K of liquidity — [Polymarket gamma API, fetched 2026-09-28](https://polymarket.com/search/pre-market)
- An "AXIS" ticker with a ~$347M FDV on CoinGecko is **AXiS ALiVE**, an unrelated project, and must not be used as a price reference — [CoinGecko AXiS ALiVE](https://www.coingecko.com/en/coins/axis-alive)
- A Turtle.Club private deal priced 5–8% per year of its return as "points and future Axis tokens". That is an indirect market valuation of the points by a deal desk — [HackMD, 2026-07-29](https://hackmd.io/@DoMnolkQRGOjIqhl46A13A/rJ59uLvSfx)
- Pendle's YT-sUSDx implied APY was 19.28% on 2026-09-28, with sUSDx's actual trailing rate at about 20% or more. YT pricing therefore appears to assign little extra value to points beyond the underlying yield. The detailed YT analysis belongs to the other workstream — [Pendle API, fetched 2026-09-28](https://api-v2.pendle.finance/core/v1/1/markets/active)

### Inferences
- The market consensus (thin as it is) and the official silence line up on a TGE in H1 2027 at the earliest. A 2026 TGE is roughly a 1-in-5 event. The Polymarket volume is too small to carry much signal.
- For comparison, peers at TGE had much bigger bases. Ethena, Usual, Resolv and Falcon each had hundreds of millions to billions in TVL and larger raises. Axis has about $56M in TVL and a $5M seed. Unless TVL grows substantially before TGE, the market is likely to price Axis's token FDV well below those peers.

### Gaps
- I did not find Axis listed on Whales Market, Hyperliquid pre-launch perps, Aevo pre-launch, or Binance Alpha/Launchpool. I did not check each platform's live listing pages exhaustively (Whales Market and Hyperliquid pages were not fetched directly), so absence is likely but not fully confirmed.
- There is no information on token supply, allocation, vesting or exchange partners.
