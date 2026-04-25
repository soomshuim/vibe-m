# Korean Hard Hip-Hop Rubric

Version: 1.1
Last Updated: 2026-04-26
Purpose: Korean Hard Hip-Hop · Workout 장르 게이트 (20-00 시리즈)

> **v1.1 변경 (2026-04-26)**: Hard 60% 정책 사용자 결정 반영. 곡수 분포 A 4 / B 5 / C 5 / D 3 / 보너스 3 = 20곡 확정 (Hard A+C+D 12곡 60% / Non-Hard B+보너스 8곡 40%).

> **Based on**:
> - `SERIES/20-00/concept.md` v0.2 (4축 + 보너스 곡수 절충)
> - `SERIES/20-00/report/2026-04-25_workout-tuned-rage-supplement.md` (Section A·B 통합)
> - `meetings/2026-04-26_20-00-genre-gate-rubric-design.md` (/team 만장 합의 평균 94.6점)
>
> **시리즈 정체성**: Korean Workout Hip-Hop 빈자리 (글로벌 Apple Music Hip-Hop Workout 외산 트랩 우세, Korean rap 0%)
> **페르소나**: 25-35 한국 직장인, 저녁 8시 운동 (헬스/PT/홈트/러닝)

---

## Hard Gates (1개라도 FAIL = 재작성)

| # | Gate | 기준 | 자동/수동 |
|---|------|------|----------|
| H1 | **BPM** | 86-95 (붐뱁) OR 140-160 (Rage·Trap·K-Drill) | 수동 |
| H2 | **Drum Pattern** | 808 + 1/16 hi-hat steady (메인 4축) OR dusty kick + rim snare swing (붐뱁). Pop kick·EDM kick = FAIL | 수동 |
| H3 | **Bass** | 808 sub-bass (메인 4축) OR walking upright bass (붐뱁). Pop sub bass·EDM bass·synth pop bass = FAIL | 수동 |
| H4 | **Vocal — Korean Hard Rap** | 한국어 95%+ (D K-Drill만 75% 예외) + chest voice + sharp articulation. Pop singing·falsetto·thin head voice = FAIL | 수동 |
| H5 | **Hook 존재** | 1-2마디 반복 hook + ad-lib layer (Rage·Trap·K-Drill) OR multisyllabic punchline (붐뱁). Hook 부재 = FAIL | 수동 |
| H6 | **EXCLUDE 공통** | EDM drop · beat switch · sung melodic chorus · k-pop 진입 = FAIL. Suno Style Prompt EXCLUDE 키워드 검증 | 자동 |
| H7 | **Workout 사운드 정합** | (1) BPM 90-180 안 / (2) 텐션 곡선 운동 단계 매칭 가능 / (3) 곡 길이 2:30-3:45 (붐뱁 3:45까지). 모두 충족 = PASS, 1개 이상 FAIL = 재작성 | 수동 |
| H8 | **콘텐츠 회피** | 무차별 폭력·살해·총기·마약·혐오 직접 묘사 = FAIL. K-Drill 본가 어휘(갱·크루·블록·동네·디스) 회피 X. 50 키워드 5카테고리 grep | 자동 (`check_lyric_avoid.sh`) |

> **자동화 비율**: H6 + H8 자동 → 실질 수동 6개 (12-00 AFROBEATS와 동등 운영 부담)

---

## Style-Specific Gates (13개)

### Style A: Rage Dry Voice (3개) — 4곡 (Hard)

| # | Gate | 기준 |
|---|------|------|
| A1 | **Vocal Delivery — Dry** | screamed / yelled / raw shouted, **NO autotune**. Suno Style Prompt에 `no autotune, no pitch correction` EXCLUDE 명시 필수 |
| A2 | **Master Loudness — Blown-out** | brick-walled mastering, -6 LUFS 수준, blown-out 의도. Polished glossy mix = FAIL (B축으로 sliding) |
| A3 | **Reverb — Short Raw** | static decay <1초, raw close-mic. Cathedral reverb · large hall = FAIL (B축으로 sliding) |

> **참조**: Playboi Carti `Whole Lotta Red` / Yeat 일부 / Ken Carson. Korean 토착 풀: Loopy `MARNI` 일부 + Lil Moshpit 비트 일부 (PUBLIC ENEMY 161 BPM, E minor 확정)

### Style B: Rage Tuned Singing (4개) — 5곡 (Non-Hard) ★ 메인 hub

