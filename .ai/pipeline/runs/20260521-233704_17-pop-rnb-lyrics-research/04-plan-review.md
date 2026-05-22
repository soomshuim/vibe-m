# Peer Agent Review

| Field | Value |
|---|---|
| Target | claude |
| Mode | plan |
| Project | wavvy |
| Repo | /Users/zenkim_office/Project/wavvy |
| Git repo | yes |
| Branch | master |
| Created | 2026-05-21 23:42:10 KST |
| Exit code | 0 |
| Timeout seconds | 2700 |
| Attempts | 1 |

## Request

Play run: /Users/zenkim_office/Project/wavvy/.ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research
Review the implementation plan artifact for this play harness run.
Source artifact: /Users/zenkim_office/Project/wavvy/.ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/03-plan.md

Original request:
2026년 기준 음악 스트리밍 사이트 인기곡 가사를 리서치해보고, 가사 서술 방식과 사용 단어를 참조해서 17-00 샘플 곡 가사를 다시 만들어줘. 저작권 가사는 직접 복사하지 말고 서술 방식, 단어장, 주제 처리 방식만 요약 참조. 대상 파일: SERIES/17-00/input/tracks/01_올라가 (Up Again).txt. 트리거: -research -play

Proposal-only run: false

## Artifact Content

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

## Context

### Git Status

```
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
?? .ai/codex-hyphen-trigger-guard.json
?? .ai/peer-review/runs/20260521-233758-claude-review-63703.md
?? .ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/
?? SERIES/17-00/
```

### Diff Stat

```
 .ai/SESSION.md             |  20 +++++-
 CHANGELOG.md               |   4 ++
 MASTER/SSOT.md             |   2 +
 MASTER/lyrics/LYRICS.md    |   9 +++
 SERIES/RNB-BEST/concept.md |  11 ++--
 tests/test_harness.py      |  81 ++++++++++++++++++++++-
 wavvy.md                   |  12 +++-
 wavvy.py                   | 160 ++++++++++++++++++++++++++++++++++++++++-----
 wavvy_harness/gate.py      |  15 ++++-
 wavvy_harness/state.py     |  88 +++++++++++++++++++++++--
 10 files changed, 367 insertions(+), 35 deletions(-)
```

## Peer Result

Now I have full context. Let me write the plan review.

---

### Peer Review Verdict
- Result: **PASS**
- Confidence: **high**

### Findings

| Severity | File/Area | Issue | Recommendation |
|---|---|---|---|
| Medium | §4 Step 2 | **Research data access method unspecified.** The plan says "인기곡 원문을 저장/인용하지 않고" 5 dimensions to extract, but doesn't specify how the agent will obtain 2026 streaming chart lyric pattern data. Web search? LLM knowledge? The feasibility of pattern extraction depends on the data source, and different sources have different copyright risk profiles. | Add a 1-line note specifying the research approach (e.g., web search for chart metadata + LLM knowledge of lyric patterns, or Wavvy's own existing track analysis as baseline). This affects both feasibility and copyright safety gate reliability. |
| Medium | §4 Step 4 / §7 Gate 4 | **Suno lyric mode not specified.** The current Track 01 uses full lyrics with `[Intro]`/`[Verse 1]`/`[Chorus]`/`[Outro]` section tags (Structure mode per LYRICS.md §1.1). The plan prescribes a structure `V1→Pre→C→V2→Pre→C→Bridge→Final Chorus` but doesn't state whether the output is a full lyric text or a Suno prompt-mode hint. Gate 4 cites "LYRICS.md §1~2" but the mode choice affects the entire output format. | Specify explicitly: rewrite will produce full lyrics with section tags (matching the current Track 01 format), not a prompt-mode 1-3 line hint. |
| Low | §0 | **Context budget at 26%.** The plan notes `remaining_pct=26, below_threshold=false` but doesn't acknowledge that the research + lexicon + rewrite + self-check sequence may be context-intensive. If context drops below 40% during implementation, the context-guard auto-handoff rule activates. | Note that implementation should be chunked efficiently and that a context checkpoint after Step 2 (research) may be prudent before starting the writing-heavy Steps 3-4. |
| Low | §3 ref #4 | **Existing Track 01 quality baseline not explicitly preserved.** The 02-review PASS noted: "The existing Track 01 lyrics are well-crafted and already follow Wavvy philosophy — the rewrite should treat them as a quality baseline, not start from zero." The plan lists the file as reference #4 but doesn't codify that the rewrite must meet or exceed the current lyric quality. | Add a note to Gate 3 or §4 Step 4: the rewrite must demonstrate improvement over the existing lyrics in trend alignment while maintaining at least equivalent quality in Wavvy philosophy adherence and hook memorability. |
| Low | §8 | **Irrelevant Image Generation boilerplate.** The 02-review flagged this as noise. The plan marks it N/A but still occupies ~5 lines. | Remove entirely or collapse to a single "N/A — no image generation in scope" line. Not harmful, just clutter. |

### Test And Acceptance Notes

- **Verified**: Plan §3 reference files are all confirmed to exist and contain the content the plan expects.
  - `MASTER/SSOT.md` — conflict order table present, compilation source map policy present
  - `MASTER/lyrics/LYRICS.md` — §0 lyric philosophy, §0.1 Time Concept vs Lyrics, §1-2 Suno rules all present and consistent with plan references
  - `SERIES/17-00/concept.md` — 120+ BPM, Major key, bright mood hard gates confirmed at lines 38-44
  - `01_올라가 (Up Again).txt` — 119 lines, full lyrics with section tags, STYLE/EXCLUDE/LYRICS/META structure confirmed
- **Verified**: Plan incorporates 02-review Medium findings:
  - Wavvy lyric philosophy (사물·공간·현상) → added as explicit Gate 3 criterion
  - Concrete pattern dimensions → Step 2 enumerates 5 specific dimensions (line length/syllable density, hook repetition, POV distribution, emotional arc, vocabulary register)
- **Verified**: Plan's 5 acceptance gates cover all critical constraints: copyright safety, series DNA, lyric philosophy+quality, Suno format, documentation.
- **Verified**: Rollback plan is sound — single file target, immediate revert to existing baseline on gate failure.
- **Verified**: EXCLUDE list in Track 01 already includes `direct time concept` which aligns with LYRICS.md §0.1 and plan Gate 2.
- **Not yet runnable**: No automated test exists for lyric quality/copyright gates — these are manual review checks as expected for creative content.

### Follow-Up For Requesting Agent

1. **PASS — proceed to implementation.** The plan is well-structured and incorporates prior review findings.
2. Address the two **Medium** findings before or during implementation:
   - Specify the research data source (web search vs. LLM knowledge vs. project-internal analysis).
   - Confirm the output format is full lyrics with section tags (not prompt-mode).
3. The **Low** findings are advisory and can be addressed during implementation without blocking.
4. Given 26% context remaining, consider a lean implementation strategy: combine the research note and lexicon pack into a single concise artifact rather than two separate documents, to conserve context for the actual lyric writing.

