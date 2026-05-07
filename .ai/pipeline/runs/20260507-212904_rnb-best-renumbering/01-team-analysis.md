# Team Analysis

## Topic

RNB-BEST 33곡의 넘버링과 러닝 오더를 사용자 선곡 이후 다시 정렬한다.

## Meeting Pattern

Team mode simulation, two-round critique.

## Roles Selected

- Product Leader: compilation의 목적과 선곡권을 보호한다.
- Design Director: 실제로 오래 틀어둘 때의 흐름과 전환감을 본다.
- Marketing Director: YouTube playlist로 보였을 때의 첫 인상과 후반 잔상을 본다.
- QA Reviewer: 파일명, 문서, 검증 결과가 서로 어긋나지 않는지 확인한다.

## Agreements

- 새 곡 추가 없이 현재 복사된 33곡만 대상으로 한다.
- 선곡 입력 순서를 유지하기보다, 하나의 best album처럼 들리는 러닝 오더를 우선한다.
- 초반은 13-00의 밝은 Urban Soul / Neo-Soul로 열어 진입 장벽을 낮춘다.
- 04-00 / 14-00의 느린 R&B는 중반의 중심부로 두어 흐름을 안정시킨다.
- 12-00 Afro-Drill / Afropiano 계열은 후반 직전의 에너지 리프트로 둔다.
- 마지막은 18-00 / 22-00의 밤, 휴식, slow jam 곡으로 내려오며 `자장가`로 닫는다.

## Conflicts

- Afro 계열을 맨 끝에 둘 수도 있으나, R&B BEST의 반복 청취감과 닫힘을 해칠 수 있다.
- `약속`이 두 곡이라 혼동 가능성이 있지만, source와 filename mood가 달라 현재 표기 유지가 낫다.

## Recommendation

Warm urban soul -> city neo-soul -> soft/slow R&B -> Afro lift -> late-night slow jam 순으로 재번호를 확정한다.

## Next Actions

1. 파일명을 새 순서에 맞춰 `NN__...`로 2단계 rename한다.
2. `concept.md` Track Selection과 YouTube Track List를 같은 순서로 갱신한다.
3. `wavvy.py validate`와 문서-파일 매칭 검사를 실행한다.
