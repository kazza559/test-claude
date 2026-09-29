# TGE muộn biến YT OnRe thành vé số nhỏ

*Dữ liệu chốt ngày 29/09/2026. Quy ước số: dấu chấm là dấu thập phân, B = tỷ, M = triệu. Mọi con số mô hình đều có công thức ở mục 5 để bạn tự chạy lại với giả định của mình.*

OnRe (ONyc) là một trong những tài sản lợi suất thật tốt nhất trên Solana: AUM **$290M**, APY thực hiện **~11%** đến từ phí tái bảo hiểm, có giấy phép của Cơ quan Tiền tệ Bermuda (BMA). Tuy vậy, dự án **chưa công bố token, tokenomics hay ngày TGE**. Docs nói point "không đại diện cho quyền nhận token", Polymarket chỉ định giá **14%** cho việc ra token trước 31/12/2026, và chưa có pre-market nào. Vì vậy kịch bản cơ sở của báo cáo là snapshot cuối Q1/2027 và **TGE trong Q2/2027**, với khoảng **30% khả năng không có airdrop cho point đến hết 2027**. Đối chiếu với 17 token stablecoin/yield/RWA đã TGE trong 2025–26, vốn có trung vị **giảm 68% so với giá đóng cửa ngày đầu**, FDV hợp lý nghiêng bearish cho OnRe là **$80–400M, cơ sở ~$200M**. Quỹ point hiện có **240.9B** và phình thêm **1.32B mỗi ngày**, nên đến snapshot cơ sở sẽ đạt ~**506B**. Với 5% nguồn cung dành cho point và chiết khấu hiện thực hóa 30%, mỗi 1M point đáng khoảng **$13.8**. YT ONyc-10JAN27 trên Exponent giá **$0.0329** cho **242 point mỗi $ mỗi ngày** (hệ số 8x). Khoảng 86% vốn mua YT quay về dưới dạng yield ONyc sau phí 5.5%, nên **chi phí ròng chỉ ~14% vốn** và điểm hòa vốn là **$5.6 mỗi 1M point (8x) hoặc $9.0 (5x)**. Với vé $1k trong 103 ngày, kỳ vọng dương mỏng: **+12% nếu 8x, +2% nếu 5x**. Phân phối lãi lỗ lệch phải: 10% khả năng lãi 60–107%, 55% khả năng lỗ 8–14%. Nếu tính thêm rủi ro người dùng Việt Nam bị loại khỏi airdrop (Việt Nam nằm trong danh sách khu vực bị loại trừ của ONyc), kỳ vọng rơi về **khoảng −3% đến +4%**. Khuyến nghị: chỉ mua YT như một vé quyền chọn nhỏ (≤$10k, đặt lệnh limit, giữ đến đáo hạn); không mua size lớn; không mua YT srONyc.

## ONyc tăng AUM 19 lần nhưng vừa có tuần rút ròng đầu tiên

