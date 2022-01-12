def is_toeplitz(matrix):
    """Renvoie True si la matrice envoyée en paramètre est une matrice de Toeplitz."""

    rows, cols = len(matrix), len(matrix[0])

    for row in range(rows - 1):
        for col in range(cols - 1):
            if matrix[row][col] != matrix[row+1][col+1]:
                return False

    return True
