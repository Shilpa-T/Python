"""
keyword if,control mechanism
if.py-conditional execution or branching
if,elif,else
"""

CASH = 10.0

try:
    cost = float(raw_input("How much does it cost ?"))
except ValueError :
    print "Do you mean its free"
else:
    tip = cost * .18
    tax = cost *.0825

    if cost+tip+tax <= CASH :
        print"I will take it"
    elif cost+tax <= CASH :
        print " i will take it but i only have",CASH-cost-tax , "to give you"
    else :
        print " I cant afford it"

