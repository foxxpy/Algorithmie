def afficher_alphabet(majuscule=True, endprint=True):
    """Affiche les lettres de l'alphabet. En majuscule si majuscule == True,
    en minuscule sinon.
    Ajoute un espace à la fin si endprint == True."""
    
    start = 65 if majuscule else 97
    for i in range(26):
        print(chr(start+i), end="")

    if endprint:
        print()



def return_alphabet(majuscule=True):
    """Renvoie une liste contenant toutes les lettres de l'alphabet"""
    
    start = 65 if majuscule else 97
    alphabet = list()
    for i in range(26):
        alphabet.append(chr(start+i))

    return alphabet
