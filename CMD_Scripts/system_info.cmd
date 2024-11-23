:: This CMD script provides you with your operating system, hardware and network information.
@ECHO OFF
TITLE My System Info
ECHO Curret ate and time: %DATE% %TIME%
ECHO.
ECHO Gathering system information.
SET line====================================================================================
SETLOCAL ENABLEDELAYEDEXPANSION

ECHO %line%
ECHO OPERATING SYSTEM:
systeminfo | findstr /c:"OS Name"
systeminfo | findstr /c:"OS Version"
ECHO.

ECHO %line%
ECHO BIOS:
systeminfo | findstr /c:"System Type"
ECHO.

ECHO %line%
ECHO MEMORY:
systeminfo | findstr /c:"Total Physical Memory"
ECHO.

ECHO %line%
ECHO CPU Name:
FOR /f "skip=1 tokens=* delims=" %%x IN ('wmic cpu get name') DO @echo|set /p cpu=%%x
ECHO.
ECHO. 

ECHO %line%
ECHO SYSTEM UPTIME:
:: Get the last boot time
FOR /F "tokens=1 delims=." %%A IN ('wmic os get lastbootuptime ^| find "."') DO (
    SET lastboot=%%A
)
SET bootYear=%lastboot:~0,4%
SET bootMonth=%lastboot:~4,2%
SET bootDay=%lastboot:~6,2%
SET bootHour=%lastboot:~8,2%
SET bootMinute=%lastboot:~10,2%
SET bootSecond=%lastboot:~12,2%
:: Get the current time
FOR /F "tokens=2 delims==" %%A IN ('wmic os get localdatetime /value') DO (
    SET now=%%A
)
SET currYear=%now:~0,4%
SET currMonth=%now:~4,2%
SET currDay=%now:~6,2%
SET currHour=%now:~8,2%
SET currMinute=%now:~10,2%
SET currSecond=%now:~12,2%
:: Convert times to seconds since midnight for simplicity
SET /A bootTotalSeconds=(1%bootHour%-100)*3600 + (1%bootMinute%-100)*60 + (1%bootSecond%-100)
SET /A currTotalSeconds=(1%currHour%-100)*3600 + (1%currMinute%-100)*60 + (1%currSecond%-100)
:: Calculate the time difference in seconds
SET /A elapsedSeconds=currTotalSeconds - bootTotalSeconds

:: If the day has changed, adjust for 24-hour day rollover
IF !elapsedSeconds! LSS 0 (
    SET /A elapsedSeconds+=86400
)
:: Convert the elapsed time to hours, minutes, and seconds
SET /A elapsedHours=elapsedSeconds / 3600
SET /A elapsedMinutes=(elapsedSeconds %% 3600) / 60
SET /A elapsedSeconds=elapsedSeconds %% 60
:: Display the result
ECHO Last boot time: %lastboot:~0,4%-%lastboot:~4,2%-%lastboot:~6,2% ^
%lastboot:~8,2%:%lastboot:~10,2%:%lastboot:~12,2% ^
(%elapsedHours% hours, %elapsedMinutes% minutes, %elapsedSeconds% seconds ago)
ECHO.

ECHO %line%
ECHO HOSTNAME AND USERNAME:
ECHO Hostname: %COMPUTERNAME%
ECHO Username: %USERNAME%
ECHO.

ECHO %line%
ECHO NETWORK ADDRESS:
ipconfig | findstr IPv4
ipconfig | findstr IPv6
ECHO Network adapters: 
wmic nic where "NetEnabled=True" get Name, MACAddress

ECHO %line%
ECHO DISK INFORMATION:
wmic logicaldisk get name,freespace,size

ECHO %line%
ECHO GRAPHICS CARD:
wmic path win32_videocontroller get name

ECHO %line%
ECHO BATTERY STATUS:
FOR /F "tokens=2 delims==" %%A IN ('wmic path win32_battery get EstimatedChargeRemaining /format:list 2^>nul ^| find "="') DO (
    IF NOT "%%A"=="" SET "battery=%%A"
)
IF NOT DEFINED battery (
    ECHO No battery detected.
) ELSE (
    ECHO Remaining Charge Percentage: !battery!
)
ECHO.

ECHO %line%
ENDLOCAL
PAUSE

IF ERRORLEVEL 1 (
    ECHO Failed to retrieve some information. Ensure you have the required permissions.
)
