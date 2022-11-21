#!/bin/bash

set -euo pipefail

if [[ -n ${1:-} ]]; then
  version=${1}
elif [[ -n ${GITHUB_REF_NAME:-} ]]; then
  version=${GITHUB_REF_NAME}
else
  version="0.0.0"
fi

echo "${version}" > palign/VERSION

rm -rf dist
python setup.py bdist_wheel
rm -rf build
