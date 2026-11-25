# Báo cáo cá nhân — NguyenCongTu-2A202604008

## 1. Thông tin thành viên

- Họ tên: Nguyễn Công Tú
- MSSV: 2A202604008
- Email:
- Vai trong nhóm: **người kiểm số** (giữ vai này suốt buổi, CP1 đến CP5)

## 2. Phần việc phụ trách

- Tính tay độc lập từ hai file CSV các con số của nhiệm vụ A và B. Không dùng code của nhóm.
- Đối chiếu với kết quả `src/lab13.py`, ngưỡng lệch 2%.
- Điền `report/team/bang_chi_phi.md` (A1–A4, B1–B4).
- Đối chiếu D1 và điền `report/team/pilot_plan.yaml` (CP4).
- Viết phần E2 (rủi ro kinh tế) trong `report/team/chi_so.md`.
- Soát số liệu giữa các file hồ sơ cho thống nhất.
- Chạy lại `lab13.py` trên máy khác với máy viết code.

## 3. Đóng góp cụ thể

**CP1 · Nhiệm vụ A**
- Lập bảng tính tay `tinh_tay_cp1.md`: tổng các cột, cách tính từng khoản.
- Kết quả: chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu. Chi phí cả hệ thống là 5.865 đ/yêu cầu, bằng 0,49× của 12.000 đ [simulated].
- Đối chiếu với code: A1, A2, A3, A4 đều khớp, lệch 0%.
- Điền A1–A4 và các câu trả lời, ghi nhãn `simulated` cho mọi số giả lập.

**CP2 · Nhiệm vụ B**
- Lập bảng tính tay `tinh_tay_cp2.md` cho 9 kịch bản B1, cặp kịch bản B2, giới hạn chạy lại B3 và xem lại 100% B4.
- Tự kiểm tra cặp "giảm một nửa" và "gấp đôi": +5,6% → −2,8%, +40,7% → −20,3%, +51,8% → −25,9%.
- Kiểm tra tính cộng tuyến tính: cặp kịch bản +46,3% = 5,6% + 40,7%.
- Đối chiếu với code: khớp, lệch 0%. Tự phát hiện và sửa một lỗi làm tròn trong bảng tính tay (12.414 thành 12.415).
- Điền B1–B4, xếp hạng ba yếu tố (làm lại, xem lại, lương), viết câu B3, B4 không quá 3 dòng, có số.

**CP4 · Nhiệm vụ D**
- Đối chiếu D1 của code với tính tay: 1.251 · 3.103 · tối đa 1.000 · tối đa 300 · 859 với m ≥ 299, DE 6,96 · power 0,64 · tỉ lệ mở lại 4,25% và 3,97%. Tất cả khớp.
- Điền toàn bộ `pilot_plan.yaml`: chú thích D1, D2, đánh đổi, chia theo nhân viên 20 + 20, `mde` 0,06, luật dừng, rollback, `simulated_inputs`.
- Sửa theo góp ý của người soát:
  - tách hoàn tiền trùng thành luật dừng ngay;
  - các luật theo tỉ lệ chỉ tính khi mỗi nhóm có ≥ 200 yêu cầu;
  - thêm ngày bắt đầu và số tuần đo, khoảng 30,7 yêu cầu/người/ngày nên cần khoảng 10 ngày để đủ 299 yêu cầu/người.
- Phát hiện mâu thuẫn: phạm vi ghi "6 depot" nhưng 6 depot chạy thử chỉ có 20 `staff_id`, không đủ 20 cụm mỗi nhóm. Đã sửa thành cả 12 depot, đồng thời sửa mục 6 hồ sơ cho khớp với `pilot_plan.yaml`.

**CP5 · Nhiệm vụ E**
- Kiểm tra lại ba chỉ số E1 (82,83% · 27,12% · 4,25%) bằng cách tính riêng: khớp với `chi_so.md`.
- Viết 3 dòng E2 lấy số từ bảng độ nhạy: làm lại gấp đôi +51,8%; xem lại 100% ra 0,98× (1,03× nếu làm lại 15,3 phút); khối lượng giảm một nửa ra 0,48× [simulated].
- Soát toàn bộ `report/team` theo checklist nộp bài. Không còn ô `...` trong các file hồ sơ đã xong, `pilot_plan.yaml` không còn dấu `?`, không có từ cấm theo quy tắc 5.

## 4. Bằng chứng

| Commit | Nội dung |
|---|---|
| `4093514` | CP1: điền bảng A1–A4 và bảng tính tay đối chiếu |
| `2a9817a` | CP2: điền B1–B4 và bảng tính tay đối chiếu |
| `ebaddee` | CP4: điền `pilot_plan.yaml` (D1, D2, đánh đổi, luật dừng) |
| `f738e32` | CP4: đặt `decision_date` sau khi rollout xong |
| `29fdaaa` | CP4/CP5: sửa luật dừng theo góp ý, thêm lịch đo; viết E2 |
| `aeb0446` | CP4: thống nhất phạm vi cả 12 depot giữa `pilot_plan.yaml` và mục 6 hồ sơ |

File liên quan:
- `report/team/tinh_tay_cp1.md`, `report/team/tinh_tay_cp2.md`: bảng tính tay, có cột "Code" và "Lệch".
- `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`.
- Phần E2 trong `report/team/chi_so.md`.

Chạy trên máy khác: `cd src && python lab13.py` trên máy riêng, với môi trường cài mới từ `requirements.txt`. Code chạy hết, ba phép thử A1 in ĐẠT (1,20 · 1,25 · 1,25), phần E1 cũng in ĐẠT. `lab13.py` không có thay đổi sau lần chạy này.

## 5. Công cụ AI đã dùng

Claude Code: hỗ trợ viết script tính tay từ CSV, chạy `lab13.py` để đối chiếu và soạn nháp các bảng. Tự kiểm tra bằng cách so mọi số với bảng tính tay, kết quả `lab13.py` và số đối chiếu trong tài liệu hướng dẫn (lệch không quá 2%); YAML kiểm tra bằng `yaml.safe_load`.

## 6. Tự đánh giá

Hoàn thành vai kiểm số: mọi số A, B, D được tính độc lập và khớp với code. Cần cải thiện: tính D1 bằng tay sớm hơn và rà lịch đo kỹ hơn trước khi đặt ngày quyết định.
