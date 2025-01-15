import math as m
a, b = input("Please enter two integers: ").split()
s = 0

if a.isnumeric() and b.isnumeric():
    a = int(a)
    b = int(b)
    if (a >= 1 and a <= 30) and (b >= 1 and b <= 30):
        if a > b:
            print("The minimum number is %d" %b)
            print("The maximum number is %d" %a)
            r = range(b,a+1,1)
            a = float(a)
            b = float(b)
            for i in r:
                s += i
                o = m.sqrt(s)
            print("The square root of the summation is %.2f"%o)
        else:
            print("The minimum number is %d" %a)
            print("The maximum number is %d" %b) 
            r = range(a,b+1,1)
            a = float(a)
            b = float(b)
            for i in r:
                s += i
                o = m.sqrt(s)
            print("The square root of the summation is %.2f"%o)
    else:
        print("Invalid Inputs")
else:
        print("Invalid Inputs")



#import math as m
#s = 0
#r = range(a,b+1,1)
#for i in r:
    #s += i  plus all of i before put in square root
    #o = m.sqrt(s)
    #print(o)

#if you directly put m.sqrt(i) before s+=i it will root i one by one then plus, not plus before root