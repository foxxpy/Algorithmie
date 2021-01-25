def two_lists_to_dict(liste1, liste2):
    """Fusionne deux listes pour les renvoyer dans un dictionnaire
    Les éléments de la première liste seront les clés du dictionnaire.
    Les éléments de la seconde liste seront les valeurs du dictionnaire"""

    #Si les listes n'ont pas la même longueur, on ne renvoie rien
    if len(liste1) != len(liste2):
        return None
    
    else:
        dictionnaire = dict()
        for i in range(len(liste1)):
            dictionnaire[liste1[i]]  = liste2[i]

        return dictionnaire
