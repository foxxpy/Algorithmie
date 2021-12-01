def conjugue_complexe(z):
    """Calcule le conjugué d'un nombre complexe z"""

    return (z[0], -z[1])



def print_complexe(z):
    """Affiche le nombre complexe z"""
    
    print("{} + {}i".format(z[0], z[1]))