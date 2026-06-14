from matches import play_match
import sys


def wait_any_key(prompt="Press any key to continue..."):
    print(prompt, end='', flush=True)
    try:
        # Unix-like single-key press
        import termios, tty
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
    except Exception:
        try:
            # Windows
            import msvcrt
            msvcrt.getch()
        except Exception:
            # Fallback
            try:
                input()
            except EOFError:
                pass
    print()


def format_team(team, prediction):
    return f"{team}*" if team == prediction else team


def initialize_points(teams):
    return {team: 0 for team in teams}


def update_points(points, team1, team2, score1, score2):
    if score1 > score2:
        points[team1] += 3
    elif score2 > score1:
        points[team2] += 3
    else:
        points[team1] += 1
        points[team2] += 1


def play_group_matches(teams, prediction):
    points = initialize_points(teams)

    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            team1 = teams[i]
            team2 = teams[j]
            score1, score2 = play_match(team1, team2, prediction)

            print(
                f"{format_team(team1, prediction)} {score1}-{score2} {format_team(team2, prediction)}"
            )
            update_points(points, team1, team2, score1, score2)

    print("\nStandings:")
    for team, pts in sorted(points.items(), key=lambda item: (-item[1], item[0])):
        print(f"{format_team(team, prediction)} - {pts} pts")

    return get_top_two(points)


def get_top_two(points):
    sorted_teams = sorted(
        points.items(),
        key=lambda item: (-item[1], item[0])
    )
    return [sorted_teams[0][0], sorted_teams[1][0]]


def run_group_stage(groups, prediction):
    qualified_teams = []

    for group_name, teams in groups.items():
        print(f"\nGroup {group_name}")
        print("Teams:", ", ".join(format_team(team, prediction) for team in teams))

        top_two = play_group_matches(teams, prediction)
        print(f"Qualified from Group {group_name}: {format_team(top_two[0], prediction)}, {format_team(top_two[1], prediction)}")
        qualified_teams.extend(top_two)
        try:
            wait_any_key()
        except NameError:
            # In case helper is missing, fallback to input()
            try:
                input()
            except EOFError:
                pass

    return qualified_teams
