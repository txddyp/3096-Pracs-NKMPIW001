#Thread changer for Cheterodyning by txddyp
from os import system as sy
from subprocess import Popen as op
import tempfile as tf

def reader():           #Reading the multiline console output and then choosing the runtime
  with tf.TemporaryFile() as tempf:
    proc = op(['make','run_threaded'],stdout=tempf)
    proc.wait()
    tempf.seek(0)
    a = tempf.read().decode("utf-8")
    a = list(a.split('\n'))
    tp = a[4]
  return tp[32::]

top = f"Results obtained from multithreading..."    #this section appends data to a text file
tp = ""
for i in range(3):
  rp = reader()
  tp = tp +f"\nrun {i+1} with time = " +rp
top+=tp
top+= '\n'

with open("results.txt","a") as text_file:
  text_file.write(top + "\n")

  sy('clean')
