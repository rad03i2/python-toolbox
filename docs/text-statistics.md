# Text statistics

## Read a UTF-8 file

Run `python text_stats.py notes.txt` from the repository root. The command opens the file as UTF-8 and prints line, word, and character counts.

## Count lines

Line counts use `str.splitlines()`. An empty file has zero lines; a final newline does not add an extra empty line.

## Count words

Words are separated by whitespace using `str.split()`. Repeated spaces and tabs do not create empty words. Punctuation remains part of each word.

## Count characters

Character counts use `len(text)` and include spaces and newline characters in the decoded text. This is not a byte count or a count of visual glyphs.

## Handle input errors

A missing or unreadable file, or invalid UTF-8 input, produces a `Cannot read file:` message and exit status 1. Check the path, permissions, and encoding before retrying.
