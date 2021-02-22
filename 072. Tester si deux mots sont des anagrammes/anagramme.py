def anagramme(string1, string2):
    """Teste si deux mots sont des anagrammes. Renvoie True si ils sont des anagrammes,
    renvoie False sinon"""

    #Si les deux mots n'ont pas la même longueur, on sait d'avance qu'ils ne sont
    #pas des anagrammes
    if len(string1) != len(string2):
        return False
    
    if sort(string1.upper()) == sort(string2.upper()):
        return True
    else:
        return False
