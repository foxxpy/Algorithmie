
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
        

    def negation(self):
        self.re = -1 * self.re
        self.im = -1 * self.im
        return self