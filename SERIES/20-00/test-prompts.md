# 20-00 🌃 AFTER HOURS — Suno 1차 테스트 프롬프트 (4축 × 1곡)

> 생성일: 2026-04-25 | Suno V5.5 | 목적: 4축 Style Template 품질 검증 → 20곡 확장 가부 결정
> 업데이트 2026-04-25: 곡 1(Paycheck) / 곡 2(Rewrite)는 Suno 샘플 PASS 가사 재활용 (Custom Mode 풀 가사 입력). 곡 3(Come Up) / 곡 4(Paranoia)는 작사 프롬프트 테스트.

**테스트 전략:**
1. 각 프롬프트로 **Suno에서 2-3회 생성** → 가장 좋은 것 선택
2. 축별 시그니처 사운드 확인 (Rage=왜곡 808+bell / Drill=sliding 808 / Boom bap=샘플+MPC swing / Hard Trap=dark 808 서스테인)
3. 한국어 발음 명료도 / 보컬 톤 / 장르 충실도 체크
4. PASS 시 Style Template 확정, FAIL 시 프롬프트 튜닝

---

## 🔥 테스트 곡 1 — Style A (Rage) `Paycheck`

**제목**: `Paycheck` (한글: `불붙은 paycheck`) — Suno 원본 + Claude Verse 6 확장 버전
**컨셉**: 허슬 → 의심 극복 → 크루/자립 → 반격/증명 → 상승/지속 → 최종 선언 6단 서사
**가사 파일**: `input/tracks/불붙은 paycheck (Paycheck on Fire).txt`
**구조**: Intro → V1 → Refrain① → V2 → V3 → Refrain② → V4 → V5 → Refrain③ → V6 → Outro (Refrain 3번, V6 뒤 Outro 직행 — final drop 유도 차단)

### Style Prompt
```
Korean rage trap, 150 BPM, distorted 808 bass with pitch slides hard clipped, bright bell lead synth, supersaw 7-voice detuned sustained stab, pitched-up vocal chop sample top layer, rolling 1/16 hi-hats with 32nd triplet burst, pitched-up screamed male rap vocal, high density ad-lib layer, mosh pit energy aggressive, raw lo-fi saturation master loud, locked drum pattern throughout no fills no switch-up, hard rap only no singing, no arp synth no stutter loop, rapping in Korean, sharp articulation
```

### EXCLUDE
```
k-pop, melodic singing, four-on-the-floor, drum fill, double-time switch, sung hook, arpeggiated synth, electronic riser, synth FX, EDM FX
```

### LYRICS (Suno Custom Mode 풀 가사 입력 — Verse 6 확장)
```
[Intro]
(Instrumental, same 2-bar drum loop)

[Verse 1]
(Shouted male Korean rap, dry voice, same drum loop)
새벽부터 hustle, I don't sleep
손에 번진 ink, got receipts
한 장 더 쌓아, keep it neat
너네 말은 too cheap, 내 발은 street

가방엔 꿈이랑 bills and plans
밑바닥에서 we made our stance
웃음은 짧게, 내 눈은 cash
한 번 더 밀어, no second chance

[Refrain]
(Shouted rap refrain, dry voice, same drum loop)
불붙은 paycheck, make it stack
불붙은 paycheck, never back
우린 올라가, no lag, no cap
불붙은 paycheck, on the map

[Verse 2]
(Shouted male Korean rap, dry voice, same drum loop)
네가 던진 doubt, I threw it back
발끝엔 grind, in my backpack
밤새워 써, then I attack
꿈이 내 code, I don't lack

형, 나 좀 봐, I came from dust
지갑은 light but the will is tough
한 글자씩 쌓아, trust the rush
끝까지 가, yeah, that's enough

[Verse 3]
(Shouted male Korean rap, dry voice, same drum loop)
내 형제들, tied by fire
한 놈도 안 비어, we go higher
손 맞잡으면, 더 entire
등 뒤를 믿어, 우리 wire

진흙에서 쌓아, built my own
땀으로 박았어, 이건 stone
혼자서 걸었지, never thrown
이 길 끝까지, fully grown

[Refrain]
(Shouted rap refrain, dry voice, same drum loop)
불붙은 paycheck, make it stack
불붙은 paycheck, never back
우린 올라가, no lag, no cap
불붙은 paycheck, on the map

[Verse 4]
(Shouted male Korean rap, dry voice, same drum loop)
비웃던 입들, 이젠 just drop
멈춤 없는 engine, 난 non-stop
한 발 더 디뎌, top of top
수많은 얼굴들, 이젠 prop

새긴 이름은, black on white
어둠 속에서, I see light
한 번 잡으면, gone too tight
끝까지 밀어, that's my fight

[Verse 5]
(Shouted male Korean rap, dry voice, same drum loop)
아직 끝 아냐, just halfway
새벽마다 시작, I pave my way
말 대신 action, that's what I say
하루도 안 쉬어, every day

이름 뒤에 brand, built from chest
거친 길 뚫어, passed every test
안 눕는 나, can't take rest
매일 깊어져, I'm my best

[Refrain]
(Shouted rap refrain, dry voice, same drum loop)
불붙은 paycheck, make it stack
불붙은 paycheck, never back
우린 올라가, no lag, no cap
불붙은 paycheck, on the map

[Verse 6]
(Shouted male Korean rap, dry voice, same drum loop)
paycheck 불붙어, 계속 burn
매일 한 걸음, my own turn
지나온 발자국, well earned
아직 갈 길 멀어, more to learn

새벽부터 밤까지, on the grind
어둠을 뚫어, 내 빛 shine
지나온 길은, 100% mine
다시 go, one more time

[Outro]
(Instrumental fade, same 2-bar drum loop)
```

