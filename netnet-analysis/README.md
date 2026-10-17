# NetNet (NET) và Robinhood Chain — phân tích on-chain, dòng tiền, dự báo

Token `0xCA9c78Dd337A67F6e0077F65F5E9218719d30eDf` trên **Robinhood Chain** (Arbitrum Orbit L2, chainId 4663).
Snapshot thời gian thực: **2026-10-17 01:30 UTC** (các bản trước: 9/10, 6/10, 3/10). Số liệu đọc trực tiếp từ chain (RPC công khai, contract verified trên Sourcify, bridge L1 trên Ethereum), đối chiếu với DefiLlama, DexScreener, GeckoTerminal, CoinGecko, HoodScan và tin tức.

> Đây là phân tích dữ liệu, không phải lời khuyên đầu tư. NET là token rebase kiểu OlympusDAO trên một chain mới. Bạn có thể mất phần lớn số vốn bỏ vào.

Bản HTML có biểu đồ: [`report.html`](report.html) (build bằng `scripts/build_report.py` từ `report.template.html`), cũng được publish tại https://claude.ai/artifact/1s4mmumZGorDN3euAZMLid. Trang HTML không tự lấy dữ liệu mới khi mở; số liệu là snapshot ở trên.

---

## TL;DR

**NET đã về sát NAV.** Giá **$165,3**, NAV **$162,66**, premium **1,02×**. Kịch bản "xấu" của bản 9/10 ($155–168) đã xảy ra từ ngày 12/10.
- **Rebase gần như dừng:** chỉ còn ~40 NET/ngày (9/10: ~760).
- **Sàn mua lại đã hoạt động.** InverseBond mua và đốt 696 NET (~$112K) trong hai ngày 12/10 và 16/10, ở giá ~$160. Đây là lần đầu sàn này được dùng đáng kể.
- **Nguồn bán chính bây giờ là bond.** Bond vẫn bán hết capacity, ~1.100–1.165 NET/ngày. Supply tăng 7,6% trong 8 ngày (144.739 → 155.808 NET).
- **Team chỉ mua nhỏ giọt.** Team Safe chuyển cho RWA Sleeve $49K USDG và 653 SPCX (~$95K). Sleeve mua 234 NET (~$41K) ngày 12–13/10, nhỏ hơn nhiều so với $60–380K/ngày hồi cuối tháng 9.
- **Rủi ro lớn nhất:** team có thể mint ngay **9.779 NET** với giá $1 (pTEAM). Nếu mint hết, NAV giảm ~5,9% xuống **~$153**.

| NET | 17/10 01:30 UTC | 9/10 |
|---|---|---|
| Giá | **$165,3** (−24% so với 9/10; −91% từ đỉnh $1.888) | $216 |
| NAV | **$162,66** (−1,3%) | $164,84 |
| Premium | **1,02×** | 1,31× |
| Sàn InverseBond | **$160,22**, ~$78,6K mỗi 8 giờ (~$236K/ngày) | $162,37 |
| Supply / stake | 155.808 NET / 89,8% | 144.739 / 92,7% |
| Treasury (RFV) | $25,34M ($7,86M liquid + $17,82M Morpho) | $23,86M |
| Dòng tiền DEX 24h (HoodScan) | mua $146K, bán $475K, **ròng −$330K** (nhỏ lẻ −$213K, cá voi −$105K) | ròng −$103K |

**Thị trường chung vẫn phòng thủ.** BTC **$81,5K** (−1,7% / 7 ngày). Ngày 16/10 BTC thủng $80K một lúc rồi được mua lại; CPI và PPI tháng 9 đều nóng hơn dự báo. ETH $2.420 (−3,4%). Fear & Greed **55** (9/10: 59). Tổng vốn hoá $2,75T (−3,7% / 24h).

**Robinhood Chain, tuần 10–16/10 (đo on-chain):**

| Dòng tiền | Tuần này | Ghi chú |
|---|---:|---|
| Stablecoin (USDG + USDe + U) | **−$8,6M** | Tuần âm đầu tiên kể từ 25/9: USDG −$1,0M, USDe −$7,6M |
| Robinhood Earn (vault Steakhouse USDG) | **−$11,9M** | **Lần đầu bị rút ròng** cả tuần: đỉnh $546,6M (12/10) còn $523,4M. Thưởng Merkl giảm từ ~3,3% xuống ~2,5%; APY tổng ~6,5% |
| Vay USDG trên Morpho | −$6,1M | Lần đầu giảm; đỉnh $488M ngày 13/10 |
| Cổ phiếu token hoá (mint trừ burn) | **+$17,9M** | **Mint ròng trở lại** sau 4 tuần bị đổi ngược |
| ETH qua bridge chính thức | **−13.594 ETH (−$33M)** | Tuần rút thứ 4 liên tiếp; −46,9K ETH (−15%) từ đỉnh 17/9 |
| Volume DEX / phí | $6,57 tỷ / $18,3M | −5% / −19% so với tuần trước |

