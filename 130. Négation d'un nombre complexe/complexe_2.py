def negation_complexe(z):
    """Calcule la négation d'un nombre complexe"""

    return (-z[0], -z[1])

def print_complexe(z):
    """Affiche le nombre complexe z"""
    
    print("{} + {}i".format(z[0], z[1]))