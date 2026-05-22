# Wavvy Lyrics Skill Baseline

Generated: 2026-05-22 KST
Worker: worker-01
Scope: research baseline only. No skill, harness, command, or production file implementation.

## Boundary

- This baseline summarizes non-copyrightable lyric narration patterns, vocabulary lanes, Wavvy policy constraints, and prior run lessons.
- No external lyric lines were copied, stored, translated, or closely paraphrased.
- External evidence is limited to chart presence, artist/songwriting interviews, and music journalism about production/narration patterns.
- Local Wavvy docs remain the authority when external trend evidence conflicts with project rules.

## Evidence Summary

### Current Pop/R&B/Neo-Soul Context

1. Streaming popularity is hybrid.
   - Current global charts include new pop/R&B hits, viral R&B records, catalog revivals, cross-genre pop, and event-driven album tracks.
   - Baseline implication: Wavvy should not chase one narrow slang surface. Use durable pop language with current low-friction phrasing.

2. Strong contemporary pop-soul writing is speakable.
   - Olivia Dean's public songwriting framing emphasizes reality-based, out-loud language rather than abstract lyricism.
   - Baseline implication for Korean lyrics: write lines that sound like a vocalist could naturally say them, then compress them into melody. Avoid ornate image chains that read as AI-poetic.

3. Hooks are phrase-first.
   - Ravyn Lenae / "Love Me Not" coverage emphasizes a simple recurring hook, classic instrumentation, and a characterful vocal spin over complex plot.
   - Baseline implication: a Wavvy hook should be a compact Korean phrase that can repeat with small contextual shifts. The verse can carry scene detail, but the chorus must survive as a short memory object.

4. Retro soul familiarity is current when paired with modern polish.
   - Recent pop-soul discourse repeatedly points to Motown/soul/R&B familiarity, guitar/bass/organ/piano color, and joyful live-performance energy.
   - Baseline implication: lyric vocabulary can stay tactile and familiar: light, air, hand, step, room, window, floor, rhythm, color, breath. The writing should not become academic neo-soul poetry unless a series concept explicitly asks for it.

5. Emotional engines are simple but mixed.
   - Current bright Pop/R&B can be joyful while carrying a small tension: confidence/softness, wanting/hesitating, ordinary day/sudden lift, fun/tears.
   - Baseline implication: Wavvy should prefer a micro before/after curve over explicit emotion labels. Show the state changing through body, object, and space.

6. Virality favors portable moments, not full-story dependence.
   - "Love Me Not" grew through social-video reuse and remix/mashup behavior before broader chart persistence.
   - Baseline implication: every Wavvy lyric draft needs at least one portable hook or post-hook phrase, but it must avoid meme slang and famous-cadence imitation.

## Wavvy Local Rules To Preserve

Priority source order follows `MASTER/SSOT.md`: machine state and series `concept.md` own current series truth; `MASTER/lyrics/LYRICS.md`, `MASTER/MANAGER.md`, and `wavvy.md` own global lyric/quality defaults.

Hard lyric identity:

- Korean lyric channel.
- Chest-dominant, single lead vocal identity.
- No harmonies / backing-vocal dependence as a lyric solution.
- Time slots define BPM, mood, energy, use case, and vocal tone before lyric topic.
- Lyrics do not need to mention the time, commute, work, sleep, or any literal station activity unless a series concept explicitly requires it.

Wavvy lyric philosophy:

- Object, space, and phenomenon first.
- One image per line when possible.
- Emotion is inferred through scene movement, body response, light, color, air, rhythm, or ordinary action.
- Avoid explanatory sentences, direct emotional slogans, meta-commentary, and over-labeled feelings.
- Genre density changes by lane: R&B can carry more narration; lo-fi/chillhop should remain more textural; bright Pop/R&B needs faster hook clarity.

Suno and project-format constraints:

- The skill must explicitly separate draft mode from Suno input mode.
- If generating Suno prompt-only input, follow `MASTER/lyrics/LYRICS.md`: 1-3 English direction lines, no parenthesized prompt-only text, and no full Korean lyric rows.
- If generating a full lyric draft for a track file, section tags are acceptable as a drafting artifact, but the handoff must state that it is not the same as prompt-only mode.
- Structure tags belong in brackets; performance/production instructions belong in style prompts, not lyric text.

## Prior 17-00 Run Lessons

The previous 17-00 research run is useful because it exposed a failure mode specific to Wavvy:

