"""
read_file.py
"""
def printfile(name):
    for line in open(name):
        print line



printfile(raw_input('file to read'))

