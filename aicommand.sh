#!/bin/bash
source ./venv/bin/activate
python3.10 ./aicommand.py "$@"
deactivate
