import math

def circle_parameter(radius):
    circumference= 2*math.pi * radius
    Area = math.pi *radius**2
    return circumference,Area


radius = float(raw_input("Enter the radius:"))
circum,area = circle_parameter(radius)

print "circumference =",circum,"Area =",area
