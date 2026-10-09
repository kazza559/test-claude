# NetNet (NET) và Robinhood Chain — phân tích on-chain, dòng tiền, dự báo

Token `0xCA9c78Dd337A67F6e0077F65F5E9218719d30eDf` trên **Robinhood Chain** (Arbitrum Orbit L2, chainId 4663).
Snapshot: **2026-10-09 ~13:30 UTC** (các bản trước: 6/10 và 3/10). Số liệu đọc trực tiếp từ chain (RPC công khai, contract verified trên Sourcify, bridge L1 trên Ethereum), đối chiếu với DefiLlama, DexScreener, GeckoTerminal, CoinGecko, HoodScan và tin tức.

> Đây là phân tích dữ liệu, không phải lời khuyên đầu tư. NET là token rebase kiểu OlympusDAO trên một chain mới. Bạn có thể mất phần lớn số vốn bỏ vào.

Bản HTML có biểu đồ: [`report.html`](report.html) (build bằng `scripts/build_report.py` từ `report.template.html`), cũng được publish tại https://claude.ai/artifact/1s4mmumZGorDN3euAZMLid.

---

## TL;DR

**Thị trường chung: chuyển sang phòng thủ.** BTC từ ~$85,8K (6/10) xuống ~$81,7K cuối ngày 8/10 (thấp nhất kể từ 21/9), hiện ~$83K. ETH $2.500 (−6% / 7 ngày). Fear & Greed giảm từ 73 xuống **59**. Nguyên nhân chính: dầu Brent vượt $100 (căng thẳng ở eo Hormuz), lợi suất trái phiếu Mỹ 10 năm lên ~5,3%, ETF rút ròng, ~$609M vị thế đòn bẩy bị thanh lý trong 24 giờ ngày 7/10. Ba ngày trước thị trường chung còn là điểm tựa, giờ thành gió ngược.

**Robinhood Chain: tiền không rời chain, nhưng đã chuyển từ đầu cơ sang gửi lấy lãi.** Đo on-chain, tuần 3–9/10:

| Dòng tiền | Tuần này | Xu hướng |
|---|---:|---|
| Stablecoin mới (USDG + USDe + U) | **+$8,8M** (tổng $1,090 tỷ) | Đi ngang từ giữa tháng 9. Hai tuần hype: +$198M và +$117M |
| ├ USDG (Paxos, tiền giao dịch) | −$5,3M | −$31M (−4,3%) so với đỉnh $726M ngày 15/9 |
| └ USDe (Ethena) | +$14,0M | Đỉnh mới $368M, chủ yếu đi vào vòng vay trên Morpho |
| Gửi vào Robinhood Earn (vault Steakhouse USDG) | **+$23,2M** | Đỉnh mới **$537M = 77% lượng USDG**, tuần nào cũng +$12–26M |
| Cổ phiếu token hoá (mint trừ burn, theo giá hiện tại) | **−$11,5M** | Rút ròng 4 tuần liên tiếp: $181M (15/9) còn $150M (−17%) |
| ETH qua bridge chính thức từ Ethereum | **−12.088 ETH (−$30M)** | Rút ròng 3 tuần liên tiếp, tổng −33,3K ETH (−$83M) từ đỉnh 16/9 |
| Volume DEX / phí | $7,3 tỷ / $22,6M | −55% / −82% so với đỉnh |
| Giao dịch người dùng (ước tính) | ~5,9 triệu/ngày | −48% so với tuần 29/8–4/9; gas dùng −70% |

Cộng stablecoin, cổ phiếu token hoá và ETH: **tiền mới vào chain đã âm 3 tuần liền** (−$30M, −$22M, −$33M), sau hai tuần hype +$474M và +$243M. Phần tiền đầu cơ (ETH, USDG, cổ phiếu token hoá, phí launchpad) đang chảy ra; phần tiền gửi lấy lãi (Earn/Morpho, USDe) vẫn chảy vào. **93% khoản vay USDG trên Morpho là vòng vay stablecoin** (thế chấp USDe, syrupUSDG); vay thế chấp cổ phiếu token hoá chỉ $1,67M, và 95% trong số đó là của team NetNet.

**NET**

| | 9/10 | 6/10 |
|---|---|---|
| Giá | **~$216** (−89% từ đỉnh $1.888; −25% / 7 ngày; −66% / 30 ngày). Ba ngày qua chạy từ $184 đến $362 | $224 |
| NAV (USDG thật bảo chứng / NET) | **$164,84** | $167,76 |
| Premium (giá / NAV) | **1,31×** (vọt lên 1,91× ngày 7/10 rồi co lại) | 1,33× |
| Sàn mua lại (InverseBond) | **$162,37** (~$75K mỗi 8 giờ) | $165,24 |
| Supply | 144.739 NET (**+5,2% trong 3 ngày**) | 137.554 |
| Pha loãng | **~1.850 NET/ngày (1,28%/ngày)**, cần ~$400K tiền mới ròng mỗi ngày để giữ giá | ~1.800 NET/ngày |
| Dòng tiền DEX 7 ngày (HoodScan) | mua $4,91M, bán $5,02M, **ròng −$0,11M** | ròng −$0,59M |

