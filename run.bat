echo %~dp0
robot --outputdir D:\yangjian\project\ui-api-robotframework\report  ^
--name robotbase  --variable  name:yangjian  --pythonpath  %~dp0\lib ^
--listener  Listener  uitest_base
pause