### 체크포인트
- [ ] BPM 140-160 범위
- [ ] 왜곡 808 + bell lead 선명
- [ ] 훅 `불붙은 paycheck` 반복성 + 한국어 버스 자연스러움
- [ ] Pitched-up 보컬 적용
- [ ] 애드립 밀도
- [ ] **전체 길이 2:30 이상** (Verse 6 확장 효과 검증)
- [ ] Refrain 3회 모두 동일 에너지 유지 (마지막 Refrain 이후 Outro 직행, final drop 없음)
- [ ] V3(크루) / V4(반격) / V5(상승) / V6(최종) 서사 구분 가능

---

## 🔪 테스트 곡 2 — Style B (K-Drill) `Rewrite`

**제목**: `Rewrite` (한글: `씬에 침 뱉어`) — Suno 샘플 PASS 가사 재활용
**컨셉**: 씬 디스 · 가짜 vs 진짜 · 판 뒤집기 · 한국 슬랭 직격
**가사 파일**: `input/tracks/씬에 침 뱉어 (Spit on the Scene).txt`

### Style Prompt
```
NY drill, Brooklyn drill hybrid, 140 BPM, sliding 808 bass portamento long notes, flipped soul sample melodic hook pitched-up chop, sharp tresillo hi-hats 3+3+2 polyrhythm, snare on beat 4 off-beat with reverb tail, dark orchestral strings cinematic piano loop D minor, menacing atmosphere, aggressive guttural male rap deadpan flow, locked drum pattern throughout no fills no switch-up, hard rap only no singing, no arp synth no stutter loop, rapping in Korean, crisp articulation
```

### EXCLUDE
```
k-pop, melodic singing, four-on-the-floor, drum fill, double-time switch, sung hook, arpeggiated synth, electronic riser, synth FX, EDM FX
```

### LYRICS (Suno Custom Mode 풀 가사 입력)
```
[Verse 1]
씬에 발 담근 척, 니 꼴 좀 봐
겉만 번지르르, 속은 다 가짜
난 말 안 섞어, 네 냄새는 trash
입만 터는 kid, 손은 늘 mash

니 crew는 구멍, 다 새는 비밀
난 빡세게 달려, 눈빛은 lethal
너흰 hype만 좇아, 금방 식어
난 여기서 살아, 매 장면 찢어

건들면 바로 back, 넌 겁나지
허세로만 버텨, 결국에 꺾이지
내 혀는 razor, 네 이름은 stain
판 뒤집는 순간, 기억해 my name

[Pre-Hook]
들어와 봐, feel the tension
네 입 닫아, no permission
한 번 더 봐, 이 scene is mine
니 얕은 폼은 다 out of line

[Hook]
씬에 침 뱉어, 씬에 침 뱉어
너흰 다 fake, 씬에 침 뱉어
씬에 침 뱉어, 씬에 침 뱉어
난 안 비켜, 씬에 침 뱉어

[Verse 2]
너의 자랑거리? 다 남의 말
복붙한 swag, 완전 밑천 탈탈
난 골목 끝까지, 발자국 박아
네가 쌓은 체면, 한 번에 박살

X on my chest, 난 표식처럼
네 편한 룰은 다 깨져버려
말 돌리지 마, 직진이 답
난 한 번 치고, 다시 또 slap

니 팬들 앞에서도 숨지 못해
표정 다 굳어, 손끝이 떨려
I do it raw, you do it for likes
난 진짜로 와, 넌 그냥 likes

[Pre-Hook]
들어와 봐, feel the tension
네 입 닫아, no permission
한 번 더 봐, 이 scene is mine
니 얕은 폼은 다 out of line

[Hook]
씬에 침 뱉어, 씬에 침 뱉어
너흰 다 fake, 씬에 침 뱉어
씬에 침 뱉어, 씬에 침 뱉어
난 안 비켜, 씬에 침 뱉어

[Final Hook]
씬에 침 뱉어, 씬에 침 뱉어
너흰 다 fake, 씬에 침 뱉어
씬에 침 뱉어, 씬에 침 뱉어
난 안 비켜, 씬에 침 뱉어
```

