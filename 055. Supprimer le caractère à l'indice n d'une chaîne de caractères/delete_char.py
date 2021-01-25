def delete_char(string, n):
    """Supprime le caractère à l'indice n de la chaîne de caractères string"""
    return string[0:n] + string[n+1:]
