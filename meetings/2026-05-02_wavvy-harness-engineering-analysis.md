# Wavvy Harness Engineering Analysis

- **Date**: 2026-05-02
- **Mode**: Team Mode — Problem Solving / Architecture Review
- **Topic**: Wavvy 프로젝트를 하네스 엔지니어링 관점에서 분석하고, 자동화 가능한 운영 하네스 방향을 정한다.
- **Roles**: AI Ops Expert, Engineering Lead, Product Leader, QA Reviewer

---

## Topic

Wavvy는 한국어 가사 플레이리스트 제작 프로젝트이면서, 실제로는 음악 기획, Suno 프롬프트, 오디오/비디오 패키징, YouTube 업로드 문안, 자막, 상태 기록을 한 워크스페이스에서 운영하는 장기 실행 에이전트 프로젝트다.

따라서 평가 기준은 "좋은 문서가 있는가"가 아니라, 같은 상태에서 다른 에이전트가 재개해도 안전하게 같은 다음 행동을 선택하고, 실행 후 결과를 검증하며, 실패를 다음 eval/skill로 환류할 수 있는가다.

---

## Meeting Pattern

Problem Solving + Feature Review.

하네스 엔지니어링 5축을 기준으로 봤다.

| Lens | 현재 판단 |
|---|---|
| Accuracy | `validate`, `finalize-upload`, 장르별 rubric 등 정확도를 높이는 도구가 있다. 다만 게이트가 통합되지 않아 작업 종류별 누락이 생긴다. |
| Reproducibility | 파일명 규칙, report/provenance, concept Final Track Sources가 강점이다. 그러나 run manifest와 artifact freshness check가 없다. |
| Safety | txt 삭제 guard, validate fail-fast, `finalize-upload --check`는 좋다. mutating command의 approval/side-effect matrix는 약하다. |
| Durability | `.ai/SESSION.md`, `.ai/HANDOFF.md`, git history가 있다. 하지만 active state가 기계 판독 가능하지 않고 오래된 TODO가 섞인다. |
| Improvability | peer review run과 lessons-learned는 있다. trace/eval/failure dataset으로 자동 환류되는 구조는 아직 없다. |

---

## Roles Selected

### AI Ops Expert

하네스 8대 계층 기준으로 Wavvy는 "정책/문서"와 "일부 도구"는 강하지만, "상태", "평가", "관측성"이 약하다.

| Layer | Current | Gap | Priority |
|---|---|---|---|
| 1. 정책/지침 | `wavvy.md`, `CLAUDE.md`, `MASTER/*` | per-series override contract 부족 | P1 |
| 2. 오케스트레이션 | 수동 workflow + handoff | machine-readable current phase 없음 | P0 |
| 3. 도구/프로토콜 | `wavvy.py`, shell gates | `doctor/gate/state` 통합 CLI 없음 | P0 |
| 4. 워크스페이스 | `SERIES/*/input/work/output` | run manifest, stale artifact guard 없음 | P1 |
| 5. 메모리/상태 | `.ai/SESSION.md`, `.ai/HANDOFF.md` | append-only라 active TODO 오염 | P0 |
| 6. 평가/검증 | validate, rubric scripts, peer review | capability/regression suite 분리 없음 | P1 |
| 7. 관측성 | provenance/report 일부 | tool version, command, duration, trace 없음 | P2 |
| 8. 거버넌스/보안 | 일부 사용자 확인 규칙 | mutating/read-only command 구분 불명확 | P1 |

가장 중요한 결론: Wavvy의 다음 개선은 "더 많은 지침"이 아니라 `.ai/state.json` + `wavvy.py state/gate/doctor` 같은 실행 가능한 state/gate 하네스다.

### Engineering Lead

`wavvy.py`는 2,891줄 단일 파일로 CLI, FFmpeg orchestration, metadata parsing, upload archive, shorts rendering을 모두 가진다. 지금 당장 대규모 분해보다, 하네스 표면을 추가하고 위험한 실행 경로를 gate로 감싸는 편이 낫다.

구체적 결함:

- `pack`은 output artifact writer return value를 확인하지 않아 `provenance.md`, `upload.csv`, `report.json` 실패 후에도 성공처럼 끝날 수 있다.
- `pack`은 validation 전에 일부 video preprocessing을 수행할 수 있어 실패 시 입력 폴더에 임시 산출물이 남을 수 있다.
- `preview`는 image mode validation을 통과해도 render 단계에서 `paths.loop_video`를 사용해 image-only 시리즈가 실패할 가능성이 있다.
- `report.json`의 `crossfade_reduction`은 repeat=2일 때 음수로 기록된다. 현재 20-00 report는 `-3922.52`다. 올바른 계산은 `sum(original_duration) * repeat - final_duration`이며 20-00의 기대값은 약 `31.20s`다.
- spec drift가 있다: CLI banner의 `VIBEM`, spec의 `final.mp4`, 구현의 `final.mkv`, 문서의 `--use-xfade`가 서로 맞지 않는다.
- shell gates는 유용하지만 Python CLI에 연결되지 않았고, 20-00 Final 상태에서는 txt가 삭제되어 `check_series_gate.sh`가 바로 실패한다.

