연결해줘 -director

Context:
- Wavvy repo already has the lyricist skill package and CLI harness:
  - skills/wavvy-lyricist/SKILL.md
  - skills/wavvy-lyricist/references/patterns.md
  - MASTER/lyrics/skills/WAVVY_LYRIC_SKILL_SPEC.md
  - python3 wavvy.py lyrics-skill SERIES/[series] --json
  - python3 wavvy.py gate SERIES/[series] --stage lyrics-review --json
- .ai/SESSION.md says the remaining TODO is: if the user confirms "연결해줘", implement Wavvy-local /write and -write command shims.

Goal:
- Implement the Wavvy-local lyric-only command shim(s): Claude Code `/write` and Codex `-write`.
- Keep the command thin. Do not copy lyric-writing rules into the command. Route users/agents to the existing Wavvy lyricist skill/spec/CLI harness.
- Scope is lyric writing, rewrite, and lyric review only. Do not route YouTube copy, concept docs, changelog, or non-lyric writing through this command.
- Preserve existing repo conventions and trigger policy.

Expected output:
- Add/update the minimum command/skill files needed so `/write` and `-write` resolve locally for Wavvy.
- Update durable project docs/session/changelog only if appropriate for the repo workflow.
- Verify with relevant lightweight checks, including command file discovery, python harness checks if touched, and git diff --check.
