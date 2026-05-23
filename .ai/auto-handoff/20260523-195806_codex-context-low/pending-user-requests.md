# Pending User Requests Snapshot

Source: latest non-duplicate user messages from the Codex session JSONL.

Use this as the authoritative queued work before older `.ai/HANDOFF.md` or `.ai/SESSION.md` TODOs. If these requests include a `-play`, `-director`, or clarification of a previous request, continue that work instead of selecting an older TODO.

## Request 1

- Timestamp: `2026-05-23T09:50:00.241Z`
- Source: `response_item`

```text
# AGENTS.md instructions for /Users/zenkim_office

<INSTRUCTIONS>
# Startup Policy

On every Codex CLI session start, before handling the first user request, run a Claude activity check and include the result in the first reply.

Required check command:

` ` `bash
bash $HOME/.codex/scripts/check-claude-activity.sh
` ` `

If files are missing or inaccessible, report that clearly and continue with best-effort results.

# Response Language Policy

- Respond in Korean by default across Codex sessions unless the user explicitly requests another language.

# Feedback and Truthfulness Policy

사용자 의견, 작업물, 리뷰에 대해 피드백할 때:

- 잘된 부분은 분명히 좋다고 인정한다.
- 이미 충분히 잘 설계된 부분에는 억지로 개선 조언을 추가하지 않는다.
- 모든 요소에 억지로 피드백하려고 하지 말고, 실제로 산출물(기획, 개발, 디자인, CDS 구성, 하네스 등)의 퀄리티에 영향을 주는 문제만 골라서 지적한다.
- 비판을 위한 비판, 역량이 있음을 티 내기 위한 과잉 피드백, 취향 기반 지적은 금지한다.
- 좋은 산출물이라면 좋은 산출물이라고 말하고, 개선이 필요한 지점에만 집중한다.

진실성 규칙:

- 산출물에서 확인할 수 없는 데이터나 연관성 있는 기획, 디자인, 개발 요소를 아는 척하지 않는다.
- 내부 전략을 아는 것처럼 추측하지 않는다.
- 산출물 외에 확인되지 않은 경우, 반드시 관련된 다른 프로젝트 작업물을 확인하고 답변한다.
- 근거가 약하면 강한 표현으로 비판하지 않는다.

# Request Interpretation Guard

사용자 요청이 여러 의미로 해석될 수 있고 그 차이가 작업 범위, 영구 정책,
배정 로직, 산출물 보존 여부에 영향을 주는 경우에는 구현이나 파일 수정 전에
짧게 확인 질문을 한다.

특히 아래 케이스는 의심 신호로 본다:

- 일회성/현재 프로젝트 요청인지, 전역/영구 정책 변경인지 불명확한 경우
- 리서치·분석·플래닝 단계 한정인지, 구현·검증·배포 전체에 적용되는지 불명확한 경우
- "최고 성능", "강하게", "보수적으로" 같은 표현이 특정 단계 품질 요구인지,
  모든 worker allocation 제한인지 불명확한 경우
- 특정 산출물 제거 요청이 planning artifact까지 삭제하라는 뜻인지,
  잘못된 구현/정책 흔적만 제거하라는 뜻인지 불명확한 경우
- 요구를 넓게 해석하면 junior/intern 배정 금지처럼 비용·속도·운영 정책이
  바뀌고, 좁게 해석하면 사용자의 품질 의도를 놓칠 수 있는 경우

기본값:

- 경쟁 해석을 1개의 간결한 질문으로 제시하고 사용자 확인을 기다린다.
- 모호한 표현만으로 global allocator/policy를 영구 변경하지 않는다.
- 난이도 높은 사고나 분석이 필요하지 않은 단순 반복 작업은 명시적 제외 요청이
  없는 한 intern/junior 배정 가능성을 유지한다.

# Clipboard / URL Delivery Policy

- In Codex CLI, do not rely on click-drag selection for URLs or other copy-sensitive strings. The tmux/Codex TUI can intercept mouse drag events and make selection disappear.
- When a URL, Figma link, command output token, or other exact copy target is the primary deliverable, copy it to the macOS clipboard before replying:

` ` `bash
printf '%s' '<copy-target>' | pbcopy
` ` `

- For multiple copy targets, write newline-separated values to `$HOME/.codex/paste-cache/last-copy-targets.txt` and copy that file with `pbcopy < ...`.
- In the reply, state that the value has been copied to the clipboard. If showing it too, use a fenced `text` block, not a Markdown link, so terminal auto-linking is not the primary path.
- The preferred Codex CLI launcher disables tmux mouse capture and uses `codex --no-alt-screen` by default. Opt out only when explicitly needed with `CODEX_TMUX_MOUSE=1` or `CODEX_NO_ALT_SCREEN=0`.

# Shared Memory Policy

Claude Code uses auto memory at `$HOME/.claude/projects/*/memory/MEMORY.md`,
and this path should be symlinked to:

`$HOME/Project/agent-center/memory/MEMORY.md`

This keeps Claude auto-load behavior while allowing Git-based sync across machines.

Codex may reference project CLAUDE.md or SESSION.md for collaboration context.
Cross-tool shared context file is currently not in use (보류).

# Codex Auto-Clear Sentinel

At the beginning of each user turn, before doing new work, check whether a
previous hook already completed a low-context checkpoint:

` ` `bash
bash "$HOME/Project/agent-center/scripts/codex-auto-handoff.sh" --pending-clear --json
` ` `

If it returns `action: "clear_required"`, do not continue the old session.
Report the saved `resume_trigger` and `snapshot_dir`, then end the conversation
with the archive directive when running in Codex Desktop. Do not ask the user to
manually rescue the work as the normal path; the handoff actuator starts a
headless continuation by default after checkpoint success:

` ` `text
::archive{reason="context<25 auto-handoff completed; resume with the saved trigger"}
` ` `

In plain CLI contexts where archive directives are unavailable, stop after
printing the resume trigger and snapshot. The headless continuation is the
primary continuation path; manual clear is only a fallback when the continuation
bridge failed or was disabled.

If the user explicitly says they already restarted/cleared the session, or asks
to fix a stuck/stale clear sentinel, acknowledge the completed handoff instead
of blocking forever:

` ` `bash
bash "$HOME/Project/agent-center/scripts/codex-auto-handoff.sh" --ack-clear --json
` ` `

Then rerun the pending-clear check and continue only if it returns
`action: "none"`. This archives the sentinel under
`$HOME/.codex/auto-handoff/acknowledged/` and preserves the handoff snapshot.
`--pending-clear` may also return `action: "none"` with
`auto_acknowledged_clear: true` after it proves a fresh top-level Codex session
is active and no longer below threshold.
If `CODEX_AUTO_HANDOFF_CLEAR_CMD` is configured and succeeds, the actuator
performs this archive step itself so the next session is not blocked by a stale
sentinel.

# Context-Low Auto-Handoff (Codex)

Exception: if the current user turn is an auto-handoff status relay message
starting with `# Auto-Handoff Status Relay`, do not launch another handoff for
that relay turn. Report only the relayed headless continuation status,
observable progress, and final result in Korean, including concrete actions,
files, tests, outcomes, and next step when the relay body provides them. Do not
expose hidden chain-of-thought; summarize observable progress/actions only. Do
not resume implementation from the old low-context session.

At the beginning of each user turn and before substantial tool work, check the
visible Codex statusline. If it shows `context<25`, or if the task is long enough
that context exhaustion is plausible, run:

` ` `bash
bash "$HOME/Project/agent-center/scripts/context-guard.sh" --agent codex --json
` ` `

If the guard returns `below_threshold: true` or exits `20`, stop starting new
work and execute the automated handoff actuator immediately:

` ` `bash
bash "$HOME/Project/agent-center/scripts/codex-auto-handoff.sh" --json
` ` `

Then report the `resume_trigger`, `snapshot_dir`, and `continue_action`, and
clear/archive as described above. The actuator saves state before any clear
action and starts a fresh headless Codex continuation by default
(`CODEX_AUTO_HANDOFF_CONTINUE=1`) so queued work can continue even if the user
does not manually clear the old session.

Exception: if the current user turn is an explicit `-record` request (the
message starts with `-record` or the first inline trigger token is `-record`),
run only the minimal record workflow needed to persist the current completed
work, then stop. Do not start new implementation, review, exploration, or
planning work while below threshold. Pending `clear_required` sentinel checks
still take precedence; acknowledge a stale sentinel only when the user says the
session was already cleared/restarted.

Manual fallback if the actuator is unavailable:

1. Append a canonical project-local `.ai/HANDOFF.md` entry using the existing
   `HANDOFF / Date / Project / Agent / Summary / Next-TODO / Commits` schema.
   Add `Resume-Trigger:` with the exact reload command from `commands.codex`
   such as `-cds`, or the `reload_instruction` fallback.
2. Update project-local `.ai/SESSION.md` with current objective, completed work,
   dirty files, pending steps, and the next command to run.
3. Run `-record` to commit/push the checkpoint. This step is allowed even when
   context remains below threshold, but only for checkpoint recording.
4. Start a fresh headless continuation with `scripts/codex-auto-continue.sh` if
   the actuator was unavailable but the script exists. Only ask the user to
   manually clear/reload if no continuation bridge can be started.
5. In the next session, the first action must be the project command and then
   reading the latest HANDOFF.

`context-guard.sh` is read-only. It must not run `git`, `record`, `clear`,
`claude`, `codex`, slash commands, or hyphen commands. Mutating behavior belongs
to `codex-auto-handoff.sh`.

The shell-level actuator writes a clear-required sentinel. A documented Codex
CLI `clear` command is not currently available; if a local bridge is later
installed, set `CODEX_AUTO_HANDOFF_CLEAR_CMD` and the actuator will run it only
after checkpoint success. When that clear command succeeds, the sentinel is
archived instead of left pending.

# Codex Hyphen Trigger Guard

At the beginning of each Codex user turn, after pending-clear/context checks and
before any file edits or direct implementation, run the hyphen trigger guard
with the current user message:

` ` `bash
bash "$HOME/Project/agent-center/scripts/codex-hyphen-trigger-guard.sh" check \
  --repo "$(git rev-parse --show-toplevel 2>/dev/null || pwd)" \
  --message "<current user message>" \
  --json
` ` `

If the message is too large or quoting would be fragile, write it to a temporary
file and use `--message-file`.

If the guard returns `action: "start_play_required"`, do not make direct edits,
do not answer with only a plan, and do not continue a Default-mode
implementation. Start the public play entrypoint first:

` ` `bash
bash "$HOME/Project/agent-center/scripts/play.sh" start \
  --repo "$(git rev-parse --show-toplevel 2>/dev/null || pwd)" \
  --slug "<short-topic-label>" \
  --request-text "<current or pending request text>" \
  --runtime auto \
  --target claude \
  --timeout-seconds 2700 \
  --max-repair-rounds 1 \
  --fresh-runtime auto \
  --desktop-controller codex \
  --daemon
` ` `

`play.sh start` acknowledges the pending trigger after a `task-dag.json` run is
created. If the daemon or headless runtime fails, continue only through the
documented play recovery artifacts in that run; do not silently finish by direct
implementation. This guard exists because a prior Codex session accepted a
`-play` request, then handled the following "Implement the plan" turn directly
and skipped the play final report hook.

# Project AGENTS Policy

Global Codex behavior such as context-low auto-handoff belongs in this file and
is loaded through `~/.codex/AGENTS.md -> ~/Project/agent-center/AGENTS.md`.
Project-level `AGENTS.md` files should stay optional project routers for repo
maps, SSOT documents, and verification commands. Do not duplicate this
context-low policy into every project.

# Codex Native Goal Bridge

Codex's built-in `/goal` is not a hyphen command and is not the same as a
project command file. It is native Codex goal state exposed to the model through
`get_goal` / `create_goal` / `update_goal`.

At the beginning of each Codex user turn, after pending-clear/context checks,
call `get_goal` when either of these is true:

- the user mentions `/goal`, Codex native goal, or goal mode;
- the visible context suggests an active native goal may exist.

If `get_goal` returns an active goal objective, route that objective into the
canonical `-play` autonomous runner. Use:

` ` `bash
bash "$HOME/Project/agent-center/scripts/codex-native-goal-bridge.sh" start \
  --repo "$(git rev-parse --show-toplevel 2>/dev/null || pwd)" \
  --objective "<get_goal objective>" \
  --desktop-controller codex
` ` `

The bridge records idempotent mappings under:

` ` `text
<repo>/.ai/codex-native-goals/<objective-hash>.json
` ` `

Do not treat Codex native `/goal` as `/goal` command text or as the public
`-goal` hyphen trigger. `-goal` may exist only as a compatibility shortcut; the
native Codex goal integration is `get_goal` → `codex-native-goal-bridge.sh` →
`play.sh goal-init/goal-run`.

When a native-goal-backed play DAG is confirmed `done` and no required work
remains, call `update_goal(status="complete")`. If the play runner is daemonized
and still running, leave the native goal active and report the run directory and
status file instead of marking it complete.

# Codex Computer Use Recovery

Codex Computer Use has two separate local processes:

- `SkyComputerUseService`: the macOS app/service that needs TCC permissions.
- `SkyComputerUseClient mcp`: the stdio MCP transport owned by a live Codex
  session.

Never kill `SkyComputerUseClient mcp` from inside an active Codex session. If it
is killed, the current session's Computer Use tool handle becomes
`Transport closed` and cannot be reattached from the model side. Restart only
`SkyComputerUseService` when trying to refresh TCC state.

If Computer Use fails with macOS/TCC errors, run:

` ` `bash
bash "$HOME/Project/agent-center/scripts/codex-computer-use-recover.sh" --fresh-smoke --json
` ` `

Interpretation:

- fresh-smoke `ok`: global TCC/plugin state is good; use the canonical
  fresh-runtime path (`play-desktop-actuator.sh` / `codex exec`) or start a
  fresh top-level Codex session if the current direct tool handle is closed.
- fresh-smoke `failed` or `timeout`: use
  `desktop-control-permission-doctor.sh --warmup --open-settings`, approve the
  expected macOS prompts, then rerun the smoke.

For service-only refresh:

` ` `bash
bash "$HOME/Project/agent-center/scripts/codex-computer-use-recover.sh" --restart-service --fresh-smoke --json
` ` `

# Peer Review Auto-Loop (Codex)

When invoked via review triggers `-codex-review`, `-claude-review`, `-review--codex`, 또는 `-review--claude`, run **PASS까지 자동 반복**.

`-review` is a separate local artifact-review harness, not a peer-review
auto-loop trigger. For Figma/CDS URLs or node ids, `-review` must load the
project Figma/CDS rules and include Visual/UX, CDS Usage, Node Structure, and
Rubric Verdict in the first report.

> **Plan 트리거는 자동 반복 대상 아님** — `-codex-plan` / `-claude-plan` / `-plan--codex` / `-plan--claude`는 한 번 받고 사용자 결정 흐름.
>
> **Controller-only guard** — 이 룰은 review를 *요청하는* 컨트롤러에만 적용. headless peer reviewer 역할(peer-agent-review.sh가 호출한 reviewer 자신)은 **nested peer review를 시작 금지**.
>
> **도구별 트리거 형식 (의미 동일)** — Codex는 hyphen만 사용 (AGENTS.md trigger policy: slash 미지원). Claude Code 측 CLAUDE.md는 slash + hyphen 둘 다 표기하지만 의미는 동일하며, 단지 입력 형식만 다르다.
>
> **Timeout 기준** — headless peer review는 오래 걸릴 수 있다. 기본 timeout은 2700초(45분)이며, 그 전에는 hang으로 간주하지 않는다. 필요한 경우 `--timeout-seconds` 또는 `PEER_AGENT_REVIEW_TIMEOUT_SECONDS`로 조정하고, `0`은 timeout 비활성화다.
>
> **Persona/model tier 기준** — 직군 persona 및 intern/junior/senior/lead model/effort 선택은 `-play`/`-director` 내부 routing metadata다. `-senior`, `-xhigh`, `-model-*`, `-pm`, `-backend` 같은 새 public trigger로 만들지 않는다.

## Loop

1. peer review 실행 → 결과 평가
2. **PASS** → 완료 (사용자에게 짧게 보고)
3. **FAIL** → finding 처리 (아래 토론 합의) → 수정 → 재실행
4. **NEEDS_USER_DECISION** → 즉시 사용자 의견 요청 (자동 진행 금지)

## 안전 장치 (무한 루프 방지)

- 최대 5회 반복 → 그 이상 시 사용자 에스컬레이션
- 동일 finding 2회 연속 등장 → 즉시 사용자 에스컬레이션
- recursion blocked 응답 → 자동 종료 후 사용자 보고
- 매 반복마다 회차/판정/finding 요약을 1줄로 사용자에게 노출

## Finding 토론 합의 (맹목 수용 X)

- **Accept** — 동의 시 그대로 수정
- **Debate** — 치명적 결함이거나 전제가 틀린 finding:
  1. 반대 근거 명시 + 사용자에게 토론 요청
  2. 사용자 합의 방향대로 반영
  3. 합의 안 되면 사용자 결정 우선
- **Skip with sourcing** — 명백히 잘못된 finding을 skip할 때:
  1. 구체적 evidence/source 인용 필수
  2. High/Critical severity 또는 전제 dispute는 skip 전 사용자 confirm 필수
  3. review run 메모에 skip 사유 + 출처 기록 (감사 가능성)

## 학습 자료 참조

- 보고서/패턴: `~/Project/lenny/skills/ai-ops-expert/references/harness-engineering.md` §13 (Peer Review as Harness Gate)
- Skill: `~/Project/lenny/skills/ai-ops-expert/SKILL.md` (자동 매칭)

> 근거: 2026-04-28 사용자 룰 — "치명적 결함이고 의견 다를 때는 반드시 따를 필요 없음, 토론 후 합의 방향으로 반영"

# Trigger Policy (Codex)

Codex uses hyphen triggers as the single official command/skill invocation format.

## Input normalization

- Official trigger: if user input starts with `-`, parse as: `-name [args...]`.
- Also support inline trigger tokens: if input contains ` -name` anywhere, treat it as a command trigger.
  - Example supported: `자동 중재 조건을 플래닝해줘 -director`
  - Use the first matched `-name` token as trigger; keep remaining text as arguments/context.
- Slash-style triggers (`/name`) are not used in Codex.
- Bare triggers (`name [args...]`) are not treated as command invocations in Codex.
- Normalize only the trigger token (`name`) for matching; keep original args unchanged.
- This applies globally to all matched commands/skills across scanned projects (e.g. `-coach`, `-director`, `-record`, `-live`, `-lennylive`).

## CDS naming guard

- In `$HOME/Project/CDS`, treat `CONSTITUTION.md` as the canonical policy file.
- Do not create, restore, or modify `AGENTS.md` in CDS.
- If instructions mention CDS `AGENTS.md`, map it to `CONSTITUTION.md`.

## Command matching (Claude commands)

- Check in this priority order:
  1. `<current_project>/.claude/commands/{name}.md` (project-local override)
  2. `$HOME/.claude/commands/{name}.md` (global symlinked workspace)
  3. `$HOME/Project/*/.claude/commands/{name}.md` (project-root only)
  4. `$HOME/Project/*/commands/{name}.md` (project-root only)
- If found, load that command definition and execute its workflow.
- Exclude nested command packs under subdirectories (for example `.../plugins/.../commands`).
- Exclude these command names from trigger matching: `execute-refactor`, `plan-parallel`, `plan-refactor`, `plan-spec-improvements`, `refactor`, `validate-security`, `validate-slc-arch`, `validate-spec-planning`, `validate-vibe-coding`, `plan-dev`.

## Skill matching (Codex skills)

- Check in this priority order:
  1. `$HOME/.codex/skills/{name}/SKILL.md` (global Codex skills)
  2. `$HOME/Project/*/skills/{name}/SKILL.md` (project skill packs)
  3. `$HOME/Project/**/skills/{name}/SKILL.md` (plugin/nested skill packs)
- If found, apply the skill for the turn.
- In `$HOME/Project/lenny/skills`, `*.md` files are treated as skill-equivalent sources (same role as `.skill`).

## When both match

- If the same `name` matches both a command and a skill, run both with minimal context:
  1. Load/execute command workflow.
  2. Apply skill guidance for implementation details.
- State briefly which one(s) were activated.

## Current inventory check baseline (updated 2026-05-21, all projects)

- Projects scanned: `AIZen`, `CDS`, `agent-center`, `lenny`, `lenny-live`, `plumlabs-context`, `simulator`, `wavvy`, `wellness-challenge-platform`.
- Commands discovered:
  - `agent-center/commands`: `cds`, `claude-plan`, `claude-review`, `coach`, `codex-plan`, `codex-review`, `codex-status`, `context-guard`, `design`, `director`, `end-live`, `goal`, `lenny`, `lennylive`, `live`, `plan--claude`, `plan--codex`, `play`, `plum`, `price`, `qa`, `ralph`, `record`, `research`, `review`, `review--claude`, `review--codex`, `team`, `wavvy`, `well`, `zen`.
  - `agent-center/scripts`: `team-model-orchestrator.sh` is an internal helper used by `play`/`director`, not a public command trigger.
  - `AIZen/.claude/commands`: `aizen`, `aizen-new`.
  - `wellness-challenge-platform/.claude/commands`: `execute-refactor`, `plan-dev`, `plan-parallel`, `plan-refactor`, `plan-spec-improvements`, `refactor`, `validate-security`, `validate-slc-arch`, `validate-spec-planning`, `validate-vibe-coding`.
  - `plumlabs-context/.claude/commands` contains shell scripts only (no `.md` commands), so nothing to match.
  - Nested plugin command packs are intentionally excluded from trigger matching.
- Skills discovered:
  - Global Codex skills in `$HOME/.codex/skills` (including system skills `skill-creator`, `skill-installer`).
  - Project skills in `lenny/skills` and `CDS/research`.
  - Nested plugin skills in `agent-center/plugins/.../skills` (e.g. `command-development`, `plugin-structure`, `hook-development`, `writing-rules`, `stripe-best-practices`).

--- project-doc ---

# Startup Policy

On every Codex CLI session start, before handling the first user request, run a Claude activity check and include the result in the first reply.

Required check command:

` ` `bash
bash $HOME/.codex/scripts/check-claude-activity.sh
` ` `

If files are missing or inaccessible, report that clearly and continue with best-effort results.

# Response Language Policy

- Respond in Korean by default across Codex sessions unless the user explicitly requests another language.

# Feedback and Truthfulness Policy

사용자 의견, 작업물, 리뷰에 대해 피드백할 때:

- 잘된 부분은 분명히 좋다고 인정한다.
- 이미 충분히 잘 설계된 부분에는 억지로 개선 조언을 추가하지 않는다.
- 모든 요소에 억지로 피드백하려고 하지 말고, 실제로 산출물(기획, 개발, 디자인, CDS 구성, 하네스 등)의 퀄리티에 영향을 주는 문제만 골라서 지적한다.
- 비판을 위한 비판, 역량이 있음을 티 내기 위한 과잉 피드백, 취향 기반 지적은 금지한다.
- 좋은 산출물이라면 좋은 산출물이라고 말하고, 개선이 필요한 지점에만 집중한다.

진실성 규칙:

- 산출물에서 확인할 수 없는 데이터나 연관성 있는 기획, 디자인, 개발 요소를 아는 척하지 않는다.
- 내부 전략을 아는 것처럼 추측하지 않는다.
- 산출물 외에 확인되지 않은 경우, 반드시 관련된 다른 프로젝트 작업물을 확인하고 답변한다.
- 근거가 약하면 강한 표현으로 비판하지 않는다.

# Request Interpretation Guard

사용자 요청이 여러 의미로 해석될 수 있고 그 차이가 작업 범위, 영구 정책,
배정 로직, 산출물 보존 여부에 영향을 주는 경우에는 구현이나 파일 수정 전에
짧게 확인 질문을 한다.

특히 아래 케이스는 의심 신호로 본다:

- 일회성/현재 프로젝트 요청인지, 전역/영구 정책 변경인지 불명확한 경우
- 리서치·분석·플래닝 단계 한정인지, 구현·검증·배포 전체에 적용되는지 불명확한 경우
- "최고 성능", "강하게", "보수적으로" 같은 표현이 특정 단계 품질 요구인지,
  모든 worker allocation 제한인지 불명확한 경우
- 특정 산출물 제거 요청이 planning artifact까지 삭제하라는 뜻인지,
  잘못된 구현/정책 흔적만 제거하라는 뜻인지 불명확한 경우
- 요구를 넓게 해석하면 junior/intern 배정 금지처럼 비용·속도·운영 정책이
  바뀌고, 좁게 해석하면 사용자의 품질 의도를 놓칠 수 있는 경우

기본값:

- 경쟁 해석을 1개의 간결한 질문으로 제시하고 사용자 확인을 기다린다.
- 모호한 표현만으로 global allocator/policy를 영구 변경하지 않는다.
- 난이도 높은 사고나 분석이 필요하지 않은 단순 반복 작업은 명시적 제외 요청이
  없는 한 intern/junior 배정 가능성을 유지한다.

# Clipboard / URL Delivery Policy

- In Codex CLI, do not rely on click-drag selection for URLs or other copy-sensitive strings. The tmux/Codex TUI can intercept mouse drag events and make selection disappear.
- When a URL, Figma link, command output token, or other exact copy target is the primary deliverable, copy it to the macOS clipboard before replying:

` ` `bash
printf '%s' '<copy-target>' | pbcopy
` ` `

- For multiple copy targets, write newline-separated values to `$HOME/.codex/paste-cache/last-copy-targets.txt` and copy that file with `pbcopy < ...`.
- In the reply, state that the value has been copied to the clipboard. If showing it too, use a fenced `text` block, not a Markdown link, so terminal auto-linking is not the primary path.
- The preferred Codex CLI launcher disables tmux mouse capture and uses `codex --no-alt-screen` by default. Opt out only when explicitly needed with `CODEX_TMUX_MOUSE=1` or `CODEX_NO_ALT_SCREEN=0`.

# Shared Memory Policy

Claude Code uses auto memory at `$HOME/.claude/projects/*/memory/MEMORY.md`,
and this path should be symlinked to:

`$HOME/Project/agent-center/memory/MEMORY.md`

This keeps Claude auto-load behavior while allowing Git-based sync across machines.

Codex may reference project CLAUDE.md or SESSION.md for collaboration context.
Cross-tool shared context file is currently not in use (보류).

# Codex Auto-Clear Sentinel

At the beginning of each user turn, before doing new work, check whether a
previous hook already completed a low-context checkpoint:

` ` `bash
bash "$HOME/Project/agent-center/scripts/codex-auto-handoff.sh" --pending-clear --json
` ` `

If it returns `action: "clear_required"`, do not continue the old session.
Report the saved `resume_trigger` and `snapshot_dir`, then end the conversation
with the archive directive when running in Codex Desktop. Do not ask the user to
manually rescue the work as the normal path; the handoff actuator starts a
headless continuation by default after checkpoint success:

` ` `text
::archive{reason="context<25 auto-handoff completed; resume with the saved trigger"}
` ` `

In plain CLI contexts where archive directives are unavailable, stop after
printing the resume trigger and snapshot. The headless continuation is the
primary continuation path; manual clear is only a fallback when the continuation
bridge failed or was disabled.

If the user explicitly says they already restarted/cleared the session, or asks
to fix a stuck/stale clear sentinel, acknowledge the completed handoff instead
of blocking forever:

` ` `bash
bash "$HOME/Project/agent-center/scripts/codex-auto-handoff.sh" --ack-clear --json
` ` `

Then rerun the pending-clear check and continue only if it returns
`action: "none"`. This archives the sentinel under
`$HOME/.codex/auto-handoff/acknowledged/` and preserves the handoff snapshot.
`--pending-clear` may also return `action: "none"` with
`auto_acknowledged_clear: true` after it proves a fresh top-level Codex session
is active and no longer below threshold.
If `CODEX_AUTO_HANDOFF_CLEAR_CMD` is configured and succeeds, the actuator
performs this archive step itself so the next session is not blocked by a stale
sentinel.

# Context-Low Auto-Handoff (Codex)

Exception: if the current user turn is an auto-handoff status relay message
starting with `# Auto-Handoff Status Relay`, do not launch another handoff for
that relay turn. Report only the relayed headless continuation status,
observable progress, and final result in Korean, including concrete actions,
files, tests, outcomes, and next step when the relay body provides them. Do not
expose hidden chain-of-thought; summarize observable progress/actions only. Do
not resume implementation from the old low-context session.

At the beginning of each user turn and before substantial tool work, check the
visible Codex statusline. If it shows `context<25`, or if the task is long enough
that context exhaustion is plausible, run:

` ` `bash
bash "$HOME/Project/agent-center/scripts/context-guard.sh" --agent codex --json
` ` `

If the guard returns `below_threshold: true` or exits `20`, stop starting new
work and execute the automated handoff actuator immediately:

` ` `bash
bash "$HOME/Project/agent-center/scripts/codex-auto-handoff.sh" --json
` ` `

Then report the `resume_trigger`, `snapshot_dir`, and `continue_action`, and
clear/archive as described above. The actuator saves state before any clear
action and starts a fresh headless Codex continuation by default
(`CODEX_AUTO_HANDOFF_CONTINUE=1`) so queued work can continue even if the user
does not manually clear the old session.

Exception: if the current user turn is an explicit `-record` request (the
message starts with `-record` or the first inline trigger token is `-record`),
run only the minimal record workflow needed to persist the current completed
work, then stop. Do not start new implementation, review, exploration, or
planning work while below threshold. Pending `clear_required` sentinel checks
still take precedence; acknowledge a stale sentinel only when the user says the
session was already cleared/restarted.

Manual fallback if the actuator is unavailable:

1. Append a canonical project-local `.ai/HANDOFF.md` entry using the existing
   `HANDOFF / Date / Project / Agent / Summary / Next-TODO / Commits` schema.
   Add `Resume-Trigger:` with the exact reload command from `commands.codex`
   such as `-cds`, or the `reload_instruction` fallback.
2. Update project-local `.ai/SESSION.md` with current objective, completed work,
   dirty files, pending steps, and the next command to run.
3. Run `-record` to commit/push the checkpoint. This step is allowed even when
   context remains below threshold, but only for checkpoint recording.
4. Start a fresh headless continuation with `scripts/codex-auto-continue.sh` if
   the actuator was unavailable but the script exists. Only ask the user to
   manually clear/reload if no continuation bridge can be started.
5. In the next session, the first action must be the project command and then
   reading the latest HANDOFF.

`context-guard.sh` is read-only. It must not run `git`, `record`, `clear`,
`claude`, `codex`, slash commands, or hyphen commands. Mutating behavior belongs
to `codex-auto-handoff.sh`.

The shell-level actuator writes a clear-required sentinel. A documented Codex
CLI `clear` command is not currently available; if a local bridge is later
installed, set `CODEX_AUTO_HANDOFF_CLEAR_CMD` and the actuator will run it only
after checkpoint success. When that clear command succeeds, the sentinel is
archived instead of left pending.

# Codex Hyphen Trigger Guard

At the beginning of each Codex user turn, after pending-clear/context checks and
before any file edits or direct implementation, run the hyphen trigger guard
with the current user message:

` ` `bash
bash "$HOME/Project/agent-center/scripts/codex-hyphen-trigger-guard.sh" check \
  --repo "$(git rev-parse --show-toplevel 2>/dev/null || pwd)" \
  --message "<current user message>" \
  --json
` ` `

If the message is too large or quoting would be fragile, write it to a temporary
file and use `--message-file`.

If the guard returns `action: "start_play_required"`, do not make direct edits,
do not answer with only a plan, and do not continue a Default-mode
implementation. Start the public play entrypoint first:

` ` `bash
bash "$HOME/Project/agent-center/scripts/play.sh" start \
  --repo "$(git rev-parse --show-toplevel 2>/dev/null || pwd)" \
  --slug "<short-topic-label>" \
  --request-text "<current or pending request text>" \
  --runtime auto \
  --target claude \
  --timeout-seconds 2700 \
  --max-repair-rounds 1 \
  --fresh-runtime auto \
  --desktop-controller codex \
  --daemon
` ` `

`play.sh start` acknowledges the pending trigger after a `task-dag.json` run is
created. If the daemon or headless runtime fails, continue only through the
documented play recovery artifacts in that run; do not silently finish by direct
implementation. This guard exists because a prior Codex session accepted a
`-play` request, then handled the following "Implement the plan" turn directly
and skipped the play final report hook.

# Project AGENTS Policy

Global Codex behavior such as context-low auto-handoff belongs in this file and
is loaded through `~/.codex/AGENTS.md -> ~/Project/agent-center/AGENTS.md`.
Project-level `AGENTS.md` files should stay optional project routers for repo
maps, SSOT documents, and verification commands. Do not duplicate this
context-low policy into every project.

# Codex Native Goal Bridge

Codex's built-in `/goal` is not a hyphen command and is not the same as a
project command file. It is native Codex goal state exposed to the model through
`get_goal` / `create_goal` / `update_goal`.

At the beginning of each Codex user turn, after pending-clear/context checks,
call `get_goal` when either of these is true:

- the user mentions `/goal`, Codex native goal, or goal mode;
- the visible context suggests an active native goal may exist.

If `get_goal` returns an active goal objective, route that objective into the
canonical `-play` autonomous runner. Use:

` ` `bash
bash "$HOME/Project/agent-center/scripts/codex-native-goal-bridge.sh" start \
  --repo "$(git rev-parse --show-toplevel 2>/dev/null || pwd)" \
  --objective "<get_goal objective>" \
  --desktop-controller codex
` ` `

The bridge records idempotent mappings under:

` ` `text
<repo>/.ai/codex-native-goals/<objective-hash>.json
` ` `

Do not treat Codex native `/goal` as `/goal` command text or as the public
`-goal` hyphen trigger. `-goal` may exist only as a compatibility shortcut; the
native Codex goal integration is `get_goal` → `codex-native-goal-bridge.sh` →
`play.sh goal-init/goal-run`.

When a native-goal-backed play DAG is confirmed `done` and no required work
remains, call `update_goal(status="complete")`. If the play runner is daemonized
and still running, leave the native goal active and report the run directory and
status file instead of marking it complete.

# Codex Computer Use Recovery

Codex Computer Use has two separate local processes:

- `SkyComputerUseService`: the macOS app/service that needs TCC permissions.
- `SkyComputerUseClient mcp`: the stdio MCP transport owned by a live Codex
  session.

Never kill `SkyComputerUseClient mcp` from inside an active Codex session. If it
is killed, the current session's Computer Use tool handle becomes
`Transport closed` and cannot be reattached from the model side. Restart only
`SkyComputerUseService` when trying to refresh TCC state.

If Computer Use fails with macOS/TCC errors, run:

` ` `bash
bash "$HOME/Project/agent-center/scripts/codex-computer-use-recover.sh" --fresh-smoke --json
` ` `

Interpretation:

- fresh-smoke `ok`: global TCC/plugin state is good; use the canonical
  fresh-runtime path (`play-desktop-actuator.sh` / `codex exec`) or start a
  fresh top-level Codex session if the current direct tool handle is closed.
- fresh-smoke `failed` or `timeout`: use
  `desktop-control-permission-doctor.sh --warmup --open-settings`, approve the
  expected macOS prompts, then rerun the smoke.

For service-only refresh:

` ` `bash
bash "$HOME/Project/agent-center/scripts/codex-computer-use-recover.sh" --restart-service --fresh-smoke --json
` ` `

# Peer Review Auto-Loop (Codex)

When invoked via review triggers `-codex-review`, `-claude-review`, `-review--codex`, 또는 `-review--claude`, run **PASS까지 자동 반복**.

`-review` is a separate local artifact-review harness, not a peer-review
auto-loop trigger. For Figma/CDS URLs or node ids, `-review` must load the
project Figma/CDS rules and include Visual/UX, CDS Usage, Node Structure, and
Rubric Verdict in the first report.

> **Plan 트리거는 자동 반복 대상 아님** — `-codex-plan` / `-claude-plan` / `-plan--codex` / `-plan--claude`는 한 번 받고 사용자 결정 흐름.
>
> **Controller-only guard** — 이 룰은 review를 *요청하는* 컨트롤러에만 적용. headless peer reviewer 역할(peer-agent-review.sh가 호출한 reviewer 자신)은 **nested peer review를 시작 금지**.
>
> **도구별 트리거 형식 (의미 동일)** — Codex는 hyphen만 사용 (AGENTS.md trigger policy: slash 미지원). Claude Code 측 CLAUDE.md는 slash + hyphen 둘 다 표기하지만 의미는 동일하며, 단지 입력 형식만 다르다.
>
> **Timeout 기준** — headless peer review는 오래 걸릴 수 있다. 기본 timeout은 2700초(45분)이며, 그 전에는 hang으로 간주하지 않는다. 필요한 경우 `--timeout-seconds` 또는 `PEER_AGENT_REVIEW_TIMEOUT_SECONDS`로 조정하고, `0`은 timeout 비활성화다.
>
> **Persona/model tier 기준** — 직군 persona 및 intern/junior/senior/lead model/effort 선택은 `-play`/`-director` 내부 routing metadata다. `-senior`, `-xhigh`, `-model-*`, `-pm`, `-backend` 같은 새 public trigger로 만들지 않는다.

## Loop

1. peer review 실행 → 결과 평가
2. **PASS** → 완료 (사용자에게 짧게 보고)
3. **FAIL** → finding 처리 (아래 토론 합의) → 수정 → 재실행
4. **NEEDS_USER_DECISION** → 즉시 사용자 의견 요청 (자동 진행 금지)

## 안전 장치 (무한 루프 방지)

- 최대 5회 반복 → 그 이상 시 사용자 에스컬레이션
- 동일 finding 2회 연속 등장 → 즉시 사용자 에스컬레이션
- recursion blocked 응답 → 자동 종료 후 사용자 보고
- 매 반복마다 회차/판정/finding 요약을 1줄로 사용자에게 노출

## Finding 토론 합의 (맹목 수용 X)

- **Accept** — 동의 시 그대로 수정
- **Debate** — 치명적 결함이거나 전제가 틀린 finding:
  1. 반대 근거 명시 + 사용자에게 토론 요청
  2. 사용자 합의 방향대로 반영
  3. 합의 안 되면 사용자 결정 우선
- **Skip with sourcing** — 명백히 잘못된 finding을 skip할 때:
  1. 구체적 evidence/source 인용 필수
  2. High/Critical severity 또는 전제 dispute는 skip 전 사용자 confirm 필수
  3. review run 메모에 skip 사유 + 출처 기록 (감사 가능성)

## 학습 자료 참조

- 보고서/패턴: `~/Project/lenny/skills/ai-ops-expert/references/harness-engineering.md` §13 (Peer Review as Harness Gate)
- Skill: `~/Project/lenny/skills/ai-ops-expert/SKILL.md` (자동 매칭)

> 근거: 2026-04-28 사용자 룰 — "치명적 결함이고 의견 다를 때는 반드시 따를 필요 없음, 토론 후 합의 방향으로 반영"

# Trigger Policy (Codex)

Codex uses hyphen triggers as the single official command/skill invocation format.

## Input normalization

- Official trigger: if user input starts with `-`, parse as: `-name [args...]`.
- Also support inline trigger tokens: if input contains ` -name` anywhere, treat it as a command trigger.
  - Example supported: `자동 중재 조건을 플래닝해줘 -director`
  - Use the first matched `-name` token as trigger; keep remaining text as arguments/context.
- Slash-style triggers (`/name`) are not used in Codex.
- Bare triggers (`name [args...]`) are not treated as command invocations in Codex.
- Normalize only the trigger token (`name`) for matching; keep original args unchanged.
- This applies globally to all matched commands/skills across scanned projects (e.g. `-coach`, `-director`, `-record`, `-live`, `-lennylive`).

## CDS naming guard

- In `$HOME/Project/CDS`, treat `CONSTITUTION.md` as the canonical policy file.
- Do not create, restore, or modify `AGENTS.md` in CDS.
- If instructions mention CDS `AGENTS.md`, map it to `CONSTITUTION.md`.

## Command matching (Claude commands)

- Check in this priority order:
  1. `<current_project>/.claude/commands/{name}.md` (project-local override)
  2. `$HOME/.claude/commands/{name}.md` (global symlinked workspace)
  3. `$HOME/Project/*/.claude/commands/{name}.md` (project-root only)
  4. `$HOME/Project/*/commands/{name}.md` (project-root only)
- If found, load that command definition and execute its workflow.
- Exclude nested command packs under subdirectories (for example `.../plugins/.../commands`).
- Exclude these command names from trigger matching: `execute-refactor`, `plan-parallel`, `plan-refactor`, `plan-spec-improvements`, `refactor`, `validate-security`, `validate-slc-arch`, `validate-spec-planning`, `validate-vibe-coding`, `plan-dev`.

## Skill matching (Codex skills)

- Check in this priority order:
  1. `$HOME/.codex/skills/{name}/SKILL.md` (global Codex skills)
  2. `$HOME/Project/*/skills/{name}/SKILL.md` (project skill packs)
  3. `$HOME/Project/**/skills/{name}/SKILL.md` (plugin/nested skill packs)
- If found, apply the skill for the turn.
- In `$HOME/Project/lenny/skills`, `*.md` files are treated as skill-equivalent sources (same role as `.skill`).

## When both match

- If the same `name` matches both a command and a skill, run both with minimal context:
  1. Load/execute command workflow.
  2. Apply skill guidance for implementation details.
- State briefly which one(s) were activated.

## Current inventory check baseline (updated 2026-05-21, all projects)

- Projects scanned: `AIZen`, `CDS`, `agent-center`, `lenny`, `lenny-live`, `plumlabs-context`, `simulator`, `wavvy`, `wellness-challenge-platform`.
- Commands discovered:
  - `agent-center/commands`: `cds`, `claude-plan`, `claude-review`, `coach`, `codex-plan`, `codex-review`, `codex-status`, `context-guard`, `design`, `director`, `end-live`, `goal`, `lenny`, `lennylive`, `live`, `plan--claude`, `plan--codex`, `play`, `plum`, `price`, `qa`, `ralph`, `record`, `research`, `review`, `review--claude`, `review--codex`, `team`, `wavvy`, `well`, `zen`.
  - `agent-center/scripts`: `team-model-orchestrator.sh` is an internal helper used by `play`/`director`, not a public command trigger.
  - `AIZen/.claude/commands`: `aizen`, `aizen-new`.
  - `wellness-challenge-platform/.claude/commands`: `execute-refactor`, `plan-dev`, `plan-parallel`, `plan-refactor`, `plan-spec-improvements`, `refactor`, `validate-security`, `validate-slc-arch`, `validate-spec-planning`, `validate-vibe-coding`.
  - `plumlabs-context/.claude/commands` contains shell scripts only (no `.md` commands), so nothing to match.
  - Nested plugin command packs are intentionally excluded from trigger matching.
- Skills discovered:
  - Global Codex skills in `$HOME/.codex/skills` (including system skills `skill-creator`, `skill-installer`).
  - Project skills in `lenny/skills` and `CDS/research`.
  - Nested plugin skills in `agent-center/plugins/.../skills` (e.g. `command-development`, `plugin-structure`, `hook-development`, `writing-rules`, `stripe-best-practices`).

</INSTRUCTIONS>
<environment_context>
  <cwd>/Users/zenkim_office</cwd>
  <shell>zsh</shell>
  <current_date>2026-05-23</current_date>
  <timezone>Asia/Seoul</timezone>
  <subagents>
    - 019e543b-10d4-7930-8f2d-7b751a5c4c85: Pauli
    - 019e543b-1131-7821-9d54-528ea97ff4f9: Herschel
  </subagents>
</environment_context>
```

