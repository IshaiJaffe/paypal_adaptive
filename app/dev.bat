START "Static_Server" run_static_server.bat
rename %cd%\logs\now.log %date:/=-%-%time::=-%.log
START "BeesMeDevServer" /MIN %cd%\run_dev_server_logged.bat
START "SASS_BeesMe" /MIN %cd%\data\sass.exe --watch media/css
START "Tail" /WAIT %cd%\data\baretail.exe %cd%\logs\now.log
taskkill /F /T /FI "WINDOWTITLE eq BeesMeDevServer*"
taskkill /F /T /FI "WINDOWTITLE eq SASS_BeesMe*"

