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

def recursion_puissance(n, p):
    """Renvoie n**p calculé par récursion"""
    if p==0:
        return 1
    elif p==1:
        return n
    else:
        return recursion_puissance(n, p-1)*n
