def concatenate(liste1, liste2):
    """Concatène deux listes et renvoie la nouvelle liste créée"""
    new_list = list()

    for liste in [liste1, liste2]:
        for element in liste:
            new_list.append(element)

    return new_list
