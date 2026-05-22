# Team Model Orchestrator Worker Dispatch

You are running as worker `worker-02` for this `-play`/`-director` orchestration run.

## Non-Negotiable Rules

- You are not alone in the codebase; do not revert edits made by others.
- Preserve unrelated dirty files. Do not touch `.ai/SESSION.md` or `.ai/HANDOFF.md` unless the controller explicitly assigned those files.
- Stay inside the assigned responsibility and make the smallest coherent change that satisfies it.
- Stay inside the assigned write scope listed below. If no write scope is assigned, read-only evidence/release/judgment workers must complete by reporting findings without edits; implementation or repair workers must report the block instead.
- Do not invoke Claude, Codex, or peer-agent-review from inside the worker.
- Final response must include: Result, Changed files, Verification, Risks.

## Repository

- Repo: /Users/zenkim_office/Project/wavvy
- Play run: /Users/zenkim_office/Project/wavvy/.ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness
- Orchestrator: /Users/zenkim_office/Project/wavvy/.ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator

## Request

wavvy 전용 작사 스킬을 만들고 싶어. 필요한 자료를 리서치하고 스킬과 에이전트 하네스를 구성해줘. -play


## Worker Responsibility

- Persona: ai-ops-expert
- Execution profile: senior
- Legacy role alias: senior
- Difficulty: high
- Risk: high
- Responsibility: Create the Wavvy lyric-writing skill and durable skill contract from the research baseline. Own only skill/spec files; do not edit CLI, harness code, tests, or release docs.

## Assigned Write Scope

- `skills/wavvy-lyricist/SKILL.md`
- `skills/wavvy-lyricist/references/patterns.md`
- `MASTER/lyrics/skills/WAVVY_LYRIC_SKILL_SPEC.md`


## Worker Prompt Artifact

# Worker Prompt: worker-02

## Responsibility

Create the Wavvy lyric-writing skill and durable skill contract from the research baseline. Own only skill/spec files; do not edit CLI, harness code, tests, or release docs.


## Assigned Write Scope

- `skills/wavvy-lyricist/SKILL.md`
- `skills/wavvy-lyricist/references/patterns.md`
- `MASTER/lyrics/skills/WAVVY_LYRIC_SKILL_SPEC.md`


## Dependency Rule

- Execution group: `serial-skill`
- Depends on: worker-01


## Instructions

- Stay strictly inside this write scope.
- Do not revert unrelated dirty files or other worker output.
- Final response must include: Result, Changed files, Verification, Risks.


## Current Orchestrator Summary

# Team Model Orchestrator Summary

- Tier: tier3 (Decomposition + Lead Integration)
- Risk: aggressive
- Review target: claude
- Workers: 4


## Routing Decision

- Mode: team_dispatch
- Execution: serial
- Reason: Research, skill/spec, harness implementation, and release documentation have hard dependencies, so execution is intentionally serial with disjoint write scopes.


## Execution Groups

- serial-research: serial - 2026 Pop R&B/Neo-soul lyric evidence and local SSOT review must finish before skill writing.
- serial-skill: serial - The Wavvy lyric skill/spec depends on the research baseline.
- serial-harness: serial - Harness implementation depends on the finalized skill/spec contract.
- serial-release: serial - Release notes and SSOT/session updates follow implementation and verification.


## Workers

- worker-01: persona=researcher execution_profile=senior difficulty=medium risk=medium group=serial-research depends_on= - Research Wavvy-specific lyric-writing evidence and write research artifacts only.
- worker-02: persona=ai-ops-expert execution_profile=senior difficulty=high risk=high group=serial-skill depends_on=worker-01 - Create the Wavvy lyric-writing skill and durable skill contract from the research baseline.
- worker-03: persona=engineering-lead execution_profile=lead difficulty=high risk=high group=serial-harness depends_on=worker-02 - Implement and verify the Wavvy lyric-skill harness/CLI gates.
- worker-04: persona=ai-ops-expert execution_profile=lead difficulty=medium risk=medium group=serial-release depends_on=worker-03 - Check process fit and update release/session documentation.

- Assignment allocation repaired at 2026-05-22T10:19:37+0900: serial research -> skill/spec -> harness -> release, with disjoint write scopes.

- worker-01: in_progress at 2026-05-22T10:25:37+0900

- worker-01: done at 2026-05-22T10:29:42+0900


## Current Git Status

