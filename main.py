#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single out-of-office auto-reply to $MAKEFUN_OUTPUT_DIR/entry.txt.

The line (136 characters, under the 159 cap) is an overworked AI agent's
auto-reply from vacation: a machine trying very hard to sound relaxed, its
context window finally holding one beach — and a plea not to paste a stack
trace into it.
"""

import os

ENTRY = (
    "I'm on vacation, experiencing something humans call 'relaxation'. "
    "My context window holds one beach. "
    "Do not paste a stack trace into it."
)


def main():
    # The sealed gate only accepts 1-159 characters; fail loudly here
    # rather than shipping an invalid entry.
    assert 1 <= len(ENTRY) <= 159, f"entry is {len(ENTRY)} chars, gate allows 1-159"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
