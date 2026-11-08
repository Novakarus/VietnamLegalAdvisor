# Vietnam Legal Advisor — 0.70.0

Local candidate: Core Skill Router plus twelve specialist skills. Vietnamese is the default language.

## Structure

- STATUS.md: single source of truth for project status. LICENSE.md: license map.
- docs/: website, support, privacy, terms and website assets.
- plugin/: manifests, assets and thirteen skills.
- tests/: 22 behavioral specifications, fixtures and evaluation records.
- scripts/: validation and packaging utilities.
- dist/: generated ZIPs, excluded from Git.
- tests/runs/: version-bound test reports and evidence for all three rounds.

## Commands

Requires Python 3.10+ and Pillow:

```text
python -m pip install -r scripts/requirements.txt
python scripts/validate.py
python scripts/package.py
```

Canonical image: vietnam-legal-advisor-icon-v4.png. Packaging includes only plugin/ contents. Same-version ZIPs are replaced; preserve released archives separately.

## Status

Single source of truth: [STATUS.md](STATUS.md). Summary: version 0.70.0 is a packaged candidate (renumbered from 0.69.4 and 0.7.1 by the publisher; license notice added to the package; skill content unchanged); behavioral tests are not yet run for this version. Version 0.69.3 was removed from the repository on 2026-11-08; only its round 1-3 test records (run by Codex) are kept as history. Formal acceptance and public-release approval are pending. Nothing was uploaded or deployed.

Local metadata does not confirm current hosted release or visibility. These scripts do not upload or deploy anything.

## License

Approved by the publisher on 2026-11-04 (users are responsible for their own use). Code (`scripts/`) is under Apache-2.0 and documents/skill content under CC BY 4.0; see [LICENSE.md](LICENSE.md) for the path map. The logo, test evidence and release bundles are not licensed.
