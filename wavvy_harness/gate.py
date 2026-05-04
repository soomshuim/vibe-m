"""Stage gates for Wavvy series."""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any

from .state import check_state


def _check(name: str, passed: bool, detail: str = "") -> dict[str, Any]:
    return {
        "name": name,
        "status": "PASS" if passed else "FAIL",
        "detail": detail,
    }


def _has_media_stream(path: Path, stream_type: str) -> bool:
    selector = "v:0" if stream_type == "video" else "a:0"
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            selector,
            "-show_entries",
            "stream=codec_type",
            "-of",
            "csv=p=0",
            str(path),
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.returncode == 0 and stream_type in result.stdout


def run_gate(
    series_path: Path,
    repo_root: Path,
    stage: str,
    validation: dict[str, Any],
) -> dict[str, Any]:
    """Run a stage-specific gate."""
    stage = stage.replace("_", "-")
    if stage not in {"source-final", "render-final", "upload-ready", "uploaded"}:
        raise ValueError(f"unknown stage: {stage}")

    checks: list[dict[str, Any]] = []
    warnings: list[str] = []
    blockers: list[str] = []

    validation_passed = bool(validation.get("is_valid"))
    checks.append(_check("validate_project", validation_passed, validation.get("detail", "")))
    if not validation_passed:
        blockers.extend(validation.get("errors", ["validate_project failed"]))

    state_result = check_state(series_path, repo_root, {"phase": stage.replace("-", "_")})
    state = state_result["state"]
    artifacts = state["artifact_status"]
    warnings.extend(state_result.get("warnings", []))
    blockers.extend(state_result.get("blockers", []))

    source_checks = [
        ("concept_md_present", artifacts["concept_md"] == "present"),
        ("final_track_sources_present", artifacts["final_track_sources"] == "present"),
        ("report_json_present", artifacts["report_json"] == "present"),
        ("youtube_metadata_present", artifacts["youtube_metadata"] == "present"),
        ("audio_files_present", artifacts["audio_files"] > 0, f"{artifacts['audio_files']} audio files"),
    ]
    for item in source_checks:
        name, passed, *detail = item
        checks.append(_check(name, bool(passed), detail[0] if detail else ""))

    if artifacts["final_track_sources_count"] and artifacts["report_tracks"]:
        counts_match = artifacts["final_track_sources_count"] == artifacts["report_tracks"]
        checks.append(
            _check(
                "final_track_sources_match_report",
                counts_match,
                f"fts={artifacts['final_track_sources_count']} report={artifacts['report_tracks']}",
            )
        )

    tracks_dir = series_path / "input" / "tracks"
    has_txt = tracks_dir.exists() and any(tracks_dir.glob("*.txt"))
    rubric_snapshot = series_path / "rubric_snapshot.json"
    report_rubric = False
    if not has_txt and artifacts["final_track_sources"] == "present" and not rubric_snapshot.exists() and not report_rubric:
        warnings.append("rubric_unverified_after_finalize")

    if stage == "render-final":
        final_mkv = series_path / "output" / "final.mkv"
        upload_csv = series_path / "output" / "upload.csv"
        checks.append(_check("final_mkv_present", final_mkv.exists()))
        checks.append(_check("upload_csv_present", upload_csv.exists()))
        if final_mkv.exists():
            has_video = _has_media_stream(final_mkv, "video")
            has_audio = _has_media_stream(final_mkv, "audio")
            checks.append(_check("final_mkv_video_stream", has_video))
            checks.append(_check("final_mkv_audio_stream", has_audio))
            if not has_video:
                blockers.append("output/final.mkv missing video stream")
            if not has_audio:
                blockers.append("output/final.mkv missing audio stream")

    if stage == "upload-ready":
        upload_completed = artifacts["youtube_upload"] == "completed"
        final_mkv = series_path / "output" / "final.mkv"
        upload_csv = series_path / "output" / "upload.csv"
        checks.append(
            _check(
                "final_mkv_present_or_uploaded",
                final_mkv.exists() or upload_completed,
                artifacts["final_mkv"],
            )
        )
        checks.append(
            _check(
                "upload_csv_present_or_uploaded",
                upload_csv.exists() or upload_completed,
                artifacts["upload_csv"],
            )
        )
        checks.append(_check("youtube_upload_status", True, "completed" if upload_completed else "pending"))
        if final_mkv.exists():
            has_video = _has_media_stream(final_mkv, "video")
            has_audio = _has_media_stream(final_mkv, "audio")
            checks.append(_check("final_mkv_video_stream", has_video))
            checks.append(_check("final_mkv_audio_stream", has_audio))
            if not has_video:
                blockers.append("output/final.mkv missing video stream")
            if not has_audio:
                blockers.append("output/final.mkv missing audio stream")
        has_subtitle = artifacts["subtitle_txt"] == "present" or artifacts["subtitle_srt"] == "present"
        checks.append(_check("subtitle_artifact_present", has_subtitle))

    if stage == "uploaded":
        checks.append(_check("youtube_upload_completed", artifacts["youtube_upload"] == "completed"))
        if artifacts["final_mkv"] == "deleted_after_upload":
            warnings.append("local final.mkv deleted after upload; regenerate with pack if needed")
        if artifacts["upload_csv"] == "deleted_after_upload":
            warnings.append("local upload.csv deleted after upload; regenerate with pack if needed")

    return {
        "schema": "wavvy.gate.v1",
        "stage": stage,
        "result": "PASS" if not blockers else "FAIL",
        "series": str(series_path),
        "checks": checks,
        "warnings": sorted(set(warnings)),
        "blockers": sorted(set(blockers)),
    }
