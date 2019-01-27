"""
Demonstrates writing a file
"""
def Capitalizefile(file_name):
    """
    writes a file,file_name
    :param file_name:
    :return:
    """
    try:
        read_file = open(file_name)
    except IOError:
        print " i cant find file",file_name
        return
    file_name_base,file_name_ext = file_name.rsplit('.',1)
    new_file_name = file_name_base +"_caps."+file_name_ext
    try:
        write_file = open(new_file_name,"w")
    except IOError:
        print " I cant open",write_file
        read_file.close()
        return
    for line in read_file:
        write_file.write(line.upper())
    read_file.close()
    write_file.close()


Capitalizefile(raw_input("File to Capitalize:"))





