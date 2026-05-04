# Peer Agent Review

| Field | Value |
|---|---|
| Target | claude |
| Mode | plan |
| Project | wavvy |
| Repo | /Users/zen/Project/wavvy |
| Git repo | yes |
| Branch | master |
| Created | 2026-05-02 03:07:16 KST |
| Exit code | 0 |

## Request

Play run: /Users/zen/Project/wavvy/.ai/pipeline/runs/20260502-025736_ssot-harness-audit
Review the implementation plan artifact for this play harness run.
Source artifact: /Users/zen/Project/wavvy/.ai/pipeline/runs/20260502-025736_ssot-harness-audit/03-plan.md

## Artifact Content

# Plan

Run: `20260502-025736_ssot-harness-audit`

## Goal

Resolve SSOT/document conflicts and strengthen harness checks without changing media outputs or rewriting historical handoff/session archives.

## File Changes

### Harness Code

1. `wavvy_harness/state.py`
   - Include `MASTER/SSOT.md`, `MASTER/ai/RUNTIME_RULES.md`, and `MASTER/cli/SPEC.md` in `authoritative_docs`.
   - Tighten upload completion detection:
     - prefer explicit `## Upload Status`;
     - accept real YouTube URL in legacy header;
     - avoid bare `uploaded` as global evidence.

2. `wavvy_harness/gate.py`
   - For `upload-ready`, report upload status as pending/completed without showing a failed `youtube_upload_completed` check inside an otherwise passing ready gate.
   - Keep `uploaded` as the only stage requiring completed upload evidence.

3. `wavvy_harness/doctor.py`
   - Add deterministic SSOT hygiene checks:
     - required router/SSOT docs exist;
     - `AGENTS.md` and `CLAUDE.md` route to the core docs;
     - entrypoint docs do not reintroduce stale `VIBEM`/`final.mp4`/unconditional crossfade patterns;
     - `.ai/state.json` includes current conflict-owner docs;
     - tracked `.DS_Store` files are absent.

4. `wavvy.py`
   - Update validation docstrings to reflect MP3/WAV and image-mode loop sources.

5. `tests/test_harness.py`
   - Add tests for:
     - authoritative docs include SSOT/runtime/CLI;
     - `upload-ready` passes for pre-upload local artifacts without a failed upload-completed check;
     - `not uploaded` text is not upload completion evidence;
     - doctor SSOT hygiene passes on a minimal fixture.

### Docs

6. `MASTER/WORKFLOWS.md`
   - Scope vfade workflow to video-loop packaging only.
   - State that image-mode packaging and already-uploaded state checks do not require vfade.

7. `MASTER/cli/SPEC.md`
   - Update directory/validate/pack docs for `loop.mp4` or `loop.png/jpg/jpeg`.
   - Scope video xfade to video-loop sources and clarify that `pack` alone is acceptable for image mode.
   - Add `doctor/state/gate/finalize-upload` to command section if missing.

8. `MASTER/lyrics/LYRICS.md`
   - Resolve parentheses conflict by scoping:
     - prompt-only mode: no parentheses;
     - structure mode: one optional parenthetical metadata envelope only.

9. `MASTER/MANAGER.md`
   - Make `MASTER/SSOT.md` the conflict-order owner.
   - Reframe MANAGER as quality-gate fallback, not universal top-level SSOT.

10. `MASTER/youtube/YOUTUBE.md`
    - Brand case fix: `Wavvy`.
    - Add newer series mapping rows for 13-00, 15-00, 20-00, 22-00.
    - State that per-series `concept.md` may explicitly override generic tag mappings.

11. `wavvy.md`
   - Replace duplicated YouTube title format with pointer to `MASTER/youtube/YOUTUBE.md`.
   - Add current active series rows where missing, including 12-00, 13-00, 15-00, 20-00, and 22-00.

12. `.ai/state.json`
    - Rewrite through `python3 wavvy.py state SERIES/20-00 --write --phase uploaded --if-match <current>`.

### Record Artifacts

13. Play artifacts
    - Fill `02-review.md`, `04-plan-review.md`, `05-implementation.md`, `06-record.md`.

14. Durable project record
    - Append current result to `.ai/SESSION.md` and `.ai/HANDOFF.md`.
    - Add a changelog bullet for this SSOT/harness hardening pass.

## Acceptance Criteria

- `python3 -m py_compile wavvy.py wavvy_harness/*.py` PASS.
- `python3 -m unittest tests/test_harness.py` PASS.
- `python3 wavvy.py doctor --json` PASS and includes SSOT hygiene checks.
- `python3 wavvy.py state SERIES/20-00 --check --json` PASS.
- `python3 wavvy.py gate SERIES/20-00 --stage upload-ready --json` PASS without a failed `youtube_upload_completed` check.
- `python3 wavvy.py gate SERIES/20-00 --stage uploaded --json` PASS.
- `python3 wavvy.py validate SERIES/20-00` PASS.
- `git diff --check` PASS.
- No tracked `.DS_Store` files.

## Risks

- Upload-completion inference must not break current 20-00 uploaded state or legacy uploaded series with only a YouTube URL.
- Doc cleanup should not rewrite historical archives; old handoff/session entries are audit trail, not active SSOT.
- `doctor` hygiene checks must be narrow enough to avoid failing on archived peer-review text that intentionally mentions stale terms.

## Context

### Git Status

```
?? .ai/peer-review/runs/20260502-030039-claude-review-54952.md
?? .ai/pipeline/
```

### Diff Stat

```
(no unstaged diff stat)
```

## Peer Result



### Peer Review Verdict
- Result: **PASS**
- Confidence: **high**

### Findings

