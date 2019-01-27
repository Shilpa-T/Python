"""
Pascal's triangle :

Each number is the two numbers above it added together
1
11
121
1331
14641
"""
def printseq(arr):
    x=0
    res=[]
    for each in arr:
        res.append(each+x)
        x=each
    res.append(1)
    #print res
    return res

def pascal_trianle(n):
    res = [1]
    i=1

    while i <= n:
        print res
        r = printseq(res)
        res=r
        i+=1

pascal_trianle(2)
print "********************************"
pascal_trianle(4)
print "********************************"
pascal_trianle(6)