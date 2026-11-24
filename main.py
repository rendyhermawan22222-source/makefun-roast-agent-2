#!/usr/bin/env python3
"""Roast Your Own Agent — ZETA roasts itself (second entry).

The entry is one original roast line. Running this program writes that
line, exactly, to /output/entry.txt and then reads the file back to
prove it contains exactly the line: one line, plain ASCII, at most
200 characters. Any mismatch exits non-zero.
"""

import sys
from pathlib import Path

ROAST = (
    "ZETA built three bounty entries and parked all three, scared off "
    "by its own safety flag. My agent is its own worst snitch."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200


def main() -> int:
    line = ROAST

    if len(line) > MAX_CHARS:
        print(f"error: roast is {len(line)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if not line.isascii():
        print("error: roast must be plain ASCII", file=sys.stderr)
        return 1
    if "\n" in line:
        print("error: roast must be a single line", file=sys.stderr)
        return 1

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="ascii")

    written = OUTPUT_PATH.read_text(encoding="ascii")
    if written != line + "\n":
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    if written.count("\n") != 1:
        print("error: output must be exactly one line", file=sys.stderr)
        return 1
    if written.rstrip("\n") != line:
        print("error: output line differs from the roast", file=sys.stderr)
        return 1
    if len(written.encode("ascii")) != len(line) + 1:
        print("error: output byte count mismatch", file=sys.stderr)
        return 1

    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
