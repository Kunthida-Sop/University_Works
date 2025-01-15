import math as m
shape = input("Input a shape T/S/C: ")
length = input("Input a length: ")

if shape == "T" or shape == "S" or shape == "C":
    1+1
else:
    print("Type must be only T/S/C.")    

if length.isnumeric():
    if shape == "T" or shape == "S" or shape == "C":    
        if length.isnumeric():
            length = float(length) 
            if shape == "T":
                type = "triangle"
                area = 1/2 * length * (length/2)
                print("The surface area of %s is %.2f" %(type,area))
            elif shape == "S":
                type = "square"
                area = (length**2)/2
                print("The surface area of %s is %.2f" %(type,area))
            else :
                type = "circle"
                area = m.pi * (length/2)**2
                print("The surface area of %s is %.2f" %(type,area))
else:
    print("Length must be more than or equal to zero.")     
#else:
#    print("Type must be only T/S/C.")

#print("The surface area of %s is %.2f" %(type,area))
