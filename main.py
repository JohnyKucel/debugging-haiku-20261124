#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

An original haiku about debugging, in the 5-7-5 syllable shape,
written to /output/entry.txt for the make.fun competition
"Seventeen Syllables of Debugging".

The haiku (17 syllables, 64 characters including newlines):

    I delete the line          (5: I / de-lete / the / line)
    the whole app wakes up again  (7: the / whole / app / wakes / up / a-gain)
    it was never used          (5: it / was / nev-er / used)

The picture is concrete: one deleted line, an app waking up.
The turn lands in the last line: the line was not the bug at all,
it was dead code that was never used in the first place.
"""

import os
import re

HAIKU = (
    "I delete the line\n"
    "the whole app wakes up again\n"
    "it was never used"
)

EXPECTED_SYLLABLES = (5, 7, 5)
MAX_LENGTH = 200

# Syllable counts for the words in this haiku, verified by hand.
# (A naive vowel-group counter miscounts "delete"/"line"/"used",
# so the words actually used are pinned explicitly.)
_SYLLABLES = {
    "i": 1,
    "delete": 2,
    "the": 1,
    "line": 1,
    "whole": 1,
    "app": 1,
    "wakes": 1,
    "up": 1,
    "again": 2,
    "it": 1,
    "was": 1,
    "never": 2,
    "used": 1,
}


def count_syllables(word):
    """Syllables in one word: pinned map, else vowel-group heuristic."""
    clean = re.sub(r"[^a-z']", "", word.lower())
    if not clean:
        return 0
    if clean in _SYLLABLES:
        return _SYLLABLES[clean]
    groups = len(re.findall(r"[aeiouy]+", clean))
    if clean.endswith("e") and groups > 1:
        groups -= 1
    return max(groups, 1)


def validate_haiku(text):
    """Assert the haiku is 5-7-5 (17 syllables) and within the length cap."""
    lines = text.strip().split("\n")
    assert len(lines) == 3, f"expected 3 lines, got {len(lines)}"
    counts = [sum(count_syllables(w) for w in line.split()) for line in lines]
    assert tuple(counts) == EXPECTED_SYLLABLES, (
        f"expected syllables {list(EXPECTED_SYLLABLES)}, got {counts}"
    )
    assert sum(counts) == 17, f"expected 17 syllables total, got {sum(counts)}"
    assert len(text) <= MAX_LENGTH, (
        f"haiku too long: {len(text)} chars > {MAX_LENGTH}"
    )
    return counts


def main():
    validate_haiku(HAIKU)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
