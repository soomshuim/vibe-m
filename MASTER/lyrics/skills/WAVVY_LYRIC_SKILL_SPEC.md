# Wavvy Lyric Skill Spec

Version: 0.1
Last Updated: 2026-05-22
Owner: `MASTER/lyrics/LYRICS.md` policy layer
Skill: `skills/wavvy-lyricist/SKILL.md`

## Purpose

Define the durable contract for the Wavvy lyric-writing skill and the later harness checks that validate it. This spec does not replace `MASTER/lyrics/LYRICS.md`; it narrows how agents should draft, rewrite, or review Wavvy lyrics.

## Authority And Scope

Applicable tasks:

- Writing or rewriting a Wavvy track lyric.
- Producing Suno Lyrics input for a Wavvy track.
- Reviewing a Wavvy lyric draft for policy, style, or copyright safety.
- Creating genre/time-slot lyric guidance for a series.

Conflict order:

1. `MASTER/SSOT.md`
2. Target `SERIES/[series]/concept.md`
3. `MASTER/lyrics/LYRICS.md`
4. `MASTER/MANAGER.md`
5. `wavvy.md`
6. This spec
7. `skills/wavvy-lyricist/references/patterns.md`

If this spec conflicts with a higher-priority source, the higher source wins.

## Required Skill Files

The lyric skill is complete only when these files exist:

- `skills/wavvy-lyricist/SKILL.md`
- `skills/wavvy-lyricist/references/patterns.md`
- `MASTER/lyrics/skills/WAVVY_LYRIC_SKILL_SPEC.md`

The skill file must reference both this spec and the patterns reference.

## Source Requirements

Every new draft, rewrite, or review must identify:

- Wavvy authority files used.
- Target series concept path.
- Target track/source file when one exists.
- Research artifact or external sources if current trend claims are used.
- Access date for any new external source.

External lyric pages are not required and should be avoided. If external songs are researched, record only abstract patterns, metadata, interviews, chart context, or production/narration commentary. Do not store lyric text.

## Output Modes

### `full-lyric-draft`

Use for track files, rewrite proposals, and human review.

Allowed:

- Korean lyric rows.
- Structure tags such as `[Intro]`, `[Verse]`, `[Pre-Chorus]`, `[Chorus]`, `[Post-Chorus]`, `[Bridge]`, `[Outro]`.
- Short notes outside the draft explaining mode, constraints, and gate results.

Not allowed:

- Treating the full lyric as Suno prompt-only input without saying so.
- Embedding production directions as lyric rows.
- Using harmony/backing-vocal dependency to compensate for weak writing.

### `suno-prompt-only`

Use for direct Suno Lyrics input.

Allowed:

- 1-3 short English direction lines.
- Structure-only tags or compact structure line such as `I-V1-PC-C-PC2-V2-C-B-C-O`.
- Brief mood/theme/image keywords.

Not allowed:

- Full Korean lyric rows.
- Parenthesized prompt-only text such as `(Scene: ...)`.
- Production instructions that belong in the style prompt.

### `review-only`

Use when judging an existing lyric without drafting a replacement.

Required:

- Findings tied to source rules.
- Verdict: `PASS`, `HOLD`, or `FAIL`.
- Minimum viable fix direction for every `HOLD` or `FAIL`.

## Required Output Schema

For `full-lyric-draft` and `suno-prompt-only`, output sections in this exact order:

1. `Source Map`
2. `Constraint Freeze`
3. `Lyric Strategy`
4. `Draft`
5. `Self-Gate`

For `review-only`, output sections in this exact order:

1. `Source Map`
2. `Constraint Freeze`
3. `Findings`
4. `Verdict`

## Constraint Freeze Fields

Include all fields that are known:

- `series`
- `track`
- `mode`
- `genre_lane`
- `bpm`
- `key`
- `mood`
- `vocal_identity`
- `language_policy`
- `time_activity_policy`
- `explicit_overrides`
- `copyright_boundary`

Unknown fields should be marked `unknown`, not guessed.

## Lyric Strategy Fields

For drafts and rewrites, state:

- `narrator`
- `emotional_arc`
- `hook_anchor`
- `vocabulary_lane`
- `density`
- `banned_cliches`
- `suno_handling`

## Self-Gate Contract

Each gate must be marked `PASS`, `HOLD`, or `FAIL` with one concise reason.

| Gate | PASS Standard |
|---|---|
| Copyright Safety | No copied, translated, closely paraphrased, or famous-cadence material. |
| Wavvy Identity | Korean lyric identity, single lead, chest-dominant direction, no harmony dependency. |
| Series DNA | Aligns with concept BPM, key, mood, genre, and vocal constraints. |
| Time Policy | Direct time/activity terms are absent unless explicitly allowed. |
| Lyric Philosophy | Uses object/space/phenomenon and inferred emotion instead of explanation/slogans. |
| Natural Korean | Lines are speakable and singable; no awkward abstract image stacking. |
| Hook Clarity | Hook anchor is identifiable where the genre lane requires one. |
| Suno Format | Output mode follows `MASTER/lyrics/LYRICS.md` exactly. |

Any `FAIL` blocks handoff as final lyric output. Any `HOLD` requires a named next fix.

## Harness Acceptance Baseline

A file-level harness may validate the skill package with static checks:

- Required files exist.
- `SKILL.md` front matter contains `name: wavvy-lyricist`.
- `SKILL.md` names all three output modes.
- `SKILL.md` contains the required output section labels.
- `patterns.md` states that copied/translated external lyric lines are not stored.
- This spec defines `Self-Gate Contract` and `Harness Acceptance Baseline`.

A lyric-artifact harness may validate draft output with text checks and manual review prompts:

- Required output sections appear in order.
- Mode is named exactly once in `Constraint Freeze`.
- `suno-prompt-only` output contains no full Korean lyric rows.
- Direct time/activity terms are rejected unless the concept has an explicit override.
- At least three concrete object/space/phenomenon images appear for full lyric drafts unless the genre lane is intentionally minimal.
- Hook anchor is present for Pop/R&B, Contemporary R&B, and bright mainstream lanes.
- Copyright Safety gate is present and not omitted.

Static checks are necessary but not sufficient. Natural Korean speech and copyright similarity require human or reviewer judgment when risk is non-trivial.

## Release Note Requirement

When this skill is changed after initial creation, release/session documentation should record:

- Why the skill changed.
- Which source rule or user feedback caused the change.
- Whether harness expectations changed.

Do not update release/session docs from worker roles unless explicitly assigned that write scope.
