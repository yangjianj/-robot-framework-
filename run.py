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
        cmd_param= {}
        cmd_param["processes"] = SETTING.PROCESSES
        cmd_param["lib"] = SETTING.LIB
        cmd_param["listener"] = SETTING.LISTENER
        cmd_param["outputdir"] = taskparam["outputdir"]
        cmd_param["taskname"] = taskparam["taskname"]
        cmd_param["include"] = taskparam["include"]
        cmd_param["suitedir"] = taskparam["suitedir"]
        cmd_param["variable"] = taskparam["variable"]
        self._build_command(cmd_param)
        self.run()
    
    def _build_command(self,cmd_param):
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

if __name__ == '__main__':
    Runner().run()
