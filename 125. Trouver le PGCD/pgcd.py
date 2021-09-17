def pgcd(x,y):
    """Renvoie le PGCD des nombres x et y"""

    if x < y:
        x, y = y, x

    #Si y est un diviseur de x, alors le PGCD est y
    if x % y == 0:
        return y

    #On recherche un diviseur commun en partant de y/2 en allant jusqu'à 0
    for k in range(y//2, 0, -1):
        if x % k == 0 and y % k == 0:
            return k
    
