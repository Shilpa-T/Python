

def Average(numbers):
    total = sum(numbers)/len(numbers)
    return total

def Processscores():
    scores = [95.2,85.1,99,100,92.3]
    Avg = Average(scores)
    print "Average:",Avg

Processscores()