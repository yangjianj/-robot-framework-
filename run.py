import time
import configparser
import subprocess
import robotRunner.config.settings as SETTING

class Runner():
    def __init__(self):
        self.exec_cmd = 'pabot'
        self.current_case = None
        self.runtime = 0
        self.strategy = None
        self.command=''

    def _read_strategy(self):
        pass
    
    def run_task(self,taskparam):
        #taskparam: 执行任务的必要参数
        cmd_param= {}
        cmd_param["processes"] = SETTING.PROCESSES
        cmd_param["lib"] = SETTING.LIB
        cmd_param["listener"] = SETTING.LISTENER
        cmd_param["outputdir"] = taskparam["outputdir"]
        cmd_param["taskname"] = taskparam["taskname"]
        cmd_param["include"] = taskparam["include"]
        cmd_param["suite"] = taskparam["suite"]
        cmd_param["suitedir"] = taskparam["suitedir"]
        cmd_param["variable"] = taskparam["variable"]  #包含变量TASKID listener中需要
        self._build_command(cmd_param)
        self.run()
        self.log_collection()
    
    def _build_command(self,cmd_param):
        #构造robot执行命令
        command = {}
        command["processes"]= str(cmd_param['processes'])
        command["outputdir"] = cmd_param['outputdir']
        command["taskname"] = cmd_param['taskname']
        command["lib"] = cmd_param['lib']
        command["listener"] = cmd_param['listener']
        command["include"] = cmd_param['include']
        command["suite"] = cmd_param['suite']
        command["variable"] = cmd_param['variable']
        
        self.command = self.exec_cmd + " --pabotlib "
        for k,v in cmd_param['variable'].items():
            tmp= " --variable "+str(k)+':'+str(v)
            self.command = self.command+tmp
        
        for k,v in command.items():
            if v == '' or v == None:
                continue
            if k == "variable":
                for vk,vv in command['variable'].items():
                    tmp = " --variable " + str(vk) + ':' + str(vv)
                    self.command = self.command + tmp
            else:
                self.command=self.command+" --"+k+" "+str(v)
        self.command = self.command+ ' '+cmd_param['suitedir']
    
    def log_collection(self):
        #对执行后生成的log文件处理
        pass
    

    def run(self):
        run_list = ["pabot","--pabotlib","--processes 3","--outputdir %~dp0\output","--name robotbase",
                    "--variable n name:yangjia","--pythonpath  %~dp0\lib:config","--listener  Listener",
                    "--include  para-test","uitest_base"]
        print(self.command)
        subprocess.call(self.command,creationflags =subprocess.CREATE_NEW_CONSOLE)
        #subprocess.call([self._exec_run] + self._arg + variable + testdir + outputdir + selected + rerun + self._testsuites,shell=True)
 

if __name__ == '__main__':
    taskparam={}
    runner= Runner()
    runner.run_task(taskparam)
