# Local validation and packaging

Python 3.10+ and Pillow required. Install with `python -m pip install -r scripts/requirements.txt`. Missing Pillow causes image checks to fail. No credentials required.

From the repository root:

```text
python scripts/validate.py
python scripts/package.py
```

Both scripts also work when invoked by absolute path from another directory. Validation checks the manifests, required skills, internal file references, test inventory and website paths. Authored YAML currently uses the JSON subset of YAML; other YAML syntax requires extending the parser before use.

The package contains only `plugin/` contents, with `plugin.json` at its root. Outputs go to `dist/`; the same-version ZIP is replaced on a new run. ZIP integrity and file bytes are checked after writing. Neither script invokes GitHub, Plugin Creator, a model, or any deployment service. Static checks are not a complete plugin schema validator, security audit or legal-quality assessment.

The fixes passed technical regression checks; see tests/TECHNICAL_REVIEW.md. Behavioral acceptance is separate.
Images are verified and fully decoded (square PNG, 256–4096 pixels, at most 5 MiB).
Packaging rejects .env and .env.* case-insensitively. Asset types are restricted to PNG; skill resources to Markdown, JSON and YAML. Other types require review and an explicit code change.
PASS evidence is checked for integrity, not independently certified for truth.
