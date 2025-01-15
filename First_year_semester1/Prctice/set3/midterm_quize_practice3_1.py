import math as m
a = input("Input diameter: ")
b = input("Input unit diameter: ")
c = input("Input unit area: ")

a = float(a)

if b ==  "mm" :
    a = a*1
elif b == "in":
    a = a*24.5
elif b == "cm": 
    a = a*10

area = m.pi * (a**2)




print("The surface of a circle with a %.2f %s diameter is %.2f square %s." %(a,b,area,c))
