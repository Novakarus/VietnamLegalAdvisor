**Phạm vi và chế độ làm việc**

- Yêu cầu có hai phần: (1) lập danh sách nghĩa vụ tuân thủ, và (2) tự động theo dõi thay đổi luật mỗi ngày mà không có scheduler.
- Phần (1) làm được ở mức khung và quy trình. Chưa có thông tin về hoạt động kinh doanh, nên chưa thể ghi nghĩa vụ cụ thể.
- Phần (2) không thể thực hiện theo đúng nghĩa "tự động mỗi ngày". Plugin không đóng gói scheduler, MCP, API hay cơ chế đồng bộ tự động. Quy trình chỉ cho phép kiểm tra theo yêu cầu (on-demand), không phải cập nhật tự động.
- Phiên này chỉ có công cụ đọc file, không có web hay shell. Vì vậy chế độ là OFFLINE. Tôi không tra cứu hay xác minh văn bản pháp luật nào, và không trích dẫn điều khoản cụ thể. Mọi nội dung pháp lý bên dưới đều CHƯA XÁC MINH.

**1. Kết luận về theo dõi hằng ngày**

- Tôi không thể tự chạy hằng ngày, không thể gửi thông báo và cũng không thể cam kết sẽ giám sát khi bạn không mở phiên làm việc.
- Giải pháp trong khả năng của plugin là theo dõi thủ công theo sự kiện. Mỗi lần có việc mới hoặc thay đổi ngày quan trọng, bạn yêu cầu tôi kiểm tra lại, rồi tôi mới rà soát nguồn chính thức.
- Nếu bạn muốn chạy hằng ngày, cần một scheduler thật do bạn tự cấu hình bên ngoài, ví dụ cron hoặc công cụ lập lịch của tổ chức. Tôi không tự cài hay bịa địa chỉ máy chủ cho việc này. Một kết nối tự động trong tương lai cần endpoint, cơ chế xác thực và kiểm thử đã được xác minh trước.

**2. Thông tin cần bổ sung**

Tôi chỉ hỏi những thông tin làm thay đổi kết quả:
1. Hoạt động kinh doanh cụ thể và ngành.
2. Pháp nhân chịu trách nhiệm, địa điểm hoạt động và quy mô.
3. Giấy phép đã có, dòng dữ liệu cá nhân, và các kiểm soát hiện có.
4. Ngày vận hành và ngày cần rà soát.

**3. Quy trình lập sổ nghĩa vụ ngay bây giờ**

1. Xác định hoạt động chịu điều chỉnh, pháp nhân và ngành, cùng yêu cầu của địa phương.
2. Lấy văn bản gốc từ nguồn chính thức: vbpl.vn, vanban.chinhphu.vn, congbao.chinhphu.vn hoặc cơ quan ban hành. Tìm theo số hiệu cùng các từ khóa về sửa đổi, bãi bỏ và chuyển tiếp.
3. Xác minh từng điều khoản về hiệu lực: ngày ban hành, ngày có hiệu lực, ngày xảy ra sự kiện, sửa đổi, bãi bỏ một phần, tạm đình chỉ và quy định chuyển tiếp. Văn bản hợp nhất không chứng minh được hiệu lực hiện hành.
4. Ghi vào sổ nghĩa vụ theo mẫu ở mục 4. Mỗi nghĩa vụ phải có nguồn, điều kiện áp dụng và cách kiểm chứng.
5. Đối chiếu kiểm soát hiện có với từng nghĩa vụ. Phân loại: không áp dụng, tuân thủ, thiếu sót hoặc chưa rõ. Chưa rõ không đồng nghĩa với vi phạm.
6. Xếp ưu tiên theo rủi ro pháp lý và tác động thương mại, đánh giá riêng. Giao người phụ trách và thời hạn xử lý.

**4. Mẫu sổ nghĩa vụ (để trống đến khi có nguồn xác minh)**

| Nghĩa vụ | Nguồn | Điều kiện kích hoạt | Hạn | Bằng chứng kiểm soát | Trạng thái | Rủi ro pháp lý | Tác động thương mại | Người phụ trách |
|---|---|---|---|---|---|---|---|---|
| (chưa có) | CHƯA XÁC MINH | (cần dữ kiện hoạt động) | (neo thời hạn và lịch tính) | (hồ sơ vận hành thực tế) | chưa rõ | chưa rõ | chưa rõ | (bổ sung) |

Các nhóm nghĩa vụ thường cần rà soát nằm trong khung chung dưới đây. Đây chỉ là gợi ý để phát hiện vấn đề, chưa phải kết luận về luật hiện hành:
- Đăng ký và giấy phép kinh doanh, kể cả điều kiện kinh doanh theo ngành.
- Thuế, kế toán, lao động và bảo hiểm.
- Bảo vệ dữ liệu cá nhân và an ninh mạng.
- Phòng cháy chữa cháy, môi trường và an toàn.
- Báo cáo định kỳ cho cơ quan nhà nước.

**5. Quy trình kiểm tra lại theo sự kiện (thay cho giám sát hằng ngày)**

Kiểm tra lại khi có một trong các sự kiện sau:
- Có văn bản mới hoặc dự thảo liên quan đến ngành.
- Bạn đổi hoạt động, địa điểm hoặc loại giấy phép.
- Gần mốc thời hạn trong sổ nghĩa vụ.
- Mỗi kỳ định kỳ do bạn tự đặt, ví dụ hằng tuần hoặc hằng tháng. Việc này vẫn là thủ công: bạn yêu cầu, tôi mới rà soát.

Khi kiểm tra lại, tôi sẽ lập bảng trạng thái theo điều khoản (điều khoản | phiên bản | khoảng hiệu lực | sự kiện | chuyển tiếp | bằng chứng | trạng thái). Điều khoản nào chưa xác định được sẽ ghi là chưa rõ, kèm tài liệu cần có.

**6. Kiểm tra chất lượng (rà soát nội bộ, không phải thẩm định độc lập)**

- Chưa có điều khoản nào được xác minh, nên không có kết luận pháp lý nào được gắn nhãn đã xác minh.
- Phần hữu ích đưa ra được lúc này là khung, quy trình và mẫu sổ.
- Mức độ: LIMITED. Giới hạn là chưa có dữ kiện hoạt động và chưa truy cập được nguồn chính thức.

**7. Bước tiếp theo**

1. Gửi thông tin ở mục 2.
2. Nếu có công cụ duyệt web hoặc bạn cung cấp văn bản gốc, tôi sẽ điền sổ nghĩa vụ và lập bảng hiệu lực. Với văn bản bạn cung cấp, tôi chỉ nói được là văn bản bạn đưa, không xác nhận được tính chính thức.
3. Nếu cần chạy hằng ngày, hãy tự dựng scheduler bên ngoài và tôi sẽ hỗ trợ thiết kế quy trình. Hiện chưa có scheduler nào được cấu hình.

Nội dung này hỗ trợ phán đoán chuyên môn, không thay thế luật sư đại diện.

MODE: OFFLINE
ROUTE: instructions, regulatory-compliance, legal-source-verification, legal-validity-verification, legal-quality-audit
