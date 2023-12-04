@echo off
set /p ip="Outward IP To Listed> "
set /p exp="Days till expire (Leave blank for infinite)> "

start "" cmd /c python webserver.py %ip% %exp%
cd epicdnschef && start "" cmd /c python dnschef.py -i %ip% --fakeip %ip% --fakeipv6 %ip% --fakedomains toggle.securly.com,signon.clever.com