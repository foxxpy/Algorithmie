from math import *



def moyenne(liste):
    return (1/len(liste)) * sum(liste)



def variance(liste):
    moy = moyenne(liste)
    var = 0

    for nb in liste:
        var += (nb - moy)**2

    return var / len(liste)



def ecart_type(liste):
    moy = moyenne(liste)
    var = 0
    for nb in liste:
        var += (nb - moy)**2

    return sqrt(var/len(liste))
