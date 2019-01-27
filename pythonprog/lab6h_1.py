

def SwapcaseAndCenter(a_string,width):
    c_string = a_string.swapcase()
    print c_string.center(width)

a_string = raw_input("say something :")
width = int(raw_input("Enter width"))
SwapcaseAndCenter(a_string,width)
