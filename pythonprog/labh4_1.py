"""
Calculatecentimeter
calculateinches
"""

MOD_CONST = 2.54


def Calculatecentimeters(inches):
    centimeters = MOD_CONST * inches
    return centimeters


def Calculateinches(centimeters):
    inches = centimeters / MOD_CONST
    return inches


length = float(raw_input("Length:"))
value = raw_input("Is that in (i)nches or (c)entimeters")
print(length, value)
if value == 'i':
    print Calculateinches(length)

elif value == 'c':
    print Calculatecentimeters(length)
else:
    print("INvalid inputs")
