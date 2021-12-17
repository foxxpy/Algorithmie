import math

def produit_hadamard(matrix_a, matrix_b):
    """Renvoie le produit d'Hadamard de deux matrices sous forme de liste de listes.
    :type matrix_a: list[list[float]]
    :type matrix_b: list[list[float]]
    :rtype: list[list[float]]
    """

    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        return None

    result_matrix = list()
    for i in range(len(matrix_a)):
        matrix_line = []
        for j in range(len(matrix_a[i])):
            matrix_line.append(matrix_a[i][j] * matrix_b[i][j])
        result_matrix.append(matrix_line)

    return result_matrix



def produit_hadamard_2(matrix_a, matrix_b):
    """Renvoie le produit d'Hadamard de deux matrices sous forme de liste de listes.
    :type matrix_a: list[list[float]]
    :type matrix_b: list[list[float]]
    :rtype: list[list[float]]
    """

    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        return None

    new_matrix = []
    for i in range(len(matrix_a)):
        line = [math.prod(x) for x in zip(matrix_a[i], matrix_b[i])]
        new_matrix.append(line)

    return new_matrix