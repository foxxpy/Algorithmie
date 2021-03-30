def is_evil(n):
    """Un evil number, c'est un nombre dont l'écriture binaire possède un nombre
    pair de 1"""

    count = 0
    #On applique la méthodologie qui permet de convertir un nombre entier en binaire
    while n != 0:
        if (n%2 == 1):
            count += 1
        n = n //2

    if count % 2 == 0:
        return True
    else:
        return False



def is_evil_bin(n):
    """Un evil number, c'est un nombre dont l'écriture binaire possède un nombre
    pair de 1"""

    n = bin(n).replace("0b", "")
    if n.count("1") % 2 == 0:
        return True
    else:
        return False
