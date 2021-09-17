def fill(nombre, nb_de_zeros):
    """Ajoute des zéros au début d'un nombre entier"""

    if nb_de_zeros < 0:
        print("Le nombre de zéros ne peut être négatif")
        return None

    return "0"*nb_de_zeros+str(nombre)



def fill_length(nombre, length):
    """Ajoute des zéros jusqu'à ce que le nombre entier soit composé de length caractères"""

    if length <= 0:
        return None

    if len(str(nombre)) >= length:
        return str(nombre)

    else:
        return "0"*(length - len(str(nombre)))+str(nombre)


def z_fill(nombre, z):
    """Ajoute des zéros jusqu'à ce que le nombre entier soit composé de z caractères"""

    return str(nombre).zfill(z)
