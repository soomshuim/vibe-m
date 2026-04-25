#!/usr/bin/env bash
# check_lyric_avoid.sh
# 가사 회피 영역 자동 검사 (HARD_HIPHOP_RUBRIC v1.1 H8)
#
# 사용법:
#   ./check_lyric_avoid.sh <파일 또는 디렉토리>
#
# 출력:
#   PASS — 회피 키워드 매칭 0
#   FAIL — 매칭 키워드 + 카테고리 + 횟수
#
# 회피 정책: 무차별 폭력·살해·총기·마약·혐오·자해·자살·노골적 성행위 직접 묘사
# 보존: K-Drill 본가 어휘 (갱·크루·블록·동네·디스·flex·돈·자랑·반항·자기 서사)

set -euo pipefail

# 50 키워드 5카테고리 (정확 매칭, 한국어 + 영어)
KW_VIOLENCE="총기 총살 살해 살인 강간 강도 흉기 칼부림 테러 폭격"
KW_DRUG="마약 코카인 필로폰 헤로인 메스암페타민 엑스터시 MDMA LSD 메스 대마초"
KW_HATE="김치녀 맘충 한남 일베 짱깨 쪽바리 검둥이 니그로 트젠 보슬"
KW_SELFHARM="자살해 자해해 목매 투신 할복 약물과다 옥상에서뛰어 농약마셔 수면제털어 동맥자르"
KW_SEXUAL="섹스해 자위해 오럴섹스 항문섹스 삽입해 사정해 정액 유두 음경 음부"

check_category() {
  local file="$1"
  local cat_name="$2"
  local keywords="$3"
  local matches=""
  local cat_total=0

  for kw in $keywords; do
    local count
    count=$(grep -c -F "$kw" "$file" 2>/dev/null || echo 0)
    if [ "$count" -gt 0 ]; then
      matches="$matches $kw($count)"
      cat_total=$((cat_total + count))
    fi
  done

  if [ "$cat_total" -gt 0 ]; then
    echo "  ${cat_name}:${matches}"
    echo "$cat_total"
  else
    echo "0"
  fi
}

check_file() {
  local file="$1"
  local total=0
  local report=""

  for entry in "violence:폭력·살해:$KW_VIOLENCE" \
               "drug:마약:$KW_DRUG" \
               "hate:혐오:$KW_HATE" \
               "selfharm:자해·자살:$KW_SELFHARM" \
               "sexual:노골적 성행위:$KW_SEXUAL"; do
    local cat_name="${entry#*:}"
    cat_name="${cat_name%%:*}"
    local keywords="${entry##*:}"
    local matches=""
    local cat_total=0

    for kw in $keywords; do
      local count
      count=$(grep -c -F -- "$kw" "$file" 2>/dev/null || true)
      count=${count:-0}
      if [ "$count" -gt 0 ]; then
        matches="$matches $kw($count)"
        cat_total=$((cat_total + count))
      fi
    done

    if [ "$cat_total" -gt 0 ]; then
      report="${report}  ${cat_name}:${matches}\n"
      total=$((total + cat_total))
    fi
  done

  if [ "$total" -eq 0 ]; then
    echo "PASS  $file"
    return 0
  else
    echo "FAIL  $file  (총 ${total}회 매칭)"
    printf "%b" "$report"
    return 1
  fi
}

main() {
  if [ $# -lt 1 ]; then
    echo "사용법: $0 <파일 또는 디렉토리>" >&2
    exit 2
  fi

  local target="$1"
  local fail_count=0
  local total_files=0

  if [ -d "$target" ]; then
    while IFS= read -r -d '' file; do
      total_files=$((total_files + 1))
      check_file "$file" || fail_count=$((fail_count + 1))
    done < <(find "$target" -name "*.txt" -type f -print0)
  elif [ -f "$target" ]; then
    total_files=1
    check_file "$target" || fail_count=1
  else
    echo "ERROR: '$target' 파일/디렉토리 없음" >&2
    exit 2
  fi

  echo ""
  if [ "$fail_count" -gt 0 ]; then
    echo "종합: FAIL ($fail_count / $total_files 파일 회피 키워드 매칭)"
    exit 1
  fi
  echo "종합: PASS ($total_files 파일 모두 회피 키워드 0)"
}

main "$@"
