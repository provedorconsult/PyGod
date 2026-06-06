from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common import command_exists, dispatch


if __name__ == "__main__":
    raise SystemExit(
        dispatch(
            adapter="antigravity",
            mode="multi-agent",
            artifact_dir="artifacts/antigravity",
            capabilities={
                "cli_available": command_exists("antigravity"),
                "roles": ["manager", "writer", "critic", "tester"],
                "human_review_artifacts": True,
            },
        )
    )
