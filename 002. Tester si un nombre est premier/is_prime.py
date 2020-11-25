def is_prime(n):
    """Renvoie un booléen indiquant si le nombre n est un nombre premier (True)
    ou non (False)"""
    for d in range(2,n):
        if n % d == 0:
            return False
    return True
