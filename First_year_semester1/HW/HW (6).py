import numpy as np


def Distance(p1,p2):
    d = np.sqrt(np.sum((p1-p2)**2))
    return d

round = 1
m = []
sd = 0
c = False

while True:
    x = input("P%d: " %round)
    if x.lower() in "end":
        break
    try:
        y = []
        for i in x.split():
            i = float(i)
            y.append(i)
        if len(y) == 3:
            m.append(np.array(y)) 
            round += 1  

    except ValueError:
        continue

if len(m) < 2:
    print("There are fewer than two points. There is no distance output.")

if len(m) >= 2:
    print("There are %d points in total." %(round-1))
    for i in range(1,len(m)):
        d = Distance(m[i-1],m[i])
        sd += d
        print("P%d -> P%d = %.2f" %(i,(i+1),d))
    print("Total distance is %.2f units." %(sd))


