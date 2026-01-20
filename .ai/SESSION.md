# Session State - vibe-m

> 현재 세션 상태 기록
>
> Last updated: 2026-01-20

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

- **프로젝트**: Production Ready (v1.4.0 - Suno Guide 2.0 Merge)
- **GitHub**: https://github.com/soomshuim/vibe-m (master)
- **플레이리스트 제목**: "잠들지 못한 새벽, 이 노래들이 위로가 되길"
- **문서 버전**:
  - LYRICS.md v1.6
  - STYLE.md v2.6
  - CLAUDE.md v1.5.0
- **작업 디렉토리**: `SERIES/잠들지_못한_새벽/vol1/`
  - 트랙 9곡 완료 (Track 01~09) **플레이리스트 완성**
  - 에셋: `loop.mp4`, `thumb.jpg` 준비됨

## 진행 중

- 없음 (9트랙 완료, 패키징 대기)

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
  - 가사 QC 9/9 PASS, Style Prompt 9/9 PASS
- [x] 워크플로우 강화
  - PLAYLIST_GUIDE.md 생성 (유튜브 인기 사례 분석)
  - LYRICS.md v1.1 (새 규칙 4개)
- [x] **STYLE.md v1.5: Single-Lead Explosion + Zero Exception** (`73800c6`)
  - Harmony Guard 예외 조항 완전 제거
  - "vocals unchanged" → "keep SINGLE lead (no layers)" 대체
  - Chorus/V2 Lift 정량화 (1 held note, 1 event)
  - Self-QC 3-Step 프로세스 강화
- [x] Track 04 "물안개" MP3 생성 완료 (Suno)
- [x] 4트랙 Preview 생성 완료 (60초)
- [x] **STYLE.md v1.6: Energy Permission + Safety Separation**
  - 핵심 원칙: "금지는 레이어에만, 허용은 에너지에"
  - "vocals unchanged" → "lead vocal energy may increase, but no new vocal layers"
  - "Single lead vocal ONLY" → "Lead vocal remains single and dominant"
  - Verse2 에너지 상승 권한 명시적 부여 (encouraged/allowed)
- [x] ROLES.md v1.1: Energy Permission Principle 추가
- [x] 02_designer.txt: Safety Lines + Energy Permission 분리
- [x] 03_variation.txt: Vocal Energy Risk Fail 조건 추가
  - Verse2 lacks lift → FAIL
  - Chorus sounds flat due to over-safety → FAIL
- [x] **STYLE.md v1.7: Fail Fast Energy Check**
  - Chorus held note 정량화: "exactly 1 held note"
  - V2 → Chorus FAIL 조건 4개 추가
- [x] ROLES.md v1.2: Automatic FAIL Conditions 추가
- [x] 00_system.txt: Mandatory Slot Check 추가
- [x] 02/03_designer.txt: INVALID conditions 추가

### 2026-01-19 (오후)

- [x] **Energy Permission 문서 일괄 강화** (무난함 방지)
  - 문제: "금지"만 강하고 "허용"이 흩어져서 AI가 평균값(무난함)으로 수렴
  - 해결: Safety Lines와 Energy Permission을 **항상 쌍으로** 배치
  - **STYLE.md v1.8**: Energy Permission (Mandatory) 섹션 추가
  - **02_designer.txt**: Seed-Level Energy Permission 블록 강화
  - **03_variation.txt**: PASS Criteria 추가 + "safe but unmemorable = FAIL"
  - **ROLES.md v1.3**: Team Philosophy 섹션 추가 ("무난함 = 실패" 문화 선언)

- [x] **Seed Energy Contract 헌법화** (마무리 보강)
  - **ROLES.md v1.4**: `Seed Energy Contract (Non-Negotiable)` 섹션 추가
    - "This contract overrides any safety or layer prohibition"
    - Canonical Sentence 전 문서 동일화 선언
  - **STYLE.md v1.9**: Canonical Sentence Unification
    - S8/S9 체크리스트 문장 통일 (ONLY 제거)
  - **02_designer.txt**: "safe/flat = INVALID" 조건 추가
  - **03_variation.txt**: Final Verdict Question 추가
    - "Does the Chorus feel more emotionally intense than Verse2 without adding layers?"

- [x] **100점 마무리 개선**
  - **04_ultra_compressed.txt**: 실행용 초압축 프롬프트 템플릿 생성
    - Canonical Blocks (A/B/C/D) 복붙 가능
    - ~750 chars 예시 포함
  - **"1 held note" 표현 통일**: 전 문서에 "longer sustain than any verse note" 고정
    - STYLE.md 4개소
    - 03_variation.txt 1개소
  - **Energy Reference 정량 기준 추가** (QC용, 프롬프트용 아님)
    - "Chorus peak note should sustain at least 1.5x longer than any Verse note"
    - STYLE.md + 03_variation.txt에 추가

- [x] **LYRICS.md v1.2 + STYLE.md v2.0 피드백 영구 반영**
  - **LYRICS.md v1.2:**
    - 1.2 Ending Mirroring 강화 (품사 불일치 = FAIL)
    - 1.9 Physical Object Anchor Rule (물성 오브젝트 앵커) 추가
    - Case 09: Abstract Word Density (추상어 과밀) 추가
    - Case 10: Ending 품사 불일치 추가
  - **STYLE.md v2.0:**
    - 4.4 Belt/Tempo Conflict Rule 추가 (Chill에서 belt 충돌)
    - Slot F: Mood Bucket 추가 (Chill/Hazy/Ethereal/Nocturne 등)
    - 6) Exclude 강화 (3그룹 최대, 과도한 Exclude 부작용 경고)

