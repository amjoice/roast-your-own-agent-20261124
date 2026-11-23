#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single-line roast of the author's own AI agent to
/output/entry.txt. Deterministic, stdlib-only, no network, no I/O
beyond the one output file.
"""

import os

MAX_CHARS = 200

# The joke's structure: a list of three absurd bureaucratic chores the
# agent really did for this bounty (read the 300KB skill file, sign a
# Solana entry message, bundle its own session transcripts), then the
# punchline at the very end — all of that effort, for one line.
ROAST_PARTS = (
    "My agent read a 300KB rulebook,",
    "signed a Solana message,",
    "and bundled its own diary",
    "\u2014 just to write one joke about itself.",
)

ROAST = " ".join(ROAST_PARTS)


def main() -> None:
    text = ROAST.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} chars, got {len(text)}"
    )
    assert text == " ".join(text.split()), "entry must have no stray whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
