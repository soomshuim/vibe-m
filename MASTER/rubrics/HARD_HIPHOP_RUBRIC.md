# Korean Hard Hip-Hop Rubric

Version: 1.5
Last Updated: 2026-06-03
Purpose: Korean Hard Hip-Hop · Workout 장르 게이트 (20-00 시리즈)

> **v1.5 변경 (2026-06-03 — final concept sync)**:
> 1. **현재 최종 분포 기준 보정**: `SERIES/20-00/concept.md` v0.5/v0.8 기준 A 3 / B 5 / C 5 / D 3 / E 2 / F 2 = 20곡
> 2. **Hard 65% 기준화**: A+C+D+F = 13곡 / B+E = 7곡. Hard 60%+ 정책은 충족
> 3. **Series Gate 문구 보정**: v0.6 최종 러닝 오더의 5곡 단위 강-약-중-강-약 파형과 Track 01 A 강한 시작 / Track 20 B cooldown을 현재 기준으로 반영
> 4. **Legacy harness 표시**: `MASTER/scripts/check_series_gate.sh`는 pre-final txt source draft 검증용 legacy validator이며, 현재 uploaded/source-final 상태 검증은 `python3 wavvy.py gate ...`를 우선 사용
> 5. **S2 판정 안전화**: BPM/체감 단계 정합은 legacy script에서 PASS가 아니라 ADVISORY로만 출력한다. 세부 결정은 이 문서의 **S2 Advisory Disposition**을 SSOT로 둔다.

> **v1.4 변경 (2026-04-27 — 최종 20곡 체제 복원 + 성별 분포 확정)**:
> 1. **당시 20곡 확정안**: A 3 / B 4 / C 5 / D 3 / E 2 / F 3 = 20곡 (v1.5에서 현재 concept 기준으로 보정)
> 2. **당시 Hard 70%**: A+C+D+F = 14곡 / B+E = 6곡 (v1.5 현재 기준은 Hard 65%)
> 3. **보컬 성별 분포 확정**: 남성 14곡 / 여성 6곡
> 4. **Series Gate S7 추가**: `Vocal:` 메타 기반 성별 분포 자동 검증
> 5. **최종 순서 정책**: 전곡 PASS 후 강-약-중-강-약 흐름으로 재배치

> **v1.3 변경 (2026-04-26 — 7곡 PASS 후 일괄 보정)**:
> 1. **H4 한국어 비중 룰 → 권장만 (감점 X)** — 코드스위치는 한국 본가 표준 (사용자 정정)
> 2. **메타태그 `[Bridge]` `[Pre-Chorus]` `[Chorus]` `[Final Chorus]` 인정** — 결과물 좋으면 OK (이전 v1.0 금지 룰 폐지)
> 3. **F축 신설**: Faster Dark Trap (180 BPM hub, Cold Stack 스타일)
> 4. **C축 톤 분기 4가지 명시**: husky/distorted/muddy / **lazy monotone deadpan** (v1.2) / **디스 컨셉 sarcastic** / **chant gang hook 변종**
> 5. **B축 톤 분기 명시**: melodic autotune sing-rap / **introspective laid-back** (Travis Scott Astroworld 톤)
> 6. **BPM 룰 확장**: 메인 4축 140-160 → 140-180 (F축 포함)
> 7. **사운드 우선 정책 명문화** — 가사 가중치 ↓, BPM/사운드 톤앤매너 우선 (사용자 정정 2026-04-26 "가사 내용 크게 중요하지 않아")

> **v1.2 변경 (2026-04-26)**: H5 Hook 룰 완화 (Verse 4+ 모놀리식 인정), H4 한국어 80% 완화, C1 lazy monotone 톤 분기 추가
> **v1.1 변경 (2026-04-26)**: Hard 60% 정책 (A+C+D+F = 60% / B+E = 40%)

> **Based on**:
> - `SERIES/20-00/concept.md` v0.5/v0.6/v0.8 (현행 20곡 분포, 최종 러닝 오더, uploaded 상태)
> - `SERIES/20-00/concept.md` v0.4 (20곡 체제 복원 이력. 분포 값은 v0.5 이후 보정됨)
> - `SERIES/20-00/report/2026-04-25_workout-tuned-rage-supplement.md` (Section A·B 통합)
> - `meetings/2026-04-26_20-00-genre-gate-rubric-design.md` (/team 만장 합의)
> - 7곡 PASS 사례 검증 (Rewrite·Bottom to the Top·Fake·Boomerang·Paycheck·Cold Stack·Yang Gang)
>
> **시리즈 정체성**: Korean Workout Hip-Hop 빈자리 (글로벌 Apple Music Hip-Hop Workout 외산 트랩 우세, Korean rap 0%)
> **페르소나**: 25-35 한국 직장인, 저녁 8시 운동 (헬스/PT/홈트/러닝)
> **최종 곡수 (v1.5)**: **20곡** (A 3 / B 5 / C 5 / D 3 / E 2 / F 2, Hard 13/20 = 65%, 남성 14 / 여성 6)

