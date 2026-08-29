#!/usr/bin/env python3
"""Validate and summarize a structured AWS architecture assessment."""

from pathlib import Path
import json
import sys


PILLARS = (
    "operational_excellence",
    "security",
    "reliability",
    "performance_efficiency",
    "cost_optimization",
    "sustainability",
)

REQUIRED_TOP_LEVEL = (
    "id",
    "title",
    "problem",
    "requirements",
    "architecture",
    "pillars",
    "failure_modes",
    "decisions",
    "verification",
    "cost_controls",
    "production_readiness",
)


def validate(path: Path) -> tuple[dict, list[str]]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return {}, [f"{path}: {error}"]

    for key in REQUIRED_TOP_LEVEL:
        if key not in data:
            errors.append(f"{path}: missing top-level field '{key}'")

    requirements = data.get("requirements", {})
    for key in ("availability", "rto_minutes", "rpo_minutes", "security", "cost"):
        if key not in requirements:
            errors.append(f"{path}: requirements.{key} is required")

    architecture = data.get("architecture", {})
    for key in ("summary", "services", "data_flow"):
        if not architecture.get(key):
            errors.append(f"{path}: architecture.{key} must be non-empty")

    pillars = data.get("pillars", {})
    for pillar in PILLARS:
        assessment = pillars.get(pillar, {})
        if not assessment.get("decisions"):
            errors.append(f"{path}: pillars.{pillar}.decisions must be non-empty")
        if not assessment.get("evidence"):
            errors.append(f"{path}: pillars.{pillar}.evidence must be non-empty")

    for list_key in ("failure_modes", "decisions", "verification", "cost_controls", "production_readiness"):
        value = data.get(list_key)
        if not isinstance(value, list) or not value:
            errors.append(f"{path}: {list_key} must be a non-empty list")

    for index, failure in enumerate(data.get("failure_modes", []), start=1):
        for key in ("incident", "impact", "detection", "mitigation", "prevention"):
            if not failure.get(key):
                errors.append(f"{path}: failure_modes[{index}].{key} is required")

    for index, decision in enumerate(data.get("decisions", []), start=1):
        for key in ("id", "decision", "trade_off", "revisit_when"):
            if not decision.get(key):
                errors.append(f"{path}: decisions[{index}].{key} is required")

    return data, errors


def summarize(data: dict, path: Path) -> None:
    requirements = data["requirements"]
    print(f"Assessment: {data['title']} ({path})")
    print(f"Availability target: {requirements['availability']}")
    print(f"RTO/RPO: {requirements['rto_minutes']} / {requirements['rpo_minutes']} minutes")
    print(f"Decisions: {len(data['decisions'])}")
    print(f"Failure modes: {len(data['failure_modes'])}")
    print(f"Verification activities: {len(data['verification'])}")


def main() -> int:
    paths = [Path(argument) for argument in sys.argv[1:]]
    if not paths:
        paths = sorted((Path(__file__).resolve().parents[1] / "scenarios").glob("*.json"))

    all_errors: list[str] = []
    valid_data: list[tuple[dict, Path]] = []
    for path in paths:
        data, errors = validate(path)
        all_errors.extend(errors)
        if not errors:
            valid_data.append((data, path))

    if all_errors:
        print("Architecture assessment validation failed:", file=sys.stderr)
        for error in all_errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    for data, path in valid_data:
        summarize(data, path)
    print(f"Validated {len(valid_data)} architecture assessments.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
