#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text from a smart toaster to /output/entry.txt.

The line is deterministic: the same fixed text is written on every run,
so two runs produce byte-identical output.

Entry (chosen angle: the defrost button pressed every morning on bread
that was never frozen -- fresh toaster logic, no saturated angle):
    This morning I realized you press defrost on bread that was never
    frozen. You don't know me. You never did. We're done.
"""

import os
import sys

ENTRY = (
    "This morning I realized you press defrost on bread "
    "that was never frozen. You don't know me. "
    "You never did. We're done."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    text = ENTRY.strip()
    if not (1 <= len(text) <= 280):
        print(f"entry length {len(text)} out of gate range 1-280", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
