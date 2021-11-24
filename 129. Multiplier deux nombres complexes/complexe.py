class Complexe:

    def __init__(self, real, imaginary):
        """Initialise les attributs représentant les nombres réels et imaginaires.
        :type self: Complexe
        :type real: float
        :type imaginary: float"""

        self.re = real
        self.im = imaginary


    def __str__(self):
        """Renvoie ce nombre Complexe sous forme de chaîne de caractères.
        :type self: Complexe
        :rtype: str"""

        if self.im < 0:
            return "{} - {}i".format(self.re, abs(self.im))

        elif self.im > 0:
            return "{} + {}i".format(self.re, self.im)

        else:
            return "{}".format(self.re)


    def __mul__(self, other):
        """Multiplie ce nombre complexe avec un autre nombre complexe.
        :type self: Complexe
        :type other: Complexe
        :rtype: Complexe
        """

        new_real = self.re * other.re - self.im * other.im
        new_im = self.im * other.re + self.re * other.im
        return Complexe(new_real, new_im)
        

    def __add__(self, other):
        """Additionner ce nombre complexe avec un autre nombre complexe.
        :type self: Complexe
        :type other: Complexe
        :rtype: Complexe"""
        
        return Complexe(self.re+other.re, self.im + other.im)

    
