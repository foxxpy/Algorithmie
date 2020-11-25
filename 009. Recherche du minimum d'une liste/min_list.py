def min_list(liste):
    """Renvoie la valeur minimale d'une liste"""
    minimum = liste[0]
    for i in range(1, len(liste)):
        if minimum > liste[i]:
            minimum = liste[i]
    return minimum

def recursion_min_list(liste, i=0, min_liste=0):
    """Renvoie la valeur minimale d'une liste"""
    if i < len(liste):
        if i == 0 or liste[i] < min_liste:
            min_liste = liste[i]
        min_liste = recursion_min_list(liste, i+1, min_liste)
    return min_liste

