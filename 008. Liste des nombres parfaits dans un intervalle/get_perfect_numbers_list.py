def get_dividers(nb):
    """Renvoie la liste des diviseurs du nombre nb"""
    dividers_list = []
    for divider in range(1, nb+1):
        if nb % divider == 0:
            dividers_list.append(divider)

    return dividers_list

def is_perfect(nb):
    """Renvoie True si nb est un nombre parfait, False sinon."""
    if sum(get_dividers(nb)[:-1]) == nb:
        return True
    else:
        return False
    

def get_perfect_numbers_list(inf, sup):
    """Renvoie la liste des nombres parfaits dans l'intervalle [inf,sup]"""
    perfect_numbers_list = []
    for n in range(inf, sup+1):
        if is_perfect(n):
            perfect_numbers_list.append(n)
    return perfect_numbers_list

print(get_perfect_numbers_list(1, 1000))
