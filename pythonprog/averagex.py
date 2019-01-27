"""
finding average of the scores
"""

def Averagefive(num1,num2,num3,num4,num5):
    total = num1+num2+num3+num4+num5
    avg = total/5.0
    return avg

def processScores():
    score1 = 95
    score2 = 85
    score3 = 99
    score4 = 100
    score5 = 92

    average = Averagefive(score1,score2,score3,score4,score5)
    print"Average",average

processScores()