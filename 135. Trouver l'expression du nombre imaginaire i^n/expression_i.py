def power_i(n):
    """Renvoie la valeur de i à la puissance n.
    :type n: int
    :rtype: Complex
    """
    if n % 4 == 1:
        return 1j

    elif n % 4 == 2:
        return -1 + 0j

    elif n % 4 == 3:
        return -1j

    else:
        return 1 + 0j