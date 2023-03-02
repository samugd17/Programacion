text = input("Introduzca su palabra: ")

for letter in text:
    if not letter.isalpha():
        print("Se han encontrado caracteres no alfabéticos")
        break
else:
    print("Es alfabético")
