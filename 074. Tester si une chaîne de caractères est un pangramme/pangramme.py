from no_accent import no_accent_word
from retirer_ponctuation import retirer_ponctuation

def pangramme(string):
    """Détermine si la chaine de caractères est un pangramme.
    Un pangramme est une phrase qui contient toutes les lettres de l'alphabet."""

    #On retire les accents, les ponctuations et on passe le texte en majuscule
    string = retirer_ponctuation(string)
    string = no_accent_word(string)
    string = string.upper()

    if "œ".upper() in string:
        string = string.replace("œ".upper(), "oe".upper())

    #Si la longueur du set est de 26, c'est qu'on a toutes les lettres de l'alphabet
    if len(set(string)) == 26:
        return True
    else:
        return False
