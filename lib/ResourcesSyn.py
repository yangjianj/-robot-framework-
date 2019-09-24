import copy
from robot.libraries.BuiltIn import BuiltIn
from pabot.pabotlib import PabotLib

class ResourcesSyn():
    def __init__(self):
        pass

    def read_resources(self,path = 'filepath'):
        slaves = [{'type':'api','ip':'192.168.100.2','health':'1'},{'type':'api','ip':'192.168.100.1','health':'1'}, \
                  {'type': 'ui', 'ip': '192.168.100.3', 'health': '1'},{'type': 'ui', 'ip': '192.168.100.4', 'health': '1'}
          ]
        return slaves

    def search_device(self,typelist,avialable_devices):
        avialable_devices_cp = copy.deepcopy(avialable_devices)
        suite_devices = []
        for type in typelist:
            for device in avialable_devices_cp:
                if type == device['type']:
                    suite_devices.append(device)
                    avialable_devices_cp.remove(device)
                    break
        if len(suite_devices) == len(typelist):
            return [suite_devices,avialable_devices_cp]
        else:
            return False




