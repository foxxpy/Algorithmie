def countAndSay(n):
    """Donne la n-ème ligne de la suite de Conway"""

    sequence = [1]

    for _ in range(n-1):
        suivant = []
        for num in sequence:
            if not suivant or suivant[-1] != num:
                suivant += [1, num]
            else:
                suivant[-2] += 1
        sequence = suivant

    return "".join(map(str, sequence))
