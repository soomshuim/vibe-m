# Wavvy SSOT Contract

Version: 1.0
Last Updated: 2026-05-02
Purpose: 하네스가 문서/상태/산출물 충돌을 판정하기 위한 단일 기준

---

## Conflict Order

| Priority | File / Artifact | Owns | Notes |
|---|---|---|---|
| 1 | `.ai/state.json` | active series, phase, next action, local artifact availability | Machine-readable resume contract. Written only by `python3 wavvy.py state --write`. |
| 2 | `SERIES/[series]/concept.md` | per-series concept, YouTube metadata, Final Track Sources | Upload-final source archive after `finalize-upload`. |
| 3 | `SERIES/[series]/output/report.json` | technical track durations, hashes, processing params | Local generated artifact. Regeneratable by `pack`. |
| 4 | `MASTER/ai/RUNTIME_RULES.md` | runtime hard constraints, media execution cautions, approval/safety rules | Entry files route here; workflow details still live in `WORKFLOWS.md` / `cli/SPEC.md`. |
| 5 | `MASTER/MANAGER.md` | quality gate hierarchy | Conservative fail when no lower rule applies. |
| 6 | `MASTER/WORKFLOWS.md` | operational workflow rules | txt-first, finalize-upload, packaging order. |
| 7 | `MASTER/youtube/YOUTUBE.md` | YouTube title/description/tag format | Final metadata lives in series concept. |
| 8 | `wavvy.md` | brand identity and global defaults | Per-series overrides must be explicit. |
| 9 | `.ai/HANDOFF.md` / `.ai/SESSION.md` | historical handoff/session archive | Read newest-first; not the active-state SSOT. |

`MASTER/ai/RUNTIME_RULES.md` is priority 4 because runtime hard constraints and approval/safety rules are absolute execution bounds; `MASTER/MANAGER.md` remains the conservative-fail quality gate fallback inside those bounds.

---

## Phase Contract

| Phase | Definition |
|---|---|
| `concept_draft` | Concept exists but source work is incomplete. |
| `track_source_draft` | Track txt/source prompt work is active. |
| `source_final` | Audio, metadata, report, and Final Track Sources are final enough for subtitle/upload prep. |
| `render_final` | Rendered video and upload CSV exist and match the current report. |
| `upload_ready` | Rendered video plus subtitle/upload support artifacts are present. |
| `uploaded` | YouTube upload is complete. Large local render artifacts may be deleted if upload completion is recorded in `concept.md`. |

`output/final.mkv` absence is a blocker for `render_final`. It is also a blocker for `upload_ready` unless upload completion is already recorded. It is not a blocker for `source_final` or `uploaded`.

---

## Per-Series Overrides

Global brand defaults in `wavvy.md` apply unless a series explicitly names an override in its `concept.md`.

Examples:

- A hip-hop series may allow code-switching or genre-specific meta tags if the concept documents the exception.
- A time-slot series may alter upload positioning if its YouTube metadata block states the final positioning.

Implicit overrides are not valid. If a global rule and a series concept conflict without a named override, `MASTER/MANAGER.md` conservative fail applies.

---

## State Writer Rule

`.ai/state.json` must be written only by:

```bash
python3 wavvy.py state SERIES/[series] --write
```

The writer uses temp-file plus atomic rename. Agents should not edit `.ai/state.json` manually.

`.ai/HANDOFF.md` remains append-only because claude-center hooks still read it. State augments handoff; it does not replace hook behavior yet.

---

## Initial Drift Rules

`python3 wavvy.py state SERIES/[series] --check` should warn or fail on these conflicts:

1. `concept.md` has `## Final Track Sources` but status/TODO text still says `draft`, `DRAFT`, or `Suno 생성/검수`.
2. `.ai/state.json` phase is `source_final` or later but `concept.md` lacks `## Final Track Sources`.
3. `.ai/state.json` next action mentions upload/render while render artifacts are missing:
   - warning for `source_final`
   - blocker for `render_final` / `upload_ready`
   - no warning for `uploaded` when upload completion is recorded

---

## Artifact Policy

Tracked:

- source docs
- concept docs
- rubric/reference docs
- state contract
- peer review records when needed for audit

Ignored/local:

- large media
- `work/`
- most `output/`
- regenerated render artifacts

If an ignored artifact becomes required for resume, state must record its availability and regeneration command.

After YouTube upload, `output/final.mkv` and `output/upload.csv` may be deleted for disk space. The series `concept.md` must then record upload completion so gates can distinguish intentional retention cleanup from an incomplete render.
