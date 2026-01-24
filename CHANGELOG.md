# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
- **PM_1400 Track 07-09 추가 (9곡 확정)**
  - Track 07 "온기" (Female, 70 BPM, Db Major)
  - Track 08 "그늘" → Track 07로 재배치 (Male, 72 BPM, Ab Major)
  - Track 09 "구름" → Track 08로 재배치 (Female, 76 BPM, F Major)
  - Track 10 수미상관 대기 중
- **CLAUDE.md v2.6: 워크플로우 개선**
  - Suno 파라미터 가이드 (W:35/I:65 기본값)
  - Style Prompt + Exclude 세트 출력 규칙
  - 곡 길이 확장 규칙 (구조 태그로 확장, Verse 8행 금지)
  - 복사용 .txt 파일 저장 워크플로우
- **PM_1400 트랙 순서 재배치 (A안)**
  - 멍(01) → 얼음(02) → 산책(03) → 온기(04) → 돛(05) → 물결(06) → 그늘(07) → 구름(08) → 먼지(09)
  - 산책/물결/먼지 2트랙 이상 간격 확보 (운율 겹침 방지)

### Changed
- **SERIES 폴더 구조 단순화** (CLAUDE.md v2.6.1)
  - vol1 폴더 제거, 파일들 상위로 이동
  - `SERIES/AM_0400/vol1/` → `SERIES/AM_0400/`
  - `SERIES/PM_1400/vol1/` → `SERIES/PM_1400/`

- **PM_1400 vol1 트랙 리스트 확정 (6곡)**
  - Track 01 "산책", Track 02 "멍", Track 03 "물결", Track 04 "얼음", Track 05 "먼지", Track 06 "돛"
  - 그룹 A/B/C 교차 배치로 운율 반복 방지
  - Female vocal (얼음) 중간 배치로 다양성 확보
  - 4곡 추가 예정 (07~10)
- **PM_1400 Track 02 "물결"**: Boat 악보 분석 반영 (Final_v4)
  - Key: A Major (Boat 원곡 동일)
  - Chord: Neo-soul extended (M9, m7)
  - Melody: Narrow range, stepwise, speech-like rhythm
  - Lyrics: 직접적/담백한 Boat 스타일
  - QC Checklist: Speech-like 항목 추가
- **PM_1400 vol.2 시드 트랙**: Track 01 "먼지" 가사/스타일 확정
  - Reference: 죠지 - Boat (표류하는 느낌, R&B groove)
  - Male vocal, Vibraphone-led, 72 BPM, Eb Major
- **CLAUDE.md v2.2.0: Style Prompt QC 워크플로우**
  - S15 글자수 제한 (< 800자, wc -c 검증 필수)
  - S16 Lead Instrument Supportive 규칙
  - S17 Chorus Expansion Density 규칙
  - 검증 통과 전 유저 제안 금지
- **LYRICS.md v1.8: 가사 품질 규칙 추가**
  - 1.10 Image Density Management (V1=공간, V2=감각 분리)
  - 1.11 Chorus Tone Rule (관조 톤, 직접 호소 최소화)
- **vibem.py: 타이틀 자동 생성 (SSOT v1.5)**
  - draft_description.txt 상단에 제목 초안 자동 생성
  - concept.md에서 Title Meta 파싱 (Context Mode, Time, GENRE 등)
  - 메타 없으면 트랙 정보에서 자동 추론
- **vibem.py: shorts 커맨드 v2.0.0**
  - 입력 변경: `loop.mp4` → `shorts.mp4` (8~10초)
  - 짧은 영상을 음악 길이만큼 자동 루프
  - 출력: `output/shorts/short_[TrackName].mp4` (유지)
- **PLAYLIST_GUIDE.md v1.2: Playlist Title Generation Rules (SSOT v1.5)**
  - 타이틀 고정 구조: `[Playlist] [AM/PM HH:MM] soomshuim | {TIME_STATE_PHRASE}, {MODIFIER_PHRASE} {GENRE}`
  - Context Mode 필수 입력 (Settling/Transition/Energizing/Focusing)
  - TIME_STATE_PHRASE Type A/B 교대 규칙
  - GENRE 확장: R&B, Rock, Pop, Jazz 등
