# Team

## Thông tin nhóm

- Tên nhóm: Lavie
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Lavie-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/DanielHa01/K5-L3B-DAY13-Lavie-LaunchEconomics, main, 

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 |    Hà Phan Đại Dương    |   2A202604119   |       |    DanielHa01    |    Trưởng nhóm, Người viết code    |
|   2 |    Nguyễn Công Tú    |   2A202604008   |       |    nguyencongtu4800    |    Người kiểm số     |
|   3 |    Hoàng Xuân Lĩnh    |   2A202604017    |   26ai.linhhx@vinuni.edu.vn    |    hxlinh    |     Người gắn nhãn 1    |
|   4 |    Nguyễn Quang Thành    |   2A202604085   |       |    quangthanhttbn1-bot    |    Người gắn nhãn 2     |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-

## NguyenCongTu-2A202604008

### Phần việc phụ trách

- Người kiểm số suốt buổi (CP1–CP5): tính tay độc lập từ CSV, đối chiếu với `src/lab13.py`, điền và soát số trong hồ sơ.
- Điền `report/team/bang_chi_phi.md` (A1–A4, B1–B4) và `report/team/pilot_plan.yaml`; viết E2 trong `report/team/chi_so.md`.

### Đóng góp cụ thể

- CP1–CP2: bảng tính tay A và B, khớp code, lệch 0% (chi phí mỗi việc thành công 4.472 đ [simulated]; xếp hạng làm lại > xem lại > lương).
- CP4: đối chiếu D1, điền `pilot_plan.yaml` (chia theo nhân viên 20 + 20, 859/nhóm, DE 6,96, 4 luật dừng); sửa phạm vi thành cả 12 depot cho khớp mục 6 hồ sơ.
- CP5: kiểm tra E1 (82,83% · 27,12% · 4,25%), viết 3 dòng rủi ro kinh tế E2.
- Chạy lại `lab13.py` trên máy khác máy viết code: chạy hết, ba phép thử A1 ĐẠT.

### Bằng chứng

- Commit: `4093514`, `2a9817a`, `ebaddee`, `f738e32`, `29fdaaa`, `aeb0446`, `b9edf43`.
- File: `report/team/tinh_tay_cp1.md`, `report/team/tinh_tay_cp2.md`, `report/team/2A202604008_NguyenCongTu.md`.

## HoangXuanLinh-2A202604017

### Phần việc phụ trách

- Người gắn nhãn 1: đọc đề, theo dõi điều kiện "Xong khi" của CP1–CP5 cho cả nhóm.
- CP3: gắn nhãn độc lập 20 ca lỗi (bộ nhãn người 1), tính đồng thuận, thống nhất ca lệch, soát bảng khắc phục, điền mục 5 hồ sơ.
- CP5: viết `report/team/chi_so.md` phần E1 (đặc tả chỉ số), danh sách event và kiểm tra chéo.
- Soát số và kế hoạch của nhóm ở CP1, CP2, CP4, CP5.

### Đóng góp cụ thể

- CP1: soát `src/lab13.py` (đọc CSV có `keep_default_na=False`, tử số tính đủ 1.624 lần chạy kể cả lần lỗi, mẫu số 978 việc thành công, chia 1.000 trước khi nhân giá); tính lại độc lập, khớp code.
- CP2: kiểm "giảm một nửa = nửa mức tăng của gấp đôi" ở cả ba yếu tố (token +5,6% / −2,8%; xem lại +40,7% / −20,3%; làm lại +51,8% / −25,9%) [simulated].
- CP3: đồng thuận 19/20 = 95% với người gắn nhãn 2; ca 9 thống nhất Do người dùng, viết câu quy tắc; soát bảng khắc phục 5 ca; điền mục 5 hồ sơ.
- CP4: soát `pilot_plan.yaml`, góp ý 3 chỗ trong luật dừng (tách luật hoàn tiền trùng, thêm ngưỡng ≥ 200 yêu cầu mỗi nhóm, thêm lịch đo); phát hiện phạm vi "6 depot" mâu thuẫn với 20 + 20 nhân viên, nhóm sửa thành cả 12 depot.
- CP5: tính thử ba chỉ số E1 (82,83% · 27,12% · 4,25%; trong phạm vi 92,26% · 21,09% · 3,97%), đề xuất thêm một chỉ số dùng và một chỉ số an toàn, viết 10 event có `trace_id`; đối chiếu code E1 của người kiểm số, khớp cả 6 số; soát E2 và hồ sơ chốt đủ 7 mục.
- Soạn slide thuyết trình Gate 2a (`docs/slide-lavie-gate2a.html`).

### Bằng chứng

- File: `report/team/chi_so.md`, `report/team/bang_loi.md`, `report/team/ho_so_launch_v0.md` (mục 5), `report/team/2A202604017_HoangXuanLinh.md`.
- Commit: `a21931a` (E1 + event + kiểm tra chéo), `401be1e` (nhãn người 1, đồng thuận 95%), `d569b39` (mục 5 hồ sơ).
- Góp ý được nhóm sửa: `29fdaaa` (luật dừng, lịch đo), `aeb0446` (phạm vi 12 depot).
