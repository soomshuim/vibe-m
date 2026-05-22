# Peer Agent Review

| Field | Value |
|---|---|
| Target | claude |
| Mode | plan |
| Project | wavvy |
| Repo | /Users/zenkim_office/Project/wavvy |
| Git repo | yes |
| Branch | master |
| Created | 2026-05-22 13:38:31 KST |
| Exit code | 0 |
| Timeout seconds | 2700 |
| Attempts | 2 |

## Request

Play run: /Users/zenkim_office/Project/wavvy/.ai/pipeline/runs/20260522-132827_wavvy-write-command-shim-impl
Review the implementation plan artifact for this play harness run.
Source artifact: /Users/zenkim_office/Project/wavvy/.ai/pipeline/runs/20260522-132827_wavvy-write-command-shim-impl/03-plan.md

Original request:
/Users/zenkim_office/Project/wavvy/.ai/pipeline/runs/20260522-132827_wavvy-write-command-shim-impl/request.md

Proposal-only run: false

## Artifact Content

# 03-plan.md — Wavvy `/write` · `-write` Thin Shim Implementation Plan

## Startup / Guard Snapshot
- Claude activity check: `bash $HOME/.codex/scripts/check-claude-activity.sh` 실행 완료 (2026-05-22, KST 기준), 접근 불가 항목 없음.
- 본 단계는 기존 top-level play run 내부 bounded artifact 작성이며, 추가 autonomous runner는 시작하지 않는다.

## Objective
`/write`(Claude)와 `-write`(Codex)를 Wavvy 로컬에서 **lyric 전용 thin shim**으로 연결한다.
명령 자체는 라우팅만 담당하고, 규칙/품질 기준/검증은 기존 SSOT 및 CLI 하네스에 위임한다.

## Scope
- 포함:
  - 로컬 `write` command shim 추가/수정
  - lyric 작성/리라이트/리뷰 범위 라우팅
  - 비범위 요청(YouTube copy, concept/changelog 등) 차단/리다이렉트 문구
- 제외:
  - lyric 규칙 본문 신규 작성/복제
  - 비가사 도메인 라우팅 확장
  - 추가 자동화 러너/오케스트레이션 도입

## Target Files
1. `.claude/commands/write.md` (신규 권장)
- `/write` 해석의 프로젝트 로컬 진입점.
- Codex hyphen trigger 정책상 `-write`도 동일 이름 command를 우선 탐지하므로 공용 shim으로 사용.

2. `AGENTS.md` (필요 시 최소 보강)
- 이미 trigger policy가 존재하면 수정 생략.
- 필요할 때만 “`write`는 lyric-only 라우팅 command” 수준의 짧은 참조 문구 추가(중복 정책 금지).

3. `.ai/SESSION.md` (조건부)
- 구현/검증 완료 후 남은 TODO 정리 시에만 업데이트.

4. `CHANGELOG.md` (조건부)
- 저장소 워크플로우가 durable 상태 변경 기록을 요구할 때만 업데이트.

## Command Content Specification (`.claude/commands/write.md`)
- 필수 포함:
  - 목적: lyric 작성/리라이트/리뷰 전용
  - SSOT 참조:
    - `skills/wavvy-lyricist/SKILL.md`
    - `MASTER/lyrics/skills/WAVVY_LYRIC_SKILL_SPEC.md`
  - 실행 하네스 참조:
    - `python3 wavvy.py lyrics-skill SERIES/[series] --json`
    - `python3 wavvy.py gate SERIES/[series] --stage lyrics-review --json`
  - 범위 밖 요청 처리:
    - YouTube metadata, concept/changelog, 일반 문서 작성 요청은 해당 전용 경로로 리다이렉트
- 금지:
  - 작사 규칙/루브릭/패턴 원문 복붙
  - 장문 정책 내장

## Sequencing
1. 현행 구조 확인
- `.claude/commands/` 존재 여부 및 기존 `write.md` 충돌 확인.
- `AGENTS.md` 내 trigger/라우팅 문구 중복 여부 확인.

2. Shim 작성
- `.claude/commands/write.md` 생성(또는 최소 수정)으로 `/write`, `-write` 공통 진입점 확보.

3. 범위 가드 반영
- lyric-only 허용/비범위 리다이렉트 문구 명시.

4. 검증 수행
- command 발견 확인 + lightweight 하네스/위생 체크 실행.

