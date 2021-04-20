def both_list(liste1, liste2):
    """Renvoie les éléments présents à la fois dans liste1 et liste2"""

    liste1 = sorted(set(liste1))
    liste2 = sorted(set(liste2))
    final_list = []
    
    for element in liste1:
        if element in liste2 and not element in final_list:
            final_list.append(element)

    for element in liste2:
        if element in liste1 and not element in final_list:
            final_list.append(element)

    return final_list

    
