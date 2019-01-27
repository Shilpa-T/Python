"""
The factorial of a number is the product of all the integers from 1 to that number.
For example, the factorial of 6 (denoted as 6!) is 1*2*3*4*5*6 = 720.
Factorial is not defined for negative numbers and the factorial of zero is one, 0! = 1.
"""

def factorial(num):
    """
    To find factorial of number
    :param num:
    :return:
    """
    fact = 1

    if num < 0:
        print "factorial does not exist for neagtive number"
    elif num ==0:
        print "factorial of 0 is 1"
    else:
        for i in range(1,num+1):
            fact= fact*i
        print "factorial",fact

factorial(-2)
factorial(0)
factorial(6)