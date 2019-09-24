echo %~dp0
robot --outputdir %~dp0\output  ^
--name robotbase  --variable  name:yangjian  --pythonpath  %~dp0\lib:config ^
--listener  Listener  uitest_base
pause

