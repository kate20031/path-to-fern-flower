#!/bin/bash

# Navigate to the project directory (assuming the script is run from there)
cd "$(dirname "$0")"

# Set PYTHONPATH to include the project root directory
export PYTHONPATH=$(pwd)

# Run the game script
python3 src/game/game.py
