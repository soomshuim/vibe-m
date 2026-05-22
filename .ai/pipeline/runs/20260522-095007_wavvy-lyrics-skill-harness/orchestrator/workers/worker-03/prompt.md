# Worker Prompt: worker-03

## Responsibility

Implement and verify the Wavvy lyric-skill harness/CLI gates using the approved skill contract. Own only code, tests, and implementation evidence; do not change release docs or broad SSOT prose.


## Assigned Write Scope

- `wavvy.py`
- `wavvy_harness/gate.py`
- `wavvy_harness/state.py`
- `tests/test_harness.py`
- `.ai/pipeline/runs/20260522-095007_wavvy-lyrics-skill-harness/implementation/harness.md`


## Dependency Rule

- Execution group: `serial-harness`
- Depends on: worker-02


## Instructions

- Stay strictly inside this write scope.
- Do not revert unrelated dirty files or other worker output.
- Final response must include: Result, Changed files, Verification, Risks.
