# 20-00 💪 AFTER HOURS WORKOUT 시리즈 장르 게이트(루브릭) 설계 회의

- **날짜**: 2026-04-26
- **모드**: Team Mode — Trade-off Discussion (5개 안건 트레이드오프 + Decision Meeting 요소)
- **참석**: Product Leader, Marketing Director, Engineering Lead + QA Reviewer (Round 2)
- **주제**: 20-00 시리즈 곡 PASS/FAIL 자동 판정용 장르 게이트(루브릭) 설계

---

## 컨텍스트

20-00 `💪 AFTER HOURS WORKOUT` 시리즈 — Korean Hard Hip-Hop · Workout · Night Grind 컨셉 (저녁 8시 운동, 25-35 직장인 페르소나). concept.md v0.2 작성 완료, 이제 곡 PASS/FAIL 판정용 장르 게이트(루브릭) 필요.

**시리즈 정체성**:
- 신 4축 + 보너스: A Rage Dry (3-4) / B Rage Tuned (5) / C Hardcore Trap (5-6) / D K-Drill 액센트 (3) / 보너스 빡센 붐뱁 (2-3) = 18-21곡
- 핵심 원칙 (사용자 정정 2026-04-26): 시리즈 컨셉(Workout) 정합 = 사운드(BPM·에너지·페이스)에서만. 가사 자유 (회피 영역만: 무차별 폭력·살해·총기·마약 직접 묘사)
- BPM: 86-95 (붐뱁) / 140-160 (Rage·Trap) / 140-146 (K-Drill)

**기존 wavvy 루브릭 형식 (참고)**: 12-00 AFROBEATS_RUBRIC = Hard Gates 7개 + Style Gates 9개 + 8-Factor Scoring 100점

---

## Phase 1: 전문가별 분석

### 안건 1 — Hard Gates 항목 정의

**[PRODUCT LEADER]** — Now/Next/Later + RICE
- 12-00의 7개 Hard Gate 골격 유지, 9개 이상은 운영 피로
- 7개 제안: BPM / Drum / Bass / Vocal / Hook / EXCLUDE / 브랜드 톤(가사 회피)

**[MARKETING DIRECTOR]** — April Dunford Positioning
- H7 가사 검사는 Hard Gate 부담 ↑ → Soft Gate로
- 대신 H7 자리에 **Workout 사운드 정합** (BPM·텐션 곡선·반복 청취 임계)
- 근거: Apple Music "격하게 운동할 때 듣는 힙합" 카테고리 진입 자격

**[ENGINEERING LEAD]** — 자동화 비용
- 가사 회피는 자동 grep으로 비용 0 → Hard Gate 유지
- MD의 Workout 사운드 정합 동의 (단 반복 청취 피로도는 자동 검사 불가, Style Checklist로 분리)
- **8개 Hard Gate**: BPM·Drum·Bass·Vocal·Hook·EXCLUDE·Workout 사운드·콘텐츠 회피

**합의**: 8개 Hard Gate (자동화 H6/H8 → 실질 수동 6개로 12-00 동등)

---

### 안건 2 — 5개 Style별 Specific Gates

**[PRODUCT LEADER]** — Style별 1-3개씩
- A. Dry: A1(no autotune) + A2(blown-out) + A3(short reverb)
- B. Tuned: B1(autotune 시그니처) + B2(melodic chorus) + B3(cathedral reverb)
- C. Hardcore: C1(husky) + C2(distorted 808 + dark piano)
- D. K-Drill: D1(sliding 808) + D2(drill snare) + D3(된소리/거센소리 + 다크 melody)
- E. 붐뱁: E1(dusty drum) + E2(라이리시즘)

**[MARKETING DIRECTOR]**
- B 추가: B4. Korean KC vangdale 광택 디자인 (mastering -7 LUFS, polished glossy mix)
- 한국 토착 색채 보호

**[ENGINEERING LEAD]**
- A·B 게이트 수 동등화 위해 C·D BPM 게이트 추가 제안 → PL "Hard Gate H1과 중복" 반대로 철회
- **13개 Style Gate** 확정 (A 3 + B 4 + C 2 + D 3 + E 2)

**합의**: 13개 Style-Specific Gate. **A1 vs B1 = 시리즈 핵심 차별점** (Section A.3.4 EXCLUDE 분리표 게이트화)

