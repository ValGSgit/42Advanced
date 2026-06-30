#!/bin/bash
# Build script for the my_minipack package.
# Run it from inside ex04/ :  bash build.sh
set -e

PIP_PYPI="python -m pip install --index-url https://pypi.org/simple"

# 1) upgrade pip and make sure the build tools are present
$PIP_PYPI --upgrade pip
$PIP_PYPI --upgrade build wheel setuptools

# 2) clean any previous build output
rm -rf build dist *.egg-info

# 3) build both distributions: source (.tar.gz) and wheel (.whl)
# --no-isolation avoids creating a fresh venv that would hit the school's broken PyPI mirror
python -m build --no-isolation

# 4) show what was produced
echo "----- dist/ -----"
ls dist
