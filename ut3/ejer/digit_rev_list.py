"""
Dado un número entero no negativo, genere una lista con los dígitos de dicho número
en orden inverso.
"""


def run(number: int) -> list:
    str_num = str(number)
    num_list = list(str_num)
    for i in range (len(num_list)):
        num_list[i] = int(num_list[i])
    rev_digits = num_list[::-1]


    return rev_digits


if __name__ == "__main__":
    run(35231)
