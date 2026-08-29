#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "==> Checking shell syntax"
while IFS= read -r script; do
  bash -n "${script}"
done < <(find "${repo_root}" -type f -name '*.sh' -not -path '*/.git/*' | sort)

echo "==> Validating architecture assessments"
python3 "${repo_root}/scripts/assess.py"

echo "==> Testing event-delivery reliability simulation"
python3 "${repo_root}/tests/test_queue_delivery.py"

echo "==> Checking documentation and identity policy"
python3 "${repo_root}/scripts/check.py"

echo "All AWS architecture checks passed. No AWS account or resources were used."
