# Pending User Requests Snapshot

Source: latest non-duplicate user messages from the Codex session JSONL.

Use this as the authoritative queued work before older `.ai/HANDOFF.md` or `.ai/SESSION.md` TODOs. If these requests include a `-play`, `-director`, or clarification of a previous request, continue that work instead of selecting an older TODO.

## Request 1

- Timestamp: `2026-06-02T10:12:57.927Z`
- Source: `response_item`

```text
<hook_prompt hook_run_id="stop:0:/Users/zen/.codex/hooks.json">최종 답변 차단: 전문 용어 설명 정규화 필요

이전 답변 전체를 반복하지 마세요. 사용자에게 이미 보였을 수 있습니다.
짧은 수정 메모만 제출하세요. 누락된 용어는 아래 첫 등장 위치 기준으로 설명하세요.

누락 항목:
- missing_term: artifact(작업 결과로 남는 산출물)
  term: "artifact"
  first_seen:
    line: 13
    region: "body"
    context: "3. **artifact policy(산출물 보존 정책)는 현재 20-00에는 맞지만 repo-wide로는 아직 legacy gap이 큽니다.**"
    snippet: "3. **artifact policy(산출물 보존 정책)는 현재 20-00에는 맞지만 repo-wide로는 아직 legacy gap이 큽니다.**"
  권장 수정: 첫 등장 위치에서 설명을 붙이세요.</hook_prompt>
```

## Request 2

- Timestamp: `2026-06-02T10:23:10.042Z`
- Source: `response_item`

```text
하네스나 실제 작동하는 정책과 문서를 오염시키거나 삭제시키지 않는 내에서 정리해줘 -director
```

## Request 3

- Timestamp: `2026-06-02T10:26:15.407Z`
- Source: `response_item`

```text
<hook_prompt hook_run_id="stop:0:/Users/zen/.codex/hooks.json">최종 답변 차단: 전문 용어 설명 정규화 필요

이전 답변 전체를 반복하지 마세요. 사용자에게 이미 보였을 수 있습니다.
짧은 수정 메모만 제출하세요. 누락된 용어는 아래 첫 등장 위치 기준으로 설명하세요.

누락 항목:
- missing_term: peer review(동료/별도 에이전트 검토)
  term: "peer review"
  first_seen:
    line: 18
    region: "body"
    context: "그래서 아직 final PASS/record/commit은 하지 않았습니다. 현재 git 상태는 tracked diff(변경 차이) 2개 파일 + peer review 결과 `untracked`(git이 아직 추적하지 않는 파일) 2개입니다."
    snippet: "그래서 아직 final PASS/record/commit은 하지 않았습니다. 현재 git 상태는 tracked diff(변경 차이) 2개 파일 + peer review 결과 `untracked`(git이 아직 추적하지 않는 파일) 2개입니다."
  권장 수정: 첫 등장 위치에서 설명을 붙이세요.</hook_prompt>
```

## Request 4

- Timestamp: `2026-06-02T10:50:44.676Z`
- Source: `response_item`

```text
이제 constitution 문서가 너무 길어서 맥락이 오염되거나 ai가 대충 훑을 가능성이 있는 문서를 찾아줘
```

## Request 5

- Timestamp: `2026-06-02T10:57:16.868Z`
- Source: `response_item`

```text
매번 읽는 문서가 아닌 기록용이나 참고용 문서는 길어도 괜찮나?
```