---

## Hard Gates (1개라도 FAIL = 재작성)

| # | Gate | 기준 | 자동/수동 |
|---|------|------|----------|
| H1 | **BPM** | 86-95 (붐뱁 E) OR **140-180** (메인 5축: A/B/C/D/F) | 수동 |
| H2 | **Drum Pattern** | 808 + 1/16 hi-hat steady (메인 5축) OR dusty kick + rim snare swing (붐뱁). Pop kick·EDM kick = FAIL | 수동 |
| H3 | **Bass** | 808 sub-bass (메인 5축) OR walking upright bass (붐뱁). Pop sub bass·EDM bass·synth pop bass = FAIL | 수동 |
| H4 | **Vocal — Korean Hard Rap** | chest voice + sharp articulation. Pop singing·falsetto·thin head voice = FAIL. **한국어 비중은 권장 (60%+)이지만 감점 X — 코드스위치는 한국 본가 표준** | 수동 |
| H5 | **Hook 존재 OR 모놀리식 Verse** | 1-2마디 반복 hook + ad-lib layer OR Verse 4+ 모놀리식 구조 OR multisyllabic punchline (붐뱁). 셋 중 하나 충족 시 PASS | 수동 |
| H6 | **EXCLUDE 공통** | EDM drop · beat switch · sung melodic chorus · k-pop 진입 = FAIL. **단 EXCLUDE Style Prompt 미명시는 경고만 (Suno 자동 처리 OK 시 PASS)** | 자동 (소프트) |
| H7 | **Workout 사운드 정합** | (1) BPM 90-180 안 / (2) 텐션 곡선 운동 단계 매칭 가능 / (3) 곡 길이 2:30-4:30 (변주 곡 길이 확장 인정). 모두 충족 = PASS | 수동 |
| H8 | **콘텐츠 회피** | 무차별 폭력·살해·총기·마약·혐오 직접 묘사 = FAIL. K-Drill 본가 어휘(갱·크루·블록·동네·디스) 회피 X. 50 키워드 5카테고리 grep | 자동 (`check_lyric_avoid.sh`) |

> **v1.3 정책 변화**:
> - **사운드 톤앤매너 우선** — H1·H2·H3·H7이 핵심 결정 게이트. H4·H5·H6는 완화 (결과물 정성 평가 우선)
> - 가사 평가는 H8 회피 영역만 강제. H4 한국어 비중·메타태그 구조는 권장만
> - **자동화 비율**: H8 자동 + H6 소프트 → 실질 수동 6개

---

## Style-Specific Gates (17개) — 7곡 PASS 사례 반영

### Style A: Rage Dry Voice — 3곡 (Hard, 베이스: Paycheck)

| # | Gate | 기준 |
|---|------|------|
| A1 | **Vocal Delivery — Dry/Shouted** | shouted / yelled / raw raw / dry voice. Style Prompt 또는 가사 메타에 `Shouted male Korean rap, dry voice` 명시 (Paycheck 패턴) |
| A2 | **Master Loudness** | brick-walled mastering 또는 raw close-mic. Polished glossy mix = B축으로 sliding 권장 |
| A3 | **Reverb** | short raw 또는 static decay |

> **참조 (글로벌)**: Playboi Carti `Whole Lotta Red` / Yeat 일부 / Ken Carson
> **Korean 토착 풀**: Loopy `MARNI` 일부 + Lil Moshpit 비트 (PUBLIC ENEMY 161 BPM)
> **Wavvy PASS 사례**: Paycheck (2026-04-26, BPM 150, "softened tight 808 + introspective" Style + "Shouted dry voice" 가사 메타 충돌이지만 결과 rage 정합)

### Style B: Rage Tuned Singing — 5곡 (Non-Hard, 신규 작성)

