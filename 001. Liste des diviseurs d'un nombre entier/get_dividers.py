def get_dividers(n):
    """Renvoie la liste des diviseurs du nombre entier n envoyé en paramètre"""
    dividers_list = []
    for divider in range(1, n+1):
        if n % divider == 0:
            dividers_list.append(divider)

    return dividers_list
