# VIBE-M STYLE.md
Version: 1.9 (Canonical Sentence Unification)
Last Updated: 2026-01-19
Purpose: Unified canonical sentence across all docs + Energy Contract enforcement

---

## 0) Non-Negotiables (Always ON)

### 0.1 Prompt Length
- **Style Prompt must be <= 1000 characters (spaces included), EXCLUDE excluded.**
- If longer: compress descriptors into fewer tokens (8–10 token rule for core identity).

### 0.2 Pure Input Principle
- **Lyrics field: only singable Korean text + minimal tags.**
- All musical instructions must live in **Style Prompt**.

### 0.3 Technical Accuracy
- Use correct music terms: `rim-shot / rim-click` (NOT rim light).
- Avoid overly broad excludes like "Electric keyboard" unless necessary—be precise.

---

## 1) Core Sound DNA (Project Constant)

Use these as the "always-on" identity baseline (pick only the essentials to stay under 1000 chars).

- Texture: **high fidelity, wide stereo, cinematic but restrained**
- Vocal production: **dry close-mic, very forward, natural breaths, minimal autotune**
- Diction: **clear Korean articulation**
- Default mood: **minimal, intimate, restrained (Verse) → release (Chorus)**

---

## 2) Harmony Guard (Mandatory Safety Lines) — v1.6 Energy Permission

> This block MUST appear in every Style Prompt. **금지는 레이어에만, 허용은 에너지에.**

**초압축 Harmony Guard (붙박이 2줄)**
```
Lead vocal remains single and dominant throughout. No stacked or choir-like harmonies.
Vocal line may intensify dynamically (belt, higher register), but no additional vocal layers.
```

**EDM 처리 금지 (별도 1줄)**
```
No EDM vocal processing (no vocoder, no vocal chops, minimal autotune).
```

**핵심 원칙 (v1.6 분리)**
- **금지 대상**: 보컬 레이어 (backing, doubles, choir, stacks)
- **허용 대상**: 보컬 에너지 (belt, higher register, dynamics, strain)
- "리드 한 명이 더 세게/높게 부르는 것" = 허용 (encouraged)
- "보컬을 겹치는 것" = 금지

**v1.5 → v1.6 변경점**
- ❌ "vocals unchanged" → 모델이 "보컬 에너지 상승도 금지"로 오해
- ✅ "vocal line may intensify dynamically" → 에너지 상승 명시 허용
- ❌ "Single lead vocal ONLY" → 너무 강압적
- ✅ "Lead vocal remains single and dominant" → 톤 다운

**운영 팁 (Style Prompt 본문에 넣지 말 것)**
- end-line ad-libs가 정말 필요하면 Exclude 옆 메모로 관리
- "If any support happens..." 문장은 모델이 오해하므로 사용 금지

**Reason**
- v1.5에서 "금지 규칙이 에너지 규칙을 덮어버림" 문제 발생
- 모델이 가성/레지스터 상승을 "보컬 변형"으로 오인 → 회피
- 해결: "금지는 레이어에만" 명확히 분리

---

## 2.1) Energy Permission (Mandatory)

> **This block MUST appear with Safety Lines. 금지와 허용은 항상 쌍으로.**

```
Energy Permission:

Chorus vocal may be delivered with stronger intensity or light belt.
Higher register emphasis is encouraged.
Natural vocal strain allowed.
Energy increase must come from vocal delivery, not harmony layers.
```

**핵심 원칙:**
- Safety Lines 바로 아래에 이 블록 배치 (같은 섹션, 같은 문단)
- "금지했다" 만으로는 부족 → "금지 + 허가했다" = 살아있는 곡
- Verse2/Chorus에서 보컬 강도(intensity) 상승은 **필수**이자 **권장**

**FAIL if missing:**
- Energy Permission 없이 Safety Lines만 있으면 → 무난함 발생 → FAIL

---

## 3) Musicality Matrix (Always ON) — v1.7 Fail Fast

Include these in Style Prompt, in compressed form.

- **Verse2 Lift (MUST):** same melodic contour as Verse1; **last 2 lines MUST rise in emotional intensity**: higher register OR light falsetto lift is **encouraged**. Natural vocal strain **allowed**.
- **Chorus Lift:** chorus first line hits peak: **belt/higher register + exactly 1 held note (longer sustain than any verse note)**. Lead vocal energy may increase.
- **Chorus Rule:** hook-first; **lyrics repeated identically**. No other sustained notes should appear in chorus besides the 1 held note.
- **Chorus2 Expansion:** bigger **by arrangement** (bass/drums energy, wider stereo instruments); **lead vocal energy may increase, but no new vocal layers**.
- **Bridge Build:** build every bar; **no energy drop into chorus**.
- **Outro:** instrumental fade; return to minimal texture.

