import random


def play_match(team1, team2, prediction):
    score1 = random.randint(0, 5)
    score2 = random.randint(0, 5)

    if team1 == prediction:
        score1 += 1
    if team2 == prediction:
        score2 += 1

    return score1, score2


def get_winner(team1, team2, score1, score2):
    if score1 > score2:
        return team1
    elif score2 > score1:
        return team2

    print("Penalty Shootout!")
    return random.choice([team1, team2])
