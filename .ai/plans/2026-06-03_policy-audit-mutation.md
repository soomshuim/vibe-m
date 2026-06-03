# 2026-06-03 Policy Audit Mutation Plan

## Scope

- Trigger: `-director`
- Repo: `/Users/zen/Project/wavvy`
- Mode: read-only audit first, then approved safe mutation
- Mutation type: documentation and legacy harness alignment only

## Audit Summary

- Scanned 236 document candidates under the repo root.
- Excluded `.git`, dependency/cache/build/vendor paths, binaries, and large media artifacts from document inventory.
- Applied repository-defined precedence from `MASTER/SSOT.md` Conflict Order.
- Confirmed `AGENTS.md` exists and acts as the canonical agent router.
- No always-loaded policy/command/skill/framework document exceeds 300 physical lines by `wc -l`-equivalent line counting.
- `meetings/`, `report/`, and `.ai/pipeline/runs` contain historical/team artifacts, but several are directly referenced by current rubric or lyric pattern docs, so no deletion/archive mutation is included.

## Finding

`SERIES/20-00/concept.md` current final state says:

- A 3 / B 5 / C 5 / D 3 / E 2 / F 2 = 20 tracks
- Hard 13 / 20 = 65%

Stale current-looking policy text remained in:

- `SERIES/20-00/concept.md` v0.4 correction notes
- `MASTER/rubrics/HARD_HIPHOP_RUBRIC.md` v1.4
- `MASTER/scripts/check_series_gate.sh`

## Approved Mutation

- Mark v0.4 concept distribution as superseded by v0.5/v0.8.
- Update `HARD_HIPHOP_RUBRIC.md` to v1.5 with current final distribution.
- Mark `check_series_gate.sh` as a legacy pre-final txt validator and minimally align S1/S2/S3/S5 to the current concept.
- Record the mutation in `CHANGELOG.md`, `.ai/SESSION.md`, and `.ai/HANDOFF.md`.

## Post-Review Safety Correction

- Reviewer concern: S2 could look like gate weakening because the legacy numeric BPM distribution check was changed from FAIL to PASS.
- Decision SSOT: `MASTER/rubrics/HARD_HIPHOP_RUBRIC.md` section `S2 Advisory Disposition`.
- This plan intentionally records only the pointer so S2 policy details do not drift into a second source of truth.

## Non-Mutations

- No deletion.
- No archive movement.
- No policy-chain restructuring.
- No commit or push unless separately requested.
