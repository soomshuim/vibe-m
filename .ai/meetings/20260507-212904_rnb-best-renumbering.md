# Team Meeting: RNB-BEST Renumbering

Date: 2026-05-07
Project: `/Users/zen/Project/wavvy`
Mode: `-team -play`

## Topic

사용자가 고른 RNB-BEST 33곡의 넘버링과 러닝 오더를 다시 정렬한다.

## Roles

- Product Leader
- Design Director
- Marketing Director
- QA Reviewer

## Decision

현재 복사된 33곡만 사용한다. 새 후보나 보류 곡은 섞지 않는다.

최종 순서는 warm-up -> groovy lift -> mixed compilation middle -> late emotional wind-down으로 둔다. 같은 원본 시리즈가 연속으로 붙지 않게 분산하고, `마음밖`/`마음안` 같은 발라드성 곡은 후반 감정선에 둔다.

## Applied Order

01. 작은 빛
02. 산책
03. 윤곽
04. 꽃비
05. 소파
06. 전화
07. 먼지
08. 물안개
09. 돛
10. 봄 꽃
11. 잠실대교
12. 눈맞춤
13. 무음
14. 꽃길
15. 약속 (Appointment)
16. 낮꿈
17. 물결
18. 봄비같은 너
19. 밤거리
20. 잔상
21. 피크닉
22. 멍
23. 진동
24. 약속 (Promise)
25. 정류장
26. 마음밖
27. 얼룩
28. 맞잡은 손
29. 마음안
30. 이름
31. 잠옷
32. 골목
33. 자장가

## Verification

- 33 audio files present.
- `concept.md` Track Selection has 33 rows.
- `python3 wavvy.py validate SERIES/RNB-BEST` passed with all 33 audio files, `input/loop.png`, `input/thumb.jpg`, and YouTube metadata.
