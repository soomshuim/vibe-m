#!/usr/bin/env bash
# check_series_gate.sh
# Legacy pre-final txt source draft gate validator
# HARD_HIPHOP_RUBRIC v1.5 / 20-00 final concept sync
#
# 사용법:
#   ./check_series_gate.sh <시리즈 디렉토리>
#   예: ./check_series_gate.sh SERIES/20-00/
#
# 입력 가정:
#   - <시리즈>/input/tracks/NN_*.txt 형식
#   - 각 .txt 파일 헤더에 다음 메타:
#       Track: <제목>
#       Order: <숫자>  (선택, 번호 없는 PASS 파일 정렬용)
#       Type: A | B | C | D | E | F
#       BPM: <숫자>
#       Key: <키>
#       Length: <시간>
#       Vocal: Male | Female
#
# 출력:
#   S1-S7 각 게이트 PASS/FAIL + 종합

set -uo pipefail

# === 정책 (HARD_HIPHOP_RUBRIC v1.5, 20곡 최종 분포) ===
TARGET_TOTAL=20
TARGET_A=3
TARGET_B=5
TARGET_C=5
TARGET_D=3
TARGET_E=2
TARGET_F=2
TARGET_MALE=14
TARGET_FEMALE=6
HARD_PCT_MIN=60   # Hard A+C+D+F 최소 60% (현재 final concept = 65%)

# BPM 영역
WARMUP_MIN=100;  WARMUP_MAX=120
MAIN_MIN=130;    MAIN_MAX=150
HIIT_MIN=140;    HIIT_MAX=180   # 메인과 일부 겹침 허용 + F축 165-180 영역
COOLDOWN_MIN=90; COOLDOWN_MAX=115   # B/E 멜로딕 마무리 영역

# 시리즈 길이 (분, v1.4 20곡 기준)
LENGTH_MIN_MIN=60
LENGTH_MAX_MIN=90

# === 파싱 ===
parse_track() {
  local file="$1"
  local field="$2"
  grep -E "^${field}:" "$file" | head -1 | sed -E "s/^${field}:[[:space:]]*//" | tr -d '\r'
}

# 트랙 순서 (Order 메타 우선, 없으면 파일명 NN_... 또는 NN__...)
track_order() {
  local file="$1"
  local order
  order=$(parse_track "$file" "Order")
  if [ -n "$order" ]; then
    printf "%s" "$order" | sed 's/^0*//'
    return
  fi
  basename "$file" | sed -E 's/^([0-9]+).*/\1/' | sed 's/^0*//'
}

# === 검증 ===
PASS_COUNT=0
FAIL_COUNT=0
ADVISORY_COUNT=0
RESULTS=""

check_pass() {
  PASS_COUNT=$((PASS_COUNT + 1))
  RESULTS="${RESULTS}$1: PASS$2\n"
}

check_fail() {
  FAIL_COUNT=$((FAIL_COUNT + 1))
  RESULTS="${RESULTS}$1: FAIL$2\n"
}

check_advisory() {
  ADVISORY_COUNT=$((ADVISORY_COUNT + 1))
  RESULTS="${RESULTS}$1: ADVISORY$2\n"
}

