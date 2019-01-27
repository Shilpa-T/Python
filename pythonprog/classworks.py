"""
classworks.py
"""
number = raw_input("Give me a number")

try:
    number = int(number)
except ValueError:
    print "Never Mind"
else:
    if number % 3 ==0:
        print"number%3 is true with",number
    elif number >100:
        print "number >100 is true",number
    else:
        print "Nice number",number
