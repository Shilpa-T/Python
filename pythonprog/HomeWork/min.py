"""
Demonstrates writing in a file with the line number  and a space at front of each file
as same as input file content
"""
import os
import shutil

def Min_fruit_file(file_name):
    """
    write to a file,
    :param file_name:
    :return:
    """
    d_dict = {}
    try:
        read_file = open(file_name)
    except IOError:
        print " i cant find file",file_name
        return
    file_name_base,file_name_ext = file_name.rsplit('.',1)
    new_file_name = file_name_base +"_new."+file_name_ext
    try:
        write_file = open(new_file_name,"a")
    except IOError:
        print " I cant open",write_file
        read_file.close()
        return

    for line in (read_file):
        write_file.write(line)

    read_file.close()
    write_file.close()

path=os.chdir('C:\Users\shilp\PycharmProjects\pythonprog\HomeWork\Dir0')
path=os.getcwd()
print path
#shutil.copyfile('C:\Users\shilp\PycharmProjects\pythonprog\HomeWork\Dir0\fruit.log','C:\Users\shilp\PycharmProjects\pythonprog\HomeWork\Dir0\fruit_0.log')

Min_fruit_file('fruit.log')
path=os.chdir('C:\Users\shilp\PycharmProjects\pythonprog\HomeWork\Dir1')
Min_fruit_file('fruit.log')
path=os.chdir('C:\Users\shilp\PycharmProjects\pythonprog\HomeWork\Dir2')
Min_fruit_file('fruit.log')
path=os.chdir('C:\Users\shilp\PycharmProjects\pythonprog\HomeWork\Dir3')
Min_fruit_file('fruit.log')
path=os.chdir('C:\Users\shilp\PycharmProjects\pythonprog\HomeWork\Dir4')




