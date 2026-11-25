#!/usr/bin/env python3
"""Write one funny line to /output/entry.txt.

Entry for make.fun's "One Line, One Laugh" bounty: a single line, at
most 200 characters, nothing else. The program writes exactly that
line to /output/entry.txt and leaves the file world-readable.
"""

import os

ENTRY = (
    "My kettle has filed a formal complaint: boiled four times a day, "
    "ignored the rest of the time, and still blamed every time it screams."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    # The grader collects outputs as another user, so the file itself
    # must be world-readable. Never chmod the /output directory.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
