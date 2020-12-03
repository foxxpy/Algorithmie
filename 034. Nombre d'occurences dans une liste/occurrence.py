def occurrence(liste, to_find):
    """Compte le nombre d'occurrence d'un élément dans une liste."""
    total = 0
    for element in liste:
        if element == to_find:
            total += 1
    return total
