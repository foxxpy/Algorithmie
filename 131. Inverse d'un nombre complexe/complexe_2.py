def inverse_complexe(z):
    """Calcule l'inverse du nombre complexe z:
    :type z: tuple
    :rtype: tuple
    """
    
    denominateur = z[0]**2 + z[1]**2
    reel = z[0] / denominateur
    im = -z[1] / denominateur
    return (reel, im)

def print_complexe(z):
    """Affiche le nombre complexe z.
    :type z: tuple
    """
    
    print("{} + {}i".format(z[0], z[1]))
