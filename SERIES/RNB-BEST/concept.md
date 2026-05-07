# R&B BEST

Version: 0.1
Last Updated: 2026-05-07

---

## Series Type

- **Type**: Compilation / Best Album
- **Source**: Existing Wavvy R&B and R&B-adjacent tracks only
- **Selection Owner**: User
- **Track Count**: Flexible. 20 tracks is not a limit.
- **New Song Generation**: None by default
- **Positioning**: Not a 24H Station entry. This is a curated Wavvy R&B best album.

---

## Core Idea

**계속 듣고 싶은 한국어 R&B 모음.**

이 시리즈는 특정 시간대나 단일 무드에 맞춘 새 제작 시리즈가 아니다.
기존 Wavvy R&B 계열 트랙 중 사용자가 반복해서 듣고 싶은 곡을 직접 고르고,
그 곡들을 하나의 앨범처럼 다시 묶는 compilation이다.

느린 곡도 들어갈 수 있고, 빠른 곡도 들어갈 수 있다.
중요한 기준은 BPM 균일성이 아니라 다시 듣고 싶은 감각이다.

---

## Selection Policy

### Do

- 사용자가 직접 고른 곡만 포함한다.
- 기존 Wavvy 트랙을 재활용한다.
- 느린 R&B, Soft R&B, Chill R&B, Neo-Soul, Funky R&B를 모두 허용한다.
- 곡 수는 선곡 결과를 따른다.
- 최종 순서는 사용자가 정하거나, 사용자가 요청할 때만 흐름 기준으로 재배열한다.

### Do Not

- 에이전트가 임의로 best 곡을 선정하지 않는다.
- 20곡 제한을 걸지 않는다.
- 단일 BPM/단일 무드로 억지 정렬하지 않는다.
- 기존 곡을 새로 리메이크하거나 재생성하지 않는다.
- 사용자가 고르기 전까지 Track Map을 확정하지 않는다.

---

## Source Pool

선곡 가능한 기본 범위는 기존 Wavvy R&B / R&B-adjacent 시리즈다.
아래 목록은 후보 풀의 경계일 뿐, 실제 선곡표가 아니다.

| Series | Existing Position |
|---|---|
| `SERIES/04-00` | Slow R&B / R&B Ballad |
| `SERIES/12-00` | Afro-Drill / Afropiano, R&B-adjacent picks |
| `SERIES/13-00` | Feel Good R&B / Urban Neo-Soul |
| `SERIES/14-00` | Soft R&B |
| `SERIES/15-00` | Funky R&B / Urban Neo-Soul |
| `SERIES/18-00` | Neo-Soul |
| `SERIES/21-00` | CityPop Ballad / NeoSoul-adjacent picks |
| `SERIES/22-00` | Chill R&B / Ambient Slow Jam |

기술 메모: 실제 패키징 단계에서는 로컬 원본 오디오가 있는 트랙만 바로 사용할 수 있다.
원본이 없고 `work/` 산출물만 남은 시리즈는 사용자가 명시적으로 선택했을 때 복구 또는 대체 경로를 확인한다.

---

## Listening Flow

선곡 전에는 러닝 오더를 확정하지 않는다.
다만 최종 배치가 필요할 때는 아래 원칙을 우선한다.

1. 첫 곡은 재생을 계속하고 싶게 만드는 곡으로 둔다.
2. 빠른 곡과 느린 곡을 장르 변화처럼 사용한다.
3. 비슷한 톤의 곡이 너무 오래 붙지 않게 한다.
4. 후반부는 감정선이 과하게 꺼지지 않게 유지한다.
5. 마지막 곡은 "한 번 더 들을까"가 남는 곡으로 둔다.

---

## Packaging Policy

- `SERIES/RNB-BEST/input/tracks/`에는 사용자 선곡 순서대로 복사한 오디오를 둔다.
- 파일명은 Wavvy 표준인 `NN__Title__Mood__Genre__BPM.ext`를 따른다.
- 기존 트랙의 원본 제목과 장르는 가능한 유지한다.
- 같은 곡을 다른 시리즈에서 가져오더라도 이 compilation 안에서는 새 순번만 부여한다.
- 사용자가 곡 이름만 말하면, 에이전트가 전체 `SERIES/*/input/tracks/`를 검색해 해당 음원을 찾는다.
- 매칭된 음원은 신규 시리즈 폴더에 실제 파일로 복사한다. 하드링크를 기본으로 쓰지 않는다.
- 동명의 곡이 여러 시리즈에 있거나 원본 오디오가 없으면, 복사 전 사용자에게 후보를 보여주고 확인받는다.
- `pack` 기본값은 repeat 2이므로, 곡 수가 많으면 최종 영상 길이를 별도로 확인한다.