| # | Gate | 기준 |
|---|------|------|
| B1 | **Vocal Delivery — Tuned** | melodic autotuned sing-rap delivery, **autotune 시그니처 필수** (Antares Auto-Tune retune 5-15ms 추정). Dry shouted = FAIL |
| B2 | **Hook — Melodic Chorus** | melodic chorus 명확 (verse-chorus 구조 보존). Chant 위주 hook = FAIL |
| B3 | **Reverb — Cathedral** | cathedral reverb plate large hall (Travis Scott 시그니처). Short raw decay = FAIL |
| B4 | **Korean KC vangdale 광택 디자인** | mastering -7 LUFS, polished glossy mix, candied vocal. Blown-out = FAIL |

> **참조**: Travis Scott `Astroworld` 톤 / Don Toliver `Hardstone Psycho` / **Sik-K × HAON `ALBUM ON THE WAY!` (2023-05-18)** / **Sik-K × Lil Moshpit `K-FLIP+` (2025-03-17, KMA 2025 Best Rap)** / KCTAPE Vol.2 / MOLLAK (Female 인접). NOWIMYOUNG `LUXURY TAPE`은 electropop 비중 → "인접 사례"로만 참조

### Style C: Hardcore Trap (2개) — 5곡 (Hard) ★ Workout 표준

| # | Gate | 기준 |
|---|------|------|
| C1 | **Vocal Delivery — Husky** | husky / distorted / muddy 딜리버리, chest voice dry close. Melodic singing = FAIL |
| C2 | **Bass + Piano** | deep distorted 808 sub-bass moving line + dark minor key piano stab loop. Pop piano·major key bright = FAIL |

> **참조**: ZENE THE ZILLA · Ash Island · Loopy (UNWANTED WRLD 시기) · EK · KWAII

### Style D: K-Drill 액센트 (3개) — 3곡 (Hard)

| # | Gate | 기준 |
|---|------|------|
| D1 | **Bass — Sliding 808** | sliding 808 bass with portamento glide (UK/NY Drill 시그니처). Static 808 = FAIL |
| D2 | **Drum — Drill Snare** | drill snare with skippy hi-hat patterns. Standard trap snare/hi-hat = FAIL |
| D3 | **본가 무드 보존** | 한국어 된소리/거센소리(ㄲ ㄸ ㅃ ㅋ ㅌ) 악센트 + 다크 minor key piano/flute melody. 가사 리라이트 강제 X (본가 무드 자유 — 디스·반항·도시·자기 서사) |

> **참조**: Fleeky Bang · Blase · Silkybois · deadbois · NO:EL. **글로벌 사례**: UK Drill / NY Drill = Workout BGM 카테고리 자리 잡음 (Spotify KaiverickDigital 1,000+곡)

### Style E: 빡센 붐뱁 (Bonus, 2개) — 3곡 (Non-Hard)

| # | Gate | 기준 |
|---|------|------|
| E1 | **Drum — Dusty + Walking Bass** | dusty drums with vinyl crackle texture + walking upright bass + rim-shot snare + head-nod swing |
| E2 | **Lyricism — 다음절 라임** | dense multisyllabic rhyme + 90s East Coast vernacular + 한국어 vernacular. 단순 단음절 라임 = FAIL |

> **참조**: 가리온 · Deepflow · Huckleberry P · Paloalto · Kid Milli · QM · 다이나믹 듀오. 리서치 자산: `report/2026-04-25_suno-boom-bap-prompt-engineering-gpt.md`

---

## 8-Factor Scoring (100점)

