"""Stage gates for Wavvy series."""

from __future__ import annotations

import subprocess
import re
from pathlib import Path
from typing import Any

from .state import check_state

LYRIC_SKILL_REQUIRED_FILES = {
    "skill": Path("skills/wavvy-lyricist/SKILL.md"),
    "patterns": Path("skills/wavvy-lyricist/references/patterns.md"),
    "spec": Path("MASTER/lyrics/skills/WAVVY_LYRIC_SKILL_SPEC.md"),
}
LYRIC_OUTPUT_MODES = ("full-lyric-draft", "suno-prompt-only", "review-only")
LYRIC_DRAFT_SECTIONS = ("Source Map", "Constraint Freeze", "Lyric Strategy", "Draft", "Self-Gate")
LYRIC_REVIEW_SECTIONS = ("Source Map", "Constraint Freeze", "Findings", "Verdict")
LYRIC_SELF_GATE_NAMES = (
    "Copyright Safety",
    "Wavvy Identity",
    "Series DNA",
    "Time Policy",
    "Lyric Philosophy",
    "Natural Korean",
    "Hook Clarity",
    "Suno Format",
)
DIRECT_TIME_ACTIVITY_TERMS = (
    "17:00",
    "퇴근",
    "출근",
    "업무",
    "근무",
    "사무실",
    "회사",
    "오피스",
    "commute",
    "clock-out",
    "office",
    "workday",
)
OBJECT_SPACE_IMAGE_TERMS = (
    "빛",
    "공기",
    "창",
    "창가",
    "바닥",
    "방",
    "걸음",
    "손",
    "숨",
    "리듬",
    "색",
    "거리",
    "문",
    "유리",
    "벽",
    "바람",
    "온도",
    "소리",
    "어깨",
    "발",
    "light",
    "air",
    "window",
    "floor",
    "room",
    "step",
    "hand",
    "breath",
    "rhythm",
    "color",
)


def _check(name: str, passed: bool, detail: str = "") -> dict[str, Any]:
    return {
        "name": name,
        "status": "PASS" if passed else "FAIL",
        "detail": detail,
    }


def _status_check(name: str, status: str, detail: str = "", path: Path | None = None) -> dict[str, Any]:
    check: dict[str, Any] = {
        "name": name,
        "status": status,
        "detail": detail,
    }
    if path is not None:
        check["path"] = str(path)
    return check


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def _token_count(text: str, token: str) -> int:
    pattern = rf"(?<![A-Za-z0-9_-]){re.escape(token)}(?![A-Za-z0-9_-])"
    return len(re.findall(pattern, text))


def _heading_pattern(label: str) -> re.Pattern[str]:
    return re.compile(rf"^(?:#{{1,6}}\s*)?{re.escape(label)}\s*$", flags=re.MULTILINE)


def _section_position(text: str, label: str) -> int:
    match = _heading_pattern(label).search(text)
    return match.start() if match else -1


def _sections_in_order(text: str, labels: tuple[str, ...]) -> bool:
    positions = [_section_position(text, label) for label in labels]
    return all(position >= 0 for position in positions) and positions == sorted(positions)


def _extract_section(text: str, label: str) -> str:
    match = _heading_pattern(label).search(text)
    if not match:
        return ""
    start = match.end()
    next_positions = []
    for candidate in set(LYRIC_DRAFT_SECTIONS + LYRIC_REVIEW_SECTIONS):
        if candidate == label:
            continue
        next_match = _heading_pattern(candidate).search(text, start)
        if next_match:
            next_positions.append(next_match.start())
    end = min(next_positions) if next_positions else len(text)
    return text[start:end].strip()


def _infer_artifact_mode(text: str) -> tuple[str | None, dict[str, int], int]:
    constraint_freeze = _extract_section(text, "Constraint Freeze")
    counts = {mode: _token_count(constraint_freeze, mode) for mode in LYRIC_OUTPUT_MODES}
    total = sum(counts.values())
    mode = next((candidate for candidate, count in counts.items() if count == 1), None) if total == 1 else None
    return mode, counts, total


def _korean_lyric_lines(text: str) -> list[str]:
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith(("#", "```", "|")):
            continue
        if re.fullmatch(r"\[[^\]]+\]", stripped):
            continue
        hangul = re.findall(r"[가-힣]", stripped)
        if len(hangul) >= 4:
            lines.append(stripped)
    return lines


def _found_terms(text: str, terms: tuple[str, ...]) -> list[str]:
    found = []
    for term in terms:
        flags = re.IGNORECASE if re.search(r"[A-Za-z]", term) else 0
        if re.search(re.escape(term), text, flags=flags):
            found.append(term)
    return sorted(set(found), key=found.index)


