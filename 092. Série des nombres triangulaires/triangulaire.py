def triangulaire(n):
    """Renvoie le n-ème nombre triangulaire"""
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def recursion_triangulaire(n, i=1):
    """Renvoie le n-ème nombre triangulaire"""
    total = i
    if n > 1:
        total += recursion_triangulaire(n-1, i+1)

    return total
        
