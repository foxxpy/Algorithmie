def tribonacci(n):
    """La suite de tribonacci est comme la suite de fibonacci sauf qu'on fait la somme
    des 3 chiffres précédents dans la suite."""

    serie = [0,1,1]
    while len(serie) <= n:
        serie.append(sum(serie[-3:]))
    return serie[n]
