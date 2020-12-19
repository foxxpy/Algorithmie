def doublon(liste):
    """Enlève les doublons dans une liste en conservant l'ordre d'apparition
    des éléments"""
    liste_sans_doublon = list()
    for element in liste:
        if not element in liste_sans_doublon:
            liste_sans_doublon.append(element)
            
    return liste_sans_doublon
