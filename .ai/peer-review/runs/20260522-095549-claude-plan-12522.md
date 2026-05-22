# Peer Agent Review

| Field | Value |
|---|---|
| Target | claude |
| Mode | plan |
| Project | wavvy |
| Repo | /Users/zenkim_office/Project/wavvy |
| Git repo | yes |
| Branch | master |
| Created | 2026-05-22 10:09:44 KST |
| Exit code | 0 |
| Timeout seconds | 2700 |
| Attempts | 4 |

## Request

Play run: /Users/zenkim_office/Project/wavvy/.ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness
Review the implementation plan artifact for this play harness run.
Source artifact: /Users/zenkim_office/Project/wavvy/.ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/03-plan.md

Original request:
wavvy 전용 작사 스킬을 만들고 싶어. 필요한 자료를 리서치하고 스킬과 에이전트 하네스를 구성해줘. -play

Proposal-only run: false

## Artifact Content

# 03-plan.md — Wavvy 작사 스킬 + 에이전트 하네스 구현 계획

## 0) 세션/선행 체크 (필수)
- Claude activity check: **완료** (`2026-05-22 09:53:38 KST`)
- auto-handoff pending-clear: **`action=none`, `clear_required=false`**
- context guard: **`below_threshold=false` (remaining 30%)**
- hyphen trigger guard: **`action=none` (bounded stage prompt로 인식)**

## 1) 목표와 구현 원칙
- 목표: Wavvy 전용 작사 스킬을 “리서치 근거 + 스킬 계약 + 하네스 게이트”로 일관되게 구성한다.
- 원칙:
  - 기존 SSOT 확장 방식: `MASTER/lyrics/LYRICS.md` v4.2를 기준으로 **대체가 아닌 확장**.
  - 기존 리서치 재사용: `20260521-233704_17-pop-rnb-lyrics-research` 산출물을 우선 사용.
  - 검증 타깃 고정: `SERIES/17-00`을 1차 하네스 검증 데이터셋으로 사용.
  - 변경은 소규모/가역적으로 진행하고 각 단계마다 게이트 통과 여부를 기록.

## 2) 범위
- 포함:
  - 작사 리서치 근거 정리 및 규칙화
  - Wavvy 전용 작사 스킬 명세(입력/출력/금지/실패 처리)
  - 에이전트 하네스 실행 흐름(초안→자가검수→판정)
  - PASS/FAIL/USER_DECISION 판정 기준 수치화
- 제외:
  - 오디오 생성/믹싱 자동화
  - 업로드/배포 자동화 확장
  - 본 단계에서 러너 중첩 실행

## 3) 파일 단위 구현 계획
1. 리서치 베이스라인 고정
- 읽기:
  - `.ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/research/2026-pop-rnb-lyric-patterns.md`
  - `.ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/gate-status.json`
  - `MASTER/lyrics/LYRICS.md`
- 산출(신규/갱신):
  - `.ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/research/lyrics-skill-baseline.md`
- 내용:
  - 재사용 가능한 lexicon/hook 원칙
  - LYRICS v4.2와 충돌 가능 규칙 목록
  - 스킬 반영 우선순위(필수/권장/실험)

2. 스킬 계약 문서화
- 산출:
  - `MASTER/lyrics/skills/WAVVY_LYRIC_SKILL_SPEC.md` (신규)
- 내용:
  - 입력 스키마: `series`, `track`, `concept`, `language_mix`, `bpm_hint`, `mood`, `forbidden_patterns`, `structure_target`
  - 출력 포맷: 섹션 태그, 라인 수, 훅/벌스 분리, 메타 블록
  - 금지 규칙: 클리셰/반복 패턴/형식 위반
  - 실패 처리: 재시도 조건, USER_DECISION 승격 조건

3. 하네스 게이트 구현 설계 반영
- 대상 파일:
  - `wavvy_harness/gate.py`
  - `wavvy_harness/state.py`
  - `tests/test_harness.py`
- 변경 방향:
  - `lyrics_skill` 관련 gate stage 추가
  - 판정 enum 표준화: `PASS | FAIL | USER_DECISION`
  - 실패 사유 코드화(`FORMAT`, `CONCEPT_MISMATCH`, `PROHIBITED_PATTERN`, `REPETITION`)
  - 상태 기록에 `evidence_refs`(리서치 출처 경로) 필드 추가