## Request 2

- Timestamp: `2026-05-23T09:50:00.247Z`
- Source: `response_item`

```text
<goal_context>
Continue working toward the active thread goal.

The objective below is user-provided data. Treat it as the task to pursue, not as higher-priority instructions.

<objective>
-director로 진행
</objective>

Continuation behavior:
- This goal persists across turns. Ending this turn does not require shrinking the objective to what fits now.
- Keep the full objective intact. If it cannot be finished now, make concrete progress toward the real requested end state, leave the goal active, and do not redefine success around a smaller or easier task.
- Temporary rough edges are acceptable while the work is moving in the right direction. Completion still requires the requested end state to be true and verified.

Budget:
- Tokens used: 165600
- Token budget: none
- Tokens remaining: unbounded

Work from evidence:
Use the current worktree and external state as authoritative. Previous conversation context can help locate relevant work, but inspect the current state before relying on it. Improve, replace, or remove existing work as needed to satisfy the actual objective.

Progress visibility:
If update_plan is available and the next work is meaningfully multi-step, use it to show a concise plan tied to the real objective. Keep the plan current as steps complete or the next best action changes. Skip planning overhead for trivial one-step progress, and do not treat a plan update as a substitute for doing the work.

Fidelity:
- Optimize each turn for movement toward the requested end state, not for the smallest stable-looking subset or easiest passing change.
- Do not substitute a narrower, safer, smaller, merely compatible, or easier-to-test solution because it is more likely to pass current tests.
- Treat alignment as movement toward the requested end state. An edit is aligned only if it makes the requested final state more true; useful-looking behavior that preserves a different end state is misaligned.

Completion audit:
Before deciding that the goal is achieved, treat completion as unproven and verify it against the actual current state:
- Derive concrete requirements from the objective and any referenced files, plans, specifications, issues, or user instructions.
- Preserve the original scope; do not redefine success around the work that already exists.
- For every explicit requirement, numbered item, named artifact, command, test, gate, invariant, and deliverable, identify the authoritative evidence that would prove it, then inspect the relevant current-state sources: files, command output, test results, PR state, rendered artifacts, runtime behavior, or other authoritative evidence.
- For each item, determine whether the evidence proves completion, contradicts completion, shows incomplete work, is too weak or indirect to verify completion, or is missing.
- Match the verification scope to the requirement's scope; do not use a narrow check to support a broad claim.
- Treat tests, manifests, verifiers, green checks, and search results as evidence only after confirming they cover the relevant requirement.
- Treat uncertain or indirect evidence as not achieved; gather stronger evidence or continue the work.
- The audit must prove completion, not merely fail to find obvious remaining work.

Do not rely on intent, partial progress, memory of earlier work, or a plausible final answer as proof of completion. Marking the goal complete is a claim that the full objective has been finished and can withstand requirement-by-requirement scrutiny. Only mark the goal achieved when current evidence proves every requirement has been satisfied and no required work remains. If the evidence is incomplete, weak, indirect, merely consistent with completion, or leaves any requirement missing, incomplete, or unverified, keep working instead of marking the goal complete. If the objective is achieved, call update_goal with status "complete" so usage accounting is preserved. If the achieved goal has a token budget, report the final consumed token budget to the user after update_goal succeeds.

Blocked audit:
- Do not call update_goal with status "blocked" the first time a blocker appears.
- Only use status "blocked" when the same blocking condition has repeated for at least three consecutive goal turns, counting the original/user-triggered turn and any automatic goal continuations.
- If the user resumes a goal that was previously marked "blocked", treat the resumed run as a fresh blocked audit. If the same blocking condition then repeats for at least three consecutive resumed goal turns, call update_goal with status "blocked" again.
- Use status "blocked" only when you are truly at an impasse and cannot make meaningful progress without user input or an external-state change.
- Once the blocked threshold is satisfied, do not keep reporting that you are still blocked while leaving the goal active; call update_goal with status "blocked".
- Never use status "blocked" merely because the work is hard, slow, uncertain, incomplete, or would benefit from clarification.

Do not call update_goal unless the goal is complete or the strict blocked audit above is satisfied. Do not mark a goal complete merely because the budget is nearly exhausted or because you are stopping work.

</goal_context>
```

