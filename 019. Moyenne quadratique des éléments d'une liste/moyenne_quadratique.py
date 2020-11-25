from math import *

def quadratique(liste):
    """Renvoie la moyenne quadratique des éléments d'une liste"""
    sum_liste = 0
    for nb in liste:
        sum_liste += nb**2
    return sqrt(sum_liste/len(liste))

