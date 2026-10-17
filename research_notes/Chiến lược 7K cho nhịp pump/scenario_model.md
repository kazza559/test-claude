# Scenario model: 7 ways to deploy the ~$6.4K sleeve (computed 2026-10-17)

Computed by the coordinator with a purpose-built engine (scratchpad/model/model.js, data.js), using Hyperliquid prices from the 2026-10-17 03:23 UTC snapshot and the betas in hl_quant_screen.md. Equity $6376 (the wallet's USDC on 2026-10-17; the user calls it ~7K). Holding period 3 months; funding "calm" = HYPE 16%, SOL 8%, LIT 0%, others 11% per year; "hot" = HYPE 60%, SOL 45%, LINK/NEAR 50%, LIT 35%, others 45% (Nov–Dec 2024 levels from hl_quant_screen.md).

## Method

- Each coin follows BTC through a power law P = P0·(B/B0)^β, with a downside β on the way to the dip low and an upside β from the low to the target, so alts that fall harder than they recover end a round trip lower.
- Base β: downside = hourly downside β × 1.4 (multi-day moves are larger than hourly betas; cycle_lessons.md shows alts fell 1.3–2.3× BTC in first corrections), upside = mean of hourly upside β and the log swing ratio of the Aug-low→Sep-top rally.
- Modes: "alts strong" multiplies upside β by 1.3 and downside β by 0.85; "alts weak" multiplies upside β by 0.75 and downside β by 1.2.
- Resting limit buys fill only if the coin's modeled price at the dip low reaches them. Cross liquidation when cross equity < Σ notional × maintenance margin (HL: half the initial margin at max leverage: BTC 1.25%, SOL 2.5%, HYPE/LINK/BNB/NEAR/PUMP/ENA/ZEC 5%, LIT 10%); isolated legs lose only their margin. Breakout adds fill at the coin's modeled price when BTC passes the trigger on the way up and are held for half the period. Options valued with Black-Scholes (IV 40%, calibrated to the Deribit asks in instruments_structures.md). Fees: HL maker 0.015%, taker 0.045%; spot 0.04%/0.07%.
- Not modeled: idiosyncratic news, momentum reversals, flash wicks beyond the β mapping (see the 2025-10-10 wick table in hl_quant_screen.md), slippage, liquidation fees.

## Base betas used

| Coin | Price | Downside β | Upside β | Maint. margin |
|---|---|---|---|---|
| BTC | 81494 | 1 | 1 | 1.25% |
| HYPE | 79.92 | 1.74 | 1.31 | 5.00% |
| SOL | 104.6 | 1.86 | 1.3 | 2.50% |
| LIT | 3.2 | 2.17 | 1.78 | 10.00% |
| LINK | 12.31 | 2.18 | 1.26 | 5.00% |
| BNB | 721.1 | 1.27 | 0.83 | 5.00% |
| NEAR | 5.07 | 2.59 | 1.92 | 5.00% |
| PUMP | 0.00461 | 2.1 | 1.56 | 5.00% |
| ENA | 0.198 | 2.72 | 2.14 | 5.00% |
| ZEC | 1151 | 2.27 | 2.33 | 5.00% |

## Strategies

- **A. Spot 1 coin (HYPE)**: Không đòn bẩy, 30% vào ngay, 70% chờ 74/69. Legs: HYPE spot $1913 @ market; HYPE spot $2232 @ 74; HYPE spot $2231 @ 69. Capital used $6376, notional if all fill $6376 (1.00x).
- **B. Spot rổ 5 coin**: HYPE, SOL, LIT, LINK, BNB mỗi coin 20%. Legs: HYPE spot $510 @ market; HYPE spot $765 @ 69.5; SOL spot $510 @ market; SOL spot $765 @ 89.5; LIT spot $510 @ market; LIT spot $765 @ 2.67; LINK spot $510 @ market; LINK spot $765 @ 10.27; BNB spot $510 @ market; BNB spot $765 @ 649. Capital used $6375, notional if all fill $6375 (1.00x).
- **C. Perp 2x đang đặt**: 5 lệnh chờ hiện tại, cross, chưa khớp. Legs: HYPE perp cross 2x 30.00 units @ 74; HYPE perp cross 2x 40.00 units @ 69; SOL perp cross 2x 25.00 units @ 95; SOL perp cross 2x 30.00 units @ 88; LIT perp cross 2x 550.00 units @ 2.6999. Capital used $5740, notional if all fill $11480 (1.80x).
- **D. Lõi + vệ tinh + nhồi** (recommended): HYPE/SOL cross có lệnh mồi, NEAR/LIT isolated, nhồi HYPE/NEAR khi BTC đóng ngày trên 88K. Legs: HYPE perp cross 2x 15.00 units @ market; HYPE perp cross 2x 25.00 units @ 74; HYPE perp cross 2x 34.00 units @ 69; SOL perp cross 2x 8.00 units @ market; SOL perp cross 2x 12.00 units @ 95; SOL perp cross 2x 18.00 units @ 88; NEAR perp isolated 2x 110.00 units @ 4.4; NEAR perp isolated 2x 125.00 units @ 3.95; LIT perp isolated 2x 330.00 units @ 2.7; breakout add HYPE $3000 notional when BTC closes above 88000; breakout add NEAR $1000 notional when BTC closes above 88000. Capital used $5412, notional if all fill $10824 (1.70x).
- **E. Degen: HYPE 3x**: Dồn hết vào HYPE, cross 3x, 30% vào ngay. Legs: HYPE perp cross 3x 72.00 units @ market; HYPE perp cross 3x 90.00 units @ 74; HYPE perp cross 3x 97.00 units @ 69. Capital used $6369, notional if all fill $19107 (3.00x).
- **F. Rổ coin trend 2x**: NEAR, PUMP, ENA, ZEC, nửa vào ngay, nửa chờ −15%. Legs: NEAR perp cross 2x 314.40 units @ market; NEAR perp cross 2x 369.88 units @ 4.309; PUMP perp cross 2x 345770 units @ market; PUMP perp cross 2x 406788 units @ 0.003919; ENA perp cross 2x 8051 units @ market; ENA perp cross 2x 9471 units @ 0.1683; ZEC perp cross 2x 1.38 units @ market; ZEC perp cross 2x 1.63 units @ 978.4. Capital used $6376, notional if all fill $12752 (2.00x).
- **G. Call BTC + USDC**: 30% mua call 110K tháng 3/2027, 70% USDC lãi ~4%/năm. Legs: 1.09 BTC calls K=110000 (~5.3 months, $1750 each). Capital used $1913, notional if all fill $0 (0.00x).

## P&L after 3 months, mode "base" (BTC path: now $81.5K → dip low → target)

| Strategy | Bật luôn (80K→100K) | Chỉnh nông (77K→100K) | Về vùng đáy (73K→100K) | Chỉnh sâu (66K→95K) | Lình xình (74K→84K) | Siêu sóng (75K→120K) | Gãy tiền đề (57K→60K) | Cross liquidation at BTC |
|---|---|---|---|---|---|---|---|---|
| A. Spot 1 coin (HYPE) | +$567 (9%) | +$1,369 (21%) | +$2,235 (35%) | +$1,333 (21%) | +$516 (8%) | +$2,779 (44%) | −$2,413 (-38%) | none |
| B. Spot rổ 5 coin | +$746 (12%) | +$678 (11%) | +$2,249 (35%) | +$1,256 (20%) | +$536 (8%) | +$2,509 (39%) | −$2,489 (-39%) | none |
| C. Perp 2x đang đặt | +$0 (0%) | +$1,606 (25%) | +$4,619 (72%) | +$2,797 (44%) | +$1,243 (19%) | +$5,095 (80%) | −$4,464 (-70%) | $50K |
| D. Lõi + vệ tinh + nhồi | +$1,267 (20%) | +$2,543 (40%) | +$4,887 (77%) | +$2,798 (44%) | +$920 (14%) | +$7,150 (112%) | −$4,544 (-71%) (iso legs liquidated) | $46.6K |
| E. Degen: HYPE 3x | +$1,443 (23%) | +$3,523 (55%) | +$5,802 (91%) | +$3,155 (49%) | +$755 (12%) | +$7,659 (120%) | −$6,046 (-95%) LIQUIDATED | $63.4K |
| F. Rổ coin trend 2x | +$2,921 (46%) | +$2,772 (43%) | +$6,736 (106%) | +$4,092 (64%) | +$1,018 (16%) | +$15,790 (248%) | −$6,213 (-97%) LIQUIDATED | $60.2K |
| G. Call BTC + USDC | +$1,828 (29%) | +$1,828 (29%) | +$1,828 (29%) | +$329 (5%) | −$1,378 (-22%) | +$13,426 (211%) | −$1,867 (-29%) | none |

## P&L after 3 months, mode "strong" (BTC path: now $81.5K → dip low → target)

| Strategy | Bật luôn (80K→100K) | Chỉnh nông (77K→100K) | Về vùng đáy (73K→100K) | Chỉnh sâu (66K→95K) | Lình xình (74K→84K) | Siêu sóng (75K→120K) | Gãy tiền đề (57K→60K) | Cross liquidation at BTC |
|---|---|---|---|---|---|---|---|---|
| A. Spot 1 coin (HYPE) | +$808 (13%) | +$2,057 (32%) | +$3,653 (57%) | +$3,024 (47%) | +$505 (8%) | +$4,366 (68%) | −$1,936 (-30%) | none |
| B. Spot rổ 5 coin | +$1,068 (17%) | +$1,087 (17%) | +$3,705 (58%) | +$2,979 (47%) | +$345 (5%) | +$2,459 (39%) | −$2,006 (-31%) | none |
| C. Perp 2x đang đặt | +$0 (0%) | +$1,107 (17%) | +$7,453 (117%) | +$6,154 (97%) | +$1,108 (17%) | +$4,987 (78%) | −$3,551 (-56%) | $45.9K |
| D. Lõi + vệ tinh + nhồi | +$1,796 (28%) | +$2,738 (43%) | +$7,315 (115%) | +$6,167 (97%) | +$880 (14%) | +$9,222 (145%) | −$3,630 (-57%) (iso legs liquidated) | $42.3K |
| E. Degen: HYPE 3x | +$2,152 (34%) | +$5,542 (87%) | +$9,967 (156%) | +$8,119 (127%) | +$985 (15%) | +$12,319 (193%) | −$6,046 (-95%) LIQUIDATED | $60.7K |
| F. Rổ coin trend 2x | +$4,344 (68%) | +$4,574 (72%) | +$11,826 (185%) | +$9,976 (156%) | +$2,655 (42%) | +$19,030 (298%) | −$6,212 (-97%) LIQUIDATED | $57.1K |
| G. Call BTC + USDC | +$1,828 (29%) | +$1,828 (29%) | +$1,828 (29%) | +$329 (5%) | −$1,378 (-22%) | +$13,426 (211%) | −$1,867 (-29%) | none |

## P&L after 3 months, mode "weak" (BTC path: now $81.5K → dip low → target)

| Strategy | Bật luôn (80K→100K) | Chỉnh nông (77K→100K) | Về vùng đáy (73K→100K) | Chỉnh sâu (66K→95K) | Lình xình (74K→84K) | Siêu sóng (75K→120K) | Gãy tiền đề (57K→60K) | Cross liquidation at BTC |
|---|---|---|---|---|---|---|---|---|
| A. Spot 1 coin (HYPE) | +$377 (6%) | +$818 (13%) | +$1,099 (17%) | −$18 (0%) | +$17 (0%) | +$2,838 (45%) | −$2,935 (-46%) | none |
| B. Spot rổ 5 coin | +$492 (8%) | +$351 (5%) | +$1,089 (17%) | −$111 (-2%) | +$24 (0%) | +$2,869 (45%) | −$3,016 (-47%) | none |
| C. Perp 2x đang đặt | +$0 (0%) | +$977 (15%) | +$2,370 (37%) | +$144 (2%) | +$263 (4%) | +$5,822 (91%) | −$5,459 (-86%) | $54.3K |
| D. Lõi + vệ tinh + nhồi | +$849 (13%) | +$1,548 (24%) | +$2,517 (39%) | +$154 (2%) | −$9 (0%) | +$6,840 (107%) | −$5,283 (-83%) (iso legs liquidated) | $51.2K |
| E. Degen: HYPE 3x | +$883 (14%) | +$1,905 (30%) | +$2,467 (39%) | −$6,047 (-95%) LIQUIDATED | −$710 (-11%) | +$7,572 (119%) | −$6,047 (-95%) LIQUIDATED | $66K |
| F. Rổ coin trend 2x | +$1,853 (29%) | +$2,783 (44%) | +$2,992 (47%) | −$125 (-2%) | −$432 (-7%) | +$8,832 (139%) | −$6,213 (-97%) LIQUIDATED | $63.3K |
| G. Call BTC + USDC | +$1,828 (29%) | +$1,828 (29%) | +$1,828 (29%) | +$329 (5%) | −$1,378 (-22%) | +$13,426 (211%) | −$1,867 (-29%) | none |

## Equity drawdown at the dip low (base mode)

| Strategy | BTC 73K | BTC 66K | BTC 57K |
|---|---|---|---|
| A. Spot 1 coin (HYPE) | −$672 (-11%) | −$1,590 (-25%) | −$2,668 (-42%) |
| B. Spot rổ 5 coin | −$655 (-10%) | −$1,619 (-25%) | −$2,732 (-43%) |
| C. Perp 2x đang đặt | −$787 (-12%) | −$2,604 (-41%) | −$4,707 (-74%) |
| D. Lõi + vệ tinh + nhồi | −$975 (-15%) | −$2,683 (-42%) | −$4,671 (-73%) |
| E. Degen: HYPE 3x | −$2,016 (-32%) | −$4,765 (-75%) | −$6,041 (-95%) |
| F. Rổ coin trend 2x | −$2,116 (-33%) | −$4,410 (-69%) | −$6,209 (-97%) |
| G. Call BTC + USDC | −$1,499 (-24%) | −$1,782 (-28%) | −$1,894 (-30%) |

## Funding drag (dip 73K → target 100K, 3 months, base mode)

| Strategy | Funding calm | Funding hot | P&L calm | P&L hot |
|---|---|---|---|---|
| C. Perp 2x đang đặt | $360 | $1747 | +$4,619 | +$3,232 |
| D. Lõi + vệ tinh + nhồi | $457 | $2015 | +$4,887 | +$3,328 |
| E. Degen: HYPE 3x | $898 | $3369 | +$5,802 | +$3,331 |
| F. Rổ coin trend 2x | $450 | $1889 | +$6,736 | +$5,297 |

## Where each resting order fills (BTC-equivalent level, base / alts-weak)

| Plan | Order | Notional | BTC level base | BTC level alts weak |
|---|---|---|---|---|
| C | HYPE 30 @ 74 | $2220 | 78.0K | 78.5K |
| C | HYPE 40 @ 69 | $2760 | 74.9K | 76.0K |
| C | SOL 25 @ 95 | $2375 | 77.4K | 78.1K |
| C | SOL 30 @ 88 | $2640 | 74.3K | 75.4K |
| C | LIT 550 @ 2.6999 | $1485 | 75.4K | 76.3K |
| D | HYPE 15 @ market (79.92) | $1199 | now | now |
| D | HYPE 25 @ 74 | $1850 | 78.0K | 78.5K |
| D | HYPE 34 @ 69 | $2346 | 74.9K | 76.0K |
| D | SOL 8 @ market (104.6) | $837 | now | now |
| D | SOL 12 @ 95 | $1140 | 77.4K | 78.1K |
| D | SOL 18 @ 88 | $1584 | 74.3K | 75.4K |
| D | NEAR 110 @ 4.4 isolated | $484 | 77.2K | 77.9K |
| D | NEAR 125 @ 3.95 isolated | $494 | 74.0K | 75.2K |
| D | LIT 330 @ 2.7 isolated | $891 | 75.4K | 76.3K |
| D | HYPE breakout add | $3000 | BTC daily close > 88K | |
| D | NEAR breakout add | $1000 | BTC daily close > 88K | |

Isolated liquidation in plan D (base): NEAR 4.40 leg at coin price 2.32 (BTC ≈ 60.2K), NEAR 3.95 leg at 2.08 (≈ 57.8K), LIT 2.70 leg at 1.50 (≈ 57.5K).

## Coin prices implied at BTC targets (path through a 75K dip; base / alts strong)

| BTC | HYPE | SOL | NEAR | LIT | LINK | BNB |
|---|---|---|---|---|---|---|
| 88K | 85.3 / 92.8 | 110 / 120 | 5.56 / 6.29 | 3.55 / 3.97 | 12.6 / 13.7 | 741 / 783 |
| 95K | 94.3 / 106 | 122 / 137 | 6.44 / 7.62 | 4.07 / 4.74 | 13.8 / 15.5 | 790 / 851 |
| 100K | 101 / 115 | 130 / 149 | 7.10 / 8.66 | 4.46 / 5.34 | 14.8 / 16.9 | 824 / 899 |
| 110K | 114 / 136 | 147 / 175 | 8.53 / 11.0 | 5.28 / 6.66 | 16.6 / 19.8 | 892 / 997 |
| 126K | 136 / 171 | 176 / 220 | 11.1 / 15.4 | 6.73 / 9.12 | 19.7 / 24.7 | 998 / 1.15e+3 |

## Takeaways from the model

- Spot (A, B) never liquidates but makes roughly a third to half of what the 2x structures make in the bull paths; a spot basket of the watchlist (B) does no better than spot HYPE alone (A), consistent with cycle_lessons.md (alt baskets lag).
- The current resting orders (C) earn nothing if BTC turns up from ~$80K without dipping to ~$78K (no order fills), and fully fill only below ~$74K.
- Plan D (starter positions + the same ladder levels + NEAR/LIT isolated + breakout adds above $88K) beats C in the no-dip, shallow-dip, base-dip and super-wave paths, ties in the deep dip, lags slightly in the slow-chop path, and moves the cross liquidation from ~$50K to ~$46.6K (base) because LIT moves to isolated and the core is smaller. Its 73K drawdown is −15% vs −12% for C.
- HYPE 3x (E) and the 2x trend basket (F) have the biggest bull payoffs but are liquidated if BTC loses the August low (E at ~$63K base / $66K alts-weak, F at ~$60K / $63K) and draw down −32% to −33% already at BTC 73K. In a hot funding regime E's edge over D disappears (3-month funding ≈ $3.4K).
- BTC calls plus USDC (G) cap the loss near −30% and pay most in the super-wave path, but lose in slow chop (time decay), need an options venue (Deribit/OKX), and add BTC exposure the user already has.
