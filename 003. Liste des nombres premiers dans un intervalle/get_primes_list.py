def is_prime(n):
    """Renvoie un booléen indiquant si le nombre n est un nombre premier (True)
    ou non (False)"""
    for d in range(2,n):
        if n % d == 0:
            return False
    return True

def get_primes_list(inf, sup):
    """Renvoie la liste des nombres premiers compris dans l'intervalle [inf, sup]"""
    primes_list = []
    for num in range(inf, sup+1):
        if is_prime(num):
            primes_list.append(num)
    return primes_list
