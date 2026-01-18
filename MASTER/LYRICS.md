# VIBE-M LYRICS.md
Version: 1.0 (Single Source of Truth)
Last Updated: 2026-01-18
Purpose: Enforce lyrical consistency, musicality, and AI-safe input

---

## 🎯 0. LYRICS.md의 존재 이유

VIBE-M에서 가사는 "감정 표현"이 아니라 **음악을 안정적으로 생성하기 위한 설계 데이터**다.

이 문서의 목표는 다음 3가지를 동시에 만족시키는 것이다.

1. Suno가 멜로디를 **안정적으로 복제/변주**하게 만든다.
2. 인간 리스너에게 **자연스럽고 트렌디한 감정선**을 전달한다.
3. 알고리즘이 **양산형/중복 콘텐츠**로 오인하지 않게 한다.

---

## 🧠 1. Core Lyrical Engineering Rules (절대 규칙)

### 1.1 Metric Mirroring (V1–V2 대칭)

- Verse 1과 Verse 2는:
  - **음절 수**
  - **행 수**
  - **문장 구조**
를 완전히 동일하게 유지한다.

목적:
- Suno가 Verse 1의 멜로디 컨투어를 Verse 2에 그대로 복제하게 유도
- 감정만 고조되고 멜로디는 흔들리지 않게 만들기 위함

---

### 1.2 Rhyme / Ending Mirroring (종지감 통일)

- V1과 V2 각 행의 끝 단어는 다음을 일치시킨다.
  - 품사 (형용사 / 명사 / 동사)
  - 어미 패턴
  - 종지감 길이

예시:
- `차가워 (adj)` → `따가워 (adj)`
- `얼굴들 (noun)` → `흔적들 (noun)`

목적:
- 멜로디 끝 처리(ending note)가 동일하게 재현되도록 강제

---

### 1.3 Chorus Static Rule (후렴 고정)

- 후렴 가사는:
  - **전 구간 100% 동일**
  - 3~4행
  - 각 행 6~10음절 권장

Chorus 2, Chorus 3에서도:
- 가사는 절대 바꾸지 않는다.
- 감정 증폭은 **사운드와 보컬 레이어**로만 처리한다.

---

### 1.4 Bridge Anchor Rule (테제 + 장면)

Bridge는 반드시 아래 구조를 따른다.

- Thesis (고정 1라인)
  - 곡의 철학적 중심 문장
  - 보통 마지막 행
- Scene (2~3라인)
  - 설명 ❌
  - 감정 설명 ❌
  - **구체적인 동작 / 감각 / 이미지**만 허용

추가 규칙:
- Bridge 1과 Bridge 2는
  - Thesis는 동일
  - Scene 라인은 최소 2행 이상 변주

---

## 🧼 2. Pure Lyric Input Rule (입력 무결성)

### 2.1 절대 금지 사항

Suno 가사 입력란에 다음을 **절대 넣지 않는다**.

- 영어 설명 문장
- 괄호 속 지시어 `( )`
- Scene 설명
- 보컬/악기/연출 지시
- 감정 메타 코멘트

이 모든 것은 STYLE.md로 이동한다.

---

### 2.2 허용되는 태그

가사 입력에서 허용되는 태그는 아래만 가능하다.

- `[intro]`
- `[verse]`, `[verse1]`, `[verse2]`
- `[bridge]`, `[bridge1]`, `[bridge2]`
- `[chorus]`
- `[instrumental]`
- `[outro]`

그 외 커스텀 태그 사용 금지.

---

## 🚫 3. Failure Case Archive (대표적인 실패 유형)

### Case 01: Metric 붕괴
- Verse 2에서 음절 수 증가/감소
- 결과: 멜로디 붕괴, AI 즉흥 변주 발생

### Case 02: Ending 불일치
- V1은 명사, V2는 의문문
- 결과: 후반 멜로디가 다른 곡처럼 들림

### Case 03: Bridge 설명조
- "~한 마음", "~한 감정"
- 결과: AI 특유의 내레이션 톤 발생

### Case 04: Meta Instruction Hallucination
- `(Scene: Wet breath)` 같은 문구 삽입
- 결과: 보컬이 이를 가사처럼 읽어버림

---

## 🧩 4. Canonical Structure (표준 구조)

모든 VIBE-M 트랙은 아래 구조를 기본으로 한다.

[intro]
[verse1]
[bridge1]
[chorus]
[verse2]
[bridge2]
[chorus]
[chorus]
[outro]

---

## 🗂️ 5. Reference Example (Clean Input Sample)

```text
[intro]
[instrumental]

[verse1]
손끝이 차가워
김이 서린 유리
뿌옇게 가려진
어제의 얼굴들

[bridge1]
마른 천을 쥐고서
지우려는 손끝이
도리어 번져가는
얼룩진 마음의 흔적

[chorus]
잊혀지는 것들은
소리도 없이 투명해
흐려진 궤적 끝에
잡히지 않는 너

[verse2]
눈끝이 따가워
나의 작은 숨이
여전히 남겨진
추억의 흔적들

[bridge2]
젖은 숨을 삼키고
다시 문지른 손끝
더 선명해져버린
얼룩진 마음의 흔적
```
