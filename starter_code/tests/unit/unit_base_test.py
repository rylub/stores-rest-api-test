# FILE: starter_code/tests/unit/unit_base_test.py
"""
UnitBaseTest

Minimal Flask app context for unit tests.
Avoids importing starter_code.app (which pulls resources/JWT).
"""
from __future__ import annotations

import unittest
from flask import Flask


class UnitBaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self._app = Flask(__name__)
        self._app.config.update(TESTING=True)
        # Keep course pattern: with self.app_context():
        from starter_code.models import store as _store  # noqa: F401
        from starter_code.models import item as _item  # noqa: F401
        self.app_context = self._app.app_context

    def tearDown(self) -> None:
        # Nothing to clean for unit tests
        pass