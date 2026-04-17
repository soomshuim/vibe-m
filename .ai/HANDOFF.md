---
HANDOFF: Claude -> User
Date: 2026-04-17 23:49:49
Project: ~/Project/wavvy
Agent: Claude
Summary: 15-00 Track 06-10 확정 + 시리즈 스타일 전면 재조정. Track 06 "벚꽃 소다 봄길"(Bubbly Doowop Pop R&B 120 F Eb, Meghan Trainor "Dear Future Husband" 리서치 후 전면 교체, "한 바퀴 더" 대체), Track 07 "달려가는 중"(Warm R&B 116 F Am ★ 예외, "비상등" 대체), Track 08 풀 가사(Neo-Soul 유지), Track 09 "잔디에 누워" 재설계(Lo-fi Chill Hop 112 M F, 제목 "봄" 제거, BPM 사용자 92→112), Track 10 "믹스테잎"(Lo-fi chill Pop Doowop 122 F C, 제목 표기 변경). Track 01 Contemporary R&B Cruise 스타일 재설계(가사 유지), 02/03 제목 변경(라디오 온→라디오를 켜고, 조수석→곁에서). A/D축 Template 재정의(Track 06/02 앵커), "Retro" 라벨 전수 제거(08/16), 브라스/호른 미확정 6곡 제거(11/12/14/16/17/18). 배분 재집계: A 4곡 + ★ 예외 3곡(01/07/09) / B 5곡 / C 5곡 / D 3곡, 보컬 F11:M7:Duet2. 리서치 리포트 `report/2026-04-17_track06-dear-future-husband.md` (신뢰도 93%, 23 소스) 생성.
Next-TODO: Track 11-20 Suno 테스트 순차 진행. 시리즈 전반 "질림" 이슈 해소 위해 variety 축(BPM/mood 대조 트랙) 추가 검토. 시리즈 정체성 "Korean Retro R&B Drive" 라벨 내 Retro 단어 잔존 — 사용자 결정 대기. 차기 시리즈 "Korean Hip-hop Drive" 기획 검토 가능.
Commits: (이번 커밋)
---

---
HANDOFF: Claude -> User
Date: 2026-04-17 15:52:51
Project: ~/Project/wavvy
Agent: Claude (+ 사용자 직접 제작 4곡)
Summary: 15-00 "오후 3시, 라디오" 신규 시리즈 기획 v0.1~v0.2. Korean Retro R&B Drive 컨셉 (13-00과 씬 분리: 걷는 산책 vs 달리는 드라이브), 장르 4축 믹스 (A Doowop 25% / B Funk-R&B 30% / C Neo-Soul 25% / D Modern K-R&B 20%), 보컬 F10:M8:Duet2 (5:5), BPM 108-126. 사용자 제작 4곡 (Track 01 오렌지 드라이브 Doowop F / 04 오늘 드라이브 Funk-R&B M Eb Major / 05 봄 냄새 Neo-Soul F D Major / 09 봄 잔디에 누워 K-R&B M) 포함 20트랙 Track Map 확정. 신규 16곡 Style + Lyrics Prompt 설계 (약칭 I-V1-PC-C-... 구조 + 영문 키워드 + English hook + "길 위" POV 전곡 검증). Lyrics 200자 QA 통과 (최대 196자). concept.md v0.2 (727줄) + input/tracks/ txt 16개 생성.
Next-TODO: 16곡 Suno 테스트 착수 (Track 02부터 순차 or 장르별 묶음). 사용자 제작 4곡 wav 파일 input/tracks/ 정리 대기. 전곡 PASS 후 YouTube Metadata / Genre Gate / 레퍼런스 보강.
Commits: (이번 커밋)
---

---
HANDOFF: Claude -> User
Date: 2026-04-13 14:50:00
Project: ~/Project/wavvy
Agent: Claude (+ 사용자 직접 제작 Track 01)
Summary: 13-00 v0.5.1 재패키지 + YouTube 재업로드. Track 01 "첫 바람 (First Breeze)" → "봄이 번져 (Spring Bleeds)" 교체 (Urban Neo-Soul, 110 BPM, E Major, Female, 사용자 직접 제작). 3-way 트랙 재배열: (02 새싹, 03 햇살, 11 봄 향기, 12 약속, 13 피크닉) → (02 봄 향기, 03 약속, 11 피크닉, 12 햇살, 13 새싹). concept.md Track Map / 배분 규칙 / Series DNA / Track 01 Details / YouTube Tracklist 실제 타임스탬프(report.json 기반 1회차 누적 + acrossfade 0.8s 반영) 재계산. wavvy.py image mode 버그 수정 (ProjectPaths.__init__ 안에서 self.logo/merged_wav/final_mkv 등 할당이 is_image_mode @property 뒤 dead code로 잘못 위치 → AttributeError) + 로고 scale `iw/2:ih/2` → `iw:ih` (50% → 100%, 4K 기준 572x312 원본 크기). PACK v0.5.1 COMPLETE — final.mkv 1.4GB, 135.6분, 4096x2304 static image mode, 로고 100%. loop.png 사용자 신규 4K 이미지 교체. 세트 A wav 20개 git rm (로컬 세트 B를 SSOT로). output/final.mkv 로컬 정리.
Next-TODO: 없음 (13-00 v0.5.1 완료)
Commits: f3d7e93 (wavvy.py image mode fix) / c02636d (13-00 v0.5.1 재패키지)
---

