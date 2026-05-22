# Wavvy Lyric Patterns

Generated: 2026-05-22 KST
Source baseline: `.ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/research/lyrics-skill-baseline.md`

This reference records copyright-safe lyric pattern guidance. It does not store copied, translated, or closely paraphrased external lyric lines.

## Source Map

Local authorities:

- `MASTER/SSOT.md`: conflict order and per-series override policy.
- `MASTER/lyrics/LYRICS.md`: Suno lyric input modes, prompt-only rules, tag rules.
- `MASTER/MANAGER.md`: document-driven conservative quality fallback.
- `wavvy.md`: Korean lyric channel, single lead vocal, chest-dominant identity, no harmonies.
- `SERIES/[series]/concept.md`: series-specific BPM, mood, genre, vocal, and explicit overrides.

Research artifacts:

- `.ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/research/lyrics-skill-baseline.md`
- `.ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/research/source-index.md`
- `.ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/research/2026-pop-rnb-lyric-patterns.md`
- `.ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/implementation/17-00-track-01-rewrite.md`

External trend sources are access-dated in the source index. They are used only for abstract market and songwriting patterns such as chart hybridity, speakable phrasing, hook portability, and retro-soul familiarity.

## Universal Pattern Dimensions

| Dimension | Wavvy Baseline |
|---|---|
| Narrator | Close first person or lightly addressed second person. Avoid omniscient explanation. |
| Line unit | Short breath units. One image or action per line. |
| Hook | Compact phrase-first anchor with small contextual variation. |
| Emotional arc | Small concrete state shift rather than dramatic confession. |
| Vocabulary | Everyday Korean plus tactile nouns; sparse English only when concept allows. |
| Imagery | Objects, space, light, air, body rhythm, movement, color. |
| Register | Speakable, sung, non-literary Korean. |
| Copyright | Abstract patterns only. Never copy, translate, or imitate external lyric lines. |

## Core Wavvy Vocabulary Lanes

Use as lanes, not as mandatory word banks:

- Light/color: 빛, 색, 반짝, 선명, 환해져, 노란, 파란, 번져.
- Body/rhythm: 손끝, 어깨, 숨, 박자, 리듬, 맥박, 발걸음.
- Space/object: 창, 거리, 바닥, 공기, 스피커, 문, 그림자, 방.
- Motion: 올라가, 가볍게, 한 칸, 고개, 돌아, 흔들려, 열려.
- Inferred emotion: 표정이 풀리다, 웃음이 나다, 괜찮아지다, 마음이 열리다.

Avoid as defaults:

- Direct time/activity labels: `17:00`, `퇴근`, `점심`, `업무`, `사무실`, `commute`, `clock-out`.
- Heavy labels: `사랑해`, `슬퍼`, `외로워`, `무너져`, `아파` unless the lane requires them.
- Dark R&B defaults: 밤새, 취해, toxic, broken, lonely-room framing.
- Trend-copy risk: distinctive English catchphrases, famous lyric turns, or borrowed cadence shapes.

## Genre Lanes

### Bright Pop/R&B

- Goal: immediate replay, clear chorus memory, bright major-key lift.
- Narration: conversational, lightly confident, close to spoken Korean.
- Hook: repeated phrase with post-hook echo or response.
- Verse: short lines that can ride 120+ BPM rhythmic delivery.
- Chorus: opens wider than the verse and tightens around one memory phrase.
- Avoid: heavy heartbreak, dark room, time/work labels, idol chant energy, and slogan-only positivity.

### Contemporary R&B

- Goal: smooth verse pocket and emotional closeness without losing Wavvy clarity.
- Narration: intimate first person, still grounded in concrete scene cues.
- Hook: melodic phrase that can stretch vocally; fewer chant-like repetitions than Pop/R&B.
- Vocabulary: hand, breath, room, glass, shadow, pulse, door, temperature, distance.
- Avoid: melodramatic confession, over-sexualized cliche, and harmony-dependent writing.

### Neo-Soul / Urban Neo-Soul

- Goal: groove, inner motion, tactile warmth, subtle sophistication.
- Narration: reflective but object-based.
- Hook: less obvious than pop, but still repeatable as phrase or cadence.
- Vocabulary: floor, lamp, cup, window, shoulder, pocket, late light, slow color.
- Avoid: abstract thesis lines, excessive metaphor density, and difficult language mirroring difficult chords.

### Lo-fi / Chillhop Adjacent

- Goal: texture and atmosphere with readable residue.
- Narration: minimal, often fragmentary, but not meaningless.
- Hook: can be mantra-like or absent when the concept supports low lyric density.
- Vocabulary: room tone, weather, small objects, light, routine movement.
- Avoid: dense story blocks, explicit emotional explanation, and over-specified scene scripts.

## Known Failure Mode

The 17-00 rewrite run showed that a draft can satisfy "image-based" on paper while still failing as a Wavvy lyric if it stacks abstract nouns without natural speech logic. Treat natural sung Korean as equal to imagery.

Reject lines that read like:

- object noun + color noun + breath/light noun with no human action.
- abstract uplift claims without scene movement.
- repeated hook surroundings that only restate the same emotion.

Prefer:

- ordinary first-person movement.
- a small before/after change.
- concrete objects that a vocalist can say naturally.
- hook repetition where nearby images shift angle.

## Suno Mode Pattern

For `suno-prompt-only`, use one of:

```text
Korean lyrics about bright air, light movement, clear repeated hook
```

```text
I-V1-PC-C-PC2-V2-C-B-C-O
Korean Pop R&B, speakable Korean, bright color, light steps, compact hook
```

Do not include full Korean lyric rows in prompt-only mode. Do not wrap prompt-only directions in parentheses.
