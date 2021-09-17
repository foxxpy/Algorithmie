from math import factorial

def coefficient_binomial(n, p):
    """Calcule le coefficient binomial"""
    
    return factorial(n) / (factorial(p) * factorial(n-p))



def display_coefficient_binomial(n,p):
    """Affiche l'égalité du calcul du coefficient binomial"""

    print("{}!/({}!*({} - {})!) = {}".format(n, p, n, p, coefficient_binomial(n,p)))
