# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm: Lavie
- Nhóm được chấm: MMV.
- Căn cứ: `ho_so_launch_v0.md`, `bang_chi_phi.md`, `pilot_plan.yaml`, `chi_so.md` và kết quả chạy `src/lab13.py`.

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Nhóm chọn Go có điều kiện. Trong phạm vi pilot, chi phí có cố định là 4.599 đ/việc ở 45.000 yêu cầu/tháng [simulated]. Hồ sơ cũng nêu điểm bất lợi: xem lại 100% có thể lên 12.415 đ/việc, chưa cộng cố định [simulated]; power chỉ còn 0,64 nếu tác động thật là 5 điểm. Nhóm đặt điều kiện đo phút thật, giảm xem lại và ghi rõ giới hạn cỡ mẫu. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Hồ sơ ghi nhãn simulated cho chi phí và có danh sách đầu vào giả lập trong kế hoạch. Pilot chỉ nhận noi_dia và hang_nang, chi phí lần lượt là 2.696 đ và 8.221 đ/việc [simulated]. Loại quoc_te vì 22.515 đ/việc, bằng 1,88 lần nhân viên tự làm; doi_tac là 10.215 đ/việc và có điều khoản riêng [simulated], nên cũng để ngoài phạm vi. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Kế hoạch chia ngẫu nhiên theo nhân viên, 20 người mỗi nhóm ở cả 12 depot, có đối chứng cùng thời gian và cách giảm chia sẻ câu trả lời. Với mức chênh 6 điểm, mỗi người cần ít nhất 299 yêu cầu, cho 859,20 yêu cầu hiệu dụng mỗi nhóm. Có luật dừng an toàn trong 3 ngày liên tiếp, chi phí trong 2 tuần liên tiếp và vai trò xử lý cụ thể. Ngày quyết định là 12/01/2027, sau cửa sổ chờ mở lại 7 ngày. |
| **Tổng tự chấm** | | | | **30 / 30** | Theo ba tiêu chí của phiếu chấm đối với hồ sơ kế hoạch; chưa xác nhận hiệu quả của pilot thực tế. |

**Đề xuất sau khi tự chấm:** Go.

**Lý do:** Qua các số đã tính, tôi thấy nhóm có cơ sở để thử trong phạm vi noi_dia và hang_nang, nhưng vẫn cần kiểm tra lại bằng dữ liệu đo thật. Trước khi bắt đầu phải có đủ 40 nhân viên, đủ 10 event có `trace_id` và thử được cách tắt trợ lý trong 30 phút. Cuối bước 0.25, thời gian xem lại trung bình phải không quá 5 phút và tỉ lệ cần xem lại không quá 50%, đồng thời đạt điều kiện an toàn thì mới sang bước tiếp theo. Kết quả 82,83% của chỉ số chính hiện chỉ mô tả đợt chạy thử, chưa chứng minh trợ lý làm tăng chỉ số vì chưa có đối chứng.

**Câu hỏi 1: Nếu phải xem lại 100% yêu cầu thì trợ lý còn tiết kiệm hơn nhân viên tự làm không?**

**Trả lời:** Với phạm vi noi_dia và hang_nang, giả định xem lại 5 phút/yêu cầu và làm lại 9 phút/ca, kết quả B4 là 11.743 đ/việc, bằng 0,98 lần mức 12.000 đ của nhân viên tự làm [simulated]. Nếu làm lại 15,3 phút/ca thì tăng lên 12.415 đ, bằng 1,03 lần [simulated]. Các số này chưa cộng cố định. Nếu cộng thêm mức 1.185 đ/việc của kịch bản A4 ở 45.000 yêu cầu/tháng, trường hợp 9 phút cũng thành khoảng 12.928 đ, bằng 1,08 lần [simulated]. Vì vậy, tôi thấy xem lại 100% kéo dài sẽ khó tiết kiệm; pilot cần đo được thời gian xem lại thật và xem có thể giảm tỉ lệ xem lại an toàn hay không.

**Câu hỏi 2: Vì sao nhóm chọn chia theo nhân viên và chấp nhận mức chênh 6 điểm thay vì 5 điểm?**

**Trả lời:** Chia theo từng yêu cầu có nguy cơ cùng một nhân viên mang cách trả lời của trợ lý sang nhóm đối chứng. Chia theo depot thì chỉ có 6 cụm mỗi nhóm, dưới mức 20 cụm. Nhóm chọn chia theo nhân viên để có 20 cụm mỗi nhóm, nhưng với ICC 0,02, cỡ mẫu hiệu dụng luôn dưới 1.000, không đạt mức 1.251 cần cho chênh 5 điểm. Khi chuyển sang chênh 6 điểm, cần 859 yêu cầu hiệu dụng mỗi nhóm. Kết quả code cho thấy 20 người × 299 yêu cầu, chia hệ số thiết kế 6,96, đạt khoảng 859,20. Đánh đổi là nếu tác động thật chỉ có 5 điểm thì power còn khoảng 64%, tức khoảng 36% khả năng bỏ sót; không thấy khác biệt cũng chưa thể kết luận trợ lý không có tác động.

**Câu hỏi 3: Với tỉ lệ mở lại hiện tại, luật an toàn có làm pilot dừng ngay khi bắt đầu không?**

**Trả lời:** Tỉ lệ mở lại hiện tại là 4,25% trên toàn mẫu và 3,97% trong phạm vi pilot, đều từ dữ liệu lab giả lập. Mức 3,97% chưa vượt trần 6%, nhưng chưa có số đối chứng nên chưa kiểm tra được điều kiện chênh 2 điểm. Theo kế hoạch, khi mỗi nhóm có ít nhất 200 yêu cầu, nếu nhóm trợ lý mở lại cao hơn đối chứng ít nhất 2 điểm phần trăm hoặc vượt 6% trong 3 ngày liên tiếp thì Giám đốc vận hành tắt trợ lý trong 30 phút. Riêng hoàn tiền trùng chỉ cần 1 ca là dừng ngay, không chờ đủ mẫu. Vì vậy, số nền hiện tại chưa tự làm pilot dừng, nhưng vẫn phải theo dõi đủ các điều kiện đã viết trước.
