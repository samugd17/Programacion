# *****************
# UN JUEGO AL TENIS
# *****************


def run(points: str) -> str:
    winner = 0
    player1 = "A"
    player2 = "B"
    game_player1 = game_player2 = 0
    points_player1 = points_player2 = 0

    for point in points:
        if point == "A":
            points_player1 += 1
        else:
            points_player2 += 1
    if points_player1 >= 4 and points_player1 - points_player2 >= 2:
            winner = player1
    elif points_player2 >= 4 and points_player2 - points_player1 >= 2:
            winner = player2
    if winner == player1 or player2:
        points_player1 = points_player2 = 0

    return winner


if __name__ == "__main__":
    run(
        "ABAABA")
