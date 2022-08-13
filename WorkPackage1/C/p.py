#Thread changer for Cheterodyning by txddyp
from os import system as sy
from subprocess import Popen as op
import tempfile as tf
from time import sleep as sl

def reader():
  with tf.TemporaryFile() as tempf:
    proc = op(['make','run_threaded'],stdout=tempf)
    proc.wait()
    tempf.seek(0)
    a = tempf.read().decode("utf-8")
    a = list(a.split('\n'))
    tp = a[4]
  return tp[30::]

def main():
  f = open('src/CHeterodyning_threaded.h','r')
  filedata = f.readlines()
  f.close()

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

  top = f"Results obtained from multithreading using {t} threads..."
  tp = ""
  for i in range(3):
    rp = reader()
    sl(0.5)
    tp = tp +f"\nrun {i+1} with time = " +rp
  top+=tp
  top+= '\n'

  with open("results.txt","a") as text_file:
    text_file.write(top + "\n")

if __name__ == '__main__':
  lev = ['16'] #,'4','8','16','32']
  for t in lev:
    main()
    sl(10)
