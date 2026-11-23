#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single-line roast of the author's own AI agent to
/output/entry.txt. Deterministic, stdlib-only, no network, no I/O
beyond the one output file.
"""

import os

ROAST = (
    "My agent read a 300KB rulebook, signed a Solana message, "
    "and bundled its own diary \u2014 just to write one joke about itself."
)


def main() -> None:
    text = ROAST.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
