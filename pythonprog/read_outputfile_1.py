def Compareresult(filename):
    tokens = []
    date_l = []

    with open(filename,'r') as f:
        f.next()
        for line in f:
            tokens = line.rstrip('\n').split('\t')
            date_l.append((tokens[3]))
        for i in date_l:

            if i == str(0):
                print 'PASS'
            else:
                print 'FAIL'
        return date_l

#Compareresult('tableout.txt')



def compareAppendResult(filename):
    tokens = []
    date_l = []

    with open(filename, 'r') as f:
        f.next()
        for line in f:
            tokens = line.rstrip('\n').split('\t')
            date_l.append((tokens[3]))
        with open(filename,'w') as fi:
            fi.write("\n".join("Result"))
            fi.next()
        for i in date_l:

            if i == str(0):
                x="PASS"
                fi.write("\n".join(x))
            else:
                x="FAIL"
                fi.write("\n".join(x))
        fi.close()
    f.close()

compareAppendResult('tableout.txt')