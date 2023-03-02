# *******************************
# VENTAS EN TIENDA DE INFORMÁTICA
# *******************************


def run(sales: list) -> tuple:
    new_sales = []
    for element in range(len(sales)):
        if type(sales[element]) is list:
            for i in sales[element]:
                new_sales.append(i)
        else:
            new_sales.append(sales[element])
    
    pcs = (sum(new_sales[::2]))
    displays = (sum(new_sales[1::2]))
    
    return pcs, displays


if __name__ == "__main__":
    run([[4, 5], [1, 3], [3, 2]])
