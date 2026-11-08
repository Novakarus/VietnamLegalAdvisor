#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Kiểm tra STATUS.md, manifest, release.json, tests/results.json và README khớp nhau.

Dùng: python scripts/check_consistency.py
Mã thoát 0 nếu khớp, 1 nếu có sai lệch. Chỉ đọc, không sửa file.
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
    need(bool(status), "Thiếu STATUS.md")
    s_ver = field(status, "Phiên bản hiện hành")
    s_state = field(status, "Trạng thái")
    s_public = field(status, "Sẵn sàng phát hành công khai")

    manifest = read_json(ROOT / "plugin/plugin.json")
    legacy = read_json(ROOT / "plugin/.codex-plugin/plugin.json")
    ver = manifest["version"]
    need(legacy["version"] == ver, f"Hai manifest khác phiên bản: {ver} vs {legacy['version']}")
    need(s_ver == ver, f"STATUS.md ghi phiên bản {s_ver}, manifest là {ver}")

    results = read_json(ROOT / "tests/results.json")
    need(results.get("candidate") == ver, f"tests/results.json candidate={results.get('candidate')} khác {ver}")

    rel_dir = ROOT / "releases" / ver
    rj = rel_dir / "release.json"
    if rj.is_file():
        rel = read_json(rj)
        need(rel.get("version") == ver, "release.json khác phiên bản")
        need(rel.get("status") == s_state, f"release.json status={rel.get('status')} khác STATUS.md ({s_state})")
        need((s_public == "không") == (rel.get("public_release_ready") is False), "public_release_ready không khớp STATUS.md")
        zp = rel_dir / rel.get("candidate_zip", "")
        if zp.is_file():
            actual = hashlib.sha256(zp.read_bytes()).hexdigest()
            need(actual == rel.get("candidate_zip_sha256"), "SHA-256 ZIP đóng băng khác release.json")
            need(actual == results.get("candidate_zip_sha256"), "SHA-256 ZIP khác tests/results.json")
        else:
            need(False, "Không thấy ZIP đóng băng trong releases/")
    else:
        need(s_state not in {"FROZEN_LOCAL_RELEASE_CANDIDATE", "ACCEPTED", "RELEASED"}, "Trạng thái yêu cầu release.json nhưng không có")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    need(ver in readme.splitlines()[0], "Tiêu đề README không chứa phiên bản hiện hành")
    need("STATUS.md" in readme, "README chưa trỏ tới STATUS.md")

    for p in sorted(ROOT.glob("CHANGES-*.md")):
        need(p.read_text(encoding="utf-8").startswith("> **LỊCH SỬ"), f"{p.name} thiếu cảnh báo lịch sử")

    for p in ["LICENSE.md", "LICENSE-Apache-2.0.txt", "NOTICE", "THIRD_PARTY_NOTICES.md"]:
        need((ROOT / p).is_file(), f"Thiếu {p}")

    if problems:
        print("KHÔNG KHỚP:")
        for m in problems:
            print("  - " + m)
        return 1
    print(f"Khớp: phiên bản {ver}, trạng thái {s_state}, công khai: {s_public}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
