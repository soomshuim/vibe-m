# Korean Indie Pop + Dream Pop Rubric

Version: 1.0
Last Updated: 2026-04-04
Purpose: Korean Indie Pop + Dream Pop 장르 게이트 (13-00 시리즈)

> Based on: `report/2026-04-04_indie-pop-dream-pop-genre-research.md`
> Evidence: Wikipedia, AllMusic, Pond5, Reverb Machine, HookGenius, SongBPM, Korea Herald

---

## Evidence Basis

### 1. Indie Pop vs Dream Pop 핵심 차이

| 항목 | Indie Pop | Dream Pop |
|------|-----------|-----------|
| 우선순위 | 캐치한 멜로디, 훅 | 분위기, 텍스처, 사운드스케이프 |
| 보컬 | 전면, 선명, conversational | 묻힘, ethereal, 악기처럼 기능 |
| 기타 | 잔글링, 클린톤 | 시머링, reverb-drenched |
| 이펙트 | 절제, dry~moderate | 대량 reverb/delay/chorus |
| 곡 구조 | 명확한 V-PC-C-B | 경계 흐릿, 흘러가는 |
| BPM | 90-130 (중심 100-120) | 80-100 (중심 85-95) |
| 13-00 적합도 | **메인 베이스** | **혼합 요소** |

### 2. 한국 인디팝 고유 특성

- 서양 대비 더 폴리시된 프로덕션 (깔끔한 믹싱, 보컬 전면)
- 어쿠스틱/일렉기타 기반 + 피아노 레이어
- Breathy + 내추럴 보컬 톤, 감정의 미세한 변화
- BPM 100-130, Major key 우세

### 3. 13-00 혼합 공식

**Korean Indie Pop (베이스)** + **Dream Pop (질감)**
= 한국 인디팝의 선명한 멜로디/보컬 + Dream Pop의 리버브/패드 질감

---

## Hard Gates (1개라도 FAIL = 재작성)

| # | Gate | 기준 |
|---|------|------|
| H1 | BPM | 90-118 범위 |
| H2 | Melody | 캐치한 멜로디 훅 존재 (인식 가능, 반복 시 각인) |
| H3 | Guitar | 잔글링 또는 시머링 기타 존재 (클린톤 기반) |
| H4 | Vocal | 한국어 보컬 + 단독 리드 (Harmony Guard) |
| H5 | Tone | 밝고 따뜻한 톤 (dark/aggressive/gritty 없음) |
| H6 | Structure | Verse-Chorus 구조 인식 가능 (Ambient drift 방지) |
| H7 | Exclude | Exclude 키워드 준수 + Articulation 포함 |

---

## Style-Specific Gates

### Style A — Korean Indie Pop
| # | Gate | 기준 |
|---|------|------|
| A1 | Jangly Guitar | 잔글링 일렉기타가 리드 악기 (클린톤, 코러스 이펙트) |
| A2 | Upbeat Drum | 경쾌한 드럼 패턴 존재 (크리스프 스네어, 오픈 하이햇) |
| A3 | Vocal Forward | 보컬이 믹스 전면, 선명하고 직접적 |

### Style B — Spring Dream Pop
| # | Gate | 기준 |
|---|------|------|
| B1 | Shimmer Guitar | 시머링 리버브 기타 존재 (heavy reverb + delay) |
| B2 | Ethereal Pad | 에테리얼 신스 패드 또는 글로켄슈필 |
| B3 | Atmospheric | 분위기/텍스처가 풍성, 공간감 넓음 |

### Style C — Dreamy Indie Pop (혼합)
| # | Gate | 기준 |
|---|------|------|
| C1 | Guitar Dual | 잔글링 + 시머링 기타 요소 공존 |
| C2 | Piano/Strings | 피아노 또는 스트링 레이어 존재 |
| C3 | Balance | 멜로디 선명 + 분위기 풍성 양립 (한쪽에 치우치지 않음) |

---

## 8-Factor Scoring (100점)

| # | Factor | 배점 | 기준 | 레퍼런스 |
|---|--------|------|------|---------|
| F1 | 멜로디/훅 | 20 | 캐치한 멜로디 훅, 반복 시 각인, 코러스 기억도 | 마틴스미스 "봄 그리고 너" |
| F2 | 봄 톤 | 15 | 밝고 따뜻한 봄 감성. 두근거림/설렘 전달 (dark/sad 아님) | concept.md 차별점 |
| F3 | 한국어 보컬 | 15 | 발음 명료, 톤 적합(Bright/Sweet/Clear), Chest voice, 자연스러움 | STYLE.md + 리서치 |
| F4 | 기타 사운드 | 10 | 잔글링/시머링 기타 품질, 클린톤, 적절한 이펙트 | AllMusic, Wikipedia |
| F5 | 프로덕션 | 15 | 악기 공간 분리, 보컬 포워드, 이펙트 밸런스, Harmony Guard | STYLE.md §1-2 |
| F6 | 에너지 아크 | 10 | V→C 상승, Chorus lift, Bridge 빌드, 4막 에너지 흐름 | STYLE.md §3-4 |
| F7 | Dream Pop 질감 | 5 | (Style B/C만) 리버브 공간감, 에테리얼 패드, 시머 텍스처 | Pond5, Reverb Machine |
| F8 | 장르 정체성 | 10 | Indie Pop(+Dream Pop)으로 인식되는가? 이탈 없는가? | 종합 판단 |

