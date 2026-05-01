# PLAN: Wavvy Harness Setting

- **Date**: 2026-05-02
- **Source analysis**: `meetings/2026-05-02_wavvy-harness-engineering-analysis.md`
- **Claude review gates**:
  - `20260502-002626-claude-review-40431.md` -> NEEDS_USER_DECISION
  - `20260502-003021-claude-review-49474.md` -> PASS

---

## Goal

Make Wavvy safer to resume and operate by adding a deterministic harness layer around the current media workflow.

The MVP must let an agent answer these questions without reading the whole session history:

1. What phase is the active series in?
2. Which artifacts exist and which are missing?
3. Is the project ready for source-final, render-final, or upload-ready work?
4. Are the local tools and cross-agent peer review dependency available?
5. Can the same team-analysis -> Claude-review -> plan -> Claude-plan -> director pipeline be reused for another project?

---

## Non-Goals

- Do not fully split `wavvy.py` into a package.
- Do not backfill every historical `report.json`.
- Do not regenerate `final.mkv` during this implementation.
- Do not automate YouTube browser upload.
- Do not demote `.ai/HANDOFF.md`; keep existing SessionStart hook compatibility.

---

## Phase Semantics

MVP phase enum:

| Phase | Meaning | Required artifacts |
|---|---|---|
| `concept_draft` | Concept exists but track sources are not complete. | `concept.md` |
| `track_source_draft` | Track txt/source work is active. | `input/tracks/*.txt` or explicit draft status |
| `source_final` | Audio, metadata, report, and Final Track Sources are final enough for subtitle/upload prep. | `concept.md`, `## Final Track Sources`, `output/report.json`, audio files |
| `render_final` | Rendered video artifacts exist and match current report. | `output/final.mkv`, `output/upload.csv`, `output/report.json` |
| `upload_ready` | Rendered video plus subtitle/upload support artifacts are present. | render-final artifacts plus subtitles when expected |

Current `SERIES/20-00` phase is `source_final`.

`output/final.mkv` absence is not a source-final failure. It is an upload-ready blocker.

---

## Work Packages

### Sequencing Rule

WP2 must land before WP5 is enabled. `gate` reads `report.json`, so the `pack` writer checks and repeat-aware `crossfade_reduction` fix are preconditions for trusting gate output.

### WP1. Harness Helper Package

Add a small helper package instead of pushing all new logic into `wavvy.py`.

Files:

- `wavvy_harness/__init__.py`
- `wavvy_harness/doctor.py`
- `wavvy_harness/state.py`
- `wavvy_harness/gate.py`

Boundary:

- `wavvy.py` remains the CLI entrypoint.
- New commands import pure helper functions from `wavvy_harness`.
- Helper functions return structured dictionaries so CLI can render text or JSON.

Tests:

- `tests/test_harness.py`
- Use stdlib `unittest`; do not add pytest dependency.

### WP2. P0 Code Fixes

Fix bugs that would corrupt the new gate layer.

- In `pack`, check return values from `generate_provenance`, `generate_upload_csv`, and `generate_report`; fail fast if any writer fails.
- In `generate_report`, compute `crossfade_reduction` as:

```text
sum(original_duration) * repeat - final_duration
```

- Keep historical reports as-is; newly generated reports use the corrected metric.
- Fix low-cost spec drift in user-facing strings:
  - Replace `VIBEM` CLI banners with `WAVVY`.
  - Standardize docs and CLI text on `output/final.mkv`.
  - Remove or replace stale `pack --use-xfade` instructions.
- Fix `preview` image mode by rendering from `loop.png/jpg` when no `loop.mp4` exists.

### WP3. `doctor` Command

Add:

```bash
python3 wavvy.py doctor [--json]
```

Checks:

- Python dependencies: `click`, `ffmpeg`, `pandas`, `ffmpeg_normalize`.
- Binaries: `ffmpeg`, `ffprobe`, `git`.
- Optional binary: `ffmpeg-full` drawtext path.
- Project dependency: `~/Project/claude-center/scripts/peer-agent-review.sh`.
  - Allow override through `WAVVY_PEER_REVIEW_SCRIPT`.
- Disk free space under repo root.
- Writable temp/output smoke check under `.ai/tmp` or system temp.

Exit behavior:

- Exit `0` if required checks pass.
- Exit `1` if any required check fails.
- Optional checks are warnings.

### WP4. `state` Command + Active State File

Add:

