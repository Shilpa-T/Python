def Determinewinner(team_a,score_a,team_b,score_b):
    if score_a > score_b:
        diff = score_a - score_b
        winner = team_a
    elif score_b > score_a:
        diff = score_b - score_a
        winner = team_b
    else:
        winner = "tie"
    if winner == "tie":
        winner = "it is a tie"

    else:
        report = winner +" won by " + str(diff)+" points."
    return report

print Determinewinner('A',6,'B',4)