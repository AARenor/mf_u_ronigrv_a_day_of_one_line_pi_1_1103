#!/usr/bin/env python3
"""Write make.fun's u-ronigrv-a-day-of-one-line-pitches-12cd9bb3 entry text."""

import os
import sys
from pathlib import Path

TEXT = (
    "My sister, who has never written code, sent make.fun a note about her "
    "plant-watering reminder and got back a little app with her plants' names "
    "still spelled wrong, which is how I knew it was really hers."
)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"entry text must be 1-280 characters, got {len(TEXT)}"

    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    entry = out_dir / "entry.txt"
    with open(entry, "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)

    print(f"{len(TEXT)} characters written to {entry}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
