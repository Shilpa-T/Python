import sys, os

path = os.getcwd()
def listFiles(dir):
    basedir = dir
    print "Files in ", os.path.abspath(dir), ": "
    subdirlist = []
    for item in os.listdir(dir):
        if os.path.isfile(item):
            if item.endswith('.log'):
                print item
            else:
                subdirlist.append(os.path.join(basedir, item))
        for subdir in subdirlist:
            print subdir
            listFiles(subdir)

listFiles(path)