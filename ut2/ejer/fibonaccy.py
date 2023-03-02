value1 = 0
print(value1)
value2 = 1
print(value2)

for _ in range(98):
    result = value1 + value2
    value1 = value2
    value2 = result
    print(result)
