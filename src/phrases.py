from __future__ import annotations

import re


_TOKEN_RE = re.compile(r"[A-Za-z0-9]+(?:'[A-Za-z0-9]+)?")


def extract_ngrams(text: str, n: int) -> list[str]:
    """Extract word n-grams using simple regex tokenization.

    Args:
        text: Input text.
        n: N-gram size (must be >= 1).

    Returns:
        List of n-grams as space-joined strings.
    """
    if n < 1:
        raise ValueError("n must be >= 1")

    tokens = [t.lower() for t in _TOKEN_RE.findall(text)]
    if len(tokens) < n:
        return []

    return [" ".join(tokens[i : i + n]) for i in range(0, len(tokens) - n + 1)]

