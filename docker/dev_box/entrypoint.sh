#!/bin/bash
source $(pipenv --venv)/bin/activate
exec "$@"