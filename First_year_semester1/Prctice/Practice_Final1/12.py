print("Welcome to coin deposit machine")
d = {1:0,
     2:0,
     5:0,
     10:0}

while True:
    x = input("Please insert coin: ")
    if x.isnumeric():
        x = int(x)
        if x in d:
            d[x] += 1
            print("You inserted %d baht coin" %x)
        else:
            print("Only 1,2,5 and 10 baht coin are allowed")
    else:
        print("Only 1,2,5 and 10 baht coin are allowed")
    if x == "done":
        break
total_amount = sum(coin * count for coin, count in d.items())

print("<-----Deposit Summary----->")
print("1 baht coins -> %d" %(d[1]))
print("2 baht coins -> %d" %(d[2]))
print("5 baht coins -> %d" %(d[5]))
print("10 baht coins -> %d" %(d[10]))
if d:
    print("Deposit Amount: %d baht" %total_amount)
else:
    print("Deposit Amount: 0 baht")