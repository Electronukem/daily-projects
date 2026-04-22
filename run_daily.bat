@echo off
REM Wait a random 0–1800 seconds (0–30 min) then generate and push
set /a delay=%RANDOM% * 1800 / 32768
echo Waiting %delay% seconds before generating...
timeout /t %delay% /nobreak >nul
python "C:\Users\zatch\github\daily-projects\generate_daily.py"
