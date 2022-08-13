#Thread changer for Cheterodyning by txddyp
from os import system as sy
from subprocess import Popen as op
import tempfile as tf

with tf.TemporaryFile() as tempf:
  proc = op(['make','run_threaded'],stdout=tempf)
  proc.wait()
  tempf.seek(0)
  a = tempf.read().decode("utf-8")
  a = list(a.split('\n'))
  tp = a[4]
  tp = tp[32::]

'''
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


sy('make threaded')
sy('clear')
'''
'''
for i in range(5):
  sy('make run_threaded')

print(f'{t} threads were used')
'''

