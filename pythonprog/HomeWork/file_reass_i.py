import os
import fnmatch
import pandas as pd
import datetime
from datetime import datetime
from operator import itemgetter


wd=os.chdir('C:\Users\shilp\PycharmProjects\pythonprog')
RootDir1 = r'C:\Users\shilp\PycharmProjects\pythonprog\HomeWork'


def find_min_max_timestamp_file(RootDir1):
    time = {}
    i = 0
    for root, dirs, files in os.walk((os.path.normpath(RootDir1)), topdown=False):
        print "root:",root

        for name in files:

            if name.endswith('.log'):

                read_file = open(os.path.join(root, name), 'r')

                df = pd.read_csv(read_file, sep=" ", header=None)

                df_data = pd.DataFrame(df)
                data_columns = ['Month', 'Day', 'Time', 'status', 'path', 'Fruit', 'hexcode', 'Count']
                df_data.columns = data_columns
                print df_data['Day'].max(), df_data['Time'].max()
                time[i]=(df_data['Day'].max(),df_data['Time'].max())
                i = i+1
            read_file.close()
    return time


x=find_min_max_timestamp_file(RootDir1)
print x


y=sorted(x.items(), key=itemgetter(1))

print y,type(y)