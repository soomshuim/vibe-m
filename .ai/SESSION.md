# Session State — Wavvy

> Last updated: 2026-03-21

## 진행 중

- **12-00 Korean Afrobeats 시리즈** — Suno 자체 작사 방식 전환 완료 (2026-03-14)
  - ✅ 워크플로우 리팩토링: 풀 가사 작성 → 작사 프롬프트 / 비움
  - ✅ LYRICS.md v4.0 (§1 Lyric Prompt Guide 신규)
  - ✅ WORKFLOWS.md v2.0 (6단계 → 3단계)
  - ✅ RUBRIC 가사→보컬 체크리스트 전환 (L1-19 → V1-5)
  - ✅ Track 01-04 제목 변경 + 가사 제거
    - 01 한낮 (Haze), 02 먼지 (Dust), 03 볕 (Sunlit), 04 무음 (Mute)
  - ✅ REFERENCE_SAMPLE.md, FAILURE_CASES.md 삭제
  - ✅ 잔존물 정리: lessons-learned dead 섹션 삭제 + SESSION stale 메모 제거
  - ✅ Track 03 "볕 (Sunlit)" 작사 프롬프트 작성 (198자, 풀 구조+DNA)
  - ✅ LYRICS.md §1.2 소괄호 금지 규칙 반영
  - ✅ LYRICS.md v4.1 — §1.4 약칭 구조 포맷 추가 (I-V-PC-C 등, Suno 인식 확인)
  - ✅ Track 03 Suno 테스트: 가사 생성됨, "아침" 톤 이슈 발견 → noon 키워드 보강 필요
  - ✅ Track 04 "무음 (Mute)" 작사 프롬프트 + 스타일 단일 라인화 (2026-03-16)
  - ✅ Track 05 "갈증 (Thirst)" 신규 디자인 (E, 104, Ab Major) — 스타일 톤 조정 (dark→heavy groove)
  - ✅ Track 06 "낮 그림자 (Noon Shadow)" 신규 디자인 (E, 107, Bb Minor) → Male로 변경
  - ✅ Track 07 "낮꿈 (Daydream)" 신규 디자인 (E, 102, Db Major, Female)
  - ✅ Track 04 Suno 테스트 PASS — 가사 자체 생성 품질 우수 (만트라+서사 대비 구조)
  - ✅ Track 05-07 Suno 테스트 PASS (2026-03-16)
  - ✅ Track 08 "차가워진 (Cold At Noon)" 신규 디자인 (D, 112, E Minor, Male, djembe bass) + Suno PASS
  - ✅ Track 09 "맥박 (Pulse)" 신규 디자인 (E, 106, F# Major, Female) + Suno PASS (2026-03-17)
  - ✅ Track 10 "잔상 (Afterimage)" 신규 디자인 (E, 108, A Minor, Male) + Suno PASS (2026-03-17)
  - ✅ Track 11 "그늘 (Shade)" 신규 디자인 (E, 100, B Major, Instrumental) + Suno PASS (2026-03-17)
  - ✅ Track 12 "기다림 (Waiting)" 신규 디자인 (D, 105, D Minor, Female) + Suno PASS (2026-03-17)
  - Track 01-02는 Empty 모드 확정 (가사 없이 PASS)
  - 보컬 비율 변경: Female 70/Male 30 → **Female 60/Male 40** (F9:M6)
  - ✅ Track 13 "정오의 균열 (Midday Crack)" 신규 디자인 (E, 110, Eb Minor, Male) + Suno PASS (2026-03-18)
  - ✅ STYLE.md §0.6 Articulation First 규칙 추가 + 전곡 반영 (2026-03-18)
  - ✅ Track 14 "설렘 (Flutter)" 디자인 (E, 104, G Major, Female) (2026-03-18)
  - ✅ **20곡 확장 결정** — Team Meeting (Product/Design/Strategy) 전원 합의 (2026-03-18)
  - ✅ Track 15-20 디자인 완료 + 프롬프트 파일 생성 (2026-03-18)
    - 15 온기 (Warmth) — E, 107, A Major, F
    - 16 미열 (Low Fever) — D, 103, F# Minor, F
    - 17 진동 (Vibration) — E, 109, C Minor, M
    - 18 얼룩 (Stain) — E, 102, Db Major, F (Track 07 동일 스타일)
    - 19 폭발 (Burst) — E, 111, B Minor, M
    - 20 고요 (Stillness) — D, 100, F Major, F
  - ✅ concept.md v5.0 — 20트랙 확장 + 배분 규칙 업데이트
  - Track 01-02는 Empty 모드 확정 (가사 없이 PASS)
  - 보컬 비율: **F12:M7:Inst1** (60:37:5)
  - 4막 구조: 기(01-05) → 승(06-10) → 전(11-15) → 결(16-20)
  - ✅ Track 14 "설렘 (Flutter)" Suno PASS (2026-03-18)
  - ✅ Track 15 "온기 (Warmth)" 사용자 직접 가사 작성 + Suno PASS (2026-03-18)
    - Chorus 중심 영한 혼합 가사, Verse/Pre-Chorus/Outro instrumental
  - ✅ Track 18 "얼룩 (Stain)" → Track 07 동일 스타일로 변경 (D→E, Afropiano→Afro-Drill, 102 BPM, Db Major) (2026-03-19)
  - ✅ Track 18 Suno PASS (2026-03-19)
  - ✅ Track 19 "폭발 (Burst)" LYRICS QA 트리밍 208→196자 (2026-03-19)
  - ✅ Track 16-19 Suno PASS (2026-03-20) — Track 19 제목 터짐→폭발 변경
  - ✅ Track 20 "고요 (Stillness)" Instrumental 전환 + PASS (2026-03-20)
  - **현황: 20/20 트랙 PASS (Track 11, 20 Instrumental)**
  - ✅ 썸네일 확정 — 밀림 젬베 + god rays (Team Meeting 3회, Image 3 선택) (2026-03-20)
  - ✅ WAV 파일 리네이밍 — `XX__제목__감정__장르__BPM.wav` 컨벤션 적용 (20곡) (2026-03-20)
  - ✅ TXT 제목 동기화 — Track 06/08/13 원본 제목 반영 (2026-03-20)
  - ✅ 루프 영상 제작 — 팔린드롬 (0.5배속 + 정방향/역방향), god rays 빛 움직임 (2026-03-21)
  - ✅ vfade PASS — 로고 오버레이 (96,68), 크로스페이드 0.5s (2026-03-21)
  - ✅ **PACK COMPLETE** — final.mp4 102.7분, 20곡 x2, -14 LUFS (2026-03-21)
  - ✅ concept.md v5.1 — YouTube 메타데이터 완성 ("리듬 맛집" 컨셉) (2026-03-21)
  - ✅ 워크플로우 보완 2건 — WAV 네이밍 컨벤션 + YouTube 설명 참조 규칙 (2026-03-20/21)
- **MASTER 문서 v3.2 완료** — Writing Formula + 워크플로우 분리 (2026-03-08)

## 다음 할 일

- [x] ~~Track 20 Suno 테스트~~ → Instrumental PASS (2026-03-20)
- [x] ~~썸네일 제작~~ → 밀림 젬베 확정 (2026-03-20)
- [x] ~~PACK~~ → 102.7분 완성 (2026-03-21)
- [x] ~~YouTube 메타데이터~~ → concept.md v5.1 (2026-03-21)
- [ ] YouTube 업로드
- [ ] Shorts 제작 (하이라이트 트랙 선정)

## 핸드오프 메모

- 채널 브랜딩: `wavvy.md` §7 참조
- 12-00 final.mp4: `SERIES/12-00/output/final.mp4` (102.7분)
- 썸네일 원본: `SERIES/12-00/input/thumb.psd`
