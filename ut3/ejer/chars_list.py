# Dada una lista de strings, obtenga otra lista que contenga todos los caracteres de cada
# uno de los strings de la lista de entrada.


def run(texts: list) -> list:
    chars = []
    for string in texts:
        for letter in string:
            chars.append(letter)

    return chars
