input_text = "Supercalifragilisticoespialidoso"
num_vowels = 0

for letter in input_text:
    if letter == "a":
        num_vowels += 1
    if letter == "e":
        num_vowels += 1
    if letter == "i":
        num_vowels += 1
    if letter == "o":
        num_vowels += 1
    if letter == "u":
        num_vowels += 1
print(num_vowels)