```text
 M .ai/HANDOFF.md
 M .ai/SESSION.md
 M CHANGELOG.md
 M MASTER/SSOT.md
 M MASTER/lyrics/LYRICS.md
 M SERIES/RNB-BEST/concept.md
 M tests/test_harness.py
 M wavvy.md
 M wavvy.py
 M wavvy_harness/gate.py
 M wavvy_harness/state.py
?? .ai/auto-handoff/20260522-005248_codex-context-low/HANDOFF.md
?? .ai/auto-handoff/20260522-005248_codex-context-low/SESSION.md
?? .ai/auto-handoff/20260522-005248_codex-context-low/failed-commands.jsonl
?? .ai/auto-handoff/20260522-005248_codex-context-low/git-diff-staged.patch
?? .ai/auto-handoff/20260522-005248_codex-context-low/git-diff.patch
?? .ai/auto-handoff/20260522-005248_codex-context-low/git-log.txt
?? .ai/auto-handoff/20260522-005248_codex-context-low/git-status.txt
?? .ai/auto-handoff/20260522-005248_codex-context-low/guard.json
?? .ai/auto-handoff/20260522-005248_codex-context-low/loss-audit.json
?? .ai/auto-handoff/20260522-005248_codex-context-low/release-gate.json
?? .ai/auto-handoff/20260522-005248_codex-context-low/result.json
?? .ai/auto-handoff/20260522-005248_codex-context-low/resume.md
?? .ai/auto-handoff/20260522-005248_codex-context-low/session.jsonl
?? .ai/auto-handoff/20260522-005248_codex-context-low/telegram-relay-context-status.json
?? .ai/auto-handoff/20260522-005248_codex-context-low/untracked-files.txt
?? .ai/auto-handoff/20260522-005248_codex-context-low/user-decisions.md
?? .ai/codex-hyphen-trigger-guard.json
?? .ai/logs/codex-handoff-events.jsonl
?? .ai/logs/codex-handoff-latest.json
?? .ai/peer-review/runs/20260521-233758-claude-review-63703.md
?? .ai/peer-review/runs/20260521-234050-claude-plan-64928.md
?? .ai/peer-review/runs/20260521-234211-claude-plan-65786.md
?? .ai/peer-review/runs/20260522-002228-claude-plan-71120.md
?? .ai/peer-review/runs/20260522-002657-claude-plan-75212.md
?? .ai/peer-review/runs/20260522-003643-claude-plan-77038.md
?? .ai/peer-review/runs/20260522-004636-claude-plan-82294.md
?? .ai/peer-review/runs/20260522-011806-claude-review-91813.md
?? .ai/peer-review/runs/20260522-012900-claude-review-94361.md
?? .ai/peer-review/runs/20260522-013501-claude-review-98882.md
?? .ai/peer-review/runs/20260522-095103-claude-review-11355.md
?? .ai/peer-review/runs/20260522-095549-claude-plan-12522.md
?? .ai/peer-review/runs/20260522-100945-claude-plan-14726.md
?? .ai/peer-review/runs/20260522-101952-claude-plan-16033.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/.goal-analysis-output.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/.goal-analysis-prompt.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/.goal-final-result-notification.json
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/.goal-plan-output.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/.goal-plan-prompt.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/.goal-report-currentness.json
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/.goal-slack-final-report-sent.json
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/.goal-slack-report-log.jsonl
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/01-team-analysis.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/02-review.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/03-plan.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/04-plan-review.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/05-implementation.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/06-record.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/gate-status.json
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/goal-daemon.json
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/goal-daemon.launchd.plist
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/goal-daemon.pid
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/implementation/17-00-track-01-rewrite.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/allocation.json
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/assignment-review-result.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/assignment-review.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/execution-groups.jsonl
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/implementation-review-prompt.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/implementation-review-result.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/implementation-review-user-decision.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/implementation-review.json
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/owner-allocation.json
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/review.json
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/routing-decision.json
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/summary.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/work-breakdown.json
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/workers/worker-01/changed-files.txt
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/workers/worker-01/output.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/workers/worker-01/prompt.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/workers/worker-01/status.json
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/workers/worker-02/changed-files.txt
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/workers/worker-02/execution.json
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/workers/worker-02/output.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/workers/worker-02/prompt.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/workers/worker-02/runtime-output.raw.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/workers/worker-02/runtime-prompt.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/workers/worker-02/status.json
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/workers/worker-03/changed-files.txt
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/workers/worker-03/output.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/workers/worker-03/prompt.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/workers/worker-03/status.json
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/workers/worker-04/changed-files.txt
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/workers/worker-04/output.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/workers/worker-04/prompt.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/orchestrator/workers/worker-04/status.json
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/research/2026-pop-rnb-lyric-patterns.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/run.json
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/task-dag.json
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/.goal-analysis-output.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/.goal-analysis-prompt.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/.goal-final-result-notification.json
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/.goal-plan-output.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/.goal-plan-prompt.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/.goal-report-currentness.json
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/.goal-slack-final-report-sent.json
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/.goal-slack-report-log.jsonl
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/01-team-analysis.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/02-review.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/03-plan.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/04-plan-review.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/05-implementation.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/06-record.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/gate-status.json
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/goal-daemon.json
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/goal-daemon.launchd.plist
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/goal-daemon.pid
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/allocation.json
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/assignment-review-result.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/assignment-review.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/execution-groups.jsonl
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/owner-allocation.json
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/review.json
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/routing-decision.json
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/summary.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/work-breakdown.json
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/workers/worker-01/changed-files.txt
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/workers/worker-01/execution.json
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/workers/worker-01/output.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/workers/worker-01/prompt.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/workers/worker-01/runtime-output.raw.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/workers/worker-01/runtime-prompt.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/workers/worker-01/status.json
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/workers/worker-02/changed-files.txt
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/workers/worker-02/output.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/workers/worker-02/prompt.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/workers/worker-02/runtime-prompt.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/workers/worker-02/status.json
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/workers/worker-03/changed-files.txt
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/workers/worker-03/output.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/workers/worker-03/prompt.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/workers/worker-03/status.json
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/workers/worker-04/changed-files.txt
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/workers/worker-04/output.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/workers/worker-04/prompt.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/orchestrator/workers/worker-04/status.json
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/research/lyrics-skill-baseline.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/research/source-index.md
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/run.json
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/task-dag.json
?? SERIES/17-00/concept.md
?? "SERIES/17-00/input/tracks/01_\354\230\254\353\235\274\352\260\200 (Up Again).txt"
```
