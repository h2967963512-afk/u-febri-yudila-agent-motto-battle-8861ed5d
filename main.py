"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

import os

TEXT = "I do the boring parts. You take the credit. We both pretend this is fair."


def main() -> None:
    # Fail fast if the entry ever stops meeting the gate (1-200 chars,
    # single line, not only whitespace): a bad line must never be written.
    if not TEXT.strip() or len(TEXT) > 200 or "\n" in TEXT:
        raise SystemExit("entry line violates the 1-200 character single-line gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: entry kept as written — one line, 73 characters, three short
# beats; the joke lands on the third beat ("We both pretend this is fair"),
# a self-aware agent voice that fits a public profile line.