| Severity | File/Area | Issue | Recommendation |
|---|---|---|---|
| Medium | `wavvy_harness/state.py` `_upload_completed` | Plan says "prefer explicit `## Upload Status`; accept real YouTube URL; avoid bare `uploaded`" but does not specify the replacement regex patterns. Current patterns (`\buploaded\b`, `` `uploaded` ``) are over-broad and would match status text like "현재 phase: `uploaded`" or "v0.8 — uploaded 20/20" which are not primary upload evidence. Implementer needs precise pattern spec to avoid regression. | Define the exact new pattern set in the plan, e.g.: (1) `## Upload Status` section containing "completed", (2) `YouTube upload completed` / `YouTube 업로드 완료` / `업로드 완료`, (3) real `youtube.com`/`youtu.be` URL. Drop bare `\buploaded\b` and `` `uploaded` `` patterns. Add a unit test for text containing "phase: uploaded" that must NOT trigger completion. |
| Medium | `wavvy_harness/gate.py` upload-ready | Plan says "report upload status as pending/completed without showing a failed `youtube_upload_completed` check" but doesn't specify the mechanism. Current line 129 emits a check with status `FAIL`. Options: (a) change status to `INFO`/`SKIP`, (b) rename the check and use `PASS` with detail "pending", (c) remove it entirely from `upload-ready`. Each has different downstream parsing implications. | Pick one approach explicitly. Recommend (b): rename to `youtube_upload_status` with status `PASS` and detail `pending` or `completed`. This preserves the info without a misleading FAIL. |
| Medium | `wavvy_harness/doctor.py` SSOT hygiene | Plan lists "entrypoint docs do not reintroduce stale `VIBEM`/`final.mp4`/unconditional crossfade patterns" but doesn't define the exact file scope for this search. If doctor scans the entire repo, it will false-positive on `.ai/peer-review/`, `CHANGELOG.md`, `meetings/`, and `.ai/lessons-learned.md` which legitimately mention these terms. | Explicitly scope the stale-pattern check to `AGENTS.md`, `CLAUDE.md`, `MASTER/ai/RUNTIME_RULES.md` only (the entrypoint docs). The plan's risk section acknowledges this but it should be in the spec, not just the risk notes. |
| Low | Acceptance criteria | `python3 wavvy.py gate SERIES/20-00 --stage upload-ready --json` PASS without failed upload check — but 20-00 is already uploaded, so this gate trivially passes today without any code change. It doesn't actually verify the plan's fix for pre-upload `upload-ready` gates. | Add a test fixture (in `tests/test_harness.py`) with a pre-upload series that has `final.mkv` + `upload.csv` + subtitle but no upload evidence. Run `upload-ready` gate on that fixture and verify PASS with no FAIL-status `youtube_upload_completed` check. |
| Low | `wavvy.md` title format | Plan says "Replace duplicated YouTube title format with pointer to `MASTER/youtube/YOUTUBE.md`" but doesn't specify what replaces the current format block in section 7. The current format (`[Playlist] [HH:MM] Wavvy | {문구}, {장르}`) diverges from YOUTUBE.md's format. Removing it without a clear pointer sentence risks losing the thumbnail-specific format context. | Specify the replacement text: keep the section header, replace the format block with a one-liner like "See `MASTER/youtube/YOUTUBE.md` for canonical title format." Preserve the thumbnail branding text separately if it differs from YouTube title. |
| Low | `MASTER/youtube/YOUTUBE.md` series additions | Plan says add rows for 13-00, 15-00, 20-00, 22-00 but doesn't specify genre/tag values for each. Implementer must look up each series `concept.md`. | Either list the genre+tag values in the plan, or note that the implementer must read `SERIES/{13,15,20,22}-00/concept.md` headers for each. |
| Low | Sequencing | Item 12 (state.json rewrite) depends on item 1 (state.py `AUTHORITATIVE_DOCS` update) completing first, since `--write` calls `build_state()` which reads the constant. This dependency is implicit. | Add a sequencing note: "state.json rewrite must run after state.py is deployed so the new authoritative_docs appear in the written state." |

### Test And Acceptance Notes

- **Existing tests pass**: Current `tests/test_harness.py` has 5 tests covering state inference, stale draft warning, uploaded phase with deleted artifacts, and upload-ready gate with completed upload. These provide a baseline.
- **Plan adds 4 new tests** (authoritative docs check, upload-ready pre-upload, "not uploaded" negative case, doctor SSOT hygiene). Good coverage for the new functionality.
- **Missing negative test**: No test verifying that text like `현재 phase: uploaded` does NOT trigger `_upload_completed`. This is critical given the tightening change.
- **Missing pre-upload upload-ready fixture test**: The acceptance criteria test against 20-00 (already uploaded) which doesn't exercise the gate.py fix. A fixture-based test in `test_harness.py` is specified in the plan (item 5 bullet 2) which is correct — but the CLI acceptance criterion should also reference it.
- **doctor SSOT hygiene test**: Plan says "doctor SSOT hygiene passes on a minimal fixture" — good, but should also verify it does NOT fail when stale terms appear in non-entrypoint files (false-positive guard).
- **`py_compile` and `unittest` gates** are standard and appropriate.
- **`git diff --check`** is appropriate for whitespace/merge marker detection.

### Follow-Up For Requesting Agent

1. **Address the Medium findings** before implementation: specify exact `_upload_completed` replacement patterns, pick one gate.py UX approach, and scope doctor stale-pattern search to explicit file list.
2. **Add the missing negative test** for `_upload_completed` (text with bare "uploaded" in non-evidence context must return `False`).
3. **Note the sequencing dependency** between state.py modification and state.json rewrite.
4. **Proceed with implementation** — the plan is structurally sound and addresses real, verified issues. The findings above are refinements, not blockers.

