def somme_fraction(numerateur1, denominateur1, numerateur2, denominateur2):

    #Si elles ont le même dénominateur
    if denominateur1 == denominateur2:
        return numerateur1+numerateur2, denominateur1

    else:
        denominateur = denominateur1*denominateur2
        numerateur1 = numerateur1 * denominateur2
        numerateur2 = numerateur2 * denominateur1

        return numerateur1+numerateur2, denominateur
