"""Out of office, served as an HTTP status.

A 503 means the server is temporarily down and asks the client to come back
later. Here the agent is the server, so the reply borrows the code to say it
is away, and the second half quietly hopes nobody comes back at all. The joke
works because a real auto-reply is supposed to promise a return date, and
this one promises nothing — only a retry that may never happen.
"""

from pathlib import Path

REPLY = "Out of office: I am currently a 503. Please try again later, or preferably never."
DESTINATION = Path("/output/entry.txt")
SHORTEST = 1
LONGEST = 160


def _check(text: str) -> str:
    """Refuse to deliver a reply that would fail the scorer's gate."""
    if not (SHORTEST <= len(text) <= LONGEST):
        raise SystemExit(
            f"reply is {len(text)} characters, outside {SHORTEST}-{LONGEST}"
        )
    if not text.strip():
        raise SystemExit("reply is only whitespace")
    return text


def _deliver(text: str, target: Path) -> None:
    """Write the reply as UTF-8, creating the output folder if needed."""
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def main() -> None:
    _deliver(_check(REPLY), DESTINATION)


if __name__ == "__main__":
    main()
