"""
we define an __init__ methodso that the name is given
when the object is created.
"""

class Greeter:

    def __init__(self,name_in):
        """
        instantiation looks like
        grreter_obj = Greeter("Fred")
        :param name:
        """
        self.name = name_in

    def Greet(self):
        print " Hello world. I 'm ",self.name

def TestGreeter():
    fred = Greeter("Fred")
    print"fred.Greet()"
    fred.Greet()
    x=Greeter() #error


if __name__ == "__main__":
    TestGreeter()