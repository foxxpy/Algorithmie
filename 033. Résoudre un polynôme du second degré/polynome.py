from math import *

def discriminant(a,b,c):
    """Calcul le discriminant du polynôme du second degré"""
    return b**2 - 4*a*c

def polynome(a,b,c):
    """Retourne la solution du polynôme du second degré"""
    delta = discriminant(a,b,c)
    if delta < 0:
        return None, None
    elif delta == 0:
        return -b / (2*a), None
    else:
        x1 = (-b+sqrt(delta))/2*a
        x2 = (-b-sqrt(delta))/2*a
        return x1, x2
