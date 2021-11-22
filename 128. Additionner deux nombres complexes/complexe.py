
class Complexe:

    def __init__(self, real, imaginary):
        self.re = real
        self.im = imaginary


    def __str__(self):
        if self.im < 0:
            return "{} - {}i".format(self.re, abs(self.im))

        elif self.im > 0:
            return "{} + {}i".format(self.re, self.im)

        else:
            return "{}".format(self.re)
        

    def __add__(self, other):
        return Complexe(self.re+other.re, self.im + other.im)

    
