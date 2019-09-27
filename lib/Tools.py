#-*-coding:utf-8-*-
from robot.libraries.Remote import Remote
class Tools():
    def __init__(self):
        pass

    def tt1(self):
        print(1234)
        print(Remote().acquire_lock('1','2'))
if __name__ == '__main__':
    for i in Remote.__dict__:
        print(i)


