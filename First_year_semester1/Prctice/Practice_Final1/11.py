d ={}
while True:
    x = input("Input: ")
    if x == "done":
        break
    y,z = x.split()
    if z.isnumeric():
        z = int(z)
        if y in d:
            d[y] += z
        else:
            d[y] = z
    else:
        print("ERROR")
print("###Summary###")
if d:
    for k,v in d.items():
        print("Total number of %s : %d" %(k,v))
else:
    print("Empty List")