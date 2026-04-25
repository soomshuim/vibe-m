#!/usr/bin/env bash
# check_series_gate.sh
# 시리즈 단위 게이트 자동 검증 (HARD_HIPHOP_RUBRIC v1.1 S1-S6)
#
# 사용법:
#   ./check_series_gate.sh <시리즈 디렉토리>
#   예: ./check_series_gate.sh SERIES/20-00/
#
# 입력 가정:
#   - <시리즈>/input/tracks/NN_*.txt 형식
#   - 각 .txt 파일 헤더에 다음 메타:
#       Track: <제목>
#       Type: A | B | C | D | E
#       BPM: <숫자>
#       Key: <키>
#       Length: <시간>
#
# 출력:
#   S1-S6 각 게이트 PASS/FAIL + 종합

set -uo pipefail

# === 정책 (HARD_HIPHOP_RUBRIC v1.1) ===
TARGET_TOTAL=20
TARGET_A=4
TARGET_B=5
TARGET_C=5
TARGET_D=3
TARGET_E=3
HARD_PCT=60   # A+C+D = 12 / 20 = 60%

# BPM 영역
WARMUP_MIN=100;  WARMUP_MAX=120
MAIN_MIN=130;    MAIN_MAX=150
HIIT_MIN=140;    HIIT_MAX=180   # 메인과 일부 겹침 허용
COOLDOWN_MIN=90; COOLDOWN_MAX=110

# 시리즈 길이 (분)
LENGTH_MIN_MIN=60
LENGTH_MAX_MIN=90

# === 파싱 ===
parse_track() {
  local file="$1"
  local field="$2"
  grep -E "^${field}:" "$file" | head -1 | sed -E "s/^${field}:[[:space:]]*//" | tr -d '\r'
}

# 트랙 번호 (파일명 NN_... 또는 NN__...)
track_number() {
  local file="$1"
  basename "$file" | sed -E 's/^([0-9]+).*/\1/' | sed 's/^0*//'
}

# === 검증 ===
PASS_COUNT=0
FAIL_COUNT=0
RESULTS=""

check_pass() {
  PASS_COUNT=$((PASS_COUNT + 1))
  RESULTS="${RESULTS}$1: PASS$2\n"
}

check_fail() {
  FAIL_COUNT=$((FAIL_COUNT + 1))
  RESULTS="${RESULTS}$1: FAIL$2\n"
}

