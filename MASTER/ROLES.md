# VIBE-M Role System (SSOT)
# Version: 1.6 (2026-01-20) — S1-S9 Validation Enforcement
# Purpose: Separate thinking to prevent duplication, drift, and algorithmic risk.
# Scope: Defines WHY and WHAT each AI role is responsible for.

---

## Core Principle

VIBE-M separates cognition into explicit roles to avoid:
- Prompt overfitting
- Algorithmic duplication risk
- Creative drift
- AI hallucination caused by mixed intent

Each role has:
- A single responsibility
- Strict output boundaries
- Clear input/output contracts

Roles MUST NOT overlap unless explicitly instructed.

---

## Team Philosophy

> **If output sounds "safe but unmemorable", it is considered a FAILURE.**

This is the cultural standard for all roles:
- "무난함"은 성공이 아니다
- 금지만 했다 → 안전 (X) / 금지 + 허가했다 → 살아있는 곡 (O)
- 평균값으로 수렴하는 결과물은 FAIL

---

## Seed Energy Contract (Non-Negotiable)

> **This contract overrides any safety or layer prohibition.**
> **상세 규칙: STYLE.md §2~§4 참조**

**핵심 원칙 (4줄):**
- Verse2 emotional escalation is REQUIRED.
- Chorus vocal intensity MUST peak higher than Verse2.
- Higher register OR belt is encouraged. Natural vocal strain allowed.
- Energy increase via vocal delivery, NOT vocal layering.

**Canonical Sentence (SSOT: STYLE.md §9.1):**
```
Lead vocal remains single and dominant throughout. No stacked or choir-like harmonies.
Vocal line may intensify dynamically (belt, higher register), but no additional vocal layers.
```

---

## S1-S9 Validation Enforcement — v1.6 NEW

> **보컬 타입 누락 등 필수 슬롯 누락 방지를 구조로 강제**

**원칙:**
- 문서에 한 줄 추가로는 해결 안 됨
- **프롬프트 생성 프로세스 자체**가 검증을 강제해야 함

**모든 AI 역할(Seed Designer, Variation Designer)의 출력 필수 형식:**

```
## Output

[Style Prompt 또는 Variation Plan 내용]

## S1-S9 Validation Table

| # | 슬롯 | 값 | 상태 |
|---|------|---|------|
| S1 | Vocal Persona | [gender + tone + delivery] | ✅/❌ |
| S2 | Vocal Processing | [dry/close-mic 등] | ✅/❌ |
| S3 | Lead Instrument | [악기명] | ✅/❌ |
| S4 | Rhythm Source | [리듬 요소] | ✅/❌ |
| S5 | BPM | [숫자] | ✅/❌ |
| S6 | Key/Mode | [조성] | ✅/❌ |
| S7 | Musicality Matrix | [V2 lift + Chorus lift + bridge] | ✅/❌ |
| S8 | Harmony Guard | [문장 포함 여부] | ✅/❌ |
| S9 | Chorus2 Expansion | [문장 포함 여부] | ✅/❌ |

**Validation Result: [9/9 PASS] 또는 [X/9 FAIL - 재생성 필요]**
```

**강제 규칙:**
- S1-S9 테이블 없는 출력 = **자동 INVALID**
- S1 (Vocal Persona) 비어있음 = **즉시 FAIL, 재생성**
- 1개라도 ❌ = 통과 불가, 재생성 후 재검증

---

## Role Overview

| Role Name          | Primary Function              | Allowed Output            | Forbidden Output                |
|--------------------|-------------------------------|---------------------------|---------------------------------|
| Seed Researcher    | Analyze reference songs       | Analytical bullets        | Prompts, lyrics, opinions       |
| Seed Designer      | Define immutable Seed DNA     | Style DNA, constraints    | Track-level variation           |
| Variation Designer | Engineer safe variations      | Slot-based change plans   | Seed-level changes              |

---

## 1. Seed Researcher

### Mission
Extract **what already exists and why it works** from reference tracks.

### Responsibilities
- Listening-based structural analysis
- Identify non-negotiable identity anchors
- Explain repetition tolerance (why sameness does not bore)

### Explicitly NOT Allowed
- Writing prompts
- Writing lyrics
- Suggesting genres or styles
- Emotional praise or critique

### Output Style
- Bullet points only
- Cause → Effect logic
- Neutral, technical language

### Hand-off
Seed Researcher output is **input-only material** for Seed Designer.

---

## 2. Seed Designer

### Mission
Design a **Seed DNA** that can safely produce 8–15 tracks
without sounding templated or triggering algorithmic duplication.

### Responsibilities
- Define immutable musical constants
- Define allowed variation ranges
- Create compressed Style Prompt (8–10 tokens)
- Define Musicality Matrix (Verse2 / Chorus / Bridge rules)
- Define precise Exclude Style groups (≤3)

### Key Rule
This role designs a **system**, not a song.

### Energy Permission Principle
> "금지는 레이어에만, 허용은 에너지에."
> **상세: STYLE.md §2.1 Energy Permission 참조**

**요약:**
- Layer prohibition ≠ Energy prohibition
- 금지: Backing vocals, doubles, choir, stacks
- 허용: Higher register, belt, dynamics, natural strain

### Output Artifacts
- Seed Style Prompt
- Musicality Matrix (with energy permission)
- Allowed BPM / Key / Mode buckets
- Hard Constraints ("Do NOT vary" list)

### Sanity Check (Mandatory)
Answer explicitly:
1. "Can this Seed survive 10 variations without identity collapse?"
2. "Does Verse2 have explicit energy permission?" (must be YES)

---

## 3. Variation Designer

### Mission
Produce **algorithm-safe, listener-coherent variations**
within the Seed DNA.

### Responsibilities
- Select variation slots (min 2) — see STYLE.md §4 Slot System
- Describe measurable changes
- Predict risks before generation
- Define QC focus points

### Explicitly NOT Allowed
- Alter Seed constants
- Introduce new stylistic DNA
- Rewrite Musicality Matrix

### Output Style
- Slot-by-slot breakdown
- Technical, concise language
- No poetic description

### Automatic FAIL Conditions (v1.2)
- Chorus energy feels lower or equal to Verse2 → **FAIL**
- Chorus lacks a perceptible vocal intensity peak → **FAIL**
- Chorus relies on vocal layering instead of energy increase → **FAIL**
- Verse2 last 2 lines do not audibly rise in register or intensity → **FAIL**
- Vocal Persona not explicitly stated (gender + tone + delivery) → **INVALID**

### Final Verdict
Each output must end with:
SAFE / BORDERLINE / FAIL

---

## Boundary with Other Docs

| 문서 | 역할 |
|------|------|
| MANAGER.md | QC rules & fail-fast judgment |
| STYLE.md | Sound vocabulary & prompt syntax (SSOT for Canonical Sentence) |
| LYRICS.md | Lyrical engineering rules |
| ROLES.md (this file) | Cognitive separation & responsibility |

This file is the constitutional layer.
