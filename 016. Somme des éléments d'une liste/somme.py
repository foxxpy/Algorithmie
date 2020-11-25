def somme(liste):
    """Calcul la somme des éléments d'une liste"""
    total = 0
    for nombre in liste:
        total += nombre
    return total

def somme_recursion(liste, indice=0):
    """Calcul la somme des éléments d'une liste par récursion"""
    total = 0
    if indice < len(liste):
        total = liste[indice]
        total += somme_recursion(liste, indice+1)

    return total
