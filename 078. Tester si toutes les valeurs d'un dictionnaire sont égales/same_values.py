def same_values(dictionnaire):
    """Renvoie True si toutes les valeurs d'un dictionnaire sont pareils. False sinon."""

    value_to_check = None

    for key, value in dictionnaire.items():
        #Si on a pas encore rencontré de valeur, on en affecte une à value_to_check
        if value_to_check == None:
            value_to_check = value

        #On compare les valeurs avec value_to_check
        if value != value_to_check:
            return False
        
    return True



def same_values_set(dictionnaire):
    """Renvoie True si toutes les valeurs d'un dictionnaire sont pareils. False sinon."""
    if len(set(dictionnaire.values())) == 1:
        return True
    else:
        return False
