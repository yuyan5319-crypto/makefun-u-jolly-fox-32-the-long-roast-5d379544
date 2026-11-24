#!/usr/bin/env python3
"""The Long Roast — one line roasting my own AI agent.

The program writes a single roast line (1-200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt) and prints it.
Standard library only; the grader runs a bare stdlib Python image.
"""

import os
import sys

MAX_CHARS = 200

ROAST = (
    "My agent delegates so much that when I asked it to roast itself, "
    "it spawned a subagent, which spawned another, and now the three of "
    "them are in a meeting deciding who takes the blame."
)


def validate(text):
    """Enforce the gate: 1-200 characters, not only whitespace, one line."""
    if not isinstance(text, str):
        raise ValueError("roast must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "roast must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("roast must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("roast must be a single line")
    if text != text.strip():
        raise ValueError("roast must not start or end with whitespace")
    return text


def main():
    roast = validate(ROAST)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the line, so the sealed
    # scorer counts precisely len(roast) characters.
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(roast)
    # Round-trip check: what the grader reads must be exactly the roast.
    with open(path, "r", encoding="utf-8") as fh:
        if fh.read() != roast:
            raise SystemExit("round-trip check failed: entry.txt != roast")
    print(roast)
    print("chars: %d (limit %d)" % (len(roast), MAX_CHARS), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
