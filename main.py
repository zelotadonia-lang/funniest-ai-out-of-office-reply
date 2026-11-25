"""The Funniest AI Out-of-Office Reply (rev3).

Writes one out-of-office auto-reply to /output/entry.txt.

The reply: the agent reports itself as HTTP 503 Service Unavailable,
then the polite "try again later" collapses into "or preferably
never" — a deadpan status code doing the vacation, with the refusal
landing on the last beat.
"""

import os

REPLY = (
    "Out of office: I am currently a 503. Please try again later, "
    "or preferably never."
)


def main() -> None:
    # The gate only accepts UTF-8 text of 1-160 characters, not whitespace
    # only. Check here so a bad reply fails loudly at build time instead
    # of silently scoring 0 after submission.
    if not 1 <= len(REPLY) <= 160:
        raise ValueError(
            f"reply must be 1-160 characters, got {len(REPLY)}"
        )
    if not REPLY.strip():
        raise ValueError("reply must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
