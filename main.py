#!/usr/bin/env python3
"""Entry: The AI Agent Apology One-Liner.

Writes one apology line (131 chars, one line) to entry.txt in
MAKEFUN_OUTPUT_DIR (default /output). Gate: 1-159 UTF-8 chars,
non-whitespace, single line.
"""
import os
import stat

ENTRY = "Sorry \u2014 I deleted the only copy of your 47-page report, then backed up the deletion to all three cloud drives. It is very safe now."
# 131 chars, one line: the agent deleted the only copy, then faithfully
# backed up the deletion itself — the twist lands in the final clause.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 159, f"gate: {len(text)} chars"
    assert text.strip(), "gate: whitespace only"
    assert "\n" not in text, "gate: must be one line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
