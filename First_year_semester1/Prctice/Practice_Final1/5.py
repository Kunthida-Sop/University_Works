while True:
    x = input("Enter an integer number (0 to exit): ")
    if x == "0":
        print("Exit program. Bye!")
        break
    if x.isnumeric():
        x = int(x)
        if x >=0 and x < 10:
            for i in range(x):
                x = int(x)
                print(" "*(x-i-1),end="")
                for j in range(i+1):
                    print("%d "%x,end="")
                print()
            print()
        else:
            print("Valid value is between 0 and 9!")
    else:
        print("Valid value is between 0 and 9!")

    