main() {
  if [ $# -lt 1 ]; then
    echo "사용법: $0 <시리즈 디렉토리>" >&2
    exit 2
  fi

  local series_dir="$1"
  local tracks_dir="${series_dir%/}/input/tracks"

  if [ ! -d "$tracks_dir" ]; then
    echo "ERROR: '$tracks_dir' 디렉토리 없음" >&2
    exit 2
  fi

  # 트랙 파일 수집 (정렬)
  local track_files=()
  while IFS= read -r -d '' file; do
    track_files+=("$file")
  done < <(find "$tracks_dir" -maxdepth 1 -name "*.txt" -type f -print0 | sort -z)

  local total=${#track_files[@]}
  if [ "$total" -eq 0 ]; then
    echo "ERROR: 트랙 파일 없음 ($tracks_dir/*.txt)" >&2
    exit 2
  fi

  # 카운트
  local count_a=0 count_b=0 count_c=0 count_d=0 count_e=0
  local count_warmup=0 count_main=0 count_hiit=0 count_cooldown=0
  local total_seconds=0
  local seq_types=()
  local seq_bpms=()

  for file in "${track_files[@]}"; do
    local type bpm length
    type=$(parse_track "$file" "Type")
    bpm=$(parse_track "$file" "BPM")
    length=$(parse_track "$file" "Length")

    seq_types+=("$type")
    seq_bpms+=("$bpm")

    # Type 카운트
    case "$type" in
      A) count_a=$((count_a + 1));;
      B) count_b=$((count_b + 1));;
      C) count_c=$((count_c + 1));;
      D) count_d=$((count_d + 1));;
      E) count_e=$((count_e + 1));;
      *) echo "WARN: $file Type 미인식 ('$type')" >&2;;
    esac

    # BPM 영역 분류 (우선순위: 워밍업 > 쿨다운 > HIIT > 메인)
    if [ -n "$bpm" ] && [ "$bpm" -ge "$COOLDOWN_MIN" ] && [ "$bpm" -le "$COOLDOWN_MAX" ]; then
      count_cooldown=$((count_cooldown + 1))
    elif [ -n "$bpm" ] && [ "$bpm" -ge "$WARMUP_MIN" ] && [ "$bpm" -le "$WARMUP_MAX" ]; then
      count_warmup=$((count_warmup + 1))
    elif [ -n "$bpm" ] && [ "$bpm" -gt "$MAIN_MAX" ] && [ "$bpm" -le "$HIIT_MAX" ]; then
      count_hiit=$((count_hiit + 1))
    elif [ -n "$bpm" ] && [ "$bpm" -ge "$MAIN_MIN" ] && [ "$bpm" -le "$MAIN_MAX" ]; then
      count_main=$((count_main + 1))
    fi

    # 길이 합산 (분 단위 추출, "3:30" 또는 "3min+" 형식)
    if [[ "$length" =~ ^([0-9]+):([0-9]+) ]]; then
      total_seconds=$((total_seconds + ${BASH_REMATCH[1]} * 60 + ${BASH_REMATCH[2]}))
    elif [[ "$length" =~ ^([0-9]+)min ]]; then
      total_seconds=$((total_seconds + ${BASH_REMATCH[1]} * 60))
    fi
  done

  # === S1: 곡수 분포 + Hard 60% ===
  local hard=$((count_a + count_c + count_d))
  local nonhard=$((count_b + count_e))
  local hard_actual_pct=0
  if [ "$total" -gt 0 ]; then hard_actual_pct=$((hard * 100 / total)); fi
  local s1_detail="(A:$count_a B:$count_b C:$count_c D:$count_d E:$count_e = ${total}곡 / Hard:${hard} Non-Hard:${nonhard} = ${hard_actual_pct}%)"
  if [ "$count_a" -eq "$TARGET_A" ] && [ "$count_b" -eq "$TARGET_B" ] && [ "$count_c" -eq "$TARGET_C" ] && [ "$count_d" -eq "$TARGET_D" ] && [ "$count_e" -eq "$TARGET_E" ] && [ "$total" -eq "$TARGET_TOTAL" ] && [ "$hard_actual_pct" -eq "$HARD_PCT" ]; then
    check_pass "S1 곡수 분포 + Hard 60%" "  $s1_detail"
  else
    check_fail "S1 곡수 분포 + Hard 60%" "  $s1_detail (목표: A:${TARGET_A} B:${TARGET_B} C:${TARGET_C} D:${TARGET_D} E:${TARGET_E} = ${TARGET_TOTAL}곡 / Hard ${HARD_PCT}%)"
  fi

  # === S2: BPM 분포 ===
  local bpm_classified=$((count_warmup + count_main + count_hiit + count_cooldown))
  local s2_detail="(워밍업:$count_warmup 메인:$count_main HIIT:$count_hiit 쿨다운:$count_cooldown = ${bpm_classified}곡)"
  if [ "$count_warmup" -ge 2 ] && [ "$count_warmup" -le 3 ] && [ "$count_main" -ge 8 ] && [ "$count_main" -le 9 ] && [ "$count_hiit" -ge 5 ] && [ "$count_hiit" -le 6 ] && [ "$count_cooldown" -ge 2 ] && [ "$count_cooldown" -le 3 ]; then
    check_pass "S2 BPM 분포" "  $s2_detail"
  else
    check_fail "S2 BPM 분포" "  $s2_detail (목표: 워밍업 2-3 / 메인 8-9 / HIIT 5-6 / 쿨다운 2-3)"
  fi

  # === S3: A·B 인접 회피 ===
  local s3_violations=()
  for ((i=0; i<${#seq_types[@]}-1; i++)); do
    local cur="${seq_types[$i]}"
    local nxt="${seq_types[$i+1]}"
    if { [ "$cur" = "A" ] && [ "$nxt" = "B" ]; } || { [ "$cur" = "B" ] && [ "$nxt" = "A" ]; }; then
      s3_violations+=("Track $((i+1))($cur)→Track $((i+2))($nxt)")
    fi
  done
  if [ "${#s3_violations[@]}" -eq 0 ]; then
    check_pass "S3 A·B 인접 회피" ""
  else
    check_fail "S3 A·B 인접 회피" "  위반: ${s3_violations[*]}"
  fi

  # === S4: 시리즈 길이 60-90분 ===
  local total_minutes=$((total_seconds / 60))
  local total_sec_remain=$((total_seconds % 60))
  local s4_detail="(${total_minutes}분 ${total_sec_remain}초)"
  if [ "$total_minutes" -ge "$LENGTH_MIN_MIN" ] && [ "$total_minutes" -le "$LENGTH_MAX_MIN" ]; then
    check_pass "S4 시리즈 길이" "  $s4_detail"
  else
    check_fail "S4 시리즈 길이" "  $s4_detail (목표: ${LENGTH_MIN_MIN}-${LENGTH_MAX_MIN}분)"
  fi

  # === S5: Track 01 = 워밍업 B축 ===
  local first_type="${seq_types[0]:-?}"
  local first_bpm="${seq_bpms[0]:-0}"
  local s5_detail="(Track 01 ${first_type}축, BPM ${first_bpm})"
  if [ "$first_type" = "B" ] && [ "$first_bpm" -ge "$WARMUP_MIN" ] && [ "$first_bpm" -le "$WARMUP_MAX" ]; then
    check_pass "S5 Track 01 워밍업 B축" "  $s5_detail"
  else
    check_fail "S5 Track 01 워밍업 B축" "  $s5_detail (목표: B축 BPM ${WARMUP_MIN}-${WARMUP_MAX})"
  fi

  # === S6: 마지막 2-3곡 = 멜로딕 마무리 (B+E, BPM 90-115) ===
  local last_idx=$((total - 1))
  local penult_idx=$((total - 2))
  local last_type="${seq_types[$last_idx]:-?}"
  local last_bpm="${seq_bpms[$last_idx]:-0}"
  local penult_type="${seq_types[$penult_idx]:-?}"
  local penult_bpm="${seq_bpms[$penult_idx]:-0}"
  local s6_detail="(Track ${total} ${last_type} BPM ${last_bpm} / Track $((total-1)) ${penult_type} BPM ${penult_bpm})"
  local s6_ok=1
  # 마지막 곡: B 또는 E + BPM 90-115
  if ! { [ "$last_type" = "B" ] || [ "$last_type" = "E" ]; } || [ "$last_bpm" -lt 90 ] || [ "$last_bpm" -gt 115 ]; then
    s6_ok=0
  fi
  if [ "$s6_ok" -eq 1 ]; then
    check_pass "S6 마지막 멜로딕 마무리" "  $s6_detail"
  else
    check_fail "S6 마지막 멜로딕 마무리" "  $s6_detail (목표: 마지막 곡 B 또는 E + BPM 90-115)"
  fi

  # === 출력 ===
  printf "%b" "$RESULTS"
  echo ""
  if [ "$FAIL_COUNT" -eq 0 ]; then
    echo "종합: PASS (${PASS_COUNT}/6 게이트)"
    exit 0
  else
    echo "종합: FAIL (${FAIL_COUNT}/6 게이트 FAIL)"
    exit 1
  fi
}

main "$@"
