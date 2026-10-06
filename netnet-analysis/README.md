# NetNet (NET) và Robinhood Chain — phân tích on-chain, dòng tiền, dự báo

Token `0xCA9c78Dd337A67F6e0077F65F5E9218719d30eDf` trên **Robinhood Chain** (Arbitrum Orbit L2, chainId 4663).
Snapshot: **2026-10-06 ~11:40 UTC** (bản trước: 2026-10-03). Số liệu đọc trực tiếp từ chain (RPC công khai, contract verified trên Sourcify, bridge L1 trên Ethereum), đối chiếu với DefiLlama, DexScreener, GeckoTerminal, CoinGecko, HoodScan và tin tức.

> Đây là phân tích dữ liệu, không phải lời khuyên đầu tư. NET là token rebase kiểu OlympusDAO trên một chain mới. Bạn có thể mất phần lớn số vốn bỏ vào.

---

## TL;DR

**Thị trường chung: thuận lợi.** BTC $86,3K (+7% trong 30 ngày, sát đỉnh 90 ngày), ETH $2.715 (+8%), Fear & Greed **73 (Greed)**. Vậy cú sập của token gốc Robinhood Chain **là chuyện riêng của hệ sinh thái**, không do thị trường chung.

**Robinhood Chain: tiền vẫn nằm trên chain nhưng hết đuổi theo đầu cơ.**

