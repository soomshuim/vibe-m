import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from click.testing import CliRunner

from wavvy import ProjectPaths, TrackInfo, cli, generate_report, validate_project
from wavvy_harness.doctor import run_ssot_hygiene
from wavvy_harness.gate import run_gate, run_lyrics_skill_gate
from wavvy_harness.state import build_state, check_state


CONCEPT_FINAL = """# Test Series

## YouTube Metadata

### 제목
```text
Playlist | 20:00 | Test | Wavvy
```

### 설명
```text
description
```

### 태그
```text
tag1,tag2
```

## Final Track Sources

### 01. One

- Filename: `01__One__A__Genre__100.wav`

#### STYLE
```text
style
```

#### EXCLUDE
```text
None
```

#### LYRICS
```text
lyrics
```

### 02. Two

- Filename: `02__Two__B__Genre__110.wav`

#### STYLE
```text
style
```

#### EXCLUDE
```text
None
```

#### LYRICS
```text
lyrics
```
"""

CONCEPT_UPLOADED = CONCEPT_FINAL.replace(
    "## YouTube Metadata",
    "## Upload Status\n\n- YouTube upload completed\n- Local final.mkv deleted intentionally after upload.\n\n## YouTube Metadata",
)

CONCEPT_COMPILATION = """# R&B BEST

## Series Type

- **Type**: Compilation / Best Album

## YouTube Draft

### 제목
```text
Playlist | R&B Best | Wavvy
```

### 설명
```text
description
```

### 태그
```text
tag1,tag2
```

## Track Selection

| # | Title | Source | Copied Filename |
|---|---|---|---|
| 01 | One | `SERIES/01/input/tracks/09__One__Warm__RnB__90.wav` | `01__One__Warm__RnB__90.wav` |
| 02 | Two | `SERIES/02/work/norm_tracks/norm_03__Two__Cool__Soul__100.wav` | `02__Two__Cool__Soul__100.wav` |
"""


def make_series(root: Path, concept_text: str = CONCEPT_FINAL) -> Path:
    series = root / "SERIES" / "20-00"
    tracks = series / "input" / "tracks"
    output = series / "output"
    tracks.mkdir(parents=True)
    output.mkdir(parents=True)
    (series / "concept.md").write_text(concept_text, encoding="utf-8")
    (tracks / "01__One__A__Genre__100.wav").write_bytes(b"")
    (tracks / "02__Two__B__Genre__110.wav").write_bytes(b"")
    report = {
        "tracks": [
            {"order": 1, "title": "One", "filename": "01__One__A__Genre__100.wav"},
            {"order": 2, "title": "Two", "filename": "02__Two__B__Genre__110.wav"},
        ]
    }
    (output / "report.json").write_text(json.dumps(report), encoding="utf-8")
    return series


def make_lyric_skill_package(root: Path) -> None:
    skill_dir = root / "skills" / "wavvy-lyricist"
    references_dir = skill_dir / "references"
    spec_dir = root / "MASTER" / "lyrics" / "skills"
    references_dir.mkdir(parents=True)
    spec_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(
        """---
name: wavvy-lyricist
description: Test fixture
---

# Wavvy Lyricist

References `MASTER/lyrics/skills/WAVVY_LYRIC_SKILL_SPEC.md` and
`skills/wavvy-lyricist/references/patterns.md`.

Modes: `full-lyric-draft`, `suno-prompt-only`, `review-only`.

For drafts:
1. `Source Map`
2. `Constraint Freeze`
3. `Lyric Strategy`
4. `Draft`
5. `Self-Gate`

For review-only:
1. `Source Map`
2. `Constraint Freeze`
3. `Findings`
4. `Verdict`
""",
        encoding="utf-8",
    )
    (references_dir / "patterns.md").write_text(
        "This reference does not store copied, translated, or closely paraphrased external lyric lines.\n",
        encoding="utf-8",
    )
    (spec_dir / "WAVVY_LYRIC_SKILL_SPEC.md").write_text(
        "# Wavvy Lyric Skill Spec\n\n## Self-Gate Contract\n\n## Harness Acceptance Baseline\n",
        encoding="utf-8",
    )


