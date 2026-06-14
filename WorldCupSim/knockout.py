from matches import play_match, get_winner
import sys


def format_team(team, prediction):
    return f"{team}*" if team == prediction else team


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


def get_round_name(num_teams):
    if num_teams == 16:
        return "ROUND OF 16"
    if num_teams == 8:
        return "QUARTERFINALS (ROUND OF 8)"
    if num_teams == 4:
        return "SEMIFINALS (ROUND OF 4)"
    if num_teams == 2:
        return "FINAL (ROUND OF 2)"
    return f"ROUND OF {num_teams}"


def play_knockout_round(teams, prediction):
    winners = []

    for i in range(0, len(teams), 2):
        team1 = teams[i]
        team2 = teams[i + 1]

        score1, score2 = play_match(team1, team2, prediction)

        print(
            f"{format_team(team1, prediction)} {score1}-{score2} {format_team(team2, prediction)}"
        )

        winner = get_winner(team1, team2, score1, score2)
        print(f"Winner: {format_team(winner, prediction)}\n")

        winners.append(winner)

    return winners


def run_knockouts(teams, prediction):
    if not teams:
        return None

    round_teams = teams
    while len(round_teams) > 1:
        round_name = get_round_name(len(round_teams))
        print(f"\n{round_name}")

        # Pause so the user sees the round name before matches start
        try:
            wait_any_key(f"Press any key to start {round_name}...")
        except Exception:
            pass

        round_teams = play_knockout_round(round_teams, prediction)

        # Pause after the round so user can review winners
        try:
            wait_any_key()
        except Exception:
            pass

    champion = round_teams[0]
    return champion
