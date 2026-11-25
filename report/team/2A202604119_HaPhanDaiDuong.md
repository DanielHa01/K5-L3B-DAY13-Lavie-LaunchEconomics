# Báo cáo cá nhân — Hà Phan Đại Dương — 2A202604119

## 1. Thông tin thành viên

- Họ tên: Hà Phan Đại Dương
- MSSV: 2A202604119
- Email:
- Vai trong nhóm: Trưởng nhóm, người viết code

## 2. Phần việc phụ trách

Phụ trách phần lập trình trong `src/lab13.py` cho CP1, CP2, CP4 và CP5. Công việc gồm tính chi phí từ hai file CSV, chạy các kịch bản độ nhạy, tính cỡ mẫu cho pilot và tính ba chỉ số của đợt chạy thử. Dùng Codex hỗ trợ triển khai code theo yêu cầu từng checkpoint, kết quả được in ra màn hình để đối chiếu với tài liệu và làm cơ sở cho hồ sơ nhóm.

## 3. Đóng góp cụ thể

CP1: triển khai ba hàm về số lần chạy kỳ vọng, tỉ lệ thành công và hệ số chi phí. Tiếp theo là hàm `mo_hinh` để cộng chi phí token, tool, xem lại và làm lại. Phần này tính cả các lần chạy lỗi nhưng chỉ chia cho số yêu cầu có `ket_qua == 'thanh_cong'`. Bổ sung bảng theo từng loại yêu cầu và phần chi phí cố định 40 triệu đồng/tháng cho phạm vi `noi_dia` + `hang_nang`.

CP2: dùng lại `mo_hinh` để tính chín kịch bản thay đổi từng yếu tố, một kịch bản thay đổi đồng thời giá token và mức xem lại, rồi xếp hạng các yếu tố ảnh hưởng. Bổ sung so sánh giới hạn một, hai, ba lần chạy, có cộng chi phí nhân viên làm thay các yêu cầu không thành công. Với kịch bản xem lại 100%, code tính cả hai giả định thời gian làm lại là 9 phút và 15,3 phút/ca.

CP4: bổ sung năm phép tính cỡ mẫu D1, gồm chia theo yêu cầu, theo nhân viên, theo depot và trường hợp chấp nhận mức chênh 6 điểm phần trăm. Code còn tính power khi tác động thật chỉ đạt 5 điểm phần trăm, cùng tỉ lệ mở lại trong 7 ngày của toàn mẫu và phạm vi pilot.

CP5: viết thêm phần E1 trong `src/lab13.py` để tính tỉ lệ đóng yêu cầu trong 24 giờ và không mở lại trong 7 ngày, tỉ lệ sửa hoặc bỏ gợi ý, cùng tỉ lệ mở lại trong 7 ngày. Code in cả số lượng và tỉ lệ cho toàn bộ dữ liệu và riêng phạm vi `noi_dia` + `hang_nang` để nhóm dễ đối chiếu. Với tỉ lệ sửa hoặc bỏ gợi ý, chỉ chia cho số yêu cầu được xem lại (`duoc_xem_lai == 1`), không chia cho toàn bộ yêu cầu. Bổ sung phép kiểm tra số đối chiếu cho cả hai phạm vi và ghi cách chạy lại trong `chi_so.md`. Sau đó chạy toàn bộ chương trình, kiểm tra ba chỉ số và so lại các số rủi ro kinh tế với kết quả B1, B4 và A4.

## 4. Bằng chứng

Các commit:

- `f97d039` — `CP1 code`.
- `f83fe05` — `CP2 code`.
- `d475d1c` — `CP4 code`.

Bằng chứng CP5 nằm ở phần `E1 · Ba chỉ số trong đợt chạy thử` trong `src/lab13.py` và phần hướng dẫn kiểm tra trong `report/team/chi_so.md`. Khi chạy `.venv/bin/python lab13.py` trong thư mục `src/`, chương trình chạy hết và in `Kiểm tra số đối chiếu E1 cho hai phạm vi: ĐẠT`. Ba chỉ số chính, dùng và an toàn của toàn mẫu lần lượt là 994/1.200 = 82,83%, 48/177 = 27,12% và 51/1.200 = 4,25%. Trong phạm vi pilot, kết quả tương ứng là 906/982 = 92,26%, 27/128 = 21,09% và 39/982 = 3,97%.

## 5. Công cụ AI đã dùng

Dùng Codex để hỗ trợ viết code Python cho CP1, CP2, CP4, CP5 và rà soát báo cáo cá nhân từ phần việc đã thực hiện. Tự kiểm tra bằng cách chạy toàn bộ script, so số đối chiếu trong hướng dẫn và đối chiếu tử số, mẫu số với `chi_so.md`.

## 6. Tự đánh giá

Hoàn thành phần code được giao ở CP1, CP2 và phần tính toán của CP4, CP5. Điều tôi rút ra là chỉ nhìn tiền token sẽ đánh giá thiếu chi phí: thời gian xem lại và làm lại ảnh hưởng lớn hơn nhiều. Tôi cũng hiểu vì sao giới hạn cho chi phí mỗi việc thành công thấp nhất chưa chắc là giới hạn rẻ nhất cho cả công ty.
