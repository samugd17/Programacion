number = int(input("Introduzca su número: "))
bin_list = []

while number > 0:
    bin_list.append(number % 2)
    number = number // 2
print(list(reversed(bin_list)))
