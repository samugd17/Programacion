v1 = [4, 3, 8, 1]
v2 = [9, 2, 7, 3]
sum_value = 0

for value1, value2 in zip(v1, v2):
    total_value = value1 * value2
    sum_value += total_value
print(sum_value)
