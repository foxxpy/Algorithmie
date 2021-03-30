def matrice_nulle(M, N):
    """Instancie une matrice nulle avec M lignes et N colonnes
    Ici, une matrice est une liste de listes"""

    matrice = []
    for i in range(M):
        matrice.append([0 for x in range(N)])
    return matrice
