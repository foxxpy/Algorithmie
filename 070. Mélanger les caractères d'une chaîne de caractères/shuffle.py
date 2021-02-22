from random import randint, shuffle
import string_utils


def shuffle_string(string):
    """Mélange les caractères d'une chaîne de caractères"""

    new_string = ""
    while(len(string) > 0):
        random_digit = randint(0, len(string)-1)
        new_string += string[random_digit]
        string = string[:random_digit] + string[random_digit+1:]

    return new_string



def shuffle_string_2(string):
    """Mélange les caractères d'une chaîne de caractères avec la méthode shuffle
    du module random"""
    liste = list(string)
    shuffle(liste)
    return "".join(liste)



def shuffle_string_utils(string):
    """Mélange les caractères d'une chaîne de caractères avec la méthode shuffle
    du module string_utils
    Ne pas oublier d'installer python-string-utils avec pip"""

    return string_utils.shuffle(string)