---

### 안건 3 — 8-Factor Scoring 카테고리 + 배점 (100점)

**[PRODUCT LEADER]** — 12-00 형식 + Hard Hip-Hop 특성

| # | Factor | 배점 |
|---|--------|------|
| F1 | Trap Groove | 15 |
| F2 | 808/Bass | 10 |
| F3 | Hook & Ad-libs | 15 |
| F4 | Korean Vocal Identity | 15 |
| F5 | Energy Arc | 10 |
| F6 | Workout 정합 | 10 |
| F7 | Production | 15 |
| F8 | 장르 정체성 (4축 정합) | 10 |

**[MARKETING DIRECTOR]**
- F4는 음성·발음·톤만, 가사 평가 X (사용자 정정 반영)
- 가사 = Hard Gate H8로 분리 (PASS/FAIL 2진), 점수화 X

**[ENGINEERING LEAD]**
- F6 Workout 정합은 곡 단위 점수화 어려움 → BPM 단계 분류만 점수화
- 페이스·반복 청취는 시리즈 게이트로

**합의**: F4 음성만 / F6 BPM 단계 매칭만 / 가사는 H8 / 시리즈 정합은 안건 5

**판정 기준**: 85+ PASS / 70-84 BORDERLINE / <70 FAIL / Critical Fail = 개별 Factor ≤30%

---

### 안건 4 — 가사 자유성 게이트 반영

**[PRODUCT LEADER]** — 사용자 정정 반영
- Hard Gate H8 콘텐츠 회피 = 자동 grep
- 8 Factor F4 가사 평가 X
- E2 라이리시즘 = 보너스 붐뱁만

**[MARKETING DIRECTOR]** — YouTube 알고리즘 친화
- 회피 어휘 50개 (5개 카테고리): 폭력·살해 / 마약 / 혐오 / 자해·자살 / 노골적 성행위
- **K-Drill 본가 어휘 보존**: 갱·크루·블록·동네·디스 등 무드 어휘는 회피 X

**[ENGINEERING LEAD]**
- `MASTER/scripts/check_lyric_avoid.sh` 스크립트 작성 (50개 키워드 grep)
- 검사 비용 0

**합의**: 가사 회피만 검사. F4·E2 분리. 자동 grep으로 비용 0

---

### 안건 5 — Workout 정합 시리즈 단위 게이트

**[PRODUCT LEADER]** — 시리즈 게이트 5개 제안
- S1. 곡수 분포 (A 3-4 / B 5 / C 5-6 / D 3 / 보너스 2-3 = 18-21곡)
- S2. BPM 분포 (워밍업/메인/HIIT/쿨다운 4단계)
- S3. A·B 인접 회피 (청취 피로)
- S4. 시리즈 길이 60-90분 (1세션 정합 88.1%)
- S5. Track 01 = 워밍업 B축 멜로딕

**[MARKETING DIRECTOR]** — 1개 추가
- S6. 마지막 2-3곡 = 멜로딕 마무리 (B + 보너스 붐뱁) — YouTube replay 친화

**[ENGINEERING LEAD]** — 자동화 검증
- 6개 모두 자동화 가능 (메타 파일 + Track Map 검증)
- `MASTER/scripts/check_series_gate.sh` 스크립트로 통합

**합의**: 시리즈 게이트 6개 (S1-S6) + 자동화 스크립트

---

## Phase 2: 종합 토론

### 합의점

1. **루브릭 4단 구조 확정**:
   - Hard Gates 8개 (H1-H8)
   - Style-Specific Gates 13개 (A 3 + B 4 + C 2 + D 3 + E 2)
   - 8-Factor Scoring 100점 (F1-F8)
   - Series Gates 6개 (S1-S6)

2. **A1 vs B1 분리 = 시리즈 핵심 차별점** — Section A.3.4 EXCLUDE 분리표 그대로 게이트화 (no autotune vs autotune 필수)

3. **가사 자유 정책 게이트 반영** — F4 음성만 / 가사 = H8 회피 영역 자동 grep / 라이리시즘 = 보너스 붐뱁만(E2)

4. **자동화 범위** — H6 EXCLUDE / H8 가사 회피 / S1-S6 시리즈 게이트 = 모두 자동 (12-00 운영 부담 동등)