**V2 → Chorus 연결 원칙:**
> V2 last 2 lines (emotional intensity rise: higher register/falsetto encouraged) → Chorus first line = peak (1 held note, longer sustain than any verse note + belt)

**Energy Reference (QC 기준, 프롬프트용 아님):**
> Chorus peak note should sustain at least **1.5x longer** than any Verse note.

**v1.7 Fail Fast 조건 (위반 시 즉시 FAIL):**
- ❌ FAIL if Verse2 last 2 lines do not audibly rise in register or intensity
- ❌ FAIL if Chorus first line is not perceptibly higher or more intense than Verse2
- ❌ FAIL if Chorus lacks the 1 held note event
- ❌ FAIL if Chorus relies on vocal layering instead of energy increase

**v1.6 표현 원칙 (유지):**
- ❌ "vocals unchanged" → 에너지까지 억제
- ❌ "keep SINGLE lead" → 너무 강압적
- ✅ "lead vocal energy may increase, but no new vocal layers" → 에너지 허용 + 레이어 금지 분리
- ✅ "higher register is encouraged" → 권한 부여

---

## 4) Energy Switch (Chorus Explosion Without AI Choir) — v1.6

> "후렴 폭발감 부족"이 뜨면 아래 2개 레버를 모두 적용.

### 4.1 Lever A: Arrangement Lift

| 요소 | 적용 방법 |
|------|----------|
| Bass | more active movement / locked to groove |
| Perc | shaker intensity up / add rim-click accents |
| Drums | (if allowed) kick enters or doubles energy **for the first time** in chorus |
| Stereo | wider instruments + extra layer (pad/guitar/piano voicing) |
| Accents | crash/ride only as impact markers (avoid over-busy) |

### 4.2 Lever B: Lead Vocal Lift (에너지 허용)

| 요소 | 적용 방법 |
|------|----------|
| Belt | chorus first line = stronger attack, more intensity |
| Register | higher register than verse (noticeable lift) |
| Held Note | **1 held note** on hook (longer sustain, event-like) |
| Dynamics | stronger dynamics, natural vocal strain allowed |
| Falsetto | brief falsetto lift encouraged (especially V2 ending) |

**핵심 (v1.6):**
- 리드 한 명이 더 세게/높게 부르는 것 = **encouraged**
- 가성/레지스터 상승 = **allowed/encouraged**
- "1 held note + higher register + belt" = 정량화된 폭발 이벤트

**금지 (레이어만):**
- 보컬 레이어 추가로 폭발감 만드는 것 = 금지

### 4.3 Do NOT Use

- "bigger chorus with backing vocals/harmonies" 같은 문장
- "choir-like", "stacked", "ensemble", "thick harmony" 유도 표현
- ❌ "vocals unchanged" → 에너지까지 억제
- ❌ "keep SINGLE lead vocal" → 너무 강압적
- ✅ "lead vocal energy may increase, but no new vocal layers" → 사용 권장

---

## 5) Variation Slots (Per-Track Choices)

Pick values per track; keep it minimal to prevent model confusion.

### Slot A — Lead Instrument (choose 1)
- Nylon guitar-led (cold arpeggio)
- Felt piano-led (soft voicing)
- Rhodes/EP-led (hazy chords)
- Ambient synth pad-led (atmospheric textures)

### Slot B — Rhythm Source (choose 1)
- No drums (perc only)
- Soft shaker + rim-shot/rim-click
- Brush kit
- Tight understated kick (heartbeat-like)

### Slot C — BPM Bucket
- Choose within concept range (ex: 75–85 for chill nightwalk)

### Slot D — Structure Emphasis
- Hook entry timing / bridge presence / pre-chorus tension cue

### Slot E — Key/Mode Bucket
- Maintain at least 3 key buckets per project (avoid fingerprint sameness)

### Slot F — Vocal Persona (Mandatory)
- Female husky / Female pure / Male soulful / Male soft
- Always specify: **gender + tone + delivery**.

---

## 6) Exclude Style Library (Use max 3 groups)

Pick up to 3 groups depending on the track risk. **그룹명에 사용 목적 표기.**

### Group A (Vocal FX) — 보컬 프로세싱 차단
```
autotune heavy, hard tune, vocoder, vocal chop, formant shift, hyperpop vocal, pitchy EDM lead
```

### Group B (EDM Arr) — EDM 편곡 차단
```
EDM drops, big room, festival, supersaw lead, sidechain pumping
```

### Group C (Harmony/Choir) — 합창/화성 차단
```
choir, gospel choir, stacked harmonies, harmony stack, ensemble vocals, backing vocal layers, doubled vocals
```

### (선택) Group D (Aggressive) — 공격적 스타일 차단
```
shouting, screaming, metal, heavy distortion
```

---

## 7) Prompt Assembly Template (Copy & Fill)

