# FILE: starter_code/tests/conftest.py
# Minimal path fix for pytest (supports both import styles).
from __future__ import annotations
import sys
from pathlib import Path

def _patch_syspath() -> None:
    tests_dir = Path(__file__).resolve().parent   # .../starter_code/tests
    pkg_dir = tests_dir.parent                    # .../starter_code
    outer_dir = pkg_dir.parent                    # .../(folder containing 'starter_code')

    # For: from starter_code.models.item import ItemModel  (used in tests)
    if str(outer_dir) not in sys.path:
        sys.path.insert(0, str(outer_dir))

    # For: from db import db  (used inside app modules)
    if str(pkg_dir) not in sys.path:
        sys.path.insert(0, str(pkg_dir))

_patch_syspath()
