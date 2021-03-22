from sum_matrix import sum_matrix

matrix = [[1,1,1],[2,2,2]]
print(sum_matrix(matrix, True))
print(sum_matrix(matrix, False))

matrix = [[1,1,1],[1,1,1], [1,1,1]]
print(sum_matrix(matrix, True))
print(sum_matrix(matrix, False))

matrix = [[0,0], [4,4]]
print(sum_matrix(matrix, True))
print(sum_matrix(matrix, False))
