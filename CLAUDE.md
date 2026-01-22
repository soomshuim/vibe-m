# Claude Code Instructions - vibe-m

> YouTube Music Playlist Generator CLI
>
> Last updated: 2026-01-23 | v2.0.0 (Title SSOT + Shorts Typography)

## Quick Reference

| 용도 | 파일 |
|------|------|
| **24H Universe Bible** | `MASTER/24H_UNIVERSE.md` |
| **운영 마스터 플랜** | `MASTER/MANAGER.md` |
| **가사 공학 규칙** | `MASTER/LYRICS.md` |
| **사운드/스타일 가이드** | `MASTER/STYLE.md` |
| **플레이리스트 컨셉 가이드** | `MASTER/PLAYLIST_GUIDE.md` |
| **타이틀 생성 규칙 (SSOT)** | `MASTER/PLAYLIST_GUIDE.md` §0 |
| **역할 분리 시스템** | `MASTER/ROLES.md` |
| **사람용 운영 매뉴얼** | `MASTER/QUICK_REF.md` |
| **역할별 프롬프트** | `MASTER/ROLES.md` 내 정의 |
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
5. **Pure Input Principle** - Suno 가사란에 가사 + 구조 태그 + Performance Cues만 (설명형 지시어 금지)

## Auto Reference Rules

| 요청 유형 | 참조 문서 | 읽을 범위 |
|----------|----------|----------|
| **24H Universe 트랙 생성** | `MASTER/24H_UNIVERSE.md` | 전체 (필수) |
| **플레이리스트 컨셉 논의/시작** | `MASTER/PLAYLIST_GUIDE.md` | 전체 (필수) |
| **플레이리스트 타이틀 생성** | `MASTER/PLAYLIST_GUIDE.md` | Section 0 (SSOT) |
| 가사 작성/수정 | `MASTER/LYRICS.md` | 전체 |
| Style Prompt 작성 | `MASTER/STYLE.md` | 전체 |
| 플레이리스트 프로파일 | `MASTER/STYLE.md` | Section 3 |
| QC/Fail Fast 기준 | `MASTER/MANAGER.md` | Section 1, 3 |
| 역할 분리/AI 작업 | `MASTER/ROLES.md` | 전체 |
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
Step 2. Run self-QC against checklist (10개 항목)
Step 3. Korean Positioning 검증 (K1-K3) ← v1.7 NEW
Step 4. If all pass → output with QC 테이블
        If any fail → 재작성 후 Step 2 반복
        (통과할 때까지 유저에게 제안하지 않음)
```

**Style Prompt 생성 요청 시:**
```
Step 0. STYLE.md Required Slots 확인
Step 1. Generate Style Prompt
Step 2. Run self-QC against checklist (13개 슬롯)
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
| 1.2 | Ending Mirroring | **행 끝 품사 엄격 일치** (동사↔동사, 형용사↔형용사) |
| 1.3 | Chorus Static | 3~4행, 100% 동일 반복 |
| 1.4 | Bridge Anchor | Thesis 1라인 고정 + Scene 2~3라인 변주 |
| 1.5 | Vocabulary Independence | 이전 트랙과 핵심 키워드 겹침 없음 |
| 1.6 | Snapshot Hook | Chorus 1-2행 명사+동사 |
| 1.7 | Bridge Thesis | 현상 기반 (사람 의존 X) |
| 1.8 | V2 Escalation | 마지막 2행 신체 반응/감정 상승 |
| 1.9 | Physical Object Anchor | **각 섹션에 물성 오브젝트 1개 이상** (추상어 과밀 금지) |
| 2.1 | Pure Input | 설명형 괄호 금지, Performance Cues `(soft)` 등은 허용 |
| 2.4 | Length Guide | **전체 100-120 단어, 섹션당 4-6행** |
| **K1** | **Korean Only** | **한국어여야만 성립하는 가사인가?** |
| **K2** | **Translation Loss** | **영어 번역 시 힘 빠지는 지점 있는가?** |
| **K3** | **Dual Satisfaction** | **배경음악 OK + 읽으면 문장으로 남는가?** |

**검증 출력 포맷:**
```
Section A: 가사 (전문)
Section B: QC Validation (각 항목 ✓/✗)
Section C: Korean Positioning (K1-K3 ✓/✗) ← v1.7 NEW
Section D: 키워드 축 요약 (이전 트랙과 비교)
```

