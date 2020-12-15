def is_numeric(text):
    """Renvoie True si une chaîne de caractères ne contient que des nombres.
    Sinon renvoie False."""
    
    text_is_numeric = True
    for char in text:
        if not 47 < ord(char) < 58:
            text_is_numeric = False
            break

    return text_is_numeric