---
HANDOFF: Claude -> User
Date: 2026-04-13 02:36:38
Project: ~/Project/wavvy
Agent: Claude
Summary: 13-00 시리즈 완료 (YouTube 업로드). WAV 20곡 리네이밍, YouTube 메타 작성(FEEL GOOD R&B · URBAN NEO-SOUL, 봄플리·산책·드라이브), 이미지 기반 영상 제작(loop.png 4K → final.mkv 1.3GB/135.4분), 업로드 완료. 부가로 wavvy.py에 이미지 모드 지원 추가 (loop.png/jpg 자동 감지 시 vfade 스킵, `-loop 1 -tune stillimage -r 1` 최적화 렌더).
Next-TODO: K_LIGHTPOP_RUBRIC.md v0.5 정합성 재검토 / brand/logo_wavvy.psd 삭제 의도 확인
Commits: (이번 커밋)
---

---
HANDOFF: Claude -> User
Date: 2026-04-12 23:46:46
Project: ~/Project/wavvy
Agent: 혼합 (사용자 직접 제작 14곡 + Claude 구조 반영)
Summary: 13-00 v0.5 전면 업데이트. 20트랙 전곡 PASS. 사용자 커스텀 14곡 (Neo-Soul/Funk/Urban Soul). concept.md에 Track Details 20곡 통합, txt 삭제.
Next-TODO: WAV 리네이밍 + 루프영상 + 썸네일 + 패키징
Commits: (이번 커밋)
---

---
HANDOFF: Claude -> User
Date: 2026-04-12 11:05:14
Project: ~/Project/wavvy
Agent: 혼합 (사용자 직접 제작 + Claude 구조 반영)
Summary: 13-00 Track 11-12 사용자 직접 제작 삽입, 기존 11-19→13-21 리넘버링, Track 07/08 스타일 교체. 21트랙 체제 전환.
Next-TODO: Track 13-21 사용자 추가 변경 반영 + Suno 테스트
Commits: (이번 커밋)
---

---
HANDOFF: Claude -> User
Date: 2026-04-12 00:05:00
Project: ~/Project/wavvy
Agent: Claude
Summary: 13-00 v0.3→v0.4 Silky R&B 전환 (3단 진화: v0.2.1 Korean Light Pop R&B → v0.3 Korean Bright Pop R&B 단일 라벨 → v0.4 Silky midtempo Korean R&B Male/Female 2종 템플릿). Suno auto-gen 2샘플 분석으로 R&B DNA 확정 (Rhodes + soft EP + round bass + rim shots + airy harmonies + intimate close-mic). Female stacked vocals 허용 (기존 No stacked harmonies 룰 폐지). Track 08 "고백" drop → **19곡 시리즈**, 기존 09-20 파일 → 08-19 리넘버링, _excluded/ 폴더도 삭제. Track 01(legacy Korean Light R&B)/02/03/04/05/06/07/08/09/10 풀 가사 저장 + Suno PASS **10/19**. Track 09 손끝 Key B Minor → B Major 변경 (Minor 배치 3곡으로 축소, 05 F#m/10 Em/14 Dm). Track 10 그네 Male+Female Duet 커스텀 스타일 (trading lines + thirds/fifths 화음).
Next-TODO: 내일 Track 11-19 (피크닉/무지개/벚꽃/봄비/눈부심/약속/노을/만개/우리의 봄) Suno 테스트 이어서. 전부 PASS 시 루브릭 K_LIGHTPOP_RUBRIC.md v0.4 정합성 재검토 (Korean Pop R&B 기준 업데이트) + 루프 영상/썸네일 컨셉 착수.
Commits: (이번 커밋)
---
---
HANDOFF: Claude -> User
Date: 2026-04-04 17:08
Project: ~/Project/wavvy
Agent: 혼합
Summary: 13-00 트랙 txt 20곡 생성 + Lyrics 약칭 포맷 + English hook 추가 + Track 01 Suno PASS + Track 02 Male Duet 전환
Next-TODO: Style B/C Suno 테스트 계속
Commits: (이번 커밋)
---
---
HANDOFF: Claude -> User
Date: 2026-04-04 15:40
Project: ~/Project/wavvy
Agent: Claude
Summary: 13-00 벚꽃 산책 시리즈 신규 생성 — concept v0.1 + INDIE_POP_RUBRIC v1.0 + 장르 리서치 2건 + Track Map 20곡 (루브릭 검증 완료)
Next-TODO: Suno 테스트 (Style A 1곡 먼저) → 프롬프트 튜닝
Commits: (이번 커밋)
---
---
HANDOFF: Claude -> User
Date: 2026-04-04 01:11
Project: ~/Project/wavvy
Agent: Claude
Summary: 22-00 YouTube 제목 변경 (태그 세분화) + 업로드 완료 반영
Next-TODO: brand/logo_wavvy.psd 삭제 의도 확인
Commits: (이번 커밋)
---
