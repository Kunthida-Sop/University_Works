x = input("Input: ")
x = int(x)


y = 0



for i in range(x): # 0 1
    for j in range(x): # 0 1
        if i > j: 
           print("0", end="\t")
        else:
            y += 1
            print(y, end="\t")
    print()
