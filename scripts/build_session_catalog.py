"""Rebuild the public catalog without exposing withdrawn curriculum source.

PUBLIC_RELEASE_STATUS.md withholds delivery. A future reviewed release must
explicitly change this policy; the presence of session files is not permission
to publish them. Ordinary builds always produce the withdrawn, empty catalog.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "data" / "sessions.json"


def build() -> None:
    catalog = {
        "generated": "2026-09-04",
        "count": 0,
        "status": "withdrawn_pending_independent_review",
        "sessions": [],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(catalog, separators=(",", ":")) + "\n", encoding="utf-8")
    print("Wrote withdrawn catalog (0 sessions)")


if __name__ == "__main__":
    build()
