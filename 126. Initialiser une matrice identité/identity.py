def identity(n):
    """Créée une matrice identité de taille nxn"""

    matrix = []
    for i in range(n):
        line = []
        for j in range(n):
            if i == j:
                line.append(1)
            else:
                line.append(0)
        matrix.append(line)

    return matrix



def matrice_nulle(M, N):
    """Instancie une matrice nulle avec M lignes et N colonnes
    Ici, une matrice est une liste de listes"""

    matrice = []
    for i in range(M):
        matrice.append([0 for x in range(N)])
    return matrice



def alt_identity(n):
    """Créée une matrice identité de taille nxn"""

    matrix = matrice_nulle(n,n)
    for i in range(n):
        matrix[i][i] = 1

    return matrix
