# Tính tay CP1 · Người kiểm số

Các con số dưới đây được tính độc lập từ hai file `src/logix_runs.csv` và `src/logix_requests.csv`, không dùng code trong `lab13.py`. Hai cột `_simulated` là dữ liệu giả lập, nên mọi con số tính từ hai cột này đều mang nhãn **simulated**.

Cách so: chạy `python lab13.py`, chép số của code vào cột "Code". Lệch (%) = (Code − Tính tay) ÷ Tính tay × 100. Mức lệch không được quá 2%.

Giá dùng chung: token vào 26 đ/1.000 token · token ra 130 đ/1.000 token · tool 15 đ/lần · nhân viên 2.000 đ/phút.

## A1 · Ba phép thử (p = 0,8)

| Phép thử | Cách tính | Tính tay | Code | Lệch |
|---|---|---:|---:|---:|
| Số lần chạy trung bình, tối đa 2 lần | (1 − 0,2²) ÷ 0,8 = 0,96 ÷ 0,8 | **1,20** | 1,20 (ĐẠT) | 0% |
| Số lần chạy trung bình, chạy đến khi đúng | 1 ÷ 0,8 | **1,25** | 1,25 (ĐẠT) | 0% |
| Hệ số chi phí, tối đa 3 lần | [(1 − 0,2³) ÷ 0,8] ÷ (1 − 0,2³) = 1,24 ÷ 0,992 | **1,25** | 1,25 (ĐẠT) | 0% |

## A2 · Mô hình chi phí từ trace

### Bước 1: cộng các cột

| Tổng | File | Giá trị |
|---|---|---:|
| Số lần chạy (mọi dòng, kể cả `loi`) | runs | 1.624 |
| Tổng `tokens_in` | runs | 5.771.712 |
| Tổng `tokens_out` | runs | 734.774 |
| Tổng `tool_calls` | runs | 5.600 |
| Số yêu cầu | requests | 1.200 |
| Tổng `phut_xem_lai_simulated` | requests | 890 phút [simulated] |
| Tổng `phut_lam_lai_simulated` | requests | 1.132 phút [simulated] |
| Đếm `ket_qua` = `thanh_cong` | requests | 978 |
| Đếm `ket_qua` = `chuyen_nhan_vien` | requests | 148 |
| Đếm `ket_qua` = `lam_lai` | requests | 74 |

Lần chạy thứ 2 và 3 (`attempt` > 1): 424 lần · tokens_in 1.815.168 · tokens_out 190.424 · tool_calls 1.457.

### Bước 2: tính tiền

| Khoản | Cách tính | Tính tay (đ) | Code | Lệch | Nhãn |
|---|---|---:|---:|---:|---|
| Token | 5.771.712 ÷ 1.000 × 26 + 734.774 ÷ 1.000 × 130 = 150.064,5 + 95.520,6 | **245.585** | 245.585,1 | 0% | đo từ trace |
| Tool | 5.600 × 15 | **84.000** | 84.000 | 0% | đo từ trace |
| Phần lần chạy 2 và 3 | 1.815.168 ÷ 1.000 × 26 + 190.424 ÷ 1.000 × 130 + 1.457 × 15 = 47.194,4 + 24.755,1 + 21.855 | **93.804** | 93.804,5 | 0% | đo từ trace |
| Xem lại | 890 × 2.000 | **1.780.000** | 1.780.000 | 0% | simulated |
| Làm lại | 1.132 × 2.000 | **2.264.000** | 2.264.000 | 0% | simulated |
| Tổng chi phí | 245.585 + 84.000 + 1.780.000 + 2.264.000 | **4.373.585** | 4.373.585,1 | 0% | có phần simulated |
| Số việc thành công | đếm `thanh_cong` | **978** | 978 | 0% | |
| Chi phí mỗi việc thành công | 4.373.585 ÷ 978 | **4.472** | 4.472,0 | 0% | simulated |
| Hoá đơn chia số yêu cầu | (245.585 + 84.000) ÷ 1.200 | **274,7** | 274,7 | 0% | đo từ trace |

### Bước 3: hai câu trả lời

- Chi phí mỗi việc thành công gấp 4.472 ÷ 274,7 = **16,3 lần** hoá đơn chia số yêu cầu [simulated].
- Tỉ trọng các khoản trong tổng chi phí:
  - Làm lại: 2.264.000 ÷ 4.373.585 = **51,8%** [simulated], khoản lớn nhất.
  - Xem lại: 40,7% [simulated].
  - Token và tool cộng lại: 7,5%.

  Như vậy giờ nhân viên chiếm 92,5% tổng chi phí.
- So với nhân viên tự làm, phải tính chi phí cả hệ thống. Có 148 ca `chuyen_nhan_vien` và 74 ca `lam_lai`, tổng cộng 222 ca do nhân viên làm thay. Chi phí cả hệ thống = (4.373.585 + 222 × 12.000) ÷ 1.200 = **5.865 đ/yêu cầu**, bằng **0,49×** của 12.000 đ [simulated].

