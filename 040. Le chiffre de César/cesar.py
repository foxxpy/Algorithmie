def cryptage(cle, lettre):
    """Encode une lettre grâce à une clé. L'encodage est le déplacement
    de la lettre dans l'alphabet par rapport à la valeur de la clé"""
    
    #Si la lettre est en majuscule
    if 65 <= ord(lettre) <= 90:
        return chr(65 + (ord(lettre)-65+cle) % 26)

    #Si la lettre est en minuscule
    elif 97 <= ord(lettre) <= 122:
        return chr(97 + (ord(lettre)-97+cle) % 26)
        
    #Si ce n'est pas une lettre
    else:
        return lettre



def cesar(cle, mot):
    """Encode un mot avec le chiffre de César"""
    
    mot_crypte = ""
    for lettre in mot:
        mot_crypte += cryptage(cle, lettre)

    return mot_crypte