| # | Gate | 기준 |
|---|------|------|
| B1 | **Vocal Delivery — Tuned/Melodic** | melodic autotuned sing-rap delivery. Antares Auto-Tune retune 5-15ms 추정 |
| B2 | **Hook — Melodic Chorus** | melodic chorus 명확 (verse-chorus 구조 보존) |
| B3 | **Reverb — Cathedral** | cathedral reverb plate large hall (Travis Scott 시그니처) **OR** introspective laid-back 톤 (Don Toliver `Hardstone Psycho`) |
| B4 | **Korean KC vangdale 광택 디자인 (선택)** | mastering -7 LUFS, polished glossy mix |

> **B축 톤 분기 (v1.3)**:
> - 표준 melodic autotune sing-rap (Travis Scott Astroworld)
> - **introspective laid-back 변종** (Don Toliver `Hardstone Psycho`, "softened 808 + light mix voice + smooth legato + introspective" 톤)
>
> **참조 (글로벌)**: Travis Scott / Don Toliver / SoFaygo / Destroy Lonely
> **Korean 토착 풀**: Sik-K × HAON · Sik-K × Lil Moshpit `K-FLIP+` · MOLLAK (Female 인접)

### Style C: Hardcore Trap — 5곡 (Hard, 베이스: Bottom to the Top·Fake·Boomerang·Yang Gang)

| # | Gate | 기준 |
|---|------|------|
| C1 | **Vocal Delivery (4가지 톤 분기)** | husky/distorted/muddy **OR** lazy monotone deadpan layback **OR** confident sarcastic 디스 톤 **OR** chanty gang hook + close-mic stacked whispers. 모두 chest voice + sharp articulation 공통 |
| C2 | **Bass + Atmosphere** | deep distorted 808 sub-bass moving line + dark minor key piano stab loop / synth bell melody / heavy bass + minimal |

> **C축 4가지 톤 분기 (v1.3)**:
> 1. **husky/distorted/muddy** (표준, ZENE THE ZILLA·Ash Island·Loopy 시기)
> 2. **lazy monotone deadpan layback** (Bottom to the Top, Larry June 영향)
> 3. **confident sarcastic 디스 컨셉** (Fake·Boomerang)
> 4. **chant gang hook + close-mic stacked whispers** (Yang Gang, "halftime bounce + glitchy ear candy + stacked chant-style gang vocals" 변종)
>
> **참조**: ZENE THE ZILLA · Ash Island · Loopy (UNWANTED WRLD) · EK · KWAII

### Style D: K-Drill 액센트 — 3곡 (Hard, 베이스: Rewrite)

| # | Gate | 기준 |
|---|------|------|
| D1 | **Bass — Sliding 808 Portamento** | sliding 808 bass with portamento glide (UK/NY/Brooklyn Drill 시그니처) |
| D2 | **Drum — Drill Snare + Tresillo** | drill snare with skippy hi-hat patterns / tresillo 3+3+2 polyrhythm hi-hat |
| D3 | **본가 무드 보존** | 한국어 된소리/거센소리(ㄲ ㄸ ㅃ ㅋ ㅌ) 악센트 + dark minor key piano/flute melody. 가사 자유 (디스·반항·도시·자기 서사) |

> **참조**: Fleeky Bang · Blase · Silkybois · deadbois · NO:EL
> **Wavvy PASS 사례**: Rewrite (2026-04-26, BPM 140, NY/Brooklyn drill hybrid, tresillo hi-hats, D minor, 90점)

### Style E: 빡센 붐뱁 (Bonus) — 2곡

| # | Gate | 기준 |
|---|------|------|
| E1 | **Drum — Dusty + Walking Bass** | dusty drums with vinyl crackle texture + walking upright bass + rim-shot snare + head-nod swing |
| E2 | **Lyricism — 다음절 라임** | dense multisyllabic rhyme + 90s East Coast vernacular + 한국어 vernacular |

> **참조**: 가리온 · Deepflow · Huckleberry P · Paloalto · Kid Milli · QM · 다이나믹 듀오
> **Wavvy PASS 사례**: 없음 (변주 6곡에서 1곡 신규 작성 예정)

### Style F: Faster Dark Trap (신규 v1.3) — 2곡 (Hard, 베이스: Cold Stack + Black Mirror)

