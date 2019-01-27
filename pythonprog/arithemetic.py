"""
arithemetic.py :Demontrates sum,sub,modulo
"""

def DoArithmetic(x,y):
    return x+y,x-y,x%y

def GetInt(prompt):

    while True:
        said = raw_input(prompt)
        if not said:
            return None
        try:
            number = int(said)
        except ValueError:
            print said,"is not number"
            continue
        return number

def test():

    first = GetInt("please give one number")

    if first:
        second = GetInt("please give another number :")
        if second :
            plus,minus,modulo = DoArithmetic(first,second)
            print first,'+',second, '=' ,plus
            print first, '-', second, '=',minus
            print first, '%', second, '=',modulo

test()