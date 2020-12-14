#Pour une équation sous la forme ax+b=c, avec a différent de 0

def equation(a,b,c):
    """Résout une équation de degré 1 sous la forme ax+b=c"""
    solution = 0
    try:
        solution = (c-b)/a
        print("La solution est : {}".format(solution))

    except ZeroDivisionError:
        print("a doit être différent de 0 :)")
