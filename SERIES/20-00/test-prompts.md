# 20-00 🌃 AFTER HOURS — Suno 1차 테스트 프롬프트 (4축 × 1곡)

> 생성일: 2026-04-25 | Suno V5.5 | 목적: 4축 Style Template 품질 검증 → 20곡 확장 가부 결정

**테스트 전략:**
1. 각 프롬프트로 **Suno에서 2-3회 생성** → 가장 좋은 것 선택
2. 축별 시그니처 사운드 확인 (Rage=왜곡 808+bell / Drill=sliding 808 / Boom bap=샘플+MPC swing / Hard Trap=dark 808 서스테인)
3. 한국어 발음 명료도 / 보컬 톤 / 장르 충실도 체크
4. PASS 시 Style Template 확정, FAIL 시 프롬프트 튜닝

---

## 🔥 테스트 곡 1 — Style A (Rage)

**가칭**: `ESCAPE` (퇴근 직후 점화)
**컨셉**: 사무실 문 닫자마자 몸이 튕겨나가는 해방감, 고속도로 질주

### Style Prompt (약 200자)
```
Korean rage trap, 150 BPM, distorted 808 bass with pitch slides hard clipped, bright bell lead synth, supersaw 7-voice detuned short staccato loop, rolling 1/16 hi-hats with 32nd triplet burst, pitched-up screamed male vocal, high density ad-lib layer, mosh pit energy aggressive, raw lo-fi saturation master loud, singing in Korean, sharp articulation
```

### EXCLUDE
```
k-pop, melodic singing, slow ballad
```

### LYRICS 프롬프트 (~180자, 한국어 가사 생성 가이드)
```
[Intro]
(Yuh!) (What!)

[Hook]
숨 막히는 하루 끝에 질러 ESCAPE
밤이 열리는 소리 내 엔진 ESCAPE
가라 가라 가라 가라
이 밤이 내 거야 ESCAPE

[Verse]
빌딩 창문 꺼지면 내가 켜져
아스팔트 튕기는 심장 박자
(Slatt!) (Huh!)
이 네온이 날 끌어당겨
오늘만 내 차선 내가 점령

[Hook]
(반복)

[Outro]
(cut)
```

### 체크포인트
- [ ] BPM 140-160 범위
- [ ] 왜곡 808 + bell lead 선명
- [ ] 영어 훅 `ESCAPE` + 한국어 버스 혼합 자연스러움
- [ ] Pitched-up 보컬 적용
- [ ] 애드립 밀도

---

## 🔪 테스트 곡 2 — Style B (K-Drill)

**가칭**: `BLOCK` (우리 동네 · 지역 프라이드)
**컨셉**: 자기 구역 인정 요구, 위협 톤, 한국적 비유(지역번호·음식)

### Style Prompt (약 200자)
```
NY drill, Brooklyn drill hybrid, 140 BPM, sliding 808 bass portamento long notes, sharp tresillo hi-hats 3+3+2 polyrhythm, snare on beat 4 off-beat with reverb tail, dark orchestral strings cinematic piano loop D minor, menacing atmosphere, aggressive guttural male rap deadpan flow, singing in Korean, crisp articulation
```

### EXCLUDE
```
k-pop, melodic singing, bright
```

### LYRICS 프롬프트 (~190자)
```
[Intro]
(Grr!) (Bow!)
우리 동네 02

[Verse 1]
신호등 꺼지면 내 구역 시작
(Pow!)
야식 트럭 연기 올라 하늘 막고
(Gang!)
떡볶이 김처럼 내 숨 뱉어
너네 눈빛 흔들리면 그게 끝

[Hook]
BLOCK BLOCK BLOCK 02
내 구역 내 땅 우리 동네
BLOCK BLOCK BLOCK 02
잠깐 들러도 빈손 못 가

[Verse 2]
대로변 네온 내 이름 부르고
지하철 막차도 날 기다려
이 도시 내 이름 새기고
밤마다 반복 같은 얘기

[Hook]
(반복)

[Bridge]
(Grr!) 02 gang
(Bow!) 02 gang

[Outro]
(cut)
```

### 체크포인트
- [ ] BPM 138-145 범위
- [ ] Sliding 808 portamento 선명
- [ ] 3+3+2 tresillo hi-hat 패턴
- [ ] Snare off-beat (2마디당 4박)
- [ ] Menace 톤 + deadpan delivery
- [ ] 한국어 된소리 악센트
- [ ] `(Grr!)` `(Bow!)` `(Pow!)` `(Gang!)` 애드립 작동

