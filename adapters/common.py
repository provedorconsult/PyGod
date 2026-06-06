from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAGES = {"discover", "spec", "plan", "implement", "verify", "finish"}


def emit(payload: dict) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def read_context() -> dict:
    docs = {}
    for name in ("PRD.md", "SPEC.md", "PLAN.md", "REVIEW.md"):
        path = ROOT / "docs" / name
        docs[name] = {"path": str(path.relative_to(ROOT)), "exists": path.exists()}
    return {
        "root": str(ROOT),
        "docs": docs,
        "supported_ides": str((ROOT / "adapters" / "supported_ides.json").relative_to(ROOT)),
    }


def run_stage(adapter: str, stage: str, mode: str, artifact_dir: str) -> dict:
    if stage not in STAGES:
        return {"ok": False, "adapter": adapter, "error": f"invalid stage: {stage}", "valid_stages": sorted(STAGES)}
    return {
        "ok": True,
        "adapter": adapter,
        "stage": stage,
        "mode": mode,
        "artifact_dir": artifact_dir,
        "message": f"{adapter} mapped generic stage '{stage}'",
    }


def command_exists(command: str) -> bool:
    return shutil.which(command) is not None


def dispatch(adapter: str, mode: str, artifact_dir: str, capabilities: dict) -> int:
    args = sys.argv[1:]
    command = args[0] if args else "help"

    if command == "detect":
        emit({"ok": True, "adapter": adapter, "mode": mode, "capabilities": capabilities})
        return 0
    if command == "context":
        emit({"ok": True, "adapter": adapter, "context": read_context()})
        return 0
    if command == "run":
        stage = args[1] if len(args) > 1 else ""
        payload = run_stage(adapter, stage, mode, artifact_dir)
        emit(payload)
        return 0 if payload["ok"] else 2
    if command == "artifacts":
        path = ROOT / artifact_dir
        emit({"ok": True, "adapter": adapter, "artifact_dir": str(path.relative_to(ROOT))})
        return 0

    emit({"ok": False, "adapter": adapter, "commands": ["detect", "context", "run <stage>", "artifacts"]})
    return 2
