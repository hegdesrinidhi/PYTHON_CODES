print("Hello, Welcome to Python");

age1 = 10;
name = 'Mike';
a1 = b1 = c1 = 10;

print("Age is " , age1);
print( "Age is :",a1)
print (a1+b1);

print (name + ","+name);

sentence="This is a line";
print(sentence[0])
print(sentence.capitalize())
print(sentence[0:5])
print(len(sentence[0:5]));
print("name is ",name,"age is",a1)

print('%s Is good and is %d old' % (name, a1));



a=11;
if ( a< 0):
    print ("a is less than 0",a);
elif(a <10):
    print("a is less than 10",a)
elif(a==10):
    print("a is = to 10", a)
else:
    print("a is greater than 10", a)




a=0;
b=1;
n=1000;
print("--" * n);
#n=int(input("Enter n:"));
while (a < n):
    print(a,end=" ");
    a,b=b,a+b;
print();
print("--" * n);


list2=range(1,100,1);
print (len(list2));

for i in list2:
    if (i == 26):
        break;

    if (i==15):
        continue;

    print("Iteration :", i)


words=["this","is","an","word","list"];

for w in words:
    #print(w,len(w));

    if (w=="a"):
        words.insert(0, "new word");
        words.insert(1, "new word");
        break;

    elif(w=="list"):
        #words.insert(0, "new word")
        continue;
    print("Word in the list is :",w);

print("Words list",words);



for w in words[:]:
    print(w,len(w));

    if (w=="an"):
        words.insert(0, "new word");
        words.insert(1, "new word");
        break;

    elif(w=="list"):
        #words.insert(0, "new word")
        continue;
    print("Word in the list is :",w);

print("Words list",words);




print(range(10));
list1=range(10);
print(list1[0    ]);


#functions

fibn=[];
def fib (n):
    d=0;
    e=1;

    while( d < n):
        print(d);
        fibn.append(d);
        d,e=e,d+e;


fib(100);
print ("fib series ",fibn);




def ask(prompt,retries=4,reminder="Please retry!"):
    while (True):
        ok=input(prompt)
        if (ok=='y'):
            return True;
        if (ok=='n'):
            return False;
        retries-=1;
        if (retries <0):
            raise ValueError(reminder);
        print(reminder)

#r=ask("Enter")
#print(r);


#keyword arguments

def keargs(a="this is a",b="This is b"):
    print("Printing A",a);
    print("Printing B", b);

keargs();
keargs(a="Override A");
keargs(b="Override B");
keargs(a="Override A",b="Override B");
keargs(b="Override A",a="Override B");




#list operations

r=range(10);
l=[*r]

print(l);
l.append(10);

print(l);


print("Length", len(l));
l.insert(1,1);
l.insert(len(l),12);
print(l);

l.extend(range(1,11,2));
print(l);

l.remove(1);
print(l);

print(l.pop());
print(l);

print(l.pop(2));
print(l);

print(l.index(3,4));
print(l);


print(l.count(2));
print(l);

l.reverse();
print("reverse:" ,l);

l.sort();
print("Sort",l);




#lambds definition

#list(map(lambda x : x**2, range(10)));


squares = list(map(lambda x: x**2, range(10)))
print (squares);

powers=[x**x for x in range(10)];
print(powers);

exps=[(x,y,x**y) for x in range(1,5,1) for y in range(1,5,1) if(x%y == 0)]
print(exps);

#flattern vectors

vec=[[1,2,3,4],[4,5,6,7]];
vl=[num for le1 in vec for num in le1];
print(vl);



from math import  pi;
pis=[(i,round(pi,i)) for i in range(10)];
print(pis);


#matrix
m=[[1,2,3,4],[5,6,7,8],[9,10,11,12]];

for i in range(4):
    print([row[i] for row in m]);

##equivalent
print([[row [i] for row in m] for i in range(4)]);

#zip function --transponse
print(list(zip(*m)));
print(zip(*m));


