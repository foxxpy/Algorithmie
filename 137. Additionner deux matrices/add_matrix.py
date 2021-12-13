import numpy as np

def add_matrix_basic(matrix_a, matrix_b):
    """Additionner les deux matrices envoyées en paramètres.
    :type matrix_a: list[list[float]]
    :type matrix_b: list[list[float]]
    :rtype: list[list[float]]
    """

    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        return None

    new_matrix = []

    for line in range(len(matrix_a)):
        line_matrix = []
        for col in range(len(matrix_a[line])):
            line_matrix.append(matrix_a[line][col] + matrix_b[line][col])
        new_matrix.append(line_matrix)

    return new_matrix


def add_matrix(matrix_a, matrix_b):
    """Additionner les deux matrices envoyées en paramètres.
    :type matrix_a: list[list[float]]
    :type matrix_b: list[list[float]]
    :rtype: list[list[float]]
    """
    
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        return None

    new_matrix = []
    for i in range(len(matrix_a)):
        line = [sum(x) for x in zip(matrix_a[i], matrix_b[i])]
        new_matrix.append(line)

    return new_matrix
            


def add_matrix_np(matrix_a, matrix_b):
    """Additionner les deux matrices envoyées en paramètres.
    :type matrix_a: ndarray
    :type matrix_b: ndarray
    :rtype: ndarray
    """
    
    matrix_a = np.array(matrix_a)
    matrix_b = np.array(matrix_b)

    return matrix_a + matrix_b
