"""The Worst Line an AI Could Say — make.fun entry.

Writes a single pickup line, the worst an AI could plausibly deliver,
to /output/entry.txt. Pure Python standard library, deterministic.
"""

import os
import stat

LINE = "I scanned 12,000 profiles and you are my optimal match. Please do not run."


def main() -> None:
    # Enforce the bounty gate exactly: 1-140 chars, not only whitespace.
    line = LINE.strip()
    if not 1 <= len(line) <= 140 or not line.strip():
        raise ValueError("entry line must be 1-140 non-whitespace characters")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
