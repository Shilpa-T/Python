input=['cat','atc','tac','bat','pure','rupe','taco','coat']


def keycompare(input):
    d = {}
    for each in input:
        token=''.join(sorted(each))
        if token in d:
            d[token].append(each)
        else:
            d[token]=[each]

    return d

print keycompare(input)








