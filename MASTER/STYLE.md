# VIBE-M STYLE.md
Version: 1.5 (제로 베이스라인 - 코러스 완전 차단)
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
- **Vocal Type 명시 필수**: "Female vocal" 또는 "Male vocal" 반드시 포함

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

**권장 버전 (2줄 완전 차단형):**
```
Lead vocal only. No backing vocals. No harmonies. No doubles. No choir.
Chorus2 bigger only by arrangement density and stereo width of instruments, vocals unchanged.
```

**핵심 원칙:**
- "Backing vocals" 단어 자체가 트리거 → **아예 제거**
- "Unison", "octave unison", "ad-libs"도 보컬 레이어 트리거 → **제로 베이스라인**
- "bigger"는 반드시 **"vocals unchanged"**로 잠금
- 프롬프트는 짧을수록 좋음: **Core 8~10 토큰 + Safety 2줄 + Musicality 1줄**

### 2.2 Harmony Guard 원칙 (제로 베이스라인)

**현재 목표: 코러스 완전 제거**

| 완전 금지 |
|-----------|
| backing vocals |
| harmonies / doubles |
| choir / ensemble |
| unison / octave unison |
| ad-libs / shouts |

**핵심:**
- 보컬은 **Lead only** → 나머지 전부 금지
- "Chorus2 bigger"는 **vocals unchanged**로 잠금
- 베이스라인 잡은 후 필요시 점진적 허용

**필수 강화 문장 (Chorus2 오독 방지):**
> Suno가 "bigger = 단체 코러스/하모니"로 오독하기 쉬움. 아래 문장 필수 포함:

```
Lead vocal only throughout; absolutely no vocal layers in chorus (no doubles, no unison, no octaves).
```

**운영 팁:**
- EDM 톤 재발 시 → Vocal Persona를 Pure로 스왑 후 다시 Husky로 복귀
- 안정화 후 ad-libs 1~2개 허용 테스트 가능

### 2.2.1 Exclude Style 충돌 방지

**원칙: Style 본문에 쓴 톤/캐릭터를 Exclude에 넣지 않는다**

| 상황 | 문제 | 해결 |
|------|------|------|
| Style: "warm soulful tone" | Exclude에 "husky tone" 포함 | 모델이 보컬 캐릭터 혼란 → **Exclude에서 삭제** |
| Style: "breathy delivery" | Exclude에 "breathy" 포함 | 지시 충돌 → **Exclude에서 삭제** |

**Exclude 작성 규칙:**
1. Style 본문의 Vocal Persona 키워드와 겹치는 항목 금지
2. Exclude는 **EDM/프로세싱 계열**만 타격 (vocoder, hard tune, autotune heavy 등)
3. 톤/캐릭터 계열 (husky, warm, breathy 등)은 Style 본문에서만 제어

---

## 🎰 2.3 Required Slots (필수 슬롯 체크리스트)

**원칙: 하나라도 누락 시 FAIL → 출력 금지**

| # | 슬롯 | 설명 | 예시 |
|---|------|------|------|
| S1 | Vocal Persona | gender + tone | "Male vocal, warm soulful tone" |
| S2 | Vocal Processing | 마이크/이펙트 | "dry close-mic, minimal autotune" |
| S3 | Lead Instrument | 메인 악기 | "Felt Piano-led" |
| S4 | Rhythm Source | 리듬 요소 | "soft shaker, rim-only" |
| S5 | BPM | 템포 | "80 BPM" |
| S6 | Key | 조성 | "key Eb Major" |
| S7 | Musicality Matrix | 섹션별 지시 | "Verse2 same melodic contour..." |
| S8 | Harmony Guard | 코러스/화성 금지 | "No backing vocals, no choir" |
| S9 | Chorus Expansion | Chorus2 규칙 | "vocals unchanged" |
| S10 | Chorus Layer Block | 코러스 레이어 완전 차단 | "Lead vocal only throughout; absolutely no vocal layers..." |
| S11 | Exclude 충돌 검사 | Style↔Exclude 톤 겹침 없음 | Style에 soulful → Exclude에 soulful 금지 |

### 검증 프로세스

```
Step 1. Generate Style Prompt
Step 2. Run self-QC against checklist (11개 슬롯)
Step 3. If all pass → output FINAL
        If any fail → STOP + report missing items
```

### Vocal Persona 강제 선언

> **Vocal persona must be explicitly declared:**
> - gender (male/female)
> - vocal character (husky / soft / soulful / airy / pure / breathy 등)
>
> If not explicitly written, output is invalid.

**목적:**
- AI의 암묵적 추론 차단
- 누락 사고 원천 봉쇄
- 검증 자동화로 휴먼 에러 방지

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

## 🚫 6. Exclude Style Rule (합창/화성 중심)

- 최대 **3개 그룹**까지만 사용
- **합창/화성 방지에 집중**, EDM은 1~2개만

### Group A – Choir/Harmony (최우선)
```
choir, gospel choir, stacked harmonies, harmony vocals, vocal ensemble, big harmonies, lush harmonies
```

### Group B – Vocal Processing
```
vocoder, vocal chop, hyperpop vocal, formant shift, hard tune, overprocessed vocal
```

### Group C – EDM (최소한만)
```
EDM drops, big room
```

> 악기 금지(Piano 등)는 트랙별 선택적 적용

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
