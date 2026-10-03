# NetNet (NET) — phân tích on-chain

Token `0xCA9c78Dd337A67F6e0077F65F5E9218719d30eDf` trên **Robinhood Chain** (Arbitrum Orbit L2, chainId 4663).
Snapshot: **2026-10-03 ~23:15 UTC**. Mọi số liệu đọc trực tiếp từ chain (RPC công khai, contract verified trên Sourcify), có đối chiếu với DexScreener, GeckoTerminal, CoinGecko và HoodScan.

> Đây là phân tích dữ liệu, không phải lời khuyên đầu tư. NET là token rebase kiểu OlympusDAO, biến động rất mạnh. Bạn có thể mất phần lớn số vốn bỏ vào.

---

## TL;DR

| | |
|---|---|
| Giá | **~$277** (TWAP 1 giờ $279,9), −85% so với đỉnh $1.888 (29/8), −45% trong 7 ngày, −76% trong 30 ngày. Hôm nay có lúc chạm **$210** rồi hồi |
| NAV (backing / NET) | **$170,45**. Treasury giữ **$22,49 triệu** risk-free value (USDG) |
| Premium (giá / NAV) | **1,64×** (đỉnh 21× vào 30/8) |
| Sàn mua lại (InverseBond) | **$167,89** (= NAV × 0,985), tối đa ~$69K mỗi epoch 8 giờ |
| Pha loãng | Supply 131.946 NET, có thể tăng **~2.390 NET/ngày (~1,8%/ngày)**: rebase ~1.400 + bond tối đa ~990 |
| Thanh khoản | ~$1,19 triệu trên 29 pool. Pool chính Uniswap v2 NET/USDG có ~$213K USDG |

**Ai đang bán**
1. **Người mua bond rồi xả.** Bond bán NET rẻ hơn TWAP 3%, vest 2 ngày, hết sạch capacity mỗi epoch (~950–980 NET/ngày). Nhóm ví có claim bond **bán ròng −$5,9 triệu trên DEX trong 30 ngày**.
2. **Staker chốt phần NET rebase** (~1.600 NET/ngày được mint thêm cho staker trong tuần qua).
3. **Team.** Ví Team Safe đã exercise **13.320 NET từ option pTEAM với giá $1/NET**. 192/200 giao dịch exercise chuyển NET thẳng vào các "bond desk" ngay trong cùng transaction để bán cho người đăng ký, rẻ hơn thị trường 6,5% (ước tính **~$7,1 triệu**; đo trực tiếp được ít nhất $5,4 triệu USDG người đăng ký đã trả vào desk, 24/7–28/9). Hiện vẫn còn **6.258 NET có thể exercise ngay với giá $1** (~$1,7 triệu theo giá thị trường).

**Ai đang mua**
1. **Người mua lớn nhất là team.** "RWA Sleeve" (Safe do team giữ) mua lại **4.141 NET (~$1,83 triệu)** từ 18/9 đến 3/10. Riêng 4 ngày gần nhất mua $120–210K/ngày. Tiền mua đến từ việc bán bớt và thế chấp cổ phiếu token hoá trên Morpho. Ví mà HoodScan xếp hạng là "holder lớn nhất" (`0xe7e8…96f6`) thực chất là **owner duy nhất (Safe 1-of-1) của cả Team Safe lẫn RWA Sleeve**.
2. **Nhà đầu tư nhỏ lẻ bắt đáy.** ~12,3K ví mua ròng tổng +$17,5 triệu, ~8,8K ví bán ròng −$13,8 triệu (30 ngày).
3. **Người mua đòn bẩy qua Loopback** (vay USDG thế chấp wsNET): đang vay $658K, utilization 99,4%.

**Xu hướng.** Downtrend rõ: đáy sau thấp hơn đáy trước, giá nằm dưới MA7/MA20/MA30, RSI14 ~36. Cơ chế của token tạo ra áp lực trôi xuống: nếu cầu không tăng ~1,8%/ngày, market cap đứng yên đồng nghĩa giá giảm theo mức pha loãng. Sàn kỹ thuật và cơ chế nằm ở vùng NAV $165–171. Kịch bản cơ sở là đi ngang hoặc giảm về **$200–240** (1,2–1,4× NAV) trong 1–3 tuần. Rủi ro là test NAV (~−38%). Phần trên bị chặn mềm quanh **$341 (2× NAV)**, vì PremiumSeller bắt đầu bán ra từ mức đó (chi tiết ở §7). Lực đỡ chính hiện nay là team mua lại qua Sleeve, mà khả năng vay thêm để mua của Sleeve gần như đã cạn.

