def is_prime(nb):
    """Teste si nb est un nombre premier. Renvoie True si il est premier
    ou False sinon"""
    if nb < 2:
        return False
    for d in range(2,nb):
        if nb % d == 0:
            return False
    return True

def get_dividers(nb):
    """Retourne la liste des diviseurs du nombre nb"""
    dividers_list = []
    for divider in range(1, nb+1):
        if nb % divider == 0:
            dividers_list.append(divider)

    return dividers_list

def get_prime_dividers(nb):
    """Retourne la liste des diviseurs du nombre nb qui sont premiers"""
    dividers_prime_list = []
    for divider in get_dividers(nb):
        if is_prime(divider):
            dividers_prime_list.append(divider)

    return dividers_prime_list
