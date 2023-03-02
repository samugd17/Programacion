target_x = 7
target_y = 8
mov_x = 0
mov_y = 0
print(f"({mov_x}, {mov_y})", end="")

flow = True
while mov_x != target_x and mov_y != target_y:
    if flow:
        mov_x += 1
        mov_y += 2
    else:
        mov_x += 2
        mov_y += 1
    print(f"({mov_x}, {mov_y})", end=" ")
    flow = not flow
