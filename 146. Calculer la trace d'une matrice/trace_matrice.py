def trace(M):
    """Renvoie la trace d'une matrice"""

    T = 0
    
    if len(M) < len(M[0]):
        calc_range = len(M)
    else:
        calc_range = len(M[0])

    for i in range(calc_range):
        T += M[i][i]

    return T