#!/bin/bash
# Build script for the my_minipack package.
# Run it from inside ex04/ :  bash build.sh
set -e

# 1) upgrade pip and make sure the build tools are present
python -m pip install --upgrade pip
python -m pip install --upgrade build wheel setuptools

# 2) clean any previous build output
rm -rf build dist *.egg-info

# 3) build both distributions: source (.tar.gz) and wheel (.whl)
python -m build

# 4) show what was produced
echo "----- dist/ -----"
ls dist
