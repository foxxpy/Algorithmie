def print_sort_dict(dictionnaire):
    """Affiche les éléments d'un dictionnaire triés par leur clé"""
    for key in sorted(dictionnaire):
        print("{} : {}".format(key, dictionnaire[key]))

        
