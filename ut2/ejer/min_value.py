value1 = int(input("Introduzca primer valor :"))
value2 = int(input("Introduzca segundo valor :"))
value3 = int(input("Introduzca tercer valor :"))

if value1 < value2:
    if value1 < value3:
        min_value = value1
    else:
        min_value = value3
elif value2 < value3:
    min_value = value2
else:
    min_value = value3

print(min_value)
