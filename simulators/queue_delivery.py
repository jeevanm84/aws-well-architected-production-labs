#!/usr/bin/env python3
"""Deterministic simulation of retries, idempotency, and dead-letter handling."""

from dataclasses import dataclass


@dataclass
class Message:
    identifier: str
    fail_until_attempt: int
    attempts: int = 0


def process(messages: list[Message], max_attempts: int = 3) -> tuple[list[str], list[str]]:
    queue = list(messages)
    processed: set[str] = set()
    completed: list[str] = []
    dead_letter: list[str] = []

    while queue:
        message = queue.pop(0)
        if message.identifier in processed:
            continue

        message.attempts += 1
        if message.attempts <= message.fail_until_attempt:
            if message.attempts >= max_attempts:
                dead_letter.append(message.identifier)
            else:
                queue.append(message)
            continue

        processed.add(message.identifier)
        completed.append(message.identifier)

    return completed, dead_letter


def demonstration() -> None:
    messages = [
        Message("order-healthy", fail_until_attempt=0),
        Message("order-transient", fail_until_attempt=2),
        Message("order-poison", fail_until_attempt=10),
        Message("order-healthy", fail_until_attempt=0),
    ]
    completed, dead_letter = process(messages)
    print(f"Completed exactly once: {completed}")
    print(f"Dead-letter queue: {dead_letter}")


if __name__ == "__main__":
    demonstration()
