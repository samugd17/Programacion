elements= [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]

flatten_elements = []
for element in elements:
    if type(element) == list:
        flatten_elements.extend(element)
    else:
        flatten_elements.append(element)

print(flatten_elements)
