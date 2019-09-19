import os
import sys
import time
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

class Email():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        # gmail
        #self._send_from = "altai.autotest@gmail.com"
        #self._server = 'smtp.gmail.com'
        #self._port = 587
        #self._username = 'altai.autotest'
        #self._password = '83pe1443'
        # office365
        self._send_from = "firmware@altaitechnologies.com"
        self._server = 'smtp.office365.com'
        self._port = 587
        self._username = 'firmware@altaitechnologies.com'
        self._password = 'Y6T17e0x64hr'

    def send_email(self, emaillog, send_to, subject, text, files=dict()):
        msg = MIMEMultipart(From=self._send_from,
                            Date=formatdate(localtime=True))
        msg['To'] = send_to
        msg['Subject'] = subject
        msg.attach(MIMEText(text))

        for key in sorted(files):
            if os.path.isfile(files[key]):
                with open(files[key], "rb") as ins:
                    msg.attach(MIMEApplication(ins.read(),
                                               Content_Disposition='attachment; filename="%s"' % basename(files[key]),
                                               Name=key + "_" + basename(files[key])))

        # Send the mail
        try:
            smtp = smtplib.SMTP(self._server, self._port)
            smtp.ehlo()
            smtp.starttls()
            smtp.login(self._username, self._password)
            smtp.sendmail(self._send_from, send_to.split(','), msg.as_string())
            smtp.close()
        except:
            print "Email.py: unexpected error! send email failed!!!"
            self.emaillog = open(os.path.abspath(emaillog), "a")
            self.emaillog.write("===Email.py: send email failed!===\n")
            self.emaillog.write(subject + "\n")
            self.emaillog.write(text + "\n")
            self.emaillog.close()

        # sleep 10 seconds s.t. the long email (Finish) would arrive before the next short email (Start)
        time.sleep(10)

if __name__ == '__main__':
    Email(sys.argv[1])