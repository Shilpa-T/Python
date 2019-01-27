# to change string value,we need to convert to list and then operate on it
s='shilpap'
L=list(s)
print L
L[6]='T'
print L
N=''.join(L)
print N

L_list= [180,'shilpa',35.6]
L_list.append('Goutham')
L_list.append(100)
print L_list

L_list.pop(4)

print L_list

M=['a','d','j','c','b']
x=M.sort()

print M.sort()
print x
print sorted(M)
print M.reverse()
print L_list.insert(4,100)