| # | Factor | 배점 | 기준 | 레퍼런스 |
|---|--------|------|------|---------|
| F1 | **Trap Groove** | 15 | 808 + 1/16 hi-hat steady, locked drum pattern. 붐뱁은 dusty kick + swing groove | concept.md §Style Templates |
| F2 | **808/Bass** | 10 | 베이스 디자인 (distorted/sliding/portamento), 킥과 sync, 저음 임팩트 | Section A.2.2 |
| F3 | **Hook & Ad-libs** | 15 | 1-2마디 hook + ad-lib stack 밀도. 붐뱁은 multisyllabic punchline 밀도 | Section A.3 |
| F4 | **Korean Vocal Identity** | 15 | Suno 한국어 발음 명료도 + 보컬 톤 정합 (A=raw shouted / B=autotuned melodic / C=husky / D=accent / E=raw chest). **음성·발음·톤만 평가, 가사 내용 X** | concept.md §Style Templates 보컬 디스크립터 |
| F5 | **Energy Arc** | 10 | Verse → Hook 텐션 빌드, drop 없이도 텐션 유지, 곡 후반 폭주 X | concept.md §LYRICS 가이드 |
| F6 | **Workout BPM 단계 매칭** | 10 | 워밍업 100-120 / 메인 130-150 / HIIT 140-180 / 쿨다운 90-110 중 어디 매칭되는지 분류. **페이스·반복 청취 피로도는 Series Gate로 분리** | concept.md §Workout 배치 룰 |
| F7 | **Production** | 15 | 믹스 분리, 보컬 포워드, 마스터링 톤 (A=blown-out / B=glossy -7 LUFS / C=gritty / D=dark / E=warm dusty). EQ·리버브·압축 적정성 | Section A.2 |
| F8 | **장르 정체성 (4축 정합)** | 10 | Hard Hip-Hop으로 인식되는가? 시리즈 4축 + 보너스 5종 중 정확히 1개에 매칭되는가? Pop·R&B·EDM 이탈 = FAIL | 종합 판단 |

---

## 판정

| 점수 | 판정 | 액션 |
|------|------|------|
| 85+ | **PASS** | 진행 |
| 70-84 | **BORDERLINE** | 문제 Factor 수정 후 재평가 |
| <70 | **FAIL** | 재작성 |

**CRITICAL FAIL**: 개별 Factor ≤ 배점의 30% = 즉시 FAIL
- F1 ≤4 / F2 ≤3 / F3 ≤4 / F4 ≤4 / F5 ≤3 / F6 ≤3 / F7 ≤4 / F8 ≤3

---

## Series Gates (6개) — 시리즈 단위 자동 검증

> **곡 단위 게이트와 분리**. 시리즈 운영 BGM 카테고리 진입 자격 검증. 자동화 스크립트 1건으로 통합 (`check_series_gate.sh`).

| # | Gate | 기준 | 자동/수동 |
|---|------|------|----------|
| S1 | **곡수 분포 + Hard 60%** | **A 4 / B 5 / C 5 / D 3 / 보너스 3 = 20곡 확정** + **Hard(A+C+D)=12곡(60%)** + **Non-Hard(B+보너스)=8곡(40%)** | 자동 |
| S2 | **BPM 분포** | 워밍업(100-120) 2-3곡 / 메인(130-150) 8-9곡 / HIIT(140-180) 5-6곡 / 쿨다운(90-110) 2-3곡 | 자동 |
| S3 | **A·B 인접 회피** | A Dry Voice 트랙 직후 B Tuned Singing 트랙 직접 인접 배치 금지 (청취 피로). Track Map 시퀀스 검증 | 자동 |
| S4 | **시리즈 길이** | 60-90분 (1세션 정합 88.1%, 직장인 운동 30분-2시간 88.1% 분포) | 자동 |
| S5 | **Track 01 = 워밍업** | Track 01은 B축 멜로딕 (BPM 100-120). 텐션 점진 빌드 | 자동 |
| S6 | **마지막 2-3곡 = 멜로딕 마무리** | Track N-1 / N-2는 B + 보너스 붐뱁 (BPM 90-115). 운동 종료 후 호흡 정리 + YouTube replay 친화 | 자동 |

> **시리즈 PASS** = 6개 모두 충족. 1개라도 FAIL → Track Map 재조정 (개별 곡은 PASS면 유지, 배치만 변경)

---

## Style Checklist (수동 청취 보조)

| # | 항목 | A Dry | B Tuned | C Hardcore | D K-Drill | E 붐뱁 | 체크 |
|---|------|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | BPM 범위 정합 | 148-160 | 140-160 | 140-150 | 140-146 | 86-95 | ☐ |
| 2 | 보컬 톤 정합 | raw shouted | autotuned melodic | husky | 한국어 악센트 | raw chest | ☐ |
| 3 | 베이스 디자인 정합 | hard clipped 808 | distorted 808 portamento | deep 808 sub-bass | sliding 808 portamento | walking upright bass | ☐ |
| 4 | 드럼 패턴 정합 | 1/16 hi-hat + 32nd roll | 1/16 hi-hat + snare on 3 | rolling 1/16 hi-hat | drill snare + skippy hi-hat | dusty kick + rim shot swing | ☐ |
| 5 | 마스터링 톤 정합 | blown-out -6 LUFS | glossy -7 LUFS | gritty | dark | warm dusty | ☐ |
| 6 | EXCLUDE 정체성 보호 | no autotune | no dry shouted | no melodic singing | no amapiano | no auto-tune | ☐ |
| 7 | Korean 가창 95%+ (D 75%) | ☐ | ☐ | ☐ | ☐ (75%+) | ☐ | ☐ |
| 8 | Workout BPM 단계 분류 | 메인/HIIT | 워밍업/쿨다운/메인 | 메인/HIIT | HIIT | 쿨다운 | ☐ |

