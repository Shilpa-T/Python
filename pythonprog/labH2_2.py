"""
calculate average number of miles per gallons.
test for all possible errors

"""

x = raw_input("enter the car model ")
y = raw_input(" Enter number of miles driven")
z = raw_input("Enter number of Gallons ")

try:
    Model = str(x)
    Miles = int(y)
    Gallons = int(z)
except ValueError:
    print "Enter the correct values for the car"
    print " Thank you!"
else:
    Average = Miles/float(Gallons)
    print "Car model:",Model
    print "Miles :",Miles
    print "Gallons :",Gallons
    print "Saturn got",Average,"miles per gallons"