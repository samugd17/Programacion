first_code = 33
last_code = 127
line = 0

for letter in range(first_code, last_code + 1):
    char = chr(letter)
    print(f"{letter:03d}{char}", end=" ")
    line += 1
    if line % 5 == 0:
        print()
