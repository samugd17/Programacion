matrix = [[4, 6, 1], [2, 9, 3], [1, 7, 7]]
size = len(matrix)
main_diagonal = []

for i in range(size):
    main_diagonal.append(matrix[i][i])
    sum_diagonal = sum(main_diagonal)
print(sum_diagonal)