def armstrong(n):
    """Détermine si n est un armstrong number ou non.
    Un armstrong number, c'est un nombre qui est égal à la somme du cube des chiffres
    qui le composent"""

    
    total = 0
    for chiffre in str(n):
        total += int(chiffre)**3

    return n == total