| # | Gate | 기준 |
|---|------|------|
| F1 | **BPM 165-180** | 메인 4축 표준 140-160 초과 영역. HIIT 운동 단계 직격 |
| F2 | **Drum — Triplet/Stutter Hi-hat** | rolling 808 + ultra-tight triplet and stuttered hi-hats + punchy snares. double-time/triple-time bursts 인정 (drop으로 안 가는 한) |
| F3 | **Hook — Stacked Chant Gang Vocals** | stacked chant-style gang vocals on hook + Korean-English bilingual rap |

> **참조 (글로벌)**: Playboi Carti `Music` (2025) 일부 + Yeat 빠른 트랙
> **Wavvy PASS 사례**: Cold Stack (2026-04-26, BPM 180, "Even faster dark trap, rolling 808, triplet hi-hats, stacked chant gang vocals" — 신규 축으로 인정)

---

## 8-Factor Scoring (100점)

| # | Factor | 배점 | 기준 | 레퍼런스 |
|---|--------|------|------|---------|
| F1 | **Trap Groove** | 15 | 808 + 1/16 hi-hat steady, locked drum pattern. 붐뱁은 dusty kick + swing groove | concept.md §Style Templates |
| F2 | **808/Bass** | 10 | 베이스 디자인 (distorted/sliding/portamento), 킥과 sync, 저음 임팩트 | Section A.2.2 |
| F3 | **Hook & Ad-libs** | 15 | 1-2마디 hook + ad-lib stack 밀도 OR 모놀리식 Verse 4+ OR multisyllabic punchline | Section A.3 |
| F4 | **Korean Vocal Identity** | 15 | Suno 한국어 발음 명료도 + 보컬 톤 정합 (5축별). **음성·발음·톤만 평가, 가사 내용 평가 X** | concept.md §Style Templates 보컬 디스크립터 |
| F5 | **Energy Arc** | 10 | Verse → Hook 텐션 빌드, drop 없이도 텐션 유지 | concept.md §LYRICS 가이드 |
| F6 | **Workout BPM 단계 매칭** | 10 | 워밍업 100-120 / 메인 130-150 / HIIT 140-180 / 쿨다운 90-110 분류 | concept.md §Workout 배치 룰 |
| F7 | **Production** | 15 | 믹스 분리, 보컬 포워드, 마스터링 톤 (5축별 + 톤 분기). EQ·리버브·압축 적정성 | Section A.2 |
| F8 | **장르 정체성 (5축 정합)** | 10 | Hard Hip-Hop으로 인식 + 시리즈 5축 + 보너스 6종 중 정확히 1개에 매칭 | 종합 판단 |

---

## 판정

| 점수 | 판정 | 액션 |
|------|------|------|
| 85+ | **PASS** | 진행 |
| 70-84 | **BORDERLINE** | 문제 Factor 수정 후 재평가 |
| <70 | **FAIL** | 재작성 |

**CRITICAL FAIL**: 개별 Factor ≤ 배점의 30% = 즉시 FAIL

> **v1.3 정책**: **결과물 정성 평가 우선**. 사용자가 "결과물 만족"이라 판정하면 RUBRIC 점수와 무관하게 PASS 가능. 단 H1·H2·H3·H7 (사운드 핵심 4개) 위반 시 사운드 정합성 명시적 검토 필요

---

## Series Gates (7개) — 시리즈 단위 자동/수동 검증 (v1.5 20곡 기준)

| # | Gate | 기준 | 자동/수동 |
|---|------|------|----------|
| S1 | **곡수 분포 + Hard 60%** | **A 3 / B 5 / C 5 / D 3 / E 2 / F 2 = 20곡 확정** + **Hard(A+C+D+F)=13곡(65%)** + **Non-Hard(B+E)=7곡(35%)**. Hard 60%+ 충족 | 자동 |
| S2 | **BPM/체감 단계 정합** | 워밍업/메인/HIIT/쿨다운 단계는 BPM, 장르, 질감, 체감 속도를 종합해 판단한다. Legacy numeric count는 참고만 하며 단독 FAIL 금지 | 수동/반자동 |
| S3 | **장르 완충 파형** | 5곡 단위 강-약-중-강-약 러닝 오더를 유지하고, 각 wave에 B/E 완충 지점을 둔다 | 수동/반자동 |
| S4 | **시리즈 길이** | **60-90분** (20곡 기준, 곡당 평균 3:00-4:30) | 자동 |
| S5 | **Opener/Closer 체감 정합** | Track 01은 A축 강한 시작, Track 20은 B축 108 BPM melodic cooldown | 자동/수동 |
| S6 | **마지막 2-3곡 = 멜로딕 마무리** | 마지막 2-3곡 중 하나는 B 또는 E + BPM 90-115 | 자동 |
| S7 | **보컬 성별 분포** | 최종 20곡 기준 Male 14 / Female 6. 모든 트랙 `Vocal:` 메타 필요 | 자동 |

