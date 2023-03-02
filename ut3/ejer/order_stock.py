# ***********
# ¿HAY STOCK?
# ***********


def run(stock: dict, merch: str, amount: int) -> bool:
    available = True
    if merch in stock.keys():
        for key, value in stock.items():
            if merch != key:
                continue
            elif value >= amount:
                available = True
            else:
                available = False
    else:
        available = False

    #2ªforma
    merch_stock = stock.get(merch, 0)
    available = merch_stock >= amount

    return available


if __name__ == '__main__':
    run({'pen': 20, 'cup': 11, 'keyring': 40}, 'cup', 9)

