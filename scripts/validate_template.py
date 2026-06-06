from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "README.md",
    "docs/PRD.md",
    "docs/SPEC.md",
    "docs/PLAN.md",
    "docs/REVIEW.md",
    ".codex/workflows/01-discover.md",
    ".codex/workflows/02-spec.md",
    ".codex/workflows/03-plan.md",
    ".codex/workflows/04-implement.md",
    ".codex/workflows/05-verify.md",
    ".codex/workflows/06-finish.md",
    "adapters/README.md",
    "adapters/supported_ides.json",
    "adapters/codex/adapter.py",
    "adapters/antigravity/adapter.py",
    "adapters/mock-ide/adapter.py",
    "db/migrations/.gitkeep",
    "db/seeds/.gitkeep",
    "services/go/.gitkeep",
    "services/python/.gitkeep",
    "services/frontend/.gitkeep",
]

STAGES = ["discover", "spec", "plan", "implement", "verify", "finish"]


def check_paths() -> list[str]:
    return [path for path in REQUIRED_PATHS if not (ROOT / path).exists()]


def check_supported_ides() -> list[str]:
    errors: list[str] = []
    data = json.loads((ROOT / "adapters" / "supported_ides.json").read_text(encoding="utf-8"))
    ids = {item["id"] for item in data.get("ides", [])}
    for required in {"codex", "antigravity", "mock-ide"}:
        if required not in ids:
            errors.append(f"missing supported IDE: {required}")
    for item in data.get("ides", []):
        adapter = ROOT / item["adapter"]
        if not adapter.exists():
            errors.append(f"missing adapter file for {item['id']}: {item['adapter']}")
    return errors


def check_adapters() -> list[str]:
    errors: list[str] = []
    for adapter in ("codex", "antigravity", "mock-ide"):
        cmd = [sys.executable, str(ROOT / "adapters" / adapter / "adapter.py"), "detect"]
        result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
        if result.returncode != 0:
            errors.append(f"{adapter} detect failed: {result.stderr or result.stdout}")
            continue
        payload = json.loads(result.stdout)
        if not payload.get("ok"):
            errors.append(f"{adapter} detect returned ok=false")
        for stage in STAGES:
            run_cmd = [sys.executable, str(ROOT / "adapters" / adapter / "adapter.py"), "run", stage]
            run_result = subprocess.run(run_cmd, cwd=ROOT, text=True, capture_output=True)
            if run_result.returncode != 0:
                errors.append(f"{adapter} run {stage} failed: {run_result.stderr or run_result.stdout}")
    return errors


def main() -> int:
    errors = []
    errors.extend(f"missing path: {path}" for path in check_paths())
    errors.extend(check_supported_ides())
    errors.extend(check_adapters())

    if errors:
        print(json.dumps({"ok": False, "errors": errors}, ensure_ascii=False, indent=2))
        return 1

    print(json.dumps({"ok": True, "checked_paths": len(REQUIRED_PATHS), "adapters": 3}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
