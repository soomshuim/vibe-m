**Result**

Claude activity check: Claude-like process was not detected; repo has existing dirty `.ai/` pipeline/review artifacts, so I treated this as shared work and made no edits.

Read-only evidence says the minimum local shim is likely:

`/Users/zenkim_office/Project/wavvy/.claude/commands/write.md`

That single project-local Claude command should cover Claude Code `/write`, and per the provided Codex trigger policy, Codex `-write` should also resolve through the same project-local `.claude/commands/write.md` command match. I found no existing local or global `write.md` command.

The shim should stay thin and route only lyric writing/rewrite/review to:
- [skills/wavvy-lyricist/SKILL.md](/Users/zenkim_office/Project/wavvy/skills/wavvy-lyricist/SKILL.md:2)
- [MASTER/lyrics/skills/WAVVY_LYRIC_SKILL_SPEC.md](/Users/zenkim_office/Project/wavvy/MASTER/lyrics/skills/WAVVY_LYRIC_SKILL_SPEC.md:14)
- [MASTER/lyrics/LYRICS.md](/Users/zenkim_office/Project/wavvy/MASTER/lyrics/LYRICS.md:98)
- CLI checks at [wavvy.py](/Users/zenkim_office/Project/wavvy/wavvy.py:2164)

**Changed Files**

None. No write scope was assigned, so I did not create `changed-files.txt` or `output.md`.

**Verification**

Passed:
- `python3 -m unittest tests/test_harness.py`
- `python3 wavvy.py lyrics-skill --json`
- `PYTHONPYCACHEPREFIX=/private/tmp/wavvy-pycache python3 -m py_compile wavvy.py wavvy_harness/*.py`
- `git diff --check`
- Command discovery: `.claude/commands/write.md` and `commands/write.md` are both currently missing.

Note: plain `python3 -m py_compile ...` initially failed because Python tried to write bytecode under `~/Library/Caches`, outside the sandbox. Re-running with `PYTHONPYCACHEPREFIX=/private/tmp/wavvy-pycache` passed.

**Risks**

Main implementation risk is over-routing: `/write` / `-write` should explicitly reject or redirect YouTube copy, concept docs, changelog/session docs, and non-lyric prose. Durable docs should not be updated by worker roles unless the integrator assigns that scope; the lyric spec explicitly says worker roles should not update release/session docs without assigned write scope.