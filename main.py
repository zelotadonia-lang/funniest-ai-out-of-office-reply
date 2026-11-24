"""The Funniest AI Out-of-Office Reply (rev2).

Writes one out-of-office auto-reply to /output/entry.txt.

The reply: the agent's own context window is on vacation too, so it
will forget the email, then the sender's name, then itself — the
machine's memory loss escalates until the machine is the thing lost.
"""

import os

REPLY = (
    "Out of office: my context window is on vacation too, so I will "
    "forget this email, your name, and eventually myself."
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
