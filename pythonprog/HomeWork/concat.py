import glob
import pandas as pd
import shutil
import os

wd=os.chdir('C:\Users\shilp\PycharmProjects\pythonprog')
RootDir1 = r'C:\Users\shilp\PycharmProjects\pythonprog\HomeWork'

def func_concatenate_files(RootDir1):
    for root, dirs, files in os.walk((os.path.normpath(RootDir1)), topdown=False):
        print "root:",root,"dirs",dirs
        for name in files:
            print name
            if name.endswith('.log'):
                print "Found",name,type(name)
                read_file = open(os.path.join(root,name),'r')
                file_name_base, file_name_ext = name.rsplit('.', 1)
                new_file_name = file_name_base + "_new." + file_name_ext
                new_name = os.path.join('C:\Users\shilp\PycharmProjects\pythonprog\HomeWork', new_file_name)
                if os.path.exists(new_name):
                    for line in (read_file):
                        write_file.write(line)
                else:
                    write_file = open(new_name, "a")
                    for line in (read_file):
                        write_file.write(line)
                read_file.close()
    write_file.close()
    return new_name

def deleteContent(fName):
    """
    :param fName: File name that needs to have contents erased
    :return: None
    """
    with open(fName, "w"):
        pass

def read_data(file_name):
    data = pd.read_csv(file_name,sep=" ", header = None)
#print data
    df_data = pd.DataFrame(data)
#print df_data.head()
    data_columns = ['Month','Day','Time','status','path','Fruit','hexcode','Count']
    df_data.columns=data_columns
    fruit_count_max = df_data.groupby(['Fruit'])['Count'].max()
    fruit_count_min = df_data.groupby(['Fruit'])['Count'].min()
    print fruit_count_max

    print fruit_count_min

#deleteContent('fruit_new.log')
file_name=func_concatenate_files(RootDir1)
read_data(file_name)
