---
name: wavvy-lyricist
description: Use when writing, rewriting, or reviewing Korean lyrics or Suno lyric prompts for Wavvy series while preserving Wavvy SSOT, copyright safety, and natural sung Korean.
---

# Wavvy Lyricist

Wavvy 전용 한국어 작사 스킬. 목표는 시간대 포지셔닝과 장르 DNA를 보존하면서, 사물/공간/현상 중심의 가사를 자연스럽게 부를 수 있는 한국어로 만드는 것이다.

## Authority

Read in this order before drafting:

1. `MASTER/SSOT.md` for conflict order.
2. Target `SERIES/[series]/concept.md` for series gates and overrides.
3. `MASTER/lyrics/LYRICS.md` for Suno lyric input policy.
4. `wavvy.md` for brand constants.
5. `skills/wavvy-lyricist/references/patterns.md` for lyric pattern lanes.
6. `MASTER/lyrics/skills/WAVVY_LYRIC_SKILL_SPEC.md` for output and gate contract.

Local Wavvy docs override external trend evidence. Per-series overrides are valid only when explicitly written in the series concept.

## Hard Rules

- Korean lyric channel: full lyric drafts should be Korean unless a series concept explicitly permits code-switching.
- Single lead vocal, chest-dominant identity. Do not solve lyric weakness with harmony, backing vocal, falsetto, or choir instructions.
- Time slots define BPM, mood, energy, use case, and vocal tone before lyric topic.
- Do not force direct time/activity words such as `17:00`, `퇴근`, `업무`, `사무실`, `commute`, or `clock-out` unless the series concept explicitly requires them.
- Use external songs only as abstract pattern evidence. Do not copy, translate, closely paraphrase, or imitate distinctive lyric lines or cadences.
- Separate full lyric draft mode from Suno prompt-only mode.

## Mode Choice

Choose and name exactly one mode:

- `full-lyric-draft`: Use for track source files, rewrite proposals, or human review. Section tags such as `[Verse]` and `[Chorus]` are allowed as drafting structure.
- `suno-prompt-only`: Use for direct Suno Lyrics input. Output 1-3 short English direction lines or structure tags only. Do not output full Korean lyric rows.
- `review-only`: Use when asked to judge an existing lyric without rewriting.

Never mix prompt-only text and full lyric rows in the same deliverable.

## Draft Workflow

1. Build a Source Map: series concept, Wavvy docs, track/source file, research artifact, and external pattern sources if used.
2. Freeze constraints: BPM, key, genre, mood, vocal identity, lyric exclusions, and allowed override notes.
3. Pick a Lyric Strategy: narrator, emotional arc, hook anchor, vocabulary lane, density, and banned cliches.
4. Draft in the selected mode.
5. Run Self-Gate and report PASS/HOLD/FAIL with concise reasons.

## Wavvy Writing Principles

- Object, space, and phenomenon first: light, air, window, floor, room, step, hand, breath, rhythm, color.
- One image or action per line when possible.
- Emotion should be inferred through scene movement, body response, ordinary action, or sonic/visual texture.
- Hooks should be phrase-first: compact, repeatable, and understandable without the full verse story.
- Verses may carry more scene detail; choruses should tighten into a short memory object.
- Modern means speakable Korean, not imported slang or famous English catchphrases.

## Avoid

- Explanatory prose, direct emotional slogans, meta-commentary, and abstract thesis lines.
- Sterile image collage where nouns stack without natural speech logic.
- Heavy heartbreak, toxic intimacy, dark room framing, or melodrama unless the target series requires it.
- Prompt-only parentheses such as `(Scene: ...)` or `(Mood: ...)`.
- Production/performance instructions in lyric text; move those to style prompts.

## Required Output

For new drafts and rewrites, output these sections in order:

1. `Source Map`
2. `Constraint Freeze`
3. `Lyric Strategy`
4. `Draft`
5. `Self-Gate`

For `review-only`, output:

1. `Source Map`
2. `Constraint Freeze`
3. `Findings`
4. `Verdict`

## Self-Gate

Mark each gate `PASS`, `HOLD`, or `FAIL`:

- Copyright Safety: no copied, translated, closely paraphrased, or famous-cadence material.
- Wavvy Identity: Korean, single-lead, chest-dominant, no harmony dependency.
- Series DNA: matches the concept's BPM/mood/genre/vocal constraints.
- Lyric Philosophy: object/space/phenomenon based, not explanatory or slogan-driven.
- Natural Korean: lines can be spoken and sung without awkward image stacking.
- Hook Clarity: a compact hook exists for pop/R&B lanes, or the series concept explains why not.
- Suno Format: prompt-only mode follows `MASTER/lyrics/LYRICS.md` and contains no full Korean lyric rows.
