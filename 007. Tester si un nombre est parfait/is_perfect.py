#Un nombre parfait est égal à la somme de ses diviseurs stricts

def get_dividers(nb):
    """Renvoie la liste des diviseurs du nombre nb"""
    dividers_list = []
    for divider in range(1, nb+1):
        if nb % divider == 0:
            dividers_list.append(divider)

    return dividers_list

def is_perfect(nb):
    """Teste si un nombre est parfait (True) ou non (False)."""
    print(get_dividers(28))
    if sum(get_dividers(nb)[:-1]) == nb:
        return True
    else:
        return False

print(is_perfect(28))
