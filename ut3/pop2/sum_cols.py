# ****************
# SUMANDO COLUMNAS
# ****************
from pathlib import Path


def run(data_path: Path) -> tuple:
    sum_array = []
    num_col = 0
    counter = 0
    i = 0
    with open(data_path) as f:
        for line in f:
            values = line.strip().split()
            for index, value in enumerate(values):
                if index == i:
                    num_col += int(value)
                    print((num_col))
                else:
                    sum_array.append(int(value))

    # data = []
    # with open(data_path, 'r') as f:
    #    for row in f:
    #        fix_row = [int(v) for v in row.strip().split()]
    #        data.append(fix_row)

    # cols = []
    # for col_index in range(len(data[0])):
    #    col = []
    #    for row_index in range(len(data)):
    #        value = data[row_index][col_index]
    #        col.append(value)
    #    cols.append(col)

    # csum = [sum(col) for col in cols]
    # csum = tuple(csum)

    #return csum


if __name__ == "__main__":
    run("data/sum_cols/data1.txt")
