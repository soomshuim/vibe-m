# AGENTS.md

Canonical agent router for Wavvy. Keep this file small; route detailed rules to the owning context document.

## Mission

- Maintain Wavvy as an agent-readable music production and YouTube packaging repo.
- Prefer deterministic gates over persuasive summaries.
- Keep changes scoped, reversible, and recorded in the project docs.

## Repository Map

- Channel identity: `wavvy.md`
- Active machine state: `.ai/state.json`
- Conflict order and artifact policy: `MASTER/SSOT.md`
- Runtime safety/media rules: `MASTER/ai/RUNTIME_RULES.md`
- Workflows: `MASTER/WORKFLOWS.md`
- CLI spec: `MASTER/cli/SPEC.md`
- Quality gates: `MASTER/MANAGER.md`
- Lyrics/style/roles: `MASTER/lyrics/`, `MASTER/style/`, `MASTER/roles/`
- YouTube metadata: `MASTER/youtube/YOUTUBE.md`
- Series work: `SERIES/[series]/concept.md`

## Context Router

| Task | Read First |
|---|---|
| Resume project state | `.ai/state.json`, then `MASTER/SSOT.md` |
| Resolve conflicting docs | `MASTER/SSOT.md` |
| Track prompt/source work | `MASTER/WORKFLOWS.md` §0-2 |
| Lyric writing/rewrite/review | `.claude/commands/write.md`, then `skills/wavvy-lyricist/SKILL.md` |
| Packaging, preview, shorts, gates | `MASTER/cli/SPEC.md` |
| Media runtime cautions | `MASTER/ai/RUNTIME_RULES.md` |
| YouTube title/description/tags | `MASTER/youtube/YOUTUBE.md`, then series `concept.md` |
| Genre or quality judgment | `MASTER/MANAGER.md`, then matching `MASTER/rubrics/*` |

## Working Agreements

- Before editing a series, inspect its `concept.md` and current state gate.
- For multi-file or architectural changes, create/update a plan in `.ai/plans/`.
- Do not duplicate detailed rules into this file; update the owning MASTER document.
- Do not treat missing ignored media artifacts as failure without checking `.ai/state.json` and `MASTER/SSOT.md`.

## Verification

```bash
python3 -m py_compile wavvy.py wavvy_harness/*.py
python3 -m unittest tests/test_harness.py
python3 wavvy.py doctor --json
python3 wavvy.py validate SERIES/[series]
python3 wavvy.py state SERIES/[series] --check --json
python3 wavvy.py gate SERIES/[series] --stage uploaded --json
git diff --check
```

## Done When

- Relevant gates pass.
- State/SSOT docs reflect any phase or artifact change.
- Generated large media remains local/ignored unless explicitly requested.
- Handoff/session/changelog are updated when the task changes durable project state.
