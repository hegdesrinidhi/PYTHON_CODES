import urllib.request
import re

html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php").read().decode()
#print(html)
x=re.findall("=[0-9]+", html)
print(x)
newhtml="http://www.pythonchallenge.com/pc/def/linkedlist.php?"+x[0];
print(newhtml)
#exit(4)
i=0
while i<398:
    html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+x[0]).read().decode()
    #print(html)
    x = re.findall("[0-9]+", html)
    if x.__len__()==0 :
        print (html)
        exit(10)
    print(x)
    print(i)
    i=i+1

print(x)
exit(2)
#data = re.findall("<!--(.*)-->", html, re.DOTALL)[-1]
print(data)
exit
#print(data)

print(re.findall("[A-Z]{3}([a-z])[A-Z]{3}", data))
print(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data))
print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data)))

