"""
The lambda operator or lambda function is a way to create small anonymous functions, i.e. functions without a name.
These functions are throw-away functions, i.e. they are just needed where they have been created.
Lambda functions are mainly used in combination with the functions filter(), map() and reduce().

The general syntax of a lambda function is quite simple:
lambda argument_list: expression

The argument list consists of a comma separated list of arguments
and the expression is an arithmetic expression using these arguments.

"""

f = lambda x, y : x + y
print f(1,1)

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
print Fahrenheit


