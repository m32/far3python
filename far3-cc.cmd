@echo off
cl ^
-Ox -MD -LD -Fefar3python.dll ^
-D_UNICODE -DUNICODE ^
-Ifar3-include ^
-Iw:\binw\Python-3.9.13.amd64\include ^
far3python.cpp ^
far3python-min.def ^
w:\binw\Python-3.9.13.amd64\libs\python39.lib

copy far3python.dll W:\binw\far3-amd64-profile\Plugins\x64\python