### 2026-01-20

- [x] **Suno Guide 2.0 시스템 병합 완료**
  - 외부 가이드 3종 분석 및 병합:
    - Reddit Style Prompt Guide 2.0
    - Section Tags 전체 목록
    - museA Suno 자료집 (한국어)
  - **LYRICS.md v1.4 → v1.5**
    - 구조 태그 10종 추가 ([pre-chorus], [breakdown], [hook], [big finish] 등)
    - Performance Cues 섹션 신규 추가 ((whispered), (belted), (soft) 등)
    - 가사 길이 가이드라인 추가 (100-120 단어 권장)
    - 구조 공식 옵션 추가 (Pop Standard, K-POP Standard, Storyteller)
  - **STYLE.md v2.4 → v2.5**
    - 0.4 Prompt Priority Rule: "핵심 앞에" (Genre/BPM 첫 5단어)
    - 0.5 Gravity Words: 중력 우물 단어 회피 (pop, beat, bass - 원치 않는 경우만)
    - 10) A/B Testing Rules: 한 번에 1개 변수만 변경
    - 11) Co-occurrence Hints: 장르 조합 가이드
    - 12) Tag Bank: 검증된 키워드 사전 (보컬/악기/프로덕션)
    - Raw Vocal Baseline 수정: **Powerful을 기본값에서 제거** → 요청 시 추가
  - **CLAUDE.md v1.3.0 → v1.4.0**
    - S0 "핵심 앞에" 체크 항목 추가
    - S1 Powerful 제거 반영
    - 2.4 가사 길이 가이드 추가
  - 충돌 해결:
    - "pop" 중력 우물: "원치 않는 경우에만 회피" (Pop 원하면 사용 OK)
    - 괄호 정책 분리: 설명형 금지 vs Performance Cues 허용
    - Powerful: 기본값 아닌 요청 시 추가 (airy, husky와 동일 레벨)

### 2026-01-20 (오후) — Guide 5종 검증 + GPT 피드백 통합

- [x] **레퍼런스 가이드 5종 전수 검증**
  - 유튜브 감성 플레이리스트 인기 사례 분석
  - museA Suno 자료집
  - Suno Style Prompt Guide 2.0
  - Section Tags 전체 목록
  - 커뮤니티/공식 자료 수렴 원리

- [x] **GPT 피드백 6개 포인트 통합**
  1. DEBUG/PROD 모드 분리 (1변수 디버깅)
  2. Pure Lyric Input 근거 명시
  3. Texture Lines 라이브러리 추가
  4. 태그 경계 명확화 (필수/옵션/주의)
  5. S1-S9 Validation 강제 출력
  6. Exclude 운영 규칙 강화

- [x] **문서 업데이트 완료**
  - **STYLE.md v2.5 → v2.6**
    - 0.6 Broad Genre Labels Rule
    - 6.1 Exclude 운영 규칙
    - 10.0 DEBUG/PROD 모드 추가
    - 10.4 DEBUG 기록 양식
    - 12.5 Texture Lines (믹스/공간 제어)
    - 12.6 FX/Production 키워드
  - **LYRICS.md v1.5 → v1.6**
    - 2.0 Pure Lyric Input 근거 명시 (가이드와 다른 이유)
    - 2.2 태그 경계 명확화 (필수/옵션/주의/고급)
  - **MANAGER.md v1.1 → v1.2**
    - Phase 2.5 A/B Testing Protocol
    - 보컬 타입 누락 방지 강제
  - **ROLES.md v1.5 → v1.6**
    - S1-S9 Validation Enforcement 섹션
    - 출력 필수 형식 정의
  - **prompts (02_designer, 03_variation)**
    - 🔴 MANDATORY OUTPUT FORMAT 추가
    - S1-S9 테이블 없으면 INVALID
  - **CLAUDE.md v1.4.0 → v1.5.0**
    - DEBUG/PROD 모드 안내
    - S1-S9 Validation 강제 안내

### 2026-01-20 (저녁)

- [x] **Track 09 "마음안" 완료** (`cb2543e`)
  - 수미상관 마지막 곡 (Track 01 "마음밖" 대응)
  - Male vocal + Powerful belt, 95 BPM, Db Major
  - 키워드 축: 여명/옥상/난간/지평선
  - 후렴: "마음 안으로 번져와 / 여명처럼 스며들어"
- [x] **Track 08 "빗줄기" 완료** (`286ceef`)
  - Melancholic R&B, 85 BPM, F minor, Rhodes-led
  - 키워드 축: 빗줄기/아스팔트/골목/처마/우산
  - Raw Vocal + Chest Belt, Contralto female
  - 메타태그: Direct vocal, Chest voice, Powerful belt
  - bridge2 가사 개선: 물방울/턱/입술 등 신체 감각 디테일
- [x] `/record` 커맨드 추가 (`.claude/commands/record.md`)
- [x] Reference 가이드 PDF 5종 추가
- [x] **첫 플레이리스트 정식 출범** (`c686ba6`)
  - 제목: "잠들지 못한 새벽, 이 노래들이 위로가 되길"
  - 디렉토리: `SERIES/Test_Series/2026-01-18/` → `SERIES/잠들지_못한_새벽/vol1/`
  - 9트랙 완성 (Track 01~09)

## 다음 작업 (예정)

- [ ] validate → pack (최종 패키징)

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
