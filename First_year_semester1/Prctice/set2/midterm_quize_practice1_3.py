x = input("Input: ")

#input(1a3432)
p = "*"

for i in x: #x = 1a3432
    if i.isnumeric():
        i = int(i)
        for j in range(i): #1a3432
            if (j+1) % 3 == 0 : #1 2 3 4 5 6
                p = "#"
            else:
                p = "*"
            print(p,end="")
    print()




