@echo off
setlocal
cd /d "%~dp0"
title Build MInstAll Pro

python --version >nul 2>&1
if errorlevel 1 (
  echo Python chua duoc cai hoac khong co trong PATH.
  pause
  exit /b 1
)

python -m pip install --upgrade pip
python -m pip install pillow pyinstaller

rmdir /s /q build 2>nul
rmdir /s /q dist 2>nul

python -m PyInstaller ^
  --clean ^
  --noconsole ^
  --onefile ^
  --name "MInstAllPro" ^
  --icon "app.ico" ^
  --add-data "icons;icons" ^
  --add-data "app.ico;." ^
  --add-data "app.png;." ^
  "MInstAllPro.py"

echo.
echo DONE! File EXE nam trong thu muc dist
pause
