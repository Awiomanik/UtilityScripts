@echo off

:start_script
cls
:: Ask the user for the desired time
set /p "desired_time=Enter the desired time (HH:MM:SS), [e]xit the programm or [s]hutdown imidietly: "
if "%desired_time%" == "e" exit
if "%desired_time%" == "s" shutdown /s /f & exit

:: Use subroutine to calculate remainning time
CALL :Calculations
:: Set s for first iteration of :clock loop
set /a s=0
:: initiate shutdown
shutdown /s /t %seconds_to_desired_time%

:: Output the result (in a loop)
:clock
    :: reloading current time
    IF %s% == 0 CALL :Calculations
    :: convertion   
    set /a h=seconds_to_desired_time/3600
    set /a remaining_seconds=seconds_to_desired_time%%3600
    set /a m=remaining_seconds/60
    set /a s=remaining_seconds%%60

    cls
    echo Shutdown at: %desired_time%
    echo Time left:   %h%:%m%:%s%
    echo.

    echo Options:
    echo [E]exit window (Note that the scheduled shutdown will occur even though the window is closed)
    echo [C]ancel scheduled shutdown
    :: /C - Specifies the list of choices to be created. Default list for English versions is YN
    :: /N - Hides the list of choices in the prompt. The message before the prompt is displayed and the choices are still enabled.
    :: /T - Timeout in seconds
    :: /D - Default value
    :: /M - Message to display
    CHOICE /C:ECD /N /T 1 /D D
    IF %ERRORLEVEL% == 1 EXIT
    IF %ERRORLEVEL% == 2 shutdown /a & GOTO start_script
    IF %ERRORLEVEL% == 3 echo.

    set /a seconds_to_desired_time-=1
    if %h%:%m%:%s% == 0:0:1 exit
    goto clock

:: Subroutine:
:Calculations
:: Check current time
set curr_time=%time%
:: Calculate the amount of seconds to the desired time
set /a desired_time_seconds=%desired_time:~0,2%*3600+%desired_time:~3,2%*60+%desired_time:~6,2%
set /a current_time_seconds=%time:~0,2%*3600+%time:~3,2%*60+%time:~6,2%
if %current_time_seconds% GTR %desired_time_seconds% set /a desired_time_seconds += 86400
set /a seconds_to_desired_time=desired_time_seconds-current_time_seconds
EXIT /B