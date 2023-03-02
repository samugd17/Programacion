player1 = "A"
player2 = "B"
game_player1 = game_player2 = 0
points_player1 = points_player2 = 0
sets_player1 = 0
sets_player2 = 0


for point in points:
    if point == "A":
        points_player1 += 1
    else:
        points_player2 += 1
    if points_player1 >= 4 and points_player1 - points_player2 >= 2:
        game_player1 += 1
        if game_player1 >= 6 and game_player1 - game_player2 >= 2:
            sets_player1 += 1
            if sets_player1 == 3:
                winner = player1
                break
    elif points_player2 >= 4 and points_player2 - points_player1 >= 2:
        game_player2 += 1
        if game_player2 >= 6 and game_player2 - game_player1 >= 2:
            sets_player2 += 1
            if sets_player2 == 3:
                winner = player2
                break
    elif game_player1 == 6 and game_player2 == 6:
        if points_player1 >= 7 and points_player1 - points_player2 >= 2:
            sets_player1 += 1
            winner = player1
            break
        elif points_player2 >= 7 and points_player2 - points_player1 >= 2:
            sets_player2 += 1
            winner = player2
            break
print(winner)