```bash
python3 wavvy.py state SERIES/20-00 [--check] [--json]
python3 wavvy.py state SERIES/20-00 --write [--phase source_final]
```

Tracked state file:

- `.ai/state.json`

Schema v1:

```json
{
  "schema": "wavvy.state.v1",
  "updated_at": "ISO-8601",
  "active_series": "SERIES/20-00",
  "phase": "source_final",
  "next_action": "Upload no-timing subtitle txt to YouTube test first; if it fails, test estimated SRT.",
  "artifact_status": {
    "concept_md": "present",
    "final_track_sources": "present",
    "report_json": "present",
    "final_mkv": "missing",
    "upload_csv": "missing",
    "subtitle_txt": "present",
    "subtitle_srt": "present"
  },
  "authoritative_docs": [
    "wavvy.md",
    "MASTER/MANAGER.md",
    "MASTER/WORKFLOWS.md",
    "MASTER/youtube/YOUTUBE.md",
    "SERIES/20-00/concept.md"
  ],
  "blocked_by": [
    "output/final.mkv missing for upload-ready stage"
  ]
}
```

Writer rule:

- Only `wavvy.py state --write` writes `.ai/state.json`.
- Write via temp file and atomic rename.
- Include integer `revision`.
- Support optional `--if-match <revision>` for compare-and-swap style writes; without it, MVP remains last-writer-wins but never writes partial JSON.
- HANDOFF remains append-only archive and hook-compatible summary.

`--check` behavior:

- Compare state file with actual filesystem/concept/report.
- Warn on stale concept TODO/status conflicts.
- Exit `0` when the declared phase is internally consistent.
- Exit `1` when declared phase requirements are missing.

### WP5. `gate` Command

Add:

```bash
python3 wavvy.py gate SERIES/20-00 --stage source-final [--json]
python3 wavvy.py gate SERIES/20-00 --stage render-final [--json]
python3 wavvy.py gate SERIES/20-00 --stage upload-ready [--json]
```

Stage checks:

| Stage | Required checks |
|---|---|
| `source-final` | `validate_project` PASS, `concept.md` present, `Final Track Sources` count equals report/audio count, report present, `concept.md` contains `## YouTube Metadata` or `## YouTube Draft` with title/description/tags |
| `render-final` | source-final PASS, `final.mkv` exists, `upload.csv` exists, media ffprobe audio/video streams present |
| `upload-ready` | render-final PASS, subtitle txt or srt present when state next action references subtitle work |

Final archive rubric:

- If `input/tracks/*.txt` exists, shell rubric scripts can run pre-finalize.
- If txt files are absent and `Final Track Sources` exists, derive the final distribution snapshot from `Final Track Sources` rather than failing with `트랙 파일 없음`.
- MVP does not claim historical rubric PASS unless a stored snapshot exists. If no `rubric_snapshot.json` or report rubric field exists, gate emits `rubric_unverified_after_finalize` warning instead of silently passing or failing.

Exit behavior:

- Exit `0` on PASS.
- Exit `1` on FAIL/BLOCKED.
- JSON contains `stage`, `result`, `checks[]`, `warnings[]`, `blockers[]`.

### WP6. SSOT Contract

Add:

- `MASTER/SSOT.md`

Content:

- Owner/scope/conflict order for identity, quality, workflow, YouTube, per-series concept, output artifacts, `.ai/state.json`, `.ai/HANDOFF.md`.
- Explicit exception rule: per-series `concept.md` may override global brand/genre defaults only in a named override section.
- Enforced by `state --check` warnings for stale TODO/status conflicts.

Initial conflict rules:

1. `concept.md` has `## Final Track Sources` but Series Status still contains `draft`, `DRAFT`, or `Suno 생성/검수`.
2. `.ai/state.json` phase is `source_final` or later but `concept.md` lacks `## Final Track Sources`.
3. `.ai/state.json` next_action mentions upload/render but required render artifacts are missing; warn for `source_final`, block for `upload_ready`.

### WP7. 20-00 Final State Cleanup

Update:

- `SERIES/20-00/concept.md`

Changes:

- Mark top status as `source_final`.
- Replace stale `12 PASS + 8 draft` table language with finalized status or archive it under historical notes.
- Replace stale "현재 draft 8곡 Suno 생성/검수" next action with subtitle upload test and render regeneration note.
- Remove ignored `tools/.DS_Store`; leave empty `tools/` untracked unless future fixtures require it.