### 체크포인트
- [ ] BPM 138-145 범위
- [ ] Sliding 808 portamento 선명
- [ ] 3+3+2 tresillo hi-hat 패턴
- [ ] Snare off-beat
- [ ] Menace 톤 + deadpan delivery
- [ ] 한국어 된소리 악센트 (꼴 / 꺾이지 / 뒤집는)
- [ ] 훅 `씬에 침 뱉어` 반복성

---

## 📼 테스트 곡 3 — Style C (모던 하드코어 붐뱁) `Come Up`

**제목**: `Come Up` (한글: `올라와`)
**컨셉**: 바닥에서 올라오는 서사 · 밤 그라인드 · 펜에서 마이크까지 · 한국 거리에서 무대까지
**가사 방향**: Suno 작사 프롬프트 테스트 (자체 생성)

### Style Prompt
```
modern hardcore boom bap, 한국 힙합, 90 BPM, chopped 70s-80s soul or ballad sample loop with vinyl crackle, dusty drum break MPC swing 58%, warm upright bass, acoustic kick snappy snare rim shot DJ scratches, confident lyrical male rap chest voice multi-syllable rhymes, analog saturation head-nodding groove, locked drum pattern throughout no fills no switch-up, hard rap only no singing, no arp synth no stutter loop, rapping in Korean, articulation
```

### EXCLUDE
```
trap, melodic singing, four-on-the-floor, drum fill, double-time switch, sung hook, arpeggiated synth, electronic riser, synth FX, EDM FX
```

### LYRICS 프롬프트 (작사 지시 포맷)
```
I-V1-H-V2-H-V3-O
modern Korean boom bap rap lyrics. Korean heavy 95 percent. dense multi-syllable internal rhymes. about come up from the bottom, night grind pen to mic, Korean street to stage, hustle scars and self-made story, chest voice confident lyrical flow, hook Come Up two bars repeat, no bridge.
```

### 체크포인트
- [ ] BPM 86-95 범위 (90 BPM 중심)
- [ ] 샘플 loop + 더스티 드럼
- [ ] MPC swing 느낌 (58%)
- [ ] Vinyl crackle 질감
- [ ] 다음절 라임 + 내재 라임 밀도
- [ ] Chest voice + 명료한 발음
- [ ] 평균 라인 12-18 음절 밀도
- [ ] 훅 `Come Up` 반복성 + 자서전 서사 성립

---

## 🌑 테스트 곡 4 — Style D (하드코어 트랩 젊은 씬) `Paranoia`

**제목**: `Paranoia` (한글: `편집`)
**컨셉**: 편집증 · 불신 · 밤의 그림자 · 거리 코드 · 아무도 믿지 않는다
**가사 방향**: Suno 작사 프롬프트 테스트 (자체 생성)

### Style Prompt
```
Korean dark hardcore trap, 142 BPM, heavy 808 bass sustain decay sidechained to kick slight distortion, punchy kick fast hi-hat triplet rolls minimal clap on 3, dark atmospheric synth pad muted electric guitar chord minor key, dark pitched vocal sample loop minor key, melancholic trap rap husky male rap vocal high-speed flow, dark tonal balance compressed master, locked drum pattern throughout no fills no switch-up, hard rap only no singing, no arp synth no stutter loop, rapping in Korean, sharp articulation
```

### EXCLUDE
```
melodic singing, k-pop, four-on-the-floor, drum fill, double-time switch, sung hook, arpeggiated synth, electronic riser, synth FX, EDM FX
```

### LYRICS 프롬프트 (작사 지시 포맷)
```
I-V1-PH-H-V2-PH-H-O
Korean dark hardcore trap rap lyrics. perfect rhyme mix Korean with English. about paranoia at night shadows behind me trust no one street code never lost watching my back, husky melancholic delivery high-speed flow, English chant hook PARANOIA four lines, no bridge, minimal Skrrt ad-lib.
```

