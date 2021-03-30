from math import sqrt

def sunny(n):
    """Un sunny number est un nombre qui a une racine carrée parfaite quand on
    lui ajoute 1"""
    
    x = sqrt(n+1)
    return int(x) == x



def sunny_interval(inf, sup):
    """Cherche tous les sunny numbers dans un intervalle [inf, sup]"""

    sunny_numbers = list()
    for i in range(inf, sup+1):
        if sunny(i):
            print("{} est un sunny number".format(i))
            sunny_numbers.append(i)
    return sunny_numbers
