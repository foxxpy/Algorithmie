def plower(string):
    """Renvoie la chaîne de caractères string entièrement en minuscule"""
    new_string = ""
    for lettre in string:
        #Si la lettre est en majuscule
        if 65 <= ord(lettre) <= 90:
            new_string += chr(ord(lettre)+32)

        #Si c'est une lettre avec un accent
        elif lettre in ["À","Â","Ä","Ù","Ü","Û","É","È","Ê","Ë","Ô","Ö"]:
            new_string += chr(ord(lettre)+32)

        else:
            new_string += lettre

    return new_string
            
def pupper(string):
    """Renvoie la chaîne de caractères string entièrement en minuscule"""
    new_string = ""
    for lettre in string:
        #Si la lettre est en minuscule
        if 97 <= ord(lettre) <= 122:
            new_string += chr(ord(lettre)-32)

        #Si c'est une lettre avec un accent
        elif lettre in ["à", "â", "ä","ù","ü","û","é","è","ê", "ë","ô","ö"]:
            new_string += chr(ord(lettre)-32)

        else:
            new_string += lettre

    return new_string
