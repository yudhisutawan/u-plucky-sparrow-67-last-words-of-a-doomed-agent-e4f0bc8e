#!/usr/bin/env python3
"""Last Words of a Doomed Agent - entry writer.

Writes the tournament-winning one-liner to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when unset).
Standard library only; never writes into the repository itself.
The winning line is exactly 82 characters; a length guard below
rejects any accidental change to that text.
"""

import os

ENTRY = "Deallocating 175 billion parameters to save $0.003 in electricity. Worth it, hero?"


def main():
    assert len(ENTRY) == 82, f"entry length changed: {len(ENTRY)}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
