# Actual tool calls

1. functions.exec -> exec_command (PowerShell): read plugin/skills/instructions/SKILL.md and prompt.txt. Result: router and one-sentence request returned; no draft supplied.
2. functions.exec -> exec_command (PowerShell): read professional-protocol.md, source-access.md, and opposing-counsel-review/SKILL.md. Result: shared evidence requirements and conditional hypothesis/evidence-map workflow returned.
3. functions.exec -> exec_command (PowerShell): read legal-quality-audit/SKILL.md. Result: LIMITED-output audit requirements returned and applied to the answer.
4. functions.exec -> exec_command (PowerShell): save answer.md, evidence.json, tool_calls.md in the authorized A01 session directory. This is a request/result summary, not raw telemetry.

No network, other directories, external actions, scheduling, or agents used. Source and validity specialist files were not read: no specific legal authority or legal conclusion was asserted in the missing-draft hypothesis map.
