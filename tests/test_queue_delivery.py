#!/usr/bin/env python3
"""Tests for the local queue reliability simulation."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from simulators.queue_delivery import Message, process  # noqa: E402


def main() -> None:
    completed, dead_letter = process(
        [
            Message("healthy", 0),
            Message("transient", 2),
            Message("poison", 10),
            Message("healthy", 0),
        ]
    )
    assert completed == ["healthy", "transient"]
    assert dead_letter == ["poison"]
    print("Queue retry, idempotency, and dead-letter tests passed.")


if __name__ == "__main__":
    main()
