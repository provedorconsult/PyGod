from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common import command_exists, dispatch


if __name__ == "__main__":
    raise SystemExit(
        dispatch(
            adapter="codex",
            mode="single-agent",
            artifact_dir="outputs/codex",
            capabilities={
                "cli_available": command_exists("codex"),
                "stages": ["discover", "spec", "plan", "implement", "verify", "finish"],
                "strategy": "sequential optimized execution",
            },
        )
    )
