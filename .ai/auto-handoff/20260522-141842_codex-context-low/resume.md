# Codex Auto Handoff Resume

- Created: 2026-05-22 14:18:42 +0900
- Project: /Users/zenkim_office/Project/wavvy
- Context remaining: 23%
- Threshold: 25%
- Resume trigger: Codex: -wavvy; Claude: /wavvy
- Guard snapshot: /Users/zenkim_office/Project/wavvy/.ai/auto-handoff/20260522-141842_codex-context-low/guard.json

## Continuation

The actuator normally starts a fresh headless Codex continuation after this
checkpoint. Manual resume is a fallback only when `continue_action` in the
result/done JSON is not `started`.

## Manual Resume Fallback

1. Start a new Codex session only if the continuation bridge failed, was
   disabled, or reached max depth.
2. Run: Codex: -wavvy; Claude: /wavvy
3. Read the latest project .ai/HANDOFF.md entry.
4. Read this snapshot directory if git state or pending work is unclear.
