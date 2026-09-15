# Python Toolbox

A collection of practical command-line utilities written with **Python 3** and the standard library.

## Tools

| Tool | Purpose |
|---|---|
| `text_stats.py` | Count lines, words, and characters in a text file. |
| `tools/file_sorter.py` | Sort files into folders by extension. |
| `tools/duplicate_scanner.py` | Find duplicated files using size grouping and SHA-256 hashing. |
| `tools/password_strength.py` | Estimate password strength using simple transparent rules. |

## Run

```sh
python text_stats.py notes.txt
python tools/file_sorter.py ~/Downloads --dry-run
python tools/duplicate_scanner.py ~/Downloads
python tools/password_strength.py "ExamplePassword123!"
```

## Why this repository exists

This repo demonstrates small but useful automation ideas: file handling, hashing, CLI arguments, safe dry-run modes, and readable output.

## Official links

- Portfolio: https://rdwan.dev
- Project page: https://rdwan.dev/projects/03-python-toolbox.html