---

### Style Prompt 필수 슬롯 체크리스트
> 상세: `MASTER/STYLE.md`
> **원칙: 하나라도 누락 시 FAIL 선언 → 출력 금지**

| # | 슬롯 | 체크 내용 | 예시 |
|---|------|----------|------|
| S0 | **핵심 앞에** | Genre/BPM이 첫 5단어 내 | "Korean Lo-fi R&B, 80 BPM, ..." |
| S1 | **Raw Vocal Baseline** | `Raw, Solid, Direct, Dry` | 기본값 (powerful/husky/airy 요청 시 추가) |
| S2 | Vocal Persona | gender + 발성 타입 | "Contralto female" 또는 "Deep male vocal" |
| S3 | **Chest Voice 강제** | `Chest voice dominant` 문장 | 진성 보컬 확보 |
| S4 | Vocal Processing | dry/close-mic 여부 | "dry close-mic, Unprocessed" |
| S5 | Lead Instrument | 메인 악기 | "Felt Piano-led" |
| S6 | Rhythm Source | 리듬 요소 | "soft brush kit, layback groove" |
| S7 | BPM | 템포 | "82 BPM" |
| S8 | Key | 조성 | "Eb Major" |
| S9 | Musicality Matrix | V2/Chorus/Bridge/Outro 지시 | "Verse2 stronger dynamics..." |
| S10 | Harmony Guard | 레이어 금지 명시 | "No harmony, no backing vocals, no doubles" |
| S11 | Chorus Layer Block | 코러스 레이어 완전 차단 | "Lead vocal remains single and dominant" |
| S12 | Exclude 필수 항목 | **Airy, Falsetto, Whisper, Harmonized** | 얇은 보컬 유발 단어 차단 |
| S13 | Exclude 제한 | **최대 3그룹, 8키워드** (기본 1줄 권장) | 과도한 Exclude = 부작용 |
| S14 | **모호 형용사 제거** | warm reflective, rich vibrato 등 제거 | 가성 유발 방지 |

**검증 프로세스:**
```
Step 0. powerful/husky/airy 별도 요청 있는지 확인
Step 1. 없으면 Raw Vocal Baseline 적용
Step 2. Run self-QC against checklist (15개 슬롯)
Step 3. If all pass → output FINAL
        If any fail → STOP + report missing items
```

**Raw Vocal Baseline (기본값):**
```
Raw vocal, Solid, Direct, Dry, Unprocessed
Chest voice dominant. No falsetto.
```

**요청 시 추가:**
- `powerful` 요청 → Powerful, Strong attack 추가
- `husky` 요청 → Raspy, Grit 추가
- `airy` 요청 → Airy, Breathy 허용

**Exclude 필수 항목:**
```
Airy, Falsetto, Harmonized, Backing vocals, Whisper, Auto-tune
```

**피해야 할 모호한 형용사:**
- ❌ `warm reflective tone` → Airy/Ethereal로 해석됨
- ❌ `rich vibrato` → 가성 비브라토 유발
- ❌ `Subtle R&B ad-libs` → 더블링으로 해석됨
- ✅ `Raw, Powerful, Solid, Direct` → 구체적 발성 키워드

### QC 체크 시 (3-Point Fail Fast)
> 상세: `MASTER/MANAGER.md` Phase 2

- [ ] Intro (0:00~0:20): 발음 뭉개짐/웅얼거림 → Fail
- [ ] Chorus: 훅이 10초 내 잡지 못함 → 보류
- [ ] Outro: 끊김/클릭 노이즈 → Fail

### DEBUG vs PROD 모드 (v1.5.0 NEW)
> 상세: `MASTER/STYLE.md` §10 + `MASTER/MANAGER.md` Phase 2.5

| 모드 | 상황 | 규칙 |
|------|------|------|
| **PROD** | 정상 트랙 제작 | 최소 2개 슬롯 변주 |
| **DEBUG** | 같은 문제 2회 재발 | **1개 변수만 변경** |

- 하모니/가성/EDM 보컬 문제 재발 시 → DEBUG 모드 전환
- DEBUG A/B 비교로 원인 특정 → PROD 복귀

### S1-S9 Validation 강제 (v1.5.0 NEW)
> 상세: `MASTER/ROLES.md` S1-S9 Validation Enforcement

