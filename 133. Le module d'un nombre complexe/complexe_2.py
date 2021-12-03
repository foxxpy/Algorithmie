def module_complexe(z):
    """Calcule le module du nombre complexe z"""

    sum_square = z[0]**2 + z[1]**2
    return sum_square**(1/2)



def print_complexe(z):
    """Affiche le nombre complexe z"""
    
    print("{} + {}i".format(z[0], z[1]))