OnRe không phát hành stablecoin theo nghĩa hẹp. ONyc là token định giá theo NAV, không rebase, đại diện phần sở hữu một tài khoản tách biệt (segregated account) tại Bermuda dùng để bảo lãnh các hợp đồng bảo hiểm và tái bảo hiểm ngắn hạn. Docs ghi thẳng: "It is not a stablecoin" ([OnRe Docs](https://docs.onre.finance/introduction/onre-tokenized-reinsurance-onyc)). Lợi suất có hai nguồn: phí tái bảo hiểm thu trước rồi ghi nhận dần, và lợi suất của tài sản thế chấp (T-bill, USDG, sUSDe, syrupUSDC…). Theo Allez Labs, tại 31/07/2026 có **$144.3M (58% AUM)** đang triển khai vào bảo lãnh với lợi suất ~13.6% trên phần vốn này, và rate-on-line của danh mục là 16.93% trên $165M exposure ([Allez](https://allez.xyz/reports/onre/ONyc_Asset_Risk_Assessment_260731.pdf)). Kết quả là đường NAV gần như tuyến tính: **$1.009 (28/05/2025) → $1.1506 (29/09/2026)**. APY hiện tại là **11.02%**; tính theo năm trên các cửa sổ 30, 90 và 365 ngày lần lượt là 11.35%, 11.83% và 11.20%. Cả lịch sử chỉ có 4 ngày NAV giảm, đều rơi vào tháng 7/2025 ([OnRe NAV API](https://core.api.onre.finance/data/nav); [OnRe live APY](https://core.api.onre.finance/data/live-apy)). Mức ~11% thấp hơn mục tiêu "16% base APY" lúc ra ONyc (07/2025), nhưng đã ổn định trong dải 9.3–13.4% từ tháng 11/2025 ([OnRe review 01/2026](https://www.onre.finance/blog/onre-in-review-january-2026); [OnRe review 11/2025](https://www.onre.finance/blog/onre-in-review-november-2025)).

Tăng trưởng rất mạnh nhưng đang chững lại. AUM đi từ **$15.2M (01/07/2025)** lên $73.5M đầu năm 2026, đạt đỉnh **$302.6M ngày 21/09/2026**, rồi lùi về **$290.3M ngày 29/09**. Nguồn cung giảm 4.3%, tương đương ~11.3M ONyc bị rút ròng. Đây là đợt rút ròng kéo dài đầu tiên, trùng với thời điểm ra Liquidity Engine (24/09) và "Season 1" (27/09) ([OnRe NAV API](https://core.api.onre.finance/data/nav)). Trên DefiLlama, TVL tăng 43% trong 90 ngày nhưng chỉ 3.5% trong 30 ngày ([DefiLlama](https://api.llama.fi/protocol/onre)). Cấu trúc vốn đáng chú ý hơn con số tổng: **63.6% nằm trên Kamino, 21% trên Loopscale, 12.4% trên Exponent** ([OnRe rewards API](https://rewards.api.onre.finance/api/v1/analytics/overview)). Nói cách khác, phần lớn ONyc đang nằm trong các vòng loop đòn bẩy ăn point 6x. Đây là TVL có yếu tố săn point, nên có rủi ro rời đi sau TGE. ONyc hiện là RWA số 1 trên Solana theo DeFi active TVL, chiếm ~45% thị phần ([OnRe blog](https://www.onre.finance/blog/onyc-is-the-1-real-world-asset-on-solana-by-defi-active-tvl)).

Hào lũy của OnRe là pháp lý. On Re SAC Ltd giữ giấy phép BMA **Class IIGB** (bảo hiểm) và **Class F DABA** (tài sản số) ([OnRe blog](https://www.onre.finance/blog/onre-evolves-one-into-onyc-to-power-stablecoin-adoption-across-defi-and-traditional-markets)). Allez xếp ONyc vào hạng "High Quality Collateral", với điểm pháp lý thành phần AA+ ([OnRe Docs](https://docs.onre.finance/security-and-verification/independent-risk-analysis)). Về vốn, lần tái ra mắt tháng 5/2025 có Ethena, Solana Ventures và RockawayX hậu thuẫn ([The Block](https://www.theblock.co/post/355248/solana-backed-onre-taps-ethena-for-first-one-token-and-pool-targets-750-billion-reinsurance-market)). Vòng **Series A $5M ngày 05/05/2026** do Forward Industries (Nasdaq: FWDI) và RockawayX đồng dẫn, kèm cam kết Forward rót tới $25M vào ONyc ([OnRe blog](https://www.onre.finance/blog/forward-industries-and-rockawayx-co-lead-strategic-investment-in-onre-to-accelerate-onchain-reinsurance-on-solana)). Mặt tối nằm ở lịch sử: OnRe là Nayms được tái cấu trúc ([Insurtech Gateway](https://www.insurtechgateway.com/2025/05/29/insurance-incubator-to-on-chain-reinsurer/)). Nayms từng gọi ~$12M, gồm một vòng bán token ở định giá $80M ([FinSMEs](https://www.finsmes.com/2023/04/nayms-raises-funding-at-80m-valuation.html)). Token NAYM mở bán công khai ở $0.05, tương đương FDV ~$50M ([TradingView/GlobeNewswire](https://www.tradingview.com/news/reuters.com,2024-10-23:newsml_GNXbY3K1j:0-naym-token-public-sale-goes-live-giving-participants-access-to-230-billion-reinsurance-market/)), và nay giao dịch quanh $0.00005, tức **mất ~99.9%** ([CoinGecko NAYM](https://www.coingecko.com/en/coins/naym)). Chưa có tuyên bố công khai nào về quyền lợi của nhà đầu tư token thời Nayms trong một token OnRe tương lai. Đây là rủi ro pha loãng chưa định lượng được và là một vết sẹo về danh tiếng.

Rủi ro cốt lõi có thể đo được. ONyc chưa từng trả bồi thường thảm họa nào trong 429 ngày. Tuy vậy, Allez mô phỏng một sự kiện cỡ bão Sandy làm **NAV giảm 13.1–22.1%**. Độ sâu bán trên DEX chỉ ~$2.14M ở mức trượt giá 2%, trong khi có $166.6M ONyc đang được dùng làm tài sản thế chấp. Hai multisig 3-of-6 nắm quyền nâng cấp chương trình đều có **time_lock = 0**. Top 10 thực thể (sau khi gộp ví) nắm 48.8% nguồn cung ([Allez](https://allez.xyz/reports/onre/ONyc_Asset_Risk_Assessment_260731.pdf)). Khả năng tích lũy giá trị cho một token cũng mờ. DefiLlama ghi nhận ~$32.4M phí/năm nhưng chỉ ~$0.9M doanh thu giao thức ([DefiLlama fees](https://api.llama.fi/summary/fees/onre?dataType=dailyFees)), và OnRe chưa công bố phần họ giữ lại (take rate).

So với nhóm stablecoin/yield đã TGE, TVL ~$290M của OnRe nằm đúng vùng TVL lúc TGE của Re ($258M), Resolv ($351M), OpenEden USDO ($235M), Cap ($221M) và Solstice USX ($401M). Khác biệt lớn nhất là nhóm tài sản. Các "đô la basis-trade" co lại mạnh: USDe giảm 67% từ đỉnh $14.82B, USDf giảm 44%, USX giảm 58% chỉ trong hai tháng. Trong khi đó, tài sản có dòng tiền thế giới thực lại tăng: reUSD tăng ~2.5 lần và ONyc tăng ~4 lần từ đầu năm ([DefiLlama stablecoins](https://stablecoins.llama.fi/stablecoins)). Nguồn cung stablecoin sinh lời giảm 15% trong Q2/2026, trong khi các sản phẩm dựa trên trái phiếu Kho bạc vẫn tăng ([CMC Academy](https://coinmarketcap.com/academy/article/yield-bearing-stablecoin-supply-falls-q2-2026-treasury-backed-growth)). Như vậy OnRe đứng ở phía đúng của sự phân hóa này. Nhưng tiềm năng sản phẩm và tiềm năng token là hai chuyện khác nhau. Yield chảy về người giữ ONyc. Một token quản trị phải đứng ngoài thực thể bảo hiểm được cấp phép. Và chính bài "2026 Outlook" của OnRe viết rằng token quản trị "are forced to earn their place" ([OnRe blog](https://www.onre.finance/blog/2026-outlook)). Đánh giá: **sản phẩm tốt hơn phần lớn các đối thủ đã TGE, còn token chỉ ở mức trung bình**, vì bị kìm bởi cơ chế tích lũy giá trị yếu, di sản Nayms và một thị trường đang trả rất ít cho token yield mới.

## Token stablecoin ra mắt 2025–26 mất trung vị 68% so với ngày đầu

Bảng dưới lấy giá từ CoinGecko API và nến ngày của sàn (FDV ngày đầu = giá đóng cửa ngày đầu × tổng cung), còn TVL lấy từ DefiLlama ([CoinGecko API](https://api.coingecko.com/api/v3/coins/re); [Binance klines](https://data-api.binance.vision/api/v3/klines?symbol=RESOLVUSDT&interval=1d&startTime=0&limit=5); [DefiLlama](https://api.llama.fi/protocol/re)). Tỷ lệ airdrop lấy từ tài liệu của từng dự án: Ethena ([The Defiant](https://thedefiant.io/news/defi/ethena-labs-ena-launches-at-usd1-billion-post-airdrop-as-sats-campaign-kicks-off)), Usual ([CoinGecko Learn](https://www.coingecko.com/learn/what-is-usual-crypto-rwa-usual-airdrop)), Resolv ([Resolv docs](https://docs.resolv.xyz/litepaper/resolv-token/resolv-token-airdrop)), Falcon ([Falcon](https://falcon.finance/news/introducing-ff-tokenomics)), OpenEden ([OpenEden docs](https://docs.openeden.com/openeden-foundation/eden/eden-token-distribution)), Solstice ([SolanaFloor](https://solanafloor.com/news/solstice-slx-launch-sparks-backlash-from-airdrop-farmers-over-surprise-vesting)), Re ([Re docs](https://docs.re.xyz/re-points/about-re-points.md)), Cap ([The Defiant](https://thedefiant.io/news/defi/cap-labs-cap-token-auction-106m-fdv-oversubscription)) và USD.AI ([USD.AI](https://usd.ai/insights/chip-is-live)).

| Token | TGE | Số tháng farm point | Airdrop mùa 1 (% cung) | FDV ngày đầu ($M) | FDV 29/09/2026 ($M) | So với ngày đầu | FDV/TVL lúc TGE |
|---|---|---|---|---|---|---|---|
| ENA (Ethena) | 04/2024 | 1.4 | 5% | 11,625 | 3,810 | −67% | 7.45x |
| USUAL (Usual) | 11/2024 | 4–6 | 7.5% + 7.5% Launchpool | ~1,141 | 28 | −95% | 3.0x |
| RESOLV (Resolv) | 06/2025 | ~8.8 | 10% | 351 | 19 | −95% | 1.00x |
| HUMA (Huma, Solana) | 05/2025 | ~1.5 | 5% + 2.5% | 669 | 290 | −57% | n/a |
| FF (Falcon) | 09/2025 | ~6 | ≤8.3% + 1.5% | 2,817 | 1,206 | −57% | 1.48x |
| EDEN (OpenEden) | 09/2025 | ~8.5 | 7.5% + 1.5% | 400 | 64 | −84% | 1.70x |
| UP (Unitas, Solana) | 03/2026 | ~9 | 3% Booster | 60 | 239 | +298% | 0.74x |
| CHIP (USD.AI) | 04/2026 | ~7 | 3% | 613 | 452 | −26% | 2.18x |
| SLX (Solstice, Solana) | 05/2026 | ~8 | 8.5% | 207 | 66 | −68% | 0.52x |
| **RE (Re, tái bảo hiểm)** | **06/2026** | **10.5** | **7% (+ mùa 2 ≥3.5%)** | **436** | **479** | **+10%** | **1.69x** |
| CAP (Cap) | 06/2026 | ~10.5 | stabledrop $4.2M | 293 | 581 | +98% | 1.33x |

Trong 17 token ra mắt 2025–26 có dữ liệu giá, **13 token đang dưới giá đóng cửa ngày đầu**. Trung vị thay đổi so với ngày đầu là −27% sau 7 ngày, −36% sau 30 ngày, **−51% sau 90 ngày**, −68% hiện tại, và trung vị mức sụt từ đỉnh là **−89%**. Trung vị FDV/TVL ngày đầu của 12 giao thức yield là ~1.4x, nay còn ~1.1x. FDV ngày đầu co lại qua từng lứa: ~$1.68B (2024), ~$495M (nửa đầu 2025), ~$671M (nửa cuối 2025, chỉ tính giao thức) và chỉ **~$293M cho lứa 2026**. TVL sau TGE thường không giữ được: trung vị TVL hiện tại chia cho TVL lúc TGE là **0.68**, với Resolv 0.04, OpenEden 0.06, Solstice 0.54, ngược lại Re 1.51 và Cap 1.32 (tính từ [DefiLlama](https://api.llama.fi/protocol/resolv) và nến sàn ở trên). Các nghiên cứu độc lập cho kết quả tương tự. Memento Research đếm 118 TGE năm 2025 và thấy ~85% đang dưới định giá TGE, trung vị giảm hơn 70% ([CoinDesk](https://www.coindesk.com/business/2026/01/06/why-crypto-s-new-token-issues-are-falling-flat-and-what-comes-next)). Bán token công khai trong Q2/2026 chỉ huy động $58M, quý tệ nhất trong 5 năm ([CryptoRank](https://cryptorank.io/insights/analytics/q2-2026-the-worst-ico-quarter)).

Bài học từ các token còn đứng vững khá rõ. Những token giữ giá hoặc tăng đều **ra mắt ở FDV thấp** (UP bán ở FDV $5M; CAP đấu giá ở $106M) hoặc **có TVL tiếp tục tăng sau TGE** (Re +51%, Cap +32%). Những token sập thường có lượng airdrop lớn chờ bán kèm TVL rút đi. Solstice, token Solana gần OnRe nhất về hệ sinh thái, còn gây phẫn nộ vì vesting bất ngờ và cơ chế chia tầng khiến 99.68% người dùng chỉ chia nhau 0.49% quỹ airdrop ([SolanaFloor](https://solanafloor.com/news/solstice-slx-launch-sparks-backlash-from-airdrop-farmers-over-surprise-vesting)). Nhóm yield-dollar còn chịu hai cú sốc niềm tin năm 2026. Resolv bị khai thác lỗ hổng, kẻ tấn công mint 80M USR không có tài sản bảo chứng và rút ~$25M ([The Block](https://www.theblock.co/post/394582/resolvs-usr-stablecoin-depegs-after-attacker-mints-80-million-unbacked-tokens-extracts-roughly-25-million)). Drift trên Solana mất ~$285M ([CoinDesk](https://www.coindesk.com/business/2026/04/02/north-koreans-hackers-likely-behind-the-usd286-million-drift-protocol-exploit-elliptic)).

Bối cảnh vĩ mô là hồi phục sớm, chưa phải bull. BTC ở $83.7k, thấp hơn 33% so với đỉnh 365 ngày $124.7k dù đã tăng 39% trong 3 tháng. DeFi TVL toàn thị trường là $94.4B (−45% từ đỉnh), Solana TVL $6.44B (−51%), còn tổng cung stablecoin đi ngang quanh $311B kể từ tháng 5 ([CoinGecko](https://api.coingecko.com/api/v3/global); [DefiLlama](https://api.llama.fi/v2/historicalChainTvl)). Rủi ro Fed tăng lãi suất vẫn là lực cản chính, và giới phân tích coi mốc $77.2k là ngưỡng mà nếu thủng thì đà hồi phục bị phủ định ([CoinDesk](https://www.coindesk.com/markets/2026/09/01/bitcoin-enters-rektember-as-rate-hike-risks-threaten-its-august-rally)). Với một TGE diễn ra 6–9 tháng tới, giả định an toàn là thị trường không tốt hơn hiện nay.

## TGE cơ sở rơi vào Q2/2027, FDV cơ sở quanh $200M

### Không có tín hiệu nào cho TGE trước cuối năm 2026

Bằng chứng chính thức về một token rất mỏng và đã cũ. Bài ra mắt tháng 5/2025 có nhắc tới "the $ONRE protocol token" ([OnRe blog](https://www.onre.finance/blog/onre-backed-by-ethena-solana-ventures-and-rockawayx-launches-structured-yield-product-combining-real-world-stability-and-on-chain-upside)), và The Block viết người gửi tiền sẽ nhận "allocation in the eventual ONRE token" ([The Block](https://www.theblock.co/post/355248/solana-backed-onre-taps-ethena-for-first-one-token-and-pool-targets-750-billion-reinsurance-market)). Từ đó đến nay, không có kênh chính thức nào nhắc lại. Docs hiện hành ghi point "do not represent any entitlement to tokens" ([OnRe Docs](https://docs.onre.finance/onyc-in-defi/onre-points-program)). Chương trình "ONyc Compounding Interest Rewards Season 1" mở ngày 27/09/2026 là phần thưởng lãi kép cho vị thế nắm giữ từ 60 ngày trở lên, không phải mùa point hay sự kiện token ([Solana Compass](https://solanacompass.com/news/onre-surpasses-300m-aum-as-onyc-compounding-interest-rewards-season-1-opens-september-27)). Thị trường cũng không kỳ vọng TGE sớm. Polymarket định giá khả năng ra token là **14% trước 31/12/2026, 25.5% trước 31/03/2027, 51.5% trước 30/06/2027 và 69.5% trước 30/09/2027**, dù thanh khoản rất mỏng (~$13k khối lượng) ([Polymarket](https://polymarket.com/event/will-onre-launch-a-token-by)). Whales Market và Hyperliquid chưa có pre-market nào cho ONRE ([Whales Market API](https://api.whales.market/v2/tokens); [Hyperliquid API](https://api.hyperliquid.xyz/info)).

Lập luận cho một TGE muộn mạnh hơn lập luận cho TGE sớm. Vòng Series A tháng 5/2026 giảm áp lực phải gọi vốn qua token. Cấu trúc token phải tách khỏi thực thể bảo hiểm được cấp phép. Season 1 yêu cầu giữ 60 ngày nên mốc đủ điều kiện sớm nhất là ~26/11/2026, trùng lúc mùa bão Đại Tây Dương kết thúc (30/11). Exponent vừa mở kỳ hạn tháng 01/2027 kèm boost point, và cấu hình của Exponent ghi "season: 1" ([Exponent points config](https://app.exponent.finance/api/points/config)). Điều đó gợi ý chương trình point còn chạy ít nhất tới đầu năm 2027. Các dự án cùng nhóm như Solstice và Cap cũng đã lùi TGE 4–6 tháng so với kế hoạch. Ở chiều ngược lại, chương trình point đã chạy **12.6 tháng**, dài hơn trung vị ~8.5 tháng của nhóm so sánh. AUM đang rút ròng, nên một token có thể được dùng để kéo vốn quay lại. Re vừa cho thấy một TGE tái bảo hiểm có thể giữ giá. Breakpoint (15–17/11/2026, London) cũng là sân khấu tự nhiên để công bố ([Solana Compass](https://solanacompass.com/news/solana-breakpoint-2026-comes-to-london-for-the-first-time-november-15-17-at-olympia)). Mùa bão 2026 đặc biệt êm: đến 21/09 chưa có cơn bão cấp hurricane nào, lần đầu tiên kể từ 1914 ([Wikipedia](https://en.wikipedia.org/wiki/2026_Atlantic_hurricane_season)). Điều này giúp OnRe có một năm "không tổn thất" để kể chuyện, nên nếu có công bố thì hợp lý nhất là sau 30/11.

| Mốc TGE | Polymarket (29/09) | Ước tính của báo cáo | Kịch bản dùng trong mô hình YT |
|---|---|---|---|
| Trước 31/12/2026 | 14% | ~10% | Bull: snapshot ~31/12/2026, TGE từ cuối 2026 đến 02/2027 (10%) |
| Trước 31/03/2027 | 25.5% | ~20–25% | |
| Trước 30/06/2027 | 51.5% | ~40–45% | Base: snapshot 31/03/2027, TGE Q2/2027 (35%) |
| Trước 30/09/2027 | 69.5% | ~55–60% | Bear: snapshot 30/06/2027, TGE nửa cuối 2027 (25%) |
| Không token hoặc không airdrop cho point đến hết 2027 | ~30% | ~30–40% | Zero (30%) |

### Các phương pháp định giá hội tụ quanh $150–350M trước khi chiết khấu

Bảng dưới áp các bội số của nhóm so sánh lên TVL ~$295M của OnRe. Nguồn gồm các bảng so sánh ở mục 2, [DefiLlama fees](https://api.llama.fi/summary/fees/re?dataType=dailyFees) cho bội số phí, và phép tính giá trị airdrop trên mỗi $1k TVL-ngày của các chương trình point đã kết thúc (Solstice $0.28, Resolv $0.44, Re ~$0.61, OpenEden $0.67).

| Phương pháp | Bội số | FDV ngụ ý cho OnRe |
|---|---|---|
| Solstice hiện tại | 0.30x TVL | ~$90M |
| Solstice lúc TGE | 0.52x TVL | ~$150M |
| Huma hiện tại | 0.74x TVL | ~$220M |
| Trung vị ngành hiện tại | ~1.0–1.1x TVL | ~$295–325M |
| Re hiện tại (so sánh gần nhất) | 1.18–1.23x TVL | ~$350–360M |
| Trung vị ngày đầu 2025–26 | ~1.4x TVL | ~$410M |
| Re ngày đầu | 1.69x TVL | ~$500M |
| Giá trị airdrop/TVL-ngày (Solstice → OpenEden), giả định 7% cung | $0.28–0.67 mỗi $1k-ngày | ~$215–510M |
| FDV/phí (Huma 9.5x → Re 24x) trên $32.4M phí | 9.5–24x | $310–780M (bị thổi phồng vì phí chủ yếu trả cho người giữ ONyc) |

Báo cáo chiết khấu các con số trên vì năm lý do. Thứ nhất, TVL lúc TGE có thể thấp hơn hiện nay: ~85% vốn nằm trong các vòng loop săn point, và trung vị TVL giữ lại sau TGE chỉ 0.68, nên TVL có thể về ~$200M. Thứ hai, chưa có tín hiệu nào về việc niêm yết spot trên Binance; các đợt ra mắt chỉ qua Binance Alpha (SLX, DAM, UP) có FDV thấp nhất nhóm. Thứ ba, di sản Nayms kéo theo cả rủi ro cap table lẫn định kiến của thị trường. Thứ tư, cơ chế tích lũy giá trị của token chưa rõ. Thứ năm, ngay cả RE, so sánh gần nhất, cũng giảm ~24% trong 90 ngày gần nhất dù thị trường hồi phục ([DefiLlama coins](https://coins.llama.fi/chart/coingecko:re?start=1781740800&span=40&period=4h)). Re còn có lợi thế riêng: niêm yết Binance spot từ ngày đầu và sổ phí bảo hiểm tự báo cáo ~$500M ([Re](https://re.xyz/insights/re-tge-launch)). Từ đó, dải FDV lúc TGE nghiêng bearish là **Bear $80–120M (điểm $100M), Base $150–250M (điểm $200M), Bull $300–450M (điểm $350M)**. Khoảng rộng tổng thể là $80–500M. Mô hình YT bên dưới dùng giá trị ngày TGE, sau đó trừ thêm một khoản chiết khấu hiện thực hóa (h) để phản ánh việc giá thường giảm và bị vesting trong những tuần đầu.

## Quỹ point 241 tỷ đang phình thêm 1.3 tỷ mỗi ngày

"OnRe Points" chạy từ **11/09/2025**, có ghi nhận hồi tố cho hoạt động từ tháng 8/2025 ([OnRe blog](https://www.onre.finance/blog/onre-introduces-points-program-rewarding-onyc-participation-across-defi)). Công thức gốc là **1 point cho mỗi ONyc mỗi ngày**. Point tính trên số đơn vị ONyc tương đương chứ không theo giá trị USD, rồi nhân với hệ số của nơi gửi và hệ số cá nhân. Point đã kiếm **không bao giờ bị thu hồi** và không có trần tổng. Snapshot bảng xếp hạng chụp mỗi ngày lúc 00:00 UTC, còn số dư cập nhật theo giờ. Một người được dùng nhiều ví. PT không được point. YT giao dịch qua order book được tính point theo số dư cao nhất trong kỳ ([OnRe Docs](https://docs.onre.finance/onyc-in-defi/onre-points-program)). Chương trình giới thiệu thưởng **+10% point của người được giới thiệu cho người giới thiệu, và +5% cho người được giới thiệu**; chỉ kích hoạt khi người được giới thiệu giữ ≥100 ONyc, không giới hạn số lượng ([OnRe Docs](https://docs.onre.finance/onyc-in-defi/referral-and-ambassador-program)).

| Hoạt động | Nơi | Hệ số (docs) | Hệ số thực tế đang thấy |
|---|---|---|---|
| Giữ trong ví | Ví | 1x | 1x |
| Cung cấp thanh khoản | Orca, Raydium, Kamino LP | 2x | 2x |
| Cho vay/gửi (kể cả stablecoin) | Kamino 3x, Loopscale USDC 3x, Elemental 4x, Accountable (ETH) 4x | 3–4x | 3–4x |
| **YT ONyc** | **Exponent** | **5x** | **8x theo config Exponent (cập nhật 21/09/2026)** |
| YT srONyc | Exponent | 5x | 4x theo config Exponent |
| Loop/đòn bẩy | Kamino "6x + Leverage", Loopscale 6x | 6x | 6x trên tài sản thế chấp gộp (boost 10x đến 21/09) |
| PT | Exponent | 0 | 0 |

Nguồn: [OnRe Docs](https://docs.onre.finance/onyc-in-defi/referral-and-ambassador-program), [Exponent points config](https://app.exponent.finance/api/points/config), bài farmer về đợt boost đến 21/09 ([KuCoin](https://www.kucoin.com/fil/news/trends/SOL/6aa10e424ca39f00075ef63a)). Hệ số YT đã đổi nhiều lần: 4x lúc ra mắt năm 2025, 5x trong docs hiện tại, 16x trong đợt boost kết thúc 21/09, và 8x trong config Exponent sau ngày đó.

Nguồn cung point được đo trực tiếp từ API chính thức. Tổng là **240.9B point** (234.39B point gốc + 6.51B point giới thiệu) trên **23,899 ví**. Tốc độ phát hành ổn định trong 7 ngày gần nhất là **1.32–1.33B/ngày**, tương đương ~5 point gốc cho mỗi ONyc lưu hành mỗi ngày, tức hệ số trung bình hiệu dụng khoảng 5x ([OnRe rewards API](https://rewards.api.onre.finance/api/v1/analytics/overview); [points growth](https://rewards.api.onre.finance/api/v1/analytics/points/growth)). Lạm phát point đang tăng tốc. Theo tracker cộng đồng, tổng point là 53.9B (23/03) → 121.3B (30/06) → 182.2B (25/08) → 239B (29/09). Tốc độ bình quân vì thế tăng từ ~0.68B/ngày (tháng 3–6) lên 1.31B/ngày (tháng 7–9) và 1.68B/ngày trong 30 ngày gần nhất, con số sau cùng có tính các đợt cộng bù ([onrepoints.xyz](https://www.onrepoints.xyz/)). API cũng ghi nhận những ngày tổng point giảm ròng, ví dụ **−3.76B ngày 15/09**, cho thấy OnRe có tính lại hoặc loại ví ở cấp tổng dù docs nói "never clawed back" ([points growth](https://rewards.api.onre.finance/api/v1/analytics/points/growth)). Point tập trung cao: ví lớn nhất nắm 8.1%, top 10 nắm 27.4%, top 100 nắm 52.3%, top 1,000 nắm 84.7%, còn ví trung vị chỉ có ~72k point. Theo nguồn, Kamino ONyc chiếm 29.6% tổng point, Loopscale ONyc 24.5%, và **YT Exponent 16.3%** ([OnRe leaderboard API](https://rewards.api.onre.finance/api/v1/points/leaderboard?page=0&size=1000)).

| Tổng point tại mốc | Giữ nguyên 1.3244B/ngày | Phát hành tăng 3%/tháng | Phát hành tăng 8%/tháng (bear) |
|---|---|---|---|
| 31/12/2026 | 364B | 370B | 380B |
| **10/01/2027 (YT đáo hạn)** | **377B** | 384B | 397B |
| 31/03/2027 | 483B | **506B** | 549B |
| 30/06/2027 | 604B | 656B | **764B** |
| 30/09/2027 | 726B | 823B | 1,038B |

*Công thức: P(n) = 240.9B + 1.3244B × ((1+r)^n − 1)/r, với r = (1+g)^(12/365) − 1 và n = số ngày từ 29/09/2026 (tính toán của báo cáo từ API chính thức).*

Chưa có tỷ lệ quy đổi point sang token nào. Con số "5% FDV cho point" lan truyền trên các trang tổng hợp thực chất chỉ là giá trị mặc định của thanh trượt trong máy tính cộng đồng onrepoints.xyz, không phải thông tin chính thức ([onrepoints.xyz](https://www.onrepoints.xyz/)). Về điều kiện tham gia, cổng Open Access không cần KYC. Tuy nhiên ONyc **loại trừ Mỹ, Anh, Hàn Quốc, Việt Nam và khoảng 60 khu vực khác** ([OnRe Docs](https://docs.onre.finance/legal/onyc-excluded-jurisdictions)), Open Access cũng chỉ "subject to jurisdictional restrictions" ([OnRe Docs](https://docs.onre.finance/for-capital-providers/open-access-vs-institutional-access)), và mint/redeem trực tiếp yêu cầu KYC qua Sumsub ([OnRe Docs](https://docs.onre.finance/legal/kyc-and-aml-policy)). Chưa có thông tin nào cho biết một đợt airdrop tương lai có loại các ví này hay không. Với người dùng ở Việt Nam, đây là rủi ro nhị phân và không thể đa dạng hóa.

## YT ONyc-10JAN27 trả ~$5.6 cho mỗi triệu point, kỳ vọng chỉ dương mỏng

### Thông số thị trường và câu hỏi 8x hay 5x

Exponent hiện là nơi duy nhất có YT ONyc, vì kỳ hạn cuối của RateX (ONyc-2609) đã đáo hạn ngày 29/09/2026 ([RateX](https://app.rate-x.io/)). Thị trường **ONyc-10JAN27** đáo hạn **10/01/2027 13:00 UTC**, còn **103.3 ngày**. Giá YT là **$0.032912** cho mỗi $1 vốn gốc (lúc 11:55 UTC là $0.03274), giá PT là 0.9671, và **implied APY 12.55%** so với lợi suất thực hiện 11.02% (7 ngày) và 11.36% (30 ngày). Thanh khoản CLMM ~$3.0M, tổng ONyc đã tách ~$20.3M. YT holder không nhận thêm phần thưởng token nào của Exponent ([Exponent markets API](https://app.exponent.finance/api/markets?include_frontend_hidden=true)). YT mua được toàn bộ yield của $1 gốc cho đến đáo hạn và về 0 khi đáo hạn ([Exponent Docs](https://docs.exponent.finance/user-documentation/yield-trading-explained)). YT đã rẻ đi đáng kể. Implied APY giảm từ 16.25% ngày 24/08 xuống 12.55%, nên giá trả cho mỗi YT-ngày giảm ~21%, từ $0.000401 xuống $0.000319 ([Exponent implied APY chart](https://app.exponent.finance/api/implied-apy-chart?vaultAddress=7f1PgxY3kGsPqLAKpwcduZkcBEhpjMz7U1iJ4pcCCzDy&timeframeSeconds=31536000)). Thị trường srONyc-10JAN27 (YT $0.0216, 4x, implied 8.04%) chỉ có ~$0.3M thanh khoản, và CLMM cạn ở khoảng $2.3k.

Biến số nhạy nhất của mô hình là hệ số nhân. Config trực tiếp của Exponent ghi `yt_multiplier: 8`, và giao diện hiển thị "earns 8x Onre Points per USD of exposure" ([Exponent points config](https://app.exponent.finance/api/points/config)). Docs OnRe vẫn ghi mức chung cho YT là 5x ([OnRe Docs](https://docs.onre.finance/onyc-in-defi/onre-points-program)), và OnRe gọi các boost kỳ hạn mới là "limited-time" ([OnRe review 08/2026](https://www.onre.finance/blog/onre-in-review-august-2026)). Có bằng chứng dữ liệu cho thấy hệ số cao hơn 5x đã thực sự được ghi có. Theo leaderboard, 878 ví nắm YT ONYC-JAN2027 đã nhận 4.24B point trong ~36 ngày ([OnRe leaderboard API](https://rewards.api.onre.finance/api/v1/points/leaderboard?page=0&size=1000)). Nếu chỉ ở 5x, lượng YT lưu hành bình quân phải là ~23.6M, lớn hơn cả quy mô thị trường hiện tại ($20.3M), điều không thể xảy ra khi thị trường lớn dần theo thời gian. Kết luận hợp lý là 8x hiện đang áp dụng, đây là mức sau khi boost 16x hết hạn ngày 21/09, và vẫn có thể bị hạ về 5x bất cứ lúc nào. Ngoài ra còn một điểm mơ hồ nữa: nếu OnRe tính point trên ONyc tương đương thay vì trên USD, số point giảm thêm 13% (chia cho NAV 1.1506). Báo cáo dùng 8x làm kịch bản chính và 5x làm kịch bản xấu.

### Yield chảy ngược kéo chi phí ròng xuống ~14% vốn

YT không phải khoản chi mất trắng. Người giữ YT nhận toàn bộ yield ONyc trên phần gốc danh nghĩa, trừ **phí 5.5%** của Exponent (tham số on-chain `interestBpsFee = 550`, đọc qua SDK chính thức ([npm](https://www.npmjs.com/package/@exponent-labs/exponent-sdk))). Yield được trả dưới dạng SY/wONyc và có thể claim dần. Ở APY 11.02%, mỗi YT nhận lại ~$0.02837, nên **chi phí ròng chỉ còn $0.00454 cho mỗi YT, tức 13.8% giá mua**. Trượt giá lấy từ mô phỏng on-chain trên CLMM ([Exponent CLMM API](https://app.exponent.finance/api/clmm)).

| Vé | Giá khớp TB | Trượt giá | Số YT | Yield về (APY 11.02%) | Chi phí ròng | Point đến đáo hạn (8x) | Hòa vốn 8x | Hòa vốn 5x |
|---|---|---|---|---|---|---|---|---|
| $1,000 | $0.03300 | +0.26% | 30,303 | $860 | **$140 (14.0%)** | 25.0M | **$5.60 / 1M pt** | **$8.96 / 1M pt** |
| $10,000 | $0.03356 | +1.97% | 297,974 | $8,454 | $1,546 (15.5%) | 246M | $6.28 | $10.05 |
| $50,000 | ~$0.0359 | ~+9.1% | ~1.39M | $39,514 | $10,486 (21.0%) | 1,151M | $9.11 | $14.58 |
| $1,000 nếu APY rơi về 10% | $0.03300 | +0.26% | 30,303 | $783 | $217 (21.7%) | 25.0M | $8.68 | $13.88 |

Mỗi $1 bỏ vào YT tạo ra **~242 point mỗi ngày** ở 8x (152 ở 5x). Con số này gấp ~280 lần giữ ONyc trơn (0.87 point/$/ngày) và gấp ~16–18 lần một vòng loop Kamino (~13–15 point/$ vốn chủ/ngày, ước tính từ hệ số 6x trên tài sản thế chấp gộp với đòn bẩy 2.5–2.9x). Một vé $1k sẽ tích ~25M point đến đáo hạn, tương đương hạng ~1,150 trên bảng xếp hạng hôm nay. Chi phí cơ hội của vốn thêm khoảng $18–31 cho mỗi $1k: $18 nếu claim yield đều đặn, $31 nếu để đến cuối kỳ. Yield trả bằng wONyc, nên người không KYC được phải thoát qua DEX; ONyc đang giao dịch thấp hơn NAV ~0.17% ([Jupiter price API](https://lite-api.jup.ag/price/v3?ids=5Y8NV33Vv7WbnLfq3zBcKSdYPrk7g2KoiQoe7M2tcxp5)).

### Công thức để tự chạy lại

```
Đầu vào (29/09/2026)                 Giá trị mặc định
P_fill  giá khớp YT ($/YT)           0.03300 (vé $1k) | 0.03356 ($10k) | 0.0359 ($50k)
D       số ngày tích point           103.28 (đến 10/01/2027) hoặc số ngày đến snapshot nếu sớm hơn
m       hệ số point YT               8 (config Exponent) | 5 (docs OnRe); nếu tính theo ONyc thì chia thêm 1.1506
APY     lợi suất ONyc                0.1102 (7 ngày) | 0.1136 (30 ngày) | 0.10 (bearish)
fee     phí yield Exponent           0.055
P0, d0  tổng point, phát hành/ngày   240.9e9 ; 1.3244e9
g       tăng trưởng phát hành/tháng  0 | 0.03 | 0.08
FDV, A  FDV lúc TGE, % cung cho point
h       chiết khấu hiện thực hóa     0.2–0.4 (giá giảm sau TGE, vesting)
e       xác suất được nhận airdrop   1.0 | 0.7 (rủi ro khu vực bị loại trừ)

(1) Số YT             N    = Vốn / P_fill
(2) Point nhận được   Pts  = N × m × D
(3) Yield chảy về     Y    = N × [(1 + APY)^(D/365) − 1] × (1 − fee)
(4) Chi phí ròng      C    = Vốn − Y
(5) Hòa vốn/point     BE   = C / Pts
(6) Tổng point snap   P_S  = P0 + d0 × ((1+r)^n − 1)/r ,  r = (1+g)^(12/365) − 1   (g = 0 → P0 + d0 × n)
(7) Giá trị/point     V    = FDV × A × (1 − h) / P_S
(8) Giá trị airdrop   V_air = Pts × V × e
(9) Lãi/lỗ            PnL  = V_air + Y − Vốn = V_air − C
(10) Kỳ vọng          EV   = Σ p_i × PnL_i
(11) FDV hòa vốn      FDV_BE = BE × P_S / (A × (1 − h))
```

### Bảng kịch bản: một nhánh thắng lớn, ba nhánh thua nhỏ

| Kịch bản (xác suất) | Snapshot | Tổng point P_S | FDV | A | h | $/1M point | Airdrop vé $1k (8x / 5x) | Lãi/lỗ vé $1k (8x / 5x) |
|---|---|---|---|---|---|---|---|---|
| Bull (10%) | 31/12/2026 | 364B | $350M | 7% | 20% | $53.8 | $1,210 / $757 | **+107% / +62%** |
| Base (35%) | 31/03/2027 | 506B | $200M | 5% | 30% | $13.8 | $346 / $216 | **+21% / +8%** |
| Bear (25%) | 30/06/2027 | 764B | $100M | 3% | 40% | $2.36 | $59 / $37 | **−8% / −10%** |
| Zero (30%) | không TGE / bị loại | — | — | — | — | $0 | $0 | **−14% / −14%** |
| **Kỳ vọng (EV)** | | | | | | | | **+11.7% / +2.0%** |

*Bull chỉ tính point đến 31/12/2026 (~92.7 ngày). Lãi/lỗ tính trên vốn bỏ ra trong 103 ngày, APY 11.02%, không tính chi phí cơ hội.*

Kỳ vọng rất nhạy với ba giả định không kiểm chứng được. Với vé $1k: ở 8x, APY 11.02% và chắc chắn đủ điều kiện, EV là **+11.7%**. Nhân xác suất đủ điều kiện 0.7 thì còn **+4.0%**. Chuyển sang 5x thì còn +2.0% (đủ điều kiện) hoặc **−2.8%** (xác suất 0.7). Nếu APY rơi về 10%, bốn con số tương ứng thành +4.0%, −3.7%, −5.7% và −10.5%. Vé $10k cho +9.8%, +2.2%, +0.3%, −4.4% ở APY 11.02%. Vé $50k chỉ còn +2.7% ở 8x và **−6.2% ở 5x**, vì trượt giá ~9% ăn hết lợi thế. Ngay kịch bản Base cũng đã bearish so với lịch sử. Quỹ $10M (trước chiết khấu) tương ứng ~$0.094 cho mỗi $1k TVL-ngày, tức ~3.4% APR tương đương, thấp hơn mọi chương trình trong nhóm so sánh ($0.18–0.67). Nếu OnRe trả ở mức trung vị lịch sử ($0.44/$1k-ngày), quỹ airdrop sẽ là ~$47M, tức ~$93 cho mỗi 1M point, và vé $1k nhận ~$2,300. Đó là phần đuôi phải có thật của khoản cược này, nhưng báo cáo không dùng nó làm kịch bản cơ sở.

**Độ nhạy: $ trên mỗi 1M point, trước chiết khấu h, với A = 5%** (A = 3% thì nhân 0.6, A = 7% thì nhân 1.4; sau đó nhân (1 − h) rồi so với mức hòa vốn $5.6 cho 8x hoặc $9.0 cho 5x):

| FDV \ P_S | 364B | 483B | 606B | 767B |
|---|---|---|---|---|
| $80M | 11.0 | 8.3 | 6.6 | 5.2 |
| $100M | 13.7 | 10.4 | 8.3 | 6.5 |
| $150M | 20.6 | 15.5 | 12.4 | 9.8 |
| $200M | 27.5 | 20.7 | 16.5 | 13.0 |
| $300M | 41.2 | 31.1 | 24.8 | 19.6 |
| $500M | 68.7 | 51.8 | 41.3 | 32.6 |

**FDV hòa vốn** (vé $1k, APY 11.02%, A = 5%, h = 30%):

| P_S | 364B | 483B | 606B | 767B |
|---|---|---|---|---|
| 8x | $58M | $77M | $97M | $123M |
| 5x | $93M | $124M | $155M | $196M |

Nếu dùng giả định khắt khe hơn (A = 3%, h = 40%), FDV hòa vốn tăng lên $113–239M ở 8x và $181–382M ở 5x. Giá YT hiện tại tự nó hàm ý thị trường chỉ định giá point OnRe ở **~$5.5 mỗi 1M point**. Với tham số Base, con số này tương đương FDV chỉ **~$60–80M**, thấp hơn mọi so sánh trừ Solstice sau khi đã sập. Nói cách khác, YT đang được định giá cho câu hỏi "có token hay không", chứ không phải "token lớn cỡ nào".

### Rủi ro có thể xóa sạch lợi thế

Rủi ro lớn nhất là **YT ngừng tích point ngày 10/01/2027, trong khi quỹ point vẫn tiếp tục phình đến snapshot**. Ở kịch bản Base, từ 377B lúc đáo hạn lên 506B lúc snapshot là thêm 129B point, làm giá trị point của YT giảm ~25%. Mỗi tháng TGE trễ sau đáo hạn lấy đi thêm ~8–10% giá trị. Kế đến là **hệ số**: hạ từ 8x về 5x cắt 37.5% số point, và điểm hòa vốn tăng từ $5.6 lên $9.0 mỗi 1M point. Thứ ba là **lạm phát point đang tăng tốc**, từ 0.68B/ngày lên 1.68B/ngày trong sáu tháng, và các đợt boost 10–16x vẫn thường xuyên được tung ra. Thứ tư là **thiết kế phân phối**. Re cho ví dưới 150M point nhận đủ ngay, còn ví lớn hơn phải vest theo điều kiện giữ TVL ([Re](https://re.xyz/insights/re-tge-launch)). Solstice chia tầng đến mức 99.68% người dùng chỉ nhận 0.49% quỹ. Một vé $1k với ~25M point nằm ở tầng giữa nên có thể được lợi hoặc bị thiệt tùy thiết kế. Trong khi đó 878 ví YT ONYC-JAN2027 đang có top 10 nắm 38% point của nhóm (tính từ [leaderboard API](https://rewards.api.onre.finance/api/v1/points/leaderboard?page=0&size=1000)).

Thứ năm là **điều kiện nhận airdrop**. Việt Nam nằm trong danh sách loại trừ của ONyc, và frontend của OnRe bật chặn địa lý. Người dùng nên đọc kỹ điều khoản và tự cân nhắc hệ quả pháp lý; báo cáo không khuyến nghị cách lách giới hạn khu vực. Thứ sáu là **thảm họa**. Mùa bão kéo dài đến 30/11, và các rủi ro toàn cầu khác (động đất, bão ở Nhật) vẫn còn. Nếu một cú sốc NAV cỡ Sandy (−13–22%) xảy ra sau ~50 ngày, YT gần như chắc chắn mất phần yield còn lại, vì NAV không kịp hồi trước đáo hạn. Khi đó vé $1k chỉ giữ ~$413 yield đã nhận và **lỗ ~59%**, trong khi token OnRe cũng sẽ bị định giá lại mạnh. Thứ bảy là **APY bị nén**: một năm ít bão thường làm giá tái tục tái bảo hiểm ngày 1/1 mềm đi, và APY giảm từ 11% xuống 10% đẩy chi phí ròng từ 14% lên 22%. Cuối cùng là rủi ro hợp đồng thông minh của Exponent v2 và multisig không timelock của OnRe.

### Quyết định: chỉ mua nhỏ, đặt lệnh limit, giữ tới đáo hạn

Câu trả lời là **có thể mua, nhưng chỉ như một vé quyền chọn nhỏ, và không nên mua lớn**. Điều kiện tiên quyết có ba. Thứ nhất, bạn chấp nhận mất 14–22% vốn nếu không có token, và tới ~60% nếu có thảm họa. Thứ hai, bạn tin xác suất có airdrop cho point từ ~55–60% trở lên. Thứ ba, bạn chấp nhận rủi ro điều khoản khu vực. Về quy mô, giữ mỗi vé ≤$10k để trượt giá dưới ~2%. Nên vào bằng lệnh `buyYT` limit trên Rate Order Book quanh implied APY 11.5–12%: vừa mua rẻ hơn, vừa có thể nhận phần thưởng maker trả bằng ONyc (~4,357 ONyc cho giai đoạn 23/09–23/10) ([Exponent orderbook emissions](https://app.exponent.finance/api/orderbook-emissions/campaigns)). Claim yield định kỳ. Không mua YT srONyc vì thanh khoản quá mỏng và hệ số chỉ 4x. Nếu config Exponent hạ về 5x, chỉ mua khi **YT ≤ ~$0.0312 (implied APY ≤ ~11.9%)**, vì ở mức đó chi phí trên mỗi point bằng mức hiện nay. Chỉ báo cần theo dõi gồm: API config point của Exponent (hệ số), API growth của OnRe (tốc độ phát hành), Polymarket, việc có kỳ hạn YT mới sau tháng 01/2027 kèm boost hay không (nếu có thì TGE nhiều khả năng còn muộn), Breakpoint, và các cơn bão đổ bộ. Nếu OnRe công bố tokenomics với ≥5% cho point và định hướng FDV ≥$150M trước đáo hạn, YT sẽ được định giá lại tăng; khi đó nên chốt một phần thay vì chờ đến 10/01.

## Kết luận

Phát hiện quan trọng nhất là thị trường YT đang định giá point OnRe ở mức tương đương FDV chỉ ~$60–80M, thấp hơn gần như mọi so sánh. Vì vậy YT không đắt nếu token thực sự ra đời. Điều đó biến khoản cược thành một câu hỏi nhị phân về **sự tồn tại của airdrop và quyền nhận nó**, chứ không phải về quy mô FDV. Với người chắc chắn đủ điều kiện và tin hệ số 8x còn giữ, đây là một quyền chọn rẻ có đuôi phải dày. Với người dùng ở khu vực bị loại trừ như Việt Nam, lợi thế đó gần như biến mất, và EV dao động quanh 0.

Điểm thứ hai ít được nhắc tới là **sự lệch thời gian giữa đáo hạn YT và snapshot**. Mỗi tháng OnRe trì hoãn sau 10/01/2027 làm giá trị point của YT giảm thêm ~8–10%. Các tín hiệu hiện có (Series A mới, Season 1 giữ 60 ngày, kỳ hạn Exponent năm 2027 kèm boost, Polymarket 14%) đều nghiêng về phía trì hoãn. Chiến lược hợp lý là giữ vị thế nhỏ, theo dõi sát hệ số và tốc độ phát hành point, và sẵn sàng chốt khi có tin tokenomics thay vì coi YT là khoản nắm giữ thụ động đến đáo hạn.
