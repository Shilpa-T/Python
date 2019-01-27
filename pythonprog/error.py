"""
error check program,when user accidently provides error input
then the code should through error message and exit the program
"""

number_string1 = raw_input("give me number")

try :
     number1=float(number_string1)
except ValueError :
     print number_string1,"is not good number"
else :
     print number1, "is a good number"
print"Thank you!"