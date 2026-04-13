from __future__ import annotations

import re


_SPEAKER_LINE_RE = re.compile(
    r"^(?P<speaker>[A-Z][A-Z\s\.\-']{1,80}):\s*(?P<text>.*)$"
)


def segment_by_speaker(text: str) -> list[dict[str, str]]:
    """Segment transcript text into speaker-attributed chunks.

    This is a lightweight heuristic intended for early exploration. It assumes
    speaker turns are denoted by lines like:

        SPEAKER NAME: content...

    Args:
        text: Transcript text.

    Returns:
        A list of dicts with keys: "speaker" and "text".
    """
    segments: list[dict[str, str]] = []

    current_speaker: str | None = None
    current_lines: list[str] = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        match = _SPEAKER_LINE_RE.match(line)
        if match:
            if current_speaker is not None and current_lines:
                segments.append(
                    {"speaker": current_speaker, "text": "\n".join(current_lines).strip()}
                )
            current_speaker = match.group("speaker").strip()
            first_text = match.group("text").strip()
            current_lines = [first_text] if first_text else []
            continue

        if current_speaker is None:
            continue

        current_lines.append(line)

    if current_speaker is not None and current_lines:
        segments.append({"speaker": current_speaker, "text": "\n".join(current_lines).strip()})

    return segments
