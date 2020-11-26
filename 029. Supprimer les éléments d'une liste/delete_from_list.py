def delete(liste, element_to_delete):
    """Supprime un élément d'une liste"""
    new_list = list()
    
    for element in liste:
        if not element == element_to_delete:
            new_list.append(element)

    return new_list

def delete_liste(liste, elements_to_delete):
    """Supprime plusieurs éléments d'une liste"""
    new_list = list()
    
    for element in liste:
        if not element in elements_to_delete:
            new_list.append(element)

    return new_list
