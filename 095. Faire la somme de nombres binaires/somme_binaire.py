def somme_binaire(binaire1, binaire2):
    """Renvoie la somme de deux nombres binaires dans une chaîne de caractères"""
    if "0b" in binaire1:
        binaire1 = binaire1.replace("0b", "")

    if "0b" in binaire2:
        binaire2 = binaire2.replace("0b", "")

    somme = int(binaire1, 2) + int(binaire2, 2)

    return bin(somme)
