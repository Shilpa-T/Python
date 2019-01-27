import lab10h_1

class Dice:

    def RollDice(self):
        return lab10h_1.RollDice()

def TestDice():
    the_dice = Dice()

    for time in range(3):
        the_dice.RollDice()


if __name__== "__main__":
    TestDice()