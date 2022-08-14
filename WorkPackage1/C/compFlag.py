#CFlags changer for makefile by txddyp
f = open('makefile','r')
filedata = f.readlines()
f.close()

t = input("Enter the compiler flag: ")
flag = 'CFLAGS = '+t
filedata[2] = flag + '\n'
newdata = ""

for i in filedata:
  newdata += i

f = open('makefile','w')
f.write(newdata)
f.close()
