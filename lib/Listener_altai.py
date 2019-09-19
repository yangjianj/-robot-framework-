import os
import settings.settings as Settings
from robot.libraries.BuiltIn import BuiltIn

class Listener():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        # get output folder from file _autotest_output (written by run.py)
        with open(os.path.abspath(__file__) + "/../../../../output/_autotest_output") as infile:
            output = infile.readline()
        runlog = os.path.abspath(output + "/" + Settings.RUN_LOG)
        self.runlog = open(runlog, "a")

        # get output folder from file _autotest_testing (written by run.py)
        with open(os.path.abspath(__file__) + "/../../../../output/_autotest_testing") as infile:
            output = infile.readline()
        faillog = os.path.abspath(output + "/" + Settings.FAIL_LOG)
        self.faillog = open(faillog, "a")
        passlog = os.path.abspath(output + "/" + Settings.PASS_LOG)
        self.passlog = open(passlog, "a")

        self.current_suite = None
        self.current_test = None
        self.current_messages = []

    def __del__(self):
        self.passlog.close()
        self.faillog.close()
        self.runlog.close()

    def _is_pabot_autorun(self):
        return False if BuiltIn().get_variable_value('${AUTOTEST_ROBOT_INCLUDED}') == 1 else True

    def start_suite(self, name, attrs):
        self.current_suite = name

    def start_test(self, name, attrs):
        if self._is_pabot_autorun():
            return

        self.current_test = name
        self.current_messages = []

        self.runlog.write(">>> %s | %s\n" % (self.current_suite, self.current_test))
        self.runlog.flush()

    def log_message(self, data):
        if self._is_pabot_autorun():
            return

        self.current_messages.append((data["level"], data["message"]))

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
        self.runlog.flush()

        self.current_messages = []
        self.current_test = None

    def end_suite(self, name, attrs):
        if self._is_pabot_autorun():
            return

        if attrs["status"] == "PASS":
            self.passlog.write("%s\n" % (self.current_suite))
        elif attrs["status"] == "FAIL":
            self.faillog.write("%s\n" % (self.current_suite))
