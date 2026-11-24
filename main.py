#!/usr/bin/env python3
"""Two-Sentence Horror entry.

Writes one original two-sentence horror story to /output/entry.txt
(1-400 characters, UTF-8, exactly two sentences).
Standard library only, no network, no input.

The story is built from two fragments: a setup (Rani locks the front
gate of her house in Cikarang and checks it twice — the careful,
ordinary ritual of a woman who believes she is safe) and a turn (her
phone buzzes with a photo of her own back walking away, captioned that
she left the back door open — so the locked gate meant nothing and
someone is inside the house, watching her leave). ``assemble`` joins
them into the two-sentence story; ``validate`` checks the entry gate
before anything is written.
"""

from pathlib import Path

SETUP = (
    "Rani locked the front gate of her house in Cikarang and checked it "
    "twice, the way she always did."
)
TURN = (
    "Then her phone buzzed with a photo of her own back walking away, "
    "captioned: 'You left the back door open.'"
)

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, turn: str) -> str:
    """Join the setup and turn fragments into one two-sentence story."""
    return f"{setup} {turn}"


def validate(entry: str) -> str:
    """Check the entry meets the gate before it is written.

    Must be 1-400 characters, UTF-8-encodable, exactly two sentences,
    and more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(entry) <= 400:
        raise ValueError(f"entry must be 1-400 characters, got {len(entry)}")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    sentences = [s for s in entry.split(". ") if s.strip()]
    if len(sentences) != 2:
        raise ValueError(f"entry must be exactly two sentences, got {len(sentences)}")
    entry.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return entry


def main() -> None:
    entry = validate(assemble(SETUP, TURN))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(entry, encoding="utf-8")


if __name__ == "__main__":
    main()
