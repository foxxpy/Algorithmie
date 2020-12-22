def only_alphabet(string):
    """Teste si une chaîne de caractères ne contient que des lettres de l'alphabet"""
    
    for char in string:
        #Si c'est pas une majuscule, ni une minuscule, ni une lettre avec accent
        if not 65 <= ord(char) <= 90 and \
        not 97 <= ord(char) <= 122 and \
        not 192 <= ord(char) <= 214 and \
        not 216 <= ord(char) <= 254:
            return False

    return True
