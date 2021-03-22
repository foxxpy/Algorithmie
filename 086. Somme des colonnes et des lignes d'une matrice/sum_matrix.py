def sum_matrix(matrix, column=False):
    if not column:
        matrix_line = []
        for line in matrix:
            matrix_line.append(sum(line))
        return matrix_line

    else:
        matrix_column = []
        M = len(matrix)
        N = len(matrix[0])
        for i in range(N):
            total = 0
            for j in range(M):
                total += matrix[j][i]
            matrix_column.append(total)
        return matrix_column
