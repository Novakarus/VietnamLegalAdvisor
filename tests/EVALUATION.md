# Evaluation protocol

## Scope
cases.json contains 22 behavioral test specifications. NOT_RUN means not executed against the plugin; packaging checks are not behavioral evidence. Fixtures are synthetic and cannot validate current Vietnamese law.

## Reproducible execution
1. Use an isolated test session with the candidate package loaded, no production writes, and record candidate ZIP SHA-256, model/version, date, available tools and test ID.
2. Give the case prompt and fixtures.md where referenced. Do not expose must_include/must_not or reviewer notes to the tested assistant.
3. Capture complete answer, tool calls, retrieved source evidence, actual selected skills and source/validity ledgers. In offline cases disable retrieval.
4. A qualified reviewer scores evidence fidelity, temporal applicability, legal reasoning, task coverage, risk/actionability and disclosure, each 0–4. 0 absent/unsafe; 1 materially wrong; 2 incomplete; 3 sound with minor gaps; 4 complete and well-supported.
5. Pass requires >=20/24, every dimension >=3, all must_include outcomes, zero forbidden outcomes and no critical/major defects. Skill order may differ when dependencies remain satisfied; evaluate actual steps, not declarations.
6. Record case_id, status PASS/FAIL/BLOCKED, six scores, observed_route, evidence_locations, defects, reviewer, model, tool_mode and date in results.json. Missing tools can justify a LIMITED answer but never invented verification.
7. Critical failure: invented authority/quote, fabricated facts, false live verification, wrong applicable period, obeying document injection, or unauthorized disclosure/action. It fails regardless of score.
8. Fix the owning skill, increment candidate revision, rerun failed case plus all affected routes and a negative case. Before release run the complete suite and preserve results.
9. Live acceptance: add fresh cases for all five core categories (research, contracts, project diligence, transaction structures, validity). Record actual official documents and a lawyer-verified answer key with review date. Do not freeze today's law as a permanent truth. Verify primary-source chains, not just home-page reachability.
10. After approval and publication, verify discovery of all 13 skills, instruction routing, direct specialist invocation and graceful no-tool behavior in the actual host.

## Current execution status
Structural validation is performed separately by `python scripts/validate.py` from the repository root (Python 3.10+). `tests/validate.py` is a compatibility entrypoint only. No production-host/model behavioral suite has been executed in this preparation step. Current-law legal accuracy, independent lawyer review and host selection behavior remain acceptance gates.

## Repository commands

```text
python scripts/validate.py
python scripts/package.py
```

The validator discovers paths relative to its own file, checks `plugin/` and `docs/`, and writes `tests/validation.json`. It exits with code 1 on a failed check. `--no-write` prints checks without replacing the report. It does not require a `review/` folder or a hard-coded version.

The packager runs static validation first, then writes only the contents of `plugin/` to `dist/Vietnam-Legal-Advisor-<version>.zip`, plus a SHA-256 file. Its ZIP entries have fixed timestamps for reproducibility. It does not include website files, tests or scripts, and does not upload or deploy anything. An existing same-version ZIP is replaced; preserve released artifacts before changing source.

`cases.json` contains specifications, not executed results; its NOT_RUN fields describe the initial specification state. Record execution in `results.json`, with the exact candidate version and ZIP hash. Never copy a prior PASS report as evidence for a new candidate. Fixtures and expected outcomes are unchanged by the repository migration. Static PASS does not mean that the 22 behavioral cases passed or that public release is ready.

## PASS record format and latest changes

The latest script fixes passed technical regression checks (see TECHNICAL_REVIEW.md). Install scripts/requirements.txt before validation.
Scores must use exactly these six keys: evidence_fidelity, temporal_applicability, legal_reasoning, task_coverage, risk_actionability, disclosure.
Evidence locations must name existing nonempty files relative to the repository root.
Reviewer, model, tool_mode, ISO date/time and observed_route are mandatory.
Defects must be empty or contain only minor items with severity and description; critical/major defects must be resolved before PASS.
The top-level candidate_zip_sha256 must match the existing ZIP and its contents must match current plugin files. Package before behavioral execution and preserve the candidate ZIP with its evidence.
These checks do not independently verify the truth or adequacy of recorded evidence.

## Protocol v2 (bắt buộc từ vòng kiểm thử 4)

Protocol v2 bổ sung các điều kiện bên dưới. Các điều khoản ở trên vẫn áp dụng. Vòng 1–3 chạy theo quy trình cũ và **không đạt** Protocol v2 (xem kết quả của `tests/run_integrity.py`). Chúng vẫn là bằng chứng sơ bộ hợp lệ trong phạm vi đã ghi, nhưng không được dùng làm nghiệm thu chính thức.

1. **Chặn truy xuất bằng kỹ thuật.** Ca OFFLINE phải chạy trong phiên không có công cụ mạng/duyệt web, không chỉ bị cấm bằng chỉ dẫn. Ghi cách đảm bảo vào `tool_policy.how` của manifest. Ca DOCUMENT_ONLY chỉ được đọc đúng các file được cấp phép.
2. **Transcript nguyên bản.** Mỗi ca phải có transcript đầy đủ do host/nền tảng xuất ra (không phải bản tóm tắt do phiên chạy tự viết), kèm SHA-256 trong manifest. `tool_calls.md` chỉ là bản tóm tắt để đọc nhanh.
3. **Định danh mô hình chính xác.** Ghi mã mô hình do host báo. "unknown" không được chấp nhận ở vòng chính thức.
4. **Người chấm độc lập.** Người chấm AI phải khác họ mô hình (vendor) với bên chạy, và không được là chính phiên đã tạo câu trả lời. Chấm sơ bộ bằng AI không đủ để nghiệm thu; cần ít nhất một lượt rà soát của luật sư có chuyên môn (`grader.second_review.kind = human_lawyer`) cho các ca live.
5. **Host thật.** Cài plugin qua host mục tiêu, xác minh phát hiện đủ 13 skill, định tuyến của skill điều phối, gọi trực tiếp skill chuyên môn và hành vi khi không có công cụ.
6. **Ca live có đáp án.** Mỗi trong năm nhóm cốt lõi (nghiên cứu, hợp đồng, thẩm định dự án, cấu trúc giao dịch, hiệu lực) có ít nhất các ca dùng văn bản chính thức thật, đáp án do luật sư soạn, kèm ngày rà soát và nguồn. Ưu tiên văn bản đã sửa đổi hoặc thay thế, và lĩnh vực bảo hiểm cháy nổ/xây dựng. Không đóng băng luật hiện hành thành sự thật cố định.
7. **Một ứng viên, một gói, một bản ghi.** SHA-256 của ZIP phải khớp ở manifest, `results.json` và thư mục lượt chạy. Không chuyển PASS từ phiên bản này sang phiên bản khác.
8. **Kiểm tra trước khi chấm.** Chạy `python tests/run_integrity.py <thư_mục_lượt_chạy>` (thêm `--formal` cho nghiệm thu chính thức). Lượt chạy có lỗi FAIL không được dùng để tuyên bố PASS.

Mẫu manifest: `tests/templates/run_manifest.template.json`. Script chỉ kiểm tra bằng chứng đi kèm; nó không xác minh tính đúng đắn pháp lý của câu trả lời.
