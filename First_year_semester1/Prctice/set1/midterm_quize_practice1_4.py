import random as r

w = input("Rectangle widh: ")
h = input("Recangle height: ")
t = input("Border thickness: ")

a = ["$","#","*"]

w = int(w) #3
h = int(h) #3
t = int(t) #1
c = 0

for i in range(w):# 0 1 2
    for j in range(h): # 0 1 2
        if j < t or j >= w-t or i < t or i >= h-t:
           o = r.choice(a)
           print(o,end="")

        
        else:
            print(" ",end="")
    print()


        
        
            