- **Ai bán:** bonder (claim ~1.000 NET/ngày; 30 ngày ròng −$5,9M), holder lâu năm (`0xf41b…9e3b` xả 686 NET, ~$139K, trong 3 lệnh), cá voi (−$171K trong 24 giờ), và người lướt sóng mua đỉnh ngày 7/10 rồi bán ra.
- **Ai mua:** vẫn chủ yếu là team. Ngày 6/10 RWA Sleeve **vay $113K USDG trên Loopback, thế chấp bằng chính 813,5 wsNET của mình**, mua thêm 435 NET (~$126K) trong ngày 6–7/10, rồi **dừng hẳn từ 15:51 UTC ngày 7/10**. Số USDG còn lại: **$340**. Nhỏ lẻ mua ròng nhẹ (+$66K trong 24 giờ).
- **Cú pump ngày 7/10:** giá từ $272 lên $362 trong 4 giờ trên thanh khoản mỏng (người mua lớn nhất là Sleeve). Premium vọt lên 1,91× làm rebase chạy tối đa (1.800 NET/ngày), sau đó giá rơi về $184–231. Pump ngắn chỉ làm supply tăng nhanh hơn.
- **Dự báo 1–3 tuần (xác suất chủ quan):** cơ sở ~50% **$175–210**; xấu ~30% **$155–168** (về NAV; NAV có thể giảm còn ~$156 nếu team mint 8.133 NET pTEAM); tốt ~20% **$240–290**. Nghiêng giảm: người mua lớn nhất đã hết tiền, thị trường chung chuyển phòng thủ, RH chain mất dòng tiền đầu cơ. Vùng NAV (~$160–165) vẫn là sàn theo cơ chế.

---

## A. Thị trường chung

| | Giá | 7 ngày | 30 ngày | 90 ngày |
|---|---:|---:|---:|---:|
| BTC | $83.030 | −1,7% | +6,1% | +30,2% (đỉnh 90 ngày $86,6K) |
| ETH | $2.500 | −6,3% | +1,3% | +39,8% |
| Tổng vốn hoá crypto | $2,81T (−2,6% / 24h), BTC dominance 59,2% | | | |
| Fear & Greed | **59** (73 ngày 6/10); trung bình 7 ngày 67, 30 ngày 67 | | | |

