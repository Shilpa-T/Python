class Greeter:

    def SetName(self,name_in):
        self.name = name_in

    def Greet(self):
        print "Hello World",
        try:
            print "I'm "+ self.name+"."
        except AttributeError:
            print

def TestGreeter():
    gracy=Greeter()
    gracy.SetName("Gracy")
    gracy.Greet()
    george = Greeter()
    george.SetName("George")
    george.Greet()


if __name__=="__main__":
    TestGreeter()

