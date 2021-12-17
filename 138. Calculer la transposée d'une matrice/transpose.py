def transpose(matrix):
    """Renvoie la transposée d'une matrice
    :type matrix: list[list[float]]
    :rtype: list[list[float]]
    """

    result_matrix = []

    for col in range(len(matrix[0])):
        line_matrix = []
        for line in range(len(matrix)):
            line_matrix.append(matrix[line][col])
        result_matrix.append(line_matrix)

    return result_matrix