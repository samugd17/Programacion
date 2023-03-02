BIN_N = "1101"
exponent = 0

for digit in BIN_N:
    ndigit = int(digit)
    print(ndigit * 2**exponent)
    exponent += 1


BIN_N = "1101"
bin_size = len(BIN_N)
result = 0

for i in range(bin_size):
    digit = int(BIN_N[i])
    exponent = bin_size - i - 1
    partial_result = digit * 2**exponent
    result = partial_result
    result += partial_result
    print(f"{digit} * 2^{exponent} = {partial_result}")

print(result)
