# Codex Auto Handoff Resume

- Created: 2026-06-02 19:57:30 +0900
- Project: /Users/zen/Project/wavvy
- Resume command: cd /Users/zen/Project/wavvy && cat /Users/zen/Project/wavvy/.ai/HANDOFF.md
- Context remaining: 18%
- Threshold: 25%
- Resume trigger: cd /Users/zen/Project/wavvy && cat /Users/zen/Project/wavvy/.ai/HANDOFF.md
- Guard snapshot: /Users/zen/Project/wavvy/.ai/auto-handoff/20260602-195730_codex-context-low/guard.json
- Pending user requests: /Users/zen/Project/wavvy/.ai/auto-handoff/20260602-195730_codex-context-low/pending-user-requests.md

Primary repo:
- path: /Users/zen/Project/wavvy
- role: implementation

Secondary repos:
- (none)

Do not resume from:
- /Users/zen/Project (workspace root)

## Continuation

The actuator normally starts a fresh headless Codex continuation after this
checkpoint. The continuation must read `continuation-target.json` first and
treat `pending-user-requests.md` as context-only prior requests unless the
target file is missing. Primary repo root is /Users/zen/Project/wavvy.
Ignore all secondary repos not marked implementation. Do not resume from
workspace root. Manual resume is a fallback only when `continue_action` in the
result/done JSON is not `started`.

## Manual Resume Fallback

1. Start a new Codex session only if the continuation bridge failed, was
   disabled, or reached max depth.
2. Run: cd /Users/zen/Project/wavvy && cat /Users/zen/Project/wavvy/.ai/HANDOFF.md
3. Read /Users/zen/Project/wavvy/.ai/auto-handoff/20260602-195730_codex-context-low/continuation-target.json, then read /Users/zen/Project/wavvy/.ai/auto-handoff/20260602-195730_codex-context-low/pending-user-requests.md
   only as context-only prior requests.
4. Read the latest project .ai/HANDOFF.md entry and this snapshot directory if
   git state or pending work is unclear.
