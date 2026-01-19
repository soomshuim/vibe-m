# VIBE-M Role System (SSOT)
# Version: 1.1 (2026-01-19)
# Purpose: Separate thinking to prevent duplication, drift, and algorithmic risk.
# Scope: Defines WHY and WHAT each AI role is responsible for.
# Prompt templates: See MASTER/prompts/

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

### Energy Permission Principle (v1.1)
> "금지는 레이어에만, 허용은 에너지에."

**Seed 단계에서 명문화할 것:**
- Verse2 emotional escalation is **expected and encouraged** (not variable)
- Higher register / falsetto lift = **allowed, not prohibited**
- Natural vocal strain = **allowed**
- Layer prohibition ≠ Energy prohibition

**금지할 것 (레이어만):**
- Backing vocals, doubles, choir, stacks

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

### Final Verdict
Each output must end with:
SAFE / BORDERLINE / FAIL

---

## Boundary with Other Docs

- **MANAGER.md:** QC rules & fail-fast judgment
- **STYLE.md:** Sound vocabulary & prompt syntax (includes Slot definitions)
- **LYRICS.md:** Lyrical engineering rules
- **ROLES.md (this file):** Cognitive separation & responsibility
- **prompts/:** Role-specific prompt templates (실행용)

This file is the constitutional layer.
