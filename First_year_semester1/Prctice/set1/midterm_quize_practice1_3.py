customer = input("Input (Number of customers): ")
code = input("Input (Discount code): ")
customer = int(customer)
if customer >= 1 and customer <=3:
    price = 399
elif customer >= 4 and customer <=6:
    price = 499
elif customer > 6 :
    price = 599

if code == "CASH":
    x = 5/100
    y = "5%"
elif code == "BIRTHDAY":
    x = 10/100
    y = "10%"
elif code == "COVID":
    x = 30/100
    y = "30%"
elif code == " ":
    x = 0
    y = "0%"

sub = price * customer
total = sub - (sub*x)
print("%s person x %.2f bath" %(customer, price))
print("A subtotal price is %.2f bath" % sub)
print("On-top discount %s" %y)
print("A total price is %.2f bath" %total)


