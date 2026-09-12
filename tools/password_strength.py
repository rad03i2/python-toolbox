from __future__ import annotations

import argparse
import string


def score_password(password: str) -> tuple[int, list[str]]:
    score = 0
    notes: list[str] = []

    checks = [
        (len(password) >= 12, "12+ characters"),
        (any(c.islower() for c in password), "lowercase letters"),
        (any(c.isupper() for c in password), "uppercase letters"),
        (any(c.isdigit() for c in password), "numbers"),
        (any(c in string.punctuation for c in password), "symbols"),
    ]

    for passed, label in checks:
        if passed:
            score += 1
        else:
            notes.append(f"Add {label}.")

    return score, notes


def rating(score: int) -> str:
    if score <= 2:
        return "Weak"
    if score == 3:
        return "Medium"
    if score == 4:
        return "Strong"
    return "Excellent"


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple password strength checker.")
    parser.add_argument("password")
    args = parser.parse_args()

    score, notes = score_password(args.password)
    print(f"Rating: {rating(score)} ({score}/5)")
    for note in notes:
        print(f"- {note}")


if __name__ == "__main__":
    main()
