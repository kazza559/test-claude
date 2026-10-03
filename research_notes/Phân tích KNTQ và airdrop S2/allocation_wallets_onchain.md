# Where the 730M non-airdrop KNTQ actually sits — and whether it is locked

Measured by the coordinator on 2026-10-03 ~23:42 UTC, read-only on HyperEVM
(`rpc.purroofgroup.com`: `eth_getLogs`, `eth_getCode`, `eth_call`). Tag **[V-ME]**.
This closes the gap the fundamentals research flagged as unresolved ("I cannot say whether the 310M
insider allocation sits in a verifiable on-chain vesting contract or in a multisig the team can move
at will").

## Takeaway
The deployer's 730M split into **exactly five addresses in one minute at TGE**, and those five addresses
are **all plain EOAs with no contract code** — there is no on-chain vesting contract, no timelock and no
multisig code behind the team, investor or foundation allocations. **660,000,000 KNTQ (66% of total
supply) sits in five externally-owned keys that can move at any moment.** The team (235M) and investor
(75M) buckets are still at their exact original balances, so nothing has moved in 10 months — but the
~2026-11-27 "cliff + 24-month linear vesting" is a **promise in the docs, not enforced by code**.

## Cited Findings [V-ME]

KNTQ `Transfer` logs with `from` = the genesis deployer `0x51172933b60847085e2a959e860e2ec9e240ac09`,
scanned over blocks 20,320,000–20,620,000 (the 3.5 days after TGE; block 20,324,553 = 2025-11-27
12:00:00 UTC). Six transfers, 730,000,001 KNTQ in total, five of them within the same minute:

| Time (UTC) | Destination | KNTQ | Matches the docs' allocation |
|---|---|---|---|
| 2025-11-27 12:07 | `0x5bd9e766c0151dcfbc4246e5f8b3193c4beeaae4` | 300,000,000 | Growth / ecosystem (30%) |
| 2025-11-27 12:07 | `0x373e0b6b57818ac2bb3a3e55e31128d5f880d90e` | 235,000,000 | Core contributors / team (23.5%) |
| 2025-11-27 12:07 | `0xf50ad63714f10f4e96eeabd43d549c8232992b36` | 100,000,000 | Foundation (10%) |
| 2025-11-27 12:07 | `0x9ef3b3a49ee9a2fd28a10f6e9407219e7ceca1a2` | 75,000,000 | Investors (7.5%) |
| 2025-11-27 12:07 | `0x4664b0453c7c483e2e262ca54351ade71b6be734` | 20,000,000 | Liquidity (2%) |
| 2025-11-27 13:20 | `0x3333…3333` | 1 | dust / test |

Current state of those five addresses:

| Address | Bucket | `eth_getCode` | KNTQ balance now | Moved since TGE |
|---|---|---|---|---|
| `0x373e0b6b…d90e` | team 235M | **EOA (no code)** | **235,000,000** | nothing |
| `0x9ef3b3a4…a1a2` | investors 75M | **EOA (no code)** | **75,000,000** | nothing |
| `0xf50ad637…2b36` | foundation 100M | **EOA (no code)** | **100,000,000** | nothing |
| `0x5bd9e766…aae4` | growth 300M | **EOA (no code)** | 250,000,000 | −50,000,000 |
| `0x4664b045…e734` | liquidity 20M | **EOA (no code)** | 4,523,810 | −15,476,190 |

- The 50,000,000 that left the growth wallet is **exactly the Season-2 claim pool**: `0x5bd9e766…aae4`
  is the address that funded the claim contract `0x435bb7ea…c03b` (100 KNTQ test + 49,999,900).
  So the "$0.26 claim" is funded out of the 30% growth bucket, not out of a separate airdrop reserve.
- 15.48M of the 20M liquidity bucket has been deployed (consistent with the ~4.2M held across the
  Nest / Project X pools plus CEX and other venues).

## Inferences
- **The Nov-27 unlock is a disclosure, not a mechanism.** Because the tokens sit in EOAs, there is no
  cliff to observe on-chain, no vesting contract to read a schedule from, and no code that prevents an
  earlier or larger release. The practical implication for position sizing: the supply risk is
  *continuous* from now on, not a dated event — and the only early-warning signal available is watching
  these five addresses for any outbound transfer.
- The flip side is a genuinely good 10-month record: both insider wallets are still at round, untouched
  balances, and the only things that have moved are the liquidity bucket (into pools) and the growth
  bucket (into the claim contract). No quiet trickle to exchanges has happened so far.
- **Float arithmetic.** 660M in these five EOAs + 27.95M still in the claim contract + 75.8M in the
  sKNTQ contract = 763.8M accounted for, leaving roughly 236M in genuinely dispersed hands — close to
  CoinGecko's 280.48M circulating and well below DropsTab's 335.48M.
- Watching these five addresses is cheap and high-signal: any transfer out of `0x373e0b6b…` or
  `0x9ef3b3a4…` is the single most bearish on-chain event available for KNTQ, and would precede
  exchange deposits by minutes to hours. The same applies to further draws on the 250M growth wallet.

## Gaps
- EOA keys may be custodied by a third party or sit behind an off-chain legal lock; "EOA" means no
  *on-chain* enforcement, not necessarily no commitment.
- The docs' exact unlock reading (1-year cliff then 24-month linear ≈ 12.92M/month, versus a 1/3-at-cliff
  reading ≈ 103.3M on day one) cannot be resolved on-chain precisely because there is no vesting contract.
- These addresses were not checked for HyperCore-side balances or for non-KNTQ assets.
