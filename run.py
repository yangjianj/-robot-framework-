import time
import configparser
import subprocess
import config.settings as SETTING

class Runner():
    def __init__(self):
        self.exec_cmd = 'pabot'
        self.current_case = None
        self.runtime = 0
        self.strategy = None
        self.cmd=''

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
        cmd_param["suitedir"] = taskparam["suitedir"]
        cmd_param["variable"] = taskparam["variable"]  #包含变量TASKID listener中需要
        self._build_command(cmd_param)
        self.run()
    
    def _build_command(self,cmd_param):
        #构造robot执行命令
        result = {}
        result["processes"]= " --processes "+cmd_param['processes']
        result["outputdir"] = " --outputdir "+cmd_param['outputdir']
        result["taskname"] = " --name "+cmd_param['taskname']
        result["lib"] = " --pythonpath "+cmd_param['lib']
        result["listener"] = " --listener "+cmd_param['listener']
        result["include"] = " --include "+cmd_param['include']
        result["variable"] = ''
        for k,v in cmd_param['variable']:
            tmp= " --variable "+str(k)+':'+str(v)
            result["variable"] = result["variable"]+tmp
        self.cmd = self.exec_cmd + " --pabotlib "
        for k,v in result:
            self.cmd=self.cmd+v
        self.cmd = self.cmd+ ' '+cmd_param['suitedir']
    

    def run(self):
        run_list = ["pabot","--pabotlib","--processes 3","--outputdir %~dp0\output","--name robotbase",
                    "--variable n name:yangjia","--pythonpath  %~dp0\lib:config","--listener  Listener",
                    "--include  para-test","uitest_base"]
        subprocess.call(self.cmd,creationflags =subprocess.CREATE_NEW_CONSOLE)
        #subprocess.call([self._exec_run] + self._arg + variable + testdir + outputdir + selected + rerun + self._testsuites,shell=True)
    
    def run_by_tag(self):
        #根据tag匹配执行
        pass
    
    def run_by_suite(self):
        #根据suite名匹配执行（文件名，非目录名）
        pass

if __name__ == '__main__':
    Runner().run()
