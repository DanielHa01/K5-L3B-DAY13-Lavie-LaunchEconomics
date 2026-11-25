# Tính tay CP2 · Người kiểm số

Các con số dưới đây được tính độc lập từ hai file `src/logix_runs.csv` và `src/logix_requests.csv`, không dùng code trong `lab13.py`. Mọi chi phí có phần xem lại hoặc làm lại đều mang nhãn **simulated**.

Cách so: chạy `python lab13.py`, chép số của code vào cột "Code". Lệch (%) = (Code − Tính tay) ÷ Tính tay × 100. Mức lệch không được quá 2%.

## Mốc gốc (từ CP1)

| Khoản | Giá trị (đ) |
|---|---:|
| Token | 245.585 |
| Tool | 84.000 |
| Xem lại (890 phút × 2.000) | 1.780.000 [simulated] |
| Làm lại (1.132 phút × 2.000) | 2.264.000 [simulated] |
| Tổng | 4.373.585 |
| Số việc thành công | 978 |
| **Chi phí mỗi việc thành công (gốc)** | **4.472** [simulated] |

Mô hình là phép cộng tuyến tính, nên mỗi kịch bản chỉ cần cộng thêm hoặc trừ bớt phần tiền bị đổi vào tổng 4.373.585 đ, rồi chia cho số việc thành công.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính tay | Tổng mới (đ) | Chi phí mỗi việc thành công | Thay đổi | Code | Lệch |
|---|---|---:|---:|---:|---:|---:|
| Giá token gấp đôi | Token 245.585 thành 491.170 (+245.585) | 4.619.170 | **4.723** | **+5,6%** | 4.723 · +5,6% | 0% |
| Giá token giảm một nửa | Token thành 122.793 (−122.793) | 4.250.793 | **4.346** | **−2,8%** | 4.346 · −2,8% | 0% |
| Tỉ lệ xem lại gấp đôi | Xem lại thành 3.560.000 (+1.780.000) | 6.153.585 | **6.292** | **+40,7%** | 6.292 · +40,7% | 0% |
| Tỉ lệ xem lại giảm một nửa | Xem lại thành 890.000 (−890.000) | 3.483.585 | **3.562** | **−20,3%** | 3.562 · −20,3% | 0% |
| Số ca làm lại gấp đôi | Làm lại thành 4.528.000 (+2.264.000) | 6.637.585 | **6.787** | **+51,8%** | 6.787 · +51,8% | 0% |
| Số ca làm lại giảm một nửa | Làm lại thành 1.132.000 (−1.132.000) | 3.241.585 | **3.315** | **−25,9%** | 3.315 · −25,9% | 0% |
| Lương nhân viên tăng 25% | (890 + 1.132) phút × 2.500 = 5.055.000 | 5.384.585 | **5.506** | **+23,1%** | 5.506 · +23,1% | 0% |
| Chỉ cho chạy tối đa 2 lần | Xem bảng giới hạn chạy bên dưới | 4.093.220 | **4.237** | **−5,2%** | 4.237 · −5,2% | 0% |
| Chỉ cho chạy 1 lần | Xem bảng giới hạn chạy bên dưới | 3.621.781 | **4.111** | **−8,1%** | 4.111 · −8,1% | 0% |

Ở bảng trên, các dòng 1 đến 7 giữ nguyên mẫu số 978. Hai dòng giới hạn chạy có mẫu số khác (966 và 881), vì các yêu cầu cần nhiều lần chạy hơn giới hạn bị coi là chuyển nhân viên.

### Tự kiểm tra B1

| Cặp kịch bản | Gấp đôi | Giảm một nửa | Bằng một nửa? |
|---|---:|---:|---|
| Giá token | +5,6% | −2,8% | Đúng |
| Xem lại | +40,7% | −20,3% | Đúng (40,70 ÷ 2 = 20,35) |
| Làm lại | +51,8% | −25,9% | Đúng |

