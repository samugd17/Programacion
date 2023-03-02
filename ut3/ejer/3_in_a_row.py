player_X = (input("Nombre del jugador 1(\u274C): ")).title()
token_x = "\u274C"
player_O = (input("Nombre del jugador 2(\u26AA): ")).title()
token_o = "\u26AA"
board = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 "]
allowed_values = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
print(board[6], "|", board[7], "|", board[8], "|")
print(board[3], "|", board[4], "|", board[5], "|")
print(board[0], "|", board[1], "|", board[2], "|")

#Condición de parada
game_over = False
while board.count(token_x) + board.count(token_o) <= len(board) and not game_over:
    valid_move = False
    # Entrada de movimientos Jugador X
    while not valid_move:
        mov_player_X = input(f"{player_X}, selecciona una casilla: ")
        if mov_player_X not in allowed_values:
            print("ERROR: Seleccione un valor del 1 al 9")
            continue
        if mov_player_X == "1":
            if not (board[0] == token_x or board[0] == token_o):
                board[0] = token_x
            else:
                print("Casilla ya ocupada. Seleccione otra.")
                continue
        elif mov_player_X == "2":
            if not (board[1] == token_x or board[1] == token_o):
                board[1] = token_x
            else:
                print("Casilla ya ocupada. Seleccione otra.")
                continue
        elif mov_player_X == "3":
            if not (board[2] == token_x or board[2] == token_o):
                board[2] = token_x
            else:
                print("Casilla ya ocupada. Seleccione otra.")
                continue
        elif mov_player_X == "4":
            if not (board[3] == token_x or board[3] == token_o):
                board[3] = token_x
            else:
                print("Casilla ya ocupada. Seleccione otra.")
                continue
        elif mov_player_X == "5":
            if not (board[4] == token_x or board[4] == token_o):
                board[4] = token_x
            else:
                print("Casilla ya ocupada. Seleccione otra.")
                continue
        elif mov_player_X == "6":
            if not (board[5] == token_x or board[5] == token_o):
                board[5] = token_x
            else:
                print("Casilla ya ocupada. Seleccione otra.")
                continue
        elif mov_player_X == "7":
            if not (board[6] == token_x or board[6] == token_o):
                board[6] = token_x
            else:
                print("Casilla ya ocupada. Seleccione otra.")
                continue
        elif mov_player_X == "8":
            if not (board[7] == token_x or board[7] == token_o):
                board[7] = token_x
            else:
                print("Casilla ya ocupada. Seleccione otra.")
                continue
        else:
            if not (board[8] == token_x or board[8] == token_o):
                board[8] = token_x
            else:
                print("Casilla ya ocupada. Seleccione otra.")
                continue
        valid_move = True
        print(board[6], "|", board[7], "|", board[8], "|")
        print(board[3], "|", board[4], "|", board[5], "|")
        print(board[0], "|", board[1], "|", board[2], "|")
        # Combinaciones ganadoras 
        if board[0] == token_x and board[1] == token_x and board[2] == token_x \
        or board[3] == token_x and board[4] == token_x and board[5] == token_x \
        or board[6] == token_x and board[7] == token_x and board[8] == token_x \
        or board[0] == token_x and board[3] == token_x and board[6] == token_x \
        or board[1] == token_x and board[4] == token_x and board[7] == token_x \
        or board[2] == token_x and board[5] == token_x and board[8] == token_x \
        or board[0] == token_x and board[4] == token_x and board[8] == token_x \
        or board[6] == token_x and board[4] == token_x and board[2] == token_x:
            print(f"{player_X} GANA")
            game_over = True
            break 
    #Condición de parada  
    if game_over or board.count(token_x) + board.count(token_o) == len(board):
        break
    valid_move = False
    # Entrada de movimientos Jugador O
    while not valid_move:
        mov_player_O = input(f"{player_O}, selecciona una casilla: ")
        if mov_player_O not in allowed_values:
            print("ERROR: Seleccione un valor del 1 al 9")
            continue
        if mov_player_O == "1":
            if not (board[0] == token_x or board[0] == token_o):
                board[0] = token_o
            else:
                print("Casilla ya ocupada. Seleccione otra.")
                continue
        elif mov_player_O == "2":
            if not (board[1] == token_x or board[1] == token_o):
                board[1] = token_o
            else:
                print("Casilla ya ocupada. Seleccione otra.")
                continue
        elif mov_player_O == "3":
            if not (board[2] == token_x or board[2] == token_o):
                board[2] = token_o
            else:
                print("Casilla ya ocupada. Seleccione otra.")
                continue
        elif mov_player_O == "4":
            if not (board[3] == token_x or board[3] == token_o):
                board[3] = token_o
            else:
                print("Casilla ya ocupada. Seleccione otra.")
                continue
        elif mov_player_O == "5":
            if not (board[4] == token_x or board[4] == token_o):
                board[4] = token_o
            else:
                print("Casilla ya ocupada. Seleccione otra.")
                continue
        elif mov_player_O == "6":
            if not (board[5] == token_x or board[5] == token_o):
                board[5] = token_o
            else:
                print("Casilla ya ocupada. Seleccione otra.")
                continue
        elif mov_player_O == "7":
            if not (board[6] == token_x or board[6] == token_o):
                board[6] = token_o
            else:
                print("Casilla ya ocupada. Seleccione otra.")
                continue
        elif mov_player_O == "8":
            if not (board[7] == token_x or board[7] == token_o):
                board[7] = token_o
            else:
                print("Casilla ya ocupada. Seleccione otra.")
                continue
        else:
            if not (board[8] == token_x or board[8] == token_o):
                board[8] = token_o
            else:
                print("Casilla ya ocupada. Seleccione otra.")
                continue
        valid_move = True
        print(board[6], "|", board[7], "|", board[8], "|")
        print(board[3], "|", board[4], "|", board[5], "|")
        print(board[0], "|", board[1], "|", board[2], "|")
    # Combinaciones ganadoras
    if board[0] == token_o and board[1] == token_o and board[2] == token_o \
        or board[3] == token_o and board[4] == token_o and board[5] == token_o \
        or board[6] == token_o and board[7] == token_o and board[8] == token_o \
        or board[0] == token_o and board[3] == token_o and board[6] == token_o \
        or board[1] == token_o and board[4] == token_o and board[7] == token_o \
        or board[2] == token_o and board[5] == token_o and board[8] == token_o \
        or board[0] == token_o and board[4] == token_o and board[8] == token_o \
        or board[6] == token_o and board[4] == token_o and board[2] == token_o:
        print(f"{player_O} GANA")
        game_over = True
        break
#Condición de parada
if not game_over and board.count(token_x) + board.count(token_o) == len(board):
    print("EMPATE")