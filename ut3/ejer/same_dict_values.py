# ******************************
# VALORES IGUALES EN DICCIONARIO
# ******************************


def run(items: dict) -> bool:
    #Opción 1
    values = list(items.values()) or [0]
    num_same_items = values.count(values[0])
    all_same = num_same_items == len(values)
    return all_same

    #Opción 2
    if len(items) == 0:
        all_same = True
    else:
        values = list(items.values())
        num_same_items = values.count(values[0])
        all_same = num_same_items == len(values)
    return all_same

    #Opción 3
    values = list(items.values())
    all_same = True
    for value in values:
        if value != values[0]:
            all_same = False
            break


if __name__ == "__main__":
    run({"a": 1, "b": 1, "c": 1, "d": 1})