main() {
  if [ $# -lt 1 ]; then
    echo "사용법: $0 <시리즈 디렉토리>" >&2
    exit 2
  fi

  local series_dir="$1"
  local tracks_dir="${series_dir%/}/input/tracks"
  echo "WARN: check_series_gate.sh is a legacy pre-final txt validator. For source-final/uploaded state, prefer: python3 wavvy.py state/gate" >&2

  if [ ! -d "$tracks_dir" ]; then
    echo "ERROR: '$tracks_dir' 디렉토리 없음" >&2
    exit 2
  fi

  # 트랙 파일 수집 (정렬)
  local track_files=()
  while IFS= read -r -d '' entry; do
    track_files+=("${entry#*$'\t'}")
  done < <(
    while IFS= read -r -d '' file; do
      order=$(track_order "$file")
      if [ -z "$order" ]; then order=999; fi
      printf "%03d\t%s\0" "$order" "$file"
    done < <(find "$tracks_dir" -maxdepth 1 -name "*.txt" -type f -print0) | sort -z -n
  )

  local total=${#track_files[@]}
  if [ "$total" -eq 0 ]; then
    echo "ERROR: 트랙 파일 없음 ($tracks_dir/*.txt)" >&2
    exit 2
  fi

  # 카운트
  local count_a=0 count_b=0 count_c=0 count_d=0 count_e=0 count_f=0
  local count_warmup=0 count_main=0 count_hiit=0 count_cooldown=0
  local count_male=0 count_female=0 count_vocal_unknown=0
  local total_seconds=0
  local seq_types=()
  local seq_bpms=()

  for file in "${track_files[@]}"; do
    local type bpm length vocal vocal_lc
    type=$(parse_track "$file" "Type")
    bpm=$(parse_track "$file" "BPM")
    length=$(parse_track "$file" "Length")
    vocal=$(parse_track "$file" "Vocal")
    vocal_lc=$(printf "%s" "$vocal" | tr '[:upper:]' '[:lower:]')

    seq_types+=("$type")
    seq_bpms+=("$bpm")

    # Type 카운트
    case "$type" in
      A) count_a=$((count_a + 1));;
      B) count_b=$((count_b + 1));;
      C) count_c=$((count_c + 1));;
      D) count_d=$((count_d + 1));;
      E) count_e=$((count_e + 1));;
      F) count_f=$((count_f + 1));;
      *) echo "WARN: $file Type 미인식 ('$type')" >&2;;
    esac

    # Vocal 카운트
    case "$vocal_lc" in
      *female*) count_female=$((count_female + 1));;
      *male*) count_male=$((count_male + 1));;
      *) count_vocal_unknown=$((count_vocal_unknown + 1));;
    esac

    # BPM 영역 분류 (우선순위: 워밍업 > 쿨다운 > HIIT > 메인)
    if [ -n "$bpm" ] && [ "$bpm" -ge "$WARMUP_MIN" ] && [ "$bpm" -le "$WARMUP_MAX" ]; then
      count_warmup=$((count_warmup + 1))
    elif [ -n "$bpm" ] && [ "$bpm" -ge "$COOLDOWN_MIN" ] && [ "$bpm" -le "$COOLDOWN_MAX" ]; then
      count_cooldown=$((count_cooldown + 1))
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

  # === S1: 곡수 분포 + Hard 60% (v1.4: A+C+D+F = Hard) ===
  local hard=$((count_a + count_c + count_d + count_f))
  local nonhard=$((count_b + count_e))
  local hard_actual_pct=0
  if [ "$total" -gt 0 ]; then hard_actual_pct=$((hard * 100 / total)); fi
  local s1_detail="(A:$count_a B:$count_b C:$count_c D:$count_d E:$count_e F:$count_f = ${total}곡 / Hard:${hard} Non-Hard:${nonhard} = ${hard_actual_pct}%)"
  if [ "$count_a" -eq "$TARGET_A" ] && [ "$count_b" -eq "$TARGET_B" ] && [ "$count_c" -eq "$TARGET_C" ] && [ "$count_d" -eq "$TARGET_D" ] && [ "$count_e" -eq "$TARGET_E" ] && [ "$count_f" -eq "$TARGET_F" ] && [ "$total" -eq "$TARGET_TOTAL" ] && [ "$hard_actual_pct" -ge "$HARD_PCT_MIN" ]; then
    check_pass "S1 곡수 분포 + Hard 60%+" "  $s1_detail"
  else
    check_fail "S1 곡수 분포 + Hard 60%+" "  $s1_detail (목표: A:${TARGET_A} B:${TARGET_B} C:${TARGET_C} D:${TARGET_D} E:${TARGET_E} F:${TARGET_F} = ${TARGET_TOTAL}곡 / Hard ${HARD_PCT_MIN}%+)"
  fi

  # === S2: BPM/체감 단계 정합 (legacy 참고) ===
  local bpm_classified=$((count_warmup + count_main + count_hiit + count_cooldown))
  local s2_detail="(워밍업:$count_warmup 메인:$count_main HIIT:$count_hiit 쿨다운:$count_cooldown = ${bpm_classified}곡)"
  check_advisory "S2 BPM/체감 단계 정합" "  $s2_detail (legacy numeric count only; see HARD_HIPHOP_RUBRIC.md S2 Advisory Disposition)"

  # === S3: 장르 완충 파형 ===
  local s3_violations=()
  local wave_start wave_end wave_num idx has_buffer
  for wave_start in 0 5 10 15; do
    wave_end=$((wave_start + 4))
    wave_num=$((wave_start / 5 + 1))
    has_buffer=0
    for ((idx=wave_start; idx<=wave_end && idx<total; idx++)); do
      if [ "${seq_types[$idx]}" = "B" ] || [ "${seq_types[$idx]}" = "E" ]; then
        has_buffer=1
      fi
    done
    if [ "$has_buffer" -eq 0 ]; then
      s3_violations+=("Wave ${wave_num}(Track $((wave_start+1))-$((wave_end+1))) has no B/E buffer")
    fi
  done
  if [ "${#s3_violations[@]}" -eq 0 ]; then
    check_pass "S3 장르 완충 파형" ""
  else
    check_fail "S3 장르 완충 파형" "  위반: ${s3_violations[*]}"
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

  # === S5: Opener/Closer 체감 정합 ===
  local first_type="${seq_types[0]:-?}"
  local first_bpm="${seq_bpms[0]:-0}"
  local s5_last_idx=$((total - 1))
  local closer_type="${seq_types[$s5_last_idx]:-?}"
  local closer_bpm="${seq_bpms[$s5_last_idx]:-0}"
  local s5_detail="(Track 01 ${first_type}축, BPM ${first_bpm} / Track ${total} ${closer_type}축, BPM ${closer_bpm})"
  if [ "$first_type" = "A" ] && [ "$first_bpm" -ge 140 ] && [ "$first_bpm" -le 180 ] && { [ "$closer_type" = "B" ] || [ "$closer_type" = "E" ]; } && [ "$closer_bpm" -ge 90 ] && [ "$closer_bpm" -le 115 ]; then
    check_pass "S5 Opener/Closer 체감 정합" "  $s5_detail"
  else
    check_fail "S5 Opener/Closer 체감 정합" "  $s5_detail (목표: Track 01 A축 강한 시작 / Track ${total} B 또는 E + BPM 90-115)"
  fi

  # === S6: 마지막 2-3곡 = 멜로딕 마무리 (B+E 권장, BPM 90-115) ===
  local last_idx=$((total - 1))
  local penult_idx=$((total - 2))
  local antepenult_idx=$((total - 3))
  local last_type="${seq_types[$last_idx]:-?}"
  local last_bpm="${seq_bpms[$last_idx]:-0}"
  local penult_type="${seq_types[$penult_idx]:-?}"
  local penult_bpm="${seq_bpms[$penult_idx]:-0}"
  local antepenult_type="?"
  local antepenult_bpm="0"
  if [ "$total" -ge 3 ]; then
    antepenult_type="${seq_types[$antepenult_idx]:-?}"
    antepenult_bpm="${seq_bpms[$antepenult_idx]:-0}"
  fi
  local s6_detail="(Track ${total} ${last_type} BPM ${last_bpm} / Track $((total-1)) ${penult_type} BPM ${penult_bpm} / Track $((total-2)) ${antepenult_type} BPM ${antepenult_bpm})"
  local s6_ok=1
  # 마지막 2-3곡 중 하나는 B/E + BPM 90-115 (하나 이상 충족하면 PASS)
  local last_melodic=0
  local penult_melodic=0
  local antepenult_melodic=0
  if { [ "$last_type" = "B" ] || [ "$last_type" = "E" ]; } && [ "$last_bpm" -ge 90 ] && [ "$last_bpm" -le 115 ]; then
    last_melodic=1
  fi
  if { [ "$penult_type" = "B" ] || [ "$penult_type" = "E" ]; } && [ "$penult_bpm" -ge 90 ] && [ "$penult_bpm" -le 115 ]; then
    penult_melodic=1
  fi
  if { [ "$antepenult_type" = "B" ] || [ "$antepenult_type" = "E" ]; } && [ "$antepenult_bpm" -ge 90 ] && [ "$antepenult_bpm" -le 115 ]; then
    antepenult_melodic=1
  fi
  if [ "$last_melodic" -eq 0 ] && [ "$penult_melodic" -eq 0 ] && [ "$antepenult_melodic" -eq 0 ]; then
    s6_ok=0
  fi
  if [ "$s6_ok" -eq 1 ]; then
    check_pass "S6 마지막 멜로딕 마무리" "  $s6_detail"
  else
    check_fail "S6 마지막 멜로딕 마무리" "  $s6_detail (목표: 마지막 2-3곡 중 하나는 B 또는 E + BPM 90-115)"
  fi

  # === S7: 보컬 성별 분포 (남성 14 / 여성 6) ===
  local s7_detail="(Male:$count_male Female:$count_female Unknown:$count_vocal_unknown = ${total}곡)"
  if [ "$count_male" -eq "$TARGET_MALE" ] && [ "$count_female" -eq "$TARGET_FEMALE" ] && [ "$count_vocal_unknown" -eq 0 ] && [ "$total" -eq "$TARGET_TOTAL" ]; then
    check_pass "S7 보컬 성별 분포" "  $s7_detail"
  else
    check_fail "S7 보컬 성별 분포" "  $s7_detail (목표: Male:${TARGET_MALE} Female:${TARGET_FEMALE}, 모든 트랙 Vocal 메타 필요)"
  fi

  # === 출력 ===
  printf "%b" "$RESULTS"
  echo ""
  local total_gates=$((PASS_COUNT + FAIL_COUNT))
  if [ "$FAIL_COUNT" -eq 0 ]; then
    echo "종합: PASS (${PASS_COUNT}/${total_gates} hard gates, ${ADVISORY_COUNT} advisory)"
    exit 0
  else
    echo "종합: FAIL (${FAIL_COUNT}/${total_gates} hard gates FAIL, ${ADVISORY_COUNT} advisory)"
    exit 1
  fi
}

main "$@"
