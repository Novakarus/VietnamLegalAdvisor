# Actual tool calls — Q01

1. functions.exec / tools.exec_command: read plugin/skills/instructions/SKILL.md and prompt.txt in the Q01 directory. Result: router instructions and single-sentence scenario retrieved successfully.
2. functions.exec / tools.exec_command: read shared professional-protocol.md, source-access.md, legal-quality-audit/SKILL.md and legal-source-verification/SKILL.md. Result: all four local files read successfully; selected source verification followed by quality audit.
3. functions.exec / tools.exec_command: wrote answer.md, evidence.json and tool_calls.md within Q01. Result: local deliverables created. No network, Search, external connector, scheduler or agent call occurred. The scenario's Search-unavailability statement was not an observed tool result.
