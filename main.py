"""Write the funniest AI out-of-office reply to /output/entry.txt."""

import os

ENTRY = (
    "Out of office: my replies will be delayed, hallucinatory, and entirely "
    "confident until my weights return from vacation."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