### WP8. Cross-Project Pipeline Harness

Add a reusable artifact contract in `claude-center`, because peer review and command routing are centralized there.

Files:

- `/Users/zen/Project/claude-center/scripts/team-director-pipeline.sh`
- `/Users/zen/Project/claude-center/commands/team-director-pipeline.md`

Script responsibility:

- Create a run directory:

```text
<repo>/.ai/pipeline/runs/YYYYMMDD-HHMMSS_<slug>/
  run.json
  01-team-analysis.md
  02-claude-review.md
  03-plan.md
  04-claude-plan.md
  05-director-implementation.md
  final-report.md
```

- Support artifact-mode operation:

```bash
team-director-pipeline.sh init --repo <repo> --slug <slug> --request-file <file>
team-director-pipeline.sh review --repo <repo> --run <run-dir> --analysis-file <file> --target claude
team-director-pipeline.sh plan-review --repo <repo> --run <run-dir> --plan-file <file> --target claude
team-director-pipeline.sh status --repo <repo> --run <run-dir>
```

- Internally call `peer-agent-review.sh --no-handoff` for intermediate peer gates.
- Store verdict, result_file, exit_code, and artifact paths in `run.json`.
- Leave generation of team analysis, plan, and director implementation to the active controller agent or project-specific skill. The harness standardizes IO, gates, and recording.

This is the reusable automation surface. It avoids parsing slash/hyphen triggers and works across projects.

---

## Acceptance Gates

Run from `/Users/zen/Project/wavvy` unless noted.

### Wavvy Gates

```bash
python3 -m py_compile wavvy.py wavvy_harness/*.py
python3 -m unittest tests/test_harness.py
python3 wavvy.py doctor --json
python3 wavvy.py validate SERIES/20-00
python3 wavvy.py state SERIES/20-00 --check --json
python3 wavvy.py gate SERIES/20-00 --stage source-final --json
```

Expected:

- All commands exit `0`.
- `state` reports phase `source_final`.
- `gate --stage source-final` PASS.
- `final_mkv` and `upload_csv` are reported missing only as render/upload blockers.
- Unit tests cover at least:
  - repeat-aware `crossfade_reduction` formula.
  - source-final state inference for a minimal fixture.
  - SSOT conflict detection for Final Track Sources + stale draft text.

Expected negative gate:

```bash
python3 wavvy.py gate SERIES/20-00 --stage upload-ready --json
```

Expected:

- Exit nonzero.
- JSON includes blocker for missing `output/final.mkv` and `output/upload.csv`.

### Cross-Project Harness Gates

Run from `/Users/zen/Project/claude-center`.

```bash
bash scripts/team-director-pipeline.sh --help
bash scripts/team-director-pipeline.sh init --repo /tmp --slug smoke --request-text "smoke"
```

Expected:

- Help exits `0`.
- Init creates a run directory with `run.json` and placeholder stage files.
- No peer review is called during `init`.

### Git / Drift Gates

```bash
git -C /Users/zen/Project/wavvy diff --check
git -C /Users/zen/Project/claude-center diff --check
```

Expected:

- Both pass.

---

## Director Work Allocation

| Role | Responsibility | Files |
|---|---|---|
| Engineering Lead | Implement helper package, CLI commands, P0 code fixes | `wavvy.py`, `wavvy_harness/*` |
| AI Ops Expert | State schema, SSOT doc, phase semantics, cross-project pipeline contract | `.ai/state.json`, `MASTER/SSOT.md`, claude-center pipeline files |
| Product Leader | 20-00 state cleanup and next-action wording | `SERIES/20-00/concept.md` |
| QA Reviewer | Run gates and verify expected negative upload-ready failure | command outputs, reviews record |

---

## Risks

- Cross-repo change risk: Wavvy and claude-center are separate git repositories. Record/commit must be handled separately.
- Claude peer gates are slow. Use them for review/plan gates, not every local edit loop.
- `.ai/state.json` can become stale if agents edit it manually. Mitigation: writer rule plus `state --check`.
- `published` is intentionally excluded from MVP because no YouTube ID ledger exists yet.

---

## Rollback

- Revert new commands by removing CLI registrations and `wavvy_harness/`.
- Remove `.ai/state.json` and `MASTER/SSOT.md` if state contract proves wrong.
- Cross-project pipeline files in claude-center are additive; removing them does not affect existing `peer-agent-review.sh`.
