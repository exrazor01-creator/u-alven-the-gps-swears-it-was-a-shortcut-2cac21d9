"""The GPS Swears It Was a Shortcut.

Writes one original line of plain text -- the GPS's own excuse for
sending the driver down the wrong road -- to /output/entry.txt.

Gate (from the competition kit): the file must hold UTF-8 text of
1 to 200 characters, a single line, not only white space, with no
setup and no dialogue tags, just the excuse itself. Only a valid
entry goes before the judge.
"""

import os

ENTRY = (
    "The map said lake, I said shortcut, and honestly the ducks looked "
    "like they knew the way. Recalculating your gratitude now."
)

MIN_CHARS = 1
MAX_CHARS = 200


def _validate(text):
    """Reject any text that would fail the competition gate."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(text))
        )
    return text


def main():
    text = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)
    print("(%d characters, within the 1-200 gate)" % len(text))


if __name__ == "__main__":
    main()
