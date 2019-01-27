"""

Collect numbers and sort them
"""

def Collectnumbers():
    numbers = []
    while True:
        num = raw_input("Enter the number(enter to quit)")
        if not num:
            break
        try :
            num = float(num)
        except ValueError:
            print "enter the correct value"
            continue

        numbers.append(num)
    return numbers

def Collectnumbersandsort():

    numbers = Collectnumbers()
    numbers.sort()
    print "Sorted numbers:",numbers

Collectnumbersandsort()