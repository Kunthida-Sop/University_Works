x = input("Input: ").upper()
if len(x) == 3:
    v = True
    for c in x:
        if not (c =="A" or c == "E" or c == "I" or c == "U" or c == "O"):
            v = False
    if v:
        for i in x:
            for j in x:
                for k in x:
                    if not ( i == j or j == k or k == i):
                        print("%s%s%s" %(i,j,k))     
    else:
        print("Invalid input, valid characters: [\"A\", \"E\", \"I\", \"O\", \"U\"]")
else:
    print("Only three charecters are allowed")