from math import *

#Détermine les valeurs approchées de racine de n, pour l'entier naturel n
#u1 = n
#u2 = 0.5*(u1 + n/u1)
#u3 = 0.5*(u2 + n/u2)

def heron(n,p):
    u = n
    while(u - sqrt(n) > p):
        u = 0.5*(u + n/u)

    return u
