
def collectsentence():

    string_list = raw_input("enter the sentence")
    return string_list

def Displaystring():

    strings = collectsentence()
    list = strings.split()
    stringsjoin= '*@!'.join(list)
    print stringsjoin + "!!!"

Displaystring()