- Style Prompt/Variation 출력 시 **반드시 S1-S9 테이블 포함**
- S1 (Vocal Persona) 비어있음 = **즉시 FAIL, 재생성**
- 테이블 없는 출력 = **자동 INVALID**

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

### Shorts 생성 요청 시 (v2.0.0)
> **원칙: 반드시 사용자에게 확인 후 생성**

**입력 파일:**
- `input/shorts.mp4` (8~10초 짧은 영상) - 사용자가 준비
- 이 영상이 음악 구간 길이만큼 자동 루프됨

**"숏츠 만들어줘" 요청 시 필수 질문:**
```
Step 0. shorts.mp4 확인: input/shorts.mp4 존재 여부 체크
Step 1. 시리즈 확인: SERIES/ 내 폴더 목록 보여주고 선택 요청
Step 2. 트랙 번호 확인: 해당 시리즈의 트랙 목록 보여주고 선택 요청
Step 3. 구간 확인: "어느 구간으로 할까요? (예: 00:45 ~ 01:15)"
Step 4. 확인 후 실행: python vibem.py shorts [TRACK_PATH] --start [MM:SS] --duration [SEC]
```

**⚠️ 절대 규칙: 시작/종료 시간 수정 금지**
```
- 사용자가 "01:35 ~ 02:15" 라고 하면 → --start 01:35 --duration 40
- 버퍼/여유 시간 임의 추가 금지
- 반올림/보정 금지
- duration = 종료시간 - 시작시간 (정확히 계산)
```

**실행 전 검증 체크리스트 (필수):**
```
□ --start 값이 사용자 지정 시작 시간과 정확히 일치하는가?
□ --duration 값이 (종료시간 - 시작시간)과 정확히 일치하는가?
□ 임의로 버퍼/여유 시간을 추가하지 않았는가?

→ 하나라도 미준수 시: 명령어 수정 후 재실행
→ 실행 후 출력 duration 확인: 오차 ±2초 초과 시 원인 파악
```

**질문 예시:**
```
숏츠를 만들기 전에 확인이 필요합니다:

1. 어떤 시리즈인가요?
   - 잠들지_못한_새벽/vol1
   - (기타 시리즈...)

2. 몇 번 트랙인가요?
   - 01. 마음밖
   - 02. 윤곽
   - ...

3. 어느 구간인가요? (시작 MM:SS ~ 끝 MM:SS)
```

**출력 경로:** `output/shorts/short_[TrackName].mp4`

### Shorts 2-Layer 텍스트 시스템 (v1.9.0)

**레이어 구조:**
```
Layer 1 (Title): 중앙 후킹 문구 - 0~2초만 표시, 빠르게 퇴장
Layer 2 (Lyric): 하단 가사 - 4초 이후 등장, 끝까지 유지
```

---

### Shorts Hook Copy Slot (필수)

> 쇼츠 계획 시 **반드시** 후킹 문구 제안 필요

**출력 형식:**
```
HOOK_TITLES (3-7 단어, 5개 제안):
1) ...
2) ...
3) ...
4) ...
5) ...

HOOK_SUBTITLES (6-12 단어, 3개 제안, 선택):
1) ...
2) ...
3) ...
```

**규칙:**
- ❌ 가사 라인 그대로 사용 금지
- ⭕ 상황/감정 선언문 (화면 타이틀용)
- ⭕ 시리즈 컨셉/시간대 포지셔닝과 일치

---

### Shorts QC 체크리스트 (필수)

```
□ Hook Title 있음? (Y/N)
□ Bottom Lyric 있음? (Y/N)
□ 역할 분리 유지? (Title: 0-2초만, Lyric: 4초 이후 하단) (Y/N)
□ Title이 가사가 아닌 선언문인가? (Y/N)

→ 하나라도 N이면 수정 후 재생성
```

---

### Shorts 자막 타이포그래피 스펙 (필수)

#### A. 공통 원칙 (가독성 3종 세트)

| 항목 | 값 | 비고 |
|------|-----|------|
| Fill (글자색) | White / Off-white | 고정 |
| Shadow | 부드럽고 넓게 | 필수 |
| Backplate | 반투명 바 | 배경 밝거나 복잡할 때만 |
| Stroke (외곽선) | **금지** | 촌스러움 방지 |

#### B. 하단 가사 스펙 (지속 레이어)

