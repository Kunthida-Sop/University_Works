rate = []
money = []
emoney = []
m = {
    "JPY":0.29,
     "USD":31.99,
     "EUR":35.62
     }

while True:
    x = input("Input: ")
    if x == "end":
        break
    y,z = x.split()
    if y in ["JPY","USD","EUR"]:
        try:
            z = float(z)
            if z > 0:
                rate.append(y)
                money.append(z)

            else:
                print("ERROR")
                continue
        except:
            print("ERROR")
            continue
    else:   
        print("ERROR")
#print(rate)
#print(money)

for i in range(len(rate)):
    currency = rate[i]
    amount = money[i]
    converted_amount = amount * m[currency]
    print("%.2f %s is %.2f THB" %(amount,currency,converted_amount))



        