from teams import get_teams
from teams import create_groups

from group_stages import run_group_stage
from knockout import run_knockouts


def welcome():
    print("=== WORLD CUP 2026 SIMULATOR ===")


def format_team(team, prediction):
    return f"{team}*" if team == prediction else team


def get_prediction(teams):
    while True:
        prediction = input("Predict the winner: ").title()

        if prediction not in teams:
            print("Invalid team.")
            continue

        return prediction


def main():
    welcome()

    teams = get_teams()
    prediction = get_prediction(teams)

    print("Your prediction:", format_team(prediction, prediction))

    groups = create_groups(teams)
    qualified_teams = run_group_stage(groups, prediction)
    champion = run_knockouts(qualified_teams, prediction)

    print("\nWORLD CUP CHAMPION")
    print(format_team(champion, prediction))

    if champion == prediction:
        print("Your prediction was correct!")
    else:
        print("Your prediction was incorrect.")


if __name__ == "__main__":
    main()