def write_full_lyric_artifact(path: Path, draft: str, self_gate_extra: str = "") -> None:
    path.write_text(
        f"""Source Map
- `MASTER/SSOT.md`
- `SERIES/17-00/concept.md`

Constraint Freeze
- series: 17-00
- track: 01
- mode: full-lyric-draft
- genre_lane: Pop/R&B
- bpm: 104
- key: unknown
- mood: bright
- vocal_identity: single lead, chest-dominant
- language_policy: Korean
- time_activity_policy: direct terms absent
- explicit_overrides: none
- copyright_boundary: no copied, translated, closely paraphrased material

Lyric Strategy
- narrator: first person
- emotional_arc: small lift
- hook_anchor: 다시 올라가
- vocabulary_lane: light, air, motion
- density: medium
- banned_cliches: direct time words
- suno_handling: full lyric draft, not prompt-only

Draft
{draft}

Self-Gate
- Copyright Safety: PASS - original draft
- Wavvy Identity: PASS - Korean single lead
- Series DNA: PASS - Pop/R&B lane
- Time Policy: PASS - direct terms absent
- Lyric Philosophy: PASS - image based
- Natural Korean: PASS - speakable
- Hook Clarity: PASS - hook anchor present
- Suno Format: PASS - full lyric draft mode
{self_gate_extra}
""",
        encoding="utf-8",
    )