Cộng stablecoin, cổ phiếu token hoá và ETH: **tiền mới vào chain âm 4 tuần liền, tổng −$97M**. Hai tuần hype (29/8–11/9) từng mang vào +$698M. Điểm mới tuần này: **tiền gửi lấy lãi bắt đầu rút** (Earn, USDe, khoản vay Morpho), trong khi cổ phiếu token hoá lần đầu có tiền vào lại.

**Dự báo 1–3 tuần (xác suất chủ quan):**
- **Cơ sở ~55%: $158–185.** Giá bám vùng NAV; InverseBond đỡ ở ~$160; premium nào xuất hiện cũng bị bond bán ra.
- **Xấu ~25%: $145–158.** Team mint pTEAM (NAV còn ~$153), hoặc lượng thoát vượt sức mua của InverseBond.
- **Tốt ~20%: $190–240.** Có cầu mới (Fables TGE ngày 20/10, kết quả quý 3 của Robinhood ngày 27/10, team nạp thêm tiền, BTC hồi).

Từ $165: **−3% xuống sàn InverseBond**, −7% nếu team mint pTEAM, **+28% lên 1,3× NAV**. Rủi ro giảm giá theo cơ chế giờ đã nhỏ hơn nhiều so với tuần trước. Nhưng muốn tăng thì cần người mua mới, và hiện chưa thấy.

---

## A. Thị trường chung

| | Giá | 7 ngày | 30 ngày | 90 ngày |
|---|---:|---:|---:|---:|
| BTC | $81.502 | −1,7% | +6,7% | +26,0% (đỉnh 90 ngày $86,6K) |
| ETH | $2.420 | −3,4% | −1,1% | +29,4% |
| Tổng vốn hoá crypto | $2,75T (−3,7% / 24h), BTC dominance 59,3% | | | |
| Fear & Greed | **55** (9/10: 59, 6/10: 73); trung bình 7 ngày 60, 30 ngày 67 | | | |

