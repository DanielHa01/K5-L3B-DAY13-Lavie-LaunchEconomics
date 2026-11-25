# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Lavie · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu 1.200 yêu cầu: **4.472 đ** [simulated], gấp 16,3 lần hoá đơn token + tool mỗi yêu cầu (274,7 đ); chưa cộng cố định. Phạm vi `noi_dia` + `hang_nang`: 3.414 đ; cộng cố định 40 triệu đ/tháng thành **4.599 đ** ở 45.000 yêu cầu/tháng, 5.784 đ ở 22.500 [simulated]. | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | So với gốc 4.472 đ [simulated]: **1. Số ca làm lại** ×2: +51,8% (6.787 đ) · **2. Tỉ lệ xem lại** ×2: +40,7% (6.292 đ) · **3. Lương nhân viên** +25%: +23,1% (5.506 đ) [simulated]. Giá token ×2 chỉ +5,6% [simulated], nên pilot ưu tiên theo dõi tỉ lệ làm lại và tỉ lệ xem lại. | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống: (4.373.585 + 222 × 12.000) ÷ 1.200 = **5.865 đ/yêu cầu = 0,49×** của 12.000 đ [simulated], đã cộng 222 ca không thành công, chưa cộng cố định. Bất lợi: `quoc_te` 1,88× và `doi_tac` 0,85× theo chi phí mỗi việc thành công, nên để ngoài pilot [simulated]. | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử 1.200 yêu cầu (trong ngoặc: phạm vi `noi_dia` + `hang_nang`, 982 yêu cầu): **chính** đóng trong 24 giờ và không mở lại trong 7 ngày là **82,83%** (92,26%) · **dùng** bỏ qua gợi ý 48/177 = **27,12%** (21,09%) · **an toàn** mở lại trong 7 ngày **4,25%** (3,97%). Không có nhóm đối chứng nên chưa kết luận được tác động so với mức 70%. Thêm hai chỉ số tự đề xuất, chưa có số đo: tỉ lệ yêu cầu xử lý qua trợ lý, tỉ lệ đơn lệch tiền qua kiểm tra mẫu. Công thức và 10 event có `trace_id` ở `chi_so.md`. | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | Hai người gắn nhãn độc lập 20 ca, đồng thuận **19/20 = 95%** (≥ 80%); ca lệch duy nhất (ca 9) thống nhất Do người dùng. Phân bố: Do người dùng 4 · Hệ thống 5 · Ngữ cảnh 4 · Giới hạn hệ thống 4 · Ngầm 3. Bảng khắc phục 5 ca đủ năm loại, mỗi dòng có event + ngưỡng + tần suất và một vai trò. Lỗi nặng nhất là Ngầm (ca 17: 212 đơn lệch tiền trong 9 ngày, không ai mở lại), chỉ bắt được qua `audit_sample_checked` 100 đơn/tuần, xác suất bắt được trong một tuần khoảng 79%. Ngưỡng phát hiện là đề xuất ban đầu, chưa có số nền. | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | ... | ... | ... |
| 7 · Rủi ro kinh tế | ... | ... | ... |

**Đề xuất:** Go · Go có điều kiện · No-go (giữ một). Go có điều kiện: ghi từng điều kiện, người phụ trách, ngày kiểm tra. No-go: ghi việc phải làm để quay lại cổng.

- ...
