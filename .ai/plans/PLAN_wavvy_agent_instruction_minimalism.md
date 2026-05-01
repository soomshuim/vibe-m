# PLAN: Wavvy Agent Instruction Minimalism

Date: 2026-05-02
Status: Draft for peer plan review
Source Team Review: `meetings/2026-05-02_wavvy-agent-instruction-minimalism-team.md`
Team Review PASS: `.ai/peer-review/runs/20260502-011803-claude-review-65918.md`

## Goal

Convert Wavvy's agent entrypoint docs from instruction stores into thin context routers.

The repo should keep always-loaded files small and route detailed instructions to context-owned docs:

- `AGENTS.md`: canonical agent-agnostic router
- `CLAUDE.md`: Claude-specific overlay that points to the same router targets
- `MASTER/ai/RUNTIME_RULES.md`: hard constraints, media execution cautions, approval/safety rules
- Existing owners remain in place: `MASTER/SSOT.md`, `MASTER/WORKFLOWS.md`, `MASTER/cli/SPEC.md`, `MASTER/MANAGER.md`, `MASTER/youtube/YOUTUBE.md`, rubrics/style/lyrics docs

External research is skipped because the local AI Ops skill/reference already contains the principle:

- `/Users/zen/Project/lenny/skills/ai-ops-expert/SKILL.md`
- `/Users/zen/Project/lenny/skills/ai-ops-expert/references/harness-engineering.md`
- `/Users/zen/Project/lenny/skills/ai-ops-expert/references/templates.md`

## Step 0: Baseline Isolation

The working tree already contains the prior Wavvy harness work (`doctor/state/gate`, `.ai/state.json`, 20-00 `uploaded` correction, tests, peer review artifacts).

Policy:

- Do not mix semantic ownership in documentation.
- Do not revert prior harness changes.
- Do not commit automatically unless the user explicitly requests it.
- If a commit is requested later, stage prior harness work and this instruction-minimalism refactor as separate logical commits.
- During this implementation, keep changed files explicit and verify with `git diff --check` plus targeted tests.

This is the no-commit equivalent of "clean base first" under the current session constraints.

## Target File Changes

### 1. Add `AGENTS.md`

Role: canonical router for Codex and other agent-compatible tools.

Must include:

- Mission
- Repository map
- Context router table
- Working agreements
- Verification commands
- Constraints
- Done criteria

Must not include:

- Long workflow tutorials
- Duplicated CLI spec
- Detailed genre/rubric rules
- Stale phase assumptions for 20-00

### 2. Rewrite `CLAUDE.md`

Role: Claude Code overlay, not independent SSOT.

Must include:

- One-line identity
- "Use `AGENTS.md` as canonical router" statement
- Claude-specific notes only
- Minimal command list
- Pointer to `MASTER/ai/RUNTIME_RULES.md` for safety/media rules

Target: under 80 lines.

### 3. Add `MASTER/ai/RUNTIME_RULES.md`

Role: owner of runtime hard constraints and safety/approval rules.

Contents:

- No Pydub; pure FFmpeg
- acrossfade vs xfade distinction
- fail-fast validation
- image-mode vs video-mode distinction
- complex media task protocol
- user confirmation/approval rule preserved
- verification gates
- local large artifact retention policy: uploaded series may delete `final.mkv/upload.csv`

Must link instead of duplicating:

- Workflow details → `MASTER/WORKFLOWS.md`
- CLI command details → `MASTER/cli/SPEC.md`
- phase/artifact semantics → `MASTER/SSOT.md`
- quality gates → `MASTER/MANAGER.md`

### 4. Update `MASTER/SSOT.md`

Add `MASTER/ai/RUNTIME_RULES.md` to Conflict Order.

Proposed row:

| Priority | File / Artifact | Owns | Notes |
|---|---|---|---|
| 4 | `MASTER/ai/RUNTIME_RULES.md` | runtime hard constraints, media execution cautions, approval/safety rules | Entry files route here; workflow details still live in `WORKFLOWS.md` / `cli/SPEC.md`. |

Then increment the priorities below it.

### 5. Update Records

- `CHANGELOG.md`: Added/Changed entry for thin router docs.
- `.ai/SESSION.md`: note completed instruction-minimalism refactor.
- `.ai/HANDOFF.md`: append final state.
- `reviews/YYYY-MM-DD_wavvy-agent-instruction-minimalism.md`: Director record.

## Drift Checks

Use deterministic text checks after implementation:

```bash
wc -l AGENTS.md CLAUDE.md MASTER/ai/RUNTIME_RULES.md
rg -n "사용자 확인 필수|user confirmation|approval" AGENTS.md CLAUDE.md MASTER/ai/RUNTIME_RULES.md
rg -n "Video Crossfade 필수|vfade --test.*pack|loop_xfade" AGENTS.md CLAUDE.md MASTER/ai/RUNTIME_RULES.md MASTER/WORKFLOWS.md
rg -n "MASTER/SSOT.md|MASTER/WORKFLOWS.md|MASTER/cli/SPEC.md|MASTER/ai/RUNTIME_RULES.md" AGENTS.md CLAUDE.md
```

Pass expectations:

- `AGENTS.md` and `CLAUDE.md` both point to `MASTER/SSOT.md`, `MASTER/WORKFLOWS.md`, `MASTER/cli/SPEC.md`, and `MASTER/ai/RUNTIME_RULES.md`.
- `사용자 확인 필수` or equivalent approval policy appears in `MASTER/ai/RUNTIME_RULES.md`; entrypoint docs only route to it.
- `Video Crossfade 필수` does not appear as an unconditional entrypoint rule.
- Video xfade guidance is scoped to video-loop packaging, not image-mode or uploaded-state workflows.

## Regression Smoke

Run:

```bash
python3 -m py_compile wavvy.py wavvy_harness/*.py
python3 -m unittest tests/test_harness.py
python3 wavvy.py doctor --json | python3 -m json.tool >/tmp/wavvy-doctor.json
python3 wavvy.py validate SERIES/20-00
python3 wavvy.py state SERIES/20-00 --check --json | python3 -m json.tool >/tmp/wavvy-state.json
python3 wavvy.py gate SERIES/20-00 --stage uploaded --json | python3 -m json.tool >/tmp/wavvy-uploaded-gate.json
python3 wavvy.py gate SERIES/20-00 --stage upload-ready --json | python3 -m json.tool >/tmp/wavvy-upload-ready-gate.json
git diff --check
```

Pass expectations:

- All commands exit 0.
- `state` phase is `uploaded`.
- `final_mkv` and `upload_csv` are `deleted_after_upload`.
- `uploaded` gate PASS.
- `upload-ready` gate PASS because upload completion evidence exists.

## Acceptance Criteria

- `AGENTS.md` exists and is the canonical router.
- `CLAUDE.md` is under 80 lines and does not own duplicated workflow details.
- `MASTER/ai/RUNTIME_RULES.md` exists and owns hard constraints/safety/media execution cautions.
- `MASTER/SSOT.md` includes `RUNTIME_RULES.md` in conflict order.
- User confirmation/approval rule is preserved, not removed.
- No stale unconditional "video crossfade required for every pack" rule remains in entrypoint docs.
- Drift checks pass.
- Regression smoke passes.
- Claude implementation review PASS after Director work.

## Non-Goals

- No external research.
- No `.claude/rules/` migration in this pass.
- No code behavior change except docs if avoidable.
- No automatic commit/push unless explicitly requested.
