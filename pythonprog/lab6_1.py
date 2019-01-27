"""
Ask word from user and print first letter as capital
"""

def Collectword():
    """
    This function return the first letter capital of user string
    :return:
    """
    strings = raw_input("enter word:")
    if not strings:
        print "Thank you"

    return strings

def Displayword():
    strings = Collectword()
    x=strings.capitalize()
    print x


Displayword()