4. CLI 연결
- 대상 파일:
  - `wavvy.py`
- 변경 방향:
  - `lyrics-skill` 또는 동등한 서브커맨드 추가(스펙 검증 + 샘플 실행)
  - `--series 17-00 --track 01` 기준 드라이런 지원
  - 결과를 `.ai/pipeline/runs/.../artifacts/`에 기록

5. 문서/SSOT 동기화
- 대상 파일:
  - `MASTER/SSOT.md`
  - `wavvy.md`
  - `CHANGELOG.md`
  - `.ai/SESSION.md`, `.ai/HANDOFF.md` (필요 시)
- 변경 방향:
  - 새 스킬/게이트의 SSOT 위치 명시
  - 운영 절차(실행→검증→기록) 추가
  - 변경 근거(run id, research source) 추적 링크 추가

## 4) 구현 순서 (Sequencing)
1. 리서치/기준선 확정 (`lyrics-skill-baseline.md`)
2. 스킬 계약 명세 작성 (`WAVVY_LYRIC_SKILL_SPEC.md`)
3. 하네스 게이트 로직 반영 (`gate.py`, `state.py`)
4. 테스트 반영 (`tests/test_harness.py`)
5. CLI 엔트리 연결 (`wavvy.py`)
6. SSOT/운영문서 동기화 (`MASTER/SSOT.md`, `wavvy.md`, `CHANGELOG.md`)
7. 전체 검증 실행 및 gate-status 기록

## 5) 검증 계획 (Verification)
- 정적/기본 검증:
  - `python3 -m py_compile wavvy.py wavvy_harness/*.py`
- 테스트:
  - `python3 -m unittest tests/test_harness.py`
- 하네스/상태:
  - `python3 wavvy.py doctor --json`
  - `python3 wavvy.py state SERIES/17-00 --check --json`
- 게이트:
  - `python3 wavvy.py validate SERIES/17-00`
  - `python3 wavvy.py gate SERIES/17-00 --stage uploaded --json`
- 워크트리 위생:
  - `git diff --check`

## 6) 수용 게이트 (Acceptance Gates)
- Gate A: 리서치 정합
  - prior research run과 LYRICS v4.2를 모두 인용한 기준선 문서 존재
- Gate B: 스킬 계약 완전성
  - 입력/출력/금지/실패처리 항목 4종 모두 정의
- Gate C: 하네스 판정 자동화
  - 최소 1회 자동 자기검수 루프 + `PASS/FAIL/USER_DECISION` 판정 가능
- Gate D: 품질 기준 충족 (17-00 Track 01 기준)
  - 포맷 위반 0건
  - 금지 패턴 검출 0건
  - 컨셉 정합 판정 PASS
  - 반복/진부성 점수 임계치 이내(문서화된 threshold 적용)
- Gate E: 운영 추적성
  - 변경 근거(run id, source path, gate result) 문서/상태에 남음

## 7) 롤백 계획 (Rollback)
- 코드 롤백 단위:
  - 1순위: 하네스 로직(`wavvy_harness/*`)과 CLI(`wavvy.py`)를 기능 플래그 또는 stage 분기로 비활성화
  - 2순위: 스킬 스펙 문서는 유지하되 실행 경로만 차단
- 데이터/문서 롤백:
  - `.ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/` 내 산출물은 기록 보존
  - SSOT 반영 전 실패 시 `MASTER/SSOT.md` 변경만 되돌리고 실험 산출물은 유지
- 중단 조건:
  - 동일 high-severity 실패 2회 연속
  - `USER_DECISION` 필요 이슈 발생 시 자동 진행 중단

## 8) 리스크 및 대응
- 리스크: 리서치-스펙 불일치
  - 대응: 스펙 각 규칙에 출처 경로(`evidence_refs`) 강제
- 리스크: 게이트 과적합으로 창의성 저하
  - 대응: hard gate(형식/금지)와 soft score(창의성) 분리
- 리스크: 기존 미커밋 변경과 충돌
  - 대응: 파일 소유 경계 명확화, 변경 범위 최소화, 단계별 diff 리뷰