Cũng kiểm tra được: +40,7% đúng bằng tỉ trọng xem lại trong tổng chi phí, +51,8% đúng bằng tỉ trọng làm lại (xem A2). Lương +25% làm tăng (40,7% + 51,8%) × 25% = 23,1%.

### Giới hạn số lần chạy

Cách làm: bỏ các lần chạy có `attempt` lớn hơn giới hạn. Yêu cầu có `so_lan_chay` lớn hơn giới hạn thì coi là `chuyen_nhan_vien`, phút xem lại và làm lại của yêu cầu đó tính bằng 0.

| Giới hạn | Số lần chạy giữ lại | tokens_in | tokens_out | tool_calls | Token (đ) | Tool (đ) | Phút xem lại | Phút làm lại | Tổng (đ) [sim] | Thành công |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 lần | 1.200 | 3.956.544 | 544.350 | 4.143 | 173.636 | 62.145 | 762 | 931 | 3.621.781 | 881 |
| 2 lần | 1.458 | 4.994.250 | 660.921 | 5.030 | 215.770 | 75.450 | 855 | 1.046 | 4.093.220 | 966 |
| 3 lần (gốc) | 1.624 | 5.771.712 | 734.774 | 5.600 | 245.585 | 84.000 | 890 | 1.132 | 4.373.585 | 978 |

Ví dụ với giới hạn 2 lần: 215.770 + 75.450 + (855 + 1.046) × 2.000 = 4.093.220, chia cho 966 ra 4.237.

## B2 · Đổi một cặp và xếp hạng

| Kịch bản | Cách tính tay | Tổng mới (đ) | Chi phí mỗi việc thành công | Thay đổi | Code | Lệch |
|---|---|---:|---:|---:|---:|---:|
| Token gấp đôi và xem lại gấp đôi | 4.373.585 + 245.585 + 1.780.000 | 6.399.170 | **6.543** | **+46,3%** | 6.543 · +46,3% | 0% |

Tự kiểm tra: 5,6% + 40,7% = 46,3%, đúng bằng tổng hai tác động riêng vì mô hình cộng tuyến tính.

Xếp hạng ba yếu tố mạnh nhất, theo mức thay đổi khi gấp đôi hoặc tăng:

1. **Số ca làm lại** (+51,8%)
2. **Tỉ lệ xem lại** (+40,7%)
3. **Lương nhân viên** (+23,1% khi tăng 25%)

Giá token chỉ gây +5,6%, đứng cuối.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 × số yêu cầu không thành công, vì nhân viên phải làm thay các yêu cầu này. Số yêu cầu không thành công = 1.200 − số việc thành công.

| Giới hạn | Tổng chi phí trợ lý [sim] | Không thành công | Cả hệ thống [sim] | Chi phí mỗi việc thành công [sim] | Code | Lệch |
|---|---:|---:|---:|---:|---:|---:|
| 1 lần | 3.621.781 | 1.200 − 881 = **319** | 3.621.781 + 319 × 12.000 = **7.449.781** | **4.111** (thấp nhất) | 3.621.781 · 319 · 7.449.781 · 4.111 | 0% |
| 2 lần | 4.093.220 | 1.200 − 966 = **234** | 4.093.220 + 234 × 12.000 = **6.901.220** (rẻ nhất) | **4.237** | 4.093.220 · 234 · 6.901.220 · 4.237 | 0% |
| 3 lần | 4.373.585 | 1.200 − 978 = **222** | 4.373.585 + 222 × 12.000 = **7.037.585** | **4.472** | 4.373.585 · 222 · 7.037.585 · 4.472 | 0% |

Kết luận: giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ). Kết quả này không trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ). Lý do: chạy 1 lần đẩy thêm 319 − 234 = 85 việc sang nhân viên [simulated].

## B4 · Nếu phải xem lại tất cả (noi_dia + hang_nang)

