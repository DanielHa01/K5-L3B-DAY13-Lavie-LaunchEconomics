# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

Ba dòng đầu tính bằng pandas trên `src/logix_requests.csv` (đọc với `keep_default_na=False`); ba cột dùng ở đây không phải cột `_simulated`, nhưng toàn bộ dữ liệu của lab là giả lập.

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200); trong phạm vi `noi_dia` + `hang_nang`: 92,26% (906/982) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48/177: 41 `sua` + 7 `bo`); trong phạm vi: 21,09% (27/128) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200); trong phạm vi: 3,97% (39/982) |
| Dùng | Nhóm tự đề xuất: **Tỉ lệ yêu cầu của nhóm trợ lý được xử lý qua trợ lý** | Số yêu cầu có `arm = tro_ly` và có ít nhất một `agent_suggestion_shown`, chia số `refund_request_created` có `arm = tro_ly`; theo dõi theo tuần và theo `staff_id` | Không cần tính |
| An toàn | Nhóm tự đề xuất: **Tỉ lệ đơn hoàn lệch tiền qua kiểm tra mẫu** | Số đơn trong `audit_sample_checked` có `so_tien_da_hoan ≠ so_tien_dung`, chia số đơn được kiểm tra (mẫu ngẫu nhiên 100 đơn/tuần); bắt được cả sai lệch mà khách không mở lại | Không cần tính |

Chỉ số chính trong đợt chạy thử là 82,83%. Không kết luận được trợ lý làm thay đổi chỉ số này so với mức 0,70, vì đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách / kênh CSKH | request_id, depot, loai, so_tien_vnd, arm (`tro_ly` / `doi_chung`), staff_id, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | request_id, attempt, tokens_in, tokens_out, tool_calls, status (`ok` / `loi`), trace_id | Sau **mỗi** lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | request_id, staff_id, so_tien_de_xuat, trace_id | Khi gợi ý của trợ lý hiện ra cho nhân viên |
| `staff_review_decision` | Nhân viên CSKH | request_id, staff_id, quyet_dinh (`giu` / `sua` / `bo`), phut_xem_lai (đo thật), trace_id | Khi nhân viên bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên CSKH | request_id, staff_id, phut_lam_lai (đo thật), ly_do, trace_id | Khi nhân viên làm lại xong |
| `handoff_to_staff` | Agent | request_id, reason (`het_lan_chay` / `thieu_du_lieu` / `ngoai_pham_vi`), tom_tat, trace_id | Khi trợ lý chuyển yêu cầu cho nhân viên |
| `refund_ledger_write` | Dịch vụ sổ cái | request_id, idempotency_key, so_tien, ket_qua (`ok` / `loi`), trace_id | Khi ghi lệnh hoàn vào sổ cái |
| `ticket_closed` | Hệ thống ticket | request_id, closed_at, created_at, trace_id | Khi yêu cầu được đóng |
| `ticket_reopened` | Khách | request_id, reopened_at, reason, trace_id | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | request_id, so_tien_da_hoan, so_tien_dung, phien_ban_bang_gia, trace_id | Hằng tuần, mẫu ngẫu nhiên 100 đơn |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chính:** `refund_request_created` (mẫu số) + `ticket_closed` (closed_at − created_at ≤ 24 giờ) + `ticket_reopened` (không có trong 7 ngày sau closed_at).
- **Dùng · bỏ qua gợi ý:** `staff_review_decision` (tử số: `sua` + `bo`; mẫu số: mọi quyết định).
- **An toàn · lỗi lọt đến khách:** `ticket_reopened` trong 7 ngày (tử số) ÷ `refund_request_created` (mẫu số).
- **Dùng · tự đề xuất:** `agent_suggestion_shown` ÷ `refund_request_created` có `arm = tro_ly`.
- **An toàn · tự đề xuất:** `audit_sample_checked` (so `so_tien_da_hoan` với `so_tien_dung`).
- **Chi phí mỗi việc thành công (dùng cho luật dừng chi phí):** `agent_run_completed` (token, tool) + `staff_review_decision.phut_xem_lai` + `staff_rework_completed.phut_lam_lai`, chia số yêu cầu đóng không mở lại. Hai event nhân viên thay hai cột `_simulated` bằng phút đo thật.
- Cả năm chỉ số đều tính được từ danh sách event; không chỉ số nào bị "chưa đo được".

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
