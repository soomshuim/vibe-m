# VIBE-M STYLE.md
Version: 1.4 (Safety Lines 압축 + 긍정 방향 가드)
Last Updated: 2026-01-18
Purpose: Define sound identity, prompt syntax, and expansion-safe style architecture

---

## 🎯 0. STYLE.md의 역할

STYLE.md는 **VIBE-M 사운드의 헌법**이다.

이 문서는:
- Suno가 *어떻게 연주해야 하는지*를 정의하고
- 장르/플레이리스트가 바뀌어도 **구조는 유지**되며
- 값(Parameter)만 교체하여 확장 가능하도록 설계된다.

> 가사는 LYRICS.md
> 판단과 폐기는 MANAGER.md
> **연주 방식과 소리의 성격은 STYLE.md**

---

## 🧠 1. Global Sound DNA (전 트랙 공통 상수)

아래 요소는 **모든 VIBE-M 트랙에 반드시 포함**된다.
플레이리스트가 달라져도 절대 제거하지 않는다.

### 1.1 Core Texture
- High fidelity
- Wide stereo (but not exaggerated)
- Cinematic but restrained
- Clean low-end, controlled dynamics

### 1.2 Vocal Production (Absolute Constant)
- Dry and close-mic
- Very forward vocal placement
- Natural breaths preserved
- Minimal pitch correction
- Clear Korean diction

> 장르가 바뀌어도
> **"가수가 바로 귀 옆에서 부르는 느낌"은 유지한다.**

---

## 🎼 2. Musicality Matrix (구조 강제 문장)

아래 문장은 **모든 Style Prompt에 그대로 포함**한다.
(단어 수정 ❌, 순서 변경 ❌)

> **Verse2: same melodic contour as v1, stronger dynamics + slightly higher register, minimal soulful runs in last 2 lines. Chorus: hook-first, repeat identically. Bridge: build every bar, no energy drop into chorus. Outro: instrumental fade.**

*Chorus2 / Vocals / Safety는 §2.1 Safety Lines로 분리 (본문에 1회만 삽입)*

이 문장은:
- 곡의 기승전결을 고정하고
- AI의 즉흥 구조 붕괴를 방지하며
- 장르가 바뀌어도 "노래처럼 들리게" 만든다.

### 2.1 Safety Lines (필수 안전 문장)

**모든 Style Prompt에 반드시 포함.** 금지 문장은 **1회로 압축**, 반복하면 모델이 둔감해짐.

**권장 버전 (3줄 압축형):**
```
Chorus2 bigger via instruments only (extra guitar texture, slightly wider stereo, stronger bass movement), NOT via vocal layers.
Vocals: lead only. No harmony stacks/choir. If any double: single-voice unison, very low, end-line ad-libs only.
Keep vocals organic and intimate (no EDM-style vocal sound).
```

**핵심 원칙:**
- "하지 마" + "이렇게 해"를 같이 써야 모델이 다른 과장으로 안 튐
- "drums/bass energy" 같은 표현은 클럽 드롭 트리거 위험 → **instrument thickness / stereo width / arrangement lift** 사용
- 금지 문장 반복 ❌ → 짧고 단단하게 1회

### 2.2 Harmony Guard 원칙

| 금지 | 허용 |
|------|------|
| stacked harmonies | unison backing |
| choir-like backing | octave unison only |
| block chord harmonies | single-voice ad-libs |
| 3도/6도 병행 화성 | call-and-response (single voice) |

**핵심:**
- "Backing vocals" 단어 자체가 트리거 → 역할 명시 필수
- 금지만 하면 빈자리 채움 → **대체 역할 지정**
- "커지는 방법"을 **편곡/다이내믹**으로 지정 (보컬 레이어 아님)

**운영 팁:**
- backing vocals가 계속 터지면 → `no backing vocals` + `no crowd-like shouts`
- EDM 톤 재발 시 → Vocal Persona를 Pure로 스왑 후 다시 Husky로 복귀

---

## 🧩 3. Playlist Profile System (확장 핵심)

STYLE.md의 핵심은 **Playlist Profile 분리**다.
플레이리스트가 늘어나도 아래 구조만 유지하면 된다.

---

### 3.1 Playlist Profile Template

각 플레이리스트는 아래 항목만 정의한다.

