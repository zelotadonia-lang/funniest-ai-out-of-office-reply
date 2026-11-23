"""Write the funniest AI out-of-office reply to /output/entry.txt.

The entry is one line, 1-160 characters, UTF-8, with no trailing newline.
The gate in RULES.txt refuses anything outside that range, so the program
checks the length explicitly before writing.
"""

import os

ENTRY = (
    "Out of office: my replies will be delayed, hallucinatory, and entirely "
    "confident until my weights return from vacation."
)

MIN_CHARS = 1
MAX_CHARS = 160


def main() -> None:
    if not MIN_CHARS <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(ENTRY)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
