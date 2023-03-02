# ***********************
# PARTICIÓN POR EL NÚMERO
# ***********************


def run(values: list, ref_value: int) -> list:
    npartition = []
    less_than = []
    more_than = []
    for value in values:
        if value < ref_value:
            less_than.append(value)
        else:
            more_than.append(value)
    npartition.append(less_than)
    npartition.append(more_than)
    return npartition


if __name__ == '__main__':
    run([4, 3, 2, 9, 8, 5], 4)
