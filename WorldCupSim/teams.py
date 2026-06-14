import random

def get_teams():
    return [
        "Brazil", "Argentina", "France", "England",
        "Spain", "Germany", "Portugal", "Netherlands",
        "Belgium", "Croatia", "Uruguay", "Mexico",
        "USA", "Canada", "Japan", "South Korea",
        "Morocco", "Senegal", "Nigeria", "Egypt",
        "Cameroon", "Ghana", "Algeria", "Tunisia",
        "Australia", "New Zealand", "Saudi Arabia", "Iran",
        "Colombia", "Chile", "Italy", "Uganda"
    ]


def create_groups(teams):

    #Shuffle the teams
    random.shuffle(teams)

    groups = {}

    for i in range(8):
        group_name = chr(65 + i)  # Group A, B, C, ...
        groups[group_name] = teams[i*4:(i+1)*4]

    

    return groups