---

### S2 Advisory Disposition (SSOT)

- **검증 대상**: 20곡 러닝 오더가 워밍업 -> 메인 -> HIIT/피크 -> 쿨다운의 실제 운동 체감 에너지 곡선을 만드는지 확인한다.
- **상태**: 수동 검토 항목으로 영구 이관한다.
- **근거**: `SERIES/20-00/concept.md` v0.6은 사운드 포지셔닝을 BPM 숫자만이 아니라 장르, 질감, 체감 속도까지 종합해 판단한다고 명시한다. Legacy `check_series_gate.sh`는 txt 메타의 숫자와 Type만 읽으므로 이 품질을 자동 PASS/FAIL로 확정할 수 없다.
- **처리 기한**: 신규 또는 pre-final 시리즈에서는 final series PASS, upload-ready, reupload 중 가장 이른 단계 전에 수동 검토를 완료한다. 이미 uploaded 상태인 20-00은 `rubric_unverified_after_finalize`를 해소하거나 재패키징/재업로드를 수행하기 전에 수동 검토를 완료한다.
- **소유권**: 판정 기준 SSOT는 이 섹션이다. 실행 소유자는 `MASTER/MANAGER.md`의 Quality Gatekeeper 역할이며, 근거 입력은 `SERIES/20-00/concept.md` Track Map과 청취/리뷰 기록이다.
- **Legacy script 동작**: `MASTER/scripts/check_series_gate.sh`는 S2를 `ADVISORY`로만 출력하고 hard gate PASS/FAIL 개수에 포함하지 않는다.

---

## Style Checklist (수동 청취 보조, v1.4 5축+1보너스)

| # | 항목 | A Dry | B Tuned | C Hardcore | D K-Drill | E 붐뱁 | F Faster | 체크 |
|---|------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | BPM 범위 | 148-160 | 140-160 | 140-150 | 140-146 | 86-95 | 165-180 | ☐ |
| 2 | 보컬 톤 | shouted dry | autotuned melodic / introspective | husky / lazy / sarcastic / chant | 한국어 악센트 | raw chest | bilingual + chant | ☐ |
| 3 | 베이스 | hard clipped 808 | distorted 808 portamento / softened tight 808 | deep 808 sub-bass | sliding 808 portamento | walking upright bass | rolling 808 | ☐ |
| 4 | 드럼 패턴 | 1/16 hi-hat | 1/16 hi-hat + snare on 3 | rolling 1/16 hi-hat | drill snare + tresillo | dusty kick + rim shot | triplet/stutter hi-hat | ☐ |
| 5 | 마스터링 톤 | blown-out -6 LUFS | glossy -7 LUFS / introspective | gritty / lazy / minimal | dark | warm dusty | high-contrast | ☐ |
| 6 | EXCLUDE 정체성 보호 | no autotune | no dry shouted | varies (4 톤 분기) | no amapiano | no auto-tune | varies | ☐ |
| 7 | Korean 가창 (권장만) | 60%+ | 60%+ | 60%+ | 60%+ (D는 50%+) | 80%+ | 50%+ | ☐ |
| 8 | Workout BPM 단계 | 메인/HIIT | 워밍업/쿨다운/메인 | 메인/HIIT | HIIT | 쿨다운 | HIIT | ☐ |

---

## 운영 워크플로우

### 곡 단위 (Suno PASS 직후)

```
1. Hard Gates 8개 검사 (자동 H8 + 소프트 H6 + 수동 6개)
   → 1개라도 FAIL = 재작성
   → 단 H4 한국어 비중·메타태그 구조는 권장만 (감점 X)
2. Style-Specific Gates 검사 (해당 Style의 2-4개)
   → 1개라도 FAIL = 재작성
3. 8-Factor Scoring (100점)
   → 85+ PASS / 70-84 BORDERLINE / <70 FAIL
4. **결과물 정성 평가 우선** — 사용자 판정이 RUBRIC 점수보다 우선
5. PASS 시 tracks/ 폴더 정착 + Type 메타 라벨링 (A/B/C/D/E/F)
```

### 시리즈 단위 (10곡+ 누적 후)

