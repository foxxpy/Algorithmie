def max_list(liste):
    """Renvoie la valeur maximale d'une liste"""
    maximum = liste[0]
    for i in range(1, len(liste)):
        if maximum < liste[i]:
            maximum = liste[i]
    return maximum

def recursion_max_list(liste, i=0, max_liste=0):
    """Renvoie la valeur maximale d'une liste"""
    if i < len(liste):
        if i == 0 or liste[i] > max_liste:
            max_liste = liste[i]
        max_liste = recursion_max_list(liste, i+1, max_liste)
    return max_liste
