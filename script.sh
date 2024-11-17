#!/bin/bash

cd "$(dirname "$0")"
export PYTHONPATH=$(pwd)
python3 src/game/game.py
