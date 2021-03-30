def happy(n):
    """Teste le nombre n est un nombre heureux ou non."""
    if n<10:
        n = n**2

    #Tant que l'addition des carrés n'a pas atteint un seul chiffre, on continue
    while n > 9:
        total = 0
        for digit in str(n):
            total += int(digit)**2
        n = total

    return n == 1
