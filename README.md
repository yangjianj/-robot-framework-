# -robot-framework-
测试脚本：脚本统一格式  
按需统一suite_setup,teardown   

测试数据：数据与脚本分离  
环境数据与脚本分离  
数据驱动相关脚本的数据存放csv  

测试执行：python脚本根据不同测试策略组装执行命令调度执行  
分块执行不同模块case  
执行过程中监控脚本执行情况  
反馈当前执行case与整体执行进度  

测试log、报告：执行数据统计，突出失败case的log  
rebot组装log  

1.提供不同操作流测试--关键字驱动  (适用操作流程多的测试：UI、网络设备后台自动化)   
2.相同操作流不同数据--数据驱动（模板使用）  （适用同一套操作多种输入数据测试：ui,api自动化）  
3.用例分类规划：tag casename suitename id  
4.执行：脚本调动cmd/shell命令执行pabot并行执行   
5.log收集与结果存储：rebot工具，除robot生成报告外在监听类中加入结果存储处理，将测试结果存储到数据库    
6.监听事件：--listener参数导入监听库     
7.失败用例收集：listener库方法记录异常用例并输出收集    
8.异常防范：case级超时，suite级超时,keyword级超时        
9.pabot并行执行并行执行资源锁+同步的使用    
10.分布式执行解决方案：remote库/ssh库/rabbitmq/运行web服务    
11.日志查看-同suite各版本日志关联:版本/suitepath/suite.log--time    

###ui自动化实现：  
1.yml管理页面元素信息    
2.支持数据驱动和关键字驱动    
3.数据驱动中csv文件管理输入数据信息    

###api自动化实现：    
1.csv文件存储用例信息    


###学习点：
1.关于robot api的使用：    
 1.1github地址：https://github.com/robotframework/robotframework/blob/v3.1.1/src/robot/libraries/BuiltIn.py    
 1.2文档：https://robot-framework.readthedocs.io/en/v3.1.1/autodoc/robot.libraries.html#module-robot.libraries.BuiltIn   
 1.3可通过纯python代码引入关键字库实现用例；python实现的扩展库可引用robot库实现相应功能,例如listener类中使用BuiltIn().set_suite_variable()    
2.robot的分布式测试库-Remote;pabot分布式库使用    
3.listener使用的想法：  
 3.1记录用例状态到本地/数据库      
 3.2提送当前执行状态到指定监控平台    
4.robot脚本中python调用    
5.

Python自动化框架对比：https://www.jianshu.com/p/b87ec158aad8    