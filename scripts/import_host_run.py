#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Protocol v2: build a run folder from the raw transcripts exported by the host (for example Codex).

  python scripts/import_host_run.py prepare  --run tests/runs/2026-11-05-round5
  python scripts/import_host_run.py import   --run tests/runs/2026-11-05-round5 --transcripts <folder> \
        --host-name Codex --host-version X --runner-vendor openai --skills-discovered 13 [--model-id ID]

<folder> contains <CASE_ID>.jsonl (the raw rollout/transcript, unedited).
The script does not grade: it only builds prompt/answer/evidence/manifest (a grader from a different vendor does the grading afterwards).
"""
import argparse, json, hashlib, shutil, sys, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
cases = {c["id"]: c for c in json.load(open(ROOT / "tests/cases.json", encoding="utf-8"))}
ZIP = next(iter(sorted((ROOT / "dist").glob("Vietnam-Legal-Advisor-*.zip"))[-1:]), None)

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def walk(o):
    if isinstance(o, dict):
        yield o
        for v in o.values(): yield from walk(v)
    elif isinstance(o, list):
        for v in o: yield from walk(v)

def parse(path):
    """Extract the model, tool calls and the last assistant message from a transcript (Codex rollout format or similar)."""
    models, tools, last, first_ts = set(), [], "", None
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line: continue
        try: e = json.loads(line)
        except ValueError: continue
        first_ts = first_ts or e.get("timestamp")
        for d in walk(e):
            if isinstance(d.get("model"), str): models.add(d["model"])
            t = d.get("type", "")
            if t in ("function_call", "tool_use", "custom_tool_call", "local_shell_call", "web_search_call"):
                tools.append(d.get("name") or t)
            if d.get("role") == "assistant" and isinstance(d.get("content"), list):
                txt = "".join(c.get("text", "") for c in d["content"] if isinstance(c, dict) and c.get("type") in ("output_text", "text"))
                if txt.strip(): last = txt
    return models, tools, last, first_ts

def prepare(a):
    run = ROOT / a.run; (run / "prompts").mkdir(parents=True, exist_ok=True)
    for cid, c in cases.items():
        (run / "prompts" / f"{cid}.txt").write_text(c["prompt"] + "\n", encoding="utf-8")
    if ZIP: shutil.copy(ZIP, run / ZIP.name)
    print(f"Created {len(cases)} prompts at {run/'prompts'} and copied {ZIP.name if ZIP else '(no ZIP)'}")

def do_import(a):
    run = ROOT / a.run; tdir = Path(a.transcripts)
    missing = [c for c in cases if not (tdir / f"{c}.jsonl").exists()]
    if missing: sys.exit(f"Missing transcripts: {missing}")
    if not ZIP: sys.exit("No ZIP in dist/")
    shutil.copy(ZIP, run / ZIP.name)
    man_t, all_models, summary = {}, set(), {}
    for cid, c in cases.items():
        ev = run / "evidence" / cid; ev.mkdir(parents=True, exist_ok=True)
        shutil.copy(tdir / f"{cid}.jsonl", ev / "transcript.jsonl")
        models, tools, last, ts = parse(ev / "transcript.jsonl")
        (ev / "prompt.txt").write_text(c["prompt"] + "\n", encoding="utf-8")
        (ev / "answer.md").write_text(last + "\n", encoding="utf-8")
        (ev / "tool_calls.md").write_text("# Tool calls (extracted from the raw transcript)\n\n" + ("\n".join(f"{i}. {t}" for i, t in enumerate(tools, 1)) or "(none)") + "\n", encoding="utf-8")
        json.dump({"test_id": cid, "models_in_transcript": sorted(models), "tools_called": tools, "transcript_sha256": sha(ev / "transcript.jsonl"), "answer_empty": not last.strip()}, open(ev / "evidence.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        man_t[cid] = {"path": f"evidence/{cid}/transcript.jsonl", "sha256": sha(ev / "transcript.jsonl")}
        all_models |= models; summary[cid] = (sorted(models), tools, bool(last.strip()))
    model = a.model_id or ("; ".join(sorted(all_models)) if all_models else "")
    man = {"protocol": "v2", "round": a.round, "candidate_version": ZIP.stem.split("-")[-1], "candidate_zip_sha256": sha(ZIP),
           "started_at": datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
           "host": {"name": a.host_name, "version": a.host_version, "production_host": True, "plugin_installed_via_host": True, "skills_discovered": a.skills_discovered},
           "runner": {"vendor": a.runner_vendor, "model_id": model},
           "tool_policy": {"offline_enforced": "technical", "how": a.offline_how, "document_only_files": ["tests/fixtures.md"]},
           "grader": {"kind": "ai", "vendor": "<fill in after grading: must differ from the runner>", "model_id": "<fill in later>"},
           "answer_key": {"applies_to": [], "reviewed_on": None, "sources": []}, "transcripts": man_t}
    json.dump(man, open(run / "run_manifest.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    bad = [c for c, (m, t, ok) in summary.items() if not ok or not m]
    net = [c for c, (m, t, ok) in summary.items() if any(x in ("web_search_call", "web_search", "WebSearch", "WebFetch") for x in t)]
    print(f"Imported {len(cases)} transcripts. Model: {model or 'NOT FOUND - use --model-id'}")
    if bad: print("WARNING missing answer/model in:", bad)
    if net: print("WARNING network calls in:", net)

ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="cmd", required=True)
p = sp.add_parser("prepare"); p.add_argument("--run", required=True); p.set_defaults(f=prepare)
i = sp.add_parser("import"); i.add_argument("--run", required=True); i.add_argument("--transcripts", required=True)
i.add_argument("--host-name", required=True); i.add_argument("--host-version", required=True)
i.add_argument("--runner-vendor", required=True); i.add_argument("--skills-discovered", type=int, required=True)
i.add_argument("--model-id", default=""); i.add_argument("--round", type=int, default=5)
i.add_argument("--offline-how", default="The session had no web/browsing tools enabled (see HOST_RUNBOOK.md)."); i.set_defaults(f=do_import)
a = ap.parse_args(); a.f(a)
