def min_dict(dictionnaire):
    """Retourne la valeur minimale d'un dictionnaire"""
    
    min_value = 0
    for i, value in enumerate(dictionnaire.values()):
        if i == 0 or value < min_value:
            min_value = value

    return min_value
