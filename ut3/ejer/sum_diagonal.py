matrix = [[4, 6, 1], [2, 9, 3], [1, 7, 7]]
size = len(matrix)
sum_diagonal = 0

for i in range(size):
    value = matrix [i] [i]
    sum_diagonal += value
print(sum_diagonal)
