# Duplicate scanning

## Scan a directory

Run `python tools/duplicate_scanner.py "sample files"` to recursively inspect files and print groups with matching content hashes.

## Group by size first

Files are grouped by byte size before hashing. A size group containing only one file is skipped because it cannot contain a duplicate within the scanned set.

## Hash in chunks

Candidate files are read in 1 MiB chunks using SHA-256. Chunked reading keeps file-content memory use bounded while processing large files.

## Read result groups

Each numbered group lists files whose computed SHA-256 hashes match. Different filenames can appear in the same group, and identical filenames can contain different content.
