# Session State - vibe-m

> 현재 세션 상태 기록
>
> Last updated: 2026-01-18 (Night)

## 완료된 작업

### 2026-01-18 (오전)

- [x] 프로젝트 초기 설정
  - `vibem.py` CLI 구현 (Click 기반)
  - `requirements.txt` 생성
  - FFmpeg 8.0.1 설치

- [x] 핵심 커맨드 구현
  - `validate` - 파일/오디오 검증
  - `preview` - 미리보기 생성
  - `pack` - 최종 패키징
  - `init` - 프로젝트 초기화
  - `clean` - 작업 폴더 정리

- [x] 버그 수정 3건
  - 필터 그래프 인덱싱 오류 수정
  - ffmpeg-normalize PATH 문제 해결
  - MP3 → WAV 출력 형식 변경

- [x] 테스트 완료
  - `SERIES/Test_Series/2026-01-18/` 테스트 프로젝트
  - preview 30초 미리보기 정상 확인

### 2026-01-18 (오후)

- [x] 프로젝트 구조 재정비
  - `series/` → `SERIES/` 대문자 변경
  - `MASTER/` 폴더 생성

- [x] MASTER 문서 3종 완성
  - `MANAGER.md` - 운영 마스터 플랜 (QC, Fail Fast)
  - `LYRICS.md` - 가사 공학 규칙 (Metric Mirroring 등)
  - `STYLE.md` - 사운드/스타일 가이드 (Playlist Profile)

- [x] `/coach` 커맨드 생성
  - `.claude/commands/coach.md`
  - 가사 검토, Style Prompt 검토, QC 체크리스트

- [x] GitHub 연동
  - Repository: https://github.com/soomshuim/vibe-m
  - Branch: master
  - Initial commit 완료

- [x] `/coach` 테스트
  - LYRICS.md Reference Example 검토 → PASS

## 현재 상태

- **프로젝트**: Production Ready (v1.0.0)
- **GitHub**: https://github.com/soomshuim/vibe-m (master)
- **플레이리스트 주제**: "혼자 걷는 밤, 습기와 잔향"
- **테스트 데이터**: `SERIES/Test_Series/2026-01-18/`
  - 트랙 3곡 완료:
    - `01__마음밖__Sentimental__RnB-Ballad__100.mp3`
    - `02__습기__Sentimental__Acoustic-RnB__88.mp3`
    - `03__잔향__Hazy__AltR&B__112.mp3`
  - 에셋: `loop.mp4`, `thumb.jpg` 준비됨
  - preview 생성 완료 (60초, 3트랙 각 20초)

## 진행 중

- [ ] Track 04-10 제작 (7곡)
  - Track 04 가사 초안 완료 (제목: 물안개)

## 완료된 추가 작업

### 2026-01-18 (저녁)

- [x] Role System 문서화 완료 (`6db9639`, `cabecb6`)
  - `MASTER/ROLES.md` 생성 (v1.0)
  - `MASTER/QUICK_REF.md` 생성 - 사람용 운영 매뉴얼
  - `MASTER/prompts/` 폴더 생성
    - `00_system.txt` - 공유 컨텍스트
    - `01_researcher.txt` - Seed Researcher 프롬프트
    - `02_designer.txt` - Seed Designer 프롬프트
    - `03_variation.txt` - Variation Designer 프롬프트
  - `CLAUDE.md` Quick Reference 업데이트
  - `CHANGELOG.md` 생성

- [x] STYLE.md 제로 베이스라인 진화 (`fcadb70` ~ `66a7a76`)
  - v1.1: Harmony Guard 추가
  - v1.2: Safety Lines + Exclude 재설계
  - v1.3: Safety Lines 강화 + Chorus 2 분리
  - v1.4: Safety Lines 압축 + 긍정 방향 가드
  - v1.5: 제로 베이스라인 - 코러스 완전 차단

- [x] MANAGER.md v1.1 (`66a7a76`)
  - Phase 2 Track QC에 코러스 과다 Fail 기준 추가

- [x] concept.md 기록 (`b5fce3d`)
  - Track 01~03 가사/스타일 기록

### 2026-01-18 (밤)

- [x] vibem.py preview 버그 수정
  - 이전: 전체 병합 후 앞 N초 자르기 (Track 01만 포함)
  - 이후: 각 트랙 앞 N/트랙수 초씩 잘라서 병합 (모든 트랙 포함)
  - 60초 preview = 3트랙 × 20.5초

- [x] Track 02 파일명 수정
  - `Sentimental_Acoustic-RnB` → `Sentimental__Acoustic-RnB` (언더스코어 2개)

- [x] 플레이리스트 주제 확정
  - "혼자 걷는 밤, 습기와 잔향"
  - 키워드: 습기, 잔향, 그림자, 번짐, 희미함, 혼자, 밤

- [x] Track 04-10 제작 플랜 수립
  - `.claude/plans/rippling-finding-lecun.md`

## 완료된 추가 작업

### 2026-01-19

- [x] Track 04 "물안개" 가사 + Style Prompt 완료 (`7cb2824`)
  - Lo-fi R&B, Male vocal, 80 BPM, Felt Piano
  - 가사 QC 9/9 PASS, Style Prompt 11/11 PASS
- [x] 워크플로우 강화
  - Style Prompt 체크리스트 9→11슬롯 확장
  - PLAYLIST_GUIDE.md 생성 (유튜브 인기 사례 분석)
  - LYRICS.md v1.1 (새 규칙 4개)
  - Exclude 충돌 방지 규칙 추가

## 다음 작업 (예정)

- [ ] Track 04 Suno 생성 + QC
- [ ] Track 05-10 순차 제작
- [ ] 10곡 완료 후 validate → pack

## 알려진 이슈

없음

## 참고 파일

| 파일 | 용도 |
|------|------|
| `MASTER/MANAGER.md` | 운영 마스터 플랜 |
| `MASTER/LYRICS.md` | 가사 공학 규칙 |
| `MASTER/STYLE.md` | 사운드/스타일 가이드 |
| `MASTER/PLAYLIST_GUIDE.md` | 플레이리스트 컨셉 가이드 |
| `MASTER/ROLES.md` | 역할 분리 시스템 (SSOT) |
| `MASTER/QUICK_REF.md` | 사람용 운영 매뉴얼 |
| `MASTER/prompts/` | 역할별 프롬프트 템플릿 |
| `MASTER/VIBE-M_Master_Plan.md` | CLI 스펙 |
| `vibem.py` | 메인 CLI 코드 |
| `CLAUDE.md` | Claude 작업 지침 |
| `.claude/commands/coach.md` | /coach 커맨드 |
| `.ai/lessons-learned.md` | 버그 패턴 |
| `CHANGELOG.md` | 변경 이력 |
| `Reference/` | 참고 자료 (인기 사례 분석 PDF)
