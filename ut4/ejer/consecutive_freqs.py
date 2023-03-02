# ************************************
# FRECUENCIA DE ELEMENTOS CONSECUTIVOS
# ************************************

def to_string(items, *, primary_sep=',', secondary_sep=':'):
    return f'{primary_sep}'.join([f'{i}{secondary_sep}{f}' for i, f in items])


def cfreq(items, /, as_string=False):
    freqs = []
    if len(items) > 0:
        prev_item = items[0]
        count_items = 1
        for item in items[1:]:
            if item == prev_item:
                count_items += 1
            else:
                freqs.append((prev_item, count_items))
                count_items = 1
                prev_item = item
        # pueden quedar elementos pendientes de insertar en la lista
        # después del bucle interno
        freqs.append((prev_item, count_items))
    if as_string:
        freqs = to_string(freqs, primary_sep='-')
    return freqs


items = [5, 5, 5, 4, 3, 1, 1, 1]
result = cfreq(items, as_string=True)
print(items)
print(result)

