char = input("Enter a special character: ")
size = input("Enter the size of the pattern: ")
option = input("Enter option for the pattern: ")


#1 = major upleft to do
#size = 5
if char == "#" or char == "@" or char == "$" or char == "*" or char == "^":
    if size.isnumeric():
        size = int(size)
        for i in range(size):
            for j in range(size):
                if option == "1":
                    if i == j:
                        print("%s" %char,end="")
                    else:
                        print(".",end="")
                elif option == "2":
                    if i == size - j - 1:
                        print("%s"%char,end="")
                    else:
                        print(".",end="")
            print()      
    else:
        print("Wrong input values2.")
else:
    print("Wrong input values.")


#   1 2 3 4
# 1
# 2
# 3
# 4