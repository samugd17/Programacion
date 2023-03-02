a = 12
b = 44

_min = a if a < b else b

for num in range(_min, 0, -1):
    if a % num == 0 and b % num == 0:
        break
print(num)
