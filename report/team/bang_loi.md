# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Hoàng Xuân Lĩnh · Người gắn nhãn 2: Nguyễn Quang Thành (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Ngữ cảnh | Do người dùng | Không | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 19 / 20 = 95%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 9 (Ngữ cảnh / Do người dùng → Do người dùng):** gắn theo nguyên nhân gốc: đầu vào sai do khách nhập nhầm loại mã (mã đơn của sàn thay vì mã vận đơn); việc trợ lý dừng mà không gợi ý là chỗ cần sửa, không phải nguyên nhân, nên không tính là Ngữ cảnh.

Đồng thuận 95% (≥ 80%) nên giữ nguyên năm định nghĩa của đề.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 14 | Do người dùng | `ticket_reopened` có `reason = bam_nham_xac_nhan` ÷ `ticket_closed`; ngưỡng > 1%; tính mỗi ngày | Chỉ bật nút "Xác nhận đã nhận tiền" sau khi có `refund_ledger_write` `ok`; hỏi lại một bước kèm số tiền và nơi nhận; cho khách hoàn tác trong 24 giờ | PM trợ lý hoàn phí |
| 7 | Hệ thống | `ticket_closed` mà cùng `request_id` có `refund_ledger_write` `loi` và không có `ok`; ngưỡng ≥ 1 ca; đối chiếu mỗi 15 phút | Chỉ báo "đã hoàn" sau khi sổ cái trả `ok`; hết 3 lần thử thì tạo `handoff_to_staff` và báo khách "đang xử lý"; nhân viên xử lý lại các ca đã báo sai | Kỹ sư trưởng agent |
| 3 | Ngữ cảnh | `ticket_reopened` có `reason = chua_nhan_tien` và cùng `request_id` đã có `refund_ledger_write` `ok`, chia số lệnh `ok`; ngưỡng > 2%; tính mỗi ngày | Tin nhắn ghi rõ tiền về ví LogiX, số tiền, giờ ghi có và cách chuyển về ngân hàng; hiện nơi nhận tiền trước khi khách gửi yêu cầu | PM trợ lý hoàn phí |
| 4 | Giới hạn hệ thống | `handoff_to_staff` có `reason = thieu_du_lieu` và `loai = quoc_te` ÷ `refund_request_created` có `loai = quoc_te` (nối theo `request_id`); ngưỡng > 10%; tính mỗi tuần | Chuyển thẳng nhân viên ngay từ đầu kèm tóm tắt, nói rõ phần không tra được và giờ phản hồi; để `quoc_te` ngoài pilot cho tới khi có dữ liệu hãng nước ngoài | Trưởng nhóm CSKH |
| 17 | Ngầm | `audit_sample_checked` có `phien_ban_bang_gia` khác bản hiệu lực, hoặc `so_tien_da_hoan ≠ so_tien_dung`; ngưỡng ≥ 1 đơn; mẫu 100 đơn mỗi tuần | Xoá bộ nhớ đệm ngay khi bảng giá đổi và chặn tính tiền bằng bản hết hiệu lực; chạy lại 212 đơn để tìm và bù chênh lệch | Kế toán trưởng |

Event lấy từ `chi_so.md`. Các ngưỡng là đề xuất ban đầu, chưa có số nền; xem lại sau tuần pilot đầu. Ca 17: nếu 212 đơn/9 ngày nằm trong khoảng 1.500 yêu cầu/ngày thì tỉ lệ khoảng 1,6%, mẫu 100 đơn bắt được ít nhất một đơn trong tuần với xác suất khoảng 79%; nên lấy mẫu thêm ngay sau mỗi lần đổi bảng giá.
