b = int(input("Enter the initial balance: "))
while True:
    z = input("Transaction type and amount (\"done 0\" to exit): ")
    if z == "done 0":
        print("> Current balance = %d THB." %(b))
        break
    x,y = z.split()
    if y.isnumeric():
        y = int(y)
        if x == "D":
            b += y
            print("> Deposit = %d THB, current balance = %d THB." %(y,b))    
        elif x == "W":
            if y > b:
                print("> Invalid transaction!")
            else:
                b-= y
                print("> Withdrawal = %d THB, current balance = %d THB." %(y,b))
        else:
            print("Invalid transaction!")
    else:
        print("Invalid transaction!")