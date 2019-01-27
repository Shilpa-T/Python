"""
file error when processing a file
"""

def printfile(name):
    try:
        open_file = open(name)
    except IOError:
        print "I canr find file",name
    else:
        for line in open_file:
            print line

printfile(raw_input('enter file name'))
