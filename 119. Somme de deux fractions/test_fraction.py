from fraction import somme_fraction

a,b,c,d = 1,2,1,3
num, den = somme_fraction(a,b,c,d)
print("{}/{} + {}/{} = {}/{}".format(a,b,c,d,num, den))
print()

a,b,c,d = 1,2,1,4
num, den = somme_fraction(a,b,c,d)
print("{}/{} + {}/{} = {}/{}".format(a,b,c,d,num, den))
print()

a,b,c,d = 1,3,1,4
num, den = somme_fraction(a,b,c,d)
print("{}/{} + {}/{} = {}/{}".format(a,b,c,d,num, den))
print()

a,b,c,d = 1,5,1,10
num, den = somme_fraction(a,b,c,d)
print("{}/{} + {}/{} = {}/{}".format(a,b,c,d,num, den))
print()
