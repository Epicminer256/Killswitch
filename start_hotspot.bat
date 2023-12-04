@echo off
cd %~dp0
set ip=192.168.137.1
set name="KillSwitch (runs on Mobile Hotspot, which needs to be on before running)"
set /p days="How many days? (Leave blank for gold)> "

start "" cmd /c python webserver.py %ip% %days%
cd epicdnschef && start "" cmd /c python dnschef.py -i %ip% --fakeip %ip% --fakeipv6 %ip% --fakedomains toggle.securly.com -l %name%
cd ..
