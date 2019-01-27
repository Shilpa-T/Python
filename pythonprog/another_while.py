"""
another_while.py

keywords:True
        False
"""

total = 0

while True :
    answer = raw_input("Give me a number")
    if answer == '':
        break
    try:
        total = total + float(answer)
    except ValueError:
        print "that wasn't a number !"
print "Total=",total