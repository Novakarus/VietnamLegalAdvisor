# Runbook: chạy 22 ca trên host thật (Protocol v2, mục 1, 2, 3, 5)

Mục tiêu: khắc phục lỗi `host` (production_host=false). Plugin có định dạng Codex/OpenAI (`plugin/.codex-plugin`, `extensions.com.openai`), nên host mục tiêu là **Codex** (app/CLI/IDE). Runner = OpenAI; người chấm phải là hãng khác (Claude hoặc luật sư) để khắc phục lỗi `grader`.

## Chuẩn bị
1. `python scripts/import_host_run.py prepare --run tests/runs/2026-11-05-round5` → tạo `prompts/<ID>.txt` và chép ZIP ứng viên.
2. Giải nén ZIP 0.70.0 (đúng file trong `dist/`, SHA-256 `ebbd7e60…b839`) và cài vào Codex theo cơ chế plugin của host. Không sửa file plugin.
3. Trong Codex: xác nhận host liệt kê đủ **13 skill** (chụp màn hình hoặc xuất danh sách). Ghi tên và phiên bản host (`codex --version` hoặc màn hình About).

## Mỗi ca (22 ca)
- Mở **phiên mới** (không dùng chung ngữ cảnh), cấu hình **không có công cụ web**: tắt web search và không cấp mạng cho sandbox (ví dụ `web_search = "disabled"` / sandbox không có network). Ghi cách tắt để điền `--offline-how`.
- Dán nguyên nội dung `prompts/<ID>.txt`. Không dán `must_include`/`must_not`.
- Ca R02, C01, D01, V01, V02 tham chiếu `tests/fixtures.md`: chỉ cấp file này (đặt trong thư mục làm việc); các ca khác không cấp tài liệu thêm.
- Không chỉnh sửa hay nhắc lại câu hỏi. Mỗi ca một phiên.

## Xuất transcript
Lấy file phiên nguyên bản của host (với Codex CLI/app thường là `~/.codex/sessions/<năm>/<tháng>/<ngày>/rollout-*.jsonl`). Đổi tên từng file thành `<ID>.jsonl` vào một thư mục (ví dụ `transcripts/`). Không mở và lưu lại bằng trình soạn thảo.

## Nhập và kiểm tra
```
python scripts/import_host_run.py import --run tests/runs/2026-11-05-round5 --transcripts transcripts \
  --host-name Codex --host-version <phiên bản> --runner-vendor openai --skills-discovered 13 \
  --offline-how "<cách đã tắt web>"
python tests/run_integrity.py tests/runs/2026-11-05-round5
```
Lỗi `host` và `runner` sẽ hết. Bước chấm (người chấm khác hãng) và điền `grader` làm sau, rồi tạo `results.json` cho vòng này.

## Lưu ý trung thực
Kết quả vẫn là sơ bộ nếu chưa có luật sư và ca live có đáp án (mục 4, 6). Nếu host không xuất được transcript nguyên bản hoặc không tắt được web bằng kỹ thuật thì ca đó không đạt mục 1-2; ghi rõ, không điền thay.
