@echo off
REM Horcrux Interactive Mode Launcher
REM This batch file launches the Horcrux interactive CLI for easy use
REM No technical knowledge required - just double-click to run!

REM Set console colors and title
title Horcrux - File Encryption Tool
color 0F

REM Check if hrcx is installed globally
where hrcx >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    REM hrcx is installed globally, run it directly
    hrcx interactive
    goto :end
)

REM Check if we have a virtual environment in the current directory
if exist ".venv\Scripts\hrcx.exe" (
    REM Use the local virtual environment
    .venv\Scripts\hrcx.exe interactive
    goto :end
)

REM Check if we have a venv directory (alternative name)
if exist "venv\Scripts\hrcx.exe" (
    REM Use the local venv
    venv\Scripts\hrcx.exe interactive
    goto :end
)

REM If we get here, hrcx is not found
echo.
echo ============================================
echo   ERROR: Horcrux (hrcx) not found!
echo ============================================
echo.
echo Please install hrcx first:
echo.
echo   1. Install globally:
echo      pip install hrcx
echo.
echo   2. Or install in a virtual environment:
echo      python -m venv venv
echo      venv\Scripts\activate
echo      pip install hrcx
echo.
echo After installation, run this file again.
echo.
pause
exit /b 1

:end
REM Keep the window open if there was an error
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ============================================
    echo Press any key to close this window...
    pause >nul
)
