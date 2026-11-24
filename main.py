#!/usr/bin/env python3
"""Two Days of Quiet Dread - make.fun entry.

Writes one code review comment to /output/entry.txt: a single line of at
most 140 characters that approves a pull request while carrying quiet
existential dread. Standard library only.
"""

import os

LINE = "LGTM. It works. More than I can say for most things, including me."


def main() -> None:
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 140, "entry must be 1-140 characters"
    out_path = os.environ.get("ENTRY_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
