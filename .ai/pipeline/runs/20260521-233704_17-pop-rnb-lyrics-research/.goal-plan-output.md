# 03-plan — 17-00 Track 01 가사 리서치 기반 재작성 구현 계획

## 0) Session Start Check (필수)
- Claude activity check: 실행 완료 (`bash $HOME/.codex/scripts/check-claude-activity.sh`)
- Auto-handoff pending-clear: `action=none`, `clear_required=false`
- Context guard: `remaining_pct=26`, `below_threshold=false`
- Hyphen-trigger guard: `action=none` (`internal_bounded_stage_prompt`)
- 해석: 본 작업은 상위 play run 내부 bounded artifact 작성으로 진행하며, `-research -play`는 실행 트리거로 소비하지 않음.

## 1) 목표
- `SERIES/17-00/input/tracks/01_올라가 (Up Again).txt`를 2026 인기곡 스타일 신호(서술 방식/어휘군/주제 처리) 기반으로 재작성한다.
- 저작권 보호 원칙 준수: 외부 가사 원문/근접 패러프레이즈/고유 문장 리듬 복제 금지.
- 17:00 시리즈 DNA 및 Wavvy 작사 철학(사물·공간·현상 중심)을 유지한다.

## 2) 적용 범위/비범위
- 포함:
  - 비저작권 패턴 리서치 요약
  - Lexicon pack(권장어/금지어/클리셰 회피어) 정의
  - Track 01 가사 본문 재작성
  - 게이트 검증 및 기록
- 제외:
  - 오디오 생성/믹스/마스터
  - 자동 러너/추가 트리거 실행
  - 다른 트랙 동시 수정

## 3) 참조 파일 (읽기 우선순위)
1. `MASTER/SSOT.md` (충돌 시 최종 기준)
2. `MASTER/lyrics/LYRICS.md` (§0 작사 원칙, §0.1 Time Concept vs Lyrics, §1~2 Suno 입력 규칙)
3. `SERIES/17-00/concept.md` (BPM/Key/Mood/Hook/EXCLUDE)
4. `SERIES/17-00/input/tracks/01_올라가 (Up Again).txt` (현행 베이스라인)
5. `.ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/01-team-analysis.md`
6. `.ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/02-review.md` (peer finding 반영)

## 4) 구현 순서 (Sequencing)
1. **Constraint Freeze**
- 시리즈 하드 제약 확정: `120+ BPM`, `Major`, 밝은 상승감, 메인 훅 `올라가`.
- 금지 영역 명시: 직접 시간개념 강요 가사, 노골적 감정 선언(예: 사랑해/슬퍼 반복), 저작권 고위험 표현.

2. **Research Pattern Extraction (원문 비보관)**
- 인기곡 원문을 저장/인용하지 않고 아래 5개 차원만 추출:
  - 라인 길이/음절 밀도 범위
  - Hook 반복 주기/변형 방식
  - 화자 시점 분포(1인칭/2인칭/무인칭)
  - 감정 전개 곡선(Verse→Pre→Chorus)
  - 어휘 레지스터(일상어/이미지어/슬랭 비율)
- 결과를 추상 메모로만 정리(출처는 플랫폼/차트군 레벨만 기록).

3. **Lexicon Pack 설계**
- 권장어: 상승/빛/공간/움직임 중심 이미지어.
- 회피어: 특정 히트곡 연상 강한 문구, 과도한 클리셰, 직접 감정 진술.
- 형식 제약: Suno 입력 호환(약어/브래킷 규칙, 길이 제한 고려).

4. **Draft Rewrite**
- 구조: Verse 1 → Pre → Chorus → Verse 2 → Pre → Chorus → Bridge → Final Chorus.
- `올라가` 훅 반복은 유지하되 문맥 변주를 통해 기억성 강화.
- LYRICS 철학 반영: 사물·공간·현상 묘사 우선, 감정은 간접 표출.

5. **Self-Check + Gate Pass**
- Copyright, Series DNA, Lyric Quality, Documentation 게이트 검사.
- 실패 항목 발생 시 해당 섹션만 부분 재작성 후 재검증.

## 5) 검증 계획 (Verification)
- 문서/정합성 검증:
  - `MASTER/lyrics/LYRICS.md` 기준 체크리스트 수동 대조
  - `SERIES/17-00/concept.md` EXCLUDE 위반 여부 점검
- 텍스트 품질 검증:
  - 훅 밀도(코러스 내 핵심 반복 존재)
  - 구간 대비(Verse/Pre/Chorus 기능 분리)
  - 발화 자연성(한국어 리듬/호흡 단위)
- 저작권 안전 검증:
  - 외부 가사 문장 직접 인용 0
  - 근접 문장 패턴(연속 핵심어/리듬) 재검토
  - 리서치 노트에 원문 비포함 확인

## 6) 롤백 계획 (Rollback)
- 단일 파일 변경 기준:
  - 재작성본이 게이트 실패 시 즉시 직전 원본(`01_올라가 (Up Again).txt`)로 복귀
  - 복귀 후 실패 원인(게이트 항목)만 수정한 최소 diff 전략 적용
- 정책 충돌 시:
  - `MASTER/SSOT.md` 우선
  - 미해결 시 본 run 산출물 내 decision note로 보류 표시 후 확정 전 반영 중지

## 7) Acceptance Gates
1. **Copyright Safety Gate (필수)**
- 외부 가사 원문/근접 패러프레이즈 0건
- 직접 인용 대신 패턴/어휘군 추상화만 사용

2. **Series DNA Gate (필수)**
- 17:00 POP R&B 정체성 유지(밝은 Major/상승감/훅 중심)
- `LYRICS.md §0.1` 준수: 시간 컨셉 직설 가사화 금지

3. **Lyric Philosophy & Quality Gate (필수)**
- `LYRICS.md §0` 준수: 사물·공간·현상 중심 묘사
- Verse/Pre/Chorus 대비 명확, 훅 기억성 확보, 발화 흐름 자연

4. **Format & Runtime Gate (필수)**
- `LYRICS.md §1~2` Suno 입력 규칙(약어/브래킷/길이) 준수

5. **Documentation Gate (필수)**
- 리서치 근거는 “원문 없는 추상 메모”로 기록
- 출처는 플랫폼/차트군 단위만 남김

## 8) Image Generation Routing Gate (정책 포함)
- 본 작업은 가사 재작성 중심으로 이미지 생성이 기본적으로 **N/A**.
- 단, 후속으로 비주얼 산출이 필요해질 경우:
  - 일반 원오프 비주얼: Codex 내장 `image_gen` 기본 사용
  - `gpt-image-2/gen2` 명시 요구 또는 모델 증빙/반복성/배치/manifest(hash, request-id)/납품·클라이언트 리뷰 요구 시: OpenAI Images API `gpt-image-2` 경로 사용
  - 투명 PNG/알파 요구 시: 생성 후 알파 채널 존재/배경 누수 여부를 별도 후처리 검증 게이트로 통과해야 승인

## 9) 완료 정의 (Done)
- 대상 파일 재작성본이 5개 Acceptance Gate 전부 통과
- 저작권 리스크 없는 추상 리서치 근거와 어휘 전략이 재현 가능 형태로 정리
- 시리즈 톤(17:00)과 Wavvy 작사 철학을 동시에 충족하는 최종 텍스트 확보