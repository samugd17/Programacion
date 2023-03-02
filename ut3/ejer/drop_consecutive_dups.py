elements = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
new_elements = []
previous_element = None

for element in elements:
    if element != previous_element:
        new_elements.append(element)
        previous_element = element
print(new_elements)
