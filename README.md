# Vietnam Legal Advisor — 0.70.0

A plugin for Vietnamese legal research and professional workflows: a core skill router plus twelve specialist skills. Vietnamese is the default language. Current status: [STATUS.md](STATUS.md) (candidate, not public, not formally accepted).

## Structure

- `plugin/`: the product: manifests, logo and thirteen skills. Only this folder is packaged.
- `tests/`: 22 behavioral case specifications, the evaluation protocol and the evidence of each test round.
- `scripts/`: validation, packaging and host-run import.
- `docs/`: the website (GitHub Pages serves this folder): guide, support, privacy, terms.
- `STATUS.md`: single source of truth for status. `CHANGELOG.md` and `history/`: history. `LICENSE.md`: license map.

## Commands

Python 3.10+, standard library only:

```text
python scripts/validate.py    # static checks of manifests, skills, test records and website links
python scripts/package.py     # validate, then write dist/Vietnam-Legal-Advisor-<version>.zip and its .sha256
```

The ZIP contains only the contents of `plugin/` and is reproducible (fixed timestamps). `dist/` is not in Git. Neither script uploads or deploys anything. Static checks do not certify legal quality; behavioral testing is described in [tests/EVALUATION.md](tests/EVALUATION.md).

## License

Code (`scripts/`, `tests/run_integrity.py`) is under Apache-2.0; documents and skill content are under CC BY 4.0. The logo, test evidence and AI-generated output are also under CC BY 4.0, to the extent the publisher holds rights. See [LICENSE.md](LICENSE.md) for the path map and limits.
