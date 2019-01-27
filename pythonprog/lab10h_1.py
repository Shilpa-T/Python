
"""
Importable dice emulation
"""
import random

def Getnumber(number):
    """
    Rool dice untill the total == number.Return the number of rolls
    :param number:
    :return:
    """
    rolls = 0
    while True:
        rolls =rolls+1
        if RollDice() == number:
            return rolls

def ReportDice(dice):
    DOUBLES =("Can't Happen","Snake Eyes","Little Joe","Hard six","HardEight","Fever","Box cars")
    total = sum(dice)
    print" ",dice[0],"and",dice[1],"totaling",total

    if dice[0] == dice[1]:
        print " ",DOUBLES[dice[0]]
    return total


def RollDice():
    """

    :return:
    """
    dice = random.randrange(1,7),random.randrange(1,7)
    return ReportDice(dice)

def main():
        for number in range(3,13,4):
            rolls  = Getnumber(number)
            print "it tooks",rolls,"rolls to get",number

if __name__ == "__main__":
    main()