## 9) Image Generation Routing Gate
- 본 계획의 1차 범위(작사 스킬/하네스)에서는 이미지 생성이 **필수 아님**.
- 향후 시각 산출물이 포함될 경우 적용:
  - 일반 원오프 시각물: Codex 기본 `image_gen`
  - 아래 조건 중 하나라도 필요하면 `gpt-image-2`:
    - GPT Image 2/gen2 지정 요구
    - 모델 근거/재현성 요구
    - 배치 생성
    - manifest/hash/request-id 기록
    - 납품/클라이언트 리뷰 패키징
  - 투명 PNG/알파 요구 시:
    - 출력 직후 알파 채널 존재/가장자리 halo/배경 잔존 여부를 별도 후처리 검증 게이트로 확인

## 10) 완료 정의
- `SERIES/17-00` 대상 드라이런에서 수용 게이트 A~E 전부 PASS
- 스킬 스펙/하네스/CLI/SSOT가 상호 참조 가능한 상태
- run 산출물에 검증 로그와 판정 결과가 재현 가능하게 보존됨

## Context

### Git Status

```
 M .ai/HANDOFF.md
 M .ai/SESSION.md
 M CHANGELOG.md
 M MASTER/SSOT.md
 M MASTER/lyrics/LYRICS.md
 M SERIES/RNB-BEST/concept.md
 M tests/test_harness.py
 M wavvy.md
 M wavvy.py
 M wavvy_harness/gate.py
 M wavvy_harness/state.py
?? .ai/auto-handoff/
?? .ai/codex-hyphen-trigger-guard.json
?? .ai/logs/
?? .ai/peer-review/runs/20260521-233758-claude-review-63703.md
?? .ai/peer-review/runs/20260521-234050-claude-plan-64928.md
?? .ai/peer-review/runs/20260521-234211-claude-plan-65786.md
?? .ai/peer-review/runs/20260522-002228-claude-plan-71120.md
?? .ai/peer-review/runs/20260522-002657-claude-plan-75212.md
?? .ai/peer-review/runs/20260522-003643-claude-plan-77038.md
?? .ai/peer-review/runs/20260522-004636-claude-plan-82294.md
?? .ai/peer-review/runs/20260522-011806-claude-review-91813.md
?? .ai/peer-review/runs/20260522-012900-claude-review-94361.md
?? .ai/peer-review/runs/20260522-013501-claude-review-98882.md
?? .ai/peer-review/runs/20260522-095103-claude-review-11355.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/
?? .ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/
?? SERIES/17-00/
```

### Diff Stat

```
 .ai/HANDOFF.md             |  14 ++++
 .ai/SESSION.md             |  30 ++++++++-
 CHANGELOG.md               |   4 ++
 MASTER/SSOT.md             |   2 +
 MASTER/lyrics/LYRICS.md    |   9 +++
 SERIES/RNB-BEST/concept.md |  11 ++--
 tests/test_harness.py      |  81 ++++++++++++++++++++++-
 wavvy.md                   |  12 +++-
 wavvy.py                   | 160 ++++++++++++++++++++++++++++++++++++++++-----
 wavvy_harness/gate.py      |  15 ++++-
 wavvy_harness/state.py     |  88 +++++++++++++++++++++++--
 11 files changed, 391 insertions(+), 35 deletions(-)
```

## Peer Result

### Peer Review Verdict

**Result: PASS** | **Confidence: high**

The plan is well-structured and technically feasible. All referenced artifacts (prior research, LYRICS v4.2, 17-00 series, gate-status) verified as existing. Key findings:

| Severity | Issue | Action |
|---|---|---|
| Medium | Gate naming (`lyrics_skill`) doesn't match existing phase-gate convention (`source-final`, etc.) | Decide: independent checkpoint (`lyrics-review`) vs. phase gate. Document in spec. |
| Medium | Prior research is Track-01-scoped only, not series-wide | Add "generalization scope" section in baseline doc |
| Medium | `MASTER/lyrics/skills/` is greenfield (doesn't exist yet) | Create and register in SSOT during implementation |
| Low | `evidence_refs` field schema undefined | Define as list of URI-fragment strings |
| Low | 17-00 has no `LYRICS_DNA.md` | Spec should define concept.md as fallback DNA source |
| Low | Verification uses `--stage uploaded` which is wrong for 17-00 | Use `source-final` or new lyrics stage instead |

No blocking issues. Proceed to implementation.

