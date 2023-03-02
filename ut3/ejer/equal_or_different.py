num_list = [1, 1, 1, 1, 1, 1, 1]
first_element = num_list[0]
previous_element = first_element

for element in num_list:
    if element != first_element:
        print("Distintos")
        break
    elif element != previous_element:
        previous_element = element
        print("Distintos")
else:
    print("Iguales")
