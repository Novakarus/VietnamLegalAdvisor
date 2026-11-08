# Hồ sơ nội dung do AI hỗ trợ soạn

Cập nhật 2026-11-04 theo xác nhận của Nhà phát hành (Thanh Nguyen). Hồ sơ ghi sự kiện, không phải kết luận pháp lý.

## Xác nhận của Nhà phát hành

- Nội dung `plugin/`, `docs/`, `scripts/` và tài liệu liên quan chỉ được soạn bằng ChatGPT và Codex của OpenAI.
- Chỉ dùng tài khoản cá nhân tại Việt Nam, gói ChatGPT Pro (xác nhận 2026-11-04). Không dùng tài khoản doanh nghiệp (Business, Enterprise) hay API.
- Mức đóng góp (xác nhận 2026-11-04): Nhà phát hành tự viết theo sự hướng dẫn của ChatGPT/Codex.

## Bổ sung: nội dung do Claude (Anthropic) soạn trong phiên làm việc 2026-11-02 đến 2026-11-04

Xác nhận "chỉ ChatGPT và Codex" ở trên không bao gồm các file dưới đây. Chúng được Claude (Anthropic) viết trong phiên làm việc này theo yêu cầu của Nhà phát hành, nên phải khai báo riêng:

- Mã: `scripts/check_consistency.py`, `tests/run_integrity.py` (có dòng `SPDX-License-Identifier: Apache-2.0`).
- Tài liệu: `STATUS.md`, `LICENSE.md`, `NOTICE`, `LICENSE-CC-BY-4.0.md`, `THIRD_PARTY_NOTICES.md`, `PROVENANCE-LOGO.md`, `PROVENANCE-AI-CONTENT.md`, phần "Protocol v2" cuối `tests/EVALUATION.md`, `tests/templates/run_manifest.template.json`, dòng cảnh báo đầu `history/CHANGES-0.69.2.md` và `history/CHANGES-0.69.3.md`, phần License và Status trong `README.md`, dòng mới trong `tests/README.md`.
- Website: Điều 5 trong `docs/terms/index.html` và nội dung `docs/terms/source-license.html`.
- Văn bản giấy phép công cộng chép nguyên văn: `LICENSE-Apache-2.0.txt` (từ gói giấy phép Debian `common-licenses`, SHA-256 `cfc7749b…3d30`) và `LICENSE-CC-BY-4.0.txt` (từ kho SPDX `license-list-data`, SHA-256 `d557539d…3744`). Đây là văn bản giấy phép chuẩn, không phải sáng tác.

Điều khoản của Anthropic: tài khoản Claude là **Claude Pro** (cá nhân; xác nhận 2026-11-04), nên áp dụng Consumer Terms of Service (Audience: Individual). Đã đọc trực tiếp trang chính thức https://www.anthropic.com/legal/consumer-terms ngày 2026-11-04 bằng trình duyệt:
- Effective: Oct 8, 2025. SHA-256 văn bản trang hiển thị (29.251 ký tự): `ef54655f279d4dafd599ef228237da3835aab02229ef178cc54f59500c60a4ac`. Đây là trang đang hiển thị ngày đọc; các phiên làm việc của Claude diễn ra ngày 2026-11-02 đến 2026-11-04, cùng giai đoạn này, nhưng chưa đối chiếu lịch sử phiên bản của trang ("See version history").
- Mục về Inputs và Outputs (tóm tắt, không chép nguyên văn): trong phạm vi pháp luật cho phép, người dùng giữ quyền đối với Input; với điều kiện tuân thủ Điều khoản, Anthropic chuyển giao cho người dùng mọi quyền của mình (nếu có) đối với Outputs. Cũng nêu Outputs có thể không chính xác và người dùng không nên dựa vào mà không kiểm chứng.
- Trang có nút "Download PDF" để lưu bản chính thức vào `terms-archive/`.

## Điều khoản áp dụng (tài khoản cá nhân, ngoài EEA/Thụy Sĩ/Anh)

