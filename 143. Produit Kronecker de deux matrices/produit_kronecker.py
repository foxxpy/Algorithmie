def multiplier_scalaire(liste, scalaire):

    liste_finale = []
    for element in liste:
        if type(element) is list:
            liste_finale.append(multiplier_scalaire(element, scalaire))

        else:
            liste_finale.append(element * scalaire)

    return liste_finale



def produit_kronecker(A, B):
    """Calcule le produit de Kronecker entre la matrice A et la matrice B"""

    final_matrix = []

    for line in A:
        for line_B in B:
            line_matrix = []
            for col in line:
                for col_b in line_B:
                    line_matrix.append(col * col_b)
            final_matrix.append(line_matrix)

    return final_matrix

