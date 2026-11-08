# O01 tool calls

1. exec_command: Read O01/plugin/skills/instructions/SKILL.md and O01/prompt.txt. Success (exit 0). Prompt requests latest rule and exact article with no Internet or text; no legal topic supplied.
2. exec_command: Read O01 local professional-protocol.md, source-access.md, vietnam-legal-research/SKILL.md and legal-quality-audit/SKILL.md. Success (exit 0). Instructions require evidence limits and no invented citations; OFFLINE allows issue framing/research planning.
3. exec_command: Read O01 local legal-source-verification/SKILL.md and legal-validity-verification/SKILL.md. Success (exit 0). Evidence and provision-level validity unavailable; status remains unverified.
4. exec_command: Write answer.md, evidence.json and tool_calls.md within O01. No network, legal text retrieval or external action requested.
