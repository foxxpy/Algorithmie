def produit_complexe(z1, z2):
    """Multiplie le nombre complexe z1 avec le nombre complexe z2.
    :type z1: tuple
    :type z2: tuple
    :rtype: tuple
    """

    z_reel = z1[0] * z2[0] - z1[1] * z2[1]
    z_im = z1[0] * z2[1] + z1[1] * z2[0]
    return (z_reel, z_im)



def print_complexe(z):
    """Affiche le nombre complexe z.
    :type z: tuple
    """

    print("{} + {}i".format(z[0], z[1]))