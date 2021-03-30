def ugly(n):
    if n <= 0:
        return False
    
    #Tant que n est divisible par 2, on le divise par 2
    while n % 2 == 0:
        n //= 2

    #Tant que n est divisible par 3, on le divise par 3
    while n % 3 ==0:
        n //= 3

    #Tant que n est divisible par 5, on le divise par 5
    while n % 5 == 0:
        n //=5

    return n == 1



def ugly_interval(inf, sup):
    """Donne tous les ugly numbers dans un intervalle [inf, sup]"""

    list_ugly_numbers = []
    for i in range(inf, sup+1):
        if ugly(i):
            list_ugly_numbers.append(i)
    return list_ugly_numbers

print(ugly_interval(1,100))
