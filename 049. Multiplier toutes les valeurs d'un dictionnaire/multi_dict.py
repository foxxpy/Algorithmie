def new_multiply_value(dictionnaire, value):
    """Multiplie toutes les valeurs d'un dictionnaire.
    Renvoie un nouveau dictionnaire"""

    nouveau_dictionnaire = dictionnaire.copy()
    for key in nouveau_dictionnaire.keys():
        nouveau_dictionnaire[key] = nouveau_dictionnaire[key] * value

    return nouveau_dictionnaire



def multiply_value(dictionnaire, value):
    """Multiplie toutes les valeurs d'un dictionnaire.
    Change le dictionnaire envoyé en paramètre"""

    for key in dictionnaire.keys():
        dictionnaire[key] = dictionnaire[key] * value

    return dictionnaire
