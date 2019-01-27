"""
Program manipulating addition,Substraction,Multiplication,
Division and Modules of two integer number and program
should handle if second number is 0.
"""

first_opernd  = int(raw_input("Enter first operand value ="))
sec_operand = int(raw_input("enter second operand value ="))

try :
    div = first_opernd / sec_operand
    Modulus = first_opernd % sec_operand

except ZeroDivisionError :
    print "enter second operand value other than zero"
else :
    print "Div = ",div
    print "Modulus = ",Modulus
Add = first_opernd + sec_operand
sub = first_opernd - sec_operand
Mul = first_opernd * sec_operand

print "Add = ",Add
print "sub = ",sub
print "Mul = ",Mul