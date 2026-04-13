from __future__ import annotations

from pathlib import Path

import requests


def fetch_html(url: str) -> str:
    """Fetch HTML content from a URL.

    Args:
        url: A fully-qualified URL.

    Returns:
        The response body as text.

    Raises:
        requests.HTTPError: If the response is not successful.
        requests.RequestException: For network/transport errors.
    """
    resp = requests.get(
        url,
        headers={"User-Agent": "Discourse-Intelligence-Engine/0.1 (+https://example.com)"},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.text


def save_raw_html(content: str, filename: str) -> Path:
    """Save raw HTML to `data/raw/`.

    Args:
        content: HTML text content.
        filename: Output filename (e.g. "sample.html").

    Returns:
        The path written.
    """
    out_dir = Path("data") / "raw"
    out_dir.mkdir(parents=True, exist_ok=True)

    out_path = out_dir / filename
    out_path.write_text(content, encoding="utf-8")
    return out_path

