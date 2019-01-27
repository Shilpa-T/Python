"""
Demonstrates writing in a file with the line number  and a space at front of each file
as same as input file content
"""
def Numberfile(file_name):
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
    #file_name_base,file_name_ext = file_name.rsplit('.',1)
    #new_file_name = file_name_base +"_numbered."+file_name_ext
    try:
        write_file = open(file_name,"a")
    except IOError:
        print " I cant open",write_file
        read_file.close()
        return

    for index,line in enumerate(read_file):
        if index == 0:
            write_file.write('\n')
        write_file.write(str(index+1)+' '+line)

    read_file.close()
    write_file.close()


Numberfile(raw_input("File to Capitalize:"))





