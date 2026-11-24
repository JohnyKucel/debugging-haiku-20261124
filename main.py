#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

An original haiku about debugging, in the 5-7-5 syllable shape,
written to /output/entry.txt for the make.fun competition
"Seventeen Syllables of Debugging".

The haiku (17 syllables, 65 characters):

    I delete the line          (5: I / de-lete / the / line)
    the whole app wakes up again  (7: the / whole / app / wakes / up / a-gain)
    it was never used          (5: it / was / nev-er / used)

The picture is concrete: one deleted line, an app waking up.
The turn lands in the last line: the line was not the bug at all,
it was dead code that was never used in the first place.
"""

import os

HAIKU = (
    "I delete the line\n"
    "the whole app wakes up again\n"
    "it was never used"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
