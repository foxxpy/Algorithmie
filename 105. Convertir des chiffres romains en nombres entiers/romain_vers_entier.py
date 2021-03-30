def romain_vers_entier(romain):
    """Convertit un nombre romain en nombre entier
    Leetcode 13"""

    double = {"CM" : 900, "CD" : 400, "XC" : 90, "XL" : 40, "IX" : 9, "IV" : 4}
    unique = {"M" : 1000, "D" : 500, "C" : 100, "L" : 50, "X" : 10, "V" : 5, "I" : 1}

    entier = 0
    i = 0

    #Tant qu'on a pas parcouru le nombre romain en entier
    while i < len(romain):
        if i < len(romain) - 1 and romain[i:i+2] in double:
            entier += double[romain[i:i+2]]
            i += 2
        else:
            entier += unique[romain[i]]
            i += 1
    return entier
