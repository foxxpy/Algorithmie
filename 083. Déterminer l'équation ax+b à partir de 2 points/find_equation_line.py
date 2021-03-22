def find_equation_line(x1, y1, x2, y2):
    """Détermine l'équation de la droite y = ax+b à partir de deux points appartenant
    à cette droite"""

    print("Point A : ({},{})".format(x1, y1))
    print("Point B : ({},{})".format(x2, y2))

    a = (y1 - y2) / (x1 - x2)
    b = y2 - a*x2
    print("L'équation est {}x+{}".format(a, b))

    return a, b
    