### 체크포인트
- [ ] BPM 140-150 범위 (142 BPM 중심)
- [ ] 808 서스테인 + 사이드체인
- [ ] 다크 패드 + 미니 피아노 모티프
- [ ] Husky/멜랑콜릭 male 보컬
- [ ] 고속 플로우 + 명료도
- [ ] Ad-lib 미니멀 (`Skrrt!` 1회만)
- [ ] 훅 `PARANOIA` 반복성 + 불신 서사

---

## 🎯 1차 테스트 종료 기준

4곡 모두 생성 완료 후:

1. **장르 충실도** — 각 축 시그니처 사운드가 명확한가?
2. **한국어 발음** — 명료한가? Romanized 섞임 없는가?
3. **보컬 톤** — Male chest voice인가? Female/Airy 섞이지 않았는가?
4. **BPM 정확도** — 프롬프트 명시 BPM과 실제 생성 BPM 일치 (Tunebat 측정)
5. **믹스 품질** — 레벨 적정 (-12~-7 LUFS), 왜곡 의도한 곳만 왜곡
6. **Wavvy DNA 호환** — Articulation, Chest voice 유지

**3개 이상 PASS** → Style Template 확정 → 20곡 확장 진행
**3개 미만 PASS** → 프롬프트 튜닝 → 재테스트

---

## 프롬프트 튜닝 가이드 (FAIL 시 대응)

### 공통 FAIL 패턴

| 증상 | 원인 | 수정 |
|-----|-----|-----|
| K-pop 드리프트 | `k-pop` EXCLUDE 누락 | EXCLUDE 추가 |
| 멜로딕 싱잉 섞임 | `melodic singing` EXCLUDE 누락 | EXCLUDE 추가 |
| 테크노 쿵짝 변주 (4/4 킥) | `four-on-the-floor` 드리프트 | EXCLUDE `four-on-the-floor` 추가 |
| 중간 드럼 빨라짐 (쪼개기 격상) | drum fill / double-time switch 삽입 | EXCLUDE `drum fill, double-time switch` + Style Prompt `locked drum pattern throughout no fills no switch-up` |
| 훅이 노래로 빠짐 (rapping in Korean + melodic singing EXCLUDE 있음에도) | `male vocal` 단어가 singing 유도 / `rap` 밀도 부족 | `male vocal` → `male rap vocal` + Style Prompt `hard rap only no singing` + EXCLUDE `sung hook` |
| 중간 전자 반복 효과 (아르페지오/스터터) | `arpeggio` / `staccato loop` 키워드가 반복 유도 | `arpeggio` → `chord`, `staccato loop` → `sustained stab` + Style Prompt `no arp synth no stutter loop` + EXCLUDE `arpeggiated synth` |
| Bridge에서 노래로 변주 | `[Bridge]` 메타태그가 섹션 변화 유도 | Bridge 섹션 제거 (4축 전부) + 약칭 구조 `B` 제거 |
| Chorus가 노래로 빠짐 (메타태그 레벨) | `[Chorus]` / `[Pre-Chorus]` 태그가 노래 유도 | `[Hook]` / `[Pre-Hook]`로 교체 (약칭 `H` / `PH`) |
| 섹션 전환 sweep/riser / EDM FX 삽입 | synth 효과음 드리프트 | EXCLUDE `electronic riser, synth FX, EDM FX` 추가 |
| 영어 vocal 섞임 | `rapping in Korean` 위치 앞쪽 | 프롬프트 맨 뒤로 이동 |
| BPM 빗나감 | BPM 태그 뒤쪽 | 장르 태그 바로 뒤로 |
| Auto-tune 과다 (Style C 붐뱁) | 태그 순서 문제 | `no auto-tune` 명시 추가 |
| Female vocal 섞임 | 보컬 태그 불명확 | `male rap` 강조 |

### 축별 특화 FAIL 대응

**Style A Rage 멜로딕 드리프트** → `distorted` `aggressive` `screamed` 앞쪽 배치
**Style B Drill 밝아짐** → `dark` `menacing` `minor key` 강조 / BPM 정확 명시
**Style C Boom bap 트랩 드리프트** → EXCLUDE에 `trap, 808` 필수
**Style D Hard Trap Rage 드리프트** → `sustain` `decay` (slide 반대) 강조

---

*테스트 결과 기록은 `report/2026-04-XX_suno-test-round1.md`에 남길 것.*
