"""
greeter_def5.py
Here both the classes have greet method.The lingo is:

"""
class Greeter:
    """
    The Greeter class makes greeter objects that can greet you
    """

    def Greet(self):
        print "Hello world"
    def Bye(self):
        print "Bye now"

class NamedGreeter(Greeter):

    def __init__(self,name):
        self.name = name

    def Greet(self):
        Greeter.Greet(self)
        print "i 'm ",self.name


class HipGreeter(NamedGreeter):

    def Greet(self):
        NamedGreeter.Greet(self)
        print "wazzup"


def Test():
    rocky= HipGreeter('Rocky')
    rocky.Greet()
    rocky.Bye()


if __name__ == "__main__":
    Test()

