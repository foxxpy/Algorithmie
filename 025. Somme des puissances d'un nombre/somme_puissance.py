def puissance(n, p):
    """Renvoie n**p"""
    if p==0:
        return 1
    elif p==1:
        return n
    else:
        total=1
        for i in range(p):
            total *= n
        return total

def somme_puissance(nb, k):
    total = 0
    for i in range(k):
        total += puissance(nb, i)
    return total