- Theo [Fortune](https://fortune.com/article/price-of-bitcoin-10-09-2026/), sáng 9/10 BTC ở ~$82,4K. [Analytics Insight](https://www.analyticsinsight.net/price-analysis/crypto-prices-today-bitcoin-holds-near-usd-82400-as-etf-outflows-oil-spike-test-support) cho rằng hỗ trợ đã lùi về $80K, kháng cự $85K; ETF rút ròng và giá dầu là hai yếu tố quyết định BTC lấy lại $83K hay test $77K.
- Ngày 7/10: Brent vượt $101,5 sau tin Iran tấn công tàu chở dầu gần eo Hormuz, lợi suất Mỹ 10 năm lên ~5,31%, BTC thủng $84K ([ARY News](https://arynews.tv/en/bitcoin-falls-under-84k-as-oil-jumps)), ~$609M vị thế đòn bẩy bị thanh lý trong 24 giờ ([NewsBytes](https://www.newsbytesapp.com/news/business/bitcoin-falls-25-to-83470-amid-609-million-liquidations-altcoins-fall/tldr)). Chứng khoán Mỹ cũng giảm hai phiên liên tiếp khi nhóm AI bị bán ([Yahoo Finance](https://finance.yahoo.com/markets/live/stock-market-today-thursday-october-8-dow-sp-500-nasdaq-080537884.html)).

**Ý nghĩa:** hôm 6/10, cú sập của token gốc RH chain còn là "chuyện riêng của hệ sinh thái" vì thị trường chung đang risk-on. Bây giờ thị trường chung cũng chuyển phòng thủ: tiền đầu cơ ít có lý do quay lại RH chain trong ngắn hạn, và mọi nhịp hồi của token gốc sẽ khó giữ.

## B. Dòng tiền Robinhood Chain (phân tích sâu)

Mainnet chạy từ 1/7/2026. Phần này đo **tiền thật đi vào/ra chain** trực tiếp on-chain (tổng cung stablecoin, vault Earn, Morpho, cổ phiếu token hoá, bridge ETH trên Ethereum, số giao dịch), rồi đối chiếu với DefiLlama. Script: `scripts/rh_flows.py`, `scripts/rh_flow_summary.py`, `scripts/rh_protocols.py`, `scripts/rh_chain.py`.

### B.1 Tiền mới vào/ra chain theo tuần

Tuần theo DefiLlama (thứ Sáu đến thứ Năm). Số on-chain tính từ 00:00 UTC ngày đầu tuần đến 00:00 UTC sau ngày cuối; tuần cuối tính đến 13:20 UTC ngày 9/10. ETH quy USD theo giá hiện tại ($2.500). File `data/market/rh_flow_weekly.csv`.

| Tuần kết thúc | Stablecoin | trong đó USDG | USDe | Earn vault | Vay USDG Morpho | Cổ phiếu token hoá | ETH bridge | Giao dịch/ngày | Volume DEX | Phí |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 17/7 | +$95M | +$77M | +$18M | +$67M | +$41M | +$6M | +40,9K (+$102M) | 8,4M | $5,7B | $39M |
| 14/8 | +$47M | +$16M | +$31M | +$35M | +$52M | +$3M | +19,2K (+$48M) | 13,6M | $3,6B | $26M |
| 28/8 | +$36M | +$20M | +$16M | +$47M | +$49M | +$12M | +18,7K (+$47M) | 9,2M | $5,2B | $30M |
| **4/9** | **+$198M** | **+$199M** | −$1M | +$32M | +$6M | **+$99M** | **+70,7K (+$177M)** | 11,4M | **$15,6B** | **$129M** |
| 11/9 | +$117M | +$84M | +$3M | +$12M | +$13M | +$23M | +41,4K (+$104M) | 10,8M | $16,1B | $122M |
| 18/9 | +$12M | −$6M | +$17M | +$19M | +$21M | −$0,5M | +13,2K (+$33M) | 10,0M | $11,9B | $70M |
| 25/9 | −$9M | −$9M | $0 | +$26M | +$5M | −$8M | **−5,5K (−$14M)** | 7,6M | $10,2B | $46M |
| 2/10 | +$16M | +$6M | +$10M | +$19M | +$16M | −$6M | **−12,7K (−$32M)** | 7,5M | $9,4B | $35M |
| **9/10** | **+$9M** | **−$5M** | +$14M | **+$23M** | +$10M | **−$12M** | **−12,1K (−$30M)** | **5,9M** | **$7,3B** | **$23M** |

Đọc bảng:
1. **Hai tuần hype (29/8–11/9) mang vào ~$717M** (stablecoin + cổ phiếu token hoá + ETH). Từ 18/9 tiền mới gần như dừng, và **3 tuần gần nhất là rút ròng** (−$30M, −$22M, −$33M).
2. **USDG**, đồng tiền giao dịch chính (Paxos phát hành trực tiếp trên chain), giảm 3/4 tuần gần nhất: từ đỉnh $726,5M (15/9) còn $695,4M.
3. **ETH rút về Ethereum:** bridge chính thức (`0xDf87…64b3`) từ 312.174 ETH (16/9) còn 278.881 ETH. Rút từ L2 về L1 phải chờ khoảng 1 tuần, nên lượng ETH ra khỏi bridge hôm nay phản ánh quyết định rút từ tuần trước. Riêng ngày 6/10: −11.800 ETH. Từ 7/10 đến nay vào lại +2.850 ETH, nhưng còn quá sớm để gọi là đảo chiều.
4. **Cổ phiếu token hoá bị đổi ngược ra:** giá trị on-chain của 191 mã (theo giá hiện tại) đỉnh $180,6M ngày 15/9, nay $149,7M. Bốn tuần liền burn nhiều hơn mint. Lớn nhất: SPY $19,2M, NVDA $17,3M, SPCX $9,7M, GLD $7,7M, META $7,1M.
5. **Hoạt động giảm một nửa.** Số giao dịch người dùng mỗi ngày (ước tính bằng cách lấy mẫu 100 block/ngày) từ ~11M (tuần 4/9) còn ~5,9M; gas dùng mỗi ngày −70%. Trợ giá gas cho ví Robinhood hết hạn ngày 29/9 ([KuCoin](https://www.kucoin.com/news/flash/robinhood-chain-ends-free-gas-subsidy-in-late-september-memecoins-face-stress-test)); trung bình 30/9–8/10 ~6,4M giao dịch/ngày so với ~7,7M trong tuần 22–28/9. Toàn chain vẫn có ~1,9 triệu swap/ngày (chỉ số swap của HoodScan tăng từ 283,6M lên 289,6M trong 3 ngày).

### B.2 Tiền đang nằm ở đâu

**Stablecoin $1,090 tỷ** (on-chain, 9/10): USDG $695,4M (64%), USDe $364,8M (33%), U (United Stables) $30M. DefiLlama: $1,093 tỷ.

| Nơi tiền đậu | Quy mô | Ghi chú |
|---|---:|---|
| **Robinhood Earn** = vault Steakhouse USDG trên Morpho (`0xbeef…09dd`) | **$537M** (77% USDG) | Robinhood chọn Morpho cho sản phẩm Earn ([FinanzNachrichten](https://www.finanznachrichten.de/nachrichten-2026-07/68920872-robinhood-chooses-morpho-to-power-new-earn-product-004.htm)). Lợi suất quảng cáo ~7%, trong đó ~3,9% là lãi thật và ~3,3% là thưởng Merkl ([DefiLlama](https://defillama.com/yields/pool/32f586b4-5358-5aa2-88ee-c842139e7023)) |
| Morpho Blue, các market cho vay USDG | Cung $534M, vay $478M (dùng 89,5% vốn) | Vay theo tài sản thế chấp: **USDe $320M (67%)**, syrupUSDG $118M (25%), mGLO $29M (6%), spUSDG $8M. Cổ phiếu token hoá $1,67M (0,35%), wsNET $0,82M |
| Perp DEX (Lighter, Arcus, Meridian) | ~$162M | Nhóm duy nhất có phí tăng đều mỗi tuần |
| Pool DEX (Uniswap v2/v3/v4, Fables, Ramses, up, Sushi…) | ~$277M | Đang rút: Uniswap V4 −14%, V3 −20%, Fables −19%, up v3 −33% trong 7 ngày |

Nghĩa là: lãi suất ~7% của Earn được trả bởi **người vay USDG thế chấp stablecoin** (vòng USDe ↔ USDG để farm lãi và điểm thưởng) cộng thêm thưởng Merkl. Đây là tiền "đậu" theo lợi suất, không phải tiền mua tài sản rủi ro. Nếu thưởng Merkl giảm hoặc lãi suất bên ngoài cao hơn, khối tiền này có thể rút nhanh.

**TVL theo protocol** (DefiLlama, `data/market/rh_protocols.csv`):

| Protocol | Loại | TVL | 7 ngày | 30 ngày |
|---|---|---:|---:|---:|
| Morpho Blue | Lending | $611M | +5,2% | +20,3% |
| Steakhouse Financial | Curator (Earn) | $537M | +4,4% | +13,8% |
| Uniswap V4 | DEX | $159M | −13,9% | +3,4% |
| Lighter Robinhood Perps | Perps | $111M | +2,7% | +58,6% |
| Uniswap V3 | DEX | $52M | −20,1% | −37,7% |
| Arcus Perps | Perps | $48M | **+40,8%** | +113% |
| Fables | DEX | $37M | −19,0% | +144% |
| Gate | CEX | $22M | −31,6% | – |
| Spark Savings | Yield | $10M | −27,3% | −70,2% |
| SushiSwap V3 | DEX | $4,0M | +46,0% | +106% |
| Meridian Perps | Perps | $3,2M | +34,7% | +26,1% |

### B.3 Hoạt động đang ở đâu

**Volume DEX theo protocol** (tuần kết thúc 8/10 so với đỉnh tuần 10/9): Uniswap V3 $2,67 tỷ (−65%), Uniswap V4 $3,00 tỷ (−49%), Fables $0,55 tỷ (đỉnh $0,70 tỷ tuần 1/10), Ramses $0,25 tỷ (−51%), **Pons V2 (launchpad meme) $0,10 tỷ (−90%)**, Metric $0,13 tỷ.

**Phí theo nhóm** (tuần kết thúc 8/10 so với tuần 10/9): DEX $13,8M (−75%), **Launchpad $6,0M (−90%)**, Trading App $1,5M (−93%), **Derivatives $1,08M (+167%, tăng liên tục từ tháng 7)**.

**Meme coin** (HoodScan, đã loại 8 pool SUSD có $310,7M "volume" từ chỉ 101 giao dịch, rõ ràng là wash trade): 1.180 token, volume 24h **$10,0M**, thanh khoản $54,1M, dòng tiền ròng 24h **−$574K**, trung vị 24h **−12,2%**, chỉ 31% token tăng giá. Vẫn có 44 token mới mỗi ngày. Theo [Crypto Briefing](https://cryptobriefing.com/robinhood-chain-memecoin-trading-surge-collapse/) và [Fortune](https://fortune.com/2026/10/06/443-million-memecoin-frenzy-robinhood-circle-latest-memecoin-boom-bust/), volume cặp meme–cổ phiếu từng đạt $443M/ngày đầu tháng 9 rồi giảm 96%.

**Cổ phiếu token hoá:** 191 mã, volume 24h $105,5M (NVDA $19,9M, SPY $19,9M, CRCL $8,1M, MSTR $6,7M, SPCX $6,4M), thanh khoản $92,6M. Volume vẫn khá, nhưng lượng token đang lưu hành giảm (B.1).

**Token gốc hệ sinh thái** (CoinGecko, 7 ngày / 30 ngày): AI −40% / −57% (vốn hoá $93M), CASHCAT −36% / −39% ($112M), PONS −34% / −55% ($237M), NET −25% / −66%, LIT (Lighter) −6% / −31% ($892M), NPC −6% / +2%.

### B.4 Kết luận về dòng tiền RH chain

- **Chưa có dấu hiệu tháo chạy:** TVL ~$1,04 tỷ, stablecoin ~$1,09 tỷ, gần đỉnh.
- **Nhưng cơ cấu đã đổi:** tiền đầu cơ ra (ETH −$83M từ đỉnh, cổ phiếu token hoá −$31M, USDG −$31M, phí launchpad −90%), tiền gửi lãi vào (Earn +$12–26M/tuần, USDe đỉnh mới). Đây là kiểu chain "đậu tiền lấy lãi", không phải chain có lực mua tài sản rủi ro.
- **Thứ duy nhất đang tăng trưởng** là perps (Arcus, Lighter, Meridian) và lending. Đầu cơ đang chuyển sang đòn bẩy trên perp DEX, không quay lại meme/token gốc.
- **Với NET:** không có dòng tiền mới từ hệ sinh thái để đỡ premium. Giá phụ thuộc vào cơ chế nội tại (NAV, InverseBond) và việc team có nạp tiền mới hay không.

Tin tức và chất xúc tác ([TokenPost](https://www.tokenpost.com/tag/robinhood-chain), [Coingabbar](https://www.coingabbar.com/en/robinhood-chain-news-dex-volume-falls-from-record-high)):
- Robinhood đang **thăm dò** một Stock Token gắn với ETF quản lý chủ động của T. Rowe Price, mới ở giai đoạn sơ bộ ([Unchained](https://unchainedcrypto.com/robinhood-explores-stock-token-tied-to-t-rowe-price-actively-managed-etf)). $HYPE lên chain qua SushiSwap ([Coinfomania](https://coinfomania.com/hype-goes-live-on-robinhood-chain)).
- Fables (DEX ve(3,3), TVL $37M) được cho là sẽ ra token ngày 20/10 theo TokenPost; chưa thấy xác nhận từ nguồn chính thức. Nếu đúng, đây có thể là đợt incentive thanh khoản mới.
- **Robinhood công bố kết quả quý 3 ngày 27/10/2026** ([GlobeNewswire](https://www.globenewswire.com/news-release/2026/10/01/3373375/0/en/robinhood-markets-inc-to-announce-third-quarter-2026-results-on-october-27-2026.html)). Đây là dịp có thể công bố số liệu hoặc kế hoạch mới cho chain.

## C. NET: pool và thanh khoản

30 pair, tổng thanh khoản **~$1,06M** (6/10: $1,10M), volume 24h ~$1,49M.

| Pool | DEX | Thanh khoản | Vol 24h | Thuế 5% |
|---|---|---:|---:|:-:|
| [`0x59F9…5B54`](https://dexscreener.com/robinhood/0x59f95461e68e0c77605299791e1449f175165b54) NET/USDG: canonical, oracle TWAP, ~98% LP thuộc Treasury | Uniswap v2 | $379K (876 NET + $189K) | $0,27M | ✅ |
| `0x0d66…deb3` NET/USDG | Uniswap v4 | $265K (6/10: $148K) | $0,26M | ❌ |
| [`0x99e7…1673`](https://dexscreener.com/robinhood/0x99e70a5b06215e5d2f3bec773b4f59c008fc1673) NET/USDG 1% | Up v3 | $165K (6/10: $226K) | $0,43M | ❌ |
| `0x4030…170d` NET/USDG | Uniswap v4 | $136K | $0,27M | ❌ |
| `0x888f…4fc1` NET/USDG | Uniswap v4 | $27K (pool mới, 3/10) | $0,02M | ❌ |
| `0x146a…18D3` NET/USDG | Alandale | $15K | $0,10M | ❌ |

Pool Ramses v3 (`0x813f…3862`, $97K ngày 6/10) gần như đã rút hết thanh khoản (còn $0,7K). Danh sách đầy đủ ở `data/pools.csv`.

## D. NET: cơ chế và trạng thái protocol

| Thành phần | Quy tắc | Hiện tại (9/10) |
|---|---|---|
| NAV | RFV / supply; RFV = USDG liquid + USDG trong Morpho × 0,98 + POL | **$164,84**. RFV **$23,86M** ($7,48M liquid + $16,69M Steakhouse/Morpho) |
| Rebase (8h) | 0,45% × clamp((P−1)/0,75, 0, 1) | P = 1,32 → **0,19%/epoch** (0,57%/ngày) ≈ **760 NET/ngày**. Ngày 7/10, khi premium lên 1,9×, rebase chạy tối đa ~1.800 NET/ngày |
| Bond | giá max(TWAP × 0,97, NAV), vest 2 ngày, 0,25% supply/epoch | ~**1.085 NET/ngày**; 1.675 NET đang vest |
| InverseBond | mua NET ở NAV × 0,985 rồi đốt; 1% USDG liquid/epoch | **$162,37**, ~$75K/epoch (~$224K/ngày). Chưa được dùng |
| PremiumSeller | bán khi TWAP > 2× NAV ($330) | tắt |
| pTEAM | team mint với giá $1, trần 15% float, không hết hạn | đã dùng 13.320 (không đổi từ 28/9); **mint được ngay 8.133 NET** (~$1,76M theo giá thị trường). Nếu mint hết, NAV giảm ~5,3% xuống **~$156** |
| Supply | | **144.739 NET** (+5,2% so với 6/10), 92,7% đang stake |

Tuần 2–8/10 mint 16.720 NET (rebase 9.937, bond 6.780), tức supply tăng ~13% trong một tuần. NAV giảm đều: $168,2 (6/10) → $167,4 (7/10) → $166,1 (8/10) → $164,8 (9/10). Nguồn của toàn bộ NET đã mint: rebase 70,7K (49%), bond 36,8K (25%), genesis 21,7K (15%), **pTEAM 13,3K (9%)**, PremiumSeller 2,3K (2%).

**Loopback** (market Morpho cho vay USDG thế chấp wsNET, `0xaa58…0589`): cung $910K, vay **$824K** (dùng 90,5% vốn), lãi vay **~49%/năm**. Thế chấp 3.204 wsNET ≈ **13.872 NET (9,6% supply)**, 165 người vay, LTV bình quân 30,5% (ngưỡng thanh lý 62,5%). Oracle `LoopbackOracle` định giá NET = TWAP × 0,9, **không bao giờ thấp hơn NAV** và không cao hơn 5× NAV, và tự dừng khi giá tức thời thấp hơn TWAP quá 15%. Vì có sàn NAV, giá giảm đến đâu thì cũng chỉ ~16 vị thế (~100 NET, nợ ~$10K) có thể bị thanh lý; nếu NAV giảm xuống ~$156 (team mint pTEAM) thì con số này là ~27 vị thế (~444 NET, nợ ~$44K). **Rủi ro thanh lý dây chuyền thấp.** Nhưng lãi vay 49%/năm là gánh nặng: người vay đang cược rằng rebase (~0,57%/ngày) bù được lãi và đà giảm giá.

## E. Ai đang bán

1. **Bonder** (nguồn bán lớn nhất và đều đặn nhất). Claim 900–1.040 NET/ngày; 7 ngày 6.927 NET, 30 ngày 28.422 NET. Trong 30 ngày, nhóm ví có claim bond: 308 ví bán ròng −$8,98M, 391 ví mua ròng +$3,08M, **tổng −$5,90M**. Top bán 7 ngày: `0xf357…401d` (−$229K, claim 937 NET), `0x7c94…f3c0` (−$144K, claim 689 NET), `0x708d…` (−$91K, claim 396 NET).
2. **Holder lâu năm thoát hàng:** `0xf41b…9e3b` bán 686 NET (~$139K) trong 3 lệnh ngày 8–9/10. Ví này không mua, không claim bond, không nhận chuyển khoản nào trong 30 ngày, tức là NET đã giữ từ trước tháng 9. `0x480c…` (−$101K) cùng kiểu: không mua trong 7 ngày, chỉ có 7 giao dịch từ trước đến nay.
3. **Đợt pump rồi xả ngày 7/10.** 00:00–12:00 UTC: 721 ví, mua ròng +$139K (Sleeve mua nhiều nhất, $56K). 12:00 ngày 7/10 đến nay: 2.149 ví, **bán ròng −$261K**. Ví `0x465b…` mua $46K lúc pump rồi bán lại toàn bộ.
4. **Cá voi** (HoodScan 24 giờ): 7 ví mua $114K, bán $285K, **ròng −$171K**. Nhóm "smart money" hoà (28 ví, ròng −$248).
5. **Team, qua desk:** không mint pTEAM mới từ 28/9, các desk không nhận thêm USDG từ 6/10. Tổng cộng đã mint 13.320 NET bằng pTEAM (24/7–28/9), 192/200 giao dịch chuyển thẳng NET vào desk ngay trong cùng một lệnh, ước tính bán ra ~$7,08M. Người đăng ký trả **$5,46M USDG** vào các desk: chỉ $0,68M (12,5%) vào Treasury, $4,78M qua router `0xc941…` để mua cổ phiếu token hoá cho RWA Sleeve. Chi tiết: `data/team_pteam_to_desks.csv`, `data/desk_usdg_flows.csv`.

## F. Ai đang mua

1. **RWA Sleeve của team** (`0x4987…c7cb`; owner duy nhất là EOA `0xe7e8…96f6`, cũng là owner 1-of-1 của Team Safe):

| Giai đoạn | NET | USD |
|---|---:|---:|
| 18/9–2/10 | 3.712 | $1,71M |
| 3–5/10 | 1.396 | $370K |
| 6/10 | 221 | $60K |
| 7/10 (lần cuối lúc 15:51 UTC) | 213 | $66K |
| 8–9/10 | ~0 | ~$0 |
| **Tổng** | **5.546** | **~$2,20M** (giá vốn trung bình ~$397) |

   - **Ngày 6/10, 18:57 UTC**, EOA của team gửi 813,5 wsNET của Sleeve vào Loopback làm thế chấp và **vay 113.324 USDG**. Số tiền này dùng để mua NET trong ngày 6–7/10. Sleeve đang dùng đòn bẩy trên chính token của mình (LTV 16,7%, an toàn nhờ oracle có sàn NAV).
   - **Bảng cân đối hiện tại:** 326 NET + 181,5 wsNET trong ví + 813,5 wsNET thế chấp ≈ **4.634 NET** (~$1,0M). USDG **$340**. Cổ phiếu trong ví ~$134K. Trên Morpho: thế chấp cổ phiếu $4,00M, nợ $1,58M (LTV 39,6%); các market NVDA/SPCX/AAPL/GOOGL vẫn dùng 99,5–99,8% vốn, không còn chỗ vay thêm. Nợ Loopback $114K.
   - **Kết luận:** sau 6/10, team đã dùng đến nguồn cuối cùng là vay thế chấp NET, và cũng đã dừng. Muốn mua tiếp, team phải bán cổ phiếu, vay thêm trên Loopback (lãi 49%/năm) hoặc nạp tiền mới từ bên ngoài.
2. **Nhỏ lẻ:** 30 ngày có 10,4K ví mua ròng +$14,1M, 7,3K ví bán ròng −$10,6M, nhóm "ví khác" ròng **+$3,5M**. 24 giờ qua mua ròng +$66K (HoodScan), nhưng số người bán vẫn đông hơn người mua (872 so với 723).
3. **Người mua lớn trong đợt giảm:** `0xfbd9…f720` (+$92K trong 7 ngày, phần lớn mua ngày 8–9/10), `0x9164…8fda` (+$70K trong 7 ngày), `0xe26e…` (+$42K từ trưa 7/10).
4. **Không tính Sleeve, dòng tiền ròng 7 ngày trên DEX là khoảng −$0,6M** (tổng mua $10,46M, bán $10,41M, trong đó Sleeve +$0,66M).

## G. Phân bổ holder

11.238 ví. Top 10 nắm 10,7%, top 100 nắm 41,1% lượng NET người dùng nắm giữ (NET + sNET + wsNET quy đổi, không tính contract). Ví lớn nhất `0x72f2…` giữ 2.604 NET (2,1%). Nếu tính cả wsNET đang thế chấp trên Loopback, Sleeve của team vẫn là holder lớn nhất (~4.634 NET). 13.872 NET (9,6% supply) đang nằm làm thế chấp trên Morpho. Chi tiết ở `data/holders_top100.csv`.

## H. Giá và dự báo

### H.1 Kỹ thuật
- Nến ngày (pool v2): 6/10 C $283 → 7/10 H **$362** C $256 → 8/10 L $203 C $231 → 9/10 L **$184** ~$216. Đỉnh 7/10 thấp hơn đỉnh 2/10 ($357); đáy 9/10 ($184) thủng vùng $200–220 từng đỡ giá ngày 3–5/10.
- MA7 $249, MA20 $436, MA30 $540, giá nằm dưới cả ba. RSI14 35.
- Cú pump 7/10 không giữ được 12 giờ. Mỗi nhịp hồi lại gặp bond (~1.000 NET/ngày) và bonder bán ra.

### H.2 Toán pha loãng (mô phỏng từ hằng số contract và trạng thái 9/10)

| Giả định | Ngày 7 | Ngày 14 | Ngày 21 |
|---|---|---|---|
| Market cap giữ nguyên | $201 (NAV $162) | $186 (NAV $161) | $174 (NAV $160) |
| Giá đứng yên $216 | NAV $162 | NAV $159 | NAV $155 |
| Premium co về 1,15× trong 10 ngày | $196 | $186 | $184 |
| Giá về NAV (rebase và bond tự dừng) | $165 | $166 | $167 |

Nếu market cap đứng yên, chỉ riêng pha loãng đã kéo giá xuống ~$174 sau 3 tuần.

### H.3 Kịch bản 1–3 tuần (xác suất chủ quan)

Ba ngày qua giá đã chạm cả vùng "tốt" của bản 6/10 ($362) lẫn đáy vùng cơ sở ($184). NET biến động rất mạnh, nên nhìn vùng giá quan trọng hơn con số cụ thể.

| Kịch bản | Xác suất | Vùng giá NET | Điều kiện / dấu hiệu |
|---|:-:|---|---|
| **Cơ sở: trôi xuống, premium co dần** | ~50% | **$175–210** (1,1–1,3× NAV) | Team không mua thêm; bond xả ~1.000 NET/ngày; rebase chậm lại khi premium co; BTC đi ngang $80–85K; RH chain tiếp tục rút tiền đầu cơ |
| **Xấu: về NAV / sàn** | ~30% | **$155–168** | Team mint pTEAM (8,1K NET) rồi bán qua desk (NAV còn ~$156); BTC thủng $80K; ETH và stablecoin rời RH chain nhanh hơn; người vay Loopback bán để trả lãi 49%/năm. Tại NAV, InverseBond hấp thụ ~$224K/ngày; rebase và bond tự về 0 |
| **Tốt: hồi về 1,45–1,75× NAV** | ~20% | **$240–290** | Team nạp tiền mới hoặc vay thêm để mua; chất xúc tác cho RH chain (Fables TGE, kết quả quý 3 ngày 27/10, thị trường mới cho stock token); BTC lấy lại $85K+. Trên $288 rebase chạy tối đa; trên $330 PremiumSeller bán ra |

Từ $216: **−24% xuống NAV**, **+33% lên 1,75× NAV**, **+53% lên 2× NAV**. Rủi ro/lợi nhuận nhìn thì cân, nhưng xác suất nghiêng về phía giảm: người mua chính đã hết tiền, thị trường chung chuyển phòng thủ, và hệ sinh thái không có tiền mới chảy vào. **Vùng NAV (~$160–165) vẫn là sàn theo cơ chế**: ở đó protocol tự mua lại và dừng pha loãng.

### H.4 Robinhood Chain 2–4 tuần tới
- **Cơ sở:** tiếp tục co lại. Volume DEX $5–8 tỷ/tuần, phí $15–25M/tuần, giao dịch 5–7 triệu/ngày. Stablecoin đi ngang ~$1,05–1,10 tỷ: Earn vẫn hút tiền gửi, USDG giao dịch tiếp tục giảm. ETH tiếp tục rút. Cổ phiếu token hoá rút ròng nhẹ nếu không có thị trường mới.
- **Rủi ro:** thưởng Merkl giảm hoặc lãi suất Earn tụt, kéo theo vòng vay USDe ↔ USDG gỡ ra, có thể làm stablecoin giảm hàng trăm triệu USD rất nhanh. Thị trường chung xấu thêm (BTC dưới $77–80K).
- **Có thể đảo chiều nếu:** USDG tăng lại (> +$20M/tuần), bridge ETH vào ròng 2 tuần liền, cổ phiếu token hoá mint ròng trở lại, volume DEX tuần > $10 tỷ. Chất xúc tác: Fables TGE (~20/10, chưa xác nhận), kết quả quý 3 của Robinhood (27/10), thêm stock token mới (ETF của T. Rowe Price).

### H.5 Theo dõi on-chain
- **RWA Sleeve** `0x4987…c7cb`: số dư USDG, nợ Loopback (`0xaa58…0589`) và Morpho cổ phiếu, có mua lại hay rút wsNET không.
- `pTEAM.exercised()` (đang 13.320) và NET chuyển vào các desk (`0x99b6…`, `0xa84e…`, `0x70ea…`, `0x2f2f…`, `0x732b…`).
- `Distributor.premium()`: < 1,1 thì rebase gần như dừng; > 1,75 thì rebase tối đa.
- `InverseBond.capacityRemaining()`: giảm tức là đã có người bán xuống dưới NAV.
- Dòng tiền RH chain hàng ngày: `python3 rh_flows.py supply` (USDG/USDe/U/Earn), `rh_chain.py` (bridge ETH), `rh_flows.py stocks` (cổ phiếu token hoá).

## I. Rủi ro chính
1. **Tập trung vào team:** một EOA ký 1-of-1 cho Team Safe và RWA Sleeve. pTEAM không hết hạn, team luôn mint được 15% float với giá $1.
2. **Đòn bẩy của team:** nợ $1,58M trên các market cổ phiếu (dùng ~100% vốn) và $114K trên Loopback, thế chấp bằng chính NET.
3. **Docs chưa khớp với chain:** NET trong desk đến từ pTEAM chứ không phải mua trên thị trường; ít nhất 4 desk do Team Safe quản lý không được công bố địa chỉ.
4. **Thanh khoản mỏng** ($1,06M) so với FDV ~$31M; 92,7% supply có thể rút stake ngay.
5. **Hệ sinh thái đang co lại** (B.1); khối stablecoin lớn nhất là tiền gửi lấy lãi có trợ cấp, có thể rút nhanh. Rủi ro contract (Morpho/Steakhouse, DEX, router) và oracle TWAP.
6. **Phản xạ kiểu OHM:** premium thường co về NAV sau giai đoạn hưng phấn. NAV $23,9M là USDG thật; phần ~$7,4M vốn hoá phía trên NAV thì không có gì bảo chứng.

## J. Phương pháp và tái lập
- **Nguồn:** RPC `rpc.mainnet.chain.robinhood.com` (eth_getLogs, block), `robinhood.drpc.org` (eth_call lịch sử, Multicall3), `eth.drpc.org` (số dư bridge trên L1), Sourcify (ABI, mã nguồn `LoopbackOracle`), DefiLlama, DexScreener, GeckoTerminal, CoinGecko, alternative.me, HoodScan (MCP công khai), tin tức (link trong bài).
- **Phân loại dòng tiền NET** (`scripts/flows.py`): ~610K transaction, ~42,5K ví. Delta mỗi địa chỉ được quy về NET (NET + sNET + wsNET × index). Pool, contract protocol và router được loại ra; phần còn lại là ví người dùng. USD quy theo nến 4 giờ. Thời gian quy từ block theo mốc binary-search (`data/block_anchors.json`).
- **Dòng tiền RH chain** (`scripts/rh_flows.py`): tổng cung USDG/USDe/U/WETH và tài sản vault Steakhouse đọc lúc 00:00 UTC mỗi ngày từ 1/7; tổng cung 191 cổ phiếu token hoá (danh sách từ HoodScan) nhân giá hiện tại, nên thay đổi là lượng mint/burn chứ không phải biến động giá; 359 market Morpho Blue (277 market cho vay USDG) đọc theo ngày; số giao dịch người dùng ước tính bằng 100 block mẫu mỗi ngày (trừ 1 giao dịch hệ thống ArbOS mỗi block).
- **Giới hạn:** HoodScan gán giao dịch theo `tx.from`, ở đây gán theo người gửi/nhận token, nên số tổng có thể lệch. Giá trị bán qua desk là ước tính. Số giao dịch/ngày là ước tính có sai số lấy mẫu (xem theo tuần). ETH quy USD theo giá hiện tại. Xác suất các kịch bản là đánh giá chủ quan.

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
python3 loopback.py                                                # market Loopback, bậc thanh lý
python3 rh_chain.py                                                # DefiLlama, bridge ETH, vĩ mô, meme, stock token
python3 rh_protocols.py                                            # TVL theo protocol, volume DEX và phí theo nhóm
python3 rh_flows.py all                                            # stablecoin, Earn, cổ phiếu token hoá, Morpho, số giao dịch theo ngày
python3 rh_flow_summary.py                                         # bảng dòng tiền theo tuần
python3 build_report.py                                            # report.html
```
`raw/` (~300MB log) không được commit. `fetch_transfers.py` resume từ file `.cursor`. Chạy `team.py` **sau khi** hai lệnh `trace_addr.py` đã xong.

### File dữ liệu
| File | Nội dung |
|---|---|
| `data/latest_state.json`, `data/protocol_history_12h.csv` | Trạng thái protocol hiện tại và lịch sử 12h |
| `data/daily_flows.csv`, `data/weekly_supply_flows.csv` | Mint theo nguồn, claim bond/desk, stake/unstake, mua/bán theo ngày/tuần |
| `data/net_flow_by_category_30d.csv`, `data/top_traders_7d.csv`, `data/top_traders_30d.csv` | Ai mua, ai bán |
| `data/team_summary.json`, `data/team_pteam_to_desks.csv`, `data/sleeve_net_buys_daily.csv`, `data/desk_usdg_flows.csv` | Team, desk, RWA Sleeve |
| `data/loopback_summary.json`, `data/loopback_positions.json` | Market Loopback: lãi vay, oracle, vị thế, bậc thanh lý |
| `data/holders_top100.csv`, `data/pools.csv` | Holder, pool |
| `data/market/rh_flow_weekly.csv`, `data/market/rh_flow_summary.json` | Dòng tiền RH chain theo tuần, đỉnh và hiện tại |
| `data/market/rh_daily_flows.csv`, `rh_stock_supply_daily.csv`, `rh_morpho_usdg_daily.csv`, `rh_morpho_usdg_borrow_by_collateral.json`, `rh_activity.csv` | Chuỗi on-chain theo ngày: stablecoin, Earn, cổ phiếu token hoá, Morpho, số giao dịch |
| `data/market/rh_protocols.csv`, `rh_dex_by_protocol_weekly.csv`, `rh_fees_by_category_weekly.csv` | TVL theo protocol, volume DEX theo protocol, phí theo nhóm (DefiLlama) |
| `data/market/rh_chain_weekly.csv`, `rh_chain_summary.json`, `rh_l1_bridge_eth.json`, `rh_stables_breakdown.json` | DefiLlama theo tuần, bridge ETH trên L1 |
| `data/market/market_snapshot.json`, `hs_chain_status.json` | BTC/ETH, Fear & Greed, token hệ sinh thái, stock token, meme (đã loại wash trade); trạng thái HoodScan |
