def inverser_entier(nombre):

    #Si le nombre est négatif, on ajoute un "-" au début de y
    if nombre < 0:
        return int("-"+str(nombre)[1:][::-1])
    else:
        return int(str(nombre)[::-1])
