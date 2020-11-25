def reverse_recurrence(string):
    """Inverse une chaîne de caractères par récurrence"""
    new_string = ""
    if string != "":
        new_string = reverse_recurrence(string[1:]) + string[0]
    return new_string



def reverse_loop(string):
    """Inverse une chaîne de caractères en utilisant une boucle"""
    new_string = ""
    for letter in string:
        new_string = letter + new_string
    return new_string



def reverse_join(string):
    """Inverse une chaîne de caractères grâce à la méthode join()"""
    string = "".join(reversed(string))
    return string



def reverse_python(string):
    """Inverse une chaîne de caractères de manière pythonesque"""
    return string[::-1]
