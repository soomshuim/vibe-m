# Claude Code — Wavvy

Purpose: Claude-specific entrypoint for Wavvy. Use `AGENTS.md` as the canonical agent router; this file only adds Claude-facing reminders.

## Start Here

1. Read `AGENTS.md`.
2. Check `.ai/state.json` with `python3 wavvy.py state SERIES/[series] --check` when continuing series work.
3. Use `MASTER/SSOT.md` for conflict resolution before trusting older handoff/session text.

## Claude Notes

- Project identity: `wavvy.md`.
- Runtime safety/media rules: `MASTER/ai/RUNTIME_RULES.md`.
- Detailed workflows: `MASTER/WORKFLOWS.md`.
- CLI details: `MASTER/cli/SPEC.md`.
- Quality gates: `MASTER/MANAGER.md`.

## Quick Commands

```bash
python3 wavvy.py doctor
python3 wavvy.py validate <series>
python3 wavvy.py state <series> --check
python3 wavvy.py gate <series> --stage uploaded
python3 wavvy.py pack <series>
```

For all other commands and options, use `MASTER/cli/SPEC.md`.