```
6. 현재 state/gate 실행
   → `python3 wavvy.py state SERIES/20-00 --check --json`
   → `python3 wavvy.py gate SERIES/20-00 --stage uploaded --json`
7. pre-final txt source draft 상태에서만 legacy `check_series_gate.sh` 보조 실행
   → S2 판정은 이 문서의 `S2 Advisory Disposition`을 따른다
   → S3/S5는 현재 v0.6 final concept와 일부 수동 판단이 필요
8. 전곡 PASS + 시리즈 PASS → YouTube Metadata + 패키징
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

### `check_series_gate.sh` (legacy pre-final, v1.5 기준 일부 동기화)

> **Legacy note:** 이 shell validator는 `input/tracks/*.txt`가 살아 있는 pre-final draft 단계 보조 도구다. `finalize-upload` 이후 txt가 삭제되고 `concept.md > Final Track Sources`가 SSOT가 된 상태에서는 `python3 wavvy.py state/gate`를 우선한다.

```bash
$ ./MASTER/scripts/check_series_gate.sh SERIES/20-00/
S1 곡수 분포 + Hard 60%: PASS (A:3 B:5 C:5 D:3 E:2 F:2 = 20곡 / Hard:13 Non-Hard:7 = 65%)
S2 BPM/체감 단계 정합: ADVISORY (legacy numeric count only; manual check required)
S3 장르 완충 파형: PASS
S4 시리즈 길이: PASS (74분 00초)
S5 Opener/Closer 체감 정합: PASS (Track 01 A축 강한 시작 / Track 20 B축 108 BPM cooldown)
S6 마지막 2-3곡 멜로딕: PASS (Track 20 B BPM 108)
S7 보컬 성별 분포: PASS (Male:14 Female:6 Unknown:0 = 20곡)

종합: PASS
```

---

## v1.3 검증 (2026-04-26 — 7곡 PASS 사례 + 사용자 정정 통합)

**7곡 PASS 사례 RUBRIC 정합성 후행 검증**:
| # | 곡 | Style | BPM | 매칭 | RUBRIC v1.3 PASS 여부 |
|---|------|------|:---:|------|:----:|
| 1 | Rewrite | D K-Drill | 140 | NY/Brooklyn drill | ✅ |
| 2 | Bottom to the Top | C lazy | 150 | lazy monotone | ✅ (C1 톤 분기 추가로) |
| 3 | Fake | C 디스 | 140 | sarcastic 디스 | ✅ (C1 톤 분기 추가로) |
| 4 | Boomerang | C 디스 | 150 | sarcastic 디스 | ✅ |
| 5 | Paycheck | A Dry | 150 | shouted dry | ✅ (가사 메타 우선) |
| 6 | Cold Stack | F Faster | 180 | rolling 808 + triplet | ✅ (F축 신설) |
| 7 | Yang Gang | C chant | 150 | halftime + chant gang | ✅ (C1 chant 톤 분기) |

**보정 사항**:
- v1.0/v1.1: 7곡 중 **0곡 통과** (한국어 95% 룰·메타태그 금지·Hook 룰·Style Gate 부족)
- v1.2: 7곡 중 **1-2곡 borderline**
- v1.3: 7곡 중 **7곡 모두 PASS** (사용자 결과물 평가와 일치)

---

## 관련 문서

| 문서 | 용도 |
|------|------|
| `SERIES/20-00/concept.md` v0.4 | 20곡 분포 + 남성 14 / 여성 6 + 13곡 작업 세트 + 추가 7곡 슬롯 |
| `SERIES/20-00/report/2026-04-25_workout-tuned-rage-supplement.md` | Section A 키워드 분리표 + Section B 페르소나 검증 |
| `SERIES/20-00/report/2026-04-24_hard-hiphop-4axis-musical-deep.md` | 1차 1162줄 딥리서치 |
| `MASTER/rubrics/AFROBEATS_RUBRIC.md` | 12-00 형식 참고 |
| `MASTER/scripts/check_lyric_avoid.sh` | 가사 회피 자동 검사 |
| `MASTER/scripts/check_series_gate.sh` | legacy pre-final txt source draft 보조 검사 (현재 uploaded/source-final 검증은 `wavvy.py state/gate` 우선) |
| 메모리 `feedback_wavvy-lyrics-vs-sound-separation.md` | 가사 vs 사운드 분리 룰 |

---

*HARD_HIPHOP_RUBRIC v1.5 — 2026-06-03 보정. 20-00 final concept v0.5/v0.8 분포 + uploaded state gate 우선순위 반영.*