a=[0,1,2,3,4,5,6];
b=a;
del  a[0];
print ("Deleted index 0", a);

del  a[3:5];
print ("Deleted range 3:5", a);

del  a[:];
print ("Deleted All ", a);

del  b;
#print ("Deleted All ", b);




#tuples

t=1,2,3,
print("Length of Tuple T",len(t));
t2=t,('x','y');
print("Length of Tuple T2",len(t2));
print("Tuple T2",t2);

v=([1,2],[2,1,0]);
print("Length of Tuple V",len(v));
print("Tuple V",v);
print("Tuple V[0]",v[1][2]);

empty=();
print("Length of Tuple empty",len(empty));


#sets - unordered collection of elements with no duplicates

elements={'apple','orange','banana','jackfruit'};
print("Element set :" ,elements);
print("Length Element set :", len(elements));

dupelements={'apple','orange','banana','jackfruit','apple'};
print("dupelements set :" ,dupelements);
print("Length dupelements set :", len(dupelements))

a=set('abracadabra');
b=set('abacus');
print("Uniqueness - check A", a);
print("Uniqueness - check B", b);

print(" A - B", a - b);
print(" A & B", a & b);
print(" A | B", a | b);
print(" A ^ B", a ^ b);
print("Is x present in A", 'x' in a);
print("Is a present in A", 'a' in a);

y= {x for x in a if x not in 'abc'}
print("Y is :",y);



#dictionary - key value pair
tel={'roy':1234,'ben': 2345};
print("Tel Dictonary :",tel);
tel['mik']=3456;
tel['lin']=4567;
print("Tel Dictonary :",tel);
print("Tel Dictonary of roy :",tel['roy']);
del(tel['lin']);
#tel['mik']=;
print("Tel Dictonary :",tel);
print("Tel Dictonary keys:",list(tel));
print("Tel Dictonary keys - sorted:",sorted(tel));
print('mike' in tel);
print('lin' in tel)

keyPair=dict([('A','a'),('B','b')]);
print("keyPair Dictonary :",keyPair);
keyPair1=dict(A='a',B='b');
print("keyPair1 Dictonary :",keyPair1);

kp1={x:x*2 for x in range(10)};
print("kp1 Dictonary :",kp1);


#looping techniques

#items to hget both key value from dictionary

for m,n in tel.items():
    print ("Key %s & Value %s" % (m,n));
    print(m, n);


for i,j in enumerate(['l','m','n'] ,start=10):
    print(i,j);

a=('A','B','C');
b=(0,1,2);

for p,q in zip(a,b):
    print ("Whats {0}? Which is {1} :) ".format(p,q));


for i in range(0,10,2):
    print(i);

for i in reversed(range(0, 10, 2)):
        print(i);


for x in sorted(tel.keys()):
    print(x);

import  math;
new_array=[]
def mfilter():
    raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8];
    print("raw_data Array :", raw_data);
    for y in raw_data:
        if not math.isnan(y):
            new_array.append(y);


mfilter();
print ("New Array :",new_array);



##input and output


x=10
y='hello'
print ("Value of x is", x)
print ("Value of x {0} with name {1}".format(x, y))
pf=f'Value of x {x}'
print (pf)

print2=f'Value of x using format "f" {x}'
print (print2)

m=1000.1234
n=pi;


print('new format {0} and {1}'.format(n, m));
print('new format {0} and {1}'.format(n, m));
print('{:-9} YES votes  {:2.2%}'.format(n, m))
print('{:-9} YES votes  {:2.2%}'.format(m, n))
print('new format with .format syntax {:-9} for {:2%}'.format(m,n))



##str and repr

print ('str on string ',str(y));
print ('repr on string ',repr(y));
print ('str on float ',str(pi));
print ('repr on float ',repr(pi));


b="hello \n";
print ("Without any formatting",b)
print ('str on string with \n',str(b));
print ('repr on string with \n',repr(b));

##further formating
print(tel);
for name, number in tel.items():
    print(' {:10} ==> {:10}'.format(name, number))
    print(f'{name:10} =====> {number:-10}')



