"""
removing elements:
eg
x = 4

a = [1, 2, 3, 4, 4, 5, 6, 1, 4]
o/p:
a=[1,2,3,5,6,1]
"""

def remove_element(a,x):
    """

    :param x:
    :return:
    """
    for i in range(a.count(x)):
        a.pop(a.index(x))
    return a


x = 4

a = [1, 2, 3, 4, 4, 5, 6, 1, 4]

print remove_element(a,x)

l=[1, 2, 3, 4, 4, 5, 6, 1, 4]
e=4

m=[v for v in l if v!=e]
print m