Các giả định của đề: mỗi yêu cầu có câu trả lời thì xem lại 5 phút, mỗi ca làm lại mất 9 phút.

| Bước | Đếm hoặc cộng | Giá trị | Tiền (đ) |
|---|---|---:|---:|
| 1 | Số yêu cầu trong phạm vi | 982 | |
| 2 | Yêu cầu có ít nhất một lần chạy `status` = `ok`, mỗi yêu cầu xem lại 5 phút | 948 | 948 × 5 × 2.000 = **9.480.000** |
| 3 | Số ca `ket_qua` = `lam_lai`, mỗi ca 9 phút | 48 | 48 × 9 × 2.000 = **864.000** |
| 4 | Token + tool của mọi lần chạy thuộc 982 yêu cầu | 165.023 + 59.490 | **224.513** |
| 5 | Tổng | | **10.568.513** |
| 6 | Số việc thành công trong phạm vi | 900 | |
| | **Chi phí mỗi việc thành công** | 10.568.513 ÷ 900 | **11.743 đ = 0,98× của 12.000 đ** [simulated] |

| Kết quả | Tính tay | Code | Lệch |
|---|---:|---:|---:|
| Chi phí mỗi việc thành công khi xem lại 100% (9 phút làm lại) | 11.743 | 11.743 · 0,98 · hoà vốn 5,1 phút | 0% |
| Chi phí mỗi việc thành công khi xem lại 100% (15,3 phút làm lại) | 12.415 | 12.415 · 1,03 · hoà vốn 4,8 phút | 0% |

### Độ nhạy theo phút làm lại

Đề cho 9 phút mỗi ca, nhưng trong dữ liệu, 74 ca `lam_lai` có `phut_lam_lai_simulated` trung bình **15,3 phút** (trung vị 14,5).

- Với 15,3 phút: 48 × 15,3 × 2.000 = 1.468.800 đ, tổng 11.173.313 đ, ra **12.415 đ = 1,03×** [simulated]. Tức là xem lại 100% còn đắt hơn để nhân viên tự làm.
- Mức hoà vốn (chi phí đúng bằng 12.000 đ), tính theo số phút xem lại mỗi yêu cầu:
  - Với 9 phút làm lại: (12.000 × 900 − 224.513 − 864.000) ÷ (948 × 2.000) = **5,1 phút**.
  - Với 15,3 phút làm lại: (10.800.000 − 224.513 − 1.468.800) ÷ 1.896.000 = **4,8 phút**.

Ý nghĩa: xem lại 100% thì trợ lý gần như không tiết kiệm được gì, vì tiền xem lại chiếm khoảng 90% chi phí. Pilot phải học được tỉ lệ xem lại giảm an toàn được đến đâu, và mỗi lần xem lại có ngắn hơn 5 phút được không.

## Kết quả đối chiếu

Đã chạy `python lab13.py` (commit `f83fe05 CP2 code`). Mọi số B1, B2, B3, B4 khớp với tính tay, lệch 0%. Xếp hạng ba yếu tố của code trùng với tính tay. CP2 đạt.

## Nếu lệch, kiểm tra những chỗ này trong code

- Kịch bản giá token: chỉ đổi `gia_vao` và `gia_ra`, giữ nguyên giá tool 15 đ.
- Kịch bản giới hạn chạy: phải đổi `ket_qua` của yêu cầu vượt giới hạn thành `chuyen_nhan_vien` và đặt phút xem lại, làm lại về 0. Nếu quên bước này, mẫu số vẫn là 978.
- B3: số không thành công là 1.200 − số việc thành công. Con số này gồm cả ca `lam_lai`, không chỉ ca `chuyen_nhan_vien`.
- B4: đếm yêu cầu có ít nhất một lần chạy `ok` (948), không đếm số lần chạy `ok`. Chỉ lấy noi_dia và hang_nang.