5. **시리즈 게이트 신설** — 곡 단위 게이트와 분리, 시리즈 운영 BGM 카테고리 점령 자격 검증

### 충돌 (해소됨)

| 충돌 | 해소 |
|------|------|
| MD: H7 자동화 부담 / EL: 자동화로 비용 0 | EL 승 — 자동 grep |
| EL: F6 Workout 점수화 어려움 / PL: 곡 단위 평가 필요 | PL 절충 — F6는 BPM 단계 분류만 |
| EL: Style Gate 16개 너무 많음 / PL: 13개 축소 | PL 승 — C·D BPM은 Hard Gate 중복 제거 |

### 트레이드오프

| 옵션 | 장점 | 단점 | 지지 역할 |
|------|------|------|----------|
| Hard Gate 7개 (12-00 동등) | 운영 부담 ↓ | Workout 정합 게이트 부재 | (기각) |
| **Hard Gate 8개 (Workout 추가)** | **시리즈 차별점 명확** | **운영 부담 ↑ but 자동화로 상쇄** | **PL+MD+EL** |
| Hard Gate 9개 이상 | 더 정밀 | 운영 피로 임계 초과 | (기각) |

### 추천

> **루브릭 v1.0 (`MASTER/rubrics/HARD_HIPHOP_RUBRIC.md`)** = Hard Gates 8 + Style Gates 13 + 8-Factor 100점 + Series Gates 6
>
> **즉시 작성 가능한 수준**. concept.md v0.2 절충안 곡수 분포(18-21곡)와 정합. 자동화 스크립트 2개(`check_lyric_avoid.sh` + `check_series_gate.sh`) 별도 작성.

### 결정 기준

- **운영 효율 우선** → Hard Gate 7개 (12-00 동등)
- **시리즈 차별점 명확성 우선** → Hard Gate 8개 (Workout 정합 추가) ← **채택**

---

## Phase 3: QA 검증 (Round 2)

### Gate별 결과
| Gate | PASS/FAIL | 점수 | 사유 |
|------|-----------|------|------|
| G1. 12-00 형식 일관성 | PASS | 96 | Hard 8 + Style 13 + 8-Factor 100점 형식 동일 |
| G2. concept.md v0.2 정합성 | PASS | 98 | S1 곡수·S2 BPM 분포 일치 |
| G3. 사용자 피드백 반영 | PASS | 95 | F4 음성만 / 가사 H8 / E2 보너스만 |
| G4. Section A·B 인용 | PASS | 92 | A1 vs B1 / S2 BPM 분포 직접 인용 |
| G5. 운영 효율 | PASS | 90 | 자동화 H6/H8/S1-S6 → 12-00 동등. Style Gate 13개 다소 많음 BORDERLINE |
| G6. 차별점 명확성 | PASS | 97 | A1 vs B1 + B4 KC 시그니처 + D1 UK/NY Drill |
| G7. Workout 카테고리 진입 | PASS | 94 | H7 + S2 + S3 + S5/S6 정합 |

### 종합 판정
- **결과: PASS**
- **점수 평균: 94.6** (모든 Gate ≥90)
- **만장일치 95+ 충족**: N (G5 90 BORDERLINE) — 단 모든 Gate 개별 PASS → 진행 OK
- **보완 권고 (선택)**: G5 BORDERLINE — Style Gate 13개 → 가능하면 11개로 축소 (B축 4→3, D축 3→2). 단 강제 X, 운영 시 부담 발생하면 재검토

---

## Next Actions (3)

1. **`MASTER/rubrics/HARD_HIPHOP_RUBRIC.md` v1.0 작성** — 위 4단 구조 (Hard 8 + Style 13 + 8-Factor 100점 + Series 6)
2. **자동화 스크립트 2개 작성**:
   - `MASTER/scripts/check_lyric_avoid.sh` (가사 회피 50 키워드 grep, 5개 카테고리)
   - `MASTER/scripts/check_series_gate.sh` (S1-S6 자동 검증)
3. **Suno 1차 테스트 5곡 (A/B/C/D/보너스 각 1)** → 루브릭 v1.0으로 PASS/FAIL 판정 → v1.1 조정

---

*Generated by Lenny's Product Team — Team Mode*
