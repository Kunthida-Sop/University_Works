from operator import itemgetter
def Print():
    print("List:")

d = {}
while True:
    x = input("Enter student ID and score: ")
    if x == "done 0":
        break
    y,z = x.split()
    if y.isnumeric() and z.isnumeric():
        if len(y) == 4:
            z = int(z)
            if z >=0 and z <= 100:
                if y in d:
                    print("The ID is already recorded!")
                else:
                    d[y] = z
            else:
                print("Invalid ID format!")
        else:
            print("Invalid ID format!")
    else:
        print("Invalid ID format!")
if d:
    student = len(d)
    average = sum(d.values())/len(d)
    Print()
    for k,v in sorted(d.items(),key=itemgetter(0)):
        print(k,"\t",v)
    print("There are %d student(s). The average score is %.2f points." %(student,average))

else:
    Print()
    print("> no score is recorded!")

