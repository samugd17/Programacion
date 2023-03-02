num_mult = 9
num = "1"

for i in range(1, num_mult + 1):
    factor = int(num * i)
    result = factor * factor
    print(f"{factor}*{factor} = {result}")