5. 문서 반영(조건부)
- 실제 durable 상태 변경 시에만 `.ai/SESSION.md`/`CHANGELOG.md` 갱신.

## Verification Plan
1. Command discovery
- `test -f .claude/commands/write.md`
- 저장소 내 `write` 명령 충돌 파일 탐색(`rg --files | rg 'commands/write\.md|skills/.*/write'`)

2. Content gate (thin shim)
- `write.md`가 SSOT 링크/CLI 위임만 포함하는지 확인
- lyric 규칙 본문 복제 문구가 없는지 `rg`로 점검

3. Harness gate (영향 확인)
- `python3 wavvy.py lyrics-skill SERIES/[series] --json`
- `python3 wavvy.py gate SERIES/[series] --stage lyrics-review --json`

4. Hygiene gate
- `git diff --check`

## Acceptance Gates
- `/write`와 `-write`가 모두 프로젝트 로컬 `write` shim으로 해석 가능한 구조다.
- command는 lyric-only 범위를 명시하고, 비가사 요청을 명확히 차단/리다이렉트한다.
- command 본문에 lyric 정책/루브릭 복제가 없다(SSOT 참조만 존재).
- 지정된 lightweight 검증이 통과한다(또는 실패 시 원인/영향이 기록된다).
- durable 문서 업데이트는 “필요한 경우에만” 반영된다.

## Rollback Plan
1. 신규 파일만 추가된 경우
- `git rm .claude/commands/write.md`로 원복 가능.

2. 기존 파일 수정 포함 시
- 해당 파일별 최소 되돌림 커밋으로 복원(부분 되돌림 우선, hard reset 금지).

3. 문서 변경 동반 시
- `.ai/SESSION.md`, `CHANGELOG.md`의 이번 항목만 역패치하여 상태 일관성 유지.

## Risks and Mitigations
- 리스크: command가 비가사 요청까지 흡수
- 대응: lyric-only 가드 문구와 리다이렉트 문구를 명시

- 리스크: 규칙 중복으로 SSOT 드리프트
- 대응: 규칙 본문 금지, 참조 링크 + CLI 하네스만 유지

- 리스크: 도구별 트리거 불일치
- 대응: 단일 `write.md` 공용 진입점 채택 후 discovery 체크로 확인

## Image Generation Routing Gate
본 작업은 이미지 생성 범위가 아니므로 실행 없음.
단, 향후 `/write` 연계 작업이 시각물 산출을 포함하면 아래를 강제한다.

- 기본: 일반 단발성 비주얼은 Codex 내장 `image_gen` 사용
- 예외: 아래 요건 중 하나라도 있으면 OpenAI Images API `gpt-image-2` 사용
  - GPT Image 2/gen2 명시 요구
  - 모델 근거/재현성 필요
  - 배치 생성 필요
  - manifest/hash/request-id 기록 필요
  - 납품/클라이언트 리뷰 추적 필요
- 투명 PNG/alpha 요구 시:
  - 결과물에 대해 별도 후처리 및 alpha 채널 검증 게이트를 명시적으로 수행한다.

## Context

### Git Status

```
 M .ai/codex-hyphen-trigger-guard.json
?? .ai/peer-review/runs/20260522-132224-claude-review-5049.md
?? .ai/peer-review/runs/20260522-132947-claude-review-7636.md
?? .ai/pipeline/runs/20260522-132138_wavvy-write-command-shim/
?? .ai/pipeline/runs/20260522-132827_wavvy-write-command-shim-impl/
```

### Diff Stat

```
 .ai/codex-hyphen-trigger-guard.json | 7 +++----
 1 file changed, 3 insertions(+), 4 deletions(-)
```

## Peer Result

### Peer Review Verdict
- **Result: PASS**
- **Confidence: high**

### Summary

The plan is well-structured, correctly scoped, and all critical assumptions verified against repository state:
- All referenced SSOT files exist
- CLI commands (`lyrics-skill`, `gate --stage lyrics-review`) confirmed available
- Scope correctly limited to lyric-only per team decision
- No rule duplication risk — SSOT reference-only approach is sound
- Rollback plan is safe and proportionate

### Minor Notes (non-blocking)
1. `.claude/commands/` directory doesn't exist yet — needs explicit `mkdir -p` during implementation
2. AGENTS.md modification likely unnecessary given its own "don't duplicate rules" working agreement
3. Keep command file thin (~40 lines max)

**Requesting agent should proceed with implementation.**
