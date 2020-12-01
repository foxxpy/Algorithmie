#Recoder la méthode index() d'une liste
def find_index(liste, to_find):
    for i, element in enumerate(liste):
        if element == to_find:
            return i
    return -1
