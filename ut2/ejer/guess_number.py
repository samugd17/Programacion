# TARGET_NUMBER = 87
# num_tries = 0
# while True:
#    number = int(input("Introduzca número: "))
#    num_tries += 1
#    if number > TARGET_NUMBER:
#        print("Menor")
#    elif number < TARGET_NUMBER:
#        print("Mayor")
#    else:
#        print(f"✅ ¡Enhorabuena! Has encontrado el número en {num_tries} intentos")
#        break

TARGET_NUMBER = 87
input_number = None
num_tries = 0

while input_number != TARGET_NUMBER:
    input_number = int(input("Dame un número: "))
    if input_number > TARGET_NUMBER:
        print("Menor")
    elif input_number < TARGET_NUMBER:
        print("Mayor")
print(f"✅ ¡Enhorabuena! Has encontrado el número en {num_tries} intentos")
