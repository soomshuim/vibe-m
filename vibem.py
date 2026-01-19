#!/usr/bin/env python3
"""
vibem - YouTube Music Playlist Generation CLI

A robust CLI tool for automating YouTube music playlist generation
using pure FFmpeg for all media operations.

Author: vibem
License: MIT
"""

import click
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional

import ffmpeg
import pandas as pd


# =============================================================================
# CONSTANTS
# =============================================================================

TRACK_PATTERN = re.compile(
    r'^(?P<order>\d{2})__(?P<title>[^_]+)__(?P<mood>[^_]+)__(?P<genre>[^_]+)__(?P<bpm>\d+)\.mp3$'
)

DEFAULT_CROSSFADE_SEC = 0.8
DEFAULT_LUFS = -14
DEFAULT_TRUE_PEAK = -1.0
DEFAULT_PREVIEW_SEC = 30

VIDEO_CODEC = 'libx264'
AUDIO_CODEC = 'aac'
AUDIO_BITRATE = '320k'
VIDEO_CRF = 18
VIDEO_PRESET = 'medium'


# =============================================================================
# DATA CLASSES
# =============================================================================

@dataclass
class TrackInfo:
    """Parsed track information from filename."""
    path: Path
    order: int
    title: str
    mood: str
    genre: str
    bpm: int
    duration: float = 0.0
    sample_rate: int = 0
    sha256: str = ""

    @classmethod
    def from_filename(cls, path: Path) -> Optional['TrackInfo']:
        """Parse track info from filename. Returns None if invalid."""
        match = TRACK_PATTERN.match(path.name)
        if not match:
            return None
        return cls(
            path=path,
            order=int(match.group('order')),
            title=match.group('title'),
            mood=match.group('mood'),
            genre=match.group('genre'),
            bpm=int(match.group('bpm')),
        )


@dataclass
class ValidationResult:
    """Result of validation checks."""
    is_valid: bool = True
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    tracks: list = field(default_factory=list)

    def add_error(self, msg: str):
        self.errors.append(msg)
        self.is_valid = False

    def add_warning(self, msg: str):
        self.warnings.append(msg)


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def log_info(msg: str):
    """Print info message."""
    click.echo(click.style(f"[INFO] {msg}", fg='blue'))


def log_success(msg: str):
    """Print success message."""
    click.echo(click.style(f"[OK] {msg}", fg='green'))


def log_warning(msg: str):
    """Print warning message."""
    click.echo(click.style(f"[WARN] {msg}", fg='yellow'))


def log_error(msg: str):
    """Print error message."""
    click.echo(click.style(f"[ERROR] {msg}", fg='red'), err=True)


def ensure_dir(path: Path) -> Path:
    """Ensure directory exists."""
    path.mkdir(parents=True, exist_ok=True)
    return path


