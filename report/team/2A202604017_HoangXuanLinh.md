# Báo cáo cá nhân — HoangXuanLinh-2A202604017

## 1. Thông tin thành viên

- Họ tên: Hoàng Xuân Lĩnh
- MSSV: 2A202604017
- Email: 26ai.linhhx@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 1

## 2. Phần việc phụ trách

- Đọc đề, theo dõi điều kiện "Xong khi" của CP1–CP5 cho cả nhóm.
- Soát code CP1 (`src/lab13.py`) và đối chiếu số A2, A3, A4.
- CP3: gắn nhãn độc lập 20 ca lỗi (bộ nhãn người 1), tính tỉ lệ đồng thuận, soát bảng khắc phục.
- CP5: `report/team/chi_so.md` phần E1 (đặc tả chỉ số), danh sách event, kiểm tra chéo chỉ số – event.
- Duyệt chéo Gate 2a: kiểm tra `report/team/phieu_cham.md`, soi tiêu chí số giả lập và phạm vi (C7).

## 3. Đóng góp cụ thể

- Soát commit `f97d039 CP1 code`: xác nhận đọc CSV có `keep_default_na=False`, tử số tính đủ 1.624 lần chạy (kể cả 572 lần `loi`), mẫu số là 978 việc thành công, chia 1.000 trước khi nhân giá token. Tính lại độc lập: token 245.585 đ, tool 84.000 đ, 890 phút xem lại và 1.132 phút làm lại [simulated], khớp code.
- Soát commit `f83fe05 CP2 code` trước khi người kiểm số điền bảng: chạy lại code, xác nhận "giảm một nửa" bằng đúng nửa mức tăng của "gấp đôi" ở cả ba yếu tố (token +5,6% / −2,8%; xem lại +40,7% / −20,3%; làm lại +51,8% / −25,9%) [simulated].
- Tính tỉ lệ ok theo lần chạy × loại để trả lời "chạy lại có giúp không" (quoc_te: 30,0% → 11,4% → 2,2%).
- E1: tính thử ba chỉ số trên 1.200 yêu cầu: chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 7 ngày 4,25% (51/1.200); thêm số trong phạm vi `noi_dia` + `hang_nang` (92,26% · 21,09% · 3,97%) cho luật dừng của pilot.
- Đề xuất thêm một chỉ số dùng (tỉ lệ yêu cầu nhóm trợ lý được xử lý qua trợ lý) và một chỉ số an toàn (tỉ lệ đơn hoàn lệch tiền qua kiểm tra mẫu 100 đơn/tuần).
- Viết danh sách 10 event có `trace_id` và phần kiểm tra chéo: cả năm chỉ số đều tính được từ event.
- CP3: gắn nhãn người 1 cho 20 ca; đồng thuận với người gắn nhãn 2 là 19/20 = 95%; ca lệch duy nhất là ca 9 (Ngữ cảnh / Do người dùng), thống nhất Do người dùng theo nguyên tắc nguyên nhân gốc, viết câu quy tắc trong `bang_loi.md`. Soát bảng khắc phục 5 ca của người gắn nhãn 2 (đủ năm loại, event + ngưỡng + tần suất, một vai trò); điền mục 5 hồ sơ (`d569b39`).
- CP4: soát `pilot_plan.yaml` (safe_load OK, hết dấu `?`, đủ NẾU – TRONG – THÌ – KHÔNG THÌ); góp ý 3 chỗ đã được sửa ở `29fdaaa`: tách luật hoàn tiền trùng thành dừng ngay, thêm điều kiện ≥ 200 yêu cầu mỗi nhóm để bước 10% không dừng oan, thêm lịch đo đủ 299 yêu cầu/người trước ngày quyết định. Phát hiện phạm vi ghi "6 depot" mâu thuẫn với 20 + 20 nhân viên (dữ liệu 6 depot chỉ có 20 `staff_id`); nhóm sửa thành cả 12 depot ở `aeb0446`.
- CP5: soát E2 (3 rủi ro, số khớp B1, B4, A4; tỉ lệ làm lại trong phạm vi 48/982 = 4,9% khớp dữ liệu).
- CP5: đối chiếu code E1 của người kiểm số (`2fe043c`): cả 6 số (toàn mẫu và phạm vi) khớp số tôi đã tính trong `chi_so.md`; `lab13.py` chạy hết từ đầu tới cuối, in ĐẠT.
- CP5: soát hồ sơ chốt (`a4767ed`): đủ 7 mục, mỗi mục có số + trạng thái + vai trò; đề xuất Go có điều kiện nêu đủ số bất lợi (xem lại 100% 0,98×–1,08×, power 0,64, mở lại 3,97%); ngày quyết định 12/01/2027 khớp giữa hồ sơ và `pilot_plan.yaml`.

## 4. Bằng chứng

- File: `report/team/chi_so.md` (E1, danh sách event, kiểm tra chéo).
- File: `report/team/bang_loi.md` (cột nhãn người 1, tỉ lệ đồng thuận, quy tắc ca 9).
- File: `report/team/ho_so_launch_v0.md` (mục 5).
- File: `report/team/phieu_cham.md` (soát tiêu chí số giả lập và phạm vi).
- Commit: `a21931a CP5: E1 chỉ số + 10 event + kiểm tra chéo`; `401be1e CP3: nhãn độc lập người 1, đồng thuận 19/20 (95%), thống nhất ca 9`; `d569b39 CP3: điền mục 5 hồ sơ`.
- Góp ý đã được nhóm sửa: `29fdaaa` (luật dừng, lịch đo), `aeb0446` (phạm vi 12 depot).

## 5. Công cụ AI đã dùng

- **Claude Code (trong VS Code):** đọc toàn bộ repo để lập bảng phân công và danh sách việc; chạy `lab13.py` và một đoạn pandas độc lập để đối chiếu số CP1; tính thử ba chỉ số E1; gợi ý bản nháp danh sách event và chỉ số tự đề xuất; hỗ trợ soát `pilot_plan.yaml` (chạy `yaml.safe_load`, tìm dấu `?`, đối chiếu số depot/nhân viên với `logix_requests.csv`) và soát hồ sơ; ghép hai bộ nhãn và tính tỉ lệ đồng thuận.
- **Cách tự kiểm tra:** so số E1 với công thức trong đề và với code của người kiểm số; số CP1 so với bảng tính tay `report/team/tinh_tay_cp1.md` (lệch 0%); thiết kế pilot (D1) so với slide chữa của giảng viên; tự đọc lại từng event để chắc mỗi chỉ số có event tính được.

## 6. Tự đánh giá

- Làm tốt: phần E1 xong sớm và khớp code của người kiểm số ở cả 6 số; phát hiện mâu thuẫn "6 depot" và ba lỗ hổng luật dừng trước khi gửi hội đồng, nhóm đã sửa.
- Điều tự giải thích được: tử số tính mọi lần chạy vì lần lỗi vẫn tốn token và tool, mẫu số chỉ đếm 978 việc thành công vì đó mới là sản phẩm; chia theo 20 nhân viên mỗi nhóm có DE = 1 + (m − 1) × 0,02 nên cỡ mẫu hiệu dụng không vượt 20 ÷ 0,02 = 1.000; đề xuất Go có điều kiện vì phạm vi 0,38× nhưng xem lại 100% lên 0,98×–1,08× và power chỉ 0,64.
