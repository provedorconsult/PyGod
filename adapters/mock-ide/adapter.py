from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common import dispatch


if __name__ == "__main__":
    raise SystemExit(
        dispatch(
            adapter="mock-ide",
            mode="reference",
            artifact_dir="artifacts/mock-ide",
            capabilities={
                "cli_available": True,
                "purpose": "reference adapter for future IDE integrations",
            },
        )
    )
