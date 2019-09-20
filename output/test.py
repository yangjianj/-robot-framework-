import os
#with open("test.txt") as infile:
#    output = infile.readline()

open("test.txt", "a")
os.path.abspath(__file__)
ss = open(os.path.abspath(__file__)+"/../../test.txt",'a')
print(ss)