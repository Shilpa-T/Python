
class Greeter:
    """
    The Greeter class makes greeter objects that can greet you
    """

    def Greet(self):
        print "Hello world"


def TestGreeter():
    fred = Greeter()
    print "fred.Greet()"
    fred.Greet()
    alma = Greeter()
    print "alma.Greet()"
    alma.Greet()

    print "fred is",id(fred),"Alma is",id(alma),"Greeter class",id(Greeter)


if __name__ == "__main__":
    TestGreeter()