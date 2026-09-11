"""Read-only text statistics. Usage: python text_stats.py notes.txt."""

import argparse
from pathlib import Path


def text_stats(text):
    """Return line, whitespace-delimited word, and character counts."""
    return {"lines": len(text.splitlines()),
            "words": len(text.split()), "characters": len(text)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="UTF-8 text file")
    args = parser.parse_args()
    try:
        content = args.file.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        parser.exit(1, f"Cannot read file: {error}\n")
    for label, count in text_stats(content).items():
        print(f"{label.capitalize()}: {count}")


if __name__ == "__main__":
    main()
