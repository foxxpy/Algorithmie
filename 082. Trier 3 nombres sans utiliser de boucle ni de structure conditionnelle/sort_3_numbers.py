def sort_3_numbers(x,y,z):
    """Méthode qui trie 3 nombres sans structure conditionnelle"""

    a1 = min(x,y,z)
    a3 = max(x,y,z)
    a2 = x+y+z - a1 - a3

    return [a1,a2,a3]
