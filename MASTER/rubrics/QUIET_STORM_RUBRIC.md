# Quiet Storm / Chill R&B Rubric

Version: 1.0
Last Updated: 2026-03-27
Purpose: Quiet Storm / Chill R&B 장르 게이트 (22-00 시리즈)

> Based on: `report/2026-03-27_22-00-genre-research.md` (19소스, 92% 신뢰도)
> Evidence: PBS, PMC 학술 논문, Spotify for Artists, Suno 커뮤니티 가이드

---

## Evidence Basis

### 1. Quiet Storm vs Slow Jam 차이점

| 항목 | Slow Jam (Slow R&B) | Quiet Storm |
|------|---------------------|-------------|
| 기원 | 1950s R&B 발라드 | 1976 WHUR 라디오 포맷 |
| BPM | 55-80 | 60-90 |
| 정서 | 로맨틱, 관능적, 에로틱 | 사색적, 친밀한, 멜랑콜리 |
| 보컬 | 팔세토, 관능적 딜리버리 | 벨벳, 절제된, 뉘앙스 |
| 프로덕션 | 레이어드 신스, 패드 | Rhodes/EP, 프렛리스 베이스, 실키 패드 |
| 가사 | 로맨스, desire, body | 사색, 회고, 친밀감 |
| 22-00 적합도 | **낮음** — 톤 불일치 | **높음** — 정서 일치 |

### 2. 핵심 특성

**필수 (없으면 해당 장르 아님):**
- Rhodes/felt piano/ambient pad 중 하나가 리드
- 친밀하고 따뜻한 공간감
- 절제된 보컬 (belt 없음)
- 60-78 BPM (22-00 범위)

**권장:**
- Brush kit / soft shaker / rim-click 퍼커션
- Warm bass (sub-bass 또는 acoustic)
- 넓은 스테레오, moderate reverb
- Chest voice, dry close-mic

**금지:**
- 로맨틱/관능적 키워드 (slow jam drift)
- Powerful belt, aggressive dynamics
- Stacked harmonies, choir
- Trap hi-hats, 808 slides, EDM drops

### References
- PBS: "What is Quiet Storm Music" (A급)
- PMC: "Audio Features of Sleep Music" (A급, 학술)
- Spotify for Artists: "Behind the Playlists: R&B" (A급)
- HookGenius: Suno R&B Prompts (B급)
- Micro Genre Music: Quiet Storm / Bedroom R&B (B급)

---

## Hard Gates (1개라도 FAIL = 재작성)

| # | Gate | 기준 |
|---|------|------|
| H1 | BPM | 60-78 범위 명시 |
| H2 | Lead Instrument | Rhodes, felt piano, ambient pad, 또는 nylon guitar |
| H3 | Mood Keyword | "intimate", "warm", "gentle" 중 1개+ 존재 |
| H4 | Slow Jam Drift | "slow jam", "sensual", "seductive", "romantic", "sultry" 없음 |
| H5 | Vocal | 한국어 + Chest voice + 단독 리드 (Harmony Guard) |
| H6 | Belt | Belt 금지 — "gentle sustained note" 또는 "tender lift"만 |
| H7 | Exclude | Exclude 키워드 준수 + Articulation 포함 |

---

## Style-Specific Gates

### Style A — Ambient Chill R&B
| # | Gate | 기준 |
|---|------|------|
| A1 | Ambient Pad | ambient pad가 리드 악기 |
| A2 | No Percussion | kick, snare 없음 (soft shaker만 허용) |
| A3 | Spacious | 넓은 공간감, floating mix |

### Style B — Quiet Storm
| # | Gate | 기준 |
|---|------|------|
| B1 | Piano/Rhodes | felt piano 또는 Rhodes가 리드 |
| B2 | Brush Kit | soft brush kit + rim-click 퍼커션 |
| B3 | Warm | 가장 따뜻한 톤, bedroom ambience |

### Style C — Acoustic Chill R&B
| # | Gate | 기준 |
|---|------|------|
| C1 | Nylon Guitar | nylon guitar가 리드 |
| C2 | Minimal | 최소 편성, stripped-back |
| C3 | Lullaby | lullaby-like phrasing, organic mix |

---

## 6-Factor Scoring (100점)

