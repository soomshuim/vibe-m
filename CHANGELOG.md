# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
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
- **첫 플레이리스트 YouTube 업로드 완료**
  - 제목: "잠들지 못한 새벽, 이 노래들이 위로가 되길"
  - URL: https://youtu.be/E62sIgkPNXI
  - 채널: soomshuim (24시간 시리즈)
- **첫 플레이리스트 정식 출범**: Test_Series → "잠들지 못한 새벽, 이 노래들이 위로가 되길"
  - 디렉토리: `SERIES/Test_Series/2026-01-18/` → `SERIES/잠들지_못한_새벽/vol1/`
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
