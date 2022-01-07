def permanent_2(M):
    """Calcule le permanent d'une matrice carrée d'ordre 2"""

    return M[0][0] * M[1][1] + M[0][1] * M[1][0]