---

## 판정

| 점수 | 판정 | 액션 |
|------|------|------|
| 85+ | **PASS** | 진행 |
| 70-84 | **BORDERLINE** | 문제 Factor 수정 후 재평가 |
| <70 | **FAIL** | 재작성 |

**CRITICAL FAIL:** 개별 Factor ≤ 배점의 30% = 즉시 FAIL
- F1 ≤6, F2 ≤4, F3 ≤4, F4 ≤3, F5 ≤4, F6 ≤3, F7 ≤1, F8 ≤3

---

## Drift 감지 체크리스트

Suno 결과물 청취 시 아래 신호가 감지되면 해당 Factor 감점:

### K-Pop Drift (→ F8 감점)
- [ ] 과도하게 폴리시된 프로덕션 (인디 질감 소실)
- [ ] 댄스비트 / 4-on-the-floor 킥 패턴
- [ ] 오토튠 보컬 / 과도한 보컬 프로세싱
- [ ] EDM 드롭 또는 빌드업

### K-Ballad Drift (→ F2, F6 감점)
- [ ] BPM <90으로 느려짐
- [ ] 피아노 발라드 구조 (기타 부재)
- [ ] 감정 과잉 (belt, 울먹임)
- [ ] 이별/상실 무드 (봄 톤 이탈)

### Indie Rock Drift (→ F5, F8 감점)
- [ ] 디스토션 기타가 사운드 지배
- [ ] 앵스트/공격적 보컬 톤
- [ ] 헤비한 드럼 드라이브

### Shoegaze Drift (→ F3, F8 감점)
- [ ] 보컬 완전 매몰 (가사 인식 불가)
- [ ] 노이즈 wall of sound
- [ ] 과도한 디스토션/퍼즈

### City Pop Drift (→ F8 감점, 21-00 영역 침범)
- [ ] 레트로 신스 / 80s 팝 프로덕션
- [ ] 펑키 베이스라인
- [ ] 시티팝 특유의 코드 진행

### Ambient Drift (→ F1, F6 감점)
- [ ] 보컬 부재 또는 극히 미미
- [ ] 곡 구조(V-C) 소멸
- [ ] 멜로디 없이 텍스처만 존재

**2개 이상 체크 시:** 해당 Factor 재평가 + 프롬프트 조정

---

## Style Checklist

| # | 항목 | A | B | C | 체크 |
|---|------|---|---|---|------|
| S1 | BPM 90-118 | ● | ● | ● | ☐ |
| S2 | Jangly guitar lead | ● | | ● | ☐ |
| S3 | Shimmer reverb guitar | | ● | ● | ☐ |
| S4 | Upbeat drum pattern | ● | | | ☐ |
| S5 | Ethereal pad / glockenspiel | | ● | ● | ☐ |
| S6 | Piano or strings layer | | | ● | ☐ |
| S7 | Vocal forward (선명) | ● | | ● | ☐ |
| S8 | Atmospheric reverb space | | ● | ● | ☐ |
| S9 | Bright/Sweet/Clear vocal | ● | | ● | ☐ |
| S10 | Airy/Ethereal vocal | | ● | | ☐ |
| S11 | Harmony Guard (단독 리드) | ● | ● | ● | ☐ |
| S12 | Articulation 포함 | ● | ● | ● | ☐ |
| S13 | Exclude 키워드 준수 | ● | ● | ● | ☐ |
| S14 | 밝은 봄 톤 (dark 아님) | ● | ● | ● | ☐ |

---

## 보컬 Checklist (Suno 결과물 청취 QC)

| # | 항목 | 체크 |
|---|------|------|
| V1 | 한국어 발음 명료 (뭉개짐 없음) | ☐ |
| V2 | 훅 존재 + 중독성 (반복 시 각인) | ☐ |
| V3 | 보컬 톤이 장르에 적합 (Bright/Sweet — 봄 감성) | ☐ |
| V4 | 단독 리드 보컬 (합창/스택 없음) | ☐ |
| V5 | 가사 자연스러움 (AI스러운 어색함 없음) | ☐ |

---

## QC Template

```md
## Indie Pop QC — Track {N} "{제목}"

### Hard Gates
| Gate | 결과 | 비고 |
|------|------|------|
| H1 BPM | | {N} BPM |
| H2 Melody | | |
| H3 Guitar | | |
| H4 Vocal | | |
| H5 Tone | | |
| H6 Structure | | |
| H7 Exclude | | |

### Style {A/B/C} Gates
| Gate | 결과 |
|------|------|
| {X}1 | |
| {X}2 | |
| {X}3 | |

### 8-Factor Scoring
| Factor | 점수 | 비고 |
|--------|------|------|
| F1 멜로디/훅 | /20 | |
| F2 봄 톤 | /15 | |
| F3 한국어 보컬 | /15 | |
| F4 기타 사운드 | /10 | |
| F5 프로덕션 | /15 | |
| F6 에너지 아크 | /10 | |
| F7 Dream Pop 질감 | /5 | |
| F8 장르 정체성 | /10 | |
| **Total** | **/100** | |

### Drift 체크: K-Pop / K-Ballad / Rock / Shoegaze / City Pop / Ambient
### Style Checklist: S1-S14
### 보컬 Checklist: V1-V5

### 판정: PASS / BORDERLINE / FAIL
### 수정 사항: (BORDERLINE/FAIL 시)
```