| # | Factor | 배점 | 기준 | 레퍼런스 |
|---|--------|------|------|---------|
| F1 | Quiet Storm 미학 | 20 | Rhodes/EP, warm pads, 실키 프로덕션, 친밀 공간감 | Evidence §2 |
| F2 | 릴랙스 톤 | 20 | 수면 전 이완 무드 (로맨틱/관능적 **아님**) — 핵심 차별점 | Drift 체크 |
| F3 | 보컬 딜리버리 | 20 | Gentle/intimate chest voice, belt 없음, falsetto 유혹 없음 | STYLE.md §4.1 |
| F4 | 편곡 절제 | 15 | Sparse, 미니멀 퍼커션, 4막 에너지 아크 준수 | concept.md 4막 구조 |
| F5 | 구조 흐름 | 15 | V-PC-C 구조, gentle chorus lift, outro fade | concept.md Song Structure |
| F6 | 장르 경계 | 10 | Slow Jam / Bedroom Pop lo-fi / Neo-Soul jazz-funk으로 이탈 안 함 | Evidence §1 |

---

## 판정

| 점수 | 판정 | 액션 |
|------|------|------|
| 85+ | **PASS** | 진행 |
| 70-84 | **BORDERLINE** | 문제 Factor 수정 후 재평가 |
| <70 | **FAIL** | 재작성 |

**CRITICAL FAIL:** 개별 Factor ≤ 배점의 30% = 즉시 FAIL
- F1 ≤6, F2 ≤6, F3 ≤6, F4 ≤4, F5 ≤4, F6 ≤3

---

## "Slow Jam Drift" 감지 체크리스트

Suno 결과물 청취 시 아래 신호가 감지되면 **F2 감점 + H4 재검토**:

### 보컬 Red Flags
- [ ] Falsetto runs / melisma 과다
- [ ] Breathy seductive whisper ("baby", "tonight")
- [ ] 관능적 ad-libs (moaning, sighing)

### 무드 Red Flags
- [ ] Romantic yearning / desire 톤
- [ ] Sensuality / 관능적 분위기
- [ ] "Come closer" 류 유혹적 가사

### 프로덕션 Red Flags
- [ ] 레이어드 신스 패드 (Quiet Storm의 clean pad와 다름)
- [ ] Bass-heavy groove (수면 릴랙스에 부적합)
- [ ] Snapping fingers / finger snap groove

### 가사 Red Flags
- [ ] Body references
- [ ] Romantic longing (그리움 ≠ 안식)
- [ ] 에로틱 암시

**1개 이상 체크 시:** F2 점수 재평가 + 프롬프트 조정 고려

---

## Style Checklist

| # | 항목 | A | B | C | 체크 |
|---|------|---|---|---|------|
| S1 | BPM 60-78 | ● | ● | ● | ☐ |
| S2 | Ambient pad lead | ● | | | ☐ |
| S3 | Felt piano / Rhodes lead | | ● | | ☐ |
| S4 | Nylon guitar lead | | | ● | ☐ |
| S5 | No kick/snare (shaker only) | ● | | | ☐ |
| S6 | Brush kit + rim-click | | ● | | ☐ |
| S7 | Minimal arrangement | | | ● | ☐ |
| S8 | Chest voice + gentle | ● | ● | ● | ☐ |
| S9 | No belt (sustained note only) | ● | ● | ● | ☐ |
| S10 | Harmony Guard (단독 리드) | ● | ● | ● | ☐ |
| S11 | Articulation 포함 | ● | ● | ● | ☐ |
| S12 | Exclude 키워드 준수 | ● | ● | ● | ☐ |
| S13 | Slow Jam Drift 없음 | ● | ● | ● | ☐ |

---

## QC 템플릿

```md
Quiet Storm Rubric Score
- Track: [시리즈/번호]
- Hard Gates: PASS/FAIL
- Slow Jam Drift: CLEAR/DETECTED

| Factor | Score | Notes |
|--------|------:|-------|
| F1 Quiet Storm 미학 |  /20 |  |
| F2 릴랙스 톤 |  /20 |  |
| F3 보컬 딜리버리 |  /20 |  |
| F4 편곡 절제 |  /15 |  |
| F5 구조 흐름 |  /15 |  |
| F6 장르 경계 |  /10 |  |
| **Total** |  /100 |  |

Verdict: PASS / BORDERLINE / FAIL
```
