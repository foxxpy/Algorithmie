def switch_value_temp(a,b):
    """Echange les valeurs de 2 variables en utilisant une variable temporaire"""
    temp = a
    a = b
    b = temp
    return a, b

def switch_value_addition(a,b):
    """Echange les valeurs de 2 variables grâce à l'arithmétique"""
    a = a + b
    b = a - b
    a = a - b
    return a, b

def switch_value_python(a,b):
    """Echange les valeurs de 2 variables de manière pythonesque"""
    a, b = b, a
    return a, b
