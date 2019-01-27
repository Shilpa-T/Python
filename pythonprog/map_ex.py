"""
map() is a function with two arguments:
r = map(func, seq)

The first argument func is the name of a function and the second a sequence (e.g. a list) seq.
map() applies the function func to all the elements of the sequence seq.
It returns a new list with the elements changed by func
"""

def fahrenheit(T):
    """
    function to convert temp in fahrenheit
    :param T:
    :return:
    """
    return ((float(9)/5)*T + 32)

def celsius(T):
    """
    function to convert temp in celsius
    :param T:
    :return:
    """
    return (float(5)/9)*(T-32)

temp = (36.5, 37, 37.5,39)

F = map(fahrenheit, temp)
C = map(celsius, F)



