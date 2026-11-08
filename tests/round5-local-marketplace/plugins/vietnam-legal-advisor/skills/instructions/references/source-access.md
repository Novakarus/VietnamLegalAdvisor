# Source access adapter

This is a capability-aware workflow, not a deployed connector. No MCP endpoint, API key, automatic synchronization or scheduler is packaged.

1. At task start inspect actually callable Search, browsing or approved MCP tools. Record provider, time and mode: LIVE / DOCUMENT_ONLY / OFFLINE.
2. For LIVE mode search official domains first using exact identifiers plus amendments, repeal and transitional terms. Open actual documents and attachments. Inspect scans/OCR for quotation accuracy; use visual checks for decisive passages if possible.
3. For each claim populate the evidence and applicability ledgers in professional-protocol.md. Home-page reachability never proves completeness, current validity or retrieval of a particular law.
4. If access fails, try another official publication channel or issuing authority. Secondary sources can identify leads. If no operative primary text can be retrieved, mark the result provisional and say exactly what is missing.
5. In DOCUMENT_ONLY mode cite file/page and supplied version; do not claim public authenticity, completeness or current status. In OFFLINE mode provide issue spotting or a draft structure as useful and an actionable research plan without invented citations. State the next steps now: define issue/jurisdiction/dates; obtain official original text; inspect relevant provisions, amendments, repeal and transition; assess provision-level applicability; record evidence and unresolved status. Missing subject matter may leave terms and document identifiers blank, but must not reduce the answer to a promise to plan later. Distinguish these planned actions from actual retrieval.
6. No tool installation or fabricated server URL. A future MCP adapter needs a verified endpoint, supported transport/authentication, data permissions and tests for exact retrieval, pagination, amendments, dates, provenance, failure handling and confidential-query minimization before connection.
7. Recheck the relevant law at each new consequential matter or material date change. This is on-demand verification, not automatic updates.

Connection smoke check on 2026-10-16 (Asia/Bangkok): built-in browsing fetched https://vanban.chinhphu.vn/ and https://congbao.chinhphu.vn/ home pages; https://vbpl.vn/ returned 403. No statutory provision or complete retrieval chain was validated in that smoke check. Lawve was accessible as a read-only skill directory, not a Vietnamese legal database. These tools are available in the authoring session; availability in a future plugin session is not guaranteed.
