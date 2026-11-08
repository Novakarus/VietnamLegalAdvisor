# Security Policy

Chính sách này áp dụng cho nguồn plugin Vietnam Legal Advisor, website, công cụ đóng gói và quy trình GitHub Actions trong kho này. Đầu mối tiếp nhận: Thanh Nguyen.

## Supported Versions

Chỉ phiên bản phát hành mới nhất được ưu tiên tiếp nhận bản sửa lỗi bảo mật. Khi có phiên bản mới thay thế, người dùng nên cập nhật; dự án không cam kết duy trì bản vá riêng cho các phiên bản cũ.

| Phiên bản / thành phần | Hỗ trợ bảo mật |
| --- | --- |
| Plugin 0.70.0 — ứng viên, chưa công khai | :white_check_mark: |
| Plugin trước 0.70.0 | :x: |
| Website và công cụ trên nhánh `main` | :white_check_mark: |

“Hỗ trợ” có nghĩa là tiếp nhận, đánh giá và ưu tiên xử lý báo cáo phù hợp; không phải chứng nhận an toàn hoặc cam kết thời hạn khắc phục. Phiên bản 0.70.0 hiện là ứng viên, chưa công khai.

## Reporting a Vulnerability

**Vui lòng báo cáo riêng qua email: ntthanh912@gmail.com**, với tiêu đề `[Security] Vietnam Legal Advisor — mô tả ngắn`.

Không đăng lỗ hổng chưa được xử lý, thông tin đăng nhập hoặc dữ liệu nhạy cảm vào Issues, Pull Requests hay thảo luận công khai.

Báo cáo nên gồm:

- Phiên bản plugin hoặc mã commit, thành phần và môi trường bị ảnh hưởng.
- Mô tả vấn đề, điều kiện xảy ra và tác động có thể có.
- Các bước tái hiện tối thiểu bằng dữ liệu giả lập.
- Kết quả mong đợi và kết quả thực tế; bằng chứng đã che thông tin nhạy cảm.
- Cách liên hệ và mong muốn được ghi nhận đóng góp, nếu có.

Các vấn đề cần báo cáo gồm tiết lộ dữ liệu hoặc bí mật; truy cập hay hành động không được phép; nội dung không đáng tin cậy khiến trợ lý vượt ranh giới được phép với tác động bảo mật cụ thể; mã độc hoặc can thiệp vào website, gói phát hành hay quy trình đóng gói.

Lỗi trả lời pháp lý, thiếu nguồn hoặc lỗi giao diện có thể gửi qua Issues sau khi loại thông tin nhạy cảm. Nếu lỗi đồng thời gây tác động bảo mật, hãy dùng email riêng.

**Quy trình phản hồi dự kiến:**

- Mục tiêu xác nhận tiếp nhận trong **5 ngày làm việc**.
- Mục tiêu cung cấp đánh giá ban đầu hoặc yêu cầu bổ sung trong **10 ngày làm việc**.
- Với báo cáo đang được xử lý, mục tiêu cập nhật ít nhất mỗi **14 ngày**, kể cả khi chưa có bản sửa.

Đây là các mốc mục tiêu của dự án do cá nhân duy trì, không phải thời hạn được bảo đảm. Nếu chưa nhận được xác nhận sau 5 ngày làm việc, bạn có thể gửi thư nhắc.

Nếu báo cáo được chấp nhận, Nhà phát hành sẽ trao đổi về phạm vi ảnh hưởng, biện pháp giảm thiểu, kế hoạch sửa và thời điểm công bố phù hợp. Nếu chưa đủ bằng chứng, báo cáo trùng hoặc không được xác nhận là lỗ hổng, Nhà phát hành sẽ giải thích lý do trong phạm vi có thể và tiếp nhận bằng chứng bổ sung.

Chỉ kiểm tra trong phạm vi bạn có quyền thực hiện. Không truy cập dữ liệu của người khác, làm gián đoạn dịch vụ hoặc kiểm thử hệ thống bên thứ ba khi chưa được phép. Vấn đề thuộc nền tảng lưu trữ, GitHub hoặc nhà cung cấp mô hình cần được báo cáo thêm qua kênh bảo mật của bên tương ứng.

Dự án chưa có chương trình thưởng lỗi. Việc ghi nhận người báo cáo chỉ thực hiện khi có sự đồng ý.
