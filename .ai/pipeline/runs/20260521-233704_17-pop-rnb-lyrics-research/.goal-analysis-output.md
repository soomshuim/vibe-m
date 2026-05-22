# Team Analysis

## Problem
2026년 기준 스트리밍 인기곡의 **가사 서술 방식/어휘/주제 처리 패턴**을 참고해 `SERIES/17-00/input/tracks/01_올라가 (Up Again).txt`를 재작성해야 한다. 단, **저작권 가사 직접 복사/패러프레이즈 복제는 금지**이며 스타일 신호만 추출해야 한다.  
요청 텍스트에 `-research -play`가 포함되어 있지만, 본 단계는 상위 run 내부의 **bounded artifact 작성 단계**이므로 실행 트리거로 취급하지 않는다.

## Current State
- 대상 트랙은 이미 `17:00 POP R&B` 콘셉트(124 BPM, D Major, 밝은 메이저 톤, 반복 훅 “올라가”)에 맞춘 샘플 가사가 존재한다.
- 현재 파이프라인의 `02-review.md`, `03-plan.md`는 placeholder 상태라 분석 기준을 명시적으로 보강할 필요가 있다.
- 세션 시작 필수 체크 결과:
  - Claude activity check 실행 완료
  - auto-handoff pending-clear: `none`
  - context-guard: `remaining 27%`, `below_threshold=false`
  - hyphen-trigger-guard: `action=none` (bounded stage prompt로 인식)

## Options
1. **최소 수정 옵션**  
   기존 가사 구조 유지, 일부 단어만 2026 트렌드 어휘로 교체.  
   장점: 빠름. 단점: 트렌드 반영 깊이 낮고 차별성 부족.

2. **패턴 기반 재작성 옵션 (권장)**  
   인기곡 코퍼스에서 “서술 관점/라인 길이/훅 반복 방식/감정 전개/어휘군”만 추출해 새 가사를 전면 재작성.  
   장점: 저작권 리스크를 낮추면서 현대성 확보. 단점: 리서치/검증 단계 필요.

3. **완전 신규 콘셉트 옵션**  
   17:00 DNA는 유지하되 가사 주제 자체를 새로 설계.  
   장점: 독창성 높음. 단점: 기존 시리즈 톤과 어긋날 가능성.

## Recommendation
옵션 2 채택.  
“복사 금지 + 스타일 참조” 조건과 시리즈 일관성을 동시에 만족한다. 산출물은 다음 3단 분리로 만든다.
- **Research Note**: 인기곡 가사에서 비저작권 패턴만 요약
- **Lexicon Pack**: 금지어/권장어/클리셰 회피 리스트
- **Rewrite Draft**: `올라가` 훅 중심의 신규 가사

## Scope
- 포함:
  - 2026 트렌드 기준의 가사 패턴 요약(직접 인용 없음)
  - `01_올라가 (Up Again).txt` 가사 재작성 방향 정의
  - POP R&B 17:00 게이트(BPM/Key/Mood/Hook) 정합성 유지
- 제외:
  - 실제 오디오 생성/믹스/마스터링
  - peer review 실행
  - trigger 기반 자율 러너 실행(`-research`, `-play`, `play.sh start`, `goal-run` 등)

## Risks
- **저작권 리스크**: 특정 히트곡 문장 구조를 과도하게 근접 모사할 위험
- **톤 이탈 리스크**: 트렌드 반영 과정에서 17:00 밝은 메이저 감성이 약화될 위험
- **과잉 일반화 리스크**: “인기곡 스타일”을 너무 넓게 잡아 훅 선명도가 떨어질 위험

## Gates
1. **Copyright Safety Gate**  
   외부 가사 원문/근접 패러프레이즈 0건, 인용 대신 패턴/어휘군만 사용.
2. **Series DNA Gate**  
   밝은 메이저 무드, `올라가` 훅 기억성, Main POP R&B 톤 유지.
3. **Lyric Quality Gate**  
   한글 발음 흐름, 훅 반복 밀도, verse-pre-chorus-chorus 대비 명확.
4. **Documentation Gate**  
   리서치 근거는 “원문 복사 없는 추상화 메모”로 남기고 출처 유형(플랫폼/차트군)만 기록.

## Harness Policy Note (Design/Image 관련 요청 발생 시)
- 일반 스케치/원오프 비주얼: Codex `image_gen` 기본 경로
- `gpt-image-2`(gen2) 명시 요구, 모델 증빙, 반복성, 배치 생성, manifest/hash/request-id, 납품/클라이언트 리뷰 요구: **OpenAI Images API (`gpt-image-2`) 경로로 라우팅**
- 투명 PNG/알파 필요 시: `gpt-image-2`가 직접 투명을 보장한다고 가정하지 말고 **별도 후처리 게이트** 추가