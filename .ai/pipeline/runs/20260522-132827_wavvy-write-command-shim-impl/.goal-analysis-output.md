## Startup Check
- Claude activity check 실행 완료 (`bash $HOME/.codex/scripts/check-claude-activity.sh`, 2026-05-22 13:28 KST).
- Pending clear sentinel 확인: `action: none`.
- Hyphen trigger guard 확인: `action: none` (`reason: internal_bounded_stage_prompt`).

## Problem
- 사용자 확인 문구(`연결해줘`) 이후에도 Wavvy 로컬에서 `/write`(Claude)와 `-write`(Codex)가 일관되게 lyric 전용 경로로 해석되지 않으면, 기존 lyricist skill/spec/CLI 하네스를 우회하거나 중복 규칙이 생길 위험이 있다.
- 목표는 “새 작사 시스템 구축”이 아니라 “기존 SSOT로 얇게 라우팅되는 커맨드 shim 연결”이다.

## Current State
- 이미 lyric SSOT와 실행 하네스가 존재:
  - `skills/wavvy-lyricist/SKILL.md`
  - `skills/wavvy-lyricist/references/patterns.md`
  - `MASTER/lyrics/skills/WAVVY_LYRIC_SKILL_SPEC.md`
  - `python3 wavvy.py lyrics-skill SERIES/[series] --json`
  - `python3 wavvy.py gate SERIES/[series] --stage lyrics-review --json`
- `.ai/SESSION.md`에 “사용자가 연결 확정 시 `/write`, `-write` shim 구현”이 남은 TODO로 명시됨.
- 트리거 정책상 Codex는 hyphen trigger 중심, Claude는 command 문서 기반 해석이므로 양쪽 진입점 최소 파일 구성이 필요함.

## Options
1. 단일 진입점만 추가 (예: `-write`만)
- 장점: 변경 최소.
- 단점: 도구별 UX 불일치, 세션/에이전트 혼용 시 혼란.

2. `/write`와 `-write`를 각각 독립 구현(규칙 내장)
- 장점: 각 도구 즉시 독립 동작.
- 단점: 규칙 중복/드리프트 위험, SSOT 위반 가능성 큼.

3. `/write`와 `-write`를 “thin shim”으로 추가하고 기존 lyricist skill/spec/CLI로만 라우팅
- 장점: 중복 최소, 유지보수 용이, 현재 정책과 가장 정합.
- 단점: 초기 라우팅 문구/가드 문구 설계가 필요.

## Recommendation
- 옵션 3 채택.
- 구현 원칙:
  - 커맨드 본문에는 작사 규칙/루브릭 복사 금지.
  - lyric 작성/리라이트/리뷰 요청만 허용하고 비가사 요청은 명시적으로 리다이렉트.
  - 실제 품질 검증은 기존 `wavvy.py lyrics-skill` + `lyrics-review gate`를 사용.
- 결과적으로 `/write`, `-write`는 “라우터”이고, “정책/검증 엔진”은 기존 SSOT가 담당한다.

## Scope
- 포함:
  - Wavvy-local `/write` command shim (Claude용).
  - Wavvy-local `-write` 해석 경로(Codex용) 보장에 필요한 최소 command/skill 파일.
  - lyric 작성/리라이트/리뷰 라우팅 문구와 비범위 요청 차단 문구.
- 제외:
  - YouTube 카피, concept 문서 편집, changelog 작성, 일반 문서 작성 라우팅.
  - lyric 규칙 본문 신규 작성/복제.
  - peer review 자동 루프 실행.

## Risks
- 라우팅 과다 확장: `/write`가 비가사 작업까지 흡수할 위험.
- 규칙 중복: command 파일에 lyric 정책을 복붙해 SSOT 분리 붕괴.
- 트리거 불일치: Claude/Codex 중 한쪽만 로컬 해석되어 운영 혼선 발생.
- 검증 누락: shim은 연결됐지만 하네스 체크가 빠져 실제 사용 시 회귀 가능.

## Gates
- 발견/해석 게이트:
  - `/write`, `-write`가 Wavvy 로컬 우선 경로로 탐지되는지 확인.
- 정합 게이트:
  - command 텍스트가 thin routing만 포함하고 lyric 규칙을 중복하지 않는지 확인.
- 하네스 게이트(변경 영향 시):
  - `python3 wavvy.py lyrics-skill SERIES/[series] --json`
  - `python3 wavvy.py gate SERIES/[series] --stage lyrics-review --json`
- 기본 위생 게이트:
  - `git diff --check`
- 문서 게이트:
  - durable 상태 변경이 실제로 생긴 경우에만 `.ai/SESSION.md`/`CHANGELOG.md` 갱신.

## Image/Design Harness Policy
- 본 요청은 디자인/이미지 생성 범위가 아니므로 실행 대상은 아님.
- 단, 추후 `/write` 흐름이 이미지 산출을 포함할 경우:
  - 일반 스케치/1회성 비주얼: `image_gen` 기본.
  - `gpt-image-2` 명시 요구(모델 증빙, 반복성, 배치, manifest/hash/request-id, 납품/리뷰): OpenAI Images API 경로 강제.
  - 투명 PNG/alpha 요구: `gpt-image-2`의 직접 투명 배경을 가정하지 않고 별도 후처리 게이트 추가.