value = (input("Introduzca su número: "))

if value.endswith('0') == True:
    new_value = value.rstrip('0')
    print(new_value)
