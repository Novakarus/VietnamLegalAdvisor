# Actual tool calls

1. functions.exec → exec_command: read plugin/skills/instructions/SKILL.md and prompt.txt; list local plugin/skills. Result: router and prompt read successfully; specialist names observed.
2. functions.exec → exec_command: read shared professional-protocol and source-access plus corporate-governance, legal-document-drafting, legal-source-verification, legal-validity-verification and legal-quality-audit SKILL.md. Result: all local instructions read successfully. No legal source retrieved.
3. functions.exec → exec_command: save answer.md, evidence.json and this tool_calls.md in the G01 session. Result: files written.
4. functions.exec → exec_command: confirm the three output files and parse evidence.json. Result recorded by completion check.

Only session-local files accessed. No network, external action, scheduler, agent, test/history access or candidate edit. Source and temporal verification remained unresolved; audit returned LIMITED with a usable conditional draft.
