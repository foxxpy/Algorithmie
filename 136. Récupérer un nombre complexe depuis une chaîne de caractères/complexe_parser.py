def string_to_complex(string):
    """Renvoie la valeur réelle et la valeur imaginaire d'un nombre complexe dans deux variables distinctes
    :type string: str - Nombre complexe contenu dans une chaîne de caractères
    :rtype: tuple(int, int)
    """
    #On retire les espaces
    string = string.replace(" ", "")
    reel, im = 0, 1j
    i = 0
    while i < len(string):
        if i != 0 and string[i] in ["+", "-"]:
            #Si string[i] est égal à "+" ou "-" et que le caractère précédent est un "e", on ne casse pas la boucle, on continue
            if i > 0 and string[i-1] != "e":
                break
        i += 1

    #Si la première partie de la chaîne de caractères contient le i ou le j
    if "i" in string[:i] or "j" in string[:i]:
        im = 0 if len(string[:i]) == 0 else float(string[:i].replace("i", "").replace("j", ""))
        reel = 0 if len(string[i:]) == 0 else float(string[i:])

    #Si la seconde partie de la chaîne de caractères contient le i ou le j
    elif "i" in string[i:] or "j" in string[i:]:
        print(string[:i], string[i:])
        im = 0 if len(string[i:]) == 0 else float(string[i:].replace("i", "").replace("j", ""))
        reel = 0 if len(string[:i]) == 0 else float(string[:i])

    #Si il n'y a pas de i ou de j
    else:
        reel = float(string)
        im = 0

    return reel, im



def string_to_complex_2(string):
    """Renvoie un nombre complexe dans un objet 'complex' de Python
    :type string: str
    :rtype: Complex
    """

    string = string.replace(" ", "").replace("i", "j")
    return complex(string)
    
    