---

## YouTube Draft (v3 - Wavvy Groovy R&B Playlist)

### Context Mode

Compilation - Wavvy의 그루브 중심 R&B best playlist.

### 제목

```text
Playlist | R&B Best | 와..이 노래 제목 뭐야? ✨ 틀자마자 리듬에 그루비 😎 | CHILL · R&B · SOUL | 카페 · 작업 · 매장 음악 | Wavvy
```

### 설명

```text
와.. 이 노래 제목 뭐야? ✨
틀자마자 분위기 좋아지는 그루비 웨이비 😎

부드럽게 기분 좋아지고,
낮부터 밤까지 자연스럽게 이어지는 Wavvy R&B 플레이리스트.

햇살 좋은 오후에 가볍게 틀어두기 좋은 Urban Soul,
차 안에서 리듬 타기 좋은 Neo-Soul,
은근하게 공간 분위기를 채워주는 Chill R&B까지.

너무 과하게 신나진 않지만,
듣고 있으면 어느새 계속 재생하게 되는 곡들.

카페에서도, 작업할 때도,
드라이브 중에도 자연스럽게 흐르는
Wavvy의 R&B, NEO-SOUL BEST만 컴필레이션으로 담았습니다. 🌊

What is this song…? ✨
Instantly groovy, instantly Wavvy 😎

A smooth Korean R&B playlist
that naturally flows from sunny afternoons into late-night vibes.

Urban Soul for slow, easy moments under the sunlight,
Neo-Soul perfect for groovy drives,
and Chill R&B that quietly fills the atmosphere.

Not overly energetic,
but the kind of songs that somehow keep playing on repeat.

Perfect for cafés, work sessions, late-night drives,
or anytime you just want good vibes flowing.

A handpicked compilation of Wavvy’s best Korean R&B and Neo-Soul tracks. 🌊

곡 제목 뒤의 시간 표기는 원곡이 수록된 Wavvy 시리즈입니다.
The time label after each title shows the original Wavvy series.

🌊 Track List
──────────────
🌊 00:00 - 01. 작은 빛 (Little Light) · 22:00
🌊 03:37 - 02. 산책 · 14:00
🌊 06:07 - 03. 윤곽 · 04:00
🌊 08:30 - 04. 꽃비 (Petal Rain) · 13:00
🌊 11:10 - 05. 소파 (Sofa) · 22:00
🌊 14:13 - 06. 전화 · 18:00
🌊 17:31 - 07. 먼지 · 14:00
🌊 20:44 - 08. 물안개 · 04:00
🌊 22:53 - 09. 돛 · 14:00
🌊 25:42 - 10. 봄 꽃 (Spring Blossom) · 13:00
🌊 29:02 - 11. 잠실대교 · 21:00
🌊 31:32 - 12. 눈맞춤 (Glance) · 13:00
🌊 34:23 - 13. 무음 (Mute) · 12:00
🌊 37:07 - 14. 꽃길 (Flower Path) · 13:00
🌊 40:30 - 15. 약속 (Appointment) · 18:00
🌊 43:52 - 16. 낮꿈 (Daydream) · 12:00
🌊 47:22 - 17. 물결 · 14:00
🌊 50:12 - 18. 봄비같은 너 (You Like Spring Rain) · 13:00
🌊 53:06 - 19. 밤거리 · 21:00
🌊 56:30 - 20. 잔상 (Afterimage) · 12:00
🌊 59:35 - 21. 피크닉 (Picnic) · 13:00
🌊 1:03:31 - 22. 멍 · 14:00
🌊 1:05:28 - 23. 진동 (Vibration) · 12:00
🌊 1:08:02 - 24. 약속 (Promise) · 13:00
🌊 1:11:22 - 25. 정류장 · 18:00
🌊 1:14:08 - 26. 마음밖 · 04:00
🌊 1:17:35 - 27. 얼룩 (Stain) · 12:00
🌊 1:20:21 - 28. 맞잡은 손 (Holding Hands) · 22:00
🌊 1:23:28 - 29. 마음안 · 04:00
🌊 1:26:24 - 30. 이름 · 18:00
🌊 1:30:14 - 31. 잠옷 · 22:00
🌊 1:33:38 - 32. 골목 · 18:00
🌊 1:36:24 - 33. 자장가 (Lullaby) · 22:00
──────────────
🌊 1:40:21 - 01. 작은 빛 (Little Light) · 22:00 (반복)
🌊 1:43:59 - 02. 산책 · 14:00
🌊 1:46:28 - 03. 윤곽 · 04:00
🌊 1:48:52 - 04. 꽃비 (Petal Rain) · 13:00
🌊 1:51:32 - 05. 소파 (Sofa) · 22:00
🌊 1:54:35 - 06. 전화 · 18:00
🌊 1:57:52 - 07. 먼지 · 14:00
🌊 2:01:06 - 08. 물안개 · 04:00
🌊 2:03:14 - 09. 돛 · 14:00
🌊 2:06:03 - 10. 봄 꽃 (Spring Blossom) · 13:00
🌊 2:09:24 - 11. 잠실대교 · 21:00
🌊 2:11:53 - 12. 눈맞춤 (Glance) · 13:00
🌊 2:14:44 - 13. 무음 (Mute) · 12:00
🌊 2:17:29 - 14. 꽃길 (Flower Path) · 13:00
🌊 2:20:51 - 15. 약속 (Appointment) · 18:00
🌊 2:24:13 - 16. 낮꿈 (Daydream) · 12:00
🌊 2:27:43 - 17. 물결 · 14:00
🌊 2:30:34 - 18. 봄비같은 너 (You Like Spring Rain) · 13:00
🌊 2:33:27 - 19. 밤거리 · 21:00
🌊 2:36:51 - 20. 잔상 (Afterimage) · 12:00
🌊 2:39:57 - 21. 피크닉 (Picnic) · 13:00
🌊 2:43:52 - 22. 멍 · 14:00
🌊 2:45:49 - 23. 진동 (Vibration) · 12:00
🌊 2:48:23 - 24. 약속 (Promise) · 13:00
🌊 2:51:44 - 25. 정류장 · 18:00
🌊 2:54:30 - 26. 마음밖 · 04:00
🌊 2:57:57 - 27. 얼룩 (Stain) · 12:00
🌊 3:00:42 - 28. 맞잡은 손 (Holding Hands) · 22:00
🌊 3:03:50 - 29. 마음안 · 04:00
🌊 3:06:45 - 30. 이름 · 18:00
🌊 3:10:36 - 31. 잠옷 · 22:00
🌊 3:14:00 - 32. 골목 · 18:00
🌊 3:16:45 - 33. 자장가 (Lullaby) · 22:00
──────────────

Music for your space, 24 hours a day.
All tracks feature Korean lyrics.

🎵 Music: Wavvy
Copyright Ⓒ Wavvy. All rights reserved.
──────────────
#RnBBest #RnBPlaylist #KoreanRnB #KoreanRnBPlaylist
#GroovyRnB #ChillRnB #SoftRnB #SlowJam #UrbanSoul
#NeoSoul #SoulMusic #RnBCompilation #NeoSoulCompilation
#카페음악 #매장음악 #작업음악 #드라이브음악 #기분좋은음악
#알앤비 #네오소울 #그루브 #플레이리스트 #음악추천
#Playlist #플리 #한국어가사 #KoreanLyrics
#Wavvy #웨이비
```

