from operator import itemgetter
d = {}
while True:
    x = input("Input: ")
    if x == "done":
        break
    y,z = x.split()
    if z.isnumeric():
        z = int(z)
        if y in d:
            print("Duplicated player")
            d[y] = z
        else:
            d[y] = z
    else:
        print("Invalid input")

if d:
    gold = max(d.values())
    average = sum(d.values()) / len(d)

else:
    print("No players")



for k,v in sorted(d.items(), key= itemgetter(1), reverse=True):
    if v == gold:
        print(k,"\t",v,"\t","Gold")
    elif v > average:
        print(k,"\t",v,"\t","Silver")
    else:
        print(k,"\t",v)
    