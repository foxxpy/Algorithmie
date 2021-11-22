def somme_complexe(z1, z2):
    z_reel = z1[0] + z2[0]
    z_img = z1[1] + z2[1]

    return (z_reel, z_img)


def print_complexe(z):
    """Affiche le nombre complexe z"""
    
    print("{} + {}i".format(z[0], z[1]))

