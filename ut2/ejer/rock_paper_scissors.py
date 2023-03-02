person1 = input("Introduzca su opción :")
person2 = input("Introduzca su opción :")
value1 = "piedra"
value2 = "papel"

if person1 == value1:
    if person2 == value2:
        print("Gana persona2: El papel envuelve a la piedra")
    else:
        print("empate")
else:
    if person2 == value1:
        print("Gana persona1: El papel envuelve a la piedra")
    else:
        print("empate")
