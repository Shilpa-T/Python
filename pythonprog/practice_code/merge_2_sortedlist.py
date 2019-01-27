

"""
def merge(a,b):
    Function to merge two arrays
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            pass
        else:
            a.append(b[0])
            b.remove(b[0])

    if len(b) == 0:
        a += b
    else:
        c += a
    return a
def mergesortlist(a,b):
    i = 0
    j = 0
    k = 0
    a=sum(a,[])
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            #list[k] = lefthalf[i]
            i = i + 1
        else:
            a[i+(len(a)-1)] = b[j]
            j = j + 1
    return a

"""




A=[1,4,7,8,9]
B=[5,6,8,99,101,9999]

A.extend(B)
A.sort()
print A

#print merge(A,B)

#print mergesortlist(A,B)

