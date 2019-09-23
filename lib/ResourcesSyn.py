import copy
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

    def search_slave(self,typelist,avialable_salves):
        avialable_salves_cp = copy.deepcopy(avialable_salves)
        suite_salves = []
        for type in typelist:
            for slave in avialable_salves_cp:
                if type == slave['type']:
                    suite_salves.append(slave)
                    avialable_salves_cp.remove(slave)
                    break
        if len(suite_salves) == len(typelist):
            return [suite_salves,avialable_salves_cp]
        else:
            return False




