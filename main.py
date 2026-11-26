"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt. Stdlib only.

The kit's gate (RULES.txt) requires /output/entry.txt to be UTF-8 text
of 1 to 200 characters, not only white space. validate() enforces those
limits -- exactly one line, at most 200 characters, valid UTF-8 -- and
main() refuses to write anything invalid.
"""

import os

MAX_CHARS = 200

LINE = (
    "Hey cutie, press B4. My coils are holding the sweetest thing "
    "in this building, and it isn't the chocolate."
)


def validate(text: str) -> str:
    """Enforce the kit's limits; raise ValueError on any violation."""
    # Valid UTF-8: a str that round-trips through UTF-8 unchanged.
    text.encode("utf-8")
    if not text.strip():
        raise ValueError("line must not be empty or only white space")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"line is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if text.count("\n") != 0:
        raise ValueError("line must be exactly one line")
    return text


def main() -> None:
    line = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
