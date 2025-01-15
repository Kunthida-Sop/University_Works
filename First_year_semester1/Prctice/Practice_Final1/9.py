l = ["x","o"]
c = 0
y = []
while True:
    x = input("Input: ")
    c +=1
    if x not in l:
        print("Wrong input")
        break
    else:
        y.append(x)
    if c == 9:
        break
#print(y)
for i in range(0,9,3):
    print("-------")
    print("|%s|%s|%s|" %(y[i],y[i+1],y[i+2]))

print("-------")
