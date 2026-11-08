# SPDX-License-Identifier: Apache-2.0
"""Compatibility entrypoint. Canonical validator: scripts/validate.py."""
from pathlib import Path
import runpy

if __name__ == '__main__':
    runpy.run_path(str(Path(__file__).resolve().parents[1]/'scripts/validate.py'),run_name='__main__')
