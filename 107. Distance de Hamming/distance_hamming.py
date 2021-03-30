def distance_hamming(binaire1, binaire2):
    """Nombre de bits différents entre deux nombres binaires"""

    #Si les deux nombres binaires ne sont pas de mêmes longueurs, on lève une
    #assertionError
    assert len(binaire1) == len(binaire2)

    #Si 0b est dans binaire1 ou binaire2, on le retire
    if "0b" in binaire1:
        binaire1 = binaire1.replace("0b", "")

    if "0b" in binaire2:
        binaire2 = binaire2.replace("0b", "")

    distance = 0
    for i in range(0, len(binaire1)):
        if binaire1[i] != binaire2[i]:
            distance +=1

    return distance