##additional formats
print(f'this is new format with "!r" {b!r}')
print(f'this is new format with "!a" {b!a}')
print(f'this is new format with "!s" {b!s}')
print('this is new format with "!r" {!r}'.format(b))

##.format examples
print(' . format example 1 : {}'.format(b));
print(' . format example 2 : {c}'.format(c=100));
print(' . format example 3 : {} & {}'.format(100,200));
print(' . format example 4 : {0} & {1}'.format(100,200));
print(' . format example 5 : {1} & {0}'.format(100,200));
print(' . format example 6 : {1} & {0} and {c}'.format(100,200,c=math.pi));


##.format with dict
print(tel);
print("roy: {0[roy]:d}".format(tel))
print("roy: {roy:d}".format(**tel))


for x in range(1,11):
    print("{0:2d} {1:3d} {2:4d}".format(x,x*x,x*x*x))


for x in range(1,11):
    print("{0:4d} - {2:4d} - {1:4d}".format(x,x*x,x*x*x))

##right justified
for x in range(1,21,2):
    print(repr(x).rjust(2),repr(x*x).rjust(3),repr(x*x*x).rjust(4))

##left justified
for x in range(1, 21, 2):
    print(repr(x).ljust(2,'-'), repr(x * x).ljust(3,'-'), repr(x * x * x).ljust(4,'-'))

##pad fill 0's
for x in range(1, 21, 2):
    print(repr(x).zfill(5), repr(x * x).zfill(8), repr(x * x * x).zfill(9))


##print f formating
print("This is printf formatiing %2.2f" % pi)
print("This is printf integer formatiing %2.2d" % pi)
print("This is printf string formatiing %2.2s" % pi)


##reading and writing into a file
import os

print(os.getcwd());
print(os.listdir(os.getcwd()));
print("Beginning of file reading")
#with open(r'C:\Users\Srini\Documents\Code\Python\Learningpython\test.csv') as f:
with open(r'C:\Users\srini\Documents\Code\Python\LearningPython\test.csv.txt') as f:
    print(f.read())
print(f.closed)
print("end of file reading")


##another way of reading
f=open(r'C:\Users\srini\Documents\Code\Python\LearningPython\test.csv.txt','r')
print(f.read());
f.close()

print ("reading with for loop -------------------------------------------")
f=open(r'C:\Users\srini\Documents\Code\Python\LearningPython\test.csv.txt','r')
for lines in f:
    print(lines,end =' ')
f.close()
print("\n")
print("Checking file close status",f.closed)



#readline

rl=open(r'C:\Users\srini\Documents\Code\Python\LearningPython\test.csv.txt','r')
print("readline method ",rl.readline())
print("readline method ",rl.readline())
print("file closed status",rl.closed)
rl.close()
print("file closed status",rl.closed)

##write to file


fw=open(r'C:\Users\srini\Documents\Code\Python\LearningPython\test1.csv.txt', 'a+')
fw.write("Third line\n")
fw.seek(0)

print("readline method writing", fw.read())
fw.close()



##handling exception

import sys

def handleExc (id):
    try:
        1/id;
        namesfsfasf/10;
    except ZeroDivisionError as zd:
        print("Zero Division Error {}".format(zd))
    except ValueError as vr:
        print("Value Error : {}".format(vr))
    except NameError as ne:
        print("Name Error : {}".format(ne))
    except TypeError as te:
        print("Type Error : {}".format(te))

    except:
        print("Catch all : {}" ,sys.exc_info())

handleExc(0)
handleExc('hi')
handleExc(100)



def readFile():
    try:
        fh=open(r'C:\Users\srini\Documents\Code\Python\LearningPython\test2.csv.txt', 'r')
    except NameError as ne:
        print("Name Error :",ne)
    except OSError as ose:
        print("File not found Error :", ose)
    else:
        print('file has ',len(fh.readlines()), 'lines')


readFile()


