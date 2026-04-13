from __future__ import annotations

from collections import Counter


def count_phrases(phrases: list[str]) -> dict[str, int]:
    """Count phrase frequencies.

    Args:
        phrases: List of phrases (e.g. n-grams).

    Returns:
        Mapping of phrase -> count.
    """
    return dict(Counter(phrases))

