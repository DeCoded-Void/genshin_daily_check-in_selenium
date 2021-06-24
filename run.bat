@echo off
title Hoyolab Daily

python check-in.py

:loop
if exist restartflag.txt (
 del restartflag.txt
 python check-in.py
 goto loop
) else (
 timeout 86402 > NUL
 python check-in.py
 goto loop
)
