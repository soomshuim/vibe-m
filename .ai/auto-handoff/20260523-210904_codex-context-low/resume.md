# Codex Auto Handoff Resume

- Created: 2026-05-23 21:09:04 +0900
- Project: /Users/zenkim_office/Project/wavvy
- Context remaining: 17%
- Threshold: 25%
- Resume trigger: Codex: -wavvy; Claude: /wavvy
- Guard snapshot: /Users/zenkim_office/Project/wavvy/.ai/auto-handoff/20260523-210904_codex-context-low/guard.json
- Pending user requests: /Users/zenkim_office/Project/wavvy/.ai/auto-handoff/20260523-210904_codex-context-low/pending-user-requests.md

## Continuation

The actuator normally starts a fresh headless Codex continuation after this
checkpoint. The continuation must read `pending-user-requests.md` before
older project HANDOFF/SESSION TODOs. Manual resume is a fallback only when
`continue_action` in the result/done JSON is not `started`.

## Manual Resume Fallback

1. Start a new Codex session only if the continuation bridge failed, was
   disabled, or reached max depth.
2. Run: Codex: -wavvy; Claude: /wavvy
3. Read /Users/zenkim_office/Project/wavvy/.ai/auto-handoff/20260523-210904_codex-context-low/pending-user-requests.md.
4. Read the latest project .ai/HANDOFF.md entry and this snapshot directory if
   git state or pending work is unclear.
