# Upload and deployment guide

## GitHub source

Commit docs/, plugin/, tests/, scripts/, releases/, terms-archive/INDEX.md (the PDFs in terms-archive/ are excluded by .gitignore and must stay local), README.md, STATUS.md, DEPLOYMENT.md, LICENSE.md, LICENSE-Apache-2.0.txt, LICENSE-CC-BY-4.0.md, LICENSE-CC-BY-4.0.txt, NOTICE, THIRD_PARTY_NOTICES.md, PROVENANCE-LOGO.md, PROVENANCE-AI-CONTENT.md, CHANGES-*.md and .gitignore. Licenses are a draft pending publisher approval (see LICENSE.md section 3); do not push before that. The releases/0.69.3/ directory preserves the tested local candidate; dist/ remains disposable. Preserve hidden files: docs/.nojekyll and plugin/.codex-plugin/plugin.json. Git excludes dist/ and Python caches. Do not use a browser upload of the entire folder without excluding those generated files.

This layout contains complete plugin source. A public repository exposes the skills and manifests; GitHub Pages publishing only docs/ does not hide them. Use a private source repository plus a separate public website repository if source confidentiality is required. No repository visibility change is performed by these scripts.

## Verify and package

```text
python -m pip install -r scripts/requirements.txt
python scripts/validate.py
python tests/run_technical.py --work-dir <new-empty-directory-outside-repository>
python scripts/package.py
```

dist/Vietnam-Legal-Advisor-<version>.zip (current candidate 0.70.0; 0.69.3 is frozen in releases/0.69.3) and its .sha256 sidecar are local deployment artifacts, not website content. The ZIP contains the contents of plugin/, with both manifests and 13 skills. Packaging never deploys it. Preserve an accepted release before replacing a same-version ZIP.

For an eventual hosted update, first fetch the current remote release and use its guarded update workflow. Local cleanup does not delete retained remote files automatically: if the remote release contains assets/gpt-icon.png, assets/logo.png or assets/vietnam-legal-advisor-v4.png, explicitly remove those exact verified paths during the authorized update. Do not assume the local version or former release ID is the current remote state.

## Remaining acceptance gates

Current status is in STATUS.md (candidate 0.70.0, behavioral tests not yet run). Historical: 0.69.3 is locally frozen against round-3 evidence: 22/22 provisional AI PASS, 109/109 pre-import static checks and 14/14 technical regressions. The tested ZIP SHA-256 is 40120521e43173191ab4babbc93180445fef33fb819f9d24ed2c25fb31dd7fa6. Use releases/0.69.3/ and its manifest; do not silently replace that frozen package. Formal legal/live-source/model-telemetry/host acceptance is still pending. Any plugin-content change requires a new version and appropriate retesting. The Terms page remains draft. Source upload, public website publication and hosted plugin deployment are separate actions; none is performed by preparation scripts.
