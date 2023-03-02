str = input("Introduzca su frase: ")
value_str = (
    str.count("1")
    + str.count("2")
    + str.count("3")
    + str.count("4")
    + str.count("5")
    + str.count("6")
    + str.count("7")
    + str.count("8")
    + str.count("9")
    + str.count("0")
)
for letter in str:
    if str.count("1"):
        print("You should use singular")
        break
    else:
        value_str >= 1
        print("You should use plural")
        break