### 태그

```text
RnBBest, RnBPlaylist, KoreanRnB, KoreanRnBPlaylist, GroovyRnB, ChillRnB, SoftRnB, SlowJam, UrbanSoul, NeoSoul, SoulMusic, RnBCompilation, NeoSoulCompilation, 카페음악, 매장음악, 작업음악, 드라이브음악, 기분좋은음악, 알앤비, 네오소울, 그루브, 플레이리스트, 음악추천, Playlist, 플리, 한국어가사, KoreanLyrics, Wavvy, 웨이비
```

### 해시태그

```text
#RnBBest #RnBPlaylist #KoreanRnB #KoreanRnBPlaylist
#GroovyRnB #ChillRnB #SoftRnB #SlowJam #UrbanSoul
#NeoSoul #SoulMusic #RnBCompilation #NeoSoulCompilation
#카페음악 #매장음악 #작업음악 #드라이브음악 #기분좋은음악
#알앤비 #네오소울 #그루브 #플레이리스트 #음악추천
#Playlist #플리 #한국어가사 #KoreanLyrics
#Wavvy #웨이비
```

### 고정 댓글

```text
부드럽게 그루브 타기 좋은 Wavvy R&B best playlist입니다.
다음 R&B BEST에 들어갔으면 하는 곡이 있다면 남겨주세요.
```

