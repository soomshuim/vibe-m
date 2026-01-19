# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
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
