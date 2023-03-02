name = input("¿Su nombre?: ")

while name != name.title():
    print("Error. Escriba su nombre correctamente")
    name = input("¿Su nombre?: ")

    # Otra forma

    # while not name.istitle():
    # print("Error. Escriba su nombre correctamente")
    # name = input("¿Su nombre?: ")
