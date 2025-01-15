
a, b, c = input("a, b, c, = ").split()

if (a == "True" or a == "False") and (b == "True" or b == "False") and (c == "True" or c == "False"):
    #"True" == True
    #"False" == False
    #a = bool(a)
    #b = bool(b)
    #c = bool(c)
    t = "True"
    f = "False"
    if a == f and b == f and c == f:
        print("Grant")
    elif a == f and b == f and c == t:
        print("Deny")
    elif a == f and b == t and c == f:
        print("Deny")
    elif a == f and b == t and c == t:
        print("Deny")
    elif a == t and b == f and c == f:
        print("Grant")
    elif a == t and b == f and c == t:
        print("Grant")
    elif a == t and b == t and c == f:
        print("Grant")
    elif a == t and b == t and c == t:
        print("Grant")
else:
    print("Invalid output")


