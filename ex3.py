import os;
os.getcwd()
line='';
with open ('C:\\Users\\srini\\Documents\\Code\\Synechron-Udemy_learning\\Python\\ex3.txt', mode='r') as f:
    con=f.readlines()
    #line=c.join(con)

for item in con:
    #print(item)
    #print(item.__len__())
    i=0
    j=9
    while i<81:
        #print(item[i:j])
        # print(item)
        # print(item.__len__())
        # print(item[0])
        # print(item[77])
        # print(item[78])
        # print(item[79])
        # print("80 is :" + item[80])
        #c=item[74:80]+item[0]
        #print("iiiii : " + item[0:2])
        #print(c)
        #exit(2)
        if (i >73):
            x=80-i ##6,5,4,3,2,1
            y=7-x  #1,2,3,4,5,6
            #print(x)
            #print(y)
            #print(item[i:80])
            c=item[i:80]+item[0:y] ##74:6, 0:1
            #print("> 74: " + c)
        else:
            c = item[i:j]

        #print(c)
        #exit(3);

        #print(c)
        #print(c[0:3])
        #print(c[4:7])
        #exit(2)
        #print(c)
        if ((ord(c[0]) >= 65 and ord(c[0])<=90) and (ord(c[1]) >= 65 and ord(c[1])<=90) and (ord(c[2]) >= 65 and ord(c[2])<=90)
                and (ord(c[4]) >= 65 and ord(c[4])<=90) and (ord(c[5]) >= 65 and ord(c[5])<=90)
            and (ord(c[6]) >= 65 and ord(c[6]) <= 90) and (ord(c[3]) >= 97 and ord(c[3])<=122)):
            #print(c[0])
            #print(c)
            print(c[3])
            #print(item)
            #print(item)
            #if (c[0:3].__eq__(c[4:7])):
            if ((c[0] == c[4]) and (c[1]== c[5]) and (c[2] == c[6])):
                #print(item)
                #print(c)
                print()
                #print(c[0:3])
                #print(c[4:7])

        i=i+1
        j=j+1
    #exit(2)
