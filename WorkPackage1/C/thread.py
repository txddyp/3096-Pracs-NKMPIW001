#Thread changer for Cheterodyning by txddyp
from os import system as sy
from subprocess import Popen as op
import tempfile as tf


f = open('src/CHeterodyning_threaded.h','r')
filedata = f.readlines()
f.close()

t = input('Enter the number of threads: ')
thread = '#define Thread_Count '+t
filedata[14] = thread + '\n'
newdata = ""

for i in filedata:
  newdata += i

f = open('src/CHeterodyning_threaded.h','w')
f.write(newdata)
f.close()
