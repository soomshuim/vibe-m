---
description: vibe-m 프로젝트 재개 - SESSION.md와 프로젝트 개요 로드
allowed-tools: [Read, Glob, Bash]
---

# /vibem Command

vibe-m 프로젝트를 재개하기 위한 컨텍스트 로딩 커맨드.

## 프로젝트 경로

```
~/vibe-m
```

## 실행 절차

### 1. 프로젝트 개요 로드

`~/vibe-m/CLAUDE.md` 파일을 읽어서 프로젝트 구조와 규칙을 파악한다.

### 2. 현재 세션 상태 로드

`~/vibe-m/.ai/SESSION.md` 파일을 읽어서:
- 진행 중인 작업
- 최근 완료된 작업
- 다음 할 일

### 3. 현재 시리즈 상태 확인

```bash
ls -la ~/vibe-m/SERIES/
```

활성 시리즈 폴더와 최신 볼륨 확인.

### 4. Git 상태 확인

```bash
cd ~/vibe-m && git status --short && git log --oneline -5
```

### 5. 요약 출력

다음 형식으로 현재 상태를 요약:

```
## vibe-m 프로젝트 재개

**현재 시리즈:** {시리즈명}
**최신 볼륨:** {vol 번호}
**Git 상태:** {clean/변경사항 있음}

### 최근 작업
- {SESSION.md에서 추출}

### 다음 할 일
- {SESSION.md에서 추출}

---
무엇을 도와드릴까요?
```

## 사용법

```
/vibem
```

인자 없이 실행하면 자동으로 프로젝트 컨텍스트를 로드하고 요약을 출력한다.
