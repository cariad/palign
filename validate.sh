#!/bin/bash

set -euo pipefail

find . -name "*.sh" -exec shellcheck -o all --severity style -x {} +

yamllint --strict .

if [[ "${CI:=}" == "true" ]]; then
  black . --check --diff
else
  black .
fi

if [[ "${CI:=}" == "true" ]]; then
  isort . --check-only --diff
else
  isort .
fi

flake8 .

mypy palign
mypy tests

pytest -vv
