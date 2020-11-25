def fibonacci(n):
    """Renvoie le n-ème terme de la suite de Fibonacci en utilisant la mémoïsation"""
    global values
    
    if not n in values.keys():
        values[n] = fibonacci(n-1)+ fibonacci(n-2)
    return values[n]
    

values = {1 : 1, 2 : 1}