---

## Track Selection

현재 33곡. 2026-05-07 기준 러닝 오더 재정렬 완료.

| # | Title | Source | Copied Filename |
|---|---|---|---|
| 01 | 작은 빛 | `SERIES/22-00/input/tracks/10__작은 빛__Little Light__Chill R&B__72.wav` | `01__작은 빛__Little Light__Chill R&B__72.wav` |
| 02 | 산책 | `SERIES/14-00/input/tracks/03__산책__Chill__Alt-RnB__74.mp3` | `02__산책__Chill__Alt-RnB__74.mp3` |
| 03 | 윤곽 | `SERIES/04-00/input/tracks/02__윤곽__Ethereal__RnB__76.mp3` | `03__윤곽__Ethereal__RnB__76.mp3` |
| 04 | 꽃비 | `SERIES/13-00/work/norm_tracks/norm_05__꽃비__Petal Rain__Silky R&B__90.wav` | `04__꽃비__Petal Rain__Silky R&B__90.wav` |
| 05 | 소파 | `SERIES/22-00/input/tracks/04__소파__Sofa__Chill R&B__75.wav` | `05__소파__Sofa__Chill R&B__75.wav` |
| 06 | 전화 | `SERIES/18-00/input/tracks/06__전화__Warmth__Soft-RnB__88.mp3` | `06__전화__Warmth__Soft-RnB__88.mp3` |
| 07 | 먼지 | `SERIES/14-00/input/tracks/09__먼지__Warm__Soft-RnB__72.mp3` | `07__먼지__Warm__Soft-RnB__72.mp3` |
| 08 | 물안개 | `SERIES/04-00/input/tracks/04__물안개__Hazy__Lo-fi-RnB__80.mp3` | `08__물안개__Hazy__Lo-fi-RnB__80.mp3` |
| 09 | 돛 | `SERIES/14-00/input/tracks/05__돛__Groovy__RnB__90.mp3` | `09__돛__Groovy__RnB__90.mp3` |
| 10 | 봄 꽃 | `SERIES/13-00/work/norm_tracks/norm_07__봄 꽃__Spring Blossom__Urban Soul__100.wav` | `10__봄 꽃__Spring Blossom__Urban Soul__100.wav` |
| 11 | 잠실대교 | `SERIES/21-00/input/tracks/06__잠실대교__취기__NeoSoul__92.wav` | `11__잠실대교__취기__NeoSoul__92.wav` |
| 12 | 눈맞춤 | `SERIES/13-00/work/norm_tracks/norm_06__눈맞춤__Glance__Silky R&B__108.wav` | `12__눈맞춤__Glance__Silky R&B__108.wav` |
| 13 | 무음 | `SERIES/12-00/input/tracks/04__무음__Mute__Afropiano__110.wav` | `13__무음__Mute__Afropiano__110.wav` |
| 14 | 꽃길 | `SERIES/13-00/work/norm_tracks/norm_04__꽃길__Flower Path__Silky R&B__100.wav` | `14__꽃길__Flower Path__Silky R&B__100.wav` |
| 15 | 약속 | `SERIES/18-00/input/tracks/02__약속__Loneliness__Neo-soul__100.mp3` | `15__약속__Appointment__Neo-soul__100.mp3` |
| 16 | 낮꿈 | `SERIES/12-00/input/tracks/07__낮꿈__Daydream__Afro-Drill__102.wav` | `16__낮꿈__Daydream__Afro-Drill__102.wav` |
| 17 | 물결 | `SERIES/14-00/input/tracks/06__물결__Chill__Alt-RnB__74.mp3` | `17__물결__Chill__Alt-RnB__74.mp3` |
| 18 | 봄비같은 너 | `SERIES/13-00/work/norm_tracks/norm_16__봄비같은 너__You Like Spring Rain__Neo-Soul Funk__104.wav` | `18__봄비같은 너__You Like Spring Rain__Neo-Soul Funk__104.wav` |
| 19 | 밤거리 | `SERIES/21-00/input/tracks/03__밤거리__관조__CityPop-Ballad__90.wav` | `19__밤거리__관조__CityPop-Ballad__90.wav` |
| 20 | 잔상 | `SERIES/12-00/input/tracks/10__잔상__Afterimage__Afro-Drill__108.wav` | `20__잔상__Afterimage__Afro-Drill__108.wav` |
| 21 | 피크닉 | `SERIES/13-00/work/norm_tracks/norm_13__피크닉__Picnic__Neo-Soul Funk__102.wav` | `21__피크닉__Picnic__Neo-Soul Funk__102.wav` |
| 22 | 멍 | `SERIES/14-00/input/tracks/01__멍__Chill__Alt-RnB__74.mp3` | `22__멍__Chill__Alt-RnB__74.mp3` |
| 23 | 진동 | `SERIES/12-00/input/tracks/17__진동__Vibration__Afro-Drill__109.wav` | `23__진동__Vibration__Afro-Drill__109.wav` |
| 24 | 약속 | `SERIES/13-00/work/norm_tracks/norm_12__약속__Promise__Neo-Soul__100.wav` | `24__약속__Promise__Neo-Soul__100.wav` |
| 25 | 정류장 | `SERIES/18-00/input/tracks/03__정류장__Loneliness__Neo-soul__100.mp3` | `25__정류장__Loneliness__Neo-soul__100.mp3` |
| 26 | 마음밖 | `SERIES/04-00/input/tracks/01__마음밖__Sentimental__RnB-Ballad__90.mp3` | `26__마음밖__Sentimental__RnB-Ballad__90.mp3` |
| 27 | 얼룩 | `SERIES/12-00/input/tracks/18__얼룩__Stain__Afro-Drill__102.wav` | `27__얼룩__Stain__Afro-Drill__102.wav` |
| 28 | 맞잡은 손 | `SERIES/22-00/input/tracks/18__맞잡은 손__Holding Hands__Chill R&B__72.wav` | `28__맞잡은 손__Holding Hands__Chill R&B__72.wav` |
| 29 | 마음안 | `SERIES/04-00/input/tracks/09__마음안__Sentimental__RnB-Ballad__95.mp3` | `29__마음안__Sentimental__RnB-Ballad__95.mp3` |
| 30 | 이름 | `SERIES/18-00/input/tracks/09__이름__Homecoming__Soft-RnB__72.mp3` | `30__이름__Homecoming__Soft-RnB__72.mp3` |
| 31 | 잠옷 | `SERIES/22-00/input/tracks/02__잠옷__Comfort__Ambient Slow Jam__76.wav` | `31__잠옷__Comfort__Ambient Slow Jam__76.wav` |
| 32 | 골목 | `SERIES/18-00/input/tracks/07__골목__Contemplation__Slow-RnB__67.mp3` | `32__골목__Contemplation__Slow-RnB__67.mp3` |
| 33 | 자장가 | `SERIES/22-00/input/tracks/19__자장가__Lullaby__Chill R&B__61.wav` | `33__자장가__Lullaby__Chill R&B__61.wav` |

### 후보 / 보류

현재 없음.

```text
선곡 입력 형식 예시:
창문 내려
작은 빛
잔향

시리즈/번호까지 알고 있을 때:
15-00 06 창문 내려
22-00 10 작은 빛
04-00 03 잔향
```

---

## Next Steps

1. 사용자 선곡 리스트 수령
2. 로컬 오디오 존재 여부 확인
3. `input/tracks/`에 사용자 순서대로 링크 또는 복사
4. `python3 wavvy.py validate SERIES/RNB-BEST`
5. 필요 시 사용자 요청에 따라 러닝 오더만 조정
6. `python3 wavvy.py pack SERIES/RNB-BEST -y`
