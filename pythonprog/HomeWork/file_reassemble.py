import os
from os import listdir,getcwd,walk
from os.path import isfile, join
import pandas as pd

import time
import filecmp

path = os.getcwd()
print path

def file_info(directory):
    file_list = []
    onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
    for i in listdir(directory):
        print i
        if isfile(i):
            print i


# for i in os.listdir(directory):
#print i


#filecmp.dircmp('C:\Users\shilp\PycharmProjects\pythonprog\HomeWork\Dir1', 'C:\Users\shilp\PycharmProjects\pythonprog\HomeWork\Dir2').report()
#file_list =
#file_info(path)


f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break
print 