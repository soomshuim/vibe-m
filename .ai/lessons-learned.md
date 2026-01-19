# Lessons Learned - vibe-m

> 버그 패턴 및 해결책 기록
>
> Last updated: 2026-01-18

---

## FFmpeg 버그 패턴

### 필터 그래프 인덱싱 오류

**날짜**: 2026-01-18

**상황**: 3개 트랙 크로스페이드 병합 시도

**증상**:
```
Filter 'acrossfade:default' has output 1 (a01) unconnected
Error binding filtergraph inputs/outputs: Invalid argument
```

**원인**:
```python
# 잘못된 코드
for i in range(2, num_tracks):
    prev_label = f"a{str(i-2).zfill(2)}"  # i=2일 때 a00 (틀림)
    curr_label = f"a{str(i-1).zfill(2)}"  # i=2일 때 a01 (중복)
```

생성된 필터:
```
[0][1]acrossfade[a01];[a00][2]acrossfade[a01]  # 틀림
```

**해결**:
```python
# 올바른 코드
for i in range(2, num_tracks):
    prev_label = f"a{str(i-1).zfill(2)}"  # i=2일 때 a01
    curr_label = f"a{str(i).zfill(2)}"    # i=2일 때 a02

final_label = f"a{str(num_tracks-1).zfill(2)}"
```

생성된 필터:
```
[0][1]acrossfade[a01];[a01][2]acrossfade[a02]  # 맞음
```

**재발 방지**:
- 필터 그래프 수정 시 반드시 출력 로그로 확인
- 라벨 체인: `[0][1]→[a01]`, `[a01][2]→[a02]`, `[a02][3]→[a03]`

---

## ffmpeg-normalize 버그 패턴

### PATH 문제

**날짜**: 2026-01-18

**상황**: `pack` 커맨드에서 정규화 실행

**증상**:
```
ffmpeg-normalize not found. Install with: pip install ffmpeg-normalize
```

**원인**:
- pip 설치 시 CLI가 `~/Library/Python/3.9/bin/`에 설치됨
- 해당 경로가 시스템 PATH에 없음

**해결**:
```python
# 변경 전
cmd = ['ffmpeg-normalize', ...]

# 변경 후
cmd = [sys.executable, '-m', 'ffmpeg_normalize', ...]
```

**재발 방지**:
- Python CLI 도구는 `python -m` 방식으로 호출

---

### MP3 출력 형식 오류

**날짜**: 2026-01-18

**상황**: 정규화 후 MP3로 저장 시도

**증상**:
```
Output extension mp3 does not support PCM audio.
Please choose a suitable audio codec with the -c:a option.
```

**원인**:
- ffmpeg-normalize는 기본적으로 PCM 출력
- MP3는 PCM을 직접 담을 수 없음

**해결**:
```python
# 변경 전
norm_path = paths.norm_tracks_dir / f"norm_{track.path.name}"  # .mp3

# 변경 후
norm_path = paths.norm_tracks_dir / f"norm_{track.path.stem}.wav"  # .wav
```

**재발 방지**:
- 중간 파일은 WAV 형식 사용
- 최종 출력만 압축 포맷 (AAC/MP3) 적용

---

## 경로 버그 패턴

### 잘못된 경로 탐색

**날짜**: 2026-01-18

**상황**: `series/test_pilot/2026-01-18` 경로 검증 시도

**증상**:
- 존재하지 않는 경로로 validate 시도
- 실제 경로: `series/TestSeries/2026-01-18`

**원인**:
- 경로명 추측 (확인 없이 진행)

**해결**:
- `ls -laR` 또는 `find`로 실제 구조 확인 후 진행

**재발 방지**:
- 경로 작업 전 항상 실제 구조 확인
- 문서에 실제 예시 경로 명시

---

## 가사 작성 버그 패턴

### 괄호 주석 혼입

**날짜**: 2026-01-18

**상황**: Track 04 가사 초안 작성 시 설명용 괄호 포함

**증상**:
```
가로등이 번져가
젖은 바닥 위로
걸음을 멈춰도
발자국만 남아 (4행, 각 5-6음절)  ← 괄호 혼입
```

**원인**:
- 가사와 설명 주석을 같은 코드블록에 작성
- LYRICS.md 2.1 "괄호 속 지시어 금지" 규칙 위반

**리스크**:
- 사용자가 복사해서 Suno에 붙여넣으면 괄호 텍스트를 가사로 인식
- 보컬이 "(4행, 각 5-6음절)"을 읽어버림

**해결**:
```markdown
# 잘못된 방식 (가사 블록 내 주석)
[verse1]
가로등이 번져가 (스냅샷)

# 올바른 방식 (가사와 분석 분리)
## 가사
[verse1]
가로등이 번져가

## 분석
- V1 1행: 스냅샷 (명사+동사)
```

**재발 방지**:
- 가사 코드블록은 **순수 가사만** 포함
- 분석/설명은 별도 섹션으로 분리
- 가사 제시 후 체크리스트 테이블로 검증 결과 제시
- **의도한 효과(스냅샷 훅, V2 에스컬레이션 등)는 Style Prompt에서 지시**

---

## 체크리스트 요약

### FFmpeg 작업 전
- [ ] 필터 라벨 체인 로직 확인
- [ ] 디버그 로그로 생성된 필터 출력

### Python CLI 도구 사용 시
- [ ] `python -m` 방식 우선 사용
- [ ] 중간 파일은 무손실 포맷 (WAV)

### 경로 작업 전
- [ ] 실제 디렉토리 구조 확인
- [ ] 문서와 실제 구조 동기화

### 가사 작성 시
- [ ] 가사 코드블록에 괄호/주석 없음 확인
- [ ] 분석/설명은 별도 섹션으로 분리
- [ ] 복사해서 Suno에 바로 붙여넣기 가능한 상태인지 확인
