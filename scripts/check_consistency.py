#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Check that STATUS.md, the manifests, release.json, tests/results.json and the README agree.

Usage: python scripts/check_consistency.py
Exit code 0 if they agree, 1 if there is a discrepancy. Read-only; it does not modify files.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_json(p):
    return json.loads(p.read_text(encoding="utf-8"))


def field(text, label):
    m = re.search(r"^" + re.escape(label) + r":\s*(.+?)\s*$", text, re.M)
    return m.group(1) if m else None


def main():
    problems = []

    def need(cond, msg):
        if not cond:
            problems.append(msg)

    status = (ROOT / "STATUS.md").read_text(encoding="utf-8") if (ROOT / "STATUS.md").is_file() else ""
    need(bool(status), "STATUS.md is missing")
    s_ver = field(status, "Current version")
    s_state = field(status, "Status")
    s_public = field(status, "Ready for public release")

    manifest = read_json(ROOT / "plugin/plugin.json")
    legacy = read_json(ROOT / "plugin/.codex-plugin/plugin.json")
    ver = manifest["version"]
    need(legacy["version"] == ver, f"The two manifests have different versions: {ver} vs {legacy['version']}")
    need(s_ver == ver, f"STATUS.md records version {s_ver}, the manifest says {ver}")

    results = read_json(ROOT / "tests/results.json")
    need(results.get("candidate") == ver, f"tests/results.json candidate={results.get('candidate')} differs from {ver}")

    rel_dir = ROOT / "releases" / ver
    rj = rel_dir / "release.json"
    if rj.is_file():
        rel = read_json(rj)
        need(rel.get("version") == ver, "release.json has a different version")
        need(rel.get("status") == s_state, f"release.json status={rel.get('status')} differs from STATUS.md ({s_state})")
        need((s_public == "no") == (rel.get("public_release_ready") is False), "public_release_ready does not match STATUS.md")
        zp = rel_dir / rel.get("candidate_zip", "")
        if zp.is_file():
            actual = hashlib.sha256(zp.read_bytes()).hexdigest()
            need(actual == rel.get("candidate_zip_sha256"), "The frozen ZIP SHA-256 differs from release.json")
            need(actual == results.get("candidate_zip_sha256"), "The ZIP SHA-256 differs from tests/results.json")
        else:
            need(False, "No frozen ZIP found in releases/")
    else:
        need(s_state not in {"FROZEN_LOCAL_RELEASE_CANDIDATE", "ACCEPTED", "RELEASED"}, "The status requires release.json but it is absent")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    need(ver in readme.splitlines()[0], "The README title does not contain the current version")
    need("STATUS.md" in readme, "The README does not point to STATUS.md")

    for p in sorted((ROOT / "history").glob("CHANGES-*.md")):
        need(p.read_text(encoding="utf-8").startswith("> **HISTORY"), f"{p.name} is missing the history warning")

    for p in ["LICENSE.md", "LICENSE-Apache-2.0.txt", "NOTICE", "THIRD_PARTY_NOTICES.md"]:
        need((ROOT / p).is_file(), f"{p} is missing")

    if problems:
        print("MISMATCH:")
        for m in problems:
            print("  - " + m)
        return 1
    print(f"Consistent: version {ver}, status {s_state}, public: {s_public}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
