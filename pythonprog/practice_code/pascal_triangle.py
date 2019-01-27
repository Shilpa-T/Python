"""
Pascal's triangle :

Each number is the two numbers above it added together
1
11
121
1331
14641
"""

def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print trow
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1

pascal_triangle(2)
print"******************************************"
pascal_triangle(5)
print"******************************************"
pascal_triangle(6)