---

## 운영 워크플로우

### 곡 단위 (Suno PASS 직후)

```
1. Hard Gates 8개 검사 (자동 H6/H8 + 수동 6개)
   → 1개라도 FAIL = 재작성, 멈춤
2. Style-Specific Gates 검사 (해당 Style의 2-4개)
   → 1개라도 FAIL = 재작성
3. 8-Factor Scoring (100점)
   → 85+ PASS → tracks/ 폴더 정착
   → 70-84 BORDERLINE → 문제 Factor 수정 후 재평가
   → <70 FAIL → 재작성
4. Critical Fail (개별 Factor ≤30%) 별도 체크
```

### 시리즈 단위 (15곡+ 누적 후)

```
5. check_series_gate.sh 실행
   → S1-S6 6개 자동 검증
   → 1개라도 FAIL = Track Map 재조정 (개별 곡 PASS는 유지)
6. 전곡 PASS + 시리즈 PASS → YouTube Metadata + 패키징
```

---

## 자동화 스크립트 인터페이스

### `check_lyric_avoid.sh`

```bash
$ ./MASTER/scripts/check_lyric_avoid.sh SERIES/20-00/input/tracks/track_01.txt
PASS

$ ./MASTER/scripts/check_lyric_avoid.sh SERIES/20-00/input/tracks/track_02.txt
FAIL
  매칭 키워드: 마약 (3회: "코카인", "필로폰", "LSD")
```

### `check_series_gate.sh`

```bash
$ ./MASTER/scripts/check_series_gate.sh SERIES/20-00/
S1 곡수 분포 + Hard 60%: PASS (A:4 B:5 C:5 D:3 E:3 = 20곡 / Hard:12 Non-Hard:8)
S2 BPM 분포: PASS (워밍업:3 메인:8 HIIT:6 쿨다운:3 = 20곡)
S3 A·B 인접 회피: PASS
S4 시리즈 길이: PASS (78분 12초)
S5 Track 01 워밍업: PASS (Track 01 B축, BPM 110)
S6 마지막 2-3곡 멜로딕: PASS (Track 19 A BPM 148 — Hard 60% 보강 / Track 20 B BPM 105)

종합: PASS
```

---

## v1.0 검증 (2026-04-26 /team 만장 합의)

- **참석**: Product Leader + Marketing Director + Engineering Lead Round 1 + QA Reviewer Round 2
- **합의 점수**: 평균 94.6점, 모든 Gate 개별 PASS
- **G5 운영 효율 BORDERLINE 90**: Style Gate 13개 다소 많음 → 추후 11개 축소 옵션 (B 4→3, D 3→2). 강제 X, 운영 시 부담 발생하면 재검토
- **회의록**: `meetings/2026-04-26_20-00-genre-gate-rubric-design.md` + `meetings/2026-04-26_20-00-genre-gate-execution-plan.md`

---

## 관련 문서

| 문서 | 용도 |
|------|------|
| `SERIES/20-00/concept.md` v0.2 | Style Templates 전문 + Suno Style Prompt + EXCLUDE v3 |
| `SERIES/20-00/report/2026-04-25_workout-tuned-rage-supplement.md` | Section A 키워드 분리표 + Section B 페르소나 검증 |
| `SERIES/20-00/report/2026-04-24_hard-hiphop-4axis-musical-deep.md` | 1차 1162줄 딥리서치 (4축 음악적 디테일) |
| `MASTER/rubrics/AFROBEATS_RUBRIC.md` | 12-00 형식 참고 (Hard Gates + Style + 8-Factor) |
| `MASTER/scripts/check_lyric_avoid.sh` | 가사 회피 자동 검사 |
| `MASTER/scripts/check_series_gate.sh` | 시리즈 게이트 자동 검사 |

---

*HARD_HIPHOP_RUBRIC v1.0 — 2026-04-26 작성. /team 만장 합의 + concept.md v0.2 + 보충 리포트 통합.*
