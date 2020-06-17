import os
from robot.libraries.BuiltIn import BuiltIn
import settings as Settings
from DataManager import DataManager

class Listener():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self):
        # get output folder from file _autotest_output (written by run.py)
        outputdir = os.path.abspath(__file__)+"/../../output/"
        self.runlog = open(outputdir + "/" + Settings.RUN_LOG, "a")

        faillog = os.path.abspath(outputdir + "/" + Settings.FAIL_LOG)
        self.faillog = open(faillog, "a")
        passlog = os.path.abspath(outputdir + "/" + Settings.PASS_LOG)
        self.passlog = open(passlog, "a")

        self.current_suite = None
        self.current_test = None
        self.current_messages = []
        self.datamanager = DataManager()

    def __del__(self):
        self.passlog.close()
        self.faillog.close()
        self.runlog.close()

    def _is_pabot_autorun(self):
        return False
        #return False if BuiltIn().get_variable_value('${AUTOTEST_ROBOT_INCLUDED}') == 1 else True

    def start_suite(self, name, attrs):
        print("############start suite%s:"%(name))
        self.current_suite = name

    def start_test(self, name, attrs):
        print("#######start test:%s"%(name))
        if self._is_pabot_autorun():
            return

        self.current_test = name
        self.current_messages = []

        print(">>> %s | %s\n" % (self.current_suite, self.current_test))
        self.runlog.write(">>> %s | %s\n" % (self.current_suite, self.current_test))
        self.runlog.flush()

    def log_message(self, data):
        print("#############in log_message")
        print(data)
        print("xxxxxxxxxxxxxxxx")
        #
        if self._is_pabot_autorun():
            return

        # self.current_messages.append((data["level"], data["message"]))
        # self.current_messages.append(data)

    def message(self,message):
        pass

    def end_test(self, name, attrs):
        # extract tid from TEST TAGS
        BuiltIn().set_suite_variable('${PREV TEST TID}', "notid")
        for tag in BuiltIn().get_variable_value('${TEST TAGS}'):
            if tag[0] == 't' and tag[1] == 'i' and tag[2] == 'd' and tag[3] == '-':
                BuiltIn().set_suite_variable('${PREV TEST TID}', tag)
                break

        if self._is_pabot_autorun():
            return

        for (level, message) in self.current_messages:
            if level == "ERROR":
                self.runlog.write("| %s | %s | %s\n" % (self.current_suite, self.current_test, message))
            elif level == "WARN":
                self.runlog.write("| %s | %s | %s\n" % (self.current_suite, self.current_test, message))

        self.runlog.write("<<< %s | %s\n" % (self.current_suite, self.current_test))
        self.passlog.write("in end test-: {0},{1}".format(attrs.status,attrs.elapsedtime))
        self.runlog.flush()
        self.current_messages = []
        self.current_test = None

    def end_suite(self, data, result):
        if self._is_pabot_autorun():
            return
        self.passlog.write("123456788900-")
        self.passlog.write("{0}\n".format(str(data)))
        self.passlog.write("{0}\n".format(str(result.status)))
        # if attrs["status"] == "PASS":
        #     self.passlog.write("%s\n" % (self.current_suite))
        # elif attrs["status"] == "FAIL":
        #     self.faillog.write("%s\n" % (self.current_suite))
        '''
        if(len(attrs["tests"]) != 0):
            msg={}
            msg["taskid"] = BuiltIn().get_variable_value("${TASKID}")
            msg["caseid"] = name
            msg["status"] = attrs["status"]
            msg["starttime"]= attrs["starttime"]
            msg["endtime"]= attrs["endtime"]
            msg["elapsedtime"]= attrs["elapsedtime"]
            self.datamanager.save_robot_suite_result(msg)
        '''

    def start_keyword(self,name,attributes):
        pass

    def end_keyword(self,name,attributes):
        pass

    def output_file(self,path):
        pass

    def report_file(self,path):
        pass

    def log_file(self,path):
        pass

    def debug_file(self,path):
        pass

    def close(self):
        pass