## A3 · Tách theo loại yêu cầu

### Bước 1: cộng các cột theo `loai`

Ghép bảng runs với bảng requests theo cột `request_id`, rồi cộng theo từng giá trị của `loai`.

| Loại | Số yêu cầu | Thành công | Số lần chạy | tokens_in | tokens_out | tool_calls | Phút xem lại | Phút làm lại |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| noi_dia | 824 | 783 | 916 | 2.961.633 | 415.268 | 3.180 | 471 | 495 |
| hang_nang | 158 | 117 | 232 | 787.921 | 104.231 | 786 | 173 | 285 |
| quoc_te | 150 | 41 | 348 | 1.570.176 | 157.863 | 1.185 | 145 | 277 |
| doi_tac | 68 | 37 | 128 | 451.982 | 57.412 | 449 | 101 | 75 |

### Bước 2: tính chi phí theo loại

| Loại | Token (đ) | Tool (đ) | Tổng (đ) [sim] | Tỉ lệ thành công | Lần chạy / yêu cầu | Chi phí mỗi việc thành công [sim] | So với 12.000 đ | Code | Lệch |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| noi_dia | 130.987 | 47.700 | 2.110.687 | 783/824 = 95,0% | 916/824 = 1,11 | **2.696** | 0,22× | 2.696 · 0,22 | 0% |
| hang_nang | 34.036 | 11.790 | 961.826 | 117/158 = 74,1% | 232/158 = 1,47 | **8.221** | 0,69× | 8.221 · 0,69 | 0% |
| quoc_te | 61.347 | 17.775 | 923.122 | 41/150 = 27,3% | 348/150 = 2,32 | **22.515** | 1,88× | 22.515 · 1,88 | 0% |
| doi_tac | 19.215 | 6.735 | 377.950 | 37/68 = 54,4% | 128/68 = 1,88 | **10.215** | 0,85× | 10.215 · 0,85 | 0% |

Tổng (đ) = token + tool + (phút xem lại + phút làm lại) × 2.000. Ví dụ với noi_dia: 130.987 + 47.700 + (471 + 495) × 2.000 = 2.110.687.

Kiểm tra chéo: cộng tổng của 4 loại phải ra đúng 4.373.585.

### Bước 3: chạy lại có giúp với quoc_te không

| Lần chạy (attempt) | Số lần chạy | Số lần `ok` | Tỉ lệ ok |
|---|---:|---:|---:|
| 1 | 150 | 45 | 30,0% |
| 2 | 105 | 12 | 11,4% |
| 3 | 93 | 2 | 2,2% |

Kết luận: quoc_te không đáng để trợ lý xử lý (1,88×, chỉ thành công 27,3%). Tỉ lệ đúng giảm mạnh qua mỗi lần chạy lại, nên chạy lại chỉ tốn thêm tiền.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Trong phạm vi này có 982 yêu cầu và 900 việc thành công. Tổng chi phí là 2.110.687 + 961.826 = 3.072.513 đ [simulated].

Chi phí mỗi việc thành công (chưa tính cố định) = 3.072.513 ÷ 900 = **3.414 đ** [simulated].

| Khối lượng | Việc thành công/tháng | Cố định mỗi việc | Chi phí + cố định | So với 12.000 đ | Code | Lệch |
|---|---:|---:|---:|---:|---:|---:|
| 45.000 yêu cầu/tháng | 45.000 × 900 ÷ 1.200 = **33.750** | 40.000.000 ÷ 33.750 = **1.185** | 3.414 + 1.185 = **4.599** | **0,38×** | 33.750 · 1.185 · 4.599 · 0,38 | 0% |
| Một nửa (22.500) | **16.875** | **2.370** | **5.784** | **0,48×** | 16.875 · 2.370 · 5.784 · 0,48 | 0% |

Hai dòng trên làm theo cách của file hướng dẫn: chia 900 cho 1.200 (toàn bộ mẫu), không chia cho 982 (số yêu cầu trong phạm vi).

Kết luận: ở quy mô 45.000 yêu cầu/tháng, chi phí cố định không đổi kết luận (0,38×). Khi khối lượng nhỏ, chi phí cố định mỗi việc tăng nhanh, nên hồ sơ phải ghi rõ con số đã cộng cố định hay chưa và ở khối lượng nào.

## Kết quả đối chiếu

Đã chạy `python lab13.py` (commit `f97d039 CP1 code`). Ba phép thử ĐẠT, mọi số A2, A3, A4 khớp với tính tay, lệch 0%. CP1 đạt.

## Nếu lệch, kiểm tra những chỗ này trong code

- Tử số chỉ cộng các lần chạy `ok`. Phải cộng cả 1.624 lần chạy.
- Mẫu số chia cho 1.200. Phải chia cho 978 (số việc thành công).
- Quên chia 1.000 trước khi nhân giá token.
- Đọc CSV thiếu `keep_default_na=False`.
