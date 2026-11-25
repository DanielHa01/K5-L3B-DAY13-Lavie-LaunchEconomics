# Báo cáo nhóm

Nhóm Lavie tổng hợp cách làm, kết quả và đóng góp từ các file bài làm cùng lịch sử commit. Số liệu chi tiết nằm trong các hồ sơ được dẫn bên dưới.

## 1. Thông tin nhóm

- Tên nhóm: Lavie
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Nhóm thực hiện bài lab để tính chi phí thật cho mỗi yêu cầu được trợ lý giải quyết, nhận diện lỗi và lập kế hoạch pilot có thể dùng để ra quyết định. Nhóm dùng hai file CSV của đề, chia phần viết code, kiểm số, gắn nhãn và giữ hồ sơ. Phần code có dùng Codex hỗ trợ; kết quả được đối chiếu với cách tính tay và hướng dẫn của lab trước khi đưa vào hồ sơ. Lab chạy offline, không gọi model thật và không dùng API key.

## 3. Giải pháp

- **A — Chi phí:** viết ba hàm A1 và mô hình cộng chi phí token, tool, xem lại, làm lại. Nhóm tính mọi lần chạy kể cả lần lỗi, nhưng chỉ chia cho số yêu cầu thành công; sau đó tách theo loại và cộng chi phí cố định. Kết quả ở [bảng chi phí](bang_chi_phi.md), đối chiếu tại [tính tay CP1](tinh_tay_cp1.md).
- **B — Độ nhạy:** chạy chín kịch bản đổi từng yếu tố, một kịch bản đổi một cặp, so sánh giới hạn chạy lại và trường hợp xem lại 100%. Nhóm kiểm tra cả chi phí nhân viên làm thay các yêu cầu không thành công. Bằng chứng ở [tính tay CP2](tinh_tay_cp2.md) và bảng chi phí.
- **C — Bảng lỗi:** hai người gắn nhãn độc lập 20 ca, so nhãn và thống nhất ca khác nhau theo nguyên nhân gốc. Nhóm chọn năm ca thuộc năm loại lỗi để đề xuất cách phát hiện, khắc phục và vai trò phụ trách trong [bảng lỗi](bang_loi.md).
- **D — Pilot:** tính cỡ mẫu trước khi chọn cách chia. Nhóm chọn chia ngẫu nhiên theo nhân viên, có đối chứng cùng thời gian, ghi rõ đánh đổi và bốn luật dừng trong [kế hoạch pilot](pilot_plan.yaml). Phạm vi cuối cùng là noi_dia và hang_nang ở cả 12 depot.
- **E — Hồ sơ launch:** tính ba chỉ số cho toàn mẫu và phạm vi pilot, đề xuất thêm hai chỉ số, đặc tả 10 event có `trace_id` và ba rủi ro kinh tế trong [chỉ số](chi_so.md). Nhóm ghép kết quả A–D thành bảy mục của [hồ sơ launch v0](ho_so_launch_v0.md), đồng thời chuẩn bị câu hỏi về chi phí, cỡ mẫu và an toàn trong [phiếu chấm](phieu_cham.md).

## 4. Kết quả

Chương trình chạy hết, ba phép thử A1 đạt và phần E1 khớp số đối chiếu. Kế hoạch YAML đọc được, có bốn luật dừng. Kết quả chính của nhóm:

- Chi phí mỗi việc thành công toàn mẫu là **4.472 đ**, gấp **16,3 lần** hóa đơn token và tool chia số yêu cầu [simulated]. Trong phạm vi pilot, chi phí có cố định là **4.599 đ/việc** ở 45.000 yêu cầu/tháng, bằng **0,38 lần** mức 12.000 đ của nhân viên tự làm [simulated].
- Làm lại gấp đôi làm chi phí tăng **51,8%**; xem lại gấp đôi làm tăng **40,7%** [simulated]. Hai người gắn nhãn đồng thuận **19/20 ca = 95%**, vượt mức 80% của đề.
- Ba chỉ số chính, dùng và an toàn toàn mẫu lần lượt là **82,83% · 27,12% · 4,25%**. Trong phạm vi pilot, kết quả tương ứng là **92,26% · 21,09% · 3,97%**. Đây là số từ dữ liệu lab giả lập, chưa chứng minh tác động của trợ lý.
- Thiết kế pilot có **20 nhân viên mỗi nhóm**, ít nhất **299 yêu cầu/người**, đạt khoảng **859,20 yêu cầu hiệu dụng mỗi nhóm** cho chênh 6 điểm. Nếu tác động thật chỉ 5 điểm, power còn khoảng **64%**.

