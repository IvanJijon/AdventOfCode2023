from __future__ import annotations


def find_first_number(line: str | reversed) -> int:
    for c in line:
        try:
            return int(c)
        except ValueError:
            continue


def find_last_number(line: str) -> int:
    return find_first_number(reversed(line))

