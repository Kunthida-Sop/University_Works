from operator import itemgetter
s = {"ce":0,
     "che":0,
     "ec":0,
     "ie":0,
     "me":0}
grade = []
name = []
sub = []
while True:
    a = input("Input: ")
    if a == "done":
        break
    b,c,d = a.split()
    try:
        d = float(d)
        if d >= 0.00 and d <= 4.00:
            if c in s:
                s[c] += 1
                grade.append(d)
                name.append(b)
                sub.append(c)
            else:
                print("ERROR")       
        else:
            print("ERROR")
    except ValueError:
        print("ERROR")

print("----SUMMARY----")
print("ce = %d" %s["ce"])
print("che = %d"%s["che"])
print("ec = %d"%s["ec"])
print("ie = %d"%s["ie"])
print("me = %d"%s["me"])
print("----LIST----")
if name:
    for i,j,k in sorted(zip(name,sub,grade) ,key=itemgetter(2),reverse=True ):
        print(i,j,"%.2f" %k)
else:
    print("The list is empty")
    
