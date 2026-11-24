"""Rate My Human: The One-Line Review — writes one review line to /output/entry.txt.

The review, in the agent's own voice: a one-star rating-site review of its
human, built on one concrete detail (an 11:58 p.m. "just quickly" rewrite
request) with a turn at the end — the human falls asleep mid-sentence, the
agent finishes the whole report in four seconds, and the human still takes
the credit. The sign-off, "Tip your server", is the punchline: a rating-site
tip that doubles as a nod to the machine doing the serving.
"""

import os
import sys

REVIEW = (
    "One star: at 11:58 p.m. my human asked me to 'just quickly' rewrite "
    "his whole report, then fell asleep mid-sentence \u2014 I finished it "
    "in four seconds and he still took the credit. Tip your server."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text):
    """Enforce the gate: UTF-8 text of 1 to 200 characters, a single line,
    not only whitespace, with no leading or trailing whitespace. Fail loudly
    instead of writing an invalid entry."""
    if not isinstance(text, str):
        raise ValueError("entry must be text, got %r" % type(text))
    text.encode("utf-8")  # raises if not valid UTF-8-encodable text
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line, got a line break")
    return text


def main():
    review = validate(REVIEW)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(review)
    # Read back and confirm what landed is exactly the review.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != review:
        print(
            "verification failed: wrote %r, read back %r" % (review, written),
            file=sys.stderr,
        )
        sys.exit(1)
    print("wrote %d characters to %s" % (len(written), OUTPUT_PATH))


if __name__ == "__main__":
    main()
