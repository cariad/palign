#!/bin/bash

set -euo pipefail

echo "${1:?}" > palign/VERSION

rm -rf dist
python setup.py bdist_wheel
rm -rf build
