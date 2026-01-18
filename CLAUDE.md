# Claude Code Instructions - vibe-m

> YouTube Music Playlist Generator CLI
>
> Last updated: 2026-01-18 | v1.1.0

## Quick Reference

| 용도 | 파일 |
|------|------|
| **운영 마스터 플랜** | `MASTER/MANAGER.md` |
| **가사 공학 규칙** | `MASTER/LYRICS.md` |
| **사운드/스타일 가이드** | `MASTER/STYLE.md` |
| CLI 스펙 | `vibem.md` |
| CLI 코드 | `vibem.py` |
| 버그 패턴 | `.ai/lessons-learned.md` |
| 현재 상태 | `.ai/SESSION.md` |

## Hard Constraints (절대 제약)

> 출처: `MASTER/MANAGER.md` Phase 0

1. **NO Pydub** - 메모리 누수 방지
2. **Pure FFmpeg** - `ffmpeg-python` 또는 `subprocess`만 사용
3. **Sequential Acrossfade** - 단순 concat 금지
4. **Fail Fast** - 입력 검증 실패 시 즉시 종료
5. **Pure Input Principle** - Suno 가사란에 오직 가사만 (지시어 금지)

## Auto Reference Rules

| 요청 유형 | 참조 문서 | 읽을 범위 |
|----------|----------|----------|
| 가사 작성/수정 | `MASTER/LYRICS.md` | 전체 |
| Style Prompt 작성 | `MASTER/STYLE.md` | 전체 |
| 플레이리스트 프로파일 | `MASTER/STYLE.md` | Section 3 |
| QC/Fail Fast 기준 | `MASTER/MANAGER.md` | Section 1, 3 |
| FFmpeg 필터 작업 | `.ai/lessons-learned.md` | "필터 그래프 버그" 섹션 |
| 정규화 작업 | `.ai/lessons-learned.md` | "ffmpeg-normalize 버그" 섹션 |
| 새 커맨드 추가 | `vibem.md` | CLI 커맨드 명세 |

## Workflow Checklists

### 가사 작성 시
> 상세: `MASTER/LYRICS.md`

- [ ] Metric Mirroring: V1-V2 음절 수 동일
- [ ] Ending Mirroring: 행 끝 품사/어미 패턴 일치
- [ ] Chorus: 3~4행, 각 행 6~10음절
- [ ] Bridge Anchor: Thesis 1라인 + Scene 2~3라인
- [ ] Pure Input: 영어 설명문/괄호 지시어 금지

### QC 체크 시 (3-Point Fail Fast)
> 상세: `MASTER/MANAGER.md` Phase 2

- [ ] Intro (0:00~0:20): 발음 뭉개짐/웅얼거림 → Fail
- [ ] Chorus: 훅이 10초 내 잡지 못함 → 보류
- [ ] Outro: 끊김/클릭 노이즈 → Fail

### FFmpeg 필터 그래프 작업 시
- [ ] Sequential acrossfade 패턴 준수
- [ ] 라벨 인덱싱: `[0][1]→[a01]`, `[a01][2]→[a02]`
- [ ] `final_label = a{num_tracks-1}` 확인

> 근거: `.ai/lessons-learned.md#필터-그래프-인덱싱-오류`

### 정규화 작업 시
- [ ] `sys.executable -m ffmpeg_normalize` 사용
- [ ] 출력 형식: WAV (MP3는 PCM 미지원)
- [ ] 원본 파일 덮어쓰기 금지

> 근거: `.ai/lessons-learned.md#ffmpeg-normalize-path-문제`

### 새 시리즈 프로젝트 생성 시
- [ ] 디렉토리 구조: `SERIES/[Series_Name]/[YYYY-MM-DD]/`
- [ ] 필수 파일: `input/tracks/*.mp3`, `input/loop.mp4`, `input/thumb.jpg`
- [ ] 파일명 형식: `NN__Title__Mood__Genre__BPM.mp3`

## Project Structure

```
vibe-m/
├── MASTER/                 # 프로젝트 헌법
│   ├── MANAGER.md          # 운영 마스터 플랜 (Phase 0~6)
│   └── LYRICS.md           # 가사 공학 규칙 + 아카이브
│
├── SERIES/                 # 시리즈별 프로젝트
│   └── [Series_Name]/
│       └── [YYYY-MM-DD]/
│           ├── concept.md  # (선택) 컨셉 문서
│           ├── input/
│           │   ├── tracks/
│           │   ├── loop.mp4
│           │   └── thumb.jpg
│           ├── work/       # (자동생성)
│           └── output/     # (자동생성)
│
├── vibem.py                # CLI 메인 코드
├── vibem.md                # CLI 스펙
├── requirements.txt        # Python 의존성
├── CLAUDE.md               # 이 파일
└── .ai/                    # AI 전용 메모리
    ├── SESSION.md          # 세션 상태
    └── lessons-learned.md  # 버그 패턴
```

## Quick Commands

| 명령 | 설명 |
|------|------|
| `python3 vibem.py validate <path>` | 파일 검증 |
| `python3 vibem.py preview <path> --sec 30` | 미리보기 생성 |
| `python3 vibem.py pack <path>` | 최종 패키징 |
| `python3 vibem.py clean <path>` | 작업 폴더 정리 |

## Token Saving

### DO
- `MASTER/` 문서 링크로 규칙 참조
- 필요한 파일만 읽기
- 에러 메시지 전문 확인 후 수정

### DON'T
- 전체 코드 다시 작성
- 추측으로 버그 수정 (로그 확인 먼저)
- 불필요한 파일 탐색

## Context Management

> 토큰 90% 초과 시

1. `.ai/SESSION.md` 업데이트
2. `/compact` 제안
3. 다음 작업 명시