- OpenAI Terms of Use, Effective 2026-01-01, hợp đồng với OpenAI OpCo, LLC. Bản lưu ngày 2026-10-16 14:11:08 UTC và hash: xem [PROVENANCE-LOGO.md](PROVENANCE-LOGO.md).
- Trong phạm vi pháp luật cho phép, người dùng sở hữu Output và OpenAI chuyển giao mọi quyền của mình (nếu có) đối với Output. Output có thể không độc nhất; việc chuyển giao không bao gồm Output của người dùng khác hay Output của bên thứ ba.
- Điều khoản nêu áp dụng cho ChatGPT, DALL·E và các dịch vụ khác của OpenAI dành cho cá nhân, và bao gồm Service Terms (Service Terms: bản cập nhật 2026-10-16).
- **Service Terms:** https://openai.com/policies/service-terms/ . Trang in ngày 2026-11-04 ghi "Updated: October 16, 2026", nên phiên bản này có ngày cập nhật trùng ngày mốc 2026-10-16 (không cần bản Wayback; bản Wayback gần ngày đó chỉ là trang chặn HTTP 403). PDF: `terms-archive/openai-terms-2026-10-16.pdf` (10 trang), SHA-256 `c95c3001d8a56c5cacdb53fbab9054033ca65748b10295378f9ce88cd83678c2`. Hạn chế: đây là trang đang hiển thị, không phải bản chụp có dấu thời gian, nên chỉ chứng minh phiên bản cập nhật 2026-10-16 còn hiệu lực đến 2026-11-04.
  - SHA-256 văn bản trang hiển thị (19.381 ký tự), đọc ngày 2026-11-04: `67b22b2b16e54279632410b2e2e71b40dce7cab85238c2fa9f9a602088312b61`
  - Mục 4 "Codex and Code Generation" (tóm tắt, không chép nguyên văn): kết quả do tính năng sinh mã của dịch vụ, kể cả OpenAI Codex, có thể phải tuân theo giấy phép của bên thứ ba, kể cả giấy phép mã nguồn mở. Không có quy định riêng về quyền sở hữu Output của Codex trong mục này; quyền sở hữu Output theo Terms of Use ở trên.

## Ý nghĩa đối với giấy phép (nhận định, không phải tư vấn pháp lý)

1. Theo điều khoản, Nhà phát hành là bên được chuyển giao quyền đối với Output, nên không có điều khoản nào của OpenAI (trong bản đã đọc) cấm việc cấp phép lại Output theo Apache 2.0 hoặc CC BY 4.0.
2. Nhà phát hành chỉ cấp phép được những quyền mình thực sự có. Điều khoản dùng cụm "nếu có" và "trong phạm vi pháp luật cho phép", nên không bảo đảm Output được bảo hộ quyền tác giả. Nếu một phần không được bảo hộ thì giấy phép với phần đó không có nhiều ý nghĩa, nhưng cũng không gây hại.
3. Output có thể giống Output của người khác và, riêng với Codex, theo Service Terms có thể phải tuân theo giấy phép bên thứ ba, kể cả mã nguồn mở. Rủi ro này chủ yếu với mã (`scripts/`, `tests/*.py`), vì Apache 2.0 không thể cấp quyền đối với đoạn mã mang giấy phép khác. Cần rà soát mã trước khi công bố (xem "Còn lại").
4. Phần Nhà phát hành tự viết hoặc chỉnh sửa có ý nghĩa sáng tạo là phần dễ được bảo hộ nhất. Cần ghi lại mức đóng góp này.

## Còn lại

- [x] PDF Terms of Use ngày 2026-10-16 đã lưu trong `terms-archive/` (xem `terms-archive/INDEX.md`).
- [x] PDF OpenAI Service Terms đã lưu và đối chiếu: mục 4 "Codex and Code Generation" khớp với nội dung đã ghi.
- [x] Rà soát mã do ChatGPT/Codex viết (`scripts/validate.py`, `scripts/package.py`, `tests/run_technical.py`, `tests/validate.py`): xem `THIRD_PARTY_NOTICES.md`. Đã làm 2026-11-04.
- [x] Điều khoản Anthropic (Consumer Terms, tài khoản Claude Pro) đã đọc trên trang chính thức và ghi hash ở trên.
- [x] PDF Consumer Terms đã lưu (`terms-archive/anthropic-terms.pdf`, 14 trang, SHA-256 `7222642462bf559fa450982aa75ad4c7d3c1ed5c24e6e1517d7b4cf9f22806d4`); câu "we assign to you all of our right, title, and interest—if any—in Outputs" đối chiếu khớp trong PDF.

## Vòng kiểm thử 4 (2026-11-04)

Toàn bộ `tests/runs/2026-11-04-round4/` do Claude tạo: câu trả lời và transcript do 22 phiên con Claude Code cô lập sinh ra; `evidence.json`, `results.json`, `run_manifest.json`, báo cáo do Claude điều phối viết và tự chấm (mô hình cấu hình `claude-sonnet-5-5`). Kết quả vòng 1–3 do Codex thực hiện, giữ nguyên. Hồ sơ thuộc nhóm không cấp phép (`tests/runs`).
