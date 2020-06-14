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
        self._build_command(SETTING.PROCESSES,taskparam.outputdir)
    
    def _build_command(self,processes,outputdir,taskname,lib,listener,include,rootdir,variable={}):
        result = {}
        result["process"]= " --processes "+processes
        result["outputdir"] = " --outputdir "+outputdir
        result["taskname"] = " --name "+taskname
        result["lib"] = " --pythonpath "+lib
        result["listener"] = " --listener "+listener
        result["include"] = " --include "+include
        result["variable"] = ''
        for k,v in variable:
            tmp= " --variable "+str(k)+':'+str(v)
            result["variable"] = result["variable"]+tmp
        self.cmd = self.exec_cmd + " --pabotlib "
        for k,v in result:
            self.cmd=self.cmd+v
        self.cmd = self.cmd+ ' '+rootdir
    

    def run(self):
        run_list = ["pabot","--pabotlib","--processes 3","--outputdir %~dp0\output","--name robotbase",
                    "--variable n name:yangjia","--pythonpath  %~dp0\lib:config","--listener  Listener",
                    "--include  para-test","uitest_base"]
        subprocess.call(self.cmd,creationflags =subprocess.CREATE_NEW_CONSOLE)
        #subprocess.call([self._exec_run] + self._arg + variable + testdir + outputdir + selected + rerun + self._testsuites,shell=True)

if __name__ == '__main__':
    Runner().run()