def _concept_allows_time_terms(concept_text: str, terms: list[str]) -> bool:
    if not concept_text or not terms:
        return False
    marker = r"(?:explicit[_ -]?overrides?|overrides?|allowed|allow|requires|required|허용|예외|필수|명시)"
    for term in terms:
        term_pattern = re.escape(term)
        if re.search(rf"{marker}.{{0,160}}{term_pattern}|{term_pattern}.{{0,160}}{marker}", concept_text, flags=re.IGNORECASE | re.DOTALL):
            return True
    return False


def _minimal_lyric_lane(concept_text: str, constraint_freeze: str) -> bool:
    text = f"{concept_text}\n{constraint_freeze}"
    return bool(
        re.search(
            r"minimal|minimalistic|ambient|instrumental|low lyric density|낮은\s*가사\s*밀도|미니멀",
            text,
            flags=re.IGNORECASE,
        )
    )


def _requires_hook(concept_text: str, constraint_freeze: str) -> bool:
    text = f"{concept_text}\n{constraint_freeze}"
    return bool(
        re.search(
            r"pop/r&b|contemporary\s+r&b|\br&b\b|\brnb\b|\bpop\b|bright mainstream|mainstream|알앤비|팝",
            text,
            flags=re.IGNORECASE,
        )
    )


def _hook_anchor_present(strategy: str) -> bool:
    match = re.search(r"(?im)^\s*[-*]?\s*`?hook[_ -]?anchor`?\s*[:：-]\s*(.+)$", strategy)
    if not match:
        return False
    value = match.group(1).strip().strip("`")
    return bool(value) and not re.fullmatch(r"unknown|none|n/?a|tbd|미정|없음", value, flags=re.IGNORECASE)


def _self_gate_statuses(self_gate: str) -> dict[str, str]:
    statuses = {}
    for name in LYRIC_SELF_GATE_NAMES:
        match = re.search(rf"{re.escape(name)}[^\n]*(PASS|HOLD|FAIL)", self_gate, flags=re.IGNORECASE)
        if match:
            statuses[name] = match.group(1).upper()
    return statuses


def _lyric_package_checks(repo_root: Path) -> tuple[list[dict[str, Any]], list[str], list[str]]:
    checks: list[dict[str, Any]] = []
    blockers: list[str] = []
    evidence_refs: list[str] = []

    paths = {name: repo_root / rel_path for name, rel_path in LYRIC_SKILL_REQUIRED_FILES.items()}
    for name, path in paths.items():
        exists = path.exists()
        checks.append(_status_check(f"{name}_file_present", "PASS" if exists else "FAIL", str(LYRIC_SKILL_REQUIRED_FILES[name]), path))
        if exists:
            evidence_refs.append(LYRIC_SKILL_REQUIRED_FILES[name].as_posix())
        else:
            blockers.append(f"missing required lyric skill file: {LYRIC_SKILL_REQUIRED_FILES[name]}")

    skill_text = _read_text(paths["skill"])
    patterns_text = _read_text(paths["patterns"])
    spec_text = _read_text(paths["spec"])

    front_matter_ok = bool(re.search(r"(?ms)^---\s.*?^name:\s*wavvy-lyricist\s*$.*?^---\s*", skill_text))
    checks.append(_status_check("skill_front_matter_name", "PASS" if front_matter_ok else "FAIL", "name: wavvy-lyricist"))
    if not front_matter_ok:
        blockers.append("SKILL.md front matter must contain name: wavvy-lyricist")

    for mode in LYRIC_OUTPUT_MODES:
        present = mode in skill_text
        checks.append(_status_check(f"skill_names_mode_{mode}", "PASS" if present else "FAIL", mode))
        if not present:
            blockers.append(f"SKILL.md must name output mode: {mode}")

    for label in dict.fromkeys(LYRIC_DRAFT_SECTIONS + LYRIC_REVIEW_SECTIONS):
        present = label in skill_text
        checks.append(_status_check(f"skill_output_section_{label.lower().replace(' ', '_')}", "PASS" if present else "FAIL", label))
        if not present:
            blockers.append(f"SKILL.md must contain output section label: {label}")

    for required_ref in ("MASTER/lyrics/skills/WAVVY_LYRIC_SKILL_SPEC.md", "skills/wavvy-lyricist/references/patterns.md"):
        present = required_ref in skill_text
        checks.append(_status_check(f"skill_references_{Path(required_ref).name}", "PASS" if present else "FAIL", required_ref))
        if not present:
            blockers.append(f"SKILL.md must reference {required_ref}")

    no_external_lyrics = bool(
        re.search(
            r"does not store copied, translated.*external lyric lines|copied/translated external lyric lines are not stored",
            patterns_text,
            flags=re.IGNORECASE | re.DOTALL,
        )
    )
    checks.append(_status_check("patterns_external_lyric_storage_boundary", "PASS" if no_external_lyrics else "FAIL"))
    if not no_external_lyrics:
        blockers.append("patterns.md must state that copied/translated external lyric lines are not stored")

    for heading in ("Self-Gate Contract", "Harness Acceptance Baseline"):
        present = heading in spec_text
        checks.append(_status_check(f"spec_defines_{heading.lower().replace('-', '_').replace(' ', '_')}", "PASS" if present else "FAIL", heading))
        if not present:
            blockers.append(f"skill spec must define {heading}")

    return checks, blockers, evidence_refs


