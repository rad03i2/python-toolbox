# Text statistics

## Read a UTF-8 file

Run `python text_stats.py notes.txt` from the repository root. The command opens the file as UTF-8 and prints line, word, and character counts.

## Count lines

Line counts use `str.splitlines()`. An empty file has zero lines; a final newline does not add an extra empty line.