Nhóm đề xuất **Go có điều kiện**: chỉ bắt đầu khi đủ nhân viên, event và thử được cách tắt trợ lý; đo phút thật và đạt điều kiện xem lại, an toàn trước khi tăng bước. Ngày quyết định là **12/01/2027**, sau cửa sổ chờ mở lại 7 ngày. Repo chưa có kết quả hội đồng chấm Lavie; phiếu nhóm lập để chấm nhóm khác không được dùng làm điểm nhóm mình nhận.

## 5. Khó khăn và cách xử lý

Khó nhất là phân biệt chi phí mỗi việc thành công với chi phí cả hệ thống. Nhóm cộng thêm chi phí nhân viên làm thay khi so giới hạn chạy lại; kết quả cho thấy hai lần chạy rẻ nhất cho cả hệ thống, dù một lần cho chi phí mỗi việc thành công thấp nhất [simulated]. Với ca lỗi 9, nhóm thống nhất nhãn Do người dùng vì nguyên nhân là khách nhập sai loại mã, không gắn theo chỗ trợ lý cần sửa.

Ở phần pilot, 20 nhân viên mỗi nhóm không đủ cho chênh 5 điểm dù tăng số yêu cầu. Nhóm chuyển sang chênh 6 điểm và ghi rõ giới hạn power. Qua các commit `29fdaaa`, `aeb0446`, `a4767ed`, nhóm bổ sung điều kiện đủ mẫu cho luật dừng, thống nhất phạm vi 12 depot và dời ngày quyết định sau khi đo xong cùng thời gian chờ mở lại.

## 6. Tổng hợp đóng góp

- **Hà Phan Đại Dương:** phụ trách code CP1, CP2, CP4, CP5 và cập nhật báo cáo cá nhân, phiếu chấm. Bằng chứng: `f97d039`, `f83fe05`, `d475d1c`, `2fe043c`, `ccb4f62`, `d8285ab`.
- **Nguyễn Công Tú:** điền bảng chi phí, tính tay đối chiếu CP1–CP2, lập và sửa kế hoạch pilot, bổ sung rủi ro E2. Bằng chứng: `4093514`, `2a9817a`, `ebaddee`, `29fdaaa`, `aeb0446`.
- **Hoàng Xuân Lĩnh:** gắn nhãn độc lập người 1, tổng hợp đồng thuận và quy tắc ca 9; viết E1, 10 event và cập nhật mục lỗi trong hồ sơ. Bằng chứng: `401be1e`, `a21931a`, `d569b39`.
- **Nguyễn Quang Thành:** gắn nhãn độc lập người 2, viết bảng khắc phục năm ca và điền dần hồ sơ launch, gồm rủi ro và đề xuất cuối. Bằng chứng: `5a55d58`, `545765a`, `614993f`, `d1b1ac0`, `7c6f6c2`, `64fc721`, `a4767ed`.

## 7. Hạn chế và hướng cải thiện

Đợt chạy thử chưa có đối chứng nên nhóm chưa thể nói trợ lý đã làm tăng chỉ số. Khi chia theo nhân viên vẫn có nguy cơ chia sẻ câu trả lời trong depot, cần kiểm soát quyền truy cập và log theo tài khoản. Nếu pilot không thấy khác biệt, nhóm cần xem lại cỡ mẫu và power trước khi kết luận. Qua bài làm, nhóm thấy cần theo dõi giờ nhân viên và lỗi ngầm bên cạnh hóa đơn token.

## 8. Tài liệu tham khảo

- [Hướng dẫn chi tiết buổi chiều](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md) và [dữ liệu, công thức](../../docs/du_lieu_va_cong_thuc.md).
- [Checkpoints](../../CHECKPOINTS.md), [quy tắc lab](../../RULES.md) và [thông tin nhóm](../../TEAM.md).
- [Code bài làm](../../src/lab13.py), `logix_requests.csv`, `logix_runs.csv` trong `src/`; các hồ sơ đã dẫn ở trên và lịch sử commit của repo nhóm.
