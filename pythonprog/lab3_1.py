"""
Collect number from given user,if user doesnt give a number,ask
again and again until the user give one.then ask for user name.
"""

while True :
    number = raw_input("Give me a number :")
    if number == '':
        continue
    try:
        number = int(number)
        name = raw_input("Enter your name")

    except ValueError:
        print " Enter correct values"
    else:
        if name == '' or number !='':
            break
print "Thank you for the", number, name