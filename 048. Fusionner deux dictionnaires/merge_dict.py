def merge_dict(dict1, dict2):
    """Fusionne deux dictionnaires"""
    
    final_dict = dict1.copy()
    final_dict.update(dict2)
    return final_dict



def merge_dict_for(dict1, dict2):
    """Fusionne deux dictionnaires grâce à une boucle for"""

    final_dict = dict()
    for dictionnaire in [dict1,dict2]:
        for key, value in dictionnaire.items():
            final_dict[key] = value

    return final_dict