def _lyric_artifact_checks(
    artifact_path: Path,
    concept_text: str,
    requested_mode: str | None,
) -> tuple[list[dict[str, Any]], list[str], list[str], list[str]]:
    checks: list[dict[str, Any]] = []
    blockers: list[str] = []
    user_decisions: list[str] = []
    evidence_refs = [str(artifact_path)]
    text = _read_text(artifact_path)

    inferred_mode, mode_counts, total_modes = _infer_artifact_mode(text)
    mode = requested_mode or inferred_mode
    mode_detail = ", ".join(f"{key}={value}" for key, value in mode_counts.items())
    mode_ok = total_modes == 1 and (requested_mode is None or mode == requested_mode)
    checks.append(_status_check("constraint_freeze_mode_exactly_once", "PASS" if mode_ok else "FAIL", mode_detail, artifact_path))
    if not mode_ok:
        blockers.append("Constraint Freeze must name exactly one output mode matching --mode when provided")

    section_labels = LYRIC_REVIEW_SECTIONS if mode == "review-only" else LYRIC_DRAFT_SECTIONS
    sections_ok = _sections_in_order(text, section_labels)
    checks.append(_status_check("required_output_sections_in_order", "PASS" if sections_ok else "FAIL", " > ".join(section_labels), artifact_path))
    if not sections_ok:
        blockers.append("lyric artifact output sections are missing or out of order")

    constraint_freeze = _extract_section(text, "Constraint Freeze")
    draft = _extract_section(text, "Draft")
    strategy = _extract_section(text, "Lyric Strategy")
    self_gate = _extract_section(text, "Self-Gate")

    if mode == "suno-prompt-only":
        korean_lines = _korean_lyric_lines(draft)
        checks.append(
            _status_check(
                "suno_prompt_only_has_no_korean_lyric_rows",
                "PASS" if not korean_lines else "FAIL",
                f"{len(korean_lines)} Korean lyric-like lines",
                artifact_path,
            )
        )
        if korean_lines:
            blockers.append("suno-prompt-only output must not contain full Korean lyric rows")

    direct_terms = _found_terms(draft, DIRECT_TIME_ACTIVITY_TERMS)
    time_allowed = _concept_allows_time_terms(concept_text, direct_terms)
    checks.append(
        _status_check(
            "direct_time_activity_terms_absent_or_overridden",
            "PASS" if not direct_terms or time_allowed else "FAIL",
            ", ".join(direct_terms) if direct_terms else "",
            artifact_path,
        )
    )
    if direct_terms and not time_allowed:
        blockers.append("direct time/activity terms require an explicit concept override: " + ", ".join(direct_terms))

    if mode == "full-lyric-draft":
        image_terms = _found_terms(draft, OBJECT_SPACE_IMAGE_TERMS)
        enough_images = len(image_terms) >= 3 or _minimal_lyric_lane(concept_text, constraint_freeze)
        checks.append(
            _status_check(
                "object_space_phenomenon_images_minimum",
                "PASS" if enough_images else "USER_DECISION",
                f"{len(image_terms)} unique terms: {', '.join(image_terms[:8])}",
                artifact_path,
            )
        )
        if not enough_images:
            user_decisions.append("full-lyric-draft has fewer than three concrete object/space/phenomenon image terms")

    if mode in {"full-lyric-draft", "suno-prompt-only"} and _requires_hook(concept_text, constraint_freeze):
        hook_ok = _hook_anchor_present(strategy)
        checks.append(_status_check("hook_anchor_present_for_pop_rnb_lane", "PASS" if hook_ok else "FAIL", "", artifact_path))
        if not hook_ok:
            blockers.append("Pop/R&B or bright mainstream lanes require a non-empty hook_anchor in Lyric Strategy")

    statuses = _self_gate_statuses(self_gate)
    copyright_status = statuses.get("Copyright Safety")
    checks.append(
        _status_check(
            "copyright_safety_self_gate_present",
            "PASS" if copyright_status else "FAIL",
            copyright_status or "",
            artifact_path,
        )
    )
    if not copyright_status:
        blockers.append("Self-Gate must include Copyright Safety")
    elif copyright_status == "FAIL":
        blockers.append("Self-Gate Copyright Safety is FAIL")
    elif copyright_status == "HOLD":
        user_decisions.append("Self-Gate Copyright Safety is HOLD")

    missing_self_gates = [name for name in LYRIC_SELF_GATE_NAMES if name not in statuses]
    checks.append(
        _status_check(
            "self_gate_contract_labels_present",
            "PASS" if not missing_self_gates else "USER_DECISION",
            ", ".join(missing_self_gates),
            artifact_path,
        )
    )
    if missing_self_gates:
        user_decisions.append("Self-Gate is missing contract labels: " + ", ".join(missing_self_gates))

    failed_gates = [name for name, status in statuses.items() if status == "FAIL"]
    held_gates = [name for name, status in statuses.items() if status == "HOLD"]
    if failed_gates:
        blockers.append("Self-Gate contains FAIL: " + ", ".join(failed_gates))
    if held_gates:
        user_decisions.append("Self-Gate contains HOLD: " + ", ".join(held_gates))

    return checks, blockers, user_decisions, evidence_refs


