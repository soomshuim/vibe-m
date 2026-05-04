# Peer Agent Review

| Field | Value |
|---|---|
| Target | claude |
| Mode | review |
| Project | wavvy |
| Repo | /Users/zen/Project/wavvy |
| Git repo | yes |
| Branch | master |
| Created | 2026-05-02 03:03:24 KST |
| Exit code | 0 |

## Request

Play run: /Users/zen/Project/wavvy/.ai/pipeline/runs/20260502-025736_ssot-harness-audit
Review the team analysis artifact for this play harness run.
Source artifact: /Users/zen/Project/wavvy/.ai/pipeline/runs/20260502-025736_ssot-harness-audit/01-team-analysis.md

## Artifact Content

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

## Context

### Git Status

```
?? .ai/pipeline/
```

### Diff Stat

```
(no unstaged diff stat)
```

## Peer Result

I now have sufficient evidence to deliver the peer review. Here is my assessment:

---

### Peer Review Verdict
- **Result: PASS**
- **Confidence: high**

### Findings

| Severity | File/Area | Issue | Recommendation |
|---|---|---|---|
| Low | Finding 2 wording | The analysis says `run_gate` emits a `youtube_upload_completed` check that "would be FAIL while the gate can still return PASS." This is accurate (`gate.py:129` adds a non-blocking check), but the description could be more precise: the semantic confusion is that a *check item* shows FAIL status inside an overall PASS gate result — not that it causes incorrect gating behavior. The gate logic itself is correct for the post-upload case. | Clarify in implementation that the issue is check-level presentation noise, not a gating logic bug. |
| Low | Finding 8 series list | The analysis claims "newer active series such as 13-00, 15-00, 20-00, and 22-00" are missing from the YouTube tag mapping. Verified: all four exist as `SERIES/*/concept.md` and are absent from `YOUTUBE.md` §6. Additionally, `wavvy.md` §6 is also missing 12-00, 13-00, 15-00, 20-00, 22-00 — slightly wider drift than the analysis states. | Note wavvy.md §6 series mapping drift alongside YOUTUBE.md §6 during implementation. |
| Info | Finding 3 precision | `_upload_completed()` (`state.py:75-83`) uses `\buploaded\b` with `IGNORECASE`. The analysis correctly flags this as too broad. Worth noting: the current `SSOT.md` phase contract (line 36) uses the exact word "uploaded" as a phase name, so the regex is not just matching arbitrary text — it's also matching a legitimate SSOT term that could appear in future concept docs in non-upload-status contexts. | No change needed to analysis; implementation should tighten as recommended. |

### Verified Findings Summary

All 9 findings were verified against repository source:

1. **State contract conflict owners** — **Confirmed**. `state.py:22-27` `AUTHORITATIVE_DOCS` omits `MASTER/SSOT.md`, `MASTER/ai/RUNTIME_RULES.md`, `MASTER/cli/SPEC.md`. These are in `SSOT.md` priority table and `AGENTS.md` router.
2. **upload-ready gate semantics** — **Confirmed**. `gate.py:129` emits `youtube_upload_completed` as a non-blocking check that shows FAIL within a PASS gate.
3. **Upload inference too broad** — **Confirmed**. `state.py:78` `\buploaded\b` is overly permissive.
4. **Video xfade scope disagreement** — **Confirmed**. `RUNTIME_RULES.md:38` correctly scopes xfade; `WORKFLOWS.md:117` and `CLI/SPEC.md:123` present it as unconditional.
5. **Lyrics parentheses contradiction** — **Confirmed**. `LYRICS.md` §1.2 line 37 forbids parentheses; §2.2 line 101 allows them for vocal meta.
6. **YouTube title format conflict** — **Confirmed**. `wavvy.md:102` uses `[Playlist] [HH:MM] Wavvy | ...`; `YOUTUBE.md:14` uses `Playlist | HH:MM | ... | Wavvy`. Different bracket conventions, different Wavvy placement.
7. **MANAGER hierarchy stale** — **Confirmed**. `MANAGER.md:22` still says "최상위"; `SSOT.md:17` places it at priority 5.
8. **YouTube brand/tag drift** — **Confirmed**. `YOUTUBE.md:109-110` uses lowercase `wavvy`; `wavvy.md:94` uses `Wavvy`. Series 13-00, 15-00, 20-00, 22-00 exist in repo but missing from tag mapping.
9. **Doctor lacks doc-drift checks** — **Confirmed**. `doctor.py:96-138` only checks env/deps, no SSOT/router/state consistency.

### Test And Acceptance Notes

- No code changes exist in this artifact — it is a planning/analysis document. No tests to run.
- The analysis was verified by reading all 12 source files referenced across the 9 findings.
- `python3 wavvy.py doctor --json` PASS was claimed and is consistent with doctor only checking env deps.
- The existing test suite (`tests/test_harness.py`) covers state/gate behavior but does not cover the doc-drift scenarios identified here — this gap is correctly identified by Finding 9.

### Follow-Up For Requesting Agent

1. **Proceed with implementation** using this analysis as the basis. All findings are evidence-backed and actionable.
2. **Minor addition**: When fixing Finding 8 (YouTube tag mapping), also update `wavvy.md` §6 Series Mapping, which is missing 12-00, 13-00, 15-00, 20-00, 22-00.
3. **Clarify Finding 2** during implementation: the fix should address check-level presentation (removing or renaming the non-blocking `youtube_upload_completed` check in the `upload-ready` stage), not the gate pass/fail logic which is already correct.
4. **Scope and recommendations are sound** — no out-of-scope creep detected, append-only policy for HANDOFF/SESSION is correctly preserved.

