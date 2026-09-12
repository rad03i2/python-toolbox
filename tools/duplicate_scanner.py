from __future__ import annotations

import argparse
import hashlib
from collections import defaultdict
from pathlib import Path

CHUNK_SIZE = 1024 * 1024


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()


def scan(folder: Path) -> dict[str, list[Path]]:
    by_size: dict[int, list[Path]] = defaultdict(list)
    for file in folder.rglob("*"):
        if file.is_file():
            try:
                by_size[file.stat().st_size].append(file)
            except OSError:
                print(f"Skipped: {file}")

    duplicates: dict[str, list[Path]] = defaultdict(list)
    for same_size in by_size.values():
        if len(same_size) < 2:
            continue
        for file in same_size:
            try:
                duplicates[sha256(file)].append(file)
            except OSError:
                print(f"Skipped: {file}")

    return {hash_value: files for hash_value, files in duplicates.items() if len(files) > 1}


def main() -> None:
    parser = argparse.ArgumentParser(description="Find duplicated files by content.")
    parser.add_argument("folder", type=Path)
    args = parser.parse_args()

    if not args.folder.exists():
        raise SystemExit("Folder not found.")

    groups = scan(args.folder)
    if not groups:
        print("No duplicated files found.")
        return

    for index, files in enumerate(groups.values(), start=1):
        print(f"\nGroup {index}")
        for file in files:
            print(f" - {file}")


if __name__ == "__main__":
    main()
