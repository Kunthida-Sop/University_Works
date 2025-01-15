from math import *
radius = input("Enter the radius of the capsule (in meters): ")
radius = float(radius)
height = input("Enter the height of the middle cylinder (in meters): ")
height = float(height)
surface_area = (2*pi*(radius**2))+(2*pi*radius*height)+(2*pi*(radius**2))

volume = (pi*(radius**2))*(((4/3)*radius)+height)

print("The volume of the capsule is %.4f cubic meters" %(volume))
print("The surface area of the capsule is %.4f square meters" %(surface_area))