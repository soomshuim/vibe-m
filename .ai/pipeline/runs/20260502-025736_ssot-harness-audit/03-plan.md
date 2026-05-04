# Plan

Run: `20260502-025736_ssot-harness-audit`

## Goal

Resolve SSOT/document conflicts and strengthen harness checks without changing media outputs or rewriting historical handoff/session archives.

## File Changes

### Harness Code

1. `wavvy_harness/state.py`
   - Include `MASTER/SSOT.md`, `MASTER/ai/RUNTIME_RULES.md`, and `MASTER/cli/SPEC.md` in `authoritative_docs`.
   - Tighten upload completion detection:
     - prefer explicit `## Upload Status` section containing `completed`, `YouTube upload completed`, `YouTube 업로드 완료`, or `업로드 완료`;
     - accept a real `youtube.com` or `youtu.be` URL in legacy header metadata;
     - accept explicit Korean/English upload-complete phrases outside the section only when paired with `YouTube`/`업로드`;
     - drop bare `` `uploaded` `` and `\buploaded\b` as global evidence.

2. `wavvy_harness/gate.py`
   - For `upload-ready`, report upload status as pending/completed without showing a failed `youtube_upload_completed` check inside an otherwise passing ready gate.
   - Use a PASS check named `youtube_upload_status` with detail `pending` or `completed`.
   - Keep `uploaded` as the only stage requiring completed upload evidence.

3. `wavvy_harness/doctor.py`
   - Add deterministic SSOT hygiene checks:
     - required router/SSOT docs exist;
     - `AGENTS.md` and `CLAUDE.md` route to the core docs;
     - entrypoint docs do not reintroduce stale `VIBEM`/`final.mp4`/unconditional crossfade patterns, scoped only to `AGENTS.md`, `CLAUDE.md`, and `MASTER/ai/RUNTIME_RULES.md`;
     - `.ai/state.json` includes current conflict-owner docs;
     - tracked `.DS_Store` files are absent.

4. `wavvy.py`
   - Update validation docstrings to reflect MP3/WAV and image-mode loop sources.

5. `tests/test_harness.py`
   - Add tests for:
     - authoritative docs include SSOT/runtime/CLI;
     - `upload-ready` passes for pre-upload local artifacts without a failed upload-completed check;
     - `not uploaded` text is not upload completion evidence;
     - bare `phase: uploaded` / `uploaded 20/20` text is not upload completion evidence;
     - doctor SSOT hygiene passes on a minimal fixture.
     - doctor stale-pattern checks ignore non-entrypoint archive files.

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
    - Add newer series mapping rows for 13-00, 15-00, 20-00, 22-00, using each series `concept.md` header/metadata for genre and tags.
    - State that per-series `concept.md` may explicitly override generic tag mappings.

11. `wavvy.md`
   - Replace duplicated YouTube title format block with a pointer sentence: `YouTube title/description/tag format SSOT: MASTER/youtube/YOUTUBE.md`.
   - Preserve thumbnail branding context separately.
   - Add current active series rows where missing, including 12-00, 13-00, 15-00, 20-00, and 22-00.

12. `.ai/state.json`
    - Rewrite through `python3 wavvy.py state SERIES/20-00 --write --phase uploaded --if-match <current>`.
    - Run only after `wavvy_harness/state.py` is updated, because `--write` reads the new authoritative doc constant.

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
- Unit fixture proves pre-upload `upload-ready` PASS has no failed `youtube_upload_completed` check.
- `python3 wavvy.py gate SERIES/20-00 --stage upload-ready --json` PASS and reports `youtube_upload_status` cleanly for the already-uploaded active series.
- `python3 wavvy.py gate SERIES/20-00 --stage uploaded --json` PASS.
- `python3 wavvy.py validate SERIES/20-00` PASS.
- `git diff --check` PASS.
- No tracked `.DS_Store` files.

## Risks

- Upload-completion inference must not break current 20-00 uploaded state or legacy uploaded series with only a YouTube URL.
- Doc cleanup should not rewrite historical archives; old handoff/session entries are audit trail, not active SSOT.
- `doctor` hygiene checks must be narrow enough to avoid failing on archived peer-review text that intentionally mentions stale terms.