- Ngày 16/10 BTC mở cửa ~$82,1K. CPI và PPI tháng 9 đều nóng hơn dự báo ([Yahoo Finance](https://finance.yahoo.com/personal-finance/investing/article/bitcoin-and-ethereum-prices-today-friday-october-16-2026-bitcoin-ethereum-prices-firm-despite-two-strong-inflation-reports-113928147.html)). BTC có lúc thủng $80K rồi được mua lại ([CoinDesk](https://www.coindesk.com/markets/2026/10/16/bitcoin-buyers-snap-up-a-brief-drop-below-usd80-000-as-asian-stocks-rebound)); [Fortune](https://fortune.com/article/price-of-bitcoin-10-16-2026/) ghi nhận ~$82,6K sáng 16/10.
- Đến 01:30 UTC ngày 17/10, BTC còn $81,5K và tổng vốn hoá giảm 3,7% trong 24 giờ.

**Ý nghĩa:** thị trường chung không sập nhưng cũng không có lực kéo. Vùng $80K của BTC đang được giữ. Tiền đầu cơ chưa có lý do quay lại các hệ sinh thái nhỏ như Robinhood Chain.

## B. Dòng tiền Robinhood Chain

Mainnet chạy từ 1/7/2026. Phần này đo tiền thật đi vào/ra chain trực tiếp on-chain: tổng cung stablecoin, vault Earn, Morpho, cổ phiếu token hoá, bridge ETH trên Ethereum, số giao dịch. Sau đó đối chiếu với DefiLlama. Script: `scripts/rh_flows.py`, `scripts/rh_flow_summary.py`, `scripts/rh_protocols.py`, `scripts/rh_chain.py`.

### B.1 Tiền mới vào/ra chain theo tuần

Tuần theo DefiLlama (thứ Sáu đến thứ Năm). Số on-chain tính từ 00:00 UTC ngày đầu tuần đến 00:00 UTC sau ngày cuối. ETH quy USD theo giá hiện tại ($2.420), đo lúc ~01:30 UTC mỗi ngày. File `data/market/rh_flow_weekly.csv`.

| Tuần kết thúc | Stablecoin | USDG | USDe | Earn vault | Vay USDG Morpho | Cổ phiếu token hoá | ETH bridge | Tổng ròng | Giao dịch/ngày | Volume DEX | Phí |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **4/9** | +$198M | +$199M | −$1M | +$32M | +$6M | +$95M | +61,1K ETH | **+$441M** | 11,4M | $15,6B | $129M |
| 11/9 | +$117M | +$84M | +$3M | +$12M | +$13M | +$21M | +49,5K | **+$258M** | 10,8M | $16,1B | $123M |
| 18/9 | +$12M | −$6M | +$17M | +$19M | +$21M | $0 | +14,6K | +$47M | 10,0M | $11,9B | $70M |
| 25/9 | −$9M | −$9M | $0 | +$26M | +$5M | −$7M | −4,6K | **−$27M** | 7,6M | $10,2B | $46M |
| 2/10 | +$16M | +$6M | +$10M | +$19M | +$16M | −$5M | −5,6K | **−$3M** | 7,5M | $9,4B | $35M |
| 9/10 | +$16M | +$2M | +$14M | +$17M | +$10M | −$13M | −19,1K | **−$43M** | 6,2M | $6,9B | $23M |
| **16/10** | **−$9M** | −$1M | **−$8M** | **−$12M** | **−$6M** | **+$18M** | **−13,6K** | **−$24M** | 7,3M | $6,6B | $18M |

Đọc bảng:
1. **Bốn tuần liền rút ròng**, tổng −$97M. Tuần này nhẹ hơn tuần trước (−$24M so với −$43M) nhờ cổ phiếu token hoá.
2. **Tiền gửi lấy lãi lần đầu rút ra.** Vault Earn −$11,9M, USDe −$7,6M, vay USDG trên Morpho −$6,1M, cùng lúc. Lợi suất Earn ([DefiLlama](https://defillama.com/yields/pool/32f586b4-5358-5aa2-88ee-c842139e7023)) còn ~6,5% (4,0% lãi thật + 2,5% thưởng Merkl), từ ~7% trước đó; phần thưởng giảm từ ~3,3%. Khối tiền này đi theo lợi suất, thưởng giảm thì tiền rút.
3. **Cổ phiếu token hoá được mint ròng +$17,9M**, chủ yếu trong hai ngày 14/10 và 16/10. Giá trị lưu hành theo giá hiện tại tăng từ $140,7M lên $158,6M. Volume 24 giờ của stock token $129M (SPCX $30M, NVDA $24M, SPY $17M, TSLA $9M).
4. **ETH tiếp tục rời chain:** 265.847 ETH trong bridge, giảm từ đỉnh 312.771 ETH ngày 17/9. Rút về L1 phải chờ khoảng 1 tuần, nên lượng ra hôm nay phản ánh quyết định từ tuần trước.
5. **Hoạt động:** ước tính ~7,3 triệu giao dịch/ngày tuần này và 6,2 triệu tuần trước. Số tuần trước khớp với growthepie (6,2 triệu/ngày ngày 2–8/10, −42% so với giữa tháng 9, theo [crypto.news](https://crypto.news/robinhood-chain-transactions-drop-42-whats-next/)); số ngày lẻ có sai số lấy mẫu lớn. HoodScan ghi ~1,87 triệu swap/ngày (9/10: ~1,94 triệu).

### B.2 Tiền đang nằm ở đâu

**Stablecoin $1,089 tỷ** (on-chain, 17/10): USDG $701,6M, USDe $357,2M, U $30M. DefiLlama: TVL $1,048 tỷ, stablecoin $1,084 tỷ.

| Nơi tiền đậu | Quy mô | Ghi chú |
|---|---:|---|
| **Robinhood Earn** (vault Steakhouse USDG trên Morpho) | **$523M** (75% USDG) | Đỉnh $547M ngày 12/10; −$23M trong 5 ngày |
| Morpho Blue, market cho vay USDG | Cung $522M, vay $472M (90,4% vốn) | Thế chấp: **USDe $313M (66%)**, syrupUSDG $118M (25%), mGLO $30M (6%), spUSDG $8M; cổ phiếu token hoá $1,67M, wsNET $0,90M |
| Perp DEX (Lighter, Arcus, Meridian…) | ~$176M | Arcus +24,6% TVL trong 7 ngày (+158% / 30 ngày) |
| Pool DEX | ~$285M | Uniswap V4 +7,4%; V3 −4,3%; Fables −6,5% trước TGE |

**TVL theo protocol** (DefiLlama, `data/market/rh_protocols.csv`):

| Protocol | Loại | TVL | 7 ngày | 30 ngày |
|---|---|---:|---:|---:|
| Morpho Blue | Lending | $593M | **−2,7%** | +12,2% |
| Steakhouse Financial | Curator (Earn) | $523M | **−2,8%** | +7,8% |
| Uniswap V4 | DEX | $172M | +7,4% | +3,4% |
| Lighter Robinhood Perps | Perps | $112M | +1,0% | +29,2% |
| Arcus Perps | Perps | $61M | **+24,6%** | +158% |
| Uniswap V3 | DEX | $50M | −4,3% | −26,0% |
| Fables | DEX | $35M | −6,5% | +65,2% |
| Gate | CEX | $20M | −8,5% | – |
| Spark Savings | Yield | $10M | +1,1% | −38,2% |

### B.3 Hoạt động đang ở đâu

- **Volume DEX tuần 10–16/10:** Uniswap V4 $3,10 tỷ (tăng), Uniswap V3 $2,29 tỷ, Fables $0,48 tỷ, Ramses $0,16 tỷ, Metric $0,12 tỷ, **Pons V2 (launchpad meme) $0,05 tỷ** (−95% so với đỉnh $0,94 tỷ).
- **Phí theo nhóm:** DEX $11,3M (−14%), Launchpad $3,3M (−36%), Trading App $1,1M, Perps $1,04M (đi ngang), Lending $0,42M.
- **Meme coin** (HoodScan): 1.309 token, volume 24h $14,2M, thanh khoản $85,9M, dòng tiền ròng −$522K. Trung vị 24h +0,9%, 57% token tăng giá. Tuần này không còn pool wash trade SUSD.
- **Token gốc hệ sinh thái** (CoinGecko, 7 ngày / 30 ngày): LIT −13% / −31% (vốn hoá $791M), NPC −10% / −8%, AI −9% / −66%, PONS −6% / −43%, CASHCAT −4% / −41%, NET −13% / −81%.

### B.4 Kết luận về dòng tiền RH chain

- **Chain co lại chậm, chưa tháo chạy.** TVL ~$1,05 tỷ, stablecoin ~$1,09 tỷ. Robinhood Chain vượt $100 tỷ volume DEX cộng dồn ([Bitcoin.com](https://news.bitcoin.com/defi/robinhood-chain-100-billion-volume-outtrades-base/)); WisdomTree ước tính chain tạo $43,78M phí và trả $4,37M cho Arbitrum ([The Crypto Times](https://www.cryptotimes.io/2026/10/16/robinhood-chain-generates-43-7m-for-arbitrum-wisdomtree/)).
- **Cơ cấu đổi lần nữa.** Tiền đầu cơ (ETH, meme, launchpad) vẫn ra. Tiền gửi lấy lãi, vốn là trụ đỡ suốt tháng 9, bắt đầu rút khi thưởng giảm. Cổ phiếu token hoá có tiền vào lại.
- **Tăng trưởng chỉ còn ở perps** (Arcus, Lighter) và Uniswap V4.
- **Với NET:** hệ sinh thái vẫn không có dòng tiền mới để đỡ premium. Giá đang được giữ bằng cơ chế nội tại (NAV, InverseBond).

Tin tức và chất xúc tác:
- **Fables ra token FABLES ngày 20/10**, cùng cơ chế ve(3,3); snapshot PROLOGUE ngày 17–18/10 ([Phemex](https://phemex.com/news/article/fables-sets-fables-token-tge-for-october-20-with-ve33-launch-98341), [Bitrue](https://www.bitrue.com/blog/fables-tge)). Có thể kéo incentive thanh khoản về DEX trên chain.
- **Robinhood Social** (mạng xã hội chia sẻ lệnh và lãi/lỗ, gắn với lịch sử giao dịch on/off-chain) đã mở công khai ([KuCoin](https://www.kucoin.com/blog/robinhood-chain-100b-dex-volume-social-launch)).
- Robinhood xác nhận đang thăm dò ETF token hoá với T. Rowe Price ([Unchained](https://unchainedcrypto.com/robinhood-explores-stock-token-tied-to-t-rowe-price-actively-managed-etf)).
- **Kết quả quý 3 của Robinhood ngày 27/10/2026** ([GlobeNewswire](https://www.globenewswire.com/news-release/2026/10/01/3373375/0/en/robinhood-markets-inc-to-announce-third-quarter-2026-results-on-october-27-2026.html)). Đây là quý đầu tiên có trọn mainnet.

## C. NET: pool và thanh khoản

25 pair, tổng thanh khoản **~$1,13M**, volume 24h ~$1,15M.

| Pool | DEX | Thanh khoản | Vol 24h | Thuế 5% |
|---|---|---:|---:|:-:|
| [`0x59F9…5B54`](https://dexscreener.com/robinhood/0x59f95461e68e0c77605299791e1449f175165b54) NET/USDG: canonical, oracle TWAP, ~98% LP thuộc Treasury | Uniswap v2 | $343K (1.036 NET + $171K) | $0,09M | ✅ |
| [`0x99e7…1673`](https://dexscreener.com/robinhood/0x99e70a5b06215e5d2f3bec773b4f59c008fc1673) NET/USDG 1% | Up v3 | $290K | $0,26M | ❌ |
| `0x4030…170d` NET/USDG | Uniswap v4 | $184K | $0,11M | ❌ |
| `0x0d66…deb3` NET/USDG | Uniswap v4 | $146K | $0,13M | ❌ |
| `0x9735…9661` NET/USDG (mới) | Metric | $50K | $0,42M | ❌ |
| `0x146a…18D3` NET/USDG | Alandale | $28K | $0,08M | ❌ |

Pool v2 mỏng nên dễ bị "râu nến". Ngày 12/10 lúc 08:33 UTC, ví `0xfbd9…f720` mua 302,5 NET trong một lệnh, đẩy giá pool v2 lên ~$244. Ngày 16/10 lúc 00:34 UTC, ví `0xf41b…9e3b` mua 459 NET trong hai lệnh, đẩy giá lên ~$339. Cả hai lần, arbitrage từ pool up v3 và alandale kéo giá về ngay trong vài giây. Hai cây nến 4 giờ đó không phản ánh mức giá có thể giao dịch thật.

## D. NET: cơ chế và trạng thái protocol

| Thành phần | Quy tắc | Hiện tại (17/10 01:28 UTC) |
|---|---|---|
| NAV | RFV / supply; RFV = USDG liquid + USDG trong Morpho × 0,98 + POL | **$162,66**. RFV **$25,34M** ($7,86M liquid + $17,82M Steakhouse/Morpho) |
| Rebase (8h) | 0,45% × clamp((P−1)/0,75, 0, 1) | P = 1,016 → **0,0095%/epoch ≈ 40 NET/ngày**, gần như dừng |
| Bond | giá max(TWAP × 0,97, NAV), vest 2 ngày, 0,25% supply/epoch | Vẫn bán hết: **~1.170 NET/ngày**; tuần 9–15/10 mint 7.843 NET; 1.763 NET đang vest. Bond bán ở NAV không làm giảm NAV, nhưng NET mới vẫn bị bán ra thị trường |
| InverseBond | mua NET ở NAV × 0,985 rồi đốt; 1% USDG liquid/epoch | **$160,22**, ~$78,6K mỗi epoch. **Đã mua 696 NET** ngày 12/10 (311) và 16/10 (385); người bán lớn nhất `0x006e…` (324 NET), `0x6241…` (194 NET) |
| PremiumSeller | bán khi TWAP > 2× NAV ($325) | tắt |
| pTEAM | team mint với giá $1, trần 15% float, không hết hạn | đã dùng 13.320 (không đổi từ 28/9); **mint được ngay 9.779 NET** (~$1,62M). Nếu mint hết, NAV còn **$153,1** (−5,9%) |
| Supply | | **155.808 NET** (+7,6% so với 9/10), 89,8% đang stake (9/10: 92,7%) |

- **NAV diễn biến:** $164,6 (10/10) → $163,6 (12/10) → $163,2 (15/10) → $162,7 (17/10). NAV giảm chậm lại vì rebase gần như dừng. Ở premium ~1, NAV sẽ đi ngang hoặc nhích lên nhờ thuế, lãi Morpho và InverseBond (mua dưới NAV rồi đốt).
- **Nguồn của toàn bộ NET đã mint:** rebase 73,8K (47%), bond 45,5K (29%), genesis 21,7K (14%), **pTEAM 13,3K (9%)**, PremiumSeller 2,3K (1%).

**Loopback** (market Morpho cho vay USDG thế chấp wsNET, `0xaa58…0589`):
- **Cung tăng mạnh:** $910K → **$1,34M**, vì lãi cao hút thêm người cho vay. Vay $904K, mức sử dụng vốn giảm từ 90% xuống **67%**, lãi vay **~44%/năm** (từ 49%).
- **Thế chấp:** 3.347 wsNET ≈ 14.845 NET (9,5% supply), 173 người vay, LTV bình quân 37%.
- **Oracle đã chạm sàn NAV ($162,66).** Oracle không xuống thấp hơn NAV, nên chỉ NAV giảm mới gây thêm thanh lý.
- **Thanh lý theo NAV:** ở NAV hiện tại không vị thế nào bị thanh lý. Nếu NAV về ~$153 (team mint pTEAM), ~9 vị thế (~236 NET, nợ ~$23K) bị thanh lý. Từ 9/10 chỉ có ~35 lệnh thanh lý nhỏ (~$9K). Các đợt lớn đã xảy ra trước đó: 26–28/9 ($224K) và 2–3/10 ($115K).

## E. Ai đang bán

1. **Bonder:** vẫn là nguồn bán lớn nhất. Claim ~1.100–1.200 NET/ngày (7 ngày: 7.823 NET). Top bán 7 ngày đều là bonder:
   - `0x7c94…f3c0`: −$219K (claim 1.239 NET).
   - `0xf357…401d`: −$171K (claim 1.105 NET).
   - `0x708d…`: −$90K (claim 452 NET).
   - Trong 30 ngày, nhóm ví có claim bond **ròng −$5,44M**.
2. **Người thoát ở sàn:** `0x006e…` bán $64K trên DEX và 324 NET vào InverseBond. `0x6754…` (3 giao dịch từ trước đến nay) bán $63K.
3. **Nhỏ lẻ và cá voi trong 24 giờ qua** (HoodScan): nhỏ lẻ ròng **−$213K**, cá voi −$105K, "smart money" −$8K. Ở các lần đo trước (6/10, 9/10), nhỏ lẻ vẫn mua ròng.
4. **Team:** không mint pTEAM mới, các desk không nhận thêm USDG từ 6/10.

## F. Ai đang mua

1. **Một nhóm trader lướt sóng** (7 ngày):
   - `0x7ddd…100d`: +$123K.
   - `0xf41b…9e3b`: +$82K. Ví này bán 686 NET ngày 8–9/10 rồi mua lại, kể cả hai lệnh lớn gây râu nến ngày 16/10. Bản 9/10 gọi đây là "holder lâu năm thoát hàng"; thực ra là trader.
   - `0xfbd9…f720`: +$46K.
   - `0x9164…8fda`: +$45K.
2. **RWA Sleeve của team** (`0x4987…c7cb`): +$41K.
   - **Tiền đến từ Team Safe:** $10K USDG ngày 9/10, $39,3K ngày 12/10, cùng 653 SPCX (~$95K) ngày 14/10.
   - **Đã mua:** 226 NET ngày 12/10 và 8 NET ngày 13/10. Ngày 14/10, Sleeve gói 560 NET thành 127 wsNET.
   - **Bảng cân đối:** 308,9 wsNET trong ví + 813,5 wsNET thế chấp Loopback ≈ **4.978 NET** (~$0,82M). USDG $586. Cổ phiếu trong ví ~$228K.
   - **Nợ:** Morpho thế chấp cổ phiếu $3,70M / nợ $1,59M (LTV 43%, giá cổ phiếu giảm). Loopback $116K.
   - **Tổng đã mua từ 18/9:** 5.780 NET, ~$2,24M (giá vốn trung bình ~$388, cao hơn giá hiện tại ~2,3 lần).
3. **InverseBond (protocol):** 696 NET trong tuần. Đây là "người mua cuối cùng" ở ~$160.
4. **Tổng 7 ngày trên DEX:** mua $7,50M, bán $7,69M, **ròng −$185K**. 30 ngày: −$429K.

## G. Phân bổ holder

11.557 ví (+319 so với 9/10). Top 10 nắm 10,5%, top 100 nắm 40,9% lượng NET người dùng nắm giữ (NET + sNET + wsNET quy đổi, không tính contract). Ví lớn nhất giữ 2,0%. Tính cả wsNET đang thế chấp, Sleeve của team vẫn là holder lớn nhất (~4.978 NET). 14.845 NET (9,5% supply) nằm làm thế chấp trên Loopback. Chi tiết ở `data/holders_top100.csv`.

## H. Giá và dự báo

### H.1 Bản 9/10 dự báo thế nào, thực tế ra sao

| Kịch bản 9/10 | Xác suất khi đó | Thực tế đến 17/10 |
|---|:-:|---|
| Cơ sở $175–210 | ~50% | Giá ở trong vùng này ngày 10–11/10 và hồi lên 14–16/10, nhưng mỗi lần hồi đều không giữ được |
| Xấu $155–168 | ~30% | **Đã xảy ra** từ 12/10 (đáy $157,9). Hiện $165 |
| Tốt $240–290 | ~20% | Chỉ chạm bằng râu nến vài giây ($244, $339), không giao dịch được ở đó |

Lý do chính: premium co nhanh hơn dự kiến. Không còn người mua lớn, trong khi bond vẫn bán hết capacity mỗi ngày.

### H.2 Kỹ thuật
- Nến ngày (pool v2): 9/10 C $194 → 10/10 C $208 → 11/10 C $170 → 12/10 L **$157,9** C $176 → 14/10 H $221,6 C $201 → 15/10 L $159,8 C $190 → 16/10 C $166 (râu $339) → hiện $165.
- Giá nằm dưới MA7 ($177), MA20 ($258) và MA30 ($390); RSI14 ~35. Biên độ thật (bỏ râu) trong tuần là $158–221.
- Vùng $158–165 (NAV và InverseBond) đã đỡ giá bốn lần: 12/10, 13/10, 15/10 và 16–17/10.

### H.3 Toán pha loãng (mô phỏng từ hằng số contract và trạng thái 17/10)

| Giả định | Ngày 7 | Ngày 14 | Ngày 21 |
|---|---|---|---|
| Giá đứng yên $165 (premium ~1) | NAV $163 | NAV $164 | NAV $164 |
| Premium hồi về 1,3× trong 10 ngày | $197 (NAV $162) | $208 (NAV $160) | $205 (NAV $157) |
| Giá về NAV | $163 | $164 | $165 |

Khi premium ~1, pha loãng gần như dừng và NAV đi ngang. Nếu premium hồi lên, rebase và bond chạy lại và NAV giảm dần. Kiểu "pump rồi về NAV" có thể lặp lại.

### H.4 Kịch bản 1–3 tuần (xác suất chủ quan)

| Kịch bản | Xác suất | Vùng giá NET | Điều kiện / dấu hiệu |
|---|:-:|---|---|
| **Cơ sở: bám vùng NAV** | ~55% | **$158–185** (0,97–1,14× NAV) | InverseBond đỡ ở ~$160 (~$236K/ngày); premium nào xuất hiện cũng bị bond bán ra (~1.170 NET/ngày); team mua nhỏ giọt; RH chain đi ngang |
| **Xấu: thủng sàn tạm thời / NAV giảm** | ~25% | **$145–158** | Team mint pTEAM (9,8K NET), NAV còn ~$153; nhiều người thoát cùng lúc vượt sức mua của InverseBond (thanh khoản mỏng, giá có thể xuống dưới sàn trong vài giờ); BTC thủng $77–80K; Earn rút mạnh hơn |
| **Tốt: premium quay lại** | ~20% | **$190–240** (1,15–1,45× NAV) | Cầu mới: Fables TGE (20/10) kéo thanh khoản về chain, kết quả quý 3 Robinhood (27/10), team nạp thêm tiền, BTC lấy lại $85K+. Trên 1,75× NAV ($285) rebase chạy tối đa |

Từ $165: **−3% xuống sàn InverseBond ($160)**, **−7% nếu team mint pTEAM ($153)**, **+15% lên $190**, **+28% lên 1,3× NAV ($211)**. So với tuần trước, phía giảm giờ được cơ chế chặn gần hơn nhiều. Nhưng NET ở NAV về bản chất là một khoản USDG có rủi ro team (pTEAM), rủi ro contract (Morpho/Steakhouse, oracle), và quyền rút qua InverseBond bị giới hạn ~1% liquid mỗi 8 giờ. Muốn có lợi nhuận phía trên NAV thì cần người mua mới.

### H.5 Robinhood Chain 2–4 tuần tới
- **Cơ sở:** đi ngang hoặc co nhẹ. Volume DEX $5–8 tỷ/tuần, phí $15–20M/tuần. Stablecoin ~$1,05–1,10 tỷ. Earn rút dần nếu thưởng Merkl tiếp tục giảm. ETH tiếp tục rút. Cổ phiếu token hoá có thể tiếp tục mint ròng nhẹ.
- **Rủi ro:** thưởng Earn giảm mạnh làm vòng vay USDe ↔ USDG gỡ nhanh, stablecoin có thể giảm hàng trăm triệu USD. BTC thủng $77–80K.
- **Có thể đảo chiều nếu:** Fables TGE và ve(3,3) kéo được thanh khoản mới; USDG tăng > +$20M/tuần; bridge ETH vào ròng; kết quả quý 3 (27/10) có tin mới cho chain.

### H.6 Theo dõi on-chain
- `InverseBond.capacityRemaining()` và `Treasury.liquidUsdg()`: sàn chỉ mạnh khi còn USDG liquid ($7,86M; mỗi epoch dùng tối đa 1%).
- `pTEAM.exercised()` (đang 13.320) và NET chuyển vào các desk: tín hiệu team chuẩn bị bán.
- RWA Sleeve `0x4987…c7cb` và Team Safe `0x3bb7…5f42`: USDG/SPCX chuyển qua lại, mua NET, nợ Loopback.
- `Distributor.premium()`: > 1,1 thì rebase chạy lại; > 1,75 thì tối đa.
- RH chain: vault Earn (`0xbeef…09dd`), tổng cung USDG/USDe, bridge ETH, cổ phiếu token hoá (`scripts/rh_flows.py`, `scripts/rh_chain.py`).

## I. Rủi ro chính
1. **Tập trung vào team:** một EOA ký 1-of-1 cho Team Safe và RWA Sleeve. pTEAM không hết hạn, team luôn mint được 15% float với giá $1 (hiện 9.779 NET).
2. **Sàn có giới hạn:** InverseBond chỉ dùng 1% USDG liquid mỗi 8 giờ; 70% RFV nằm trong Morpho/Steakhouse, không dùng trực tiếp cho InverseBond.
3. **Đòn bẩy của team:** nợ $1,59M trên các market cổ phiếu (gần 100% vốn) và $116K trên Loopback, thế chấp bằng chính NET.
4. **Docs chưa khớp với chain:** NET trong desk đến từ pTEAM chứ không phải mua trên thị trường; ít nhất 4 desk do Team Safe quản lý không được công bố.
5. **Thanh khoản mỏng** ($1,13M) so với FDV ~$26M; 89,8% supply có thể rút stake ngay.
6. **Hệ sinh thái co lại;** tiền gửi lấy lãi (trụ đỡ lớn nhất) bắt đầu rút.

## J. Phương pháp và tái lập
- **Nguồn:** RPC `rpc.mainnet.chain.robinhood.com` (eth_getLogs, block) và `robinhood.drpc.org` (eth_call lịch sử, Multicall3), `eth.drpc.org` (bridge trên L1), Sourcify (ABI, mã nguồn `LoopbackOracle`), DefiLlama (kể cả yields của vault Earn), DexScreener, GeckoTerminal, CoinGecko, alternative.me, HoodScan (MCP công khai), tin tức (link trong bài).
- **Phân loại dòng tiền NET** (`scripts/flows.py`): ~654K transaction, ~44K ví. Delta mỗi địa chỉ được quy về NET (NET + sNET + wsNET × index). Pool, contract protocol và router được loại ra; phần còn lại là ví người dùng. USD quy theo nến 4 giờ. Thời gian quy từ block theo mốc binary-search (`data/block_anchors.json`).
- **Dòng tiền RH chain** (`scripts/rh_flows.py`): tổng cung USDG/USDe/U/WETH và tài sản vault Steakhouse đọc lúc 00:00 UTC mỗi ngày từ 1/7. Cổ phiếu token hoá (191 mã) nhân giá hiện tại, nên thay đổi là mint/burn. Các market Morpho Blue cho vay USDG đọc theo ngày. Số giao dịch người dùng ước tính bằng 100 block mẫu mỗi ngày; ngày đã xong được giữ lại, chỉ tính thêm ngày mới.
- **Giới hạn:** HoodScan gán giao dịch theo `tx.from`, ở đây gán theo người gửi/nhận token, nên số tổng có thể lệch. Giá trị bán qua desk là ước tính. Số giao dịch/ngày có sai số lấy mẫu (xem theo tuần). ETH quy USD theo giá hiện tại; số bridge theo tuần thay đổi nhẹ theo giờ lấy mẫu. Xác suất các kịch bản là đánh giá chủ quan.

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
python3 rh_chain.py                                                # DefiLlama, bridge ETH, vĩ mô, meme, stock token, lợi suất Earn
python3 rh_protocols.py                                            # TVL theo protocol, volume DEX và phí theo nhóm
python3 rh_flows.py all                                            # stablecoin, Earn, cổ phiếu token hoá, Morpho, số giao dịch theo ngày
python3 rh_flow_summary.py                                         # bảng dòng tiền theo tuần
python3 build_report.py                                            # report.html
```
`raw/` (~330MB log) không được commit. `fetch_transfers.py` resume từ file `.cursor`. Chạy `team.py` **sau khi** hai lệnh `trace_addr.py` đã xong.

### File dữ liệu
| File | Nội dung |
|---|---|
| `data/latest_state.json`, `data/protocol_history_12h.csv` | Trạng thái protocol hiện tại và lịch sử 12h |
| `data/daily_flows.csv`, `data/weekly_supply_flows.csv` | Mint theo nguồn, claim bond/desk, InverseBond, stake/unstake, mua/bán theo ngày/tuần |
| `data/net_flow_by_category_30d.csv`, `data/top_traders_7d.csv`, `data/top_traders_30d.csv` | Ai mua, ai bán |
| `data/team_summary.json`, `data/team_pteam_to_desks.csv`, `data/sleeve_net_buys_daily.csv`, `data/desk_usdg_flows.csv` | Team, desk, RWA Sleeve |
| `data/loopback_summary.json`, `data/loopback_positions.json` | Market Loopback: lãi vay, oracle, vị thế, bậc thanh lý |
| `data/holders_top100.csv`, `data/pools.csv` | Holder, pool |
| `data/market/rh_flow_weekly.csv`, `data/market/rh_flow_summary.json` | Dòng tiền RH chain theo tuần, đỉnh, hiện tại, lợi suất Earn |
| `data/market/rh_daily_flows.csv`, `rh_stock_supply_daily.csv`, `rh_morpho_usdg_daily.csv`, `rh_morpho_usdg_borrow_by_collateral.json`, `rh_activity.csv` | Chuỗi on-chain theo ngày: stablecoin, Earn, cổ phiếu token hoá, Morpho, số giao dịch |
| `data/market/rh_protocols.csv`, `rh_dex_by_protocol_weekly.csv`, `rh_fees_by_category_weekly.csv` | TVL theo protocol, volume DEX theo protocol, phí theo nhóm (DefiLlama) |
| `data/market/rh_chain_weekly.csv`, `rh_chain_summary.json`, `rh_l1_bridge_eth.json`, `rh_stables_breakdown.json` | DefiLlama theo tuần, bridge ETH trên L1 |
| `data/market/market_snapshot.json`, `hs_chain_status.json` | BTC/ETH, Fear & Greed, token hệ sinh thái, stock token, meme (đã loại wash trade); trạng thái HoodScan |
