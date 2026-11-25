# Báo cáo cá nhân — NguyenQuangThanh-2A202604085

## 1. Thông tin thành viên

- Họ tên: Nguyễn Quang Thành
- MSSV: 2A202604085
- Email:
- Vai trong nhóm: **người gắn nhãn 2 kiêm giữ hồ sơ**

## 2. Phần việc phụ trách

- Gắn nhãn 20 ca lỗi với vai người gắn nhãn 2 và viết bảng khắc phục 5 ca trong `bang_loi.md` (CP3).
- Giữ hồ sơ `ho_so_launch_v0.md`: điền mục 1, 2, 3, 4, 6, 7 và đề xuất cuối từ CP1 đến CP5. Mục 5 do Hoàng Xuân Lĩnh điền; mục 6 sau đó được Nguyễn Công Tú sửa phạm vi cho khớp với `pilot_plan.yaml`.
- Dời ngày quyết định trong `pilot_plan.yaml` cho khớp với thời gian chờ đo mở lại.

## 3. Đóng góp cụ thể

**CP1, CP2 · Hồ sơ mục 1, 2, 3**
- Mục 1: 4.472 đ/việc thành công, gấp 16,3 lần hoá đơn 274,7 đ mỗi yêu cầu; phạm vi `noi_dia` + `hang_nang` có cố định là 4.599 đ ở 45.000 yêu cầu/tháng [simulated].
- Mục 2: ba yếu tố nhạy nhất là làm lại ×2 (+51,8%), xem lại ×2 (+40,7%), lương +25% (+23,1%); giá token ×2 chỉ +5,6% [simulated].
- Mục 3: so bằng chi phí cả hệ thống, có cộng 222 ca không thành công: (4.373.585 + 222 × 12.000) ÷ 1.200 = 5.865 đ, bằng 0,49× mức 12.000 đ. Ghi kèm số bất lợi: `quoc_te` 1,88× và `doi_tac` 0,85× [simulated].

**CP3 · Nhãn và bảng khắc phục**
- Điền nhãn người 2 cho 20 ca. So với người 1 trùng 19/20 = 95%. Ca lệch duy nhất là ca 9: tôi gắn Do người dùng, người 1 gắn Ngữ cảnh; nhóm thống nhất Do người dùng vì nguyên nhân gốc là khách nhập nhầm loại mã.
- Viết bảng khắc phục 5 ca, mỗi loại một ca (14, 7, 3, 4, 17), mỗi dòng có event, ngưỡng, tần suất và một vai trò phụ trách.
- Ca 17 (Ngầm): mẫu 100 đơn/tuần chỉ bắt được lỗi với xác suất khoảng 79% (1 − (1 − 1,6%)^100, với giả định 212 đơn trong 9 ngày ở 1.500 yêu cầu/ngày). Vì vậy đề xuất lấy mẫu thêm sau mỗi lần đổi bảng giá.

**CP4, CP5 · Hồ sơ mục 4, 6, 7 và đề xuất**
- Mục 4: ghi ba chỉ số 82,83% · 27,12% · 4,25%, nói rõ không có đối chứng nên chưa kết luận được tác động.
- Mục 6: tóm tắt pilot 20 cụm mỗi nhóm, 20 × 299 = 5.980 yêu cầu mỗi nhóm, DE 6,96; nêu số bất lợi là power chỉ 0,64 nếu tác động thật là 5 điểm.
- Mục 7: ba rủi ro kinh tế. Cộng thêm cố định 1.185 đ vào kịch bản xem lại 100%: 11.743 + 1.185 = 12.928 đ, bằng 1,08×, tức đắt hơn nhân viên tự làm [simulated].
- Dời `decision_date` từ 05/01/2027 sang 12/01/2027: đợt đo kết thúc 03/01, yêu cầu cuối cần đủ 7 ngày chờ mở lại (đến 10/01) mới tính được chỉ số chính và chỉ số an toàn.
- Viết đề xuất **Go có điều kiện** với 5 điều kiện, mỗi điều kiện có vai trò phụ trách và ngày kiểm tra.

## 4. Bằng chứng

| Commit | Nội dung |
|---|---|
| `614993f` | CP1: điền mục 1 và 3 hồ sơ |
| `d1b1ac0` | CP2: điền mục 2 hồ sơ |
| `5a55d58` | CP3: điền nhãn người 2 cho 20 ca |
| `545765a` | CP3: bảng khắc phục 5 ca, mỗi loại một ca |
| `7c6f6c2` | CP5: điền mục 4 hồ sơ |
| `64fc721` | CP4: điền mục 6 hồ sơ |
| `a4767ed` | CP5: điền mục 7 và đề xuất; dời ngày quyết định trong hồ sơ và `pilot_plan.yaml` |

File: `report/team/ho_so_launch_v0.md`, cột "Nhãn người 2" và bảng khắc phục trong `report/team/bang_loi.md`, `decision_date` trong `report/team/pilot_plan.yaml`.

## 5. Công cụ AI đã dùng

Dùng Claude Code hỗ trợ trong cả bảy commit ở mục 4 (đều ghi `Co-Authored-By: Claude`), gồm cả commit điền nhãn CP3, và soạn báo cáo này từ lịch sử commit và các file của nhóm.

Kiểm tra lại khi viết báo cáo: chạy lại `lab13.py` với `.venv` trên máy tôi, code chạy hết, A1 và E1 in ĐẠT; so các số chi phí, độ nhạy, cỡ mẫu và chỉ số nêu ở mục 3 với kết quả in ra; `pilot_plan.yaml` đọc được bằng `yaml.safe_load`, không còn dấu `?` ngoài chú thích; tìm từ cấm theo quy tắc 5 trong `report/team` không thấy.

## 6. Tự đánh giá

Hoàn thành phần được giao: 20 nhãn, bảng khắc phục đủ năm loại và hồ sơ đủ bảy mục cùng đề xuất. Điểm tôi rút ra là hồ sơ phải ghi cả số bất lợi: cùng một trợ lý, 0,38× ở mức xem lại hiện tại nhưng thành 1,08× nếu xem lại 100% có cộng cố định [simulated], nên đề xuất phải kèm điều kiện đo phút xem lại thật.

Hạn chế: các ngưỡng phát hiện trong bảng khắc phục là đề xuất ban đầu, chưa có số nền; phút xem lại và làm lại vẫn là số giả lập. Cần cải thiện: ngày quyết định phải sửa ở CP5 vì trước đó chưa tính thời gian chờ 7 ngày của chỉ số mở lại; lần sau cần đối chiếu lịch đo với định nghĩa chỉ số ngay khi lập kế hoạch.