- **vibem.py: pack --repeat 옵션**
  - 플레이리스트 N회 반복 재생 (기본값 2회)
  - description에 회차 구분 없이 단일 타임스탬프 표시
- **vibem.py: draft_description.txt 자동 생성**
  - 시리즈/컨셉 기반 커스텀 인트로 문단
  - 📌 고정 댓글 섹션 (시간대별 인삿말)
  - Source/Derived 분리 원칙 (concept.md = SSOT)
- **/vibem 커맨드**: 프로젝트 재개용 컨텍스트 로더

### Changed
- **시리즈 디렉토리 변경**: `SERIES/잠들지_못한_새벽/` → `SERIES/AM_0400/`
- **첫 플레이리스트 제목/URL 변경**
  - 시리즈 컨셉: "[AM 04:00] 하루가 멈춘 시간"
  - YouTube 제목: "[Playlist] [AM 04:00] soomshuim | 하루가 멈춘 시간, Slow R&B 보컬"
  - 새 URL: https://youtu.be/i1GHmn1WZr4
- **CLAUDE.md v2.0.0: Shorts 워크플로우 업데이트**
  - 입력: shorts.mp4 (8~10초) 루프 방식
  - 프로젝트 구조에 shorts.mp4 추가
- **VIBE-M_Master_Plan.md: Shorts 커맨드 스펙 추가**
- **커맨드 체계 변경**: .claude/commands/ → 글로벌 커맨드로 통합
  - coach, record 삭제 → 글로벌 스킬로 이전
  - /vibem 신규 추가

- **LYRICS.md v1.7: Korean Lyric Positioning**
  - 한국어 가사 플레이리스트 차별점 공식화
  - 포지셔닝 원칙: 의미 있는 가사, 혼자 읽히는 언어, 소리가 먼저
  - 가사 설계 철학: 감정 직접 표출 금지, 사물/공간/현상 중심
  - K1-K3 한국어 검증 체크리스트 추가
  - 메타/브랜딩 적용 규칙
- **CLAUDE.md v1.6.0: Korean Positioning Workflow**
  - 가사 생성 Step 3에 Korean Positioning 검증 추가
  - 검증 출력 포맷에 Section C (K1-K3) 추가
- **24H_UNIVERSE.md v1.0: Master Project Bible**
  - 24H Universe 세계관 정의 (시간 기반 감정 스테이션)
  - 10개 Time Station 정의 (02:00~04:30)
  - 5개 Key/Mode Bucket 시스템
  - Production Templates 3종 (Track Brief, Style Skeleton, Lyrics Skeleton)
  - Station QC Checklist (Listen/Lyric/Style/Exclude 검증)
  - DNA Constants vs Variables 명세
- **PLAYLIST_GUIDE.md v1.1: Korean Lyric Positioning 3-Layer 전략**
  - Layer 1: 재생목록 설명 (자연스럽게)
  - Layer 2: 고정 댓글 (팬 메시지)
  - Layer 3: 채널 About (명확하게)
  - 템플릿 + DO/DON'T 규칙
- **vibem.py: description.txt 우리말 가사 문구 자동 추가**
  - "이 플레이리스트의 노래들은 모두 우리말 가사로 만들어졌습니다."
  - "*All tracks feature Korean lyrics.*"

- Track 09 "마음안": 수미상관 마지막 곡 (Track 01 "마음밖" 대응)
  - Male vocal + Powerful belt, 95 BPM, Db Major
  - 키워드 축: 여명/옥상/난간/지평선
  - 후렴: "마음 안으로 번져와 / 여명처럼 스며들어"
- Track 08 "빗줄기": Melancholic R&B, 85 BPM, F minor, Rhodes-led
  - 키워드 축: 빗줄기/아스팔트/골목/처마/우산
  - Raw Vocal + Chest Belt, Contralto female
  - 메타태그 포함 (Direct vocal, Chest voice, Powerful belt)
- **STYLE.md v1.7: Fail Fast Energy Check**
  - Chorus held note 정량화: "exactly 1 held note (longer sustain than any verse note)"
  - V2 → Chorus FAIL 조건 4개: register/intensity 미상승, 1 held note 부재, 레이어 의존
