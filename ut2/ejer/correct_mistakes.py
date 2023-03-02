text = "Como 5 hemos visto en este 111 ejemplo, break n000os permite finalizar el bucle una vez que hemos llegado al máximo número de preguntas. Pero si no hubiéramos 105 llegado a dicho límite, el bucle habría seguido hasta que el usuario indicara que quiere salir."

for char in text:
    if char == "5":
        text = text.replace("5", "S")
    if char == "0":
        text = text.replace("0", "O")
    if char == "1":
        text = text.replace("1", "I")
print(text)
