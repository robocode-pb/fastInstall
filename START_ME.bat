@echo off

color 4

:: Перевірка наявності winget
winget --version >nul 2>&1
if %errorLevel% neq 0 (
    echo !!!! Winget is not installed. Please install it first. !!!!
    pause
    exit /b
)

:: Перевірка, чи запущено з правами адміністратора
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo !!!! Start as administrator !!!!
    pause
    exit /b
)

color 2
echo Start install
color 0


winget install Google.Chrome
winget install Git.Git
winget install M2Team.NanaZip

winget install Microsoft.VisualStudioCode

::Sctath 3 msstore
winget install 9PFGJ25JL6X3 
::Arduino IDE 1s.18.19 msstore
winget install 9NBLGGH4RSD8 

:: Запхнути папку Arduino в архів є сенс? TODO: перевірити різницю розміру

::Arduino libraries and Ardublock
xcopy %CD%\programs\Arduino C:\Users\%USERNAME%\Documents\Arduino /E /I /H /Y
start "" "%CD%\programs\S4A16\S4A16.exe"

start chrome "https://ai2.appinventor.mit.edu"

winget install Unity.UnityHub
start chrome "https://unity.com/releases/editor/whats-new/2021.3.29"

start chrome "https://editor.construct.net"


winget install Python.Python.3.10

pause
exit

:: установка  esp32
git clone https://github.com/espressif/arduino-esp32.git C:\Users\%USERNAME%\Documents\Arduino\hardware/espressif/esp32
cd C:\Users\%USERNAME%\Documents\Arduino\hardware/espressif/esp32/tools && python get.py

