from complexe_2 import produit_complexe

#Instanciation des nombres complexes
z1 = (1,1)
z2 = (3,2)

z3 = (5,0)
z4 = (2,2)

z5 = (1,-2)
z6 = (3, -1)

#Test des méthodes multipliant les nombres complexes
print(produit_complexe(z1,z2))
print((1+1j)*(3+2j))
print(produit_complexe(z3,z4))
print((5+0j)*(2+2j))
print(produit_complexe(z5,z6))
print((1-2j)*(3-1j))