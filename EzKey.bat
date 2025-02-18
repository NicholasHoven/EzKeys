@echo off
set "script_dir=%~dp0"
set "python_script=%script_dir%main.py"

start /min python "%python_script%"
exit
