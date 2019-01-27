"""
Collect a floating point from the user.if the user doesn't give
number,say "Thank you",otherwise  print out the number,multiplied by two
"""

number_string1 = raw_input("Give number for calculation = ")

try :
     number1 = float(number_string1)
except ValueError :
     print "Thank you!"
else :
     print "number",number1,"multiplied_2_num",number1*2