Engineering recommendation: 먼저 새 대형 abstraction보다 작은 deterministic command를 추가한다.

1. `doctor`: 환경과 의존성 점검.
2. `state`: 현재 series 상태와 artifact availability 점검.
3. `gate`: validate + state + 선택적 rubric/script + media artifact checks 통합.

### Product Leader

Wavvy의 product problem은 "음악을 만드는 것"만이 아니라 "한 시리즈의 제작 상태를 에이전트가 오판하지 않게 하는 것"이다.

현재 사용자에게 가장 비싼 실패는 다음 세 가지다.

1. 이미 FINAL인 20-00을 draft 상태로 오판해 불필요한 Suno/가사 작업을 다시 하는 것.
2. `final.mkv`가 없는데 업로드 단계로 착각하는 것.
3. subtitle/upload/finalize 같은 upload-final 단계에서 어떤 artifact가 authoritative인지 놓치는 것.

따라서 MVP 범위는 신규 기능보다 "active state + upload readiness"가 먼저다. 성공 지표는 다른 에이전트가 `-wavvy` 후 `wavvy.py state SERIES/20-00 --check`만 보고 다음 행동을 정확히 말할 수 있는 것이다.

### QA Reviewer

현재 PASS라고 말할 수 있는 항목:

- `python3 -m py_compile wavvy.py` PASS.
- `python3 wavvy.py validate SERIES/20-00` PASS.
- 20-00은 20개 WAV, loop image, thumb, YouTube metadata를 갖고 있다.
- `concept.md > Final Track Sources`가 존재한다.

현재 FAIL 또는 보완 필요:

- `bash MASTER/scripts/check_series_gate.sh SERIES/20-00`는 txt 삭제 상태에서 `ERROR: 트랙 파일 없음`으로 실패한다. Final 상태용 gate가 없다.
- 20-00 `concept.md`는 Final Track Sources와 FINAL metadata가 있으면서 Series Status는 `12 PASS + 8 draft`를 유지한다.
- `output/final.mkv`와 `upload.csv`는 현재 없다. `report.json`과 subtitle txt/srt는 ignored local output에 존재한다. 단, 이는 `source_final` 상태에서는 실패가 아니며, `render_final` 또는 `upload_ready` 단계에서만 blocker로 취급해야 한다.
- `tools/`에는 실질 도구가 없고 `.DS_Store`만 있다.

---

## Agreements

- Wavvy는 이미 문서 기반 운영 문화가 강하다. `wavvy.md`, `MANAGER.md`, `WORKFLOWS.md`, `YOUTUBE.md`, per-series `concept.md`의 계층은 유지한다.
- `finalize-upload`는 좋은 하네스 패턴이다. "소스 txt + report.json -> concept Final Track Sources" 전환은 다른 단계에도 재사용할 만하다.
- 다음 개선은 문서 추가보다 실행 가능한 deterministic checks가 우선이다.
- 상태는 `.ai/SESSION.md`만으로 부족하다. active state를 기계 판독 가능한 파일로 분리해야 한다.
- peer review는 이미 agent-center에 있으므로 새로 만들기보다 `peer-agent-review.sh`를 재사용한다.

---

## Conflicts

| Role | Position | Trade-off |
|---|---|---|
| AI Ops Expert | `.ai/state.json`과 run manifest를 먼저 만들어야 한다. | 운영 안정성은 커지지만 구현 범위가 늘어난다. |
| Engineering Lead | 지금은 `wavvy.py`를 크게 분해하지 말고 gate command부터 붙여야 한다. | 구조 개선은 미뤄지지만 회귀 위험이 낮다. |
| Product Leader | 사용자가 바로 체감할 upload readiness/check가 우선이다. | 내부 trace/observability는 후순위가 된다. |
| QA Reviewer | Final 상태용 gate 없이는 PASS 판정을 낼 수 없다. | 기존 txt 기반 gate와 Final archive 기반 gate를 나눠야 한다. |

---

## Recommendation

Wavvy용 하네스 셋팅은 다음 순서로 한다.

1. **Active State Contract**
   - `.ai/state.json` 추가.
   - 현재 series, phase, next_action, artifact_status, authoritative_docs, blocked_by를 기록.
   - `.ai/HANDOFF.md`는 당장 demote하지 않는다. SessionStart/UserPromptSubmit hook이 HANDOFF를 읽는 기존 계약이 있으므로, state 파일은 resume source를 보강하고 HANDOFF에는 active summary를 계속 남긴다.
   - phase enum을 명시한다: `concept_draft`, `track_source_draft`, `source_final`, `render_final`, `upload_ready`, `published`.
   - 20-00의 현재 phase는 `source_final`이다. `final.mkv` 부재는 `upload_ready=false`로 표시하되 `source_final` 자체를 FAIL 처리하지 않는다.
   - writer는 `wavvy.py state`만 허용하고, state write는 temp file + atomic rename으로 처리한다.

