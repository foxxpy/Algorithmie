def determinant_3(M):
    """Calcule le déterminant d'une matrice carrée d'ordre 3"""

    aei = M[0][0] * M[1][1] * M[2][2]
    bfg = M[0][1] * M[1][2] * M[2][0]
    cdh = M[0][2] * M[1][0] * M[2][1]
    ceg = M[0][2] * M[1][1] * M[2][0]
    bdi = M[0][1] * M[1][0] * M[2][2]
    afh = M[0][0] * M[1][2] * M[2][1]

    return aei + bfg + cdh - ceg - bdi - afh