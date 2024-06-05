#!/bin/sh

set -o errexit
set -o nounset

uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8000
