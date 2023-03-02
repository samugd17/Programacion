str1 = "0001010011101"
str2 = "0000110010001"
hamming_distance = 0
letter = 0

while letter < len(str1):
    if str1[letter] != str2[letter]:
        hamming_distance += 1
    letter += 1
print(hamming_distance)
