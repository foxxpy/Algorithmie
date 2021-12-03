class Complexe:

    def __init__(self, real, imaginary):
        self.re = real
        self.im = imaginary


    def __str__(self):
        """Renvoie ce nombre complexe sous forme de chaîne de caractères."""
        if self.im < 0:
            return "{} - {}i".format(self.re, abs(self.im))

        elif self.im > 0:
            return "{} + {}i".format(self.re, self.im)

        else:
            return "{}".format(self.re)
        

    def module(self):
        """Renvoie le module de ce nombre complexe"""

        sum_square = self.re**2 + self.im**2
        return sum_square**(1/2)