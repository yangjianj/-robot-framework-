import time
import configparser
import subprocess

class Runner():
    def __init__(self):
        self.current_case = None
        self.runtime = 0
        self.strategy = None

    def _read_strategy(self):
        pass

    def run(self):
        run_list = ["pabot","--pabotlib","--processes 3","--outputdir %~dp0\output","--name robotbase",
                    "--variable n name:yangjia","--pythonpath  %~dp0\lib:config","--listener  Listener",
                    "--include  para-test","uitest_base"]
        subprocess.call(run_list,creationflags =subprocess.CREATE_NEW_CONSOLE)

if __name__ == '__main__':
    Runner().run()
