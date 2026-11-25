#!/usr/bin/env python3
"""One-Line Office Jokes: a single self-contained office gag.

Writes one line of office comedy (1-199 characters, no line breaks)
to /output/entry.txt for the house judge to read.
"""
from pathlib import Path


def check_line(text):
    """Refuse anything that is not one plain line of the right size."""
    assert text and text.strip(), "line must not be blank"
    assert text == text.strip(), "line must not have edge whitespace"
    assert "\n" not in text and "\r" not in text, "line must be one line"
    assert 1 <= len(text) <= 199, "line must be 1-199 characters"
    return text


def joke_line():
    opener = "I asked 400 colleagues to take me off this thread, "
    closer = "and 87 of them replied-all to agree."
    line = check_line(opener + closer)
    assert len(line) == 87, "joke came out the wrong length"
    return line


def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(joke_line(), encoding="utf-8")


if __name__ == "__main__":
    main()