- A first rewrite can satisfy "image-based" on paper while still sounding awkward if it stacks abstract nouns such as color/light/breath without natural speech logic.
- The corrected direction moved toward conversational first-person narration, everyday objects, and a clear before/after lift while preserving Wavvy's object/space/phenomenon philosophy.
- For bright 17:00 Pop R&B, the direct topic is not "work ending"; the useful curve is low battery to renewed motion.
- The hook anchor may stay simple, but surrounding lines should vary the angle rather than copy the same emotional claim.

Baseline guardrail:

- Wavvy lyrics should be visual and indirect, but not cryptic.
- Trend alignment means speakable modern phrasing, not importing English catchphrases or famous lyric turns.
- "Poetic" is acceptable only when the sung line still feels natural in Korean.

## Bounded Pattern Dimensions For The Skill

Use these dimensions when researching or drafting. Do not store external lyric lines.

| Dimension | Baseline |
|---|---|
| Narrator | Mostly close first-person or lightly addressed second-person; avoid omniscient explanation. |
| Line unit | Short breath units; one action/image per line; verse may be denser than chorus. |
| Hook | Compact phrase-first anchor; repeat with small scene/context variations. |
| Emotional arc | Small, concrete state shift rather than dramatic confession. |
| Vocabulary | Everyday Korean plus tactile nouns; sparse English only when series concept allows. |
| Imagery | Objects, space, light, air, body rhythm, movement, color. |
| Register | Speakable, sung, non-literary; avoid diary-prose blocks and slogan writing. |
| Copyright safety | Use abstract patterns only; never copy or translate source lyric lines. |

## Genre-Specific Baseline

### Bright Pop/R&B

- Goal: immediate replay, clear chorus memory, bright major-key lift.
- Narration: conversational and lightly confident.
- Hook: repeated phrase with post-hook echo or response.
- Vocabulary: light, step, window, air, color, smile, shoulder, rhythm, speaker, street.
- Avoid: heavy heartbreak, dark room, toxic intimacy, direct commute/work/time labels unless explicitly allowed.

### Contemporary R&B

- Goal: smoother verse pocket and emotional closeness without losing Wavvy clarity.
- Narration: more intimate first-person, but still scene-based.
- Hook: melodic phrase that can stretch vocally; fewer chant-like repetitions than Pop/R&B.
- Vocabulary: hand, breath, room, glass, shadow, pulse, door, temperature, distance.
- Avoid: melodramatic confession, over-sexualized R&B cliche, stacked harmony dependency.

### Neo-Soul / Urban Neo-Soul

- Goal: groove, inner motion, tactile warmth, subtle sophistication.
- Narration: reflective but grounded in objects/actions.
- Hook: less obvious than pop but still has a repeatable phrase or cadence.
- Vocabulary: floor, lamp, cup, window, vinyl/record only if not cliche, shoulder, pocket, late light, slow color.
- Avoid: abstract thesis lines, excessive metaphor density, difficult chord language mirrored as difficult lyric language.

## Recommended Skill Output Contract

A Wavvy lyric-writing skill should produce these sections, in this order:

1. Source Map
   - Series concept, Wavvy docs, prior track/source file, and any external trend sources used.

2. Constraint Freeze
   - Series BPM/mood/genre/vocal constraints, Wavvy lyric philosophy, and explicit exclusions.

3. Lyric Strategy
   - Narrator, emotional arc, hook anchor, vocabulary lane, banned cliches, and mode choice.

4. Draft
   - Either full lyric draft with section tags or Suno prompt-only input. The mode must be named.

5. Self-Gate
   - Copyright safety, Wavvy philosophy, series DNA, Suno format, and natural Korean speech.

## Harness Baseline For Later Implementers

Research-only checks:

- Confirm no external lyric line is present in research artifacts.
- Confirm each local rule cites its owning Wavvy document.
- Confirm source-index includes accessed date, source type, relevance, and risk.

Draft-quality checks:

- The hook is identifiable without reading the whole lyric.
- The chorus opens or tightens relative to the verse.
- At least three concrete object/space/phenomenon images exist.
- Direct time/work/activity terms are absent unless the series concept explicitly permits them.
- Lines are speakable in Korean; reject awkward image stacking even if the image category is allowed.

Copyright checks:

- No copied lyric text.
- No translated lyric text.
- No distinctive famous phrase or cadence imitation.
- External sources are used only as pattern evidence.

## Open Risks

- External chart pages are volatile; the skill should record access dates and avoid depending on one chart snapshot as a permanent truth.
- Wavvy's global policy prefers prompt-only or structure prompts for Suno, while current track workflows may include full lyric files. The skill must make this mode distinction explicit to avoid policy confusion.
- "Object/space/phenomenon" can be misapplied into sterile image collage. Natural Korean speech should be a co-equal gate.