- ROLES.md v1.2: Automatic FAIL Conditions 추가
  - Chorus energy ≤ Verse2 → FAIL
  - Vocal intensity peak 부재 → FAIL
- 00_system.txt: Mandatory Slot Check 추가
  - 슬롯 누락 시 재생성 강제
  - Vocal Persona 누락 = INVALID
- 02/03_designer.txt: INVALID conditions 추가
- **STYLE.md v1.6: Energy Permission + Safety Separation**
  - 핵심 원칙: "금지는 레이어에만, 허용은 에너지에"
  - Verse2 에너지 상승 권한 명시적 부여 (encouraged/allowed/must)
  - 새 Harmony Guard: "Lead vocal remains single and dominant"
- ROLES.md v1.1: Energy Permission Principle 추가
  - Seed Designer에 에너지 허용 원칙 명문화
  - Sanity Check에 "Verse2 energy permission" 항목 추가
- 02_designer.txt: Safety Lines + Energy Permission 분리
- 03_variation.txt: Vocal Energy Risk Fail 조건 추가
  - Verse2 lacks lift → FAIL
  - Chorus sounds flat due to over-safety → FAIL
- PLAYLIST_GUIDE.md: 유튜브 감성 플레이리스트 인기 사례 분석 가이드
  - TPO 패턴, 제목 전략, 썸네일 가이드, 시리즈화 전략
  - Reference/ 디렉토리에 원본 PDF 추가
- Track 04 "물안개": 가사 + Style Prompt (Lo-fi R&B, Male vocal, 80 BPM)
- LYRICS.md v1.1: 새 규칙 4개 추가
  - 1.5 Vocabulary Independence (어휘 독립성)
  - 1.6 Snapshot Hook Rule (스냅샷 훅)
  - 1.7 Bridge Thesis Constraint (테제 제약)
  - 1.8 V2 Escalation Rule (2절 상승)
- Role System 문서화: ROLES.md + prompts/ 4종 + QUICK_REF.md
  - Seed Researcher / Seed Designer / Variation Designer 역할 분리
  - 사람용 운영 매뉴얼 (QUICK_REF.md) 별도 분리
- Test_Series concept.md: Track 01~04 가사/스타일 기록

### Changed
- **첫 플레이리스트 YouTube 업로드 완료** (2026-01-20 22:00 공개)
  - 제목: "[Playlist] [AM 04:00] soomshuim | 하루가 멈춘 시간, Slow R&B 보컬"
  - URL: https://youtu.be/i1GHmn1WZr4
  - 채널: soomshuim
  - 재생목록: "하루를 듣는 방법 | 24 Hours Playlist"
- **첫 플레이리스트 정식 출범**: Test_Series → "[AM 04:00] 하루가 멈춘 시간"
  - 디렉토리: `SERIES/Test_Series/2026-01-18/` → `SERIES/AM_0400/vol1/`
  - 9트랙 완성 (Track 01~09)
- **STYLE.md v1.5 → v1.6: Energy Permission + Safety Separation**
  - v1.5 문제: "금지 규칙이 에너지 규칙을 덮어버림" → 보컬이 무난해짐
  - v1.6 해결: "금지는 레이어에만, 허용은 에너지에" 분리
  - ❌ "vocals unchanged" → ✅ "lead vocal energy may increase, but no new vocal layers"
  - ❌ "Single lead vocal ONLY" → ✅ "Lead vocal remains single and dominant"
  - Verse2 에너지 상승: "encouraged", "allowed", "must" 권한 부여
- CLAUDE.md: 체크리스트 기반 워크플로우 강화
  - 가사/Style Prompt 생성 시 필수 검증 프로세스 명문화
  - 플레이리스트 컨셉 논의 시 PLAYLIST_GUIDE.md 자동 참조
- MANAGER.md v1.1: Phase 2 Track QC에 코러스 과다 Fail 기준 추가
- 02_designer.txt: Safety Lines 작성 규칙 제로 베이스라인으로 업데이트

### Fixed
- vibem.py preview: 각 트랙이 미리보기에 포함되도록 수정
  - 이전: 전체 병합 후 앞 N초 (Track 01만 포함)
  - 이후: 각 트랙 앞 N/트랙수 초씩 잘라서 병합
