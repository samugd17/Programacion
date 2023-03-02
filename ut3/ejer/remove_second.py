'''
Dada una lista, genere otra lista eliminando el segundo elemento de forma repetida.
'''


def run(items: list) -> list:
    filter = []
#Solución 1
    for item in items [::2]:
        filter.append(item)
#Solución 2
    for item in range(0, len(items), 2):
        filter.append(item)      
    return filter
