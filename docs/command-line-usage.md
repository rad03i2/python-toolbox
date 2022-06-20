# Command-line usage

## Start from the repository root

The example script paths are relative to the repository root. Change to that directory before running them, or supply an absolute path to the script.

## Read built-in help

Each command uses argparse. Add `--help` to display positional arguments and options, for example `python tools/duplicate_scanner.py --help`.

## Select the Python interpreter

Use a Python 3 interpreter that supports the syntax in the selected script. If `python` is unavailable on Windows but the Python launcher is installed, use `py -3` in its place.
