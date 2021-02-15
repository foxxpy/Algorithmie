def elements_uniques(liste):
    """Renvoie True si la liste contient que des éléments uniques, renvoie False sinon"""

    if len(liste) == len(list(set(liste))):
        return True

    else:
        return False
