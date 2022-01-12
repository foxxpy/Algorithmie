def flatten_recursif(liste):
    """Applatit une liste en utilisant la récursivité"""

    final_liste = []
    for element in liste:
        if type(element) is list:
            final_liste += flatten_recursif(element)
        else:
            final_liste.append(element)

    return final_liste



def flatten_recursif_short(liste):
    """Applatit une liste en utilisant la récursivité : code obtenu sur http://www.rosettacode.org/wiki/Flatten_a_list#Python"""

    return sum(([x] if not isinstance(x,list) else flatten_recursif_short(x) for x in liste), [])



def flatten(liste):
    """Applatit une liste de listes de profondeur 2 avec une méthode itérative."""

    return [element for sousliste in liste for element in sousliste]