### 7.1 Style Prompt (<=1000 chars, EXCLUDE excluded)

**순서:**
1. Genre/BPM/Key + Lead Inst + Rhythm
2. Vocal Persona + Vocal Production
3. Harmony Guard (compressed)
4. Musicality Matrix (compressed)
5. Outro

### 7.2 Exclude (separate field)
- Choose max 3 groups above.

---

## 8) Self-QC Checklist (Claude must pass) — v1.5

**"요소 빠짐 방지"를 구조로 강제하는 3-Step 프로세스:**

```
Step 1: 9-Slot 값 먼저 채우기 (빈칸 있으면 FAIL)
Step 2: 그 값으로 Style Prompt 생성
Step 3: 글자수 체크 (Style만 1000자 이하) → 넘으면 압축 루프
```

### 9-Slot Table (PASS/FAIL)

| # | 슬롯 | 체크 내용 |
|---|------|----------|
| S1 | Vocal Persona | gender + tone + delivery 명시 |
| S2 | Vocal Processing | dry/close-mic + minimal autotune |
| S3 | Lead Instrument | 메인 악기 1개 |
| S4 | Rhythm Source | 리듬 요소 명시 |
| S5 | BPM | 템포 명시 |
| S6 | Key/Mode | 조성 명시 |
| S7 | Musicality Matrix | V2 lift (1 event) + Chorus lift (1 held note) + bridge build + outro |
| S8 | Harmony Guard | "Lead vocal remains single and dominant; no additional vocal layers" 명시 |
| S9 | Chorus2 Expansion | "bigger by arrangement; vocal may intensify but no layers added" 명시 |

**If any FAIL:** regenerate and shorten until 9/9 PASS + <=1000 chars.

---

## 9) Quick Reference — v1.7

### 9.1 Harmony Guard 초압축 (붙박이 2줄)
```
Lead vocal remains single and dominant throughout. No stacked or choir-like harmonies.
Vocal line may intensify dynamically (belt, higher register), but no additional vocal layers.
```

### 9.2 Musicality Matrix 압축
```
Verse2: same melodic contour, last 2 lines MUST rise in emotional intensity (higher register or falsetto encouraged, natural strain allowed).
Chorus: hook-first, repeat identical; chorus first line hits peak with belt/higher register + 1 held note (longer sustain than any verse note). Lead vocal energy may increase.
Chorus2: bigger by arrangement (bass/drums energy, wider stereo); lead vocal energy may increase, but no new vocal layers.
Bridge: build every bar, no energy drop into chorus.
Outro: instrumental fade.
```

### 9.3 V2 → Chorus Lift 연결 (에너지 허용)
```
Verse2 last 2 lines: emotional intensity MUST rise (higher register/falsetto encouraged, natural strain allowed).
Chorus first line: 1 held note (longer sustain) + belt/higher register. Lead vocal energy may increase.
```

### 9.4 물안개 예시 (v1.6 적용)
```
articulation, Korean Lo-fi R&B, 80 BPM, Eb Major, felt piano-led, soft shaker, hazy ambient pad, cinematic but restrained, high fidelity, wide stereo.
Male vocal: warm soulful tone, dry close-mic, very forward, clear Korean diction, natural breaths, minimal autotune, straight delivery.
Lead vocal remains single and dominant. No stacked or choir-like harmonies. Vocal line may intensify dynamically, but no additional vocal layers. No EDM vocal processing.
Verse2 same melodic contour as v1; last 2 lines MUST rise in emotional intensity (higher register or brief falsetto encouraged).
Chorus hook-first, repeat identical; chorus first line hits peak with belt/higher register + 1 held note (longer sustain than any verse note). Lead vocal energy may increase.
Chorus2 bigger by arrangement (bass/drums energy, wider stereo); lead vocal energy may increase, but no new vocal layers.
Bridge builds every bar; no energy drop into chorus. Outro felt piano fades.
```

### 9.5 금지 표현 vs 권장 표현 (v1.7)
| 금지 | 권장 |
|------|------|
| vocals unchanged | lead vocal energy may increase, but no new vocal layers |
| keep SINGLE lead vocal | lead vocal remains single and dominant |
| Single lead vocal ONLY | Lead vocal remains single and dominant |
| If any support happens... | (예외 조항 사용 금지) |
| bigger chorus with backing vocals | bigger by arrangement |

### 9.6 Fail Fast 조건 요약 (v1.7)
```
FAIL if:
- Verse2 last 2 lines do not audibly rise in register or intensity
- Chorus first line is not perceptibly higher or more intense than Verse2
- Chorus lacks the 1 held note event
- Chorus relies on vocal layering instead of energy increase

INVALID if:
- Vocal Persona not explicitly stated (gender + tone + delivery)
- Any mandatory slot missing
```
