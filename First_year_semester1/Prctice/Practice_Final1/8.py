from operator import itemgetter
c = {}

while True:
    x = input("Input: ")
    if x == "done":
        break
    if x.isnumeric():
        x = int(x)
        if x >= 0 and x <= 1000:
            if x in c:
                c[x] += 1
            else:
                c[x] = 1
        else:
            print("ERROR")
    else:
        print("ERROR")
print("----SUMMARY----")
if c:
    for k,v in sorted(c.items(),key=itemgetter(0)):
        print(k,v)
else:
    print("The list is empty")
    
    