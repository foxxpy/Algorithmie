def transpose(matrix):
    """Renvoie la transposée d'une matrice"""

    result_matrix = []

    for col in range(len(matrix[0])):
        line_matrix = []
        for line in range(len(matrix)):
            line_matrix.append(matrix[line][col])
        result_matrix.append(line_matrix)

    return result_matrix



def produit_scalaire(A, B):
    """Calcule le produit scalaire de deux matrices"""

    if len(A[0]) != len(B):
        return None

    result_matrix = []
    for line in A:
        line_matrix = []
        for col_B in transpose(B):
            result = 0
            for i, a in enumerate(line):
                result += a * col_B[i]
            line_matrix.append(result)
        result_matrix.append(line_matrix)

    return result_matrix