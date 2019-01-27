

"""
dice.py:
here we roll dice until the user gets seven
"""

import random

def Getseven():
    rolls = 0
    while True:
        rolls=rolls+1
        if Rollem() == 7:
            break
    if rolls ==1:
        print "you got seven in one roll"
    else:
        print"you got seven in ",rolls,"rolls"

def Reportdice(dice1,dice2):
    total = dice1+dice2
    print dice1,"and",dice2,"equal",total

    if dice1==dice2:
        if dice1==1:
            print"Snake eyes"
        elif dice1==2:
            print "Little joe"
        elif dice1 == 3:
            print "Hard six"
        elif dice1 == 4:
            print "Hard eight"
        elif dice1 == 5:
            print "Fever!"
        elif dice1 == 6:
            print "Box cars"
    return total

def RollDice():

    return random.randrange(1,7),random.randrange(1,7)

def Rollem():
    dice1,dice2 = RollDice()
    total = Reportdice(dice1,dice2)
    return total

if __name__ == "__main__":
    Getseven()