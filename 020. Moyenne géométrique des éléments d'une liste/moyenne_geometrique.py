def geometrique(liste):
    """Renvoie la moyenne géométrique des éléments d'une liste"""
    product_list = 1
    for nb in liste:
        product_list *= nb

    return product_list**(1/len(liste))