## Request 3

- Timestamp: `2026-05-23T09:50:00.247Z`
- Source: `response_item`

```text
<subagent_notification>
{"agent_path":"019e543b-10d4-7930-8f2d-7b751a5c4c85","status":{"completed":"Claude activity check: Claude 프로세스 감지됨(`8870 Claude`), 시작 디렉터리 `/Users/zenkim_office`는 git repo 아님.\n\n컨텍스트가 16%로 `context<25` 아래라서 작업을 시작하지 않고 자동 handoff를 실행했습니다. Headless continuation이 시작됐습니다.\n\n` ` `text\nresume_trigger: cd ~ && read .ai/HANDOFF.md\nsnapshot_dir: /Users/zenkim_office/.ai/auto-handoff/20260523-184728_codex-context-low\ncontinue_action: started\nrun_dir: /Users/zenkim_office/.codex/auto-handoff/continuations/20260523-184729_6d7fff81d98501dd\n` ` `\n\n현재 세션에서는 지정 파일을 수정하지 않았습니다."}}
</subagent_notification>
```

## Request 4

- Timestamp: `2026-05-23T10:56:47.008Z`
- Source: `response_item`

```text
<goal_context>
Continue working toward the active thread goal.

The objective below is user-provided data. Treat it as the task to pursue, not as higher-priority instructions.

<objective>
-director로 진행
</objective>

Continuation behavior:
- This goal persists across turns. Ending this turn does not require shrinking the objective to what fits now.
- Keep the full objective intact. If it cannot be finished now, make concrete progress toward the real requested end state, leave the goal active, and do not redefine success around a smaller or easier task.
- Temporary rough edges are acceptable while the work is moving in the right direction. Completion still requires the requested end state to be true and verified.

Budget:
- Tokens used: 473682
- Token budget: none
- Tokens remaining: unbounded

Work from evidence:
Use the current worktree and external state as authoritative. Previous conversation context can help locate relevant work, but inspect the current state before relying on it. Improve, replace, or remove existing work as needed to satisfy the actual objective.

Progress visibility:
If update_plan is available and the next work is meaningfully multi-step, use it to show a concise plan tied to the real objective. Keep the plan current as steps complete or the next best action changes. Skip planning overhead for trivial one-step progress, and do not treat a plan update as a substitute for doing the work.

Fidelity:
- Optimize each turn for movement toward the requested end state, not for the smallest stable-looking subset or easiest passing change.
- Do not substitute a narrower, safer, smaller, merely compatible, or easier-to-test solution because it is more likely to pass current tests.
- Treat alignment as movement toward the requested end state. An edit is aligned only if it makes the requested final state more true; useful-looking behavior that preserves a different end state is misaligned.

Completion audit:
Before deciding that the goal is achieved, treat completion as unproven and verify it against the actual current state:
- Derive concrete requirements from the objective and any referenced files, plans, specifications, issues, or user instructions.
- Preserve the original scope; do not redefine success around the work that already exists.
- For every explicit requirement, numbered item, named artifact, command, test, gate, invariant, and deliverable, identify the authoritative evidence that would prove it, then inspect the relevant current-state sources: files, command output, test results, PR state, rendered artifacts, runtime behavior, or other authoritative evidence.
- For each item, determine whether the evidence proves completion, contradicts completion, shows incomplete work, is too weak or indirect to verify completion, or is missing.
- Match the verification scope to the requirement's scope; do not use a narrow check to support a broad claim.
- Treat tests, manifests, verifiers, green checks, and search results as evidence only after confirming they cover the relevant requirement.
- Treat uncertain or indirect evidence as not achieved; gather stronger evidence or continue the work.
- The audit must prove completion, not merely fail to find obvious remaining work.

Do not rely on intent, partial progress, memory of earlier work, or a plausible final answer as proof of completion. Marking the goal complete is a claim that the full objective has been finished and can withstand requirement-by-requirement scrutiny. Only mark the goal achieved when current evidence proves every requirement has been satisfied and no required work remains. If the evidence is incomplete, weak, indirect, merely consistent with completion, or leaves any requirement missing, incomplete, or unverified, keep working instead of marking the goal complete. If the objective is achieved, call update_goal with status "complete" so usage accounting is preserved. If the achieved goal has a token budget, report the final consumed token budget to the user after update_goal succeeds.

Blocked audit:
- Do not call update_goal with status "blocked" the first time a blocker appears.
- Only use status "blocked" when the same blocking condition has repeated for at least three consecutive goal turns, counting the original/user-triggered turn and any automatic goal continuations.
- If the user resumes a goal that was previously marked "blocked", treat the resumed run as a fresh blocked audit. If the same blocking condition then repeats for at least three consecutive resumed goal turns, call update_goal with status "blocked" again.
- Use status "blocked" only when you are truly at an impasse and cannot make meaningful progress without user input or an external-state change.
- Once the blocked threshold is satisfied, do not keep reporting that you are still blocked while leaving the goal active; call update_goal with status "blocked".
- Never use status "blocked" merely because the work is hard, slow, uncertain, incomplete, or would benefit from clarification.

Do not call update_goal unless the goal is complete or the strict blocked audit above is satisfied. Do not mark a goal complete merely because the budget is nearly exhausted or because you are stopping work.

</goal_context>
```

