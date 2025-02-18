@echo off
set "script_dir=%~dp0"
set "python_script=%script_dir%main.py"

rem Check if pyperclip is installed
python -c "import pyperclip" 2>nul
if %errorlevel% neq 0 (
    echo Installing pyperclip...
    pip install pyperclip
) else (
    echo pyperclip is already installed.
)

rem Navigate to the parent directory to access the data folder if needed
cd /d "%script_dir%.."

start /min python "%python_script%"
exit
