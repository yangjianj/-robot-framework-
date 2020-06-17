echo %~dp0
pabot --pabotlib  --processes 3 --outputdir  %~dp0\output  ^
--name robotbase  --variable  name:yangjian  --variable  taskid:taskid123456 --pythonpath  %~dp0\lib:config ^
--listener  Listener   --include    para-test  %~dp0\uitest_base
pause

