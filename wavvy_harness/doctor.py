"""Environment checks for Wavvy harness operations."""

from __future__ import annotations

import importlib.util
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any


REQUIRED_MODULES = {
    "click": "click",
    "ffmpeg-python": "ffmpeg",
    "pandas": "pandas",
    "ffmpeg-normalize": "ffmpeg_normalize",
}

REQUIRED_BINARIES = ["ffmpeg", "ffprobe", "git"]
DEFAULT_PEER_REVIEW_SCRIPT = Path("~/Project/claude-center/scripts/peer-agent-review.sh").expanduser()
DEFAULT_FFMPEG_FULL = Path("/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg")


def _check_module(package_name: str, module_name: str) -> dict[str, Any]:
    present = importlib.util.find_spec(module_name) is not None
    return {
        "name": package_name,
        "module": module_name,
        "required": True,
        "status": "pass" if present else "fail",
    }


def _binary_version(binary: str) -> str:
    path = shutil.which(binary)
    if not path:
        return ""
    try:
        result = subprocess.run(
            [path, "-version"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
    except Exception:
        return path
    first_line = result.stdout.splitlines()[0] if result.stdout else path
    return first_line.strip()


def _check_binary(binary: str) -> dict[str, Any]:
    path = shutil.which(binary)
    return {
        "name": binary,
        "path": path or "",
        "version": _binary_version(binary) if path else "",
        "required": True,
        "status": "pass" if path else "fail",
    }


def _check_writable_temp(repo_root: Path) -> dict[str, Any]:
    base = repo_root / ".ai" / "tmp"
    try:
        base.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile("w", dir=base, prefix="doctor-", delete=True) as tmp:
            tmp.write("ok")
            tmp.flush()
        return {"name": "workspace_writable", "path": str(base), "required": True, "status": "pass"}
    except Exception as exc:
        return {
            "name": "workspace_writable",
            "path": str(base),
            "required": True,
            "status": "fail",
            "detail": str(exc),
        }


def _check_disk(repo_root: Path) -> dict[str, Any]:
    usage = shutil.disk_usage(repo_root)
    free_gib = usage.free / (1024**3)
    status = "pass" if free_gib >= 5 else "warn"
    return {
        "name": "disk_free",
        "path": str(repo_root),
        "required": False,
        "status": status,
        "free_gib": round(free_gib, 2),
    }


def run_doctor(repo_root: Path) -> dict[str, Any]:
    """Run deterministic local dependency checks."""
    repo_root = repo_root.resolve()
    checks: list[dict[str, Any]] = []

    for package_name, module_name in REQUIRED_MODULES.items():
        checks.append(_check_module(package_name, module_name))

    for binary in REQUIRED_BINARIES:
        checks.append(_check_binary(binary))

    peer_script = Path(os.environ.get("WAVVY_PEER_REVIEW_SCRIPT", str(DEFAULT_PEER_REVIEW_SCRIPT))).expanduser()
    checks.append(
        {
            "name": "peer_review_script",
            "path": str(peer_script),
            "required": True,
            "status": "pass" if peer_script.exists() else "fail",
        }
    )

    checks.append(
        {
            "name": "ffmpeg_full_drawtext",
            "path": str(DEFAULT_FFMPEG_FULL),
            "required": False,
            "status": "pass" if DEFAULT_FFMPEG_FULL.exists() else "warn",
        }
    )
    checks.append(_check_disk(repo_root))
    checks.append(_check_writable_temp(repo_root))

    blockers = [check for check in checks if check.get("required") and check.get("status") == "fail"]
    warnings = [check for check in checks if check.get("status") == "warn"]

    return {
        "schema": "wavvy.doctor.v1",
        "repo": str(repo_root),
        "result": "PASS" if not blockers else "FAIL",
        "checks": checks,
        "warnings": warnings,
        "blockers": blockers,
    }
