from operator import itemgetter
s = {}
def Input ():
    while True:
        x = input("Enter student name and score: ")
        if x == "end 0" or x == "end":
            break
        y,z = x.split()
        if y in s:
            print("Duplicate name!")
        else:
            z = int(z)
            if z >= 0 and z <= 100:
                s[y] = z
            else:
                print("Invalid score!")
Input()
print("List:")        
if s:
    for k,v in sorted(s.items(), key= itemgetter(1),reverse=True):
        print(k,"\t", v)
else:
    print("> empty list!")