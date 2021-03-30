from factorial import factorial

def strong_number(n):
    """Détermine si n est un strong number ou non.
    Strong number : nombre dont la somme des valeurs factorielles de ses chiffres
    est égale à ce nombre"""

    total = 0
    for chiffre in str(n):
        total += factorial(int(chiffre))

    return total == n

    