---

## 📼 테스트 곡 3 — Style C (모던 하드코어 붐뱁)

**가칭**: `CLOCK OUT` (퇴근 자전 서사)
**컨셉**: 퇴근길 자기 응시, 회사 생활 관찰, 막차 · 한강 · 고시원 레퍼런스

### Style Prompt (약 200자)
```
modern hardcore boom bap, 한국 힙합, 90 BPM, chopped Korean soul sample loop, dusty drum break MPC swing 58%, vinyl crackle warm upright bass, acoustic kick snappy snare rim shot DJ scratches, confident lyrical male rap chest voice multi-syllable rhymes, analog saturation head-nodding groove, singing in Korean, articulation
```

### EXCLUDE
```
trap, 808, auto-tune
```

### LYRICS 프롬프트 (~195자)
```
[Intro]
(샘플 loop 4 bars)

[Verse 1]
여섯시 반 정각 엘리베이터 문 열리면
하루 종일 눌러둔 내 숨도 같이 나와
회의실 목소리 아직 내 귓가에 맴돌아도
한강 바람은 그걸 모두 지워주지
월요일 또 찾아오겠지만 지금은 금요일
막차 한 대 놓쳐도 괜찮아 내 하루 내 거니까
(Uh!)

[Hook]
시계가 돌아 Clock Out
하루가 끝나 Clock Out

[Verse 2]
고시원 창문 너머 지는 해 주황으로
내가 못 본 하늘을 오늘도 놓쳤어도
펜 대신 마이크 잡은 이 시간만은 내 거
기록된 모든 한숨이 여기서 라임으로

[Hook]
(반복)

[Outro]
(샘플 loop fade)
```

### 체크포인트
- [ ] BPM 86-95 범위 (90 BPM 중심)
- [ ] 샘플 loop + 더스티 드럼
- [ ] MPC swing 느낌 (58%)
- [ ] Vinyl crackle 질감
- [ ] 다음절 라임 (나와/맴돌아도 · 지워주지/내 거니까 · 주황으로/놓쳤어도/라임으로)
- [ ] Chest voice + 명료한 발음
- [ ] 평균 라인 12-18 음절 밀도

---

## 🌑 테스트 곡 4 — Style D (하드코어 트랩 젊은 씬)

**가칭**: `INSOMNIA` (불면 · 새벽 직전 내면)
**컨셉**: 잠 못 드는 밤, 천장 보며 반복되는 생각, 도시 고독

### Style Prompt (약 200자)
```
Korean dark hardcore trap, 142 BPM, heavy 808 bass sustain decay sidechained to kick slight distortion, punchy kick fast hi-hat triplet rolls minimal clap on 3, dark atmospheric synth pad muted electric guitar arpeggio minor key, melancholic trap rap husky male vocal high-speed flow, dark tonal balance compressed master, singing in Korean, sharp articulation
```

### EXCLUDE
```
melodic singing, k-pop, ballad
```

### LYRICS 프롬프트 (~195자)
```
[Intro]
(dark pad fade in)

[Verse 1]
천장의 무늬가 매일 달라져 보여
새벽 세시 이 방 혼자 남아
머릿속 소음이 TV처럼 켜져
리모컨 끄는 법 난 아직 몰라
(Skrrt!)

[Hook]
Insomnia 오늘도
Insomnia 또 다시
눈감아도 꿈이 없어
Insomnia 내 도시

[Verse 2]
도시 불빛 창문 넘어 흘러
그림자마다 내 얼굴 걸어
잠 못 드는 밤마다 난 쌓여
먼지처럼 쌓여 사라지게

[Bridge: Breakdown]
(808 drop)
반복 반복 반복

[Hook]
(반복)

[Outro]
(멜랑콜릭 fade)
```

### 체크포인트
- [ ] BPM 140-150 범위 (142 BPM 중심)
- [ ] 808 서스테인 + 사이드체인
- [ ] 다크 패드 + 미니 피아노 모티프
- [ ] Husky/멜랑콜릭 male 보컬
- [ ] 고속 플로우 + 명료도
- [ ] Ad-lib 미니멀 (`Skrrt!` 1회만)

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
| 영어 vocal 섞임 | `singing in Korean` 위치 앞쪽 | 프롬프트 맨 뒤로 이동 |
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
