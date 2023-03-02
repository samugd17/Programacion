'''
Genere una lista con los "n" primeros múltiplos de "x", donde "n" y "x" son parámetros de
entrada representando valores enteros mayores que 0.

Resuelva el ejercicio utilizando listas por comprensión.
'''


def run(x: int, n: int) -> list:
    multiples=[]
    
    for num in range(1, n + 1):
        value_multiple = x * num 
        multiples.append(value_multiple)

        multiples = [value_multiple for num in range(1, n + 1)]

    return multiples
