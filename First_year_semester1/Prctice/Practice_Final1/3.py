i = 100

while True:
    x = input("Command: ")
    if x == "done 0":
        break
    y,z = x.split()
    if z.isnumeric():
        z = int(z)
        if y == "P":
            earn = z//50
            i+=(z//50)
            print("You earned %s points" %(earn))
            print("Your accumulated points = %d points" %(i))
        elif y == "R":
            if z > i:
                print("Not enough points")
            else:
                i -= z
                print("You redeemed %d points" %z)
                print("Your accumulated points = %d points" %(i))
        else:
            print("Invalid command")
    else:
        print("Invalid command")




