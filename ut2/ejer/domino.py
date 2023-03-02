DOMINO_MAX = 6

for left_side in range(DOMINO_MAX + 1):
    for right_side in range(left_side, DOMINO_MAX + 1):
        print(f"{left_side}|{right_side}", end=" ")
    print()
