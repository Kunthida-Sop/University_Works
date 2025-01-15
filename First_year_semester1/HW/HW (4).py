c = True
p = []
y = 0
while c:
    x = input("Numbers: ")
    if x == "EXIT" :
        break
    try:
        x = float(x)
        y += x
        p.append("%.2f"%x) 

    except ValueError:
        p.append(x)
        p.remove(x)
    if y > 1000:
        break

if len(p) > 0 and y > 1000:
    z = sorted(p, key=float)

    print("----------")
    print(", ".join(z))
    print("sum = %.2f" %y)
else:
    print("Exit without summary.")