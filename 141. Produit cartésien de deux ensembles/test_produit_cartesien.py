from produit_cartesien import *

#On créé nos vecteurs de tests
v1 = [1,2,3,4]
v2 = ["a", "b", "c"]
v3 = ["y", "z"]

#On teste la méthode produit_cartesien()
print(produit_cartesien(v1, v2))
print(cartesien_itertools(v1,v2))
print(produit_cartesien_short(v1,v2))
print("------------------")

print(produit_cartesien(v1, v3))
print(cartesien_itertools(v1,v3))
print(produit_cartesien_short(v1,v2))
print("------------------")

print(produit_cartesien(v2, v3))
print(cartesien_itertools(v2,v3))
print(produit_cartesien_short(v1,v2))
print("------------------")