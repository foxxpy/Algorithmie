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
        

    def conjugue(self):
        """Calcule le conjugué de ce nombre complexe"""

        self.im = -self.im
        return self