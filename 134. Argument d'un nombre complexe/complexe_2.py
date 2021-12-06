import math

def module_complexe(z):
    """Calcule le module du nombre complexe z"""

    sum_square = z[0]**2 + z[1]**2
    return sum_square**(1/2)


def argument_complexe(z, degree=True):
    """Calcule l'argument du nombre complexe z"""

    arg = math.acos(z[0] / module_complexe(z))
    if z[1] < 0:
        arg = -arg
    
    if degree:
        return math.degrees(arg)
    return arg


def print_complexe(z):
    """Affiche le nombre complexe z"""
    
    print("{} + {}i".format(z[0], z[1]))