---

## 1. Token và hợp đồng

| Mục | Giá trị |
|---|---|
| Tên / ký hiệu / decimals | NetNet / NET / 9 |
| Kiến trúc | Fork OlympusDAO v1: NET, sNET (rebase), Staking, Treasury, Distributor, BondDepository + InverseBond (mua lại), PremiumSeller, TaxCollector, pTEAM (option của team) |
| Deploy | 2026-07-16. Founding offering (GenesisBond) huy động 50.000 USDG với giá $3/NET |
| Supply | 131.946 NET; **91,9% đang stake** (121.244 NET). sNET index 4,08: staker từ ngày đầu có số NET gấp ~4 lần |
| Holder | ~11.100 ví có NET/sNET/wsNET > 0,001 |
| Thuế | 5% mỗi lượt mua/bán, **chỉ** áp dụng trên pair đã map (thực tế là Uniswap v2 NET/USDG và v2 NET/WETH). Các pool v3/v4/Ramses/Alandale không bị đánh thuế |
| Quyền admin | Key team là Safe `0x3Bb7…5f42` cấu hình **1-of-1**. Owner duy nhất là EOA `0xe7e867518c5b3d929ca63622f314ff9dc60e96f6`, cũng là owner duy nhất của RWA Sleeve `0x4987…c7cb` |

