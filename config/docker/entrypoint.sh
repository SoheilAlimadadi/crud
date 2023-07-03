#!/bin/sh

# if any of the commands in your code fails the entire scripts fails.
set -o errexit

# exit if any of your variables is not set.
set -o nounset

set -x

# Clear Python caches
find . -name "*.pyc" -exec rm -f {} \;

alembic upgrade head

uvicorn main:app --host 0.0.0.0 --port 8000