def compute_sha256(filepath: Path) -> str:
    """Compute SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()


def get_audio_info(filepath: Path) -> dict:
    """Get audio file info using ffprobe."""
    try:
        probe = ffmpeg.probe(str(filepath))
        audio_stream = next(
            (s for s in probe['streams'] if s['codec_type'] == 'audio'),
            None
        )
        if not audio_stream:
            return {'error': 'No audio stream found'}

        duration = float(probe['format'].get('duration', 0))
        sample_rate = int(audio_stream.get('sample_rate', 0))

        return {
            'duration': duration,
            'sample_rate': sample_rate,
            'codec': audio_stream.get('codec_name', 'unknown'),
            'channels': audio_stream.get('channels', 0),
            'bit_rate': probe['format'].get('bit_rate', 'unknown'),
        }
    except ffmpeg.Error as e:
        return {'error': f'ffprobe failed: {e.stderr.decode() if e.stderr else str(e)}'}
    except Exception as e:
        return {'error': str(e)}


def get_video_info(filepath: Path) -> dict:
    """Get video file info using ffprobe."""
    try:
        probe = ffmpeg.probe(str(filepath))
        video_stream = next(
            (s for s in probe['streams'] if s['codec_type'] == 'video'),
            None
        )
        if not video_stream:
            return {'error': 'No video stream found'}

        duration = float(probe['format'].get('duration', 0))

        return {
            'duration': duration,
            'width': video_stream.get('width', 0),
            'height': video_stream.get('height', 0),
            'codec': video_stream.get('codec_name', 'unknown'),
        }
    except ffmpeg.Error as e:
        return {'error': f'ffprobe failed: {e.stderr.decode() if e.stderr else str(e)}'}
    except Exception as e:
        return {'error': str(e)}


# =============================================================================
# PATH RESOLVER
# =============================================================================

class ProjectPaths:
    """Resolve and manage project paths."""

    def __init__(self, base_path: Path):
        self.base = base_path
        self.input_dir = base_path / 'input'
        self.tracks_dir = self.input_dir / 'tracks'
        self.work_dir = base_path / 'work'
        self.output_dir = base_path / 'output'
        self.norm_tracks_dir = self.work_dir / 'norm_tracks'

        # Input files
        self.loop_video = self.input_dir / 'loop.mp4'
        self.thumbnail = self.input_dir / 'thumb.jpg'

        # Work files
        self.merged_wav = self.work_dir / 'merged.wav'

        # Output files
        self.preview_mp4 = self.output_dir / 'preview.mp4'
        self.final_mp4 = self.output_dir / 'final.mp4'
        self.provenance_md = self.output_dir / 'provenance.md'
        self.description_txt = self.output_dir / 'description.txt'
        self.upload_csv = self.output_dir / 'upload.csv'
        self.report_json = self.output_dir / 'report.json'

    def ensure_work_dirs(self):
        """Create work and output directories."""
        ensure_dir(self.work_dir)
        ensure_dir(self.norm_tracks_dir)
        ensure_dir(self.output_dir)

    def clean_work_dir(self):
        """Clean work directory."""
        if self.work_dir.exists():
            shutil.rmtree(self.work_dir)
        ensure_dir(self.work_dir)
        ensure_dir(self.norm_tracks_dir)


# =============================================================================
# VALIDATION
# =============================================================================

def validate_project(paths: ProjectPaths) -> ValidationResult:
    """
    Validate project structure and files.

    Checks:
    1. tracks/ contains at least one MP3
    2. Filename format matches spec (NN__Title__Mood__Genre__BPM.mp3)
    3. loop.mp4 and thumb.jpg exist
    4. Audio integrity via ffprobe
    5. Sample rate consistency
    """
    result = ValidationResult()

    # Check base directory exists
    if not paths.base.exists():
        result.add_error(f"Project directory does not exist: {paths.base}")
        return result

    # Check input directory structure
    if not paths.input_dir.exists():
        result.add_error(f"Input directory does not exist: {paths.input_dir}")
        return result

    if not paths.tracks_dir.exists():
        result.add_error(f"Tracks directory does not exist: {paths.tracks_dir}")
        return result

    # Find MP3 files
    mp3_files = sorted(paths.tracks_dir.glob('*.mp3'))
    if not mp3_files:
        result.add_error(f"No MP3 files found in: {paths.tracks_dir}")
        return result

    log_info(f"Found {len(mp3_files)} MP3 file(s)")

    # Validate filename format and parse tracks
    tracks = []
    sample_rates = set()

    for mp3_path in mp3_files:
        track = TrackInfo.from_filename(mp3_path)
        if track is None:
            result.add_error(
                f"Invalid filename format: {mp3_path.name}\n"
                f"  Expected: NN__Title__Mood__Genre__BPM.mp3"
            )
            continue

        # Check audio integrity
        audio_info = get_audio_info(mp3_path)
        if 'error' in audio_info:
            result.add_error(f"Audio integrity check failed for {mp3_path.name}: {audio_info['error']}")
            continue

        if audio_info['duration'] <= 0:
            result.add_error(f"Invalid duration (<=0) for {mp3_path.name}")
            continue

        track.duration = audio_info['duration']
        track.sample_rate = audio_info['sample_rate']
        track.sha256 = compute_sha256(mp3_path)

        sample_rates.add(track.sample_rate)
        tracks.append(track)

        log_success(f"  {track.order:02d}. {track.title} ({track.duration:.1f}s, {track.sample_rate}Hz)")

    # Check sample rate consistency
    if len(sample_rates) > 1:
        result.add_warning(
            f"Inconsistent sample rates detected: {sorted(sample_rates)}\n"
            f"  This may cause issues during merging."
        )

    # Check required media files
    if not paths.loop_video.exists():
        result.add_error(f"Missing loop video: {paths.loop_video}")
    else:
        video_info = get_video_info(paths.loop_video)
        if 'error' in video_info:
            result.add_error(f"Loop video integrity check failed: {video_info['error']}")
        else:
            log_success(f"Loop video: {video_info['width']}x{video_info['height']}, {video_info['duration']:.1f}s")

    if not paths.thumbnail.exists():
        result.add_error(f"Missing thumbnail: {paths.thumbnail}")
    else:
        log_success(f"Thumbnail found: {paths.thumbnail.name}")

    # Sort tracks by order
    result.tracks = sorted(tracks, key=lambda t: t.order)

    # Check for duplicate order numbers
    orders = [t.order for t in result.tracks]
    if len(orders) != len(set(orders)):
        result.add_error("Duplicate track order numbers detected")

    return result


# =============================================================================
# FFMPEG FILTER GRAPH CONSTRUCTION
# =============================================================================

def build_sequential_acrossfade_filter(
    num_tracks: int,
    crossfade_sec: float = DEFAULT_CROSSFADE_SEC,
    curve: str = 'tri'
) -> tuple[str, str]:
    """
    Build a sequential acrossfade filter graph.

    For N tracks, creates:
    [0][1]acrossfade=d=0.8:c1=tri:c2=tri[a01];
    [a01][2]acrossfade=d=0.8:c1=tri:c2=tri[a02];
    ...
    [aN-2][N-1]acrossfade=d=0.8:c1=tri:c2=tri[aFINAL]

    Returns:
        tuple: (filter_complex string, final output label)
    """
    if num_tracks < 2:
        raise ValueError("Need at least 2 tracks to build crossfade filter")

    filters = []

    # First crossfade: [0][1]acrossfade[a01]
    filters.append(
        f"[0][1]acrossfade=d={crossfade_sec}:c1={curve}:c2={curve}[a01]"
    )

    # Subsequent crossfades: [a01][2] -> [a02], [a02][3] -> [a03], ...
    for i in range(2, num_tracks):
        prev_label = f"a{str(i-1).zfill(2)}"  # a01, a02, a03, ...
        curr_label = f"a{str(i).zfill(2)}"    # a02, a03, a04, ...
        filters.append(
            f"[{prev_label}][{i}]acrossfade=d={crossfade_sec}:c1={curve}:c2={curve}[{curr_label}]"
        )

    final_label = f"a{str(num_tracks-1).zfill(2)}"
    filter_complex = ";".join(filters)

    return filter_complex, final_label


def calculate_merged_duration(tracks: list[TrackInfo], crossfade_sec: float) -> float:
    """Calculate expected duration after crossfade merge."""
    if not tracks:
        return 0.0
    if len(tracks) == 1:
        return tracks[0].duration

    total = sum(t.duration for t in tracks)
    # Each crossfade removes crossfade_sec from total
    overlap_reduction = crossfade_sec * (len(tracks) - 1)
    return total - overlap_reduction


# =============================================================================
# FFMPEG OPERATIONS
# =============================================================================

def merge_tracks_with_crossfade(
    tracks: list[TrackInfo],
    output_path: Path,
    crossfade_sec: float = DEFAULT_CROSSFADE_SEC,
    sample_rate: int = 44100
) -> bool:
    """
    Merge multiple audio tracks using sequential acrossfade filter.

    Uses subprocess for maximum control over the FFmpeg command.
    """
    if len(tracks) < 2:
        if len(tracks) == 1:
            # Single track: just copy
            shutil.copy(tracks[0].path, output_path)
            return True
        return False

    # Build the filter complex
    filter_complex, final_label = build_sequential_acrossfade_filter(
        len(tracks), crossfade_sec
    )

    # Build FFmpeg command
    cmd = ['ffmpeg', '-y']

    # Add all input files
    for track in tracks:
        cmd.extend(['-i', str(track.path)])

    # Add filter complex
    cmd.extend([
        '-filter_complex', filter_complex,
        '-map', f'[{final_label}]',
        '-ar', str(sample_rate),
        '-ac', '2',
        str(output_path)
    ])

    log_info(f"Merging {len(tracks)} tracks with {crossfade_sec}s crossfade...")
    log_info(f"Filter graph: {filter_complex[:100]}..." if len(filter_complex) > 100 else f"Filter graph: {filter_complex}")

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        log_success(f"Merged audio saved to: {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        log_error(f"FFmpeg merge failed: {e.stderr}")
        return False


def trim_audio(input_path: Path, output_path: Path, duration_sec: float) -> bool:
    """Trim audio to specified duration."""
    try:
        (
            ffmpeg
            .input(str(input_path))
            .output(str(output_path), t=duration_sec, acodec='copy')
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
        return True
    except ffmpeg.Error as e:
        log_error(f"Trim failed: {e.stderr.decode() if e.stderr else str(e)}")
        return False


def normalize_track(
    input_path: Path,
    output_path: Path,
    target_lufs: float = DEFAULT_LUFS,
    true_peak: float = DEFAULT_TRUE_PEAK
) -> bool:
    """
    Normalize a single track using ffmpeg-normalize.
    Uses python -m to ensure module is found regardless of PATH.
    """
    cmd = [
        sys.executable, '-m', 'ffmpeg_normalize',
        str(input_path),
        '-o', str(output_path),
        '-t', str(target_lufs),
        '-tp', str(true_peak),
        '-ar', '44100',
        '-f',  # Force overwrite
        '-pr'  # Progress bar
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        return True
    except subprocess.CalledProcessError as e:
        log_error(f"Normalization failed for {input_path.name}: {e.stderr}")
        return False
    except FileNotFoundError:
        log_error("ffmpeg-normalize not found. Install with: pip install ffmpeg-normalize")
        return False


def render_video(
    audio_path: Path,
    loop_video_path: Path,
    thumbnail_path: Path,
    output_path: Path,
    use_shortest: bool = True
) -> bool:
    """
    Render final video with looped background and audio.

    Uses -stream_loop -1 for infinite video loop and -shortest to stop at audio end.
    """
    # Get audio duration for logging
    audio_info = get_audio_info(audio_path)
    audio_duration = audio_info.get('duration', 0)
    log_info(f"Rendering video with audio duration: {audio_duration:.1f}s")

    # Build FFmpeg command with proper loop handling
    cmd = [
        'ffmpeg', '-y',
        '-stream_loop', '-1',  # Loop video infinitely
        '-i', str(loop_video_path),
        '-i', str(audio_path),
        '-i', str(thumbnail_path),  # Thumbnail as attachment
        '-map', '0:v',
        '-map', '1:a',
        '-c:v', VIDEO_CODEC,
        '-preset', VIDEO_PRESET,
        '-crf', str(VIDEO_CRF),
        '-c:a', AUDIO_CODEC,
        '-b:a', AUDIO_BITRATE,
        '-pix_fmt', 'yuv420p',
        '-movflags', '+faststart',
    ]

    if use_shortest:
        cmd.append('-shortest')

    cmd.append(str(output_path))

    try:
        log_info("Running FFmpeg render...")
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        log_success(f"Video rendered to: {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        log_error(f"Video render failed: {e.stderr}")
        return False


# =============================================================================
# ARTIFACT GENERATION
# =============================================================================

def generate_provenance(
    tracks: list[TrackInfo],
    output_path: Path,
    params: dict
) -> bool:
    """Generate provenance.md with processing details."""
    timestamp = datetime.now().isoformat()

    content = [
        "# Provenance Report",
        "",
        f"Generated: {timestamp}",
        "",
        "## Processing Parameters",
        "",
        f"- Target LUFS: {params.get('lufs', DEFAULT_LUFS)}",
        f"- True Peak: {params.get('tp', DEFAULT_TRUE_PEAK)} dBTP",
        f"- Crossfade: {params.get('fade', DEFAULT_CROSSFADE_SEC)}s",
        "",
        "## Track Details",
        "",
        "| # | Filename | SHA-256 | Duration | Sample Rate |",
        "|---|----------|---------|----------|-------------|",
    ]

    for track in tracks:
        content.append(
            f"| {track.order:02d} | {track.path.name} | `{track.sha256[:16]}...` | "
            f"{track.duration:.1f}s | {track.sample_rate}Hz |"
        )

    content.extend([
        "",
        "## SHA-256 Full Hashes",
        "",
    ])

    for track in tracks:
        content.append(f"- `{track.path.name}`: `{track.sha256}`")

    try:
        output_path.write_text("\n".join(content), encoding='utf-8')
        log_success(f"Provenance saved to: {output_path}")
        return True
    except Exception as e:
        log_error(f"Failed to write provenance: {e}")
        return False


def generate_description(
    tracks: list[TrackInfo],
    output_path: Path,
    crossfade_sec: float
) -> bool:
    """Generate description.txt with timestamps and hashtags."""
    lines = []
    current_time = 0.0

    # Collect all unique hashtags
    all_moods = set()
    all_genres = set()

    for track in tracks:
        # Format timestamp as MM:SS
        minutes = int(current_time // 60)
        seconds = int(current_time % 60)
        timestamp = f"{minutes:02d}:{seconds:02d}"

        lines.append(f"{timestamp} {track.order:02d}. {track.title}")

        all_moods.add(track.mood)
        all_genres.add(track.genre)

        # Next track starts after this duration minus crossfade overlap
        if track != tracks[-1]:
            current_time += track.duration - crossfade_sec
        else:
            current_time += track.duration

    # Add hashtags
    lines.extend([
        "",
        "---",
        "",
        "Hashtags:",
    ])

    hashtags = []
    for mood in sorted(all_moods):
        hashtags.append(f"#{mood.replace(' ', '')}")
    for genre in sorted(all_genres):
        hashtags.append(f"#{genre.replace(' ', '')}")

    lines.append(" ".join(hashtags))

    try:
        output_path.write_text("\n".join(lines), encoding='utf-8')
        log_success(f"Description saved to: {output_path}")
        return True
    except Exception as e:
        log_error(f"Failed to write description: {e}")
        return False


def generate_upload_csv(
    paths: ProjectPaths,
    tracks: list[TrackInfo],
    output_path: Path
) -> bool:
    """Generate upload.csv for batch uploading."""
    # Generate title from first few tracks or folder name
    series_name = paths.base.parent.name if paths.base.parent != paths.base else "Playlist"
    date_str = paths.base.name
    title = f"{series_name} - {date_str}"

    # Collect tags
    tags = set()
    for track in tracks:
        tags.add(track.mood)
        tags.add(track.genre)

    row = {
        'video_path': str(paths.final_mp4),
        'title': title,
        'description': str(paths.description_txt),
        'tags': ','.join(sorted(tags)),
        'thumbnail_path': str(paths.thumbnail),
        'visibility': 'private'  # Default to private for safety
    }

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=row.keys())
            writer.writeheader()
            writer.writerow(row)
        log_success(f"Upload CSV saved to: {output_path}")
        return True
    except Exception as e:
        log_error(f"Failed to write upload CSV: {e}")
        return False


def generate_report(
    tracks: list[TrackInfo],
    output_path: Path,
    final_duration: float,
    params: dict
) -> bool:
    """Generate report.json with technical statistics."""
    report = {
        'generated_at': datetime.now().isoformat(),
        'processing_params': params,
        'summary': {
            'total_tracks': len(tracks),
            'total_original_duration': sum(t.duration for t in tracks),
            'final_duration': final_duration,
            'crossfade_reduction': sum(t.duration for t in tracks) - final_duration,
        },
        'tracks': [
            {
                'order': t.order,
                'title': t.title,
                'mood': t.mood,
                'genre': t.genre,
                'bpm': t.bpm,
                'duration': t.duration,
                'sample_rate': t.sample_rate,
                'sha256': t.sha256,
                'filename': t.path.name,
            }
            for t in tracks
        ]
    }

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        log_success(f"Report saved to: {output_path}")
        return True
    except Exception as e:
        log_error(f"Failed to write report: {e}")
        return False


# =============================================================================
# CLI COMMANDS
# =============================================================================

@click.group()
@click.version_option(version='1.0.0', prog_name='vibem')
def cli():
    """
    vibem - YouTube Music Playlist Generation CLI

    Automate the creation of YouTube music playlist videos with
    professional audio processing and crossfade transitions.
    """
    pass


@cli.command()
@click.argument('path', type=click.Path(exists=True, file_okay=False, path_type=Path))
def validate(path: Path):
    """
    Validate project structure and files.

    Performs health checks before processing:
    - Verifies tracks exist with valid filenames
    - Checks audio integrity via ffprobe
    - Validates required media files (loop.mp4, thumb.jpg)
    - Reports sample rate consistency
    """
    click.echo(click.style("\n=== VIBEM VALIDATION ===\n", fg='cyan', bold=True))

    paths = ProjectPaths(path)
    result = validate_project(paths)

    # Print summary
    click.echo("")

    if result.warnings:
        click.echo(click.style("Warnings:", fg='yellow', bold=True))
        for warning in result.warnings:
            log_warning(warning)
        click.echo("")

    if result.errors:
        click.echo(click.style("Errors:", fg='red', bold=True))
        for error in result.errors:
            log_error(error)
        click.echo("")
        click.echo(click.style("VALIDATION FAILED", fg='red', bold=True))
        sys.exit(1)

    # Success summary
    total_duration = sum(t.duration for t in result.tracks)
    click.echo(click.style("Summary:", fg='green', bold=True))
    click.echo(f"  Tracks: {len(result.tracks)}")
    click.echo(f"  Total Duration: {total_duration:.1f}s ({total_duration/60:.1f} min)")
    click.echo("")
    click.echo(click.style("VALIDATION PASSED", fg='green', bold=True))


@cli.command()
@click.argument('path', type=click.Path(exists=True, file_okay=False, path_type=Path))
@click.option('--sec', default=DEFAULT_PREVIEW_SEC, help='Preview duration in seconds')
@click.option('--fade', default=DEFAULT_CROSSFADE_SEC, help='Crossfade duration in seconds')
def preview(path: Path, sec: int, fade: float):
    """
    Generate a quick preview video.

    Creates a fast preview by:
    - Taking first N seconds from EACH track (sec / num_tracks)
    - Merging trimmed tracks with crossfade (no normalization)
    - Rendering with loop video

    This ensures all tracks are represented in the preview.

    Output: output/preview.mp4
    """
    click.echo(click.style("\n=== VIBEM PREVIEW ===\n", fg='cyan', bold=True))

    paths = ProjectPaths(path)

    # Validate first
    log_info("Running validation...")
    result = validate_project(paths)

    if not result.is_valid:
        for error in result.errors:
            log_error(error)
        click.echo(click.style("\nVALIDATION FAILED - Cannot generate preview", fg='red', bold=True))
        sys.exit(1)

    if not result.tracks:
        log_error("No valid tracks found")
        sys.exit(1)

    # Ensure output directories
    paths.ensure_work_dirs()

    num_tracks = len(result.tracks)

    if num_tracks == 1:
        # Single track: trim and use directly
        log_info("Single track detected...")
        trimmed_path = paths.work_dir / 'preview_trimmed.wav'
        trim_duration = min(sec, result.tracks[0].duration)

        if not trim_audio(result.tracks[0].path, trimmed_path, trim_duration):
            log_error("Failed to trim audio")
            sys.exit(1)
    else:
        # Multiple tracks: trim each track first, then merge
        # Calculate duration per track (accounting for crossfade overlap)
        # Crossfade overlaps: (num_tracks - 1) * fade seconds are shared
        # So we need: sec + (num_tracks - 1) * fade total track time
        total_track_time = sec + (num_tracks - 1) * fade
        sec_per_track = total_track_time / num_tracks

        log_info(f"Trimming each track to {sec_per_track:.1f}s for {sec}s preview...")

        # Trim each track
        trimmed_tracks = []
        for i, track in enumerate(result.tracks):
            trimmed_path_i = paths.work_dir / f'preview_track_{i:02d}.wav'
            trim_duration = min(sec_per_track, track.duration)

            log_info(f"  Trimming {track.title} to {trim_duration:.1f}s...")
            if not trim_audio(track.path, trimmed_path_i, trim_duration):
                log_error(f"Failed to trim track {track.title}")
                sys.exit(1)

            # Create a temporary TrackInfo with the trimmed path
            trimmed_track = TrackInfo(
                path=trimmed_path_i,
                order=track.order,
                title=track.title,
                mood=track.mood,
                genre=track.genre,
                bpm=track.bpm,
                duration=trim_duration,
                sample_rate=track.sample_rate
            )
            trimmed_tracks.append(trimmed_track)

        # Merge trimmed tracks with crossfade
        merged_path = paths.work_dir / 'preview_merged.wav'
        log_info(f"Merging {num_tracks} trimmed tracks with {fade}s crossfade...")

        if not merge_tracks_with_crossfade(trimmed_tracks, merged_path, fade):
            log_error("Failed to merge tracks")
            sys.exit(1)

        trimmed_path = merged_path

    # Render video
    # Get actual duration of the audio
    audio_info = get_audio_info(trimmed_path)
    audio_duration = audio_info.get('duration', 0)
    log_info(f"Rendering video with audio duration: {audio_duration:.1f}s")

    if not render_video(
        trimmed_path,
        paths.loop_video,
        paths.thumbnail,
        paths.preview_mp4,
        use_shortest=True
    ):
        log_error("Failed to render video")
        sys.exit(1)

    # Summary
    click.echo("")
    click.echo(click.style("PREVIEW COMPLETE", fg='green', bold=True))
    click.echo(f"Output: {paths.preview_mp4}")
    if num_tracks > 1:
        click.echo(f"Duration: {audio_duration:.1f}s ({num_tracks} tracks × ~{sec_per_track:.1f}s each)")


@cli.command()
@click.argument('path', type=click.Path(exists=True, file_okay=False, path_type=Path))
@click.option('--lufs', default=DEFAULT_LUFS, help='Target loudness in LUFS')
@click.option('--tp', default=DEFAULT_TRUE_PEAK, help='True peak in dBTP')
@click.option('--fade', default=DEFAULT_CROSSFADE_SEC, help='Crossfade duration in seconds')
@click.option('--skip-normalize', is_flag=True, help='Skip normalization step')
def pack(path: Path, lufs: float, tp: float, fade: float, skip_normalize: bool):
    """
    Create final deliverables for YouTube.

    Full production workflow:
    1. Validate project structure
    2. Normalize each track (ffmpeg-normalize)
    3. Merge with sequential crossfade
    4. Render final video
    5. Generate artifacts (provenance, description, upload CSV, report)

    Output: output/final.mp4 + artifacts
    """
    click.echo(click.style("\n=== VIBEM PACK ===\n", fg='cyan', bold=True))

    paths = ProjectPaths(path)
    params = {'lufs': lufs, 'tp': tp, 'fade': fade}

    # Step 1: Validate
    log_info("Step 1/5: Validation...")
    result = validate_project(paths)

    if not result.is_valid:
        for error in result.errors:
            log_error(error)
        click.echo(click.style("\nVALIDATION FAILED - Cannot proceed", fg='red', bold=True))
        sys.exit(1)

    if not result.tracks:
        log_error("No valid tracks found")
        sys.exit(1)

    for warning in result.warnings:
        log_warning(warning)

    log_success(f"Validation passed: {len(result.tracks)} tracks")

    # Ensure directories
    paths.ensure_work_dirs()

    # Step 2: Normalize
    log_info(f"Step 2/5: Normalizing tracks (Target: {lufs} LUFS, TP: {tp} dBTP)...")

    normalized_tracks = []

    if skip_normalize:
        log_warning("Skipping normalization (--skip-normalize)")
        normalized_tracks = result.tracks
    else:
        for i, track in enumerate(result.tracks, 1):
            norm_path = paths.norm_tracks_dir / f"norm_{track.path.stem}.wav"
            log_info(f"  [{i}/{len(result.tracks)}] Normalizing {track.path.name}...")

            if not normalize_track(track.path, norm_path, lufs, tp):
                log_error(f"Failed to normalize {track.path.name}")
                sys.exit(1)

            # Create new track info with normalized path
            norm_track = TrackInfo(
                path=norm_path,
                order=track.order,
                title=track.title,
                mood=track.mood,
                genre=track.genre,
                bpm=track.bpm,
                duration=track.duration,
                sample_rate=track.sample_rate,
                sha256=track.sha256,  # Keep original hash for provenance
            )
            normalized_tracks.append(norm_track)

        log_success("Normalization complete")

    # Step 3: Merge with crossfade
    log_info(f"Step 3/5: Merging tracks with {fade}s crossfade...")

    if len(normalized_tracks) == 1:
        log_info("Single track detected, converting to WAV...")
        (
            ffmpeg
            .input(str(normalized_tracks[0].path))
            .output(str(paths.merged_wav), ar=44100, ac=2)
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
    else:
        if not merge_tracks_with_crossfade(normalized_tracks, paths.merged_wav, fade):
            log_error("Failed to merge tracks")
            sys.exit(1)

    log_success("Merge complete")

    # Step 4: Render video
    log_info("Step 4/5: Rendering final video...")

    if not render_video(
        paths.merged_wav,
        paths.loop_video,
        paths.thumbnail,
        paths.final_mp4,
        use_shortest=True
    ):
        log_error("Failed to render video")
        sys.exit(1)

    log_success("Video render complete")

    # Step 5: Generate artifacts
    log_info("Step 5/5: Generating artifacts...")

    # Get final duration
    final_info = get_audio_info(paths.merged_wav)
    final_duration = final_info.get('duration', 0)

    # Use original tracks for provenance (contains original hashes)
    generate_provenance(result.tracks, paths.provenance_md, params)
    generate_description(result.tracks, paths.description_txt, fade)
    generate_upload_csv(paths, result.tracks, paths.upload_csv)
    generate_report(result.tracks, paths.report_json, final_duration, params)

    # Final summary
    click.echo("")
    click.echo(click.style("=" * 50, fg='green'))
    click.echo(click.style("PACK COMPLETE", fg='green', bold=True))
    click.echo(click.style("=" * 50, fg='green'))
    click.echo("")
    click.echo("Deliverables:")
    click.echo(f"  Video:       {paths.final_mp4}")
    click.echo(f"  Provenance:  {paths.provenance_md}")
    click.echo(f"  Description: {paths.description_txt}")
    click.echo(f"  Upload CSV:  {paths.upload_csv}")
    click.echo(f"  Report:      {paths.report_json}")
    click.echo("")
    click.echo(f"Total tracks:   {len(result.tracks)}")
    click.echo(f"Final duration: {final_duration:.1f}s ({final_duration/60:.1f} min)")


@cli.command()
@click.argument('path', type=click.Path(exists=True, file_okay=False, path_type=Path))
def init(path: Path):
    """
    Initialize project directory structure.

    Creates the required folder structure:
    - input/tracks/
    - input/ (for loop.mp4 and thumb.jpg)
    - work/
    - output/
    """
    click.echo(click.style("\n=== VIBEM INIT ===\n", fg='cyan', bold=True))

    paths = ProjectPaths(path)

    # Create directories
    ensure_dir(paths.input_dir)
    ensure_dir(paths.tracks_dir)
    ensure_dir(paths.work_dir)
    ensure_dir(paths.output_dir)

    log_success(f"Created: {paths.input_dir}")
    log_success(f"Created: {paths.tracks_dir}")
    log_success(f"Created: {paths.work_dir}")
    log_success(f"Created: {paths.output_dir}")

    click.echo("")
    click.echo("Next steps:")
    click.echo(f"  1. Add MP3 files to: {paths.tracks_dir}")
    click.echo(f"     Format: NN__Title__Mood__Genre__BPM.mp3")
    click.echo(f"  2. Add loop.mp4 to: {paths.input_dir}")
    click.echo(f"  3. Add thumb.jpg to: {paths.input_dir}")
    click.echo(f"  4. Run: vibem validate {path}")


@cli.command()
@click.argument('path', type=click.Path(exists=True, file_okay=False, path_type=Path))
def clean(path: Path):
    """
    Clean work and output directories.

    Removes all generated files while preserving input files.
    """
    click.echo(click.style("\n=== VIBEM CLEAN ===\n", fg='cyan', bold=True))

    paths = ProjectPaths(path)

    if paths.work_dir.exists():
        shutil.rmtree(paths.work_dir)
        log_success(f"Removed: {paths.work_dir}")

    if paths.output_dir.exists():
        shutil.rmtree(paths.output_dir)
        log_success(f"Removed: {paths.output_dir}")

    click.echo("")
    click.echo(click.style("CLEAN COMPLETE", fg='green', bold=True))


# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == '__main__':
    cli()
