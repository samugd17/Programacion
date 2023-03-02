number = 11
num_divisors = 0

for poss_div in range(1, number + 1):
    if number % poss_div == 0:
        num_divisors += 1

if num_divisors == 2:
    print("Es primo")
else:
    print("No es primo")
