#!usr/bin/python

"""

conversion.py
Asks the user for number of inches and converts the number
given to centimeters

"""

CM_PER_INCH = 2.54

inches = raw_input("How many inches? ")

try :
    inches = float(inches)
except ValueError :
    pass
else :
    print inches,"inches =",inches * CM_PER_INCH
    print "centimeters"
