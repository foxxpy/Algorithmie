def vector_add(vector1, vector2):
    """Calcule la somme de deux vecteurs"""

    #Si les vecteurs ont une longueur différentes, on ne peut pas calculer la somme
    if len(vector1) != len(vector2):
        return None
    
    new_vector = list()
    for i in range(len(vector1)):
        new_vector.append(vector1[i] + vector2[i])

    return new_vector

    