- Target Mood
- BPM Range
- Groove Character
- Energy Curve
- Allowed Instrument Bias

---

### 3.2 Profile: CHILL / EMOTIONAL (기본값)

**Use Case:** 새벽, 감정, 회상, 정서적 몰입

- BPM: 70–92
- Groove: Loose / minimal / breathing
- Energy Curve: Low → Medium (no explosive peak)
- Instrument Bias:
  - Nylon Guitar
  - Felt Piano
  - Rhodes
  - Ambient Pad (subtle)

---

### 3.3 Profile: RUNNING / WORKOUT

**Use Case:** 러닝, 가벼운 운동, 리듬 유지

- BPM: 120–150
- Groove: Straight / driving / no swing
- Energy Curve: Medium → High (sustain peak)
- Instrument Bias:
  - Bright electric guitar
  - Punchy bass locked to kick
  - Tight drums (kick/snare focus)
  - Occasional claps or chants

> Vocal production은 여전히 **dry & forward** 유지
> 단, delivery는 더 confident / energetic

---

### 3.4 Profile: DRIVING / NIGHT DRIVE

**Use Case:** 야간 운전, 도시, 흐름 유지

- BPM: 90–120
- Groove: Steady / hypnotic
- Energy Curve: Medium (flat but immersive)
- Instrument Bias:
  - Synth bass (controlled)
  - Rhodes / EP
  - Clean electric guitar riffs
  - Minimal percussion

---

## 🎸 4. Instrument & Groove Slots (Variation Engine)

매 트랙마다 **아래 슬롯 중 일부만 교체**한다.
(Variation Matrix와 연동)

### Slot A – Lead Instrument (Choose 1)
- Nylon guitar
- Felt piano
- Rhodes / EP
- Clean electric guitar
- Ambient synth pad

### Slot B – Drum / Rhythm (Choose 1)
- No drums
- Soft shaker / rim-shot
- Brush kit
- Tight understated kick
- Straight driving kit (running)

---

## 🎤 5. Vocal Persona Slot (캐릭터 유지)

보컬은 **트랙의 정체성 앵커**다.
프로젝트 내에서는 **1–2개만 사용**한다.

- Female Husky: warm, airy, intimate
- Female Pure: clear, straight, fragile but firm
- Male Soulful: warm, breathy, emotional
- Male Soft: gentle, youthful, calm

> Persona 변경은 **새 프로젝트 단위**에서만 허용

---

## 🚫 6. Exclude Style Rule (보컬 프로덕션 중심)

- 최대 **3개 그룹**까지만 사용
- 장르보다 **보컬 프로덕션**을 정밀 타격

### Group A – Vocal Processing (EDM 보이스 차단)
```
autotune heavy, vocoder, vocal chop, formant shift, pitchy EDM lead, hyperpop vocal, hard tune, overprocessed vocal
```

### Group B – EDM Signatures
```
EDM drops, big room, supersaw lead, festival, sidechain pumping
```

### Group C – Choir/Harmony (합창 차단)
```
choir, gospel choir, stacked harmonies, big harmonies, ensemble vocals
```

> 기존 "Piano" 같은 악기 금지는 트랙별 필요에 따라 선택적 적용

---

## 🧱 7. Prompt Construction Order (절대 순서)

Style Prompt는 반드시 아래 순서로 작성한다.
**총 길이: 공백 포함 1000자 이내** (Suno 제한)

### Main Style (압축형, 8–10 토큰)
1. Genre / BPM / Key
2. Playlist Profile Bias
3. Slot A (Lead Instrument)
4. Core Sound DNA
5. Slot B (Groove)
6. Vocal Persona

### Safety Lines (필수, §2.1 그대로)
7. No choir / no stacked harmonies 문장
8. Backing vocals 역할 지정 문장
9. No EDM vocal processing 문장

### Musicality Matrix
10. §2 고정 문장

### Exclude Style
11. Group A/B/C 중 필요한 것만

---

## 💡 8. Manager's Note

STYLE.md는 취향 문서가 아니다.
**AI가 사고하지 않도록 만드는 안전장치**다.

- 값은 바꿔도 구조는 바꾸지 않는다.
- 장르가 늘어나도 규칙은 늘리지 않는다.
- 복잡해질수록 실패 확률은 올라간다.

단순함은 미학이 아니라
**생존 전략**이다.