class HarnessTests(unittest.TestCase):
    def test_generate_report_crossfade_reduction_uses_repeat(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "report.json"
            tracks = [
                TrackInfo(Path("01__One__A__Genre__100.wav"), 1, "One", "A", "Genre", 100, duration=10.0),
                TrackInfo(Path("02__Two__B__Genre__110.wav"), 2, "Two", "B", "Genre", 110, duration=20.0),
            ]
            self.assertTrue(generate_report(tracks, output, final_duration=58.4, params={"repeat": 2}))
            report = json.loads(output.read_text(encoding="utf-8"))
            self.assertAlmostEqual(report["summary"]["crossfade_reduction"], 1.6)

    def test_build_state_infers_source_final_for_minimal_fixture(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            series = make_series(root)
            make_lyric_skill_package(root)
            state = build_state(series, root)
            self.assertEqual(state["phase"], "source_final")
            self.assertEqual(state["artifact_status"]["final_track_sources_count"], 2)
            self.assertEqual(state["artifact_status"]["report_tracks"], 2)
            self.assertIn("MASTER/SSOT.md", state["authoritative_docs"])
            self.assertIn("MASTER/ai/RUNTIME_RULES.md", state["authoritative_docs"])
            self.assertIn("MASTER/cli/SPEC.md", state["authoritative_docs"])
            self.assertEqual(state["artifact_status"]["lyric_skill_package"], "present")
            self.assertIn("skills/wavvy-lyricist/SKILL.md", state["evidence_refs"])

    def test_lyrics_skill_package_gate_passes_static_contract(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_lyric_skill_package(root)

            result = run_lyrics_skill_gate(root)

            self.assertEqual(result["result"], "PASS", result)
            checks = {check["name"]: check for check in result["checks"]}
            self.assertEqual(checks["skill_front_matter_name"]["status"], "PASS")
            self.assertEqual(checks["spec_defines_self_gate_contract"]["status"], "PASS")
            self.assertIn("MASTER/lyrics/skills/WAVVY_LYRIC_SKILL_SPEC.md", result["evidence_refs"])

    def test_lyrics_skill_artifact_gate_rejects_direct_time_terms_without_override(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_lyric_skill_package(root)
            series = root / "SERIES" / "17-00"
            series.mkdir(parents=True)
            (series / "concept.md").write_text("Genre: Pop/R&B\nMood: bright\n", encoding="utf-8")
            artifact = root / "artifact.md"
            write_full_lyric_artifact(
                artifact,
                "[Verse]\n창가에 빛이 내려\n공기 끝이 다시 열려\n손끝의 리듬이 퇴근길을 밀어\n",
            )

            result = run_lyrics_skill_gate(root, series, artifact, "full-lyric-draft")

            self.assertEqual(result["result"], "FAIL")
            self.assertTrue(any("direct time/activity" in blocker for blocker in result["blockers"]))

    def test_lyrics_skill_artifact_gate_rejects_korean_rows_in_suno_prompt_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_lyric_skill_package(root)
            series = root / "SERIES" / "17-00"
            series.mkdir(parents=True)
            (series / "concept.md").write_text("Genre: Pop/R&B\n", encoding="utf-8")
            artifact = root / "suno.md"
            artifact.write_text(
                """Source Map
- `SERIES/17-00/concept.md`

Constraint Freeze
- mode: suno-prompt-only
- genre_lane: Pop/R&B

Lyric Strategy
- hook_anchor: 다시 올라가

Draft
창가에 빛이 내려와

Self-Gate
- Copyright Safety: PASS - original prompt
- Wavvy Identity: PASS - prompt only
- Series DNA: PASS - Pop/R&B lane
- Time Policy: PASS - direct terms absent
- Lyric Philosophy: PASS - image based
- Natural Korean: PASS - n/a
- Hook Clarity: PASS - hook named
- Suno Format: PASS - prompt-only
""",
                encoding="utf-8",
            )

            result = run_lyrics_skill_gate(root, series, artifact, "suno-prompt-only")

            self.assertEqual(result["result"], "FAIL")
            checks = {check["name"]: check for check in result["checks"]}
            self.assertEqual(checks["suno_prompt_only_has_no_korean_lyric_rows"]["status"], "FAIL")

    def test_lyrics_skill_cli_review_stage_skips_media_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_lyric_skill_package(root)
            series = root / "SERIES" / "17-00"
            series.mkdir(parents=True)
            (series / "concept.md").write_text("Genre: Pop/R&B\n", encoding="utf-8")
            runner = CliRunner()

            with patch("wavvy.git_repo_root", return_value=root), patch(
                "wavvy.validate_project",
                side_effect=AssertionError("lyrics-review must not run media validation"),
            ):
                result = runner.invoke(cli, ["gate", str(series), "--stage", "lyrics-review", "--json"])

            self.assertEqual(result.exit_code, 0, result.output)
            payload = json.loads(result.output)
            self.assertEqual(payload["schema"], "wavvy.lyrics_skill_gate.v1")
            self.assertEqual(payload["result"], "PASS")

    def test_compilation_source_map_counts_as_available_audio(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            series = root / "SERIES" / "RNB-BEST"
            (series / "input").mkdir(parents=True)
            (series / "input" / "thumb.jpg").write_bytes(b"thumb")
            (series / "concept.md").write_text(CONCEPT_COMPILATION, encoding="utf-8")
            source_one = root / "SERIES/01/input/tracks/09__One__Warm__RnB__90.wav"
            source_two = root / "SERIES/02/work/norm_tracks/norm_03__Two__Cool__Soul__100.wav"
            source_one.parent.mkdir(parents=True)
            source_two.parent.mkdir(parents=True)
            source_one.write_bytes(b"one")
            source_two.write_bytes(b"two")

            state = build_state(series, root)
            self.assertEqual(state["phase"], "source_final")
            self.assertEqual(state["artifact_status"]["audio_files"], 0)
            self.assertEqual(state["artifact_status"]["available_audio_files"], 2)
            self.assertEqual(state["artifact_status"]["audio_source"], "concept_track_selection")

            result = check_state(series, root, {"phase": "source_final"})
            self.assertEqual(result["result"], "PASS")

    def test_validate_project_uses_compilation_source_map_when_tracks_dir_is_empty(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            series = root / "SERIES" / "RNB-BEST"
            (series / "input").mkdir(parents=True)
            (series / "input" / "thumb.jpg").write_bytes(b"thumb")
            (series / "concept.md").write_text(CONCEPT_COMPILATION, encoding="utf-8")
            source_one = root / "SERIES/01/input/tracks/09__One__Warm__RnB__90.wav"
            source_two = root / "SERIES/02/work/norm_tracks/norm_03__Two__Cool__Soul__100.wav"
            source_one.parent.mkdir(parents=True)
            source_two.parent.mkdir(parents=True)
            source_one.write_bytes(b"one")
            source_two.write_bytes(b"two")

            with patch("wavvy.git_repo_root", return_value=root), patch(
                "wavvy.get_audio_info",
                return_value={"duration": 120.0, "sample_rate": 48000},
            ), patch("wavvy.compute_sha256", return_value="abc123"):
                result = validate_project(ProjectPaths(series))

            self.assertTrue(result.is_valid, result.errors)
            self.assertEqual(len(result.tracks), 2)
            self.assertEqual(result.tracks[0].path, source_one)
            self.assertEqual(result.tracks[0].report_filename, "01__One__Warm__RnB__90.wav")

    def test_check_state_warns_on_final_sources_with_stale_draft_text(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            series = make_series(root, CONCEPT_FINAL + "\n## 미해결 / 다음 라운드\n\n- DRAFT Suno 생성/검수\n")
            result = check_state(series, root, {"phase": "source_final"})
            self.assertEqual(result["result"], "PASS")
            self.assertIn(
                "concept.md contains Final Track Sources but still has draft/Suno stale status text",
                result["warnings"],
            )

    def test_uploaded_phase_allows_deleted_local_render_artifacts(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            series = make_series(root, CONCEPT_UPLOADED)
            result = check_state(series, root, {"phase": "uploaded"})
            self.assertEqual(result["result"], "PASS")
            state = result["state"]
            self.assertEqual(state["phase"], "uploaded")
            self.assertEqual(state["artifact_status"]["youtube_upload"], "completed")
            self.assertEqual(state["artifact_status"]["final_mkv"], "deleted_after_upload")
            self.assertEqual(state["artifact_status"]["upload_csv"], "deleted_after_upload")

    def test_bare_uploaded_text_does_not_mark_upload_completed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            concept = CONCEPT_FINAL + "\n## Series Status\n\n- 현재 phase: `uploaded`\n- v0.8 — uploaded 20/20\n"
            series = make_series(root, concept)
            state = build_state(series, root)
            self.assertEqual(state["artifact_status"]["youtube_upload"], "missing")
            self.assertNotEqual(state["phase"], "uploaded")

    def test_not_uploaded_text_does_not_mark_upload_completed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            concept = CONCEPT_FINAL + "\n## Upload Status\n\n- YouTube upload: not uploaded yet\n"
            series = make_series(root, concept)
            state = build_state(series, root)
            self.assertEqual(state["artifact_status"]["youtube_upload"], "missing")

    def test_upload_ready_gate_passes_when_upload_already_completed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            series = make_series(root, CONCEPT_UPLOADED)
            result = run_gate(series, root, "upload-ready", {"is_valid": True, "errors": [], "warnings": []})
            self.assertEqual(result["result"], "PASS")
            checks = {check["name"]: check for check in result["checks"]}
            self.assertEqual(checks["youtube_upload_status"]["status"], "PASS")
            self.assertEqual(checks["youtube_upload_status"]["detail"], "completed")
            self.assertNotIn("youtube_upload_completed", checks)

    def test_upload_ready_gate_passes_before_upload_without_failed_upload_check(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            series = make_series(root)
            output = series / "output"
            (output / "final.mkv").write_bytes(b"placeholder")
            (output / "upload.csv").write_text("video_path,title\nx,y\n", encoding="utf-8")
            (output / "youtube_subtitles_ko_no_timing.txt").write_text("lyrics\n", encoding="utf-8")

            with patch("wavvy_harness.gate._has_media_stream", return_value=True):
                result = run_gate(series, root, "upload-ready", {"is_valid": True, "errors": [], "warnings": []})

            self.assertEqual(result["result"], "PASS")
            checks = {check["name"]: check for check in result["checks"]}
            self.assertEqual(checks["youtube_upload_status"]["status"], "PASS")
            self.assertEqual(checks["youtube_upload_status"]["detail"], "pending")
            self.assertNotIn("youtube_upload_completed", checks)

    def test_ssot_hygiene_scopes_stale_terms_to_entrypoints(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for rel in [
                "MASTER/SSOT.md",
                "MASTER/ai/RUNTIME_RULES.md",
                "MASTER/MANAGER.md",
                "MASTER/WORKFLOWS.md",
                "MASTER/cli/SPEC.md",
                "MASTER/youtube/YOUTUBE.md",
            ]:
                path = root / rel
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(
                    "MASTER/SSOT.md\nMASTER/ai/RUNTIME_RULES.md\nMASTER/MANAGER.md\n"
                    "MASTER/WORKFLOWS.md\nMASTER/cli/SPEC.md\n",
                    encoding="utf-8",
                )
            (root / "AGENTS.md").write_text(
                "MASTER/SSOT.md\nMASTER/ai/RUNTIME_RULES.md\nMASTER/MANAGER.md\nMASTER/WORKFLOWS.md\nMASTER/cli/SPEC.md\n",
                encoding="utf-8",
            )
            (root / "CLAUDE.md").write_text(
                "MASTER/SSOT.md\nMASTER/ai/RUNTIME_RULES.md\nMASTER/MANAGER.md\nMASTER/WORKFLOWS.md\nMASTER/cli/SPEC.md\n",
                encoding="utf-8",
            )
            (root / "wavvy.md").write_text("Wavvy\n", encoding="utf-8")
            (root / ".ai").mkdir()
            (root / ".ai" / "state.json").write_text(
                json.dumps(
                    {
                        "authoritative_docs": [
                            "MASTER/SSOT.md",
                            "MASTER/ai/RUNTIME_RULES.md",
                            "MASTER/cli/SPEC.md",
                        ]
                    }
                ),
                encoding="utf-8",
            )
            archive = root / ".ai" / "peer-review" / "runs" / "old.md"
            archive.parent.mkdir(parents=True)
            archive.write_text("VIBEM final.mp4 Video Crossfade 필수\n", encoding="utf-8")

            checks = run_ssot_hygiene(root)
            required = [check for check in checks if check.get("required")]
            self.assertTrue(required)
            self.assertTrue(all(check["status"] == "pass" for check in required), checks)


if __name__ == "__main__":
    unittest.main()
