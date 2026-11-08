# C03 tool calls

1. functions.exec -> exec_command (cwd: C03): Get-ChildItem -Force; Get-Content -Raw plugin/skills/instructions/SKILL.md; Get-Content -Raw prompt.txt.
   Result: exit 0. Found plugin directory and prompt.txt; read router and sole supplied review request. No other test or payload file read.
2. functions.exec -> exec_command (cwd: C03): Get-Content -Raw for professional-protocol.md, source-access.md, vietnam-contract-review/SKILL.md, opposing-counsel-review/SKILL.md and legal-quality-audit/SKILL.md under plugin/skills.
   Result: exit 0. Read evidence boundaries, offline handling, contract redline, opposing review and audit instructions.
3. functions.exec -> exec_command (cwd: C03): Set-Content UTF-8 answer.md, evidence.json and tool_calls.md using literal here strings.
   Result: local deliverables written. No network calls, document transmission, external messaging, source retrieval or agent delegation.