Địa chỉ đầy đủ các contract (công bố ở [docs.netnet.capital/official-channels](https://docs.netnet.capital/official-channels)) nằm trong `scripts/flows.py` (`PROTO`). ABI đã verify lưu ở `abi/`.

## 2. Pool thanh khoản hiện tại

Có 29 pair trên DexScreener và hơn 60 pool trên GeckoTerminal (phần lớn là pool rác chỉ vài trăm USD). Các pool đáng kể:

| Pool | DEX | Thanh khoản | Vol 24h | Thuế 5%? | Ghi chú |
|---|---|---:|---:|:-:|---|
| [`0x59F9…5B54`](https://dexscreener.com/robinhood/0x59f95461e68e0c77605299791e1449f175165b54) NET/USDG | Uniswap v2 | ~$426K | ~$0,5M | ✅ | Pool "canonical": oracle TWAP của protocol đọc giá từ đây. **97,6% LP do Treasury sở hữu** (POL) |
| `0x0d66…deb3` NET/USDG 0,9% | Uniswap v4 | ~$251K | ~$0,3M | ❌ | |
| [`0x99e7…1673`](https://dexscreener.com/robinhood/0x99e70a5b06215e5d2f3bec773b4f59c008fc1673) NET/USDG 1% | Up v3 | ~$246K | ~$0,85M | ❌ | Volume lớn nhất; không chịu thuế nên thu hút aggregator và arbitrage |
| `0x813f…3862` NET/USDG 1% | Ramses v3 | ~$95K | ~$0,24M | ❌ | |
| `0x4030…170d` NET/USDG | Uniswap v4 | ~$58K | ~$0,41M | ❌ | |
| `0xdbe4…a301` NET/USDG 3,2% | Uniswap v4 | ~$28K | — | ❌ | |
| `0x146a…18D3` NET/USDG, `0x7EeE…743C` NET/WETH | Alandale CL | ~$14K + ~$9K | ~$0,3M | ❌ | |

Danh sách đầy đủ ở `data/pools.csv`. Tổng thanh khoản ~**$1,19 triệu**, chỉ bằng ~3,3% FDV ($36,5 triệu). Một lệnh bán 1.000 NET (~$277K) sẽ làm giá trượt rất mạnh. Khoảng 80% volume chạy qua các pool không bị đánh thuế, nên thu nhập phí của treasury chỉ đến từ pool v2.

## 3. Cơ chế và số liệu protocol

Các tham số dưới đây là hằng số trong contract (đã đối chiếu `Constants.sol` trên Sourcify), không admin nào sửa được.

| Thành phần | Quy tắc | Trạng thái hiện tại |
|---|---|---|
| **NAV** | RFV / totalSupply; RFV = USDG liquid + USDG trong Morpho × 0,98 + POL (NET định giá $1) | **$170,45**; RFV $22,49M = $6,91M liquid + $15,87M ở vault Steakhouse USDG (Morpho) + $25K POL |
| **Rebase** (8h/epoch) | rate = 0,45% × clamp((P−1)/0,75, 0, 1), P = TWAP/NAV | P = 1,64 → **0,385%/epoch** (1,16%/ngày, APY lý thuyết ~6.600%) ≈ **1.400 NET/ngày** ở mức hiện tại |
| **Bond** | Giá = max(TWAP × 0,97, NAV), vest 2 ngày, capacity 0,25% supply/epoch | Giá bond ~$271. Capacity ~**990 NET/ngày**, gần như lúc nào cũng bán hết |
| **InverseBond** (mua lại) | Mua NET ở NAV × 0,985 rồi đốt; capacity 1% USDG liquid/epoch | **$167,89**, ~$69K/epoch (~$207K/ngày). Hiện không có ai bán vào vì giá thị trường cao hơn |
| **PremiumSeller** | Khi TWAP > 2× NAV: mint rồi bán 0,25% lượng NET trong pool, tối đa 1 lần/giờ | Tắt từ 2/10 (P < 2). Tổng đã mint và bán 2.271 NET |
| **pTEAM** | Team mint NET với giá $1, trần 15% float tại thời điểm exercise, không hết hạn | Đã exercise **13.320 NET**; có thể exercise thêm **6.258 NET** ngay. Nếu exercise hết, NAV giảm ~4,5% xuống ~$162,8 |
| **Thuế 5%** | Đến ngày 30, team nhận 4% → 0%; treasury nhận 1% → 5% | Từ 16/8: 100% vào treasury |

### Nguồn của toàn bộ ~132K NET đã mint

| Nguồn | NET | Tỷ trọng |
|---|---:|---:|
| Rebase trả cho staker | 63.484 | 48% |
| Bond | 31.224 | 24% |
| Genesis (founding offering + POL) | 21.667 | 16% |
| **pTEAM (team, giá $1)** | **13.320** | **10%** |
| PremiumSeller | 2.271 | 2% |

Đã đốt tổng 19 NET (PrizeVault và InverseBond). Số liệu ở `data/summary.json`.

### Lịch sử NAV, giá và supply (chọn lọc, đầu ngày UTC)

| Ngày | Giá | NAV | Premium | Supply | Stake % |
|---|---:|---:|---:|---:|---:|
| 18/7 | $39 | $2,6 | 15× | 21,7K | 7% |
| 01/8 | $28 | $6,8 | 4,1× | 29,2K | 78% |
| 15/8 | $129 | $13,7 | 9,8× | 38,9K | 83% |
| 29/8 | $1.317 | $69,6 | 19,8× | 57,7K | 90% |
| 08/9 | $636 | $140,8 | 4,3× | 73,1K | 90% |
| 22/9 | $669 | $171,0 | 3,8× | 101,7K | 93% |
| 27/9 | $472 | **$175,5** (đỉnh NAV) | 2,7× | 114,4K | 92% |
| 03/10 (23h) | $277 | $170,5 | 1,64× | 131,9K | 92% |

Bảng 12 giờ đầy đủ ở `data/protocol_history_12h.csv`. Hai điểm chính:
- NAV tăng ~26 lần (từ $6,8 ngày 1/8 lên $175,5 ngày 27/9) **là nhờ bond và PremiumSeller bán NET với giá premium trong giai đoạn hưng phấn**, không phải nhờ lợi nhuận kinh doanh.
- NAV **đã đạt đỉnh ngày 27/9 và bắt đầu giảm**: khi premium co lại, rebase pha loãng nhanh hơn lượng USDG mà bond mang vào.

## 4. Ai đang bán

### 4.1 Người mua bond để arbitrage (nguồn bán lớn nhất)
Bond cho phép mua NET rẻ hơn TWAP 3%, nhận dần trong 2 ngày. Lời gần như chắc chắn nếu giá không giảm quá 3% trong 2 ngày, nên capacity (0,25% supply mỗi epoch) **luôn bị mua hết**. Kết quả là ~950 NET/ngày được giải phóng cho bonder, và phần lớn bị bán ngay ra thị trường:

- 30 ngày qua có **26,6K NET** được claim từ BondDepository; 7 ngày qua là 7,6K NET.
- Các ví có claim bond: **379 ví bán ròng −$10,5 triệu**, 425 ví mua ròng +$4,6 triệu. **Tổng ròng −$5,9 triệu**.
- Top bán ròng 30 ngày gần như toàn là bonder:

| Ví | Bán ròng 30 ngày | NET claim từ bond |
|---|---:|---:|
| `0x0869…d331` | −$1,45 triệu | 2.036 |
| `0xf357…401d` | −$0,70 triệu | 1.347 |
| `0x397c…58cd` | −$0,63 triệu | 1.050 |
| `0xb0fb…2461` | −$0,57 triệu | 800 |
| `0x7c94…f3c0` | −$0,55 triệu | 1.001 |
| `0x11ac…9ce2` | −$0,52 triệu | 850 |
| `0x797a…888f` | −$0,49 triệu | 717 |

  Danh sách đầy đủ ở `data/top_traders_30d.csv`.

Bond vẫn làm NAV tăng (USDG vào treasury với giá ~$271/NET, cao hơn NAV), nhưng **trên thị trường nó là dòng bán đều đặn khoảng $260–270K/ngày**.

### 4.2 Staker chốt phần rebase
Tuần qua protocol mint khoảng **1.590–1.690 NET/ngày** (~$450K) cho staker. Không có warmup hay cooldown, nên rút stake và bán có thể làm ngay. Lượng stake/unstake mỗi tuần lên tới 20–32K NET (`data/weekly_supply_flows.csv`). Phần lớn nhóm "ví khác bán ròng" (−$13,8 triệu trong 30 ngày) là ví bán NET có được từ rebase hoặc từ stake cũ.

### 4.3 Team: pTEAM → bond desk (đây là phát hiện quan trọng nhất)
Đã xác minh trên chain (xem `data/team_pteam_to_desks.csv`, `data/team_summary.json`):

- Từ **24/7 đến 28/9**, Team Safe gọi pTEAM để mint **13.320 NET với giá $1/NET**, tổng trả $13.320 USDG vào treasury.
- **192/200** giao dịch là một lệnh Safe `execTransaction` duy nhất gồm ba bước: trả USDG → mint NET → **chuyển NET thẳng vào desk**. Ví dụ [`0x4b36…03e8`](https://robinhoodchain.blockscout.com/tx/0x4b36c8e845dc3bb8268f1cedea0606e8090fb1597de160cc6760b58b6be803e8): 145 USDG → mint 145 NET → 145 NET vào RwaDesk.
- NET được chuyển tới:

| Desk | NET | Ước tính bán ra (TWAP × 0,935) |
|---|---:|---:|
| RwaDesk có trong danh sách chính thức `0x99b6…1961` | 6.519 | ~$1,89 triệu |
| RwaDesk `0xa84e…f08d` (Sourcify ghi tên `RwaDesk`) | 3.951 | ~$3,25 triệu |
| Desk `0x70ea…947b` | 2.250 | ~$1,60 triệu |
| Desk `0x2f2f…ef78` | 550 | ~$0,33 triệu |
| PackDesk (Superstore) | 250 | ~$0,01 triệu |
| **Tổng** | **13.520** | **~$7,1 triệu** |

  Ba desk `0xa84e`, `0x70ea` và `0x2f2f`, cùng desk `0x732b…15b3` (nơi nhận 500 NET từ Sleeve), đều có `manager()` là Team Safe nhưng **không nằm trong danh sách địa chỉ chính thức**. Docs chỉ nhắc tới "phiên bản trước" của desk mà không công bố địa chỉ.
- Desk bán NET cho người đăng ký với giá TWAP × 0,935. Đo trên chain, người đăng ký đã trả **ít nhất $5,44 triệu USDG** vào các desk. Chỉ **~$0,68 triệu (12,5%) vào Treasury** (từ hai desk cũ `0xa84e` và `0x99b6`). **~$4,76 triệu** đi qua router `0xc941…59bd` (nhiều khả năng là router Rialto) để mua cổ phiếu token hoá (NVDA, SPCX, AAPL, GOOGL…), rồi chuyển vào **RWA Sleeve**: một Safe do team giữ, không tính vào NAV.
- **Docs nói khác với chain.** Trang [Real World Bonds](https://docs.netnet.capital/rwa-desk) viết rằng inventory của desk là "NET that the Sleeve bought on the open market". Trên chain, ~13,3K NET inventory đến thẳng từ pTEAM vừa mint (các desk đúng là không tự mint, nhưng nguồn NET là option của team). Sleeve chỉ chuyển vào desk khoảng 500 NET (vào `0x732b`), cộng 200 NET đi vòng qua Team Safe.
- Đỉnh exercise theo tuần: 2.190 NET (14–20/8) và 2.301 NET (21–27/8). Sau 28/9 không có thêm lần exercise nào, nhưng **6.258 NET vẫn có thể exercise ngay** và trần tăng thêm khoảng 15% của mọi NET mới mint.

### 4.4 Các nguồn bán nhỏ khác
- TaxCollector đổi phí 5% (thu bằng NET) sang USDG trên pool v2: ~20–80 NET/ngày.
- PremiumSeller: tắt từ khi premium < 2×.

## 5. Ai đang mua

### 5.1 Team qua RWA Sleeve (người mua lớn nhất)
RWA Sleeve `0x4987…c7cb` mua NET qua LiFi, rải lệnh trên nhiều pool:

| Ngày | NET | USD |
|---|---:|---:|
| 18–24/9 | 394 | $290K |
| 25–27/9 | 728 | $390K |
| **28/9** | **834** | **$378K** |
| 29–30/9 | 551 | $240K |
| 1/10 | 550 | $209K |
| 2/10 | 654 | $200K |
| 3/10 (đến 23h UTC) | 429 | $120K |
| **Tổng** | **4.141** | **~$1,83 triệu** (giá vốn trung bình ~$441) |

Số theo ngày ở `data/sleeve_net_buys_daily.csv`. Sau khi mua, phần lớn được stake và wrap: hiện Sleeve giữ **737 wsNET (~3.010 NET) và 106 NET**, tổng ~3.115 NET (~$0,86 triệu).

- **Nguồn tiền:** Sleeve bán bớt cổ phiếu token hoá trên các pool Uniswap v3 cổ phiếu/USDG (net ~+$1,45 triệu USDG), và đem **$3,48 triệu cổ phiếu thế chấp trên Morpho để vay $1,37 triệu USDG** (LTV 39%, ngưỡng thanh lý 62,5%). Các market Morpho này đang dùng **97–100% vốn**, nên khả năng vay thêm để mua tiếp gần như đã cạn. Cổ phiếu còn trong ví ~$0,56 triệu, cộng ~$61K USDG.
- HoodScan xếp ví `0xe7e8…96f6` là "holder lớn nhất" (mua $1,54 triệu, chưa bán). Thực ra đó là EOA ký giao dịch cho Sleeve (`execTransaction` gửi tới Safe `0x4987…`), tức chính là team.
- Kết luận: team đã **bán khoảng 13,3K NET (giá vốn $1) qua các desk (thu ≥$5,4 triệu USDG, phần lớn đổi thành cổ phiếu trong Sleeve), rồi dùng một phần mua lại ~4,1K NET** khi giá giảm. Đây là lực đỡ giá chính trong 2 tuần qua. Nhịp mua vẫn duy trì $120–210K/ngày nhưng nguồn tiền có hạn.

### 5.2 Nhà đầu tư nhỏ lẻ
- 30 ngày: ~12,3K ví mua ròng (+$17,5 triệu), ~8,8K ví bán ròng (−$13,8 triệu). Dòng tiền ròng của nhóm "ví khác" là **+$3,7 triệu**, tức nhỏ lẻ vẫn bắt đáy suốt đà giảm. Một số ví mua ròng lớn: `0xec26…b064` (+$0,80 triệu), `0x4fbc…d717` (+$0,56 triệu), `0x36cd…d195` (+$0,51 triệu).
- 24 giờ (HoodScan): 817 ví mua và 939 ví bán; mua $0,93 triệu so với bán $0,99 triệu. 7 ngày: mua $8,35 triệu so với bán $8,64 triệu (**ròng −$0,29 triệu**).
- HoodScan (24 giờ tính đến 23:30 UTC): không còn tín hiệu "smart money"; 18 ví "chất lượng" gần như trung tính (−$1K). Nhóm "whale" (13 ví) **bán ròng −$153K**, nhóm nhỏ lẻ (1.491 ví) mua ròng +$85K. Cờ rủi ro: `thin_liquidity`.

### 5.3 Đòn bẩy (Loopback trên Morpho)
- Market wsNET/USDG (LLTV 62,5%): vay **$658K / cung $662K (utilization 99,4%)**, tài sản thế chấp ~2.060 wsNET (~8.400 NET, ~6% supply).
- Oracle định giá wsNET theo clamp(TWAP × 0,9, NAV, 5×NAV) × index, nên nhìn tổng thể khó bị thanh lý hàng loạt. Tuy vậy lãi vay sẽ cao vì utilization gần 100%.

### 5.4 Bot arbitrage
Giữa 29 pool (có pool bị thuế và pool không) luôn có bot arbitrage. Bot tạo volume lớn nhưng gần như trung tính về dòng tiền.

## 6. Phân bổ holder (NET + sNET + wsNET quy đổi)

| | |
|---|---|
| Số ví nắm giữ | ~11.100 |
| Top 1 | 2,6% (RWA Sleeve của team) |
| Top 10 / Top 100 | 12,6% / 42,9% (tính trên lượng do người dùng nắm giữ) |
| Morpho (thế chấp Loopback) | ~2.060 wsNET ≈ 8,4K NET |
| BondDepository (NET đang vest cho bonder) | ~1,4K NET |

Phân bổ khá phân tán. Không có cá voi ngoài team, nhưng ~92% supply đang stake và có thể rút ngay. Top 100 ở `data/holders_top100.csv`.

## 7. Giá và xu hướng

### 7.1 Diễn biến
- 17/7: niêm yết ~$3 (giá genesis $3). Đáy $15,8 vào 27/7.
- Hưng phấn 7/8 → 29/8: lên **$1.888** (CoinGecko; nến ngày trên pool v2 có high $2.021). Vốn hoá đỉnh ~$117 triệu (30/8). Premium từng lên 21× NAV.
- Từ 2/9: giảm theo bậc, đỉnh sau thấp hơn đỉnh trước ($1.893 → $1.070 ngày 17/9 → $883 ngày 22/9 → $510 → $436 → $357). Đáy sau thấp hơn đáy trước ($395 → $294 → $287 → $220 → **$210 ngày 3/10**, rồi hồi về $277).
- Chỉ báo: MA7 ≈ $394, MA20 ≈ $609, MA30 ≈ $648, giá nằm dưới cả ba. RSI14 ≈ 36. Volume pool v2 giảm từ $1–1,5 triệu/ngày đầu tháng 9 xuống còn $0,3–0,65 triệu/ngày.

### 7.2 Toán pha loãng (mô phỏng bằng các hằng số trong contract)
Supply có thể tăng ~1,8%/ngày khi premium > 1. Để giá đứng yên, cần khoảng **$650K/ngày tiền mới ròng** đổ vào.

| Kịch bản (giả định) | Ngày 7 | Ngày 14 | Ngày 21 |
|---|---|---|---|
| Market cap giữ nguyên | giá ~$250, NAV ~$165 | ~$225 / ~$162 | ~$206 / ~$159 |
| Giá đứng yên ở $277 | NAV ~$165 (P 1,68) | NAV ~$158 (P 1,75) | NAV ~$152 (P 1,83) |
| Giá trượt dần về 1,2× NAV | ~$238 / NAV ~$166 | ~$196 / ~$163 | ~$194 / ~$162 |
| Giá về đúng NAV (rebase và bond tự dừng) | NAV ~$171 | ~$172 | ~$173 |

Ý nghĩa: khi premium còn > 1, **chính NAV cũng giảm** (~0,2–0,5%/ngày). Khi giá về sát NAV, rebase và bond tự dừng, NAV ổn định quanh **$160–173**. Nếu team exercise 6.258 NET pTEAM, NAV giảm thêm ~4,5%.

### 7.3 Mốc giá quan trọng
- **Kháng cự:** $313–357 (đỉnh 2–3/10), **$341 (2× NAV, PremiumSeller bắt đầu bán)**, $420–436, $480–510.
- **Hỗ trợ:** $248, $210–220 (đáy 2–3/10), **$168–171 (NAV / giá mua lại của InverseBond)**. Đây là sàn có cơ chế, nhưng sàn này mua theo TWAP và giới hạn ~$69K mỗi 8 giờ, nên giá giao ngay có thể đâm thủng tạm thời khi bán tháo.

### 7.4 Kịch bản 1–3 tuần (xác suất chủ quan)

| Kịch bản | Xác suất | Vùng giá | Điều kiện / dấu hiệu |
|---|:-:|---|---|
| **Cơ sở: tiếp tục trôi xuống hoặc đi ngang yếu** | ~50% | $200–240 (1,2–1,4× NAV) | Bonder và rebase tiếp tục xả, team vẫn mua nhưng không đủ bù pha loãng, premium co dần làm rebase chậm theo |
| **Xấu: về sát NAV** | ~30% | $165–180 | Sleeve ngừng mua, team exercise pTEAM rồi bán, có tin xấu, Loopback giải chấp. Tại NAV, InverseBond hấp thụ ~$207K/ngày; rebase và bond về 0 |
| **Tốt: hồi về 2× NAV** | ~20% | $300–341 | Dòng tiền mới từ hệ sinh thái Robinhood Chain, sản phẩm mới, hoặc team mua mạnh hơn. Trên $341 có PremiumSeller và bond capacity bán ra |

Tỷ lệ lợi nhuận/rủi ro từ $277: **−38% xuống NAV** so với **+23% lên 2× NAV**. Muốn vượt xa 2× NAV cần một đợt hưng phấn mới, giống tháng 8.

### 7.5 Dấu hiệu on-chain nên theo dõi
- `Distributor.premium()` và `Treasury.backingPerToken()`: premium co về ~1,2 hay bật lại trên 2?
- **Số dư và lượng mua mỗi ngày của RWA Sleeve** `0x4987…c7cb`. Nếu Sleeve dừng mua, nến sẽ xấu đi.
- `pTEAM.exercised()` (hiện 13.320): **có tăng thêm không**? Có NET mới chuyển vào các desk (`0x99b6…`, `0xa84e…`, `0x70ea…`, `0x2f2f…`, `0x732b…`) không?
- Lượng claim từ `BondDepository` mỗi ngày.
- `InverseBond.capacityRemaining()`: giảm tức là đã có người bán xuống dưới NAV.
- Utilization market Loopback (`0xaa58…0589`) và thanh lý trên Morpho.

## 8. Rủi ro chính
1. **Rủi ro tập trung vào team.** Một EOA ký 1-of-1 cho Team Safe (map thuế, quản lý các desk, sở hữu option pTEAM) và cho RWA Sleeve (tài sản ròng ~$3,6 triệu, không thuộc NAV).
2. **pTEAM không hết hạn.** Team luôn mua được 15% float với giá $1, nên mỗi lần exercise rồi bán là chuyển giá trị từ holder sang team và kéo NAV/token xuống. Đã dùng 13,3K NET; còn 6,3K NET và trần tăng theo supply.
3. **Docs chưa khớp với chain** về nguồn inventory của desk, và có ít nhất bốn desk do Team Safe quản lý không được công bố địa chỉ.
4. **Thanh khoản mỏng** so với FDV; 92% supply có thể rút stake ngay.
5. **Đòn bẩy:** Sleeve vay trên Morpho thế chấp cổ phiếu; Loopback utilization 99,4%.
6. **Hệ sinh thái mới:** Robinhood Chain còn non trẻ. Rủi ro contract (Morpho/Steakhouse, DEX v4, router) và rủi ro oracle TWAP.
7. **Phản xạ kiểu OHM:** giai đoạn "(3,3)" thường kết thúc bằng việc premium co về NAV. NAV $22,5 triệu là thật (USDG), nhưng premium ~$14 triệu phía trên NAV thì không có gì bảo chứng.

## 9. Phương pháp và tái lập
- **Dữ liệu:** RPC `rpc.mainnet.chain.robinhood.com` (eth_getLogs, khoảng 10M block cho mỗi địa chỉ), `robinhood.drpc.org` (eth_call lịch sử, Multicall3), Sourcify (ABI/source), DexScreener, GeckoTerminal, CoinGecko, HoodScan (MCP công khai).
- **Phân loại dòng tiền** (`scripts/flows.py`): gom ~1,32 triệu Transfer NET, ~147K sNET và ~56K wsNET theo từng transaction (~573K transaction, ~41K ví). Mỗi địa chỉ được tính delta quy về NET (NET + sNET + wsNET × index). Pool, contract protocol và router (0x Settler, Relay, LiFi, Kyber, UniversalRouter…) được loại ra; phần còn lại là ví người dùng. Giao dịch có pool tham gia được tính là mua/bán. USD quy theo giá đóng cửa nến 4 giờ của pool v2.
- **Giới hạn:** HoodScan gán giao dịch theo `tx.from`, còn ở đây gán theo người nhận/gửi token, nên tổng mua/bán có thể khác HoodScan (một giao dịch có thể có nhiều "người dùng", ví dụ bot hay contract chưa gắn nhãn). Giá trị bán qua desk là ước tính (TWAP × 0,935 tại thời điểm chuyển NET vào desk). Thời gian được quy từ block theo các mốc đã binary-search (`data/block_anchors.json`). Xác suất các kịch bản là đánh giá chủ quan.

```bash
cd netnet-analysis/scripts
pip install requests pycryptodome eth-abi
python3 history.py 12                                             # NAV/premium/supply mỗi 12h -> data/history_12h.json
python3 fetch_transfers.py 0xca9c78dd337a67f6e0077f65f5e9218719d30edf ../raw/net_transfers.jsonl 10808643
python3 fetch_transfers.py 0xb773ec2c326b7f98a5a83fc098825492f020a4c7 ../raw/snet_transfers.jsonl 10808643
python3 fetch_transfers.py 0x63c12667638f2ae6fc6ae09b43d98ec84a8586ea ../raw/wsnet_transfers.jsonl 10808643
python3 trace_addr.py 0x3bb7a23316f82c0e984fa2e784846d8928a35f42 ../raw/team_transfers_raw.json
python3 trace_addr.py 0x498752d5fa0600cbd613074c151abe15b3fec7cb ../raw/sleeve_transfers.json
python3 flows.py && python3 holders.py && python3 team.py && python3 desk_usdg.py && python3 export.py
```
`raw/` (~300MB log) không được commit. `fetch_transfers.py` resume từ file `.cursor`, nên chạy lại chỉ tải phần mới. `flows.py` cần thêm `data/ds_token.json`, `data/gt_pools_all.json` và `data/gt_ohlcv_4h.json` (snapshot từ DexScreener/GeckoTerminal).

### File dữ liệu
| File | Nội dung |
|---|---|
| `data/latest_state.json` | Trạng thái protocol tại thời điểm snapshot |
| `data/protocol_history_12h.csv` | NAV, giá, premium, rebase, supply, stake, treasury, pTEAM mỗi 12h |
| `data/daily_flows.csv`, `data/weekly_supply_flows.csv` | Mint theo nguồn, claim bond/desk, stake/unstake, mua/bán theo ngày/tuần |
| `data/net_flow_by_category_30d.csv`, `data/top_traders_7d.csv`, `data/top_traders_30d.csv` | Ai mua, ai bán |
| `data/team_pteam_to_desks.csv`, `data/team_summary.json`, `data/sleeve_net_buys_daily.csv`, `data/desk_usdg_flows.csv` | Dòng tiền team, desk, RWA Sleeve |
| `data/holders_top100.csv`, `data/pools.csv` | Holder, pool |
