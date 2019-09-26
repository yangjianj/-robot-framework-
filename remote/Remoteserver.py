from robotremoteserver import RobotRemoteServer
from examplelibrary import ExampleLibrary

server=RobotRemoteServer(ExampleLibrary(), host='0.0.0.0', port=8270)
server.serve()

'''
使用说明：开启remoteserver后可以脚本执行pc上执行remoteserver上的keyword(keyword在remoteserver上被执行)
查看远程库是否已开启：python -m robotremoteserver test http://10.0.0.42:57347
列出远程库: python -m robot.libdoc Remote::http://127.0.0.1:8270 list

引入remoteserver库：Library     Remote   192.168.1.110:8270

'''