class Complexe:

    def __init__(self, real, imaginary):
        self.re = real
        self.im = imaginary


    def __str__(self):
        """Renvoie le nombre complexe sous forme de chaîne de caractères."""

        if self.im < 0:
            return "{} - {}i".format(self.re, abs(self.im))

        elif self.im > 0:
            return "{} + {}i".format(self.re, self.im)

        else:
            return "{}".format(self.re)
        

    def inverse(self):
        """Calcule l'inverse de ce nombre complexe"""

        denominateur = self.re**2 + self.im**2
        self.re = self.re / denominateur
        self.im = -self.im / denominateur
        return self