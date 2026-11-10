# Third-Party Notices

Updated 2026-11-10; approved by the Publisher. This is not a legal confirmation.

## Dependencies

None. The scripts use only the Python standard library (the Pillow dependency of `scripts/validate.py` was removed on 2026-11-10).

## Screening result for `plugin/`

A search of `plugin/` for the keywords copyright, license, "third-party" and "©" returned only one ordinary legal phrase in `investment-and-ma/SKILL.md` ("third-party consents") and the logo image file. No code or text carrying another license notice was found. This is a keyword screen, not a content review.

## Items not yet confirmed (the Publisher needs to answer)

1. **Logo** `vietnam-legal-advisor-icon-v4.png`: details of origin, prompt, personal account in Vietnam, and the OpenAI terms of 2026-10-16 (Wayback copy with hash) are in [PROVENANCE-LOGO.md](PROVENANCE-LOGO.md). Created by GPT-6 Astra through OpenAI's ChatGPT. Licensed under CC BY 4.0 to the extent the Publisher holds rights.
2. **AI-assisted content**: the plugin is packaged for platforms with a `com.openai` manifest, and the test runs used Codex subagents. The model providers' terms on rights in output need to be confirmed when sublicensing.
3. **Vietnamese legal texts**: the plugin does not package legal texts (`knowledge-index.json` is empty). If any are packaged later, the current rules on copyright in normative legal documents must be verified before any status is asserted.
4. **Test evidence** (`tests/runs/`): contains model output and zip packages; licensed under CC BY 4.0 to the extent the Publisher holds rights.

## Code review (2026-11-04)

Read in full: `scripts/validate.py` (189 lines), `scripts/package.py` (49), `tests/run_technical.py` (52) and `tests/validate.py` (6), written by ChatGPT/Codex under the Publisher's direction. Result:

- Uses only the Python standard library and Pillow (through its public API). The logic is tightly bound to the project structure (13 skills, 22 test cases, manifests, package SHA-256).
- There are two common techniques, both ordinary idioms: opening an image with Pillow, calling `verify()` and reloading to check a PNG; and packaging a ZIP with a fixed timestamp (1980-01-01) and fixed file permissions so the ZIP is reproducible.
- No copyright headers, license notes, other author names or code that looks copied wholesale were found.

Since this review, `tests/run_technical.py`, `tests/validate.py` and the Pillow-based image check were removed (2026-11-10); the review above describes the files as they were on 2026-11-04.

Limitation: this was a manual read, without an open-source code-matching tool. It cannot prove there is no coincidence; it shows only that there is no obvious sign. Code written by Claude (`tests/run_integrity.py`, `scripts/import_host_run.py`, and the 2026-11-10 simplification of `scripts/validate.py`) is not part of this review and is declared in `PROVENANCE-AI-CONTENT.md`.

## License texts reproduced verbatim

- `LICENSE-Apache-2.0.txt`: the version from the Debian `common-licenses` package, SHA-256 `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30`.
- `LICENSE-CC-BY-4.0.txt`: the version from the `spdx/license-list-data` repository, SHA-256 `d557539df68e771cc1eedcc91d13f70fca930e508d11eedcafa4b15db49e3744`.
