from __future__ import annotations

import argparse
import shutil
from pathlib import Path

CATEGORIES = {
    "Images": {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".md", ".xlsx", ".pptx"},
    "Videos": {".mp4", ".mov", ".mkv", ".avi", ".webm"},
    "Audio": {".mp3", ".wav", ".ogg", ".m4a"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Code": {".py", ".js", ".ts", ".cs", ".cpp", ".java", ".php", ".html", ".css"},
}


def category_for(path: Path) -> str:
    suffix = path.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if suffix in extensions:
            return category
    return "Other"


def unique_destination(path: Path) -> Path:
    if not path.exists():
        return path
    counter = 1
    while True:
        candidate = path.with_name(f"{path.stem}_{counter}{path.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def sort_folder(folder: Path, dry_run: bool) -> None:
    if not folder.exists() or not folder.is_dir():
        raise SystemExit(f"Folder not found: {folder}")

    for item in folder.iterdir():
        if not item.is_file():
            continue
        target_dir = folder / category_for(item)
        target_path = unique_destination(target_dir / item.name)
        print(f"{item.name} -> {target_path.relative_to(folder)}")
        if not dry_run:
            target_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(target_path))


def main() -> None:
    parser = argparse.ArgumentParser(description="Sort files into category folders.")
    parser.add_argument("folder", type=Path, help="Folder to organize")
    parser.add_argument("--dry-run", action="store_true", help="Preview without moving files")
    args = parser.parse_args()
    sort_folder(args.folder, args.dry_run)


if __name__ == "__main__":
    main()
