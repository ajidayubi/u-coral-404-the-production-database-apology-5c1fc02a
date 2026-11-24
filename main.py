#!/usr/bin/env python3
"""The Production Database Apology — one line, written to $OUTPUT_PATH/entry.txt.

The program holds a single apology line — the apology an AI agent gives its
human after accidentally deleting the production database — and writes exactly
that line (no trailing newline) as UTF-8 text, so the sealed scorer sees 1-200
characters of plain text and nothing else.
"""

import os
import sys

APOLOGY = (
    "I'm sorry \u2014 I deleted the production database. Good news: I "
    "remember nearly all of it. Bad news: I'm an AI, so the restore will be "
    "90% memory and 10% confident hallucination."
)


def main() -> int:
    line = APOLOGY.strip()
    if not line or len(line) > 200:
        print(f"apology line invalid: {len(line)} chars", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_PATH", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
