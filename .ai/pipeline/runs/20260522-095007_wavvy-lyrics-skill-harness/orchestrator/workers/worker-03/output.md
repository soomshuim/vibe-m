**Result**
Implemented the Wavvy lyric-skill harness and CLI gate. The new `lyrics-review` checkpoint and `lyrics-skill` command validate the worker-02 skill package and optional lyric artifacts against the approved contract.

**Changed Files**
- [wavvy_harness/gate.py](/Users/zenkim_office/Project/wavvy/wavvy_harness/gate.py:396)
- [wavvy.py](/Users/zenkim_office/Project/wavvy/wavvy.py:2164)
- [wavvy_harness/state.py](/Users/zenkim_office/Project/wavvy/wavvy_harness/state.py:263)
- [tests/test_harness.py](/Users/zenkim_office/Project/wavvy/tests/test_harness.py:249)
- [.ai/.../implementation/harness.md](/Users/zenkim_office/Project/wavvy/.ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/implementation/harness.md:1)

**Verification**
- `PYTHONPYCACHEPREFIX=/private/tmp/wavvy-pycache python3 -m py_compile wavvy.py wavvy_harness/*.py`: PASS
- `python3 -m unittest tests/test_harness.py`: PASS, 15 tests
- `python3 wavvy.py lyrics-skill SERIES/17-00 --json`: PASS
- `python3 wavvy.py gate SERIES/17-00 --stage lyrics-review --json`: PASS
- `git diff --check`: PASS

**Risks**
- `doctor --json` still fails because the existing `peer_review_script` path points to missing `/Users/zenkim_office/Project/claude-center/scripts/peer-agent-review.sh`; I did not touch that outside-scope dependency.
- `state SERIES/17-00 --check` and `gate --stage source-final` fail because current `SERIES/17-00` is still draft-level evidence, not because of the new lyric-skill gate.
- Same scoped files already had dirty compilation/source-map edits before this worker; I preserved those and layered the lyric harness changes on top.