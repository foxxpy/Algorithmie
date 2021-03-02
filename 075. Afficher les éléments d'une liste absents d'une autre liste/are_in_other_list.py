def are_in_other_list(liste1, liste2):
    """Renvoie une liste des éléments de la première liste qui ne sont pas
    présents dans la seconde liste"""

    element_not_in_other_list = list()
    for element in liste1:
        if not element in liste2:
            element_not_in_other_list.append(element)

    return element_not_in_other_list
