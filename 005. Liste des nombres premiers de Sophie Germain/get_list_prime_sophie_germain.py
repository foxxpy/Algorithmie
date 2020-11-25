def is_prime(n):
    """Teste si un nombre est premier. Renvoie True si il l'est, False sinon"""
    for d in range(2,n):
        if n % d == 0:
            return False
    return True

def is_prime_sophie_germain(n):
    """Teste si un nombre est un nombre premier de Sophie Germain"""
    if is_prime(n) and is_prime(2*n + 1):
        return True
    else:
        return False

def get_list_primes_sophie_germain(inf, sup):
    """Renvoie la liste des nombres premiers de Sophie Germain présents dans
    un intervalle [inf, sup]"""
    list_primes_sophie_germain = []
    for num in range(inf, sup+1):
        if is_prime_sophie_germain(num):
            list_primes_sophie_germain.append(num)

    return list_primes_sophie_germain

print(is_prime_sophie_germain(2))
print(is_prime_sophie_germain(3))
print(is_prime_sophie_germain(5))
print(is_prime_sophie_germain(12))
print(is_prime_sophie_germain(4055))

print(get_list_primes_sophie_germain(1, 100))
print(get_list_primes_sophie_germain(1, 500))
print(get_list_primes_sophie_germain(1, 1000))
