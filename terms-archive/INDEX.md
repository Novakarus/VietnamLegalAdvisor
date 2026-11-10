# Index of Related Terms

This folder holds copies of third-party terms relevant to the provenance of, and rights in, the project's content. The PDF files are the copyright of the owners of the terms; they are kept **locally only** as evidence and are excluded from Git by `.gitignore` (only `INDEX.md` is pushed to Git). Updated 2026-11-04. Note: the file `openai-terms-2026-01-01.pdf` is the Terms of Use (effective 2026-01-01, Wayback capture of 2026-10-16); `openai-terms-2026-10-16.pdf` is the Service Terms (update date 2026-10-16).

## Stored

| File | Source | Version and time | SHA-256 | Used for |
|---|---|---|---|---|
| `openai-terms-2026-01-01.pdf` (12 pages) | Wayback Machine: https://web.archive.org/web/20261016141108/https://openai.com/policies/terms-of-use/ | OpenAI Terms of Use, Published and Effective 2026-01-01, capture taken 2026-10-16 14:11:08 UTC; printed to PDF by the Publisher on 2026-11-04 | `83e1e2b8e0d277fb9ebfaa1dced2b6d280aa0a042cdd51ace43d4457e1bafb3a` | Rights in ChatGPT Output (the logo, content drafted with ChatGPT/Codex). See `PROVENANCE.md` |
| `openai-terms-2026-10-16.pdf` (10 pages) | https://openai.com/policies/service-terms/ (printed from the official page 2026-11-04 19:35 Vietnam time) | OpenAI **Service Terms**, the page reads "Updated: October 16, 2026" (exactly the logo's reference date) | `c95c3001d8a56c5cacdb53fbab9054033ca65748b10295378f9ce88cd83678c2` | Section 4 "Codex and Code Generation": Output of code generation features, including OpenAI Codex, may be subject to third-party licenses, including open source |
| `anthropic-terms.pdf` (14 pages) | https://www.anthropic.com/legal/consumer-terms (PDF) | Consumer Terms of Service, Effective Oct 8, 2025, saved 2026-11-04 | `7222642462bf559fa450982aa75ad4c7d3c1ed5c24e6e1517d7b4cf9f22806d4` | Claude Pro account; rights in the Output of files drafted by Claude |

## Not stored

| Terms | Suggested source | Why needed | Note |
|---|---|---|---|
| Apache 2.0 and CC BY 4.0 licenses | Already in the root directory (`LICENSE-Apache-2.0.txt`, `LICENSE-CC-BY-4.0.txt`) | The project's licenses | Not part of this archive because they are already part of the project's license |

## Rules

1. Name each file `<provider>-<terms-type>-<effective-date-or-save-date>.pdf` and add a new row to the "Stored" table with its SHA-256.
2. Prefer a dated capture (Wayback) or a PDF printed from the official page, with the URL and download date.
3. Do not push the PDFs to the public repository. If proof is needed later, keep the original file outside Git and use the SHA-256 in this table.
