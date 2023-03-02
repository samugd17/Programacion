'''
El objetivo es encontrar el primer número no consecutivo dentro de una lista de valores
numéricos enteros. Si todos los valores son consecutivos entonces el resultado es None.
'''


def run(values: list) -> int:
    value1= values[0]
    target = 0
    
    if value1 == [] or len(values) == 1:
        Target = None
    else:
        for value in values:
            value1 = values[0]
            if value1 + 1 == value:

                    
                    
                
        
    
    return target


if __name__ == '__main__':
    run([1, 2, 3, 4, 6, 7, 8])
