from math import prod

def spy_numbers(n):
    """Teste si un nombre est un nombre espion ou non.
    Un nombre espion est un nombre dont le produit de ses chiffres est égal
    à la somme de ses chiffres"""
    
    sum_n = sum(map(int, list(str(n))))
    product_n = prod(map(int, list(str(n))))
    return sum_n == product_n
