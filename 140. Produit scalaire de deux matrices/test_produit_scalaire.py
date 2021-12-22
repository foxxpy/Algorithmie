from produit_scalaire import *
import numpy as np

#On créé nos matrices
a1 = [[1,2,3], [-1,-2,-3]]
a2 = [[1,2], [3,4], [5,6]]

b1 = [[1,2,3,4,5]]
b2 = [[5], [4], [3], [2], [1]]

c1 = [[1,2,3,4]]
c2 = [[1,2], [3,4], [5,6]]

#On calcule le résultat du produit scalaire des matrices précédentes
print(produit_scalaire(a1,a2))
print(np.dot(np.array(a1), np.array(a2)))
print("----------------")

print(produit_scalaire(b1,b2))
print(np.dot(np.array(b1), np.array(b2)))
print("----------------")

print(produit_scalaire(c1,c2)) #Doit renvoyer None car les dimensions des matrices ne permettent pas le produit scalaire