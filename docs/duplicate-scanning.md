# Duplicate scanning

## Scan a directory

Run `python tools/duplicate_scanner.py "sample files"` to recursively inspect files and print groups with matching content hashes.

## Group by size first

Files are grouped by byte size before hashing. A size group containing only one file is skipped because it cannot contain a duplicate within the scanned set.
