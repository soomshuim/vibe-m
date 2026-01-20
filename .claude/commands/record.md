---
description: 완료된 작업을 기록하는 표준 사후정리 도구 (CHANGELOG + SESSION.md)
allowed-tools: [Read, Edit, Glob, Grep, Bash]
---

# /record Command

완료된 작업을 기록하는 표준 사후정리 도구.

## 사용법

```
/record <type> <message>
```

## 타입

| type | 설명 | CHANGELOG 섹션 |
|------|------|----------------|
| `feature` | 새 기능 | Added |
| `refactor` | 구조 개선 | Changed |
| `fix` | 버그 수정 | Fixed |
| `docs` | 문서 변경 | Changed |
| `track` | 트랙 추가 | Added |

## 실행 절차

### 1. Git Diff 분석

```bash
# 마지막 태그 이후 변경 요약
git diff --stat $(git describe --tags --abbrev=0 2>/dev/null || echo HEAD~10)..HEAD
git diff --name-status $(git describe --tags --abbrev=0 2>/dev/null || echo HEAD~10)..HEAD
```

### 2. CHANGELOG.md 업데이트

```markdown
## [Unreleased]

### {섹션}
- {message}
```

- 버전 번호는 수동 태깅 시 확정
- `[Unreleased]` 섹션이 없으면 생성

### 3. SESSION.md 링크 추가

"완료된 작업" 섹션에 한 줄 추가:
```markdown
| {type}: {message 요약} | - | - | `{최신커밋hash}` |
```

### 4. 완료 메시지

```
✅ 기록 완료
- CHANGELOG: {섹션}에 추가
- SESSION: 링크 추가
- 커밋: {hash}
```

## 예시

```
/record track Track 08 "빗줄기" 추가
/record docs STYLE.md v2.6 업데이트
/record fix 가사 QC 체크리스트 오류 수정
/record feature 새 플레이리스트 컨셉 추가
```

## 주의사항

- `/record`는 **커밋 후** 실행 (커밋되지 않은 변경은 무시)
- 버전 태그는 별도 수동 작업
- 트랙 작업 시 `track` 타입 사용 권장
