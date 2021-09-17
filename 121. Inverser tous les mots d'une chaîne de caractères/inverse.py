def inverse(string):
    """Inverse l'ordre des lettres de tous les mots de la phrase"""

    return " ".join([word[::-1] for word in string.split(" ")])