| 항목 | 값 |
|------|-----|
| **위치** | 세로 35-40% (화면 중앙보다 약간 아래) |
| **정렬** | Center |
| **폰트** | 산세리프 (얇게~보통) |
| **크기** | 화면 높이의 4.5-5.5% |
| **자간** | +1 ~ +3 |
| **행간** | 1.0 ~ 1.1 |
| **페이드** | In/Out 6-8프레임 (컷점프 금지) |

**드랍쉐도우 (하단 가사):**
| 항목 | 값 |
|------|-----|
| Opacity | 55-70% |
| Blur | 12-18 |
| Distance Y | 6-10 |
| Distance X | 0 |
| Color | Black |

**백플레이트 (옵션):**
| 항목 | 값 |
|------|-----|
| Shape | Rounded rectangle |
| Opacity | 18-28% |
| Blur | 0 (단색) |
| Padding | 좌우 24-36px, 상하 12-16px |

#### C. 중앙 타이틀 스펙 (0-2초만)

| 항목 | 값 |
|------|-----|
| **위치** | 세로 45% (화면 중앙보다 살짝 위) |
| **폰트 두께** | Medium ~ Semibold |
| **크기** | 화면 높이의 7-9% |
| **줄 수** | 1줄 권장, 최대 2줄 (행간 0.95) |
| **등장/퇴장** | 0.2초 이내 (강한 타이틀 느낌) |

**드랍쉐도우 (중앙 타이틀):**
| 항목 | 값 |
|------|-----|
| Opacity | 60-80% |
| Blur | 20-28 |
| Distance Y | 10-16 |
| Distance X | 0 |
| Color | Black |

#### D. 금지 구역

| 구역 | 규칙 |
|------|------|
| 하단 0-30% | ❌ 절대 침범 금지 (YouTube UI 영역) |
| 우측 중앙 | ❌ 텍스트 길게 금지 (좋아요/댓글 버튼) |

> ⚠️ 하단 30%에 텍스트 배치 시 YouTube UI에 가려짐

---

### Shorts CLI 옵션

```bash
python vibem.py shorts [TRACK_PATH] \
  --start 01:35 --duration 40 \
  --title "잠들지 못한 새벽" \
  --srt lyrics.srt \
  --title-font /path/to/heavy.otf \
  --lyric-font /path/to/medium.otf
```

| 옵션 | 기본값 | 설명 |
|------|--------|------|
| `--title` | None | 중앙 타이틀 (훅 문구) |
| `--title-duration` | 4 | 타이틀 표시 시간 (초) |
| `--lyric` | None | 하단 고정 가사 (static) |
| `--srt` | None | 동적 가사 SRT 파일 (dynamic) |
| `--lyric-delay` | 1 | 가사 페이드인 시작 (초) |
| `--title-font` | Pretendard Black | 타이틀(훅) 폰트 |
| `--lyric-font` | Pretendard Medium | 가사 폰트 |

**기본 폰트:**
- 훅 문구: `Pretendard-Black.otf` (Heavy)
- 가사: `Pretendard-Medium.otf`

**의존성:** 텍스트 옵션 사용 시 `ffmpeg-full` 필요
```bash
brew install ffmpeg-full
```

## Project Structure

```
vibe-m/
├── MASTER/                 # 프로젝트 헌법
│   ├── MANAGER.md          # 운영 마스터 플랜 (Phase 0~6)
│   ├── LYRICS.md           # 가사 공학 규칙 + 아카이브
│   ├── STYLE.md            # 사운드/스타일 가이드
│   ├── ROLES.md            # 역할 분리 시스템 (SSOT)
│   ├── QUICK_REF.md        # 사람용 운영 매뉴얼
│   └── VIBE-M_Master_Plan.md # CLI 스펙
│
├── SERIES/                 # 시리즈별 프로젝트
│   └── [Series_Name]/
│       └── [YYYY-MM-DD]/
│           ├── concept.md  # (선택) 컨셉 문서
│           ├── input/
│           │   ├── tracks/
│           │   ├── loop.mp4      # pack용 배경 영상
│           │   ├── shorts.mp4    # shorts용 (8~10초, 루프됨)
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
| `python3 vibem.py shorts <track_path> --start MM:SS --duration SEC [--title "..."] [--lyric "..."]` | 숏츠 생성 (9:16, 텍스트 옵션) |
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
