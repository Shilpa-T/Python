squares = [x**2 for x in range(10)]
print squares


seq = [(x,y) for x in [1,2,3] for y in [1,2,3] if x==y]
print seq

vec = [-4,-2,0,2,4]

print "create a new list with the values doubled"
vec_double = [x*2 for x in vec]
print vec_double

print " filter the list to exclude negative numbers"
res = [x for x in vec if x>=0]
print res


vec = [-4,-2,0,2,4]
res1 = []

for i in vec:
    if i>=0:
        res1.append(i)
print res1
