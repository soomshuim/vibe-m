# Worker Prompt: worker-02

## Responsibility

Create the Wavvy lyric-writing skill and durable skill contract from the research baseline. Own only skill/spec files; do not edit CLI, harness code, tests, or release docs.


## Assigned Write Scope

- `skills/wavvy-lyricist/SKILL.md`
- `skills/wavvy-lyricist/references/patterns.md`
- `MASTER/lyrics/skills/WAVVY_LYRIC_SKILL_SPEC.md`


## Dependency Rule

- Execution group: `serial-skill`
- Depends on: worker-01


## Instructions

- Stay strictly inside this write scope.
- Do not revert unrelated dirty files or other worker output.
- Final response must include: Result, Changed files, Verification, Risks.
