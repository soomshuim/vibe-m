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
| **플레이리스트 컨셉 가이드** | `MASTER/PLAYLIST_GUIDE.md` |
| **역할 분리 시스템** | `MASTER/ROLES.md` |
| **사람용 운영 매뉴얼** | `MASTER/QUICK_REF.md` |
| **역할별 프롬프트** | `MASTER/prompts/` |
| **실행용 초압축 템플릿** | `MASTER/prompts/04_ultra_compressed.txt` |
| CLI 스펙 | `MASTER/VIBE-M_Master_Plan.md` |
| CLI 코드 | `vibem.py` |
| 버그 패턴 | `.ai/lessons-learned.md` |
| 현재 상태 | `.ai/SESSION.md` |
| 인기 사례 분석 PDF | `Reference/유튜브 감성 플레이리스트 인기 사례 분석.pdf` |

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
| **플레이리스트 컨셉 논의/시작** | `MASTER/PLAYLIST_GUIDE.md` | 전체 (필수) |
| 가사 작성/수정 | `MASTER/LYRICS.md` | 전체 |
| Style Prompt 작성 | `MASTER/STYLE.md` | 전체 |
| 플레이리스트 프로파일 | `MASTER/STYLE.md` | Section 3 |
| QC/Fail Fast 기준 | `MASTER/MANAGER.md` | Section 1, 3 |
| 역할 분리/AI 작업 | `MASTER/ROLES.md` | 전체 |
| 역할별 프롬프트 | `MASTER/prompts/` | 해당 역할 파일 |
| FFmpeg 필터 작업 | `.ai/lessons-learned.md` | "필터 그래프 버그" 섹션 |
| 정규화 작업 | `.ai/lessons-learned.md` | "ffmpeg-normalize 버그" 섹션 |
| 새 커맨드 추가 | `MASTER/VIBE-M_Master_Plan.md` | CLI 커맨드 명세 |

## Workflow Checklists

### 가사/Style Prompt 제안 워크플로우 (필수)

**원칙**: 체크리스트 기반 출력 + 누락 검증 강제
> "자유 생성"이 아니라 **"이걸 다 포함했는지 증명해라"**가 핵심

**가사 생성 요청 시:**
```
Step 0. LYRICS.md + 이전 트랙 키워드 확인
Step 1. Generate 가사 초안
Step 2. Run self-QC against checklist (9개 항목)
Step 3. If all pass → output with QC 테이블
        If any fail → 재작성 후 Step 2 반복
        (통과할 때까지 유저에게 제안하지 않음)
```

**Style Prompt 생성 요청 시:**
```
Step 0. STYLE.md Required Slots 확인
Step 1. Generate Style Prompt
Step 2. Run self-QC against checklist (9개 슬롯)
Step 3. If all pass → output with QC 테이블
        If any fail → STOP + report missing items → 재작성
```

---

### 가사 필수 슬롯 체크리스트
> 상세: `MASTER/LYRICS.md`
> **원칙: 하나라도 누락 시 FAIL → 재작성 후 통과 시 제안**

| # | 규칙 | 체크 내용 |
|---|------|----------|
| 1.1 | Metric Mirroring | V1-V2 음절 수 동일 |
| 1.2 | Ending Mirroring | 행 끝 품사/어미 패턴 일치 |
| 1.3 | Chorus Static | 3~4행, 100% 동일 반복 |
| 1.4 | Bridge Anchor | Thesis 1라인 고정 + Scene 2~3라인 변주 |
| 1.5 | Vocabulary Independence | 이전 트랙과 핵심 키워드 겹침 없음 |
| 1.6 | Snapshot Hook | Chorus 1-2행 명사+동사 |
| 1.7 | Bridge Thesis | 현상 기반 (사람 의존 X) |
| 1.8 | V2 Escalation | 마지막 2행 신체 반응/감정 상승 |
| 2.1 | Pure Input | 괄호/영어 설명/지시어 없음 |

**검증 출력 포맷:**
```
Section A: 가사 (전문)
Section B: QC Validation (각 항목 ✓/✗)
Section C: 키워드 축 요약 (이전 트랙과 비교)
```

---

### Style Prompt 필수 슬롯 체크리스트
> 상세: `MASTER/STYLE.md`
> **원칙: 하나라도 누락 시 FAIL 선언 → 출력 금지**

| # | 슬롯 | 체크 내용 | 예시 |
|---|------|----------|------|
| S1 | Vocal Persona | gender + tone 명시 | "Male vocal, warm soulful tone" |
| S2 | Vocal Processing | dry/close-mic 여부 | "dry close-mic, minimal autotune" |
| S3 | Lead Instrument | 메인 악기 | "Felt Piano-led" |
| S4 | Rhythm Source | 리듬 요소 | "soft shaker, rim-only" |
| S5 | BPM | 템포 | "80 BPM" |
| S6 | Key | 조성 | "key Eb Major" |
| S7 | Musicality Matrix | V2/Chorus/Bridge/Outro 지시 | "Verse2 same melodic contour..." |
| S8 | Harmony Guard | 코러스/화성 금지 명시 | "No backing vocals, no choir" |
| S9 | Chorus Expansion | Chorus2 악기만 확장 | "vocals unchanged" |
| S10 | Chorus Layer Block | 코러스 레이어 완전 차단 문장 | "Lead vocal only throughout; absolutely no vocal layers..." |
| S11 | Exclude 충돌 검사 | Style 톤과 Exclude 항목 겹침 없음 | Style에 soulful → Exclude에 soulful 금지 |

**검증 프로세스:**
```
Step 1. Generate Style Prompt
Step 2. Run self-QC against checklist (11개 슬롯)
Step 3. If all pass → output FINAL
        If any fail → STOP + report missing items
```

**Exclude 작성 규칙:**
- Style 본문의 Vocal Persona 키워드와 겹치는 항목 금지
- Exclude는 **EDM/프로세싱 계열**만 타격 (vocoder, hard tune, autotune heavy 등)
- 톤/캐릭터 계열 (husky, warm, breathy 등)은 Style 본문에서만 제어

**Vocal Persona 강제 선언:**
> Vocal persona must be explicitly declared as gender (male/female) + vocal character (husky/soft/soulful/airy 등).
> If not explicitly written, output is invalid.

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
│   ├── LYRICS.md           # 가사 공학 규칙 + 아카이브
│   ├── STYLE.md            # 사운드/스타일 가이드
│   ├── ROLES.md            # 역할 분리 시스템 (SSOT)
│   ├── QUICK_REF.md        # 사람용 운영 매뉴얼
│   ├── VIBE-M_Master_Plan.md # CLI 스펙
│   └── prompts/            # 역할별 프롬프트 템플릿
│       ├── 00_system.txt
│       ├── 01_researcher.txt
│       ├── 02_designer.txt
│       └── 03_variation.txt
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
