echo %~dp0
pabot --pabotlib --processes 3 --outputdir  D:\yangjian\project\ui-api-robotframework\output  ^
--name robotbase  --variable  name:yangjian  --pythonpath  %~dp0\lib:config ^
--listener  Listener  uitest_base
pause

