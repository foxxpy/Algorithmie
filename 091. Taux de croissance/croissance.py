def croissance(valeur, pourcentage, n=1, entier=True):
    """Calcul les intérets en appliquant n fois le pourcentage"""
    
    interet = 0
    if entier:
        interet = valeur * (1+ (pourcentage/100))**n
    else:
        interet = valeur * (1 + pourcentage)**n

    return interet
