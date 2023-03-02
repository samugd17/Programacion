# ************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO
# ************************************


def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return None
    fact = 1
    while n > 0:
        fact = fact * n
        n -= 1

    return fact
