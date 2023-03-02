import sys

# En values tendremos una lista con los valores (como strings)
values = sys.argv[1:]

result = [int(value) for value in values]
sum = sum(values) 