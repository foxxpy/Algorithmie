import itertools

def produit_cartesien(v1, v2):
    """Calcule le produit cartésien de deux vecteurs (deux listes ici)"""
    vecteur_final = []
    for element in v1:
        for element_2 in v2:
            vecteur_final.append([element, element_2])

    return vecteur_final



def produit_cartesien_short(v1, v2):
    return [[x0, y0] for x0 in v1 for y0 in v2]



def cartesien_itertools(v1, v2):
    """Calcule le produit cartésien en utilisant la méthode product() du module itertools"""

    vecteur_final = []

    for element in itertools.product(v1,v2):
        vecteur_final.append(element)

    return vecteur_final