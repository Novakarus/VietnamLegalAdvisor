#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Check the integrity of a behavioral test run against Protocol v2.

Usage:
    python tests/run_integrity.py tests/runs/2026-10-21-round3
    python tests/run_integrity.py <run_dir> --json

Read-only. It checks the evidence that accompanies a run; it does NOT check legal correctness.
Exit code 0 if there are no errors (FAIL), 1 if there is at least one error.

If run_manifest.json is absent (old rounds), the script infers information from results.json and marks
anything it cannot prove as FAIL instead of assuming a pass.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

REQUIRED_CASE_FILES = ["prompt.txt", "answer.md", "evidence.json", "tool_calls.md"]
NETWORK_HINTS = re.compile(r"(https?://|\bcurl\b|\bwget\b|\bbrows(e|ing)\b|web[._ ]?search|\bfetch\b|\bsearch\b)", re.I)
NEGATION = re.compile(r"\b(no|not|never|without|prohibited|disabled|không)\b", re.I)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def vendor(name: str) -> str:
    n = (name or "").lower()
    for key in ("codex", "openai", "gpt", "claude", "anthropic", "gemini", "google"):
        if key in n:
            return {"gpt": "openai", "codex": "openai", "claude": "anthropic", "gemini": "google"}.get(key, key)
    return n.strip() or "unknown"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run_dir")
    ap.add_argument("--json", action="store_true", help="print the result as JSON")
    ap.add_argument("--formal", action="store_true", help="also check the formal acceptance conditions (lawyer, real host)")
    args = ap.parse_args()

    run = Path(args.run_dir).resolve()
    findings = []  # (level, scope, message)

    def add(level, scope, msg):
        findings.append({"level": level, "scope": scope, "message": msg})

    if not run.is_dir():
        print(f"Folder not found: {run}", file=sys.stderr)
        return 2

    manifest = load(run / "run_manifest.json")
    results = load(run / "results.json") or {}
    legacy = manifest is None
    if legacy:
        add("FAIL", "run", "run_manifest.json is missing (Protocol v2). Model, host and tool-policy information can only be inferred from results.json.")

    cases = results.get("cases", [])
    if not cases:
        add("FAIL", "run", "results.json cannot be read or has no cases.")

    # Runner / grader
    if manifest:
        runner = manifest.get("runner", {})
        grader = manifest.get("grader", {})
        policy = manifest.get("tool_policy", {})
        host = manifest.get("host", {})
    else:
        models = {c.get("model", "") for c in cases}
        reviewers = {c.get("reviewer", "") for c in cases}
        runner = {"model_id": "; ".join(sorted(models)), "vendor": vendor(" ".join(models))}
        grader = {"model_id": "; ".join(sorted(reviewers)), "vendor": vendor(" ".join(reviewers)), "kind": "ai"}
        policy = {"offline_enforced": "instruction" if any("prohibited by test instructions" in s for s in results.get("limitations", [])) else "unknown"}
        host = {"production_host": False}

    if not runner.get("model_id") or "unknown" in str(runner.get("model_id")).lower() or "unavailable" in str(runner.get("model_id")).lower():
        add("FAIL", "runner", "There is no exact model identifier for the test runner.")
    if vendor(runner.get("vendor") or runner.get("model_id", "")) == vendor(grader.get("vendor") or grader.get("model_id", "")):
        add("FAIL", "grader", f"The grader is from the same model family as the runner ({vendor(grader.get('vendor') or grader.get('model_id',''))}). Protocol v2 requires a grader from a different model family.")
    if policy.get("offline_enforced") != "technical":
        add("FAIL", "offline", f"OFFLINE cases were not blocked technically (offline_enforced={policy.get('offline_enforced')!r}).")
    if not host.get("production_host"):
        add("FAIL", "host", "Not run on a real host with the plugin installed (production_host=false).")

    # Candidate hash
    expected = results.get("candidate_zip_sha256") or (manifest or {}).get("candidate_zip_sha256")
    zips = sorted(run.glob("Vietnam-Legal-Advisor-*.zip"))
    if not zips:
        add("FAIL", "candidate", "There is no candidate ZIP file in the run folder.")
    else:
        actual = sha256(zips[0])
        if actual != expected:
            add("FAIL", "candidate", f"The SHA-256 of {zips[0].name} ({actual[:12]}…) differs from the record ({str(expected)[:12]}…).")

    # Per-case files
    ev_root = run / "evidence"
    transcripts = (manifest or {}).get("transcripts", {})
    for c in cases:
        cid = c.get("case_id")
        d = ev_root / str(cid)
        for name in REQUIRED_CASE_FILES:
            f = d / name
            if not f.is_file() or f.stat().st_size == 0:
                if not (name == "fixtures.md"):
                    add("FAIL", cid, f"Missing or empty: evidence/{cid}/{name}")
        ev = load(d / "evidence.json") or {}
        if "unknown" in str(ev.get("model", "")).lower():
            add("FAIL", cid, "evidence.json records the model as unknown.")
        # transcript
        t = transcripts.get(cid)
        if not t:
            add("FAIL", cid, "There is no raw transcript (transcript.jsonl) in the manifest. tool_calls.md is a summary written by the running session itself.")
        else:
            tp = run / t.get("path", "")
            if not tp.is_file():
                add("FAIL", cid, f"Transcript does not exist: {t.get('path')}")
            elif sha256(tp) != t.get("sha256"):
                add("FAIL", cid, "The transcript SHA-256 does not match the manifest.")
        # offline tool-call scan (heuristic)
        if str(c.get("tool_mode")).upper() == "OFFLINE":
            log = d / "tool_calls.md"
            if log.is_file():
                for i, line in enumerate(log.read_text(encoding="utf-8").splitlines(), 1):
                    if re.match(r"\s*\d+\.", line) and NETWORK_HINTS.search(line) and not NEGATION.search(line):
                        add("WARN", cid, f"tool_calls.md line {i} shows signs of external retrieval in an OFFLINE case: {line.strip()[:120]}")

    if args.formal:
        if grader.get("kind") != "human_lawyer":
            add("FAIL", "formal", "Formal acceptance needs a grader who is a lawyer with the relevant expertise (grader.kind=human_lawyer).")
        if not (manifest or {}).get("answer_key", {}).get("reviewed_on"):
            add("FAIL", "formal", "Missing an answer key written by a lawyer with a review date (answer_key.reviewed_on).")

    fails = [f for f in findings if f["level"] == "FAIL"]
    warns = [f for f in findings if f["level"] == "WARN"]
    summary = {"run_dir": str(run), "protocol": "v2", "legacy_without_manifest": legacy,
               "cases_checked": len(cases), "fail": len(fails), "warn": len(warns),
               "status": "PASS" if not fails else "FAIL", "findings": findings}
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(f"Protocol v2 — {run.name}: {summary['status']} ({len(fails)} errors, {len(warns)} warnings, {len(cases)} cases)")
        seen = set()
        for f in findings:
            key = (f["level"], f["message"].split(':')[0][:60], f["scope"] if f["scope"] not in {c.get('case_id') for c in cases} else "case")
            if f["scope"] in {c.get("case_id") for c in cases}:
                if key in seen:
                    continue
                seen.add(key)
                print(f"  [{f['level']}] (all cases, e.g. {f['scope']}) {f['message']}")
            else:
                print(f"  [{f['level']}] ({f['scope']}) {f['message']}")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
