echo %~dp0
pabot --pabotlib  --processes 3 --outputdir  %~dp0\output  ^
--name robotbase  --variable  name:yangjian  --pythonpath  %~dp0\lib:config ^
--listener  Listener    --suite  suite1  %~dp0\uitest_base\parallel_test
pause

