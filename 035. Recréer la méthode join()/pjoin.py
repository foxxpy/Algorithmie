def pjoin(char, liste):
    """Méthode join() des chaînes de caractères recodée en Python"""
    final_string = str()
    length_char = len(char)
    for element in liste:
        final_string = final_string + element + char

    if length_char == 0:
        return final_string
    else:
        return final_string[:-length_char]
