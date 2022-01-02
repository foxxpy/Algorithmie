def multiplier_scalaire(liste, scalaire):

    liste_finale = []
    for element in liste:
        if type(element) is list:
            liste_finale.append(multiplier_scalaire(element, scalaire))

        else:
            liste_finale.append(element * scalaire)

    return liste_finale
    