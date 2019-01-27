"""
greeter_def4.py
Here we implement 'inheritenvce' to leave the original
Greeter class in tack and add a NamedGreeter class,that has all the functionality
 of the greeter class plus  some new changes
"""
class Greeter:
    """
    The Greeter class makes greeter objects that can greet you
    """

    def Greet(self):
        print "Hello world"

class NamedGreeter(Greeter):

    def __init__(self,name):
        self.name = name

    def saybyname(self):
        print " I,m",self.name

def Test():
    fred = NamedGreeter('fred')
    print 'fred.Greet():'

    fred.Greet()
    fred.saybyname()

    x = Greeter()
    print 'x.Greet():'

    x.Greet()

if __name__ == "__main__":
    Test()

