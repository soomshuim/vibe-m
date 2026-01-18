# VIBE-M STYLE.md
Version: 1.1 (Harmony Guard 추가)
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

> **Verse2: same melodic contour as v1, stronger dynamics + slightly higher register, minimal soulful runs in last 2 lines. Chorus: hook-first, repeat identically. Chorus 2 bigger with backing vocals, unison or octave unison only. No stacked harmonies, no choir-like backing vocals. End-line ad-libs only, very subtle, single-voice. Bridge: build every bar, no energy drop into chorus. Outro: instrumental fade.**

이 문장은:
- 곡의 기승전결을 고정하고
- AI의 즉흥 구조 붕괴를 방지하며
- 장르가 바뀌어도 "노래처럼 들리게" 만든다.

### 2.1 Harmony Guard (화성 과잉 방지)

Suno는 역할 미지정 시 "AI 합창단" 스타일로 과잉 서비스한다.
아래 규칙으로 방지:

| 금지 | 허용 |
|------|------|
| stacked harmonies | unison backing |
| choir-like backing | octave unison only |
| block chord harmonies | single-voice ad-libs |
| 3도/6도 병행 화성 | call-and-response (single voice) |

**핵심 원칙:**
- "Backing vocals"의 **역할을 명시**해야 함
- 금지만 하면 빈자리를 채우려 함 → 대체 역할 필수
- 완전 차단보다 **타이밍 제한**이 효과적 (예: "no harmonies until last chorus")

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

## 🚫 6. Exclude Style Rule (장르 오염 방지)

- 최대 **3개 그룹**까지만 사용
- 광범위 단어 금지, **정밀 타격**

### Allowed Examples
- trap / 808
- heavy EDM drops
- shouting / screaming
- metal distortion

---

## 🧱 7. Prompt Construction Order (절대 순서)

Style Prompt는 반드시 아래 순서로 작성한다.

1. Genre / BPM / Key
2. Playlist Profile Bias
3. Slot A (Lead Instrument)
4. Core Sound DNA
5. Slot B (Groove)
6. Vocal Persona
7. Musicality Matrix (고정 문장)
8. Exclude Style

---

## 💡 8. Manager's Note

STYLE.md는 취향 문서가 아니다.
**AI가 사고하지 않도록 만드는 안전장치**다.

- 값은 바꿔도 구조는 바꾸지 않는다.
- 장르가 늘어나도 규칙은 늘리지 않는다.
- 복잡해질수록 실패 확률은 올라간다.

단순함은 미학이 아니라
**생존 전략**이다.
