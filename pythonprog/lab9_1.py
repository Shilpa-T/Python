"""
demonstrates word count in file
"""

def CountWords(file_name):
    """
    Function  returns number of words in a file.
    :param file_name:
    :return:
    """
    tokens = []
    d={}
    try:
        open_file = open(file_name)
    except IOError:
        print "I canr find file",file_name
    else:
        for line in open_file:
            tokens = tokens+line.split()

    for token in tokens:
        d[token] = d.get(token,0)+1
    return d.keys(),len(d.keys())


def PrinntHighFreqword(file_name):
   """
   Find high freq word in file
   :param file_name:
   :return: high frequency word
   """
   tokens = []
   d ={}

   try:
       read_file = open(file_name)
   except IOError:
       print "I cant find file",read_file
   else:
       for line in read_file:
           tokens = tokens + line.split()

       for token in tokens:
           d[token]=d.get(token,0)+1
       for i,v in d.items():
           if v >= max(d.values()):
            return i,v




#print CountWords('test.txt')
print PrinntHighFreqword('test.txt')
