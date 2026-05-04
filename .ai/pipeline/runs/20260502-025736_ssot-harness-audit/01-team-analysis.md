# Team Analysis

Run: `20260502-025736_ssot-harness-audit`
Request: `-play 프로젝트 전반의 모든 SSOT 정책과 문서간 중복-충돌사항들, 하네스 셋팅 점검하고 문제점을 꼼꼼하게 분석해서 해결해줘.`

## Current State

- Repo was clean before this play run except the newly initialized `.ai/pipeline/` artifact directory.
- `python3 wavvy.py doctor --json`: PASS.
- `python3 wavvy.py state SERIES/20-00 --check --json`: PASS, phase `uploaded`.
- `python3 wavvy.py gate SERIES/20-00 --stage uploaded --json`: PASS.
- Entrypoints are already thin: `AGENTS.md` is canonical router, `CLAUDE.md` is Claude overlay.

## Findings

1. **State contract omits its own conflict owners.**
   `.ai/state.json` and `wavvy_harness/state.py` list authoritative docs as `wavvy.md`, `MANAGER`, `WORKFLOWS`, `YOUTUBE`, and series concept only. This conflicts with `AGENTS.md` and `MASTER/SSOT.md`, which make `MASTER/SSOT.md`, `MASTER/ai/RUNTIME_RULES.md`, and CLI spec part of the routing and phase contract.

2. **`upload-ready` gate has a semantic contradiction.**
   `upload-ready` means ready before upload, but `run_gate` emits a `youtube_upload_completed` check. On a pre-upload series with local render/subtitles present, this check would be FAIL while the gate can still return PASS. The result is confusing and undermines the phase model.

3. **Upload completion inference is too broad.**
   `_upload_completed()` treats bare `uploaded` anywhere in `concept.md` as evidence. This is acceptable for current `20-00` because it has an explicit `Upload Status`, but it can falsely classify future docs that mention an uploaded phase or say "not uploaded".

4. **Runtime docs and workflow/CLI docs still disagree on video xfade scope.**
   `MASTER/ai/RUNTIME_RULES.md` correctly says video xfade is only required for video-loop packaging and not image-mode/uploaded state checks. `MASTER/WORKFLOWS.md` and `MASTER/cli/SPEC.md` still present `vfade -> pack` as an unconditional packaging workflow and describe `loop.mp4` as required even though the implementation supports image mode with `loop.png/jpg/jpeg`.

5. **Lyrics SSOT contains an internal parentheses contradiction.**
   `MASTER/lyrics/LYRICS.md` §1.2 says prompt mode must use no parentheses. §2.2 says parentheses are a valid SSOT form for vocal meta + prompt. Both can be valid only with scoped wording: prompt-only mode defaults to no parentheses; structure mode may use one parenthetical metadata envelope.

6. **Project identity and YouTube title SSOT conflict.**
   `wavvy.md` still provides a separate YouTube title format (`[Playlist] [HH:MM] Wavvy | ...`) while `MASTER/youtube/YOUTUBE.md` owns the current `Playlist | HH:MM | ... | Wavvy` format. This is a duplicated policy likely to drift.

7. **Manager hierarchy is stale after the SSOT refactor.**
   `MASTER/MANAGER.md` still presents itself as the top of the whole document hierarchy and only names `CLAUDE.md` as an execution summary. The current SSOT contract makes MANAGER the quality-gate fallback, not the universal conflict resolver.

8. **YouTube SSOT has small brand/template drift.**
   The template uses lowercase `wavvy` in `Music:` and copyright lines while current brand and series metadata use `Wavvy`. Series tag mapping also lacks newer active series such as 13-00, 15-00, 20-00, and 22-00.

9. **Harness has no deterministic doc-drift check.**
   Peer reviews previously called out router drift checks as optional. For this request, doctor should cover the cheap invariants: required SSOT docs exist, router docs point to core targets, entrypoints do not reintroduce stale project/output strings, `.ai/state.json` includes current conflict owners, and `.DS_Store` files are not tracked.

## Recommendation

Implement a focused SSOT hardening pass:

- Update `wavvy_harness/state.py` and `.ai/state.json` so state reports the same conflict-owner docs as `MASTER/SSOT.md`.
- Fix `upload-ready` gate semantics and tighten upload-completion inference.
- Extend `doctor` with deterministic SSOT/router/state hygiene checks.
- Update tests to lock these behaviors.
- Clean the duplicated/conflicting wording in `MASTER/WORKFLOWS.md`, `MASTER/cli/SPEC.md`, `MASTER/lyrics/LYRICS.md`, `MASTER/MANAGER.md`, `MASTER/youtube/YOUTUBE.md`, `wavvy.md`, and targeted code docstrings.
- Preserve historical `.ai/HANDOFF.md` / `.ai/SESSION.md` as append-only archives; do not rewrite old history beyond adding this run's record.

## Scope

In scope:

- Harness code and unit tests.
- Current SSOT/routing/master docs.
- Current `.ai/state.json` rewrite through `wavvy.py state --write`.
- Play artifact record and session/handoff update.

Out of scope:

- Rewriting old handoff/session history.
- Regenerating large media.
- Committing/pushing unless explicitly requested after the run.
