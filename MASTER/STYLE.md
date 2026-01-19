# VIBE-M STYLE.md
Version: 1.5 (Single-Lead Explosion + Zero Exception)
Last Updated: 2026-01-19
Purpose: Prevent AI-chorus with zero exception, enforce single-lead V2/Chorus lift, keep prompt <= 1000 chars (EXCLUDE excluded)

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

## 2) Harmony Guard (Mandatory Safety Lines) — v1.5 Zero Exception

> This block MUST appear in every Style Prompt. **예외 조항 제거** - 모델이 "지원 보컬 권리"로 해석하는 것 차단.

**초압축 Harmony Guard (붙박이 2줄)**
```
Single lead vocal ONLY. No backing vocals, no doubles, no harmonies, no choir, no stacks.
Chorus lift = single-lead belt/higher register/stronger attack (NO extra vocal layers, NO vocal sweetening).
```

**EDM 처리 금지 (별도 1줄)**
```
No EDM vocal processing (no vocoder, no vocal chops, minimal autotune).
```

**핵심 원칙**
- 레이어 금지 ≠ 에너지 금지
- "리드 한 명이 더 세게 부르는 것" = 허용/강제
- "보컬 레이어를 늘리는 것" = 금지
- **예외 조항 없음** - "unison OK", "ad-libs OK" 같은 문장 제거

**운영 팁 (Style Prompt 본문에 넣지 말 것)**
- end-line ad-libs가 정말 필요하면 Exclude 옆 메모로 관리
- "If any support happens..." 문장은 모델이 오해하므로 사용 금지

**Reason**
- Suno often "upgrades" chorus with harmony stacks by default
- "지원 보컬 허용" 문장 → 모델이 "지원 보컬을 만들 권리"로 해석
- We allow "release" via **arrangement energy + single-lead belt/lift**, not vocal layering.

---

## 3) Musicality Matrix (Always ON) — v1.5 정량화

Include these in Style Prompt, in compressed form.

- **Verse2 Lift:** same melodic contour as Verse1; **last 2 lines** = stronger dynamics + **higher-register push OR brief falsetto lift** (single lead, 1 event).
- **Chorus Lift:** chorus first line hits peak: **single-lead belt/higher register + 1 held note (longer sustain)**. No layers, no doubles.
- **Chorus Rule:** hook-first; **lyrics repeated identically**.
- **Chorus2 Expansion:** bigger **by arrangement only** (bass/drums energy, wider stereo instruments); **keep SINGLE lead vocal (no layers)**.
- **Bridge Build:** build every bar; **no energy drop into chorus**.
- **Outro:** instrumental fade; return to minimal texture.

**V2 → Chorus 연결 원칙:**
> V2 last 2 lines (1 event: higher register push) → Chorus first line = peak (1 held note + belt)

**금지 표현:**
- ❌ "vocals unchanged" (에너지까지 억제할 수 있음)
- ✅ "keep SINGLE lead vocal (no layers)" (대체 표현)

---

## 4) Energy Switch (Chorus Explosion Without AI Choir) — v1.5

> "후렴 폭발감 부족"이 뜨면 아래 2개 레버를 모두 적용.

### 4.1 Lever A: Arrangement Lift

| 요소 | 적용 방법 |
|------|----------|
| Bass | more active movement / locked to groove |
| Perc | shaker intensity up / add rim-click accents |
| Drums | (if allowed) kick enters or doubles energy **for the first time** in chorus |
| Stereo | wider instruments + extra layer (pad/guitar/piano voicing) |
| Accents | crash/ride only as impact markers (avoid over-busy) |

### 4.2 Lever B: Lead Vocal Lift (정량화)

| 요소 | 적용 방법 |
|------|----------|
| Belt | chorus first line = single-lead belt/stronger attack |
| Register | higher register than verse (noticeable lift) |
| Held Note | **1 held note** on hook (longer sustain, event-like) |
| Dynamics | stronger dynamics, not just same intensity |

**핵심:**
- 리드 한 명이 더 세게/높게 부르는 것 = 허용/강제
- "1 held note + higher register" = 정량화된 폭발 이벤트

**금지:**
- 레이어 추가로 폭발감 만드는 것 = 금지

### 4.3 Do NOT Use

- "bigger chorus with backing vocals/harmonies" 같은 문장
- "choir-like", "stacked", "ensemble", "thick harmony" 유도 표현
- "vocals unchanged" → 대신 "keep SINGLE lead vocal (no layers)" 사용
- "If any support happens..." (예외 조항 금지)

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
| S8 | Harmony Guard | "Single lead ONLY, no backing/doubles/choir/stacks" 명시 |
| S9 | Chorus2 Expansion | "by arrangement only; keep SINGLE lead (no layers)" 명시 |

**If any FAIL:** regenerate and shorten until 9/9 PASS + <=1000 chars.

---

## 9) Quick Reference — v1.5

### 9.1 Harmony Guard 초압축 (붙박이 2줄)
```
Single lead vocal ONLY. No backing vocals, no doubles, no harmonies, no choir, no stacks.
Chorus lift = single-lead belt/higher register/stronger attack (NO extra vocal layers, NO vocal sweetening).
```

### 9.2 Musicality Matrix 압축
```
Verse2: same melodic contour, last 2 lines stronger dynamics + higher-register push or brief falsetto lift (1 event).
Chorus: hook-first, repeat identical; chorus first line hits peak with single-lead belt/higher register + 1 held note (no layers).
Chorus2: bigger by arrangement only (bass/drums energy, wider stereo); keep SINGLE lead vocal (no layers).
Bridge: build every bar, no energy drop into chorus.
Outro: instrumental fade.
```

### 9.3 V2 → Chorus Lift 연결 (정량화)
```
Verse2 last 2 lines: higher-register push or brief falsetto lift (single lead, 1 event).
Chorus first line: 1 held note (longer sustain) + higher register lift (single lead, no layers).
```

### 9.4 물안개 예시 (v1.5 적용)
```
articulation, Korean Lo-fi R&B, 80 BPM, Eb Major, felt piano-led, soft shaker, hazy ambient pad, cinematic but restrained, high fidelity, wide stereo.
Male vocal: warm soulful tone, dry close-mic, very forward, clear Korean diction, natural breaths, minimal autotune, straight delivery.
Single lead vocal ONLY: no backing vocals, no doubles, no harmonies, no choir, no stacked layers; no EDM vocal processing.
Verse2 same melodic contour as v1; last 2 lines stronger dynamics + higher register push or brief falsetto lift.
Chorus hook-first, repeat identical; chorus first line hits peak with single-lead belt/higher register + 1 held note (no layers).
Chorus2 bigger by arrangement only (bass/drums energy, wider stereo instruments); keep SINGLE lead vocal (no layers).
Bridge builds every bar; no energy drop into chorus. Outro felt piano fades.
```

### 9.5 금지 표현 vs 대체 표현
| 금지 | 대체 |
|------|------|
| vocals unchanged | keep SINGLE lead vocal (no layers) |
| If any support happens... | (예외 조항 사용 금지) |
| bigger chorus with backing vocals | bigger by arrangement only |
