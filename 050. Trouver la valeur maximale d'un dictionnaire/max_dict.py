def max_dict(dictionnaire):
    """Retourne la valeur maximale d'un dictionnaire"""
    
    max_value = 0
    for i, value in enumerate(dictionnaire.values()):
        if i == 0 or value > max_value:
            max_value = value

    return max_value