| Chỉ số | Hiện tại | So với đỉnh / 30 ngày |
|---|---|---|
| TVL DeFi | $1,05 tỷ (#9/468 chain) | +16% / 30 ngày nhưng tăng chậm dần (+3,9% / 7 ngày) |
| Stablecoin | $1,113 tỷ (đỉnh mới): USDG $713M, USDe $361M | Gần như đi ngang từ giữa tháng 9 ($1,088 tỷ ngày 15/9) |
| Volume DEX / tuần | $8,3 tỷ | **−55%** so với đỉnh $18,4 tỷ (2–8/9); đỉnh ngày $3,5–3,7 tỷ (4/9) |
| Phí / tuần | $28,7M | **−81%** so với đỉnh $153M |
| ETH khoá trong bridge L1 | 276K ETH (~$750M) | **−12%** so với đỉnh 313,6K (17/9), riêng 24 giờ qua −11,8K ETH |
| Token gốc (30 ngày) | PONS −57%, AI −44%, CASHCAT −33%, NET −75% | Lượng meme mới phát hành trên Pons giảm 72%, phí meme giảm 78% |

**NET**

| | Hiện tại (6/10) | 3/10 |
|---|---|---|
| Giá | **~$224** (−88% từ đỉnh $1.888; −47% / 7 ngày, −75% / 30 ngày) | $277 |
| NAV (USDG thật bảo chứng / NET) | **$167,8** | $170,5 |
| Premium (giá / NAV) | **1,33×** | 1,64× |
| Sàn mua lại (InverseBond) | **$165,2** (~$72K mỗi 8 giờ) | $167,9 |
| Pha loãng | **~1.800 NET/ngày (~1,3%/ngày)**: rebase ~770 + bond ~1.030 | ~2.390 NET/ngày |
| Dòng tiền DEX 7 ngày (HoodScan) | mua $5,65M, bán $6,24M, **ròng −$0,59M** | ròng −$0,29M |

- **Ai bán:** bonder (mua bond rẻ hơn 3% rồi xả, ~900 NET/ngày; ròng −$5,9M trong 30 ngày), staker chốt rebase, cá voi (−$158K trong 24 giờ). Team vẫn bán NET qua "bond desk" (nạp thêm 100 NET ngày 5/10).
- **Ai mua:** **chủ yếu là team.** RWA Sleeve của team mua lại **5.108 NET (~$2,08M)** từ 18/9 đến 5/10, chiếm +$954K trong số mua ròng 7 ngày (gấp ~9 lần ví đứng thứ hai). Bỏ team ra, dòng tiền ròng 7 ngày khoảng **−$1M**.
- **Tín hiệu mới quan trọng nhất:** lực mua của team **gần như đã cạn tiền**. Sleeve còn ~$10K USDG; các market Morpho thế chấp cổ phiếu đã dùng **100%** vốn nên không vay thêm được; cổ phiếu còn trong ví ~$135K. Sleeve không mua thêm từ 19:25 UTC ngày 5/10.
- **Dự báo 1–3 tuần:** cơ sở (~50%) là trôi về **$180–215** (1,1–1,3× NAV); xấu (~30%) là test NAV **$160–168**; tốt (~20%) là hồi **$260–295**. Rủi ro/lợi nhuận đã cân hơn trước: **−25% xuống NAV**, **+50% lên 2× NAV**. Nhưng xu hướng vẫn giảm và người mua lớn nhất đã hết tiền.

---

## A. Thị trường chung

| | Giá | 7 ngày | 30 ngày | 90 ngày |
|---|---:|---:|---:|---:|
| BTC | $86.280 | +3,2% | +7,4% | +38,6% (đỉnh 90 ngày $86,6K) |
| ETH | $2.715 | +1,4% | +8,0% | +55,8% |
| Tổng vốn hoá crypto | $2,92T (−2,6% / 24h), BTC dominance 59,3% | | | |
| Fear & Greed | **73 (Greed)**; trung bình 7 ngày 70, 30 ngày 68 | | | |

Thị trường chung đang ở pha tăng (risk-on). Trong khi đó, token gốc Robinhood Chain giảm 30–75% trong 30 ngày, tức là **tương quan âm với thị trường chung**. Đây là pha hạ nhiệt sau đợt hype ra mắt chain, không phải pha "risk-off" toàn thị trường. Ý nghĩa: nếu RH chain có câu chuyện mới, tiền có sẵn để quay lại; nhưng hiện tại tiền đang chảy sang nơi khác.

## B. Dòng tiền vào Robinhood Chain

Mainnet chạy từ 1/7/2026. Số liệu tuần (DefiLlama; ETH bridge đo trên Ethereum; file `data/market/rh_chain_weekly.csv`):

| Tuần | Volume DEX | Phí | TVL cuối tuần | Stablecoin | ETH trong bridge L1 | BTC |
|---|---:|---:|---:|---:|---:|---:|
| 8–14/7 | $5,4B | $37M | $160M | $327M | 85,5K | $62K |
| 5–11/8 | $3,7B | $26M | $479M | $611M | 153,4K | $64K |
| 26/8–1/9 | $9,4B | $73M | $729M | $797M | 219,4K | $79K |
| **2–8/9** | **$18,4B** (đỉnh) | **$153M** (đỉnh) | $900M | $1.001M | 292,2K | $79K |
| 9–15/9 | $13,8B | $88M | $930M | $1.088M | 309,0K | $78K |
| 16–22/9 | $10,6B | $52M | $995M | $1.106M | 309,0K (đỉnh 313,6K ngày 17/9) | $87K |
| 23–29/9 | $9,4B | $37M | $1.010M | $1.065M | 297,0K | $83K |
| **30/9–6/10** | **$8,3B** | **$29M** | **$1.050M** | **$1.113M** | **276,0K** | $86K |

Nhận xét:
1. **Tiền vẫn "đậu" trên chain.** TVL và stablecoin đều ở đỉnh. USDG (Paxos, phát hành trực tiếp trên chain) chiếm $713M (+11% / 30 ngày), USDe (Ethena) $361M (+13%). Phần lớn là tiền gửi lấy lãi (vault Steakhouse USDG trên Morpho, Robinhood Earn). Treasury của NetNet cũng gửi $16,1M vào đây.
2. **Hoạt động đầu cơ giảm mạnh.** Volume DEX giảm 55% và phí giảm 81% so với đỉnh. Theo KuCoin (4/10): lượng token mới phát hành trên Pons V2 giảm 72% (còn ~6.768/ngày), phí ngày giảm 78% (từ $6,87M xuống $1,48M). Có trường hợp một nhóm phát hành 56 token meme và thu lời ~$15,5M từ người mua.
3. **ETH bắt đầu rút ra.** ETH trong bridge chính thức trên Ethereum (`0xDf87…64b3`) giảm từ 313,6K (17/9) xuống 276K (−37,6K ETH ≈ −$100M), riêng 24 giờ qua −11,8K ETH. Vì rút từ L2 về L1 có thời gian chờ, các lệnh rút này phản ánh quyết định từ khoảng 1 tuần trước. ERC20 bridge qua đường chính thức không đáng kể (USDC/USDT chỉ vài nghìn USD).
4. **Cổ phiếu token hoá tăng chậm và còn nhỏ:** 191 mã, vốn hoá on-chain $156M, thanh khoản $92M, volume 24h $99M (NVDA $36M, SPY $15M). Stock token không mở cho người dùng Mỹ.
5. **Token gốc hệ sinh thái (CoinGecko, 30 ngày):** PONS −57% (vốn hoá $268M), AI −44% ($111M), CASHCAT −33% ($151M), NPC −4%, LIT (Lighter) −15%. HoodScan theo dõi 1.293 meme đang có thanh khoản; 24 giờ qua tổng dòng tiền ròng −$0,84M.

Tin tức và chất xúc tác:
- **HOOD Summit (cuối tháng 9):** công bố AI trading agent, giao dịch cổ phiếu cuối tuần, perps qua Bitstamp. **Không có gì trực tiếp cho token gốc trên chain.**
- **Robinhood báo cáo quý 3 vào 27/10/2026** (sau giờ đóng cửa). Đây là dịp có thể công bố số liệu chain hoặc kế hoạch mới.
- Robinhood Chain chiếm 53% doanh thu tháng 9 của Uniswap. Robinhood Wallet đã mở truy cập hơn 190 stock token. Ví Robinhood chỉ chiếm 1–2% giao dịch on-chain.

## C. NET: pool và thanh khoản

30 pair, tổng thanh khoản ~**$1,10M** (giảm từ $1,19M), volume 24h ~$1,5M (giảm từ $2,3M).

| Pool | DEX | Thanh khoản | Vol 24h | Thuế 5% |
|---|---|---:|---:|:-:|
| [`0x59F9…5B54`](https://dexscreener.com/robinhood/0x59f95461e68e0c77605299791e1449f175165b54) NET/USDG: canonical, oracle TWAP, 97,6% LP thuộc Treasury | Uniswap v2 | $383K (854 NET + $191K) | $0,23M | ✅ |
| [`0x99e7…1673`](https://dexscreener.com/robinhood/0x99e70a5b06215e5d2f3bec773b4f59c008fc1673) NET/USDG 1% | Up v3 | $226K | $0,54M | ❌ |
| `0x0d66…deb3` NET/USDG 0,9% | Uniswap v4 | $148K | $0,06M | ❌ |
| `0x4030…170d` NET/USDG | Uniswap v4 | $103K | $0,26M | ❌ |
| `0x813f…3862` NET/USDG 1% | Ramses v3 | $97K | $0,11M | ❌ |
| `0x146a…18D3` NET/USDG | Alandale | $18K | $0,13M | ❌ |

Danh sách đầy đủ ở `data/pools.csv`. Chỉ pool v2 bị đánh thuế 5%, nên ~85% volume đi qua các pool không thuế.

## D. NET: cơ chế và trạng thái protocol

Các hằng số dưới đây đã đối chiếu `Constants.sol` trên Sourcify.

| Thành phần | Quy tắc | Hiện tại (6/10) |
|---|---|---|
| NAV | RFV / supply; RFV = USDG liquid + USDG trong Morpho × 0,98 + POL | **$167,76**. RFV **$23,08M** ($7,24M liquid + $16,14M Steakhouse/Morpho) |
| Rebase (8h) | 0,45% × clamp((P−1)/0,75, 0, 1) | P = 1,33 → **0,197%/epoch** (0,59%/ngày) ≈ **770 NET/ngày**. Đã giảm một nửa so với 3/10 |
| Bond | giá max(TWAP × 0,97, NAV), vest 2 ngày, 0,25% supply/epoch | ~**1.030 NET/ngày**; còn 1.603 NET đang vest |
| InverseBond | mua NET ở NAV × 0,985 rồi đốt; 1% USDG liquid/epoch | **$165,24**, ~$72K/epoch. Chưa từng được dùng đáng kể |
| PremiumSeller | bán khi TWAP > 2× NAV ($335) | tắt |
| pTEAM | team mint với giá $1, trần 15% float, không hết hạn | đã dùng 13.320; **có thể mint ngay 7.066 NET** (~$1,6M). NAV sẽ giảm ~4,9% xuống ~$159,6 |
| Supply | | 137.554 NET (+4,3% so với 3/10), **92,2% đang stake** |

Nguồn của toàn bộ NET đã mint: rebase 66,7K (48%), bond 33,7K (24%), genesis 21,7K (16%), **pTEAM 13,3K (10%)**, PremiumSeller 2,3K (2%).

NAV đạt đỉnh $175,5 (27/9) rồi giảm dần ($170,5 ngày 3/10, $167,8 hiện tại), vì rebase pha loãng nhanh hơn lượng USDG mà bond mang vào. Bảng 12 giờ ở `data/protocol_history_12h.csv`.

## E. Ai đang bán

1. **Bonder (nguồn bán lớn nhất và đều đặn nhất).** Claim ~885–960 NET/ngày; 7 ngày 7.043 NET, 30 ngày 27.623 NET. 30 ngày qua, nhóm ví có claim bond: 353 ví bán ròng −$10,1M, 401 ví mua ròng +$4,2M, **tổng ròng −$5,9M**. Top bán 7 ngày cũng là bonder: `0xf357…401d` (−$247K, claim 825 NET), `0x7c94…f3c0` (−$164K), `0x708d…b1a9` (−$107K).
2. **Staker chốt rebase.** Rebase mint 1.590/ngày (3/10), sau đó giảm còn ~1.000 (5/10) và ~770 (hiện tại). Không có cooldown khi rút stake.
3. **Cá voi.** HoodScan 24 giờ: 9 ví cá voi mua $100K, bán $258K (**−$158K**). Không còn ví "smart money" nào mua.
4. **Team, qua bond desk.** Từ 24/7 đến 28/9, team mint 13.320 NET bằng pTEAM với giá $1. 192/200 giao dịch chuyển NET thẳng vào desk ngay trong cùng một lệnh, ước tính bán ra ~$7,1M. Người đăng ký đã trả **$5,46M USDG** vào các desk: chỉ $0,68M (12,5%) vào Treasury, còn $4,78M qua router `0xc941…` để mua cổ phiếu token hoá cho RWA Sleeve. **Ngày 5/10, Sleeve tiếp tục nạp 100 NET vào desk `0x732b`** (không có trong danh sách chính thức) để bán. Chi tiết ở `data/team_pteam_to_desks.csv` và `data/desk_usdg_flows.csv`.

## F. Ai đang mua

1. **RWA Sleeve của team** (`0x4987…c7cb`; owner duy nhất là EOA `0xe7e8…96f6`, cũng là owner 1-of-1 của Team Safe; HoodScan liệt kê ví này là "holder lớn nhất"):

| Giai đoạn | NET | USD |
|---|---:|---:|
| 18–27/9 | 1.122 | $680K |
| 28/9 | 834 | $378K |
| 29/9–2/10 | 1.755 | $648K |
| 3/10 | 429 | $121K |
| 4/10 | 315 | $89K |
| 5/10 (lần cuối lúc 19:25 UTC) | 652 | $160K |
| **Tổng** | **5.108** | **~$2,08M** (giá vốn trung bình ~$406) |

   - **Tài sản hiện tại:** 652 NET + 813,5 wsNET (≈3.413 NET), tổng ~4.070 NET (~$0,91M, 3,4% lượng NET do người dùng nắm giữ). Cổ phiếu trong ví ~$135K, **USDG ~$10K**. Trên Morpho: thế chấp cổ phiếu **$4,10M**, nợ **$1,58M** (LTV 38,5%).
   - **Vì sao nói lực mua đã cạn:** các market Morpho NVDA/SPCX/AAPL/GOOGL đều **dùng 100% vốn** (không còn USDG để vay). Lãi suất ở mức utilization 100% sẽ tăng dần theo thuật toán AdaptiveCurve. Muốn mua tiếp, team phải bán cổ phiếu hoặc nạp tiền mới từ bên ngoài.
2. **Nhỏ lẻ:** 30 ngày có 11,4K ví mua ròng +$15,4M, 7,9K ví bán ròng −$11,7M; nhóm "ví khác" ròng **+$3,7M**. Nhưng 24 giờ qua nhỏ lẻ chỉ mua ròng +$15K (HoodScan), và số người bán đông hơn người mua (915 so với 668).
3. **Đòn bẩy Loopback (Morpho):** đang vay $660K / cung $717K (utilization 92%, giảm từ 99%), thế chấp 2.229 wsNET (~9.350 NET, ~7% supply). Định giá thế chấp có sàn bằng NAV, nên rủi ro thanh lý hàng loạt thấp.

## G. Phân bổ holder

~11.000 ví. Top 10 nắm 13,2%, top 100 nắm 43,8% lượng NET do người dùng nắm giữ (NET + sNET + wsNET quy đổi). Top 1 là Sleeve của team (3,4%). 92% supply đang stake và có thể rút bất cứ lúc nào. Chi tiết ở `data/holders_top100.csv`.

## H. Giá và dự báo

### H.1 Kỹ thuật
- Nến ngày (pool v2): 3/10 L $210 C $280 → 4/10 L $220 C $236 → 5/10 L **$201** C $243 → 6/10 ~$224. Đỉnh sau thấp hơn đỉnh trước ($313 → $294 → $261 → $251).
- MA7 $297, MA20 $522, MA30 $583, giá nằm dưới cả ba. RSI14 34. Volume pool v2 chỉ còn $0,1–0,25M/ngày (so với $0,65M ngày 2/10).
- Vùng $200–220 đã đỡ giá ba ngày liên tiếp (đáy $210, $220, $201).

### H.2 Toán pha loãng (mô phỏng từ hằng số contract và trạng thái hiện tại)
Cần ~**$400K/ngày** tiền mới ròng chỉ để giữ giá đứng yên.

| Giả định | Ngày 7 | Ngày 14 | Ngày 21 |
|---|---|---|---|
| Market cap giữ nguyên | $208 (NAV $165) | $192 (NAV $163) | $180 (NAV $162) |
| Giá đứng yên $224 | NAV $165 | NAV $161 | NAV $157 |
| Premium co về 1,15× trong 10 ngày | $201 | $189 | $188 |
| Giá về NAV (rebase và bond tự dừng) | $168 | $169 | $170 |

### H.3 Kịch bản 1–3 tuần (xác suất chủ quan)

| Kịch bản | Xác suất | Vùng giá NET | Điều kiện / dấu hiệu |
|---|:-:|---|---|
| **Cơ sở: trôi xuống / đi ngang yếu** | ~50% | **$180–215** (1,1–1,3× NAV) | Team ngừng mua vì hết tiền; bond tiếp tục xả ~1.000 NET/ngày; premium co dần làm rebase chậm lại; hệ sinh thái RH tiếp tục hạ nhiệt |
| **Xấu: về NAV** | ~30% | **$160–168** | Team exercise pTEAM (7K NET) rồi bán qua desk, hoặc Sleeve phải bán NET để trả nợ Morpho khi lãi vay tăng; ETH tiếp tục rút khỏi chain; meme RH sập thêm. Tại NAV, InverseBond hấp thụ ~$217K/ngày; rebase và bond tự về 0 |
| **Tốt: hồi về 1,55–1,75× NAV** | ~20% | **$260–295** | Dòng tiền mới vào RH chain (báo cáo quý 3 ngày 27/10, sản phẩm hoặc thị trường mới cho stock token), BTC/ETH tiếp tục lên đỉnh, team nạp tiền mới để mua. Trên $294 rebase chạy tối đa; trên $335 PremiumSeller bán ra |

Từ $224: **−25% xuống NAV** so với **+50% lên 2× NAV**. Rủi ro/lợi nhuận cân hơn hôm 3/10, vì giá đã gần NAV và NAV là USDG thật. Nhưng trong ngắn hạn cung vẫn lớn hơn cầu, và người mua chính (team) đã hết tiền. **Điểm "an toàn" theo cơ chế là vùng NAV (~$160–170): ở đó protocol tự mua lại và dừng pha loãng.**

### H.4 Robinhood Chain 2–4 tuần tới
- **Cơ sở:** tiếp tục "bình thường hoá sau hype". Volume DEX quanh $0,8–1,2 tỷ/ngày, phí thấp, token gốc dao động hoặc giảm tiếp với các nhịp pump ngắn. Stablecoin đi ngang hoặc tăng nhẹ (gửi lấy lãi). ETH tiếp tục rút dần.
- **Có thể đảo chiều nếu:** Robinhood công bố số liệu hoặc ưu đãi mới cho chain (27/10), stock token mở thêm thị trường, có chương trình incentive mới, hoặc tiền risk-on từ BTC/ETH tràn sang. Tín hiệu cần chờ là volume DEX tuần quay lại trên $10 tỷ và stablecoin tăng tiếp.

### H.5 Theo dõi on-chain
- **Số dư USDG và giao dịch của RWA Sleeve** `0x4987…c7cb`: có mua lại không, có bán NET hay rút wsNET không. Theo dõi thêm nợ Morpho.
- `pTEAM.exercised()` (đang 13.320) và NET chuyển vào các desk (`0x99b6…`, `0xa84e…`, `0x70ea…`, `0x2f2f…`, `0x732b…`).
- `Distributor.premium()`: < 1,1 thì rebase gần như dừng; > 1,75 thì rebase tối đa.
- `InverseBond.capacityRemaining()`: giảm tức là đã có người bán xuống dưới NAV.
- ETH trong bridge L1 và stablecoin trên chain (`scripts/rh_chain.py`).

## I. Rủi ro chính
1. **Tập trung vào team:** một EOA ký 1-of-1 cho Team Safe và RWA Sleeve. pTEAM không hết hạn, team luôn mint được 15% float với giá $1.
2. **Docs chưa khớp với chain:** inventory của desk đến từ pTEAM chứ không phải "mua trên thị trường", và có ít nhất 4 desk do Team Safe quản lý không được công bố địa chỉ.
3. **Thanh khoản mỏng** ($1,1M) so với FDV ~$31M; 92% supply có thể rút stake ngay.
4. **Đòn bẩy của team:** Sleeve nợ $1,58M trên các market Morpho đã dùng 100% vốn.
5. **Hệ sinh thái mới đang hạ nhiệt:** volume −55%, phí −81%, ETH rút ra. Rủi ro contract (Morpho/Steakhouse, DEX, router) và rủi ro oracle TWAP.
6. **Phản xạ kiểu OHM:** premium thường co về NAV sau giai đoạn hưng phấn. NAV $23,1M là USDG thật, nhưng phần ~$7,7M vốn hoá phía trên NAV thì không có gì bảo chứng.

## J. Phương pháp và tái lập
- **Nguồn:** RPC `rpc.mainnet.chain.robinhood.com` (eth_getLogs) và `robinhood.drpc.org` (eth_call lịch sử, Multicall3), `eth.drpc.org` (số dư bridge trên L1), Sourcify, DefiLlama, DexScreener, GeckoTerminal, CoinGecko, alternative.me, HoodScan (MCP công khai), tin tức (KuCoin, Coingabbar, Nasdaq/GlobeNewswire).
- **Phân loại dòng tiền** (`scripts/flows.py`): ~587K transaction, ~42K ví. Delta mỗi địa chỉ được quy về NET (NET + sNET + wsNET × index). Pool, contract protocol và router được loại ra, phần còn lại là ví người dùng. USD quy theo nến 4 giờ. Thời gian quy từ block theo mốc binary-search (`data/block_anchors.json`).
- **Giới hạn:** HoodScan gán giao dịch theo `tx.from`, ở đây gán theo người gửi/nhận token, nên số tổng có thể lệch. Giá trị bán qua desk là ước tính. Xác suất các kịch bản là đánh giá chủ quan.

```bash
cd netnet-analysis/scripts
pip install requests pycryptodome eth-abi
python3 anchors.py                                                 # mốc block <-> thời gian
python3 history.py 12                                              # NAV/premium/supply mỗi 12h
python3 fetch_transfers.py 0xca9c78dd337a67f6e0077f65f5e9218719d30edf ../raw/net_transfers.jsonl 10808643
python3 fetch_transfers.py 0xb773ec2c326b7f98a5a83fc098825492f020a4c7 ../raw/snet_transfers.jsonl 10808643
python3 fetch_transfers.py 0x63c12667638f2ae6fc6ae09b43d98ec84a8586ea ../raw/wsnet_transfers.jsonl 10808643
python3 trace_addr.py 0x3bb7a23316f82c0e984fa2e784846d8928a35f42 ../raw/team_transfers_raw.json
python3 trace_addr.py 0x498752d5fa0600cbd613074c151abe15b3fec7cb ../raw/sleeve_transfers.json
python3 flows.py && python3 holders.py && python3 team.py && python3 desk_usdg.py && python3 export.py
python3 rh_chain.py                                                # dòng tiền Robinhood Chain + vĩ mô
```
`raw/` (~300MB log) không được commit. `fetch_transfers.py` resume từ file `.cursor`. Chạy `team.py` **sau khi** hai lệnh `trace_addr.py` đã xong.

### File dữ liệu
| File | Nội dung |
|---|---|
| `data/latest_state.json`, `data/protocol_history_12h.csv` | Trạng thái protocol hiện tại và lịch sử 12h |
| `data/daily_flows.csv`, `data/weekly_supply_flows.csv` | Mint theo nguồn, claim bond/desk, stake/unstake, mua/bán theo ngày/tuần |
| `data/net_flow_by_category_30d.csv`, `data/top_traders_7d.csv`, `data/top_traders_30d.csv` | Ai mua, ai bán |
| `data/team_summary.json`, `data/team_pteam_to_desks.csv`, `data/sleeve_net_buys_daily.csv`, `data/desk_usdg_flows.csv` | Team, desk, RWA Sleeve |
| `data/holders_top100.csv`, `data/pools.csv` | Holder, pool |
| `data/market/rh_chain_weekly.csv`, `data/market/rh_chain_summary.json`, `data/market/rh_l1_bridge_eth.json`, `data/market/rh_stables_breakdown.json` | Dòng tiền Robinhood Chain |
| `data/market/market_snapshot.json` | BTC/ETH, Fear & Greed, token hệ sinh thái, stock token, meme (câu trả lời API thô nằm ở `raw/market/`, không commit) |