2. **SSOT Contract**
   - `MASTER/SSOT.md` 추가.
   - `wavvy.md`, `MANAGER.md`, `WORKFLOWS.md`, `YOUTUBE.md`, `concept.md`, `.ai/state.json`, output artifacts의 owner/scope/conflict order를 명시.
   - 문서만 추가하면 stale해질 수 있으므로 `wavvy.py state --check`가 SSOT conflict를 검사해야 한다.

3. **Deterministic Gate Surface**
   - `wavvy.py doctor`: ffmpeg/ffprobe/ffmpeg_normalize/git/font/disk/output writability 점검.
   - `doctor`는 cross-repo dependency인 `~/Project/agent-center/scripts/peer-agent-review.sh`도 점검한다.
   - `wavvy.py state SERIES/20-00 --check --json`: concept/report/artifact/current-state drift 점검.
   - `wavvy.py gate SERIES/20-00 --stage source-final|render-final|upload-ready --json`: validate + final archive + artifact readiness + stale TODO scan 통합.
   - Final archive 이후에는 txt 기반 `check_series_gate.sh`를 다시 실행하지 않는다. 대신 pre-finalize rubric result를 `report.json` 또는 `rubric_snapshot.json`에 저장하고 post-final gate가 그 snapshot을 검증한다.

4. **Final State Cleanup**
   - 20-00 `concept.md`에서 현재 FINAL 상태와 충돌하는 draft status/TODO를 historical note로 내리거나 명시적으로 stale로 표시.
   - `output/final.mkv`가 없다는 사실을 state/gate가 `render_artifact_missing`으로 표시한다. `source_final`에서는 warning, `upload-ready`에서는 blocker다.
   - `pack`의 artifact writer return value를 확인하도록 고친다. `generate_provenance`, `generate_upload_csv`, `generate_report` 중 하나라도 실패하면 PACK은 실패해야 한다.
   - `generate_report`의 `crossfade_reduction` 계산을 repeat-aware로 수정한다. 기존 historical report backfill은 선택 사항이며, gate는 stale report를 warning으로 표시한다.

5. **Cross-Project Pipeline Harness**
   - `agent-center/scripts/peer-agent-review.sh`를 peer gate API로 재사용.
   - `team`/`director`는 직접 slash/hyphen trigger로 부르지 않고 artifact-mode adapter로 감싼다.
   - run directory: `.ai/pipeline/runs/YYYYMMDD-HHMMSS_<slug>/`.
   - stages: `team_analysis -> claude_review -> plan -> claude_plan -> director_implementation`.
   - 각 stage는 입력 artifact, 출력 artifact, verdict, exit code를 `run.json`에 남긴다. 내부 stage에서는 `peer-agent-review.sh --no-handoff`를 기본으로 쓰고, 최종 성공 시에만 summary handoff/record를 남긴다.

6. **Code Organization**
   - `wavvy.py`가 이미 2,891줄이므로 신규 하네스 로직은 별도 helper module에 둔다.
   - 단, 기존 CLI entrypoint 호환성은 유지한다: 사용자는 계속 `python3 wavvy.py state|doctor|gate ...`로 실행한다.

---

## Next Actions (3)

1. 이 분석 파일을 `-claude-review` 게이트로 보내고, Claude finding을 반영해 분석을 보완한다.
2. 보완된 분석을 바탕으로 plan gate를 통과시킨다. 당시 draft plan 파일은 이후 구현/record 산출물로 대체되어 제거됐다.
3. PASS된 플랜의 MVP 범위만 Director mode로 구현한다: `MASTER/SSOT.md`, `.ai/state.json`, Wavvy state/gate/doctor 중 P0 command, 그리고 cross-project pipeline harness spec.

---

## Claude Review Resolution

Claude review result: `NEEDS_USER_DECISION`, high confidence.

Accepted changes:

- Final semantics split: `source_final` / `render_final` / `upload_ready` / `published`.
- 20-00 current phase: `source_final`.
- Missing `final.mkv` is not a source-final failure. It is a render/upload readiness blocker.
- HANDOFF is not demoted until agent-center hooks are updated or a generator exists.
- `.ai/state.json` needs schema, single writer, and atomic writes.
- `pack` artifact writer return values and `crossfade_reduction` are P0 code fixes.
- Post-final rubric gates need snapshots because txt sources are intentionally deleted after finalize.
- Cross-project pipeline must specify stage IO and pass/fail signals.
- `preview` image-mode issue is supported by `wavvy.py:2086-2090`, where preview always calls `render_video(..., paths.loop_video, ...)`.

Deferred:

- Full `wavvy.py` package split. New harness logic should live outside the monolith, but a full CLI refactor is not required for MVP.
- Backfilling historical `report.json` files. Gate may warn; regeneration can refresh reports when needed.

---

*Generated by Lenny's Product Team — Team Mode*