def run_lyrics_skill_gate(
    repo_root: Path,
    series_path: Path | None = None,
    artifact_path: Path | None = None,
    mode: str | None = None,
) -> dict[str, Any]:
    """Validate the Wavvy lyric skill package and optional lyric artifact."""
    repo_root = repo_root.resolve()
    checks, blockers, evidence_refs = _lyric_package_checks(repo_root)
    warnings: list[str] = []
    user_decisions: list[str] = []

    concept_text = ""
    if series_path is not None:
        concept_path = series_path / "concept.md"
        concept_text = _read_text(concept_path)
        concept_ok = bool(concept_text)
        checks.append(_status_check("series_concept_present", "PASS" if concept_ok else "FAIL", str(concept_path), concept_path))
        evidence_refs.append(str(concept_path))
        if not concept_ok:
            blockers.append("series concept.md is required when a series path is supplied")

    if artifact_path is not None:
        artifact_checks, artifact_blockers, artifact_decisions, artifact_refs = _lyric_artifact_checks(
            artifact_path,
            concept_text,
            mode,
        )
        checks.extend(artifact_checks)
        blockers.extend(artifact_blockers)
        user_decisions.extend(artifact_decisions)
        evidence_refs.extend(artifact_refs)

    result = "FAIL" if blockers else ("USER_DECISION" if user_decisions else "PASS")
    return {
        "schema": "wavvy.lyrics_skill_gate.v1",
        "stage": "lyrics-review",
        "result": result,
        "series": str(series_path) if series_path else "",
        "artifact": str(artifact_path) if artifact_path else "",
        "mode": mode or "",
        "checks": checks,
        "warnings": sorted(set(warnings)),
        "blockers": sorted(set(blockers)),
        "user_decisions": sorted(set(user_decisions)),
        "evidence_refs": sorted(set(evidence_refs)),
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
    if stage not in {"source-final", "render-final", "upload-ready", "uploaded", "lyrics-review"}:
        raise ValueError(f"unknown stage: {stage}")

    if stage == "lyrics-review":
        return run_lyrics_skill_gate(repo_root, series_path)

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
    available_audio_files = artifacts.get("available_audio_files", artifacts.get("audio_files", 0))
    audio_source = artifacts.get("audio_source", "input_tracks")

    source_checks = [
        ("concept_md_present", artifacts["concept_md"] == "present"),
        (
            "final_track_sources_or_source_map_present",
            artifacts["final_track_sources"] == "present" or artifacts.get("source_map") == "present",
        ),
        (
            "report_json_present_or_source_map_ready",
            artifacts["report_json"] == "present"
            or (artifacts.get("source_map") == "present" and not artifacts.get("source_map_missing")),
        ),
        ("youtube_metadata_present", artifacts["youtube_metadata"] == "present"),
        ("audio_files_present", available_audio_files > 0, f"{available_audio_files} audio files via {audio_source}"),
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