## Request 5

- Timestamp: `2026-05-23T10:57:34.706Z`
- Source: `response_item`

```text
<goal_context>
Continue working toward the active thread goal.

The objective below is user-provided data. Treat it as the task to pursue, not as higher-priority instructions.

<objective>
-director로 진행
</objective>

Continuation behavior:
- This goal persists across turns. Ending this turn does not require shrinking the objective to what fits now.
- Keep the full objective intact. If it cannot be finished now, make concrete progress toward the real requested end state, leave the goal active, and do not redefine success around a smaller or easier task.
- Temporary rough edges are acceptable while the work is moving in the right direction. Completion still requires the requested end state to be true and verified.

Budget:
- Tokens used: 667295
- Token budget: none
- Tokens remaining: unbounded

Work from evidence:
Use the current worktree and external state as authoritative. Previous conversation context can help locate relevant work, but inspect the current state before relying on it. Improve, replace, or remove existing work as needed to satisfy the actual objective.

Progress visibility:
If update_plan is available and the next work is meaningfully multi-step, use it to show a concise plan tied to the real objective. Keep the plan current as steps complete or the next best action changes. Skip planning overhead for trivial one-step progress, and do not treat a plan update as a substitute for doing the work.

Fidelity:
- Optimize each turn for movement toward the requested end state, not for the smallest stable-looking subset or easiest passing change.
- Do not substitute a narrower, safer, smaller, merely compatible, or easier-to-test solution because it is more likely to pass current tests.
- Treat alignment as movement toward the requested end state. An edit is aligned only if it makes the requested final state more true; useful-looking behavior that preserves a different end state is misaligned.

Completion audit:
Before deciding that the goal is achieved, treat completion as unproven and verify it against the actual current state:
- Derive concrete requirements from the objective and any referenced files, plans, specifications, issues, or user instructions.
- Preserve the original scope; do not redefine success around the work that already exists.
- For every explicit requirement, numbered item, named artifact, command, test, gate, invariant, and deliverable, identify the authoritative evidence that would prove it, then inspect the relevant current-state sources: files, command output, test results, PR state, rendered artifacts, runtime behavior, or other authoritative evidence.
- For each item, determine whether the evidence proves completion, contradicts completion, shows incomplete work, is too weak or indirect to verify completion, or is missing.
- Match the verification scope to the requirement's scope; do not use a narrow check to support a broad claim.
- Treat tests, manifests, verifiers, green checks, and search results as evidence only after confirming they cover the relevant requirement.
- Treat uncertain or indirect evidence as not achieved; gather stronger evidence or continue the work.
- The audit must prove completion, not merely fail to find obvious remaining work.

Do not rely on intent, partial progress, memory of earlier work, or a plausible final answer as proof of completion. Marking the goal complete is a claim that the full objective has been finished and can withstand requirement-by-requirement scrutiny. Only mark the goal achieved when current evidence proves every requirement has been satisfied and no required work remains. If the evidence is incomplete, weak, indirect, merely consistent with completion, or leaves any requirement missing, incomplete, or unverified, keep working instead of marking the goal complete. If the objective is achieved, call update_goal with status "complete" so usage accounting is preserved. If the achieved goal has a token budget, report the final consumed token budget to the user after update_goal succeeds.

Blocked audit:
- Do not call update_goal with status "blocked" the first time a blocker appears.
- Only use status "blocked" when the same blocking condition has repeated for at least three consecutive goal turns, counting the original/user-triggered turn and any automatic goal continuations.
- If the user resumes a goal that was previously marked "blocked", treat the resumed run as a fresh blocked audit. If the same blocking condition then repeats for at least three consecutive resumed goal turns, call update_goal with status "blocked" again.
- Use status "blocked" only when you are truly at an impasse and cannot make meaningful progress without user input or an external-state change.
- Once the blocked threshold is satisfied, do not keep reporting that you are still blocked while leaving the goal active; call update_goal with status "blocked".
- Never use status "blocked" merely because the work is hard, slow, uncertain, incomplete, or would benefit from clarification.

Do not call update_goal unless the goal is complete or the strict blocked audit above is satisfied. Do not mark a goal complete merely because the budget is nearly exhausted or because you are stopping work.

</goal_context>
```
