# *************
# SUMANDO FILAS
# *************
from pathlib import Path


def run(data_path: Path) -> tuple:
    sum_array = []
    num_row = 0
    counter = 0
    with open(data_path) as f:
        for line in f:
            values = line.strip().split()
            for value in values:
                num_row += int(value)
                counter += 1
                if counter == len(values):
                    sum_array.append(num_row)
                    counter = 0
                    num_row = 0
    rsum = tuple(sum_array)
            

    return rsum


if __name__ == "__main__":
    run("data/sum_rows/data1.txt")
