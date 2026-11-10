# Runbook: run the 22 cases on a real host (Protocol v2, items 1, 2, 3, 5)

Goal: fix the `host` error (production_host=false). The plugin is in Codex/OpenAI format (root `plugin.json` with `extensions.com.openai`), so the target host is **Codex** (app/CLI/IDE). Runner = OpenAI; the grader must be from a different vendor (Claude or a lawyer) to fix the `grader` error.

## Preparation
1. `python scripts/import_host_run.py prepare --run tests/runs/2026-11-05-round5` → creates `prompts/<ID>.txt` and copies the candidate ZIP.
2. Unzip the **current** candidate ZIP (the file in `dist/`; its SHA-256 is in `tests/results.json` under `post_test_changes.current_zip_sha256`) and install it in Codex through the host's plugin mechanism. Do not edit the plugin files. If `plugin/` changes again, repackage and use the new hash for the whole round.
3. In Codex: confirm that the host lists all **13 skills** (screenshot or export the list). Record the host name and version (`codex --version` or the About screen).

## Each case (22 cases)
- Open a **new session** (do not share context), configured with **no web tools**: turn off web search and give the sandbox no network (for example `web_search = "disabled"` / a sandbox without network). Record how it was turned off to fill in `--offline-how`.
- Paste the content of `prompts/<ID>.txt` as is. Do not paste `must_include`/`must_not`.
- Cases R02, C01, D01, V01 and V02 refer to `tests/fixtures.md`: provide only this file (placed in the working directory); give the other cases no additional documents.
- Do not edit or repeat the question. One session per case.

## Export the transcripts
Take the host's raw session file (for the Codex CLI/app usually `~/.codex/sessions/<year>/<month>/<day>/rollout-*.jsonl`). Rename each file to `<ID>.jsonl` in one folder (for example `transcripts/`). Do not open and re-save it in an editor.

## Import and check
```
python scripts/import_host_run.py import --run tests/runs/2026-11-05-round5 --transcripts transcripts \
  --host-name Codex --host-version <version> --runner-vendor openai --skills-discovered 13 \
  --offline-how "<how web was turned off>"
python tests/run_integrity.py tests/runs/2026-11-05-round5
```
The `host` and `runner` errors should disappear. Grading (a grader from a different vendor) and filling in `grader` come afterwards, then create the `results.json` for this round.

## Honesty note
The result is still preliminary without a lawyer and live cases with answer keys (items 4 and 6). If the host cannot export a raw transcript or web cannot be turned off technically, that case does not meet items 1–2; record this plainly and do not fill it in.
