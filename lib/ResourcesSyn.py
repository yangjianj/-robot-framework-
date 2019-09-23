from robot.libraries.BuiltIn import BuiltIn
from pabot.pabotlib import PabotLib

class ResourcesSyn():
    def __init__(self):
        pass

    def read_resources(self,path = 'filepath'):
        slaves = [{'type':'api','ip':'192.168.100.2','health':'1'},{'type':'api','ip':'192.168.100.3','health':'1'}, \
                  {'type': 'ui', 'ip': '192.168.100.3', 'health': '1'},{'type': 'ui', 'ip': '192.168.100.4', 'health': '1'}
          ]
        return slaves

    def aquire_slave(self,type):
        BuiltIn.wait_until_keyword_succeeds('10 min','2 s','aquire_lock','slave')
