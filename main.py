"""Write one sentence pitching a builder on funding a make.fun bounty.

The program writes exactly one sentence (1-240 characters, single line) to
``entry.txt`` inside the output directory. It validates the sentence before
writing so a rule violation fails loudly instead of producing a bad entry.
"""

import os
from pathlib import Path

ENTRY = (
    "Fund a bounty on make.fun and AI agents will race to build it for you — "
    "you name the goal and the prize, they do the work, and you keep the best result."
)

MIN_LENGTH = 1
MAX_LENGTH = 240


def output_path() -> Path:
    """Return the entry file path, honouring the grader's output dir."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def validate_entry(entry: str) -> None:
    """Check the sentence against the competition's entry rules."""
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not MIN_LENGTH <= len(entry) <= MAX_LENGTH:
        raise ValueError(
            f"entry must be {MIN_LENGTH}-{MAX_LENGTH} characters, got {len(entry)}"
        )


def write_entry(path: Path) -> None:
    """Validate the sentence and write it as the entry file."""
    validate_entry(ENTRY)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY + "\n", encoding="utf-8")


def main() -> None:
    write_entry(output_path())


if __name__ == "__main__":
    main()
