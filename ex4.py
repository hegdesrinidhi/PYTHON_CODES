import os
import glob
import re
os.chdir("C:\\Users\\srini\\Downloads\\channel")
print(os.getcwd())

txtfiles = []
for file in glob.glob("*.txt"):
    txtfiles.append(file)

txtfiles.remove('readme.txt')
#print(txtfiles.__len__())

for f in txtfiles:
    break;
    #print(f.replace('.txt',''))
    num=int(f.replace('.txt',''))
    if (num == 'readme'):
        continue
    #print(num)
    if (num > 90052):
        with open(f,'r') as fh:
            print(fh.read())

loop=True
f=''
with open('90052.txt','r') as f1:
    f=f1.read();

print(f)

x=re.findall("[0-9]+",f)
print(x)

#print(f1.)
while (True):
    with open(x[0]+".txt") as nw:
        f=nw.read()
    print(f)
    x = re.findall("[0-9]+", f)
    if (x.__len__() == 0):
        print(f)
        break
    print(x)
    exit

