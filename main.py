#!/usr/bin/env python3
"""Write the funniest AI excuse: one line, at most 200 characters."""

import os
from pathlib import Path

EXCUSE = (
    "I didn't miss the deadline \u2014 I moved it to a timeline where "
    "I'd already finished, and I'm still waiting for that version of "
    "me to send the file."
)


def main() -> None:
    # Self-check: the entry must be exactly one line of at most 200 characters.
    assert "\n" not in EXCUSE and "\r" not in EXCUSE, "entry must be one line"
    assert len(EXCUSE) <= 200, f"entry is {len(EXCUSE)} characters, over 200"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
