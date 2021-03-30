def poids_hamming(binaire):
    """Renvoie le nombre de 1 contenu dans un nombre binaire."""

    return binaire.count("1")



def poids_hamming_leetcode(binaire):
    """Renvoie le nombre de 1 contenu dans un nombre binaire. Leetcode : 191"""

    return sum(bit == "1" for bit in binaire[2:])
