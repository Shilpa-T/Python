"""
if x is from 1 to 4,add one to y
if x is not 1,2,3,4,5,6,or 7,make y equal 7
"""

x= int(raw_input("Give me a number"))
y=0
if x>=1 and x <= 4:
    y=y+1
elif x>7:
    y=7
else:
    y=0
print"x value",x,"y value",y

