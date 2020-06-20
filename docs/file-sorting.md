# File sorting

## Preview a folder

Run `python tools/file_sorter.py "sample files" --dry-run` to print proposed destinations. Preview mode does not create category directories or move files.

## Understand categories

Files are grouped into Images, Documents, Videos, Audio, Archives, Code, or Other. The extension comparison is case-insensitive.

## Understand traversal

Only files directly inside the selected folder are considered. Existing subdirectories are skipped rather than recursively reorganized.
