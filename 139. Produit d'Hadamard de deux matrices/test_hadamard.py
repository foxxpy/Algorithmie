from hadamard import *
import numpy as np

#On créé nos matrices de test
a1 = [[1,2],[3,4]]
a2 = [[-1, -1], [-1, -1]]

b1 = [[0,1,2], [-1,-2,-3], [5, 10, 15], [100, 200, 300]]
b2 = [[1,2,3], [5,10,15], [1,1,1], [0,-5, 0]]

#On calcule le produit hadamard des matrices
print(produit_hadamard(a1, a2))
print(produit_hadamard_2(a1, a2))
print(np.multiply(np.array(a1), np.array(a2)))
print("-------------")

print(produit_hadamard(b1, b2))
print(produit_hadamard_2(b1, b2))
print(np.multiply(np.array(b1), np.array(b2)))
