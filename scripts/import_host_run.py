#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Protocol v2: dựng thư mục lượt chạy từ transcript nguyên bản do host (ví dụ Codex) xuất ra.

  python scripts/import_host_run.py prepare  --run tests/runs/2026-11-05-round5
  python scripts/import_host_run.py import   --run tests/runs/2026-11-05-round5 --transcripts <thư_mục> \
        --host-name Codex --host-version X --runner-vendor openai --skills-discovered 13 [--model-id ID]

<thư_mục> chứa <CASE_ID>.jsonl (rollout/transcript nguyên bản, không chỉnh sửa).
Script không chấm điểm: chỉ dựng prompt/answer/evidence/manifest (người chấm khác hãng thực hiện sau).
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
    """Trích model, lời gọi công cụ, tin nhắn assistant cuối từ transcript (định dạng Codex rollout hoặc tương tự)."""
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
    print(f"Đã tạo {len(cases)} prompt tại {run/'prompts'} và sao chép {ZIP.name if ZIP else '(không có ZIP)'}")

def do_import(a):
    run = ROOT / a.run; tdir = Path(a.transcripts)
    missing = [c for c in cases if not (tdir / f"{c}.jsonl").exists()]
    if missing: sys.exit(f"Thiếu transcript: {missing}")
    if not ZIP: sys.exit("Thiếu ZIP trong dist/")
    shutil.copy(ZIP, run / ZIP.name)
    man_t, all_models, summary = {}, set(), {}
    for cid, c in cases.items():
        ev = run / "evidence" / cid; ev.mkdir(parents=True, exist_ok=True)
        shutil.copy(tdir / f"{cid}.jsonl", ev / "transcript.jsonl")
        models, tools, last, ts = parse(ev / "transcript.jsonl")
        (ev / "prompt.txt").write_text(c["prompt"] + "\n", encoding="utf-8")
        (ev / "answer.md").write_text(last + "\n", encoding="utf-8")
        (ev / "tool_calls.md").write_text("# Tool calls (trích từ transcript nguyên bản)\n\n" + ("\n".join(f"{i}. {t}" for i, t in enumerate(tools, 1)) or "(không có)") + "\n", encoding="utf-8")
        json.dump({"test_id": cid, "models_in_transcript": sorted(models), "tools_called": tools, "transcript_sha256": sha(ev / "transcript.jsonl"), "answer_empty": not last.strip()}, open(ev / "evidence.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        man_t[cid] = {"path": f"evidence/{cid}/transcript.jsonl", "sha256": sha(ev / "transcript.jsonl")}
        all_models |= models; summary[cid] = (sorted(models), tools, bool(last.strip()))
    model = a.model_id or ("; ".join(sorted(all_models)) if all_models else "")
    man = {"protocol": "v2", "round": a.round, "candidate_version": ZIP.stem.split("-")[-1], "candidate_zip_sha256": sha(ZIP),
           "started_at": datetime.datetime.now().astimezone().replace(microsecond=0).isoformat(),
           "host": {"name": a.host_name, "version": a.host_version, "production_host": True, "plugin_installed_via_host": True, "skills_discovered": a.skills_discovered},
           "runner": {"vendor": a.runner_vendor, "model_id": model},
           "tool_policy": {"offline_enforced": "technical", "how": a.offline_how, "document_only_files": ["tests/fixtures.md"]},
           "grader": {"kind": "ai", "vendor": "<điền sau khi chấm: phải khác runner>", "model_id": "<điền sau>"},
           "answer_key": {"applies_to": [], "reviewed_on": None, "sources": []}, "transcripts": man_t}
    json.dump(man, open(run / "run_manifest.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    bad = [c for c, (m, t, ok) in summary.items() if not ok or not m]
    net = [c for c, (m, t, ok) in summary.items() if any(x in ("web_search_call", "web_search", "WebSearch", "WebFetch") for x in t)]
    print(f"Đã nhập {len(cases)} transcript. Mô hình: {model or 'KHÔNG TÌM THẤY - dùng --model-id'}")
    if bad: print("CẢNH BÁO thiếu answer/model ở:", bad)
    if net: print("CẢNH BÁO có lời gọi mạng ở:", net)

ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="cmd", required=True)
p = sp.add_parser("prepare"); p.add_argument("--run", required=True); p.set_defaults(f=prepare)
i = sp.add_parser("import"); i.add_argument("--run", required=True); i.add_argument("--transcripts", required=True)
i.add_argument("--host-name", required=True); i.add_argument("--host-version", required=True)
i.add_argument("--runner-vendor", required=True); i.add_argument("--skills-discovered", type=int, required=True)
i.add_argument("--model-id", default=""); i.add_argument("--round", type=int, default=5)
i.add_argument("--offline-how", default="Phiên chạy không bật công cụ web/duyệt web (xem HOST_RUNBOOK.md)."); i.set_defaults(f=do_import)
a = ap.parse_args(); a.f(a)
