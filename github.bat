@echo off

REM Navigate to the directory of the batch file
cd /d "%~dp0"

REM Run the git_commands.sh script using Git Bash and keep it open
"C:\Program Files\Git\bin\bash.exe" --login -i "git_commands.sh"
