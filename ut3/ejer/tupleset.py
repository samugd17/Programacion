# ******************
# TUPLAS Y CONJUNTOS
# ******************


def run(input: tuple) -> set:
    set1, set2 = set(), set()
    for first, second in input:
        set1.add(first)
        set2.add(second)
    output = (set1, set2)

    return output


if __name__ == '__main__':
    run(((4, 3), (8, 2), (7, 5), (8, 2), (9, 1)))