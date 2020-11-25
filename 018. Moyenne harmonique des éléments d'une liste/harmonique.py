#Moyenne harmonique : N / sum(1/ai)

def harmonique(liste):
    """Renvoie la moyenne harmonique des éléments d'une liste"""
    sum_liste = 0
    for nb in liste:
        sum_liste += (1/nb)

    return len(liste) / sum_liste
