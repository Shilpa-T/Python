def readinputfile(file):
    tokens = []
    date_l = []
    read_file=open(file,'r')


    for line in read_file:

        tokens = line.split(' ')
        date_l.append((tokens[0]))
    print tokens
    print date_l

readinputfile('fruit.log')
