#Codée à l'épisode 22
def factorial(nb):
    """Calcul nb!"""
    product = 1
    for num in range(1, nb+1):
        product *= num

    return product

def euler(n):
    euler_number = 0
    for i in range(n):
        euler_number += 1/factorial(i)
    return euler_number
