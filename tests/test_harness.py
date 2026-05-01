import json
import tempfile
import unittest
from pathlib import Path

from wavvy import TrackInfo, generate_report
from wavvy_harness.gate import run_gate
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
            state = build_state(series, root)
            self.assertEqual(state["phase"], "source_final")
            self.assertEqual(state["artifact_status"]["final_track_sources_count"], 2)
            self.assertEqual(state["artifact_status"]["report_tracks"], 2)

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

    def test_upload_ready_gate_passes_when_upload_already_completed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            series = make_series(root, CONCEPT_UPLOADED)
            result = run_gate(series, root, "upload-ready", {"is_valid": True, "errors": [], "warnings": []})
            self.assertEqual(result["result"], "PASS")


if __name__ == "__main__":
    unittest.main()
