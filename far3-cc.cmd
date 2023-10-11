@echo off
cl ^
-Ox -MD -LD -Fefar3python.dll ^
-D_UNICODE -DUNICODE ^
-Ifar3-include ^
-Iw:\binw\Python-3.12.0.amd64\include ^
far3python.cpp ^
far3python-min.def ^
w:\binw\Python-3.12.0.amd64\libs\python312.lib

copy far3python.dll far3-installed