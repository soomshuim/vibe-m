# Source Index

Generated: 2026-05-22 KST
Worker: worker-01
Purpose: source map for `lyrics-skill-baseline.md`

## Local Wavvy Sources

| ID | Source | Type | Use | Reliability | Risk / Note |
|---|---|---|---|---|---|
| L1 | `MASTER/SSOT.md` | Local SSOT | Conflict order, artifact ownership, series concept priority | High | Dirty worktree exists, but this is the project-owned SSOT loaded for the run. |
| L2 | `MASTER/lyrics/LYRICS.md` | Local lyric SSOT | Korean lyric positioning, time concept policy, Suno prompt/structure rules, tag rules | High | Governs lyric format and should override external trend advice. |
| L3 | `MASTER/MANAGER.md` | Local quality gate | Pure input, document-driven work, conservative fail policy | High | Quality fallback, not a lyric style guide by itself. |
| L4 | `wavvy.md` | Local brand identity | Korean lyrics, single lead/chest-dominant vocal, no harmonies, lyric philosophy | High | Global default; per-series concept can override only when explicit. |
| L5 | `SERIES/17-00/concept.md` | Local series concept | Bright Main Pop R&B example, major-key/hook/time-slot handling | High | Series-specific example; do not overgeneralize to all Wavvy series. |
| L6 | `.ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/research/2026-pop-rnb-lyric-patterns.md` | Prior research artifact | 2026 Pop/R&B pattern summary, lexicon lanes, copyright-safe abstraction method | Medium-high | Prior run artifact, not global SSOT. Useful as precedent. |
| L7 | `.ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/implementation/17-00-track-01-rewrite.md` | Prior implementation note | Documents the correction from awkward abstract imagery to natural spoken-pop narration | Medium-high | Implementation-specific; use as failure-mode evidence only. |
| L8 | `.ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/02-review.md` | Prior peer review | Adds Wavvy philosophy and concrete pattern-dimension gates | Medium | Review artifact; not authoritative over SSOT, but useful QA memory. |
| L9 | `.ai/pipeline/runs/20260521-233704_17-pop-rnb-lyrics-research/04-plan-review.md` | Prior plan review | Notes research source method, full-lyric vs prompt-mode ambiguity, and baseline preservation | Medium | Review artifact; used to prevent repeated process defects. |

## External Sources

| ID | Source | URL | Accessed | Use | Reliability | Copyright Handling |
|---|---|---|---|---|---|---|
| E1 | Soundcharts Spotify Global chart | https://soundcharts.com/en/charts/spotify/global | 2026-05-22 | Current streaming context; visible Pop/R&B/cross-genre/catalog mix | Medium | Chart metadata only; no lyric text used. |
| E2 | Billboard Canada Global 200 chart page | https://ca.billboard.com/charts/billboard-global-200 | 2026-05-22 | Global chart methodology and current chart context | Medium-high | Chart/methodology only; no lyric text used. |
| E3 | MusicRadar, Olivia Dean songwriting feature | https://www.musicradar.com/artists/a-barometer-is-if-i-wouldnt-say-it-out-loud-then-i-probably-wouldnt-use-it-as-a-lyric-how-olivia-deans-joyous-breakthrough-song-was-crafted | 2026-05-22 | Speakable lyric principle, reality-based writing, soul/Motown familiarity | Medium | Short attribution only; no lyric text copied. |
| E4 | MusicRadar, Ravyn Lenae / Love Me Not production feature | https://www.musicradar.com/artists/he-was-like-yeah-we-just-layered-like-10-different-guitars-to-get-that-guitar-tone-i-was-like-oh-thats-pretty-amazing-how-a-warped-sample-and-some-anderson-paak-magic-helped-ravyn-lenae-to-create-love-me-not-her-viral-hit | 2026-05-22 | Hook-first construction, classic instrumentation, artist-specific vocal spin | Medium | Used for production/songwriting pattern only; no lyric text copied. |
| E5 | Billboard Canada, Ravyn Lenae Hot 100 first-timer article | https://ca.billboard.com/music/chart-beat/ravyn-lenae-hot-100-first-timer-love-me-not-1235941197/ | 2026-05-22 | Viral path, TikTok reuse, chart growth, social-video portability | Medium-high | Chart/virality facts only; no lyric text copied. |
| E6 | Los Angeles Times, Ravyn Lenae profile | https://www.latimes.com/entertainment-arts/music/story/2025-11-19/ravyn-lenae-love-me-not-birds-eye-sabrina-carpenter-renee-rapp | 2026-05-22 | Describes runaway success and song characterization as lightly psychedelic soul | Medium | Used only as high-level context; no lyric text copied. |
| E7 | The Guardian, Olivia Dean profile | https://www.theguardian.com/music/2026/feb/28/hard-work-romance-and-bell-hooks-how-olivia-dean-became-british-pops-newest-megastar | 2026-05-22 | Pop-soul/throwback R&B context, fun/lightness, performance-driven appeal | Medium | High-level artist/style context only; no lyric text copied. |

## Excluded / Not Used

- External lyric databases and lyric pages were not used as sources.
- No Genius lyric pages were opened for lyric text.
- No copied lyric corpus was created.
- Reddit/commentary sources were not used for baseline claims.

## Source Adequacy

This source set is adequate for a bounded baseline, not for a permanent market report. It combines:

- Wavvy SSOT rules for binding constraints.
- Prior Wavvy run artifacts for project-specific failure modes.
- Current chart/context sources for 2026 popularity shape.
- Music journalism/interview sources for non-lyric songwriting patterns.

The later skill/harness implementer should keep these as baseline evidence and add new access-dated sources when applying the skill to a different year, series, or genre lane.
