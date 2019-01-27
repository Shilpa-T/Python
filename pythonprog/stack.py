"""
Here calls to a function,that call function
that call function
"""

def Askuser():
    return int(raw_input("say something: "))

def AskGrandmother():
    return Askuser()

def Askmother():
    return AskGrandmother()

print Askmother()
