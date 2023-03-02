n = 3
m = 13
sum_mult = 0

for num in range(n, m):
    sum_mult += n
    if sum_mult > m:
        break
    if n <= 0 or m <= 0:
        print("ERROR")
        break
    result = sum_mult
    print(result)
