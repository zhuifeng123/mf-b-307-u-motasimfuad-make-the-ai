#!/usr/bin/env python3
"""Write the competition entry to /output/entry.txt (deterministic, stdlib only)."""

import os

ENTRY = (
    "It works on my machine — so I've promoted my laptop to production. "
    "Please send snacks and a fire extinguisher."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
