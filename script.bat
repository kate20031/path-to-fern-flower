@echo off
REM
cd /d "%~dp0"

REM
set PYTHONPATH=%cd